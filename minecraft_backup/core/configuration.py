#*-* coding: utf-8 *-*
# This file is part of Minecraft Backup Manager
# Source: https://github.com/LuqueDaniel/Minecraft_backup.git

"""
    The module contain functions for configurations
"""

# Minecraft Backup Manager
from minecraft_backup.resources import D_TEMPLATE_CONFIG_JSON
from minecraft_backup.resources import CONFIG_FOLDER

# os
from os import path
from os import mkdir
from os import chdir

# json
from json import dumps
from json import loads


def load_config(option):
    """Load configuration"""

    load_file = open('config.json', 'r')
    read_file = loads(load_file.read())
    load_file.close()

    for op in read_file.items():
        if op[0] == option:
            return op[1]
        else:
            continue


def d_save_config():
    """Save default configurations in .json file"""

    save_config_file = open('config.json', 'w')
    save_config_file.write(dumps(D_TEMPLATE_CONFIG_JSON, indent=4))
    save_config_file.close()


def save_new_config(save_backup_folder):
    """Saves new configurations in .json file"""

    save_config_file = open('config.json', 'w')

    save_template = dumps({
                          'save_backup_folder': save_backup_folder
                          }, indent=4)

    save_config_file.write(save_template)
    save_config_file.close()


def check_config_file():
    """Check exists configuration file"""

    if path.exists('config.json') is False:
        d_save_config()


def config():
    """Checking if exists config folder and app directory"""

    if path.exists(CONFIG_FOLDER) is True:
        chdir(CONFIG_FOLDER)
        check_config_file()
    else:
        mkdir(CONFIG_FOLDER, 0777)
        chdir(CONFIG_FOLDER)
        check_config_file()
