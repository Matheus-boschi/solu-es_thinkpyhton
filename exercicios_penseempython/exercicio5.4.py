def recurse(n, s) :
    '''
    uma função que recebe dois parâmetros n e s    

    tem como caso base, quando n for igual a 0

    enqunto n não for igual a 0,
    é subtraído 1 de n e somado n com s

    quando n chegar ao valor 0
    s é printado
    ''' 
    if n == 0 :
        print(s)
    else :
        recurse(n - 1, s + n)


recurse(3, 0)

