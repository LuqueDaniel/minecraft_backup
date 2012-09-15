
# Minecraft Backup Imports
from vars_config import config_folder
from vars_config import template_config_json
from vars_config import save_backup_folder

# Imports platform
from platform import system
# Imports os
from os import path
from os import mkdir
from os import chdir
# Imports json
from json import dumps
from json import loads


def get_OS():
    os_info = system()

    if os_info == 'Linux':
        return 'Linux'
    elif os_info == 'Windows':
        return 'Windows'
    elif os_info == 'Darwin':
        return 'MacOS'


def save_config():
    config_file = open('config.json', 'w')
    config_file.write(dumps(template_config_json, indent=4))
    config_file.close()


def load_config(os):
    if path.exists('config.json') is True:
        config_file = open('config.json', 'r')
        read_config_file = loads(config_file.read())
        config_file.close()

        save_backup_folder = read_config_file['save_backup_folder']
    else:
        save_config()


def config(os):
    if path.exists(config_folder[os]) is True:
        chdir(config_folder[os])
        load_config(os)
    else:
        mkdir(config_folder[os], 0777)
        chdir(config_folder[os])
        load_config(os)

config(get_OS())
