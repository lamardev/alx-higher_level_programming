#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv)
    argv_sum = 0
    for i in range(1, argv_len):
        argv_sum += int(argv[i])
    print(argv_sum)
