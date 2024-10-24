###############EXERCICIO 3.1###################
# def right_justify(s):
#     n = 70 - len(s)
#     print(" " * n + s)

# right_justify("matheus")

###############EXERCICIO 3.2###################
# def do_twice(f, valor ) :
#     f(valor)
#     f(valor)

# # def print_(horas) : 
# #     print(f"Olá são {horas} horas")


# # do_twice(print_, 4)



# # def print_twice(bruce) : 
# #     print(bruce)
# #     print(bruce)



# def do_four(f, valor) : 
#     do_twice(f,valor)
#     do_twice(f,valor)


# do_four()


###### EXERCICIO 3.3 ######
def desenha_tudo() :

    def linha_horizontal() : 
        print("+", "- - - - ", "+", "- - - - ", "+",sep="")
        


    def linha_vertical() :
        print("|", ' ' * 8, "|", ' ' * 8, "|", sep="")
        print("|", ' ' * 8, "|", ' ' * 8, "|", sep="")
        print("|", ' ' * 8, "|", ' ' * 8, "|", sep="")
        print("|", ' ' * 8, "|", ' ' * 8, "|", sep="")

        
        
    linha_horizontal()
    linha_vertical()
    linha_horizontal()
    linha_vertical()
    linha_horizontal()



desenha_tudo()






           








    


    








