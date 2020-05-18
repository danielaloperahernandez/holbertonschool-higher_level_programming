#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as error:
        sys.stderr.write("Exception: {}".format(error))
        return None
