# -*- coding: utf-8 *-*
# This file is part of Minecraft backup Manager

# Minecraft Backup Manager
from minecraft_backup.resources import IMAGES
from minecraft_backup.core import configuration
from minecraft_backup.core.backup_manager import load_backup_list
from minecraft_backup.core.backup_manager import remove_backup_name
from minecraft_backup.core.backup_manager import remove_backup
from minecraft_backup.gui.center_widget import center_widget
from minecraft_backup.gui.msg_box import msg_about_qt
from minecraft_backup.gui.msg_box import msg_backup_folder_not_exists
from minecraft_backup.gui.msg_box import msg_remove_backup
from minecraft_backup.gui.dialogs import config_window
from minecraft_backup.gui.dialogs import new_backup_window

# PyQt4.QtGui
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QListWidgetItem
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QMessageBox

# PyQt4.QtCore
from PyQt4.QtCore import QCoreApplication
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QRect

# sys
import sys

# os
from os import path


class main_window(QMainWindow):

    def __init__(self):
        super(main_window, self).__init__()

        self.setWindowTitle('Minecraft Backup Manager')
        self.setGeometry(0, 0, 700, 500)
        self.setMinimumSize(700, 500)
        self.setMaximumSize(700, 500)
        center_widget(self)

        self.header()

        # btn_config
        self.btn_config = QPushButton(self)
        self.btn_config.setGeometry(QRect(7, 7, 30, 30))
        self.btn_config.setToolTip('Configuration')

        # menu bar
        self.menu_bar = self.menuBar()

        self.menu_help = self.menu_bar.addMenu('About')
        self.menu_help.addAction('About Minecraft Backup Manager')
        self.menu_help.addAction('About Qt', lambda: msg_about_qt(self))

        # list_backup
        self.list_backup = QListWidget(self)
        self.list_backup.setGeometry(QRect(20, 170, 450, 310))

        # btn_new_backup
        self.btn_new_backup = QPushButton('New backup', self)
        self.btn_new_backup.setGeometry(QRect(485, 170, 200, 30))

        # btn_restore_backup
        self.btn_restore_backup = QPushButton('Restore backup', self)
        self.btn_restore_backup.setGeometry(QRect(485, 240, 200, 30))
        self.btn_restore_backup.setEnabled(False)

        # btn_remove_backup
        self.btn_remove_backup = QPushButton('Remove Backup', self)
        self.btn_remove_backup.setGeometry(QRect(485, 280, 200, 30))
        self.btn_remove_backup.setEnabled(False)

        # CONNECT SIGNALS
        self.connect(self.btn_config, SIGNAL('clicked()'), self.open_config)
        self.connect(self.btn_new_backup, SIGNAL('clicked()'),
                     self.open_new_backup)
        self.connect(self.btn_remove_backup, SIGNAL('clicked()'),
                     self.remove_backup)
        self.connect(self.list_backup,
                     SIGNAL('itemClicked(QListWidgetItem *)'),
                     self.enabled_buttons)

        self.load_backup_list()

    def load_backup_list(self):
        self.list_backup.clear()
        self.backup_list = load_backup_list()

        if self.backup_list is not False:
            for backup in self.backup_list.items():
                if path.exists(backup[1]):
                    self.list_item = QListWidgetItem(backup[0])
                    self.list_item.setToolTip(backup[1])

                    self.list_backup.addItem(self.list_item)
                else:
                    msg_backup_folder_not_exists(self, backup[0])
                    remove_backup_name(backup[0])

    def header(self):
        self.header_label = QLabel(self)
        self.header_label.resize(700, 150)
        self.header_label.setPixmap(QPixmap(IMAGES['header']))

    def enabled_buttons(self):
        self.btn_remove_backup.setEnabled(True)
        self.btn_restore_backup.setEnabled(True)

    def open_config(self):
        self.configuration_window = config_window.config_window(self)
        self.configuration_window.show()

    def open_new_backup(self):
        self.new_backup_window = new_backup_window.new_backup_window(self)
        self.new_backup_window.show()

        # CONNECT SIGNALS
        self.connect(self.new_backup_window, SIGNAL('close()'),
                     self.load_backup_list)

    def remove_backup(self):
        self.remove_question = msg_remove_backup(self)

        if self.remove_question is not False:
            self.backup_item = self.list_backup.currentItem()
            remove_backup(self.backup_item.text())
            self.load_backup_list()


def start():
    app = QApplication(sys.argv)

    QCoreApplication.setApplicationName('Minecraft Backup Manager')

    # Create configuration
    configuration.config(configuration.get_os())

    minebackup = main_window()
    minebackup.show()

    sys.exit(app.exec_())
