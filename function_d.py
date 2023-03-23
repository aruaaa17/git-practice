def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max_value = 0
    for i in numbers:
        if i > max_value:
            max_value = i
    
    return max_value

# Julie
# testing

if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
