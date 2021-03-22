#a multiuses tool phishing tool,facebook information gathering etc.
import pyfiglet 
import sys
import os
import requests

def fcBin():
    os.system("clear")
    print(pyfiglet.figlet_format("NOEL", font = "slant"))
    print("++++++++++++++++++++++++++++++")
    resp = input  ("1.friend of firend\n"+ "2.information gathering\n" + "3.facebook info\n")
    print("++++++++++++++++++++++++++++++")
    if(resp =="1"):
        print(pyfiglet.figlet_format("NOEL", font = "slant"))
        print("+++++++++++++++++++++++++++++")
        print("login to get your friends)
        resp1 input = ("username:")
        resp2 input = ("password:")
        rr = requests.get("https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&resp1=123&client_secret=resp2 ")
        sys.exit()
        print("++++++++++++++++++++++++++++++")
    elif(resp == "2"):
        print ("no script yet <(")
        sys.exit()
    elif(resp ==  "3"):
        fcBin()
    else:
        print("this is not a option")
def info():
    os.system("clear")
    print(pyfiglet.figlet_format("NOEL", font = "slant"))
    print ("+++++++++++++++++++++++")
    resp = input  ("1.account hunter\n"+ "2.information gathering\n" + "3.facebook info\n")
    print ("++++++++++++++++++++++++++++")

    if(resp =="1"):
        print ("no script yet <(")
        sys.exit()
    elif(resp == "2"):
        print ("no script yet <(")
        sys.exit()
    elif(resp ==  "3"):
        fcBin()
    else:
        print("this is not a option")
info()