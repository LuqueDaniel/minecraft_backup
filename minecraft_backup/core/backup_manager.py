# -*- coding: utf-8 *-*
# This file is part of Minecraft Backup Manager

"""
    This module contain all functions and class for manage backup
"""

# Minecraft Backup Manager
from minecraft_backup.resources import GAME_PATH
from minecraft_backup.core.configuration import get_os

# PyQt4.QtCore
from PyQt4.QtCore import QThread
from PyQt4.QtCore import SIGNAL

# OS
from os import listdir
from os import mkdir
from os import path
from os import remove

# Shutil
from shutil import copytree
from shutil import copy2
from shutil import copystat
from shutil import rmtree

# Json
from json import dumps
from json import loads


class make_backup_thread(QThread):
    """This class create a Minecraft backup. Inherit of QThread"""

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def run(self, dst_, backup_name):
        """Start QThread"""

        # Decode and encode dst for Windows
        if get_os() == 'Windows':
            self.dst = dst_.decode('utf-8').encode('windows-1252')
        else:
            self.dst = dst_

        if path.exists(self.dst):
            self.emit(SIGNAL('direxists()'))
            self.exit()
        else:
            self.make_backup(self.dst, backup_name)

            self.exit()

    def make_backup(self, dst, backup_name):
        """This function make a Minecraft backup"""

        os = get_os()
        mkdir(dst)

        copy_backup_files(GAME_PATH[os], dst)

        self.save_backup_list(backup_name, dst)
        self.emit(SIGNAL('makeend()'))

    def save_backup_list(self, backup_name, path):
        """This function save backup list"""

        # Decode in Windows and encode UTF-8 for save in Json
        if get_os() == 'Windows':
            self.path = path.decode('windows-1252').encode('utf-8')
        else:
            self.path = path.decode('ascii').encode('utf-8')

        self.backup_list = load_backup_list()

        if self.backup_list is not False:
            self.backup_list[backup_name] = self.path
            save_backup_file(self.backup_list)

        else:
            self.first_backup_list = {}
            self.first_backup_list[backup_name] = self.path
            save_backup_file(self.first_backup_list)


def copy_backup_files(src, dst):
    """Function for copy and remove files"""

    names = listdir(src)

    for name in names:
        src_name = path.join(src, name)
        dst_name = path.join(dst, name)

        if path.isdir(src_name):
            if path.exists(dst_name):
                rmtree(dst_name)
            copytree(src_name, dst_name)
        else:
            if path.exists(dst_name):
                remove(dst_name)
            copy2(src_name, dst_name)

        copystat(src, dst)


def save_backup_file(backup_list):
    """Create template and save template in blist.json"""

    save_backup_list_file = open('blist.json', 'w')
    save_template_list_backup = dumps(backup_list, indent=4, encoding='utf-8')

    save_backup_list_file.write(save_template_list_backup)
    save_backup_list_file.close()


def load_backup_list():
    """check and load blist.json"""

    if path.exists('blist.json'):
        list_backup_file = open('blist.json', 'r')
        load_backup_file = loads(list_backup_file.read(), encoding='utf-8')
        list_backup_file.close()

        return load_backup_file
    else:
        return False


def remove_backup_name(backup_name):
    """Remove data of backup and save blis.json"""

    backup_list = load_backup_list()
    backup_list.pop(backup_name)
    save_backup_file(backup_list)


def remove_backup(backup_name):
    """Remove data and backup files"""

    backup = backup_name
    if backup == 'ñ':
        print backup
    else:
        print 'Nop'

    backup_list = load_backup_list()
    print backup_list
    rmtree(backup_list[backup])

    remove_backup_name(backup)


def restore_backup(os, backup_name):
    """This function restore backup"""

    backup = str(backup_name)

    backup_list = load_backup_list()
    dst = os
    src = backup_list[backup]

    if path.exists(os):
        copy_backup_files(src, dst)
    else:
        mkdir(os)
        copy_backup_files(src, dst)
