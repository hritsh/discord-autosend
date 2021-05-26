from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from progress.bar import ChargingBar
from time import sleep
from os import system, name as osname
from pickle import load
from login import store

def retrieve():
    try:
        frobj = open("logindetails.dat","rb")
        details = load(frobj)
        frobj.close()
        return details
    except:
        frobj.close()
        return None

def clearscreen():
    system('cls' if osname == 'nt' else 'clear')
    print("-"*100+"\n"+" "*36+"DISCORD SPAM / AUTO SEND"+"\n"+"-"*100+"\n")

## Opening link and logging in
def login(link,email,passwd):
    ## Initialising/Installing Chromedriver
    global driver, flag
    if (flag == False):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        flag = True
    driver.get(link)
    clearscreen()
    print("\nLogging in...")
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('password').send_keys(passwd)
    driver.find_element_by_name('password').send_keys(Keys.RETURN)
    sleep(5)
    print("\nLogged in successfully")
    sleep(1)
    clearscreen()

## Starting spam
def spam(n,message):
    with ChargingBar('Sending Messages', max=n) as bar:
        bar.suffix = '%(percent).1f%% [ %(index)d / %(max)d ]'
        for i in range(n):
            actions = ActionChains(driver)
            actions.send_keys(message)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            bar.next()
            sleep(1)
    print("\nAll Messages Sent")

## Menu
def main():
    global flag
    flag = False
    details = retrieve()
    if (details != None):
        email,passwd = details
    else:
        store()
        main()

    while True:
        clearscreen()
        link = input("Enter link to channel: ")
        message = input("\nEnter message to send: ")
        n = int(input("Enter number of messages: "))
        print()
        login(link,email,passwd)
        spam(n,message)
        choice = input("\nDo you want to send more messages (y/n): ")
        if (choice == "n"):
            break

if __name__ == '__main__':
    main()