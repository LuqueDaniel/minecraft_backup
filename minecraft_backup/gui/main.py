# -*- coding: utf-8 *-*
#
# This file is part of Minecraft backup Manager
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


# Minecraft Backup Manager
from minecraft_backup.resources import IMAGES
from minecraft_backup.core import configuration
from minecraft_backup.core.backup_manager import load_backup_list
from minecraft_backup.core.backup_manager import remove_backup_name
from minecraft_backup.core.backup_manager import remove_backup
from minecraft_backup.core.backup_manager import restore_backup
from minecraft_backup.gui.center_widget import center_widget
from minecraft_backup.gui.msg_box import msg_about_qt
from minecraft_backup.gui.msg_box import msg_backup_folder_not_exists
from minecraft_backup.gui.msg_box import msg_remove_backup
from minecraft_backup.gui.msg_box import msg_restore_backup
from minecraft_backup.gui.msg_box import msg_restore_finishied
from minecraft_backup.gui.dialogs import config_window
from minecraft_backup.gui.dialogs import about_minebackup
from minecraft_backup.gui.dialogs import new_backup_window

# PyQt4.QtGui
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QListWidgetItem
from PyQt4.QtGui import QPushButton

# PyQt4.QtCore
from PyQt4.QtCore import QCoreApplication
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QRect

# os
from os import path

# sys
import sys


class main_window(QMainWindow):

    def __init__(self):
        super(main_window, self).__init__()

        self.setWindowTitle('Minecraft Backup Manager')
        self.setGeometry(0, 0, 700, 520)
        self.setMinimumSize(700, 520)
        self.setMaximumSize(700, 520)
        center_widget(self)

        self.header()

        # btn_config
        self.btn_config = QPushButton(QIcon(IMAGES['config_icon']), '', self)
        if sys.platform == 'win32':
            self.btn_config.setGeometry(QRect(7, 27, 32, 32))
        else:
            self.btn_config.setGeometry(QRect(7, 7, 32, 32))
        self.btn_config.setToolTip('Configuration')

        # menu bar
        self.menu_bar = self.menuBar()

        self.menu_help = self.menu_bar.addMenu('About')
        self.menu_help.addAction('About Minecraft Backup Manager',
                            lambda: self.open_about_minebackup())
        self.menu_help.addAction('About Qt', lambda: msg_about_qt(self))

        # list_backup
        self.list_backup = QListWidget(self)
        self.list_backup.setGeometry(QRect(20, 190, 450, 310))

        # btn_new_backup
        self.btn_new_backup = QPushButton('New backup', self)
        self.btn_new_backup.setGeometry(QRect(485, 190, 200, 30))

        # btn_restore_backup
        self.btn_restore_backup = QPushButton('Restore backup', self)
        self.btn_restore_backup.setGeometry(QRect(485, 260, 200, 30))
        self.btn_restore_backup.setEnabled(False)

        # btn_remove_backup
        self.btn_remove_backup = QPushButton('Remove Backup', self)
        self.btn_remove_backup.setGeometry(QRect(485, 300, 200, 30))
        self.btn_remove_backup.setEnabled(False)

        # CONNECT SIGNALS
        self.connect(self.btn_config, SIGNAL('clicked()'), self.open_config)
        self.connect(self.btn_new_backup, SIGNAL('clicked()'),
                     self.open_new_backup)
        self.connect(self.btn_remove_backup, SIGNAL('clicked()'),
                     self.remove_backup)
        self.connect(self.btn_restore_backup, SIGNAL('clicked()'),
                     self.restore_backup)
        self.connect(self.list_backup,
                     SIGNAL('itemClicked(QListWidgetItem *)'),
                     self.enabled_buttons)

        self.load_backup_list()

    def load_backup_list(self):
        self.list_backup.clear()
        self.backup_list = load_backup_list()

        self.name_list = []

        if self.backup_list is not False:
            for backup in self.backup_list.values():
                if path.exists(backup['path']):
                    self.list_item = QListWidgetItem(backup['name'])
                    self.list_item.setToolTip('<b>Directory:</b> %s' %
                                    backup['path'])

                    self.name_list.append(backup['name'])

                    self.list_backup.addItem(self.list_item)
                else:
                    msg_backup_folder_not_exists(self, backup['name'])
                    remove_backup_name(backup['name'])

    def header(self):
        self.header_label = QLabel(self)
        self.header_label.resize(700, 170)
        self.header_label.setPixmap(QPixmap(IMAGES['header']))

    def enabled_buttons(self):
        self.btn_remove_backup.setEnabled(True)
        self.btn_restore_backup.setEnabled(True)

    def open_config(self):
        self.configuration_window = config_window.config_window(self)
        self.configuration_window.show()

    def open_about_minebackup(self):
        self.about_minebackup = about_minebackup.about_minebackup(self)
        self.about_minebackup.show()

    def open_new_backup(self):
        self.new_backup_window = new_backup_window.new_backup_window(self)
        self.new_backup_window.show()

        # CONNECT SIGNALS
        self.connect(self.new_backup_window, SIGNAL('close()'),
                     self.load_backup_list)

    def backup_item_selector(self, item):
        for name in self.name_list:
            if item.text() == name:
                return self.name_list[self.name_list.index(name)]
            else:
                continue

    def remove_backup(self):
        self.remove_question = msg_remove_backup(self)

        if self.remove_question is not False:
            self.backup_item = self.list_backup.currentItem()
            self.backup_name = self.backup_item_selector(self.backup_item)

            remove_backup(self.backup_name)
            self.load_backup_list()

    def restore_backup(self):
        self.restore_question = msg_restore_backup(self)

        if self.restore_question is not False:
            self.backup_item = self.list_backup.currentItem()
            self.backup_name = self.backup_item_selector(self.backup_item)

            restore_backup(self.backup_name)
            msg_restore_finishied(self, self.backup_name)


def start():
    app = QApplication(sys.argv)

    QCoreApplication.setApplicationName('Minecraft Backup Manager')
    QCoreApplication.setApplicationVersion('1.0')
    app.setWindowIcon(QIcon(IMAGES['minebackup_icon']))

    #Create configuration
    configuration.config()

    minebackup = main_window()
    minebackup.show()

    sys.exit(app.exec_())
