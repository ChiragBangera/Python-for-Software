# input vales are unpacked


def add_numbers(n1, n2):
    return n1 + n2


start_number = 2
add_number = 4

input_vals = [start_number, add_number]

numbers_mult = add_numbers(*input_vals)

print(numbers_mult)

# Global Variable


def test_function(x):
    y = x + 23
