#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""
    if key not in a_dictionary.keys():
        return a_dictionary
    del a_dictionary[key]

    return a_dictionary
