#x = y = 1
#print(x)
#print(virgula)
#x = 2
#y = 2
#resultado = x * y
#print(resultado)
#EXERCICIOS 2.2


#pi = 3.14
#r = 5
#esfera = (r**3) * pi

# #print(f"A esfera com raio 5 mede {esfera}")

# capa = 24.95
# desconto_capa = capa * 0.40
# transporte = 3
# adicional = transporte + 0.75
# primeira_cópia = desconto_capa + transporte
# copias_totais =(primeira_cópia + adicional) * 59
# print(f"O custo total de cópias do livro vai ser igual a: {copias_totais}")


h_inicio = 6 + 52/60 # hora que ele saiu
# tempo de passo
segundos_para_minuto = (27 + 15) / 60
minuto = 23
minutos_totais = (minuto + segundos_para_minuto) * 5
hora_que_chegou = h_inicio + minutos_totais/60

hora = int(hora_que_chegou)
minutos = int((hora_que_chegou - hora) * 60)

print(f"Ele chegou as {hora}:{minutos} da manhã")




