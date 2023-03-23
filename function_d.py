def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max_value = 0
    for k in numbers:
        if k > max_value:
            max_value = k
    
    return max_value

if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
