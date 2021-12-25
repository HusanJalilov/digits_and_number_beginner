#get number of digits in an int?
def get_length(num):
    """
    Get length of integer
`   
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
    num//=10


    
    
    # return number of digits in integer
    return 5-(x1%2+x2%2+x3%2+x4%2+x5%2)+(x1%2+x2%2+x3%2+x4%2+x5%2)
print(get_length(24))

 