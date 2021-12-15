import os
import subprocess as sp

paths = {
    'notepad': "/System/Applications/Notes.app",
    'discord': "/Applications/Discord.app",
    'calculator': "/System/Applications/Calculator.app",
    'camera': "/System/Applications/Photo Booth.app"
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_camera():
    os.startfile(paths['camera'])


def open_calculator():
    sp.Popen(paths['calculator'])


def open_cmd():
    os.system('start cmd')
