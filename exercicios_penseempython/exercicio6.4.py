def is_power(a, b) :
    if b == a :
        return True
    elif b == 1 :
        return a == 1
    elif a % b == 0 : 
        return is_power(a / b, b)
    else : 
        return False
    
print(is_power(27,3))