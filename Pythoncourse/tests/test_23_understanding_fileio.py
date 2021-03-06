__author__ = 'Kalyan'

notes = '''
Python has a good api to deal with text and binary files. We explore that
in this module.

Use help(file.XXX) to find help on file method XXX (tell, seek etc.)
'''

from placeholders import *

#opens a file from the module directory.
def open_test_file(file, mode="rt"):
    import inspect, os.path
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)


def test_file_readlines():
    f = open_test_file("test_file.txt")
    lines = f.readlines()
    assert __ == lines


def test_file_read():
    f = open_test_file("test_file.txt")
    data = f.read()
    assert __ == data


def test_file_end():
    f = open_test_file("test_file.txt")
    s = f.read() # read till end.
    assert __ == f.read()
    assert __ == f.read()


def test_file_read_binary():
    f = open_test_file("test_file.txt", "rb")
    lines = f.readlines()
    assert __ == lines
    f.seek(0, 0)
    data = f.read()
    assert __ == data


def test_file_windows_newlines():
    f = open_test_file("newlines_tmp.txt", "wb")
    f.write("one\r\ntwo\rthree\n")
    f.close()

    f = open_test_file("newlines_tmp.txt", "rt")
    assert __ == f.read()
    f.close()

    f = open_test_file("newlines_tmp.txt", "rb")
    data = f.read()
    assert __ == f.read()

    #windows behavior : http://docs.python.org/2/bit-manipulation-tutorial/inputoutput.html#reading-and-writing-files


def test_file_universal_newlines():
    f = open_test_file("newlines_tmp.txt", "wb")
    f.write("one\r\ntwo\rthree\n")
    f.close()

    f = open_test_file("newlines_tmp.txt", "rU")
    assert __ == f.read()
    assert __ == f.newlines


def test_file_readline():
    f = open_test_file("test_file.txt")
    lines = []
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line)

    assert __ == lines


def test_file_iteration():
    f = open_test_file("test_file.txt")
    lines = []
    for x in f:
        lines.append(x)
    assert __ == lines


def test_file_tell():
    tells = []
    f = open_test_file("test_file.txt")
    while True:
        line = f.readline()
        tells.append(f.tell())
        if not line:
            break
    assert __ == tells


def test_file_readlines_tell():
    tells = []
    f = open_test_file("test_file.txt")
    for line in f.readlines():
        tells.append(f.tell())

    assert __ == tells


def test_file_iteration_tell():
    tells = []
    f = open_test_file("test_file.txt")
    for line in f:
        tells.append(f.tell())

    assert __ == tells # is there really no difference between readlines and iteration?


def test_file_seek():
    f = open_test_file("test_file.txt")
    assert __ == f.tell()
    f.read()
    assert __ == f.tell()
    assert __ == f.read()

    f.seek(0, 0)
    assert __ == f.read()
    f.seek(-3, 2)
    assert __ == f.read()
    f.seek(-2, 1)
    assert __ == f.read()

#windows has a few newlines quirks.
def test_file_write_text():
    f = open_test_file("test_write.txt", "w") # same as "wt"
    f.write("one\ntwo\nthree\n")
    f.close()

    f = open_test_file("test_write.txt", "rb")
    assert __ == f.read()

    f = open_test_file("test_write.txt", "rt")
    assert __ == f.read()


def test_file_write_binary():
    f = open_test_file("test_write.txt", "wb")
    f.write("one\ntwo\nthree\n")
    f.close()

    f = open_test_file("test_write.txt", "rb")
    assert __ == f.read()

    f = open_test_file("test_write.txt", "rt")
    assert __ == f.read()


# It is generally a good practice to close files after their use is over
def test_file_close():
    f = open_test_file("test_file.txt")
    assert __ == f.closed
    try:
        lines = [line.strip() for line in f.readlines()]
    finally:
    # putting it in finally so that it is closed even if an exception is raised
        f.close()
    assert __ == f.closed

# http://effbot.org/zone/python-with-statement.htm
def test_with_statement():
    try:
        with open_test_file("test_file.txt") as f:
            assert __ == f.closed
            raise Exception("some random exception")
    except Exception as ex:
        print ex
        pass

    assert __ == f.closed


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___
