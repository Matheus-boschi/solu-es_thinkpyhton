def is_triangle(a, b, c):
    if a > c + b or b > a + c or c > a + b :
        print("no")
    else : 
        print("yes")

# is_triangle(5, 2, 8)# NO
# is_triangle(4, 4, 4)# YES


def comprimento() : 
    a = int(input("Digite o comprimento a: "))
    b = int(input("Digite o comprimento b: "))
    c = int(input("Digite o comprimento c: "))


    is_triangle(a, b, c)


comprimento()




