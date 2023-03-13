import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = '1 2 3 4 5\n55 66 77 88 99'
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
    assert len(result) == 10
    assert result[0] == 1
    assert result[1] == 55
    assert result[2] == 2
    assert result[3] == 66
    assert result[4] == 3
    assert result[5] == 77
    assert result[6] == 4
    assert result[7] == 88
    assert result[8] == 5
    assert result[9] == 99


def test_main_2():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = '1 3 5\n 2 4 6'
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
    assert result[0] == 1
    assert result[1] == 2
    assert result[2] == 3
    assert result[3] == 4
    assert result[4] == 5
    assert result[5] == 6
