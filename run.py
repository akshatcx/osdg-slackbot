#!/usr/bin/python
# coding=utf8
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import os
import re
import json
import sys
import slackbot_settings
import requests


@respond_to('(.*)$')
def audit_log(message, sent_message):
    print(f"COMMAND '{sent_message}' FROM '{message.user['name']}'")

@respond_to('^hi$', re.IGNORECASE)
@respond_to('^help$', re.IGNORECASE)
@respond_to('^help (.*)$', re.IGNORECASE)
def help(message, command=None):
    art = """
   ____   _____ _____   _____ 
  / __ \ / ____|  __ \ / ____|
 | |  | | (___ | |  | | |  __ 
 | |  | |\___ \| |  | | | |_ |
 | |__| |____) | |__| | |__| |
  \____/|_____/|_____/ \_____|
"""                              

    reply = "*Beep-boop-beep* I am the OSDG bot and I am here to help you!"

#Command Usage: help [command]
#    """
#    if command is None:
#        message.reply('```' + help.__doc__ + '\nAvailable commands are: ' + ', '.join([c.__name__ for c in bot_commands]) + '```')
#        return
#    else:
#        for c in bot_commands:
#            if c.__name__ == command:
#              message.reply('```' + c.__doc__ + '```')
#              return
    message.reply(f'```{art}```{reply}')

@respond_to('Are we on a roll?', re.IGNORECASE)
def on_roll(message):
    on_roll_img = "media/on_roll.png"
    message.channel.upload_file(f"We are on a roll!!", on_roll_img)

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
