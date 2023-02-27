# message_handler.py
import re
from app.message_handler.bot_commands import bot_commands
from app.message_handler.command_error_handler import command_error_handler
from app.message_handler.permission_denied_handler import permission_denied
from app.conf.authority.authority import Authority


def message_handler(message: str, gid=None, qid=None):
    def check_command(message, command_list):
        pattern = r'(#\w+)\s*(.*)'
        match = re.match(pattern, message.strip())
        if match:
            command = match.group(1)
            if command in command_list:
                param_list = match.group(2).strip().split()
                return command, param_list
            else:
                return 'error', 'invalid command'
        else:
            return None, None
    key_word_list = list(bot_commands.keys())
    key_word, param_list = check_command(message, key_word_list)
    if key_word:
        if 'error' == key_word:
            command_error_handler(gid, qid)
        else:

            if Authority.check_command_permission(key_word, gid, qid):
                bot_commands[key_word](gid, qid, param_list)
            else:
                permission_denied(gid, qid)
