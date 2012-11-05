# -*- coding: utf-8 -*-
# This file is part of Minecraft Backup Manager
# Source: https://github.com/LuqueDaniel/Minecraft_backup.git


# Minecraft Backup Manager
import minecraft_backup
from minecraft_backup.resources import IMAGES

# PyQt4.QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QHBoxLayout

# PyQt4.QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QSize


class about_minebackup(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.setWindowTitle('About Minecraft Backup')
        self.setMaximumSize(QSize(0, 0))

        vbox = QVBoxLayout(self)

        #Header
        self.header = QLabel()
        self.header.setPixmap(QPixmap(IMAGES['minebackup_icon_128']))

        hbox = QHBoxLayout()
        hbox.addWidget(self.header)

        #title_label
        self.label_title = QLabel('<h1>Minecraft Backup Manager</h1>', self)
        self.label_title.setAlignment(Qt.AlignRight)
        self.label_title.setTextFormat(Qt.RichText)

        hbox.addWidget(self.label_title)
        vbox.addLayout(hbox)

        #label_description
        self.label_description = QLabel(
"""Minecraft Backup Manager is an application for managing Minecraft
backups quickly and easily.""")

        vbox.addWidget(self.label_description)

        #label_version
        self.label_version = QLabel('Version: %s (%s)' % (
                                    minecraft_backup.__version__,
                                    minecraft_backup.__version_name__))

        vbox.addWidget(self.label_version)

        #label_license
        self.label_license = QLabel('License: %s' % (
                                    minecraft_backup.__license__))

        vbox.addWidget(self.label_license)

        #label_source
        self.label_source = QLabel('Source: <a href="%s">%s</a>' % (
                minecraft_backup.__source__, minecraft_backup.__source__))

        vbox.addWidget(self.label_source)
