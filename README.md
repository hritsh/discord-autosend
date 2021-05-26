# discord-autosend
A Python program that uses selenium to autosend/spam messages on Discord.

## Prerequisites
These libraries are needed for the script to run and can be installed using pip:
```
pip install selenium
pip install webdriver-manager
pip install progress
```
## Running the script
Steps:
1. Download both discord_spam.py and login.py
2. Run discord_spam.py
3. Enter your discord email id and password (Only required for first run)
4. Enter the discord channel link you want to spam
5. Enter the message you want to send and number of messages
6. An automated chrome window will open, log in and send the messages indicated by a progress bar
7. After the messages are sent, a prompt will be shown asking if you want to send more messages
8. Type y if you want to continue or n if you want to quit and hit enter

Your email and password is stored locally in logindetails.dat
You can modify login details by running login.py

Note: The message sending rate is capped at 1 message per second as discord gives a warning otherwise.
