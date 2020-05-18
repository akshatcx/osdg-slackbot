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
    print("COMMAND:" + sent_message)

@respond_to('^hi$', re.IGNORECASE)
@respond_to('^help$', re.IGNORECASE)
@respond_to('^help (.*)$', re.IGNORECASE)
def help(message, command=None):
"""
 _______  _______  ______   _______ 
(  ___  )(  ____ \(  __  \ (  ____ \
| (   ) || (    \/| (  \  )| (    \/
| |   | || (_____ | |   ) || |      
| |   | |(_____  )| |   | || | ____ 
| |   | |      ) || |   ) || | \_  )
| (___) |/\____) || (__/  )| (___) |
(_______)\_______)(______/ (_______)

*Beep-boop-beep* I am the OSDG bot and I am here to help you!
"""

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
#    message.reply('```ERROR: Unknown Usage!\n' + help.__doc__ + '```')

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()