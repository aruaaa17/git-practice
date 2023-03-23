def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max_value = 0
    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value

<<<<<<< HEAD
# April
=======
# testing
>>>>>>> c9e217fa196d305d5f3f1eaecf81acc232e2300f

if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
