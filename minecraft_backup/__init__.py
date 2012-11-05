#-*- conding: utf-8 -*-
#This file is part of Minecraft Backup Manager
# Source: https://github.com/LuqueDaniel/Minecraft_backup.git


__prj__ = 'Minecraft Backup Manager'
__author__ = 'Daniel Luque'
__mail__ = 'danielluque14@gmail.com'
__source__ = 'http://github.com/LuqueDaniel/Minecraft_backup.git'
__version__ = '1.0'
__version_name__ = 'Dirt'
__license__ = 'GPL3'
__docu__ = """Minecraft Backup Manager is an application for managing Minecraft
backups quickly and easily."""


def run():
    from minecraft_backup import core

    core.run_minebackup()
