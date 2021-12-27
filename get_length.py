#get number of digits in an int?
def get_length(num):
    """
    Get length of integer

    Args:
        num (int): integer to get length of

    Returns:
        int: length of integer
    """
    
    x1=pow(0,num)

    num//=10
    x2=pow(0,num)

    num//=10
    x3=pow(0,num)

    num//=10
    x4=pow(0,num)

    num//=10
    x5=pow(0,num)
    
    # return number of digits in integer
    return 5-(x1+x2+x3+x4+x5)

 