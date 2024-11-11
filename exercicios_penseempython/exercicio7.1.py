import math

def mysqrt(a) :
    x = 4.0
    while True : 
        y = (x + a/x) / 2
        if y == x : 
            return y
        x = y



def test_square_root() : 
    print(f"{'a':<5} {'mysqrt(a)':<15} {'math.sqrt(a)':<15} {'diff':<15}") 
    print(f"{'-':<5} {'---------':<15} {'------------':<15} {'----':<15}")

    a = 1.0
    while a < 10 :
        my_sqrt = mysqrt(a)
        math_sqrt = math.sqrt(a)
        diff = abs(my_sqrt - math_sqrt)
        print(f"{a:<5.1f} {my_sqrt:<15.12f} {math_sqrt:<15.12f} {diff:<15.12f}")
        a += 1



test_square_root()


    







