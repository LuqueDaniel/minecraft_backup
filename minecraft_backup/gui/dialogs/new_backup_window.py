# -*- coding: utf-8 *-*
# This file is part of Minecraft Backup

# Minecraft Backup
from minecraft_backup.core.configuration import load_config
from minecraft_backup.gui.center_widget import center_widget
from minecraft_backup.core.make_backup import make_backup

# PyQt4.QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QFileDialog

# PyQt4.QtCore
from PyQt4.QtCore import QRect
from PyQt4.QtCore import SIGNAL

# os
from os import path


class new_backup_window(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setGeometry(QRect(0, 0, 450, 150))
        self.setMaximumSize(450, 150)
        self.setMinimumSize(450, 150)
        self.setWindowTitle('Create a new backup')
        center_widget(self)

        # STANNDARD BUTTONS
        self.btn_cancel = QPushButton('Cancel', self)
        self.btn_cancel.setGeometry(QRect(135, 110, 80, 28))

        # btn_create_backup
        self.btn_create_backup = QPushButton('Create backup', self)
        self.btn_create_backup.setGeometry(QRect(235, 110, 200, 28))

        # LABELS
        self.generate_label('Name', 15, 20)
        self.generate_label('Save folder', 15, 70)

        # input_backup_name
        self.input_backup_name = QLineEdit(self)
        self.input_backup_name.setGeometry(QRect(100, 17, 335, 25))
        self.input_backup_name.setToolTip('Name of backup')
        self.input_backup_name.setFocus()

        # btn_change_save_backup
        self.btn_change_save_backup = QPushButton(
                                      load_config('save_backup_folder'), self)
        self.btn_change_save_backup.setGeometry(QRect(100, 64, 335, 30))

        # CONNECT SIGNALS
        self.connect(self.btn_change_save_backup, SIGNAL('clicked()'),
                     self.change_save_backup)
        self.connect(self.btn_cancel, SIGNAL('clicked()'), self.close)
        self.connect(self.btn_create_backup, SIGNAL('clicked()'),
                     self.create_backup)

    def generate_label(self, text, h, v):
        self.label = QLabel(self)
        self.label.setText(text)
        self.label.adjustSize()
        self.label.move(h, v)

    def change_save_backup(self):
        self.file_dialog = QFileDialog.getExistingDirectory(self,
                           'Select folder saved for backup',
                           directory=self.btn_change_save_backup.text())

        if self.file_dialog != '':
            self.btn_change_save_backup.setText(self.file_dialog)

    def create_backup(self):
        self.dst = path.join(str(self.btn_change_save_backup.text().toUtf8()),
                             str(self.input_backup_name.text().toUtf8()))
        make_backup(self.dst)

        self.close()
