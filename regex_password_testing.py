# ^                         Start anchor
# (?=.*[A-Z].*[A-Z])        Ensure string has two uppercase letters.
# (?=.*[!@#$&*])            Ensure string has one special case letter.
# (?=.*[0-9].*[0-9])        Ensure string has two digits.
# (?=.*[a-z].*[a-z].*[a-z]) Ensure string has three lowercase letters.
# .{8,100}                  Ensure string is of length 8-100.
# $                         End anchor.

import re

regex_dict = {
    'full_pattern': {
        'regex': '^(?=.*[A-Z].*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8,100}$',
        'true_string': 'This is a full match, nice password!  \nLets look at all the things you did right.\n\n',
        'false_string': 'Lets dig a little deeper into why this password doesn\' work!\n',
    },
    'two_upper_pattern': {
        'regex': '^(?=.*[A-Z].*[A-Z])',
        'true_string': 'This password contains two uppercase letters!',
        'false_string': 'Add at least two uppercase letters!',
    },
    'special_case_pattern': {
        'regex': '^(?=.*[!@#$&*])',
        'true_string': 'This password contains a special character!',
        'false_string': 'You need to add a special character!',
    },
    'two_digits_pattern': {
        'regex': '^(?=.*[0-9].*[0-9])',
        'true_string': 'This password contains two digits!',
        'false_string': 'Add at least two digits!',
    },
    'three_lower_pattern': {
        'regex': '^(?=.*[a-z].*[a-z].*[a-z])',
        'true_string': 'This password contains three lowercase letters!',
        'false_string': 'Add at least three lowercase letters!',
    },
    'at_least_eight_pattern': {
        'regex': '^(?=.{8,100})',
        'true_string': 'This password contains at least eight characters (less than 100)!',
        'false_string': 'You need to add at least eight characters(or less than 100)!',
    },
}
string = input('Enter a string to search: ')
example_good_password = 'T3st!ngPassw0rd'

for pattern_name, pattern_data in regex_dict.items():
    regex_pattern = pattern_data['regex']
    true_string = pattern_data['true_string']
    false_string = pattern_data['false_string']

    if re.search(regex_pattern, string):
        print(true_string)
    else:
        print(false_string)
