#!/usr/bin/python3
from collections import namedtuple

File = namedtuple("File", "size contents".split())


fs = {
    "A:": {},
    "B:": {},
    "C:": {
        "DOS64": {
            "COMMAND.COM": File(234234, "blep"),
            "MODEM.COM": File(23432, "boop"),
            "README.TXT": File(234, "what u lookin at?"),
        },
        "natpunk": {
            "DOCS": {
                "help.txt": File(16287897674576, "RTFM!"),
                "Dloads": {
                    "dos64-updater.py": File(236866, "Know one knows that."),
                },
            },
        },
        "Sys": {
            "dos64.conf": File(7657657765765765676755, "STOP"),
        },
        "sys32": {
            "PROGRAMS": {
                "clear": File(1234, "Clears screen"),
                "dir": File(6565646465564566567765564546464656, "Do NOT EDIT"),
                "exit": File(6010101, "EXIT"),
                "date": File(6545677, "DATE"),
            },
        },
    },
    "D:": {},
}


def printdir(dir):
    contents = dir.keys()
    for item in contents:
        if type(dir[item]) == File:
            print(f"{item:13s} {dir[item].size:012d}")
        else:
            print(f"{item:13s} <DIR>")


if __name__ == "__main__":
    printdir(fs["C:"]["natpunk"]["DOCS"])
