import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = 'Python\n3 4 1 2 0 5'
    sys.stdin = io.StringIO(datastr)

    result = main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
    assert len(result) == 6
    assert result[0] == 'o'
    assert result[1] == 't'
    assert result[2] == 'h'
    assert result[3] == 'P'
    assert result[4] == 'y'
    assert result[5] == 'n'


def test_main_2():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = 'Python\n0 5 1 2 3 4'
    sys.stdin = io.StringIO(datastr)

    result = main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
    assert len(result) == 6
    assert result[0] == 'P'
    assert result[1] == 't'
    assert result[2] == 'h'
    assert result[3] == 'o'
    assert result[4] == 'n'
    assert result[5] == 'y'
