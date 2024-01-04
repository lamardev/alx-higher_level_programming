#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv)
    if argv_len == 1:
        print("0 arguments.")
    elif argv_len == 2:
        print("1 argument:")
        print("{:d}: {}".format(argv_len-1, argv[1]))
    else:
        print("{:d} arguments:".format(argv_len-1))
        for i in range(1, argv_len):
            print("{:d}: {}".format(i, argv[i]))
