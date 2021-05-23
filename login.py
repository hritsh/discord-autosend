from pickle import dump
from time import sleep

def store():
    email = input("\nEnter discord e-mail address: ")
    passwd = input("Enter password: ")
    fwobj = open("logindetails.dat","wb")
    dump((email,passwd),fwobj)
    fwobj.close()
    print("\nLogin stored successfully")
    sleep(1)

if __name__ == '__main__':
  store()