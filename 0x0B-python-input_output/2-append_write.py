#!/usr/bin/python3
"""
appends a string at the
end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
     Returns The number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
