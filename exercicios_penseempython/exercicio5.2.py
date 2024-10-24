def check_fermat(a, b , c, n) : 
    if n > 2 and (a ** n) + (b ** n) == (c ** n) : 
        print("Holy smokes, Fermat was wrong!")                 
    else:
        print("No, that doesn't work")


# check_fermat(2, 3, 4, 1)
# check_fermat(1, 5, 6, 3)


#parte dois
def register() : 
    a = int(input("informe um valor para a: "))
    b = int(input("informe um valor para b: "))
    c = int(input("informe um valor para c: "))
    n = int(input("informe um valor para n: "))
    check_fermat(a, b, c, n)
    


register()



