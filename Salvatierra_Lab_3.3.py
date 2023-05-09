from utils.utils import sort_low, remove_dup

integer_numbers: list = []
entered_numbers: str = input(
    'Enter a list of interger numbers separeted by spaces: '
).strip()  # remove whitespaces at the beginning and the end of the string

if not entered_numbers:
    print('The entered list is empty')
else:
    valid_list: bool = False
    while not valid_list:
        try:
            # list comprehension to split a whole string in a list of element,
            # and then trying to parse the string to a integer value
            integer_numbers = [int(i) for i in entered_numbers.split()]
            valid_list = True
        except ValueError:
            # this exception happens when one of the elements can't be
            # converted to a valid integer 
            entered_numbers = input(
                'Some element in the list are not valid integers, please '
                'enter a valid list of integers: '
            )

    # remove duplicated elements
    integer_numbers = remove_dup(integer_numbers=integer_numbers)
    # sort the list in ascending order
    sort_low(integer_numbers=integer_numbers)

    print('The ordered list is: ' + ', '.join(str(i) for i in integer_numbers))
