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
        print ("no script yet <(")
        sys.exit()
    elif(resp == "2"):
        print ("no script yet <(")
        sys.exit()



def info():
    os.system("clear")
    print(pyfiglet.figlet_format("NOEL", font = "slant"))
    print ("+++++++++++++++++++++++")
    resp = input  ("1.phishing\n"+ "2.information gathering\n" + "3.facebook info\n")
    print ("++++++++++++++++++++++++++++")

    if(resp =="1"):
        print ("no script yet <(")
        sys.exit()
    elif(resp == "2"):
        print ("no script yet <(")
        sys.exit()
    else:
        fcBin()
info()