def solve():
    my_string = 'abcdef'
    result_str = hidden_operation(my_string)
    if result_str == my_string:
        print('or')
        print(hidden_operation(False))
    elif result_str is False:
        if hidden_operation(True) is False and hidden_operation(False) is False:
            print('and')
            print('False')
        else:
            print('not')
    elif hidden_operation(False) is False:
        print('and')
        print(result_str)
