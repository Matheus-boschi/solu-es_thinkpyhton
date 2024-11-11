def eval_loop() : 
    while True : 
        entrada = eval(str(input(f"Digite um cálculo matemático :")))
        print(entrada)
        if entrada == "done" : 
            break
        


eval_loop()



