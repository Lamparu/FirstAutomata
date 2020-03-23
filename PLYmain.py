from checkYACC import ParserClass


def PLYcheck():
    f = open('genSTR.txt')
    parser = ParserClass()
    for line in f.readlines():
        parser.checkString(line)
        if parser.flag:
            print(line)
    f.close()


PLYcheck()