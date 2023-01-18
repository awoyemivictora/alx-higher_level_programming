#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{Ld}".format(value))
        return True
    except (ValueError, TypeError):
        return False
