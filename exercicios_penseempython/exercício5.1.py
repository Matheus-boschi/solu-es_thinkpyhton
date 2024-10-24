import time

# Obtendo a hora atual em segundos desde a época
hora_atual = time.time()

# Convertendo para dias, horas, minutos e segundos
dias = int(hora_atual // (24 * 3600))  # Número de dias
segundos_restantes = int(hora_atual % (24 * 3600))  # Segundos restantes
horas = segundos_restantes // 3600  # Número de horas
segundos_restantes %= 3600  # Atualizando segundos restantes
minutos = segundos_restantes // 60  # Número de minutos
segundos = segundos_restantes % 60  # Segundos finais

# Exibindo os resultados
print(f"Horas: {horas}, Minutos: {minutos}, Segundos: {segundos}, Dias desde a época: {dias}")



