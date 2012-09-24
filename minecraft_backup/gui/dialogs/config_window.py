# -*- coding: utf-8 *-*
# This file is part of Minecraft Backup

# Minecraft Backu
from minecraft_backup.core.configuration import load_config
from minecraft_backup.core.configuration import save_new_config
from minecraft_backup.gui.center_widget import center_widget

# PyQt4.QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QDialogButtonBox

# PyQt4.QtCore
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QRect


class config_window(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setGeometry(0, 0, 500, 400)
        self.setMaximumSize(500, 400)
        self.setMinimumSize(500, 400)
        self.setWindowTitle('Minecraft Backup - Configuration')
        center_widget(self)

        # STANNDARD BUTTONS
        self.button_box = QDialogButtonBox(self)
        self.button_box.setGeometry(QRect(150, 360, 341, 32))
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel |
             QDialogButtonBox.Save)

        # LABELS
        self.label_save_folder = self.generate_label('Save Folder', 15, 20)

        # input_save_folder
        self.input_save_folder = QLineEdit(self)
        self.input_save_folder.setGeometry(QRect(100, 17, 290, 25))
        self.input_save_folder.setText(load_config('save_backup_folder'))
        self.input_save_folder.setToolTip('Default folder save backup')

        # change_save_folder
        self.btn_save_folder = QPushButton('Change', self)
        self.btn_save_folder.move(400, 15)

        # CONNECT SIGNALS
        self.connect(self.btn_save_folder, SIGNAL('clicked()'),
                     self.change_save_folder)
        self.connect(self.button_box, SIGNAL('accepted()'),
                     self.save_configurations)
        self.connect(self.button_box, SIGNAL('rejected()'), self.close)

    def generate_label(self, text, h, v):
        self.label = QLabel(self)
        self.label.setText(text)
        self.label.adjustSize()
        self.label.move(h, v)

    def change_save_folder(self):
        self.file_dialog = QFileDialog.getExistingDirectory(self,
                           'Change Default folder save backup',
                           directory=self.input_save_folder.text())

        if self.file_dialog != '':
            self.input_save_folder.setText(self.file_dialog)

    def save_configurations(self):
        self.backup_folder = str(self.input_save_folder.text().toUtf8())

        save_new_config(self.backup_folder)
        self.close()
