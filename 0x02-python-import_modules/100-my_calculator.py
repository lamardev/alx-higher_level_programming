#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1

    argv_len = len(argv)
    error_usage = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    error_operator = "Unknown operator. Available operators: +, -, * and /"
    operators = ['+', '-', '*', '/']

    if argv_len > 3:
        if argv[2] in operators:
            #operate()
            print(f"{argv[1]} {argv[2]} {argv[3]} = {exec[int(argv[1]) argv[2] int(argv[3]))]}")
        else:
            print()
    else:
        print(error_usage)

    #def operate():
    #    """ Performs arithmetic operation based on argv passed
    #    """
        

    


