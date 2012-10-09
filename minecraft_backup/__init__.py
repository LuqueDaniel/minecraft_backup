#-*- conding: utf-8 -*-
#This file is part of Minecraft Backup Manager


__prj__ = 'Minecraft Backup Manager'
__author__ = 'Daniel Luque'
__mail__ = 'danielluque14@gmail.com'
__source__ = ''
__version__ = "0.1"
__license__ = "GPL3"
__docu__ = """Minecraft Backup Manager is
             an application for manage backups of Minecraft
           """


def run():
    from minecraft_backup import core

    core.run_minebackup()
