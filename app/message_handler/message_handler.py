# message_handler.py
import re
from app.message_handler.bot_commands import BotCommands
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
    commands = list(BotCommands.get_commands())
    command, param_list = check_command(message, commands)
    if command:
        if 'error' == command:
            command_error_handler(gid, qid)
        else:
            server_name = BotCommands.get_server_name(command)
            print(server_name)
            # if Authority.check_command_permission(command, gid, qid):
            #     bot_commands[command](gid, qid, param_list)
            # else:
            #     permission_denied(gid, qid)
