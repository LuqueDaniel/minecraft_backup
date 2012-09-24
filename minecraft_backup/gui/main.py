# -*- coding: utf-8 *-*
# This file is part of Minecraft backup

# sys
import sys

# Minecraft Backup
from minecraft_backup.resources import IMAGES
from minecraft_backup.core import configuration
from minecraft_backup.gui.center_widget import center_widget
from minecraft_backup.gui.dialogs import config_window
from minecraft_backup.gui.dialogs import new_backup_window

# PyQt4.QtGui
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QPushButton

# PyQt4.QtCore
from PyQt4.QtCore import QCoreApplication
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QRect


class main_window(QMainWindow):

    def __init__(self):
        super(main_window, self).__init__()

        self.setWindowTitle('Minecraft Backup')
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
        self.menu_help.addAction('About Minecraft Backup')
        self.menu_help.addAction('About Qt')

        # list_backup
        self.list_backup = QListWidget(self)
        self.list_backup.setGeometry(QRect(20, 170, 450, 310))

        # btn_new_backup
        self.btn_new_backup = QPushButton('New backup', self)
        self.btn_new_backup.setGeometry(QRect(485, 170, 200, 30))

        # CONNECT SIGNALS
        self.connect(self.btn_config, SIGNAL('clicked()'), self.open_config)
        self.connect(self.btn_new_backup, SIGNAL('clicked()'),
                     self.open_new_backup)

    def header(self):
        header_label = QLabel(self)
        header_label.resize(700, 150)
        header_label.setPixmap(QPixmap(IMAGES['header']))

    def open_config(self):
        self.configuration_window = config_window.config_window(self)
        self.configuration_window.show()

    def open_new_backup(self):
        self.new_backup_window = new_backup_window.new_backup_window(self)
        self.new_backup_window.show()


def start():
    app = QApplication(sys.argv)

    QCoreApplication.setApplicationName('Minecraft Backup')

    # Create or load configuration
    configuration.config(configuration.get_os())

    minebackup = main_window()
    minebackup.show()

    sys.exit(app.exec_())

if __name__ != '__main__':
    start()
