#get number of digits in an int?
def get_length(num):
    """
    Get length of integer

    Args:
        num (int): integer to get length of

    Returns:
        int: length of integer
    """
    x1=num%10
    num//=10
    x2=num%10
    num//=10
    x3=num%10
    num//=10
    x4=num%10
    num//=10
    x5=num%10
    num//10


    
    # return number of digits in integer
    return x1,x2,x3,x4,x5

 