# -*- coding: utf-8 *-*
#
# This file is part of Minecraft Backup Manager
#
# Minecraft Backup Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# Minecraft Backup Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Minecraft Backup Manager. If not, see <http://www.gnu.org/licenses/>.
#
# Source: https://github.com/LuqueDaniel/Minecraft_backup.git

"""
    This module contain all functions and class for manage backup
"""

# Minecraft Backup Manager
from minecraft_backup.resources import GAME_PATH

# PyQt4.QtCore
from PyQt4.QtCore import QThread
from PyQt4.QtCore import SIGNAL

# OS
from os import listdir
from os import mkdir
from os import path
from os import remove

# sys
import sys

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

        #Encode in windows-1252 for create folders in Windows
        if sys.platform == 'win32':
            self.dst = dst_.decode('utf-8').encode('windows-1252')
        else:
            self.dst = dst_

        self.backup_list = load_backup_list()

        if self.backup_list is not False:
            if unicode(backup_name, 'utf-8') not in self.backup_list:
                self.check_exist_directory(backup_name)
            else:
                self.emit(SIGNAL('nameexists()'))
                self.exit()
        else:
            self.check_exist_directory(backup_name)

    def check_exist_directory(self, backup_name):
        """This function checks if exists directory"""

        if path.exists(self.dst):
            self.emit(SIGNAL('direxists()'))
            self.exit()
        else:
            self.make_backup(self.dst, backup_name)
            self.exit()

    def make_backup(self, dst, backup_name):
        """This function make a Minecraft backup"""

        mkdir(dst)

        try:
            self.make_backup_continue = True
            copy_backup_files(GAME_PATH, dst)
        except IOError:
            self.make_backup_continue = False
            self.emit(SIGNAL('IOdenied()'))
            rmtree(dst)

        if self.make_backup_continue is True:
            self.save_backup_list(backup_name, dst)
            self.emit(SIGNAL('makeend()'))

    def save_backup_list(self, backup_name, path):
        """This function create and save backup list"""

        #Decode for save in utf-8
        if sys.platform == 'win32':
            self.path = path.decode('windows-1252').encode('utf-8')
        else:
            self.path = path

        self.backup_list = load_backup_list()

        if self.backup_list is not False:
            self.backup_list[backup_name] = {'name': backup_name,
                                             'path': self.path}

            save_backup_file(self.backup_list)
        else:
            self.first_backup_list = {}
            self.first_backup_list[backup_name] = {'name': backup_name,
                                                   'path': self.path}

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

    backup_list = load_backup_list()

    rmtree(backup_list[backup_name]['path'])
    remove_backup_name(backup_name)


def restore_backup(backup_name):
    """This function restore backup"""

    backup_list = load_backup_list()
    src = backup_list[backup_name]['path']

    if path.exists(GAME_PATH):
        copy_backup_files(src, GAME_PATH)
    else:
        mkdir(GAME_PATH)
        copy_backup_files(src, GAME_PATH)
