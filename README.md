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
The script opens chrome in an automation window after you enter your login details and link to the channel.
You then need to enter the message you want to send and how many times you want it to in the command line.
It shows a progress bar along with the number of messages sent and asks if you want to continue.

Note: The message sending rate is capped at 1 message per second as discord gives a warning otherwise.
