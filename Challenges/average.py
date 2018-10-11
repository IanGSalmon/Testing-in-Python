# Add a doctest to average() that tests the function with the list [1, 2].
# Because of how we test doctests, you need to leave a blank line
# at the end of the doctest before the closing quotes.

def average(num_list):
    """Return the average for a list of numbers
    
    >>> average([1, 2])
    1.5
    
    """
    return sum(num_list) / len(num_list)