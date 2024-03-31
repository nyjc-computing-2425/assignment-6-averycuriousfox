from datetime import datetime
import time


# Part 1
def clock(n):
    """
    This function takes in a parameter "n", and will show the current time and update it once every second for "n" number of seconds

    Parameters
    ----------
    n:
        A positive integer

    Returns
    -------
    datetime:
        Current time that updates every second for "n" numbers of seconds.

    Examples
    ----------
    >>> clock(3)
    12:59:17

    """
    # Your code here
    counter = 0
    while counter < n:
        time_now = datetime.now()
        print(time_now.strftime("%H:%M:%S"),end="\r")
        counter += 1
        time.sleep(1)

# Part 2
def lcm(a, b):
    """
    Take in two integers, a and b, and calculate their lowest common multiples (lcm)

    Parameters
    ----------
    a,b:
        Two integers

    Returns
    -------
    int:
        a single integer, the lcm of a and b

    Examples
    ---------
    >>> lcm(2, 3)
    6
    >>> lcm(12, 5)
    60

    """
    # Your code here
    if a == b:
        lcm = a
    else:
        val_1 = a
        val_2 = b
        while a != b:
            if a < b:
                a += val_1
            else:
                b += val_2
        lcm = a
    return lcm

# Part 3
def gcf(a, b):
    """
    This function takes in two positive integers, a and b, and calculate their greatest common factor (gcf)

    Parameters
    -----------
    a,b:
        two positive integers

    Returns
    -------
    int:
        a single integer, the gcf of a and b

    Examples
    ----------
    >>> gcf(60, 48)
    12
    >>> gcf(70, 14)
    14
    """
    # Your code here
    while b > 0:
        if b == 0:
            return a
        else:
            r = a % b
            a = b
            b = r
            
    return a 
