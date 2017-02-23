import sys
import operator


class Interpreter:
    # variables here

    # look up table for operations
    ops = {
        # math
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
        'div': operator.mod,
        # logical
        '&': operator.and_,
        '!': operator.not_,
        '|': operator.or_,
        '<>': operator.ne,
        '<=': operator.le,
        '>=': operator.ge,
        '<': operator.lt,
        '>': operator.gt,
        '=': operator.eq
    }

    # boolean conversions
    boolConvert = {
        0: False,
        1: True,
        False: 0,
        True: 1
    }



    def __init__(self):
        # initializing function
	
    # rest goes here


    # used to grab the file from command line arguments
    if __name__ == '__main__':
    # error catching
    if len(sys.argv) != 2:
        sys.stderr.write('incorrect number of arguments')
        sys.exit(1)
    filename = sys.argv[1]
    if not (filename.endswith('.jaz')):
        sys.stderr.write('incorrect file type')
        sys.exit(1)
    # read file into an array of lines
    file = open(filename)
    memory = [line.lstrip(' ').rstrip('\n') for line in file]
    file.close()
    # ***INTERPRETER CALL HERE***

