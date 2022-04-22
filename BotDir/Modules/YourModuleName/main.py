import telebot
from every_bot.types import *


class YourModuleName(BotModule):
    name = 'YourModuleName'
    helpStr = "This string will be printed when user type '@YourModuleName /help'"
    bot: telebot.TeleBot = None

    commands: list[Command] = []
    """Do not delete this, it fixes a bug"""

    userNamesDict: dict[str: str] = {}

    # If your command doesn't uses any arguments you need to leave 'agrs: list[str]' anyway
    def hello_handler(self, message: telebot.types.Message, args: list[str]):
        """Every command needs a handler..."""
        self.core.send_message(message, self, f"Hello, {self.userNamesDict.setdefault(message.from_user.username, message.from_user.username)}!")

    def hello_help_handler(self, message: telebot.types.Message, docStr: str):
        """And a help_handler"""
        self.core.send_message(message, self, docStr + "\nIt will say hello to you :3")

    def callme_handler(self, message: telebot.types.Message, args: list[str]):
        self.core.send_message(message, self, f"Ok, I'll be calling you '{args[0]}'")
        self.userNamesDict[message.from_user.username] = args[0]

    def callme_help_handler(self, message: telebot.types.Message, docStr: str):
        self.core.send_message(message, self, docStr + "\nI can call you how you want :3")

    def __init__(self, core: Core):
        super().__init__(core)

        self.bot = self.core.bot

        """Initialize your commands here like this:"""
        self.add_new_command("/hello", [], self.hello_handler, self.hello_help_handler)
        self.add_new_command("/callme", [str], self.callme_handler, self.callme_help_handler)

    def handle_message(self, message: telebot.types.Message):
        splitMessage = message.text.split(' ')

        for command in self.commands:
            if command.name == splitMessage[0]:
                command.handle(message, message.text)


def get_module(core):
    return YourModuleName(core)
