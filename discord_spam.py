from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from progress.bar import ChargingBar
from time import sleep
from os import system, name as osname

## Opening link and logging in
def login(link,email,passwd):
    ## Initialising/Installing Chromedriver
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    system('cls' if osname == 'nt' else 'clear')
    print("\nLogging in...")
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('password').send_keys(passwd)
    driver.find_element_by_name('password').send_keys(Keys.RETURN)
    sleep(5)
    print("\nLogged in successfully")
    sleep(1)
    system('cls' if osname == 'nt' else 'clear')

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

## Menu
def main():
    while True:
        system('cls' if osname == 'nt' else 'clear')
        print("-"*100+"\n"+" "*36+"DISCORD SPAM / AUTO SEND"+"\n"+"-"*100+"\n")
        email = input("Enter discord e-mail address: ")
        passwd = input("Enter password: ")
        link = input("Enter link to channel: ")
        login(link,email,passwd)
        message = input("\nEnter message to send: ")
        n = int(input("Enter number of messages: "))
        print()
        spam(n,message)
        choice = input("\nDo you want to continue (y/n): ")
        if (choice == "n"):
            break

main()