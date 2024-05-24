#!/usr/bin/python3
"""
A module that defines a validation function
"""


def validUTF8(data):
    """
    function to validate utf-8 encoding
    Returns:
        boolean: true if the data is valid utf-8 encoded,
        otherwise false
    """
    utf8valid = 0
    for val in data:
        byte = val & 255
        if utf8valid:
            if byte >> 6 != 2:
                return False
            utf8valid -= 1
            continue
        while (1 << abs(7 - utf8valid)) & byte:
            utf8valid += 1
        if utf8valid == 1 or utf8valid > 4:
            return False
        utf8valid = max(utf8valid - 1, 0)
    return utf8valid == 0
