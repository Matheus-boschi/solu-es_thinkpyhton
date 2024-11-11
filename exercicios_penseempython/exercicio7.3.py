import math
def estimate_pi() : 
    C = (2 * math.sqrt(2) / 9801)

    soma_tot = 0
    k = 0 

    while True : 
        num = math.factorial(4 * k) * (1103 + 26390*k)
        den = (math.factorial(k) ** 4) * (396 ** (4*k))

        term = C * (num / den)

        soma_tot += term

        if term < 1e-15 : 
            break

        k += 1
    pi_estimate = 1 / soma_tot
    return pi_estimate



pi_aproximed = estimate_pi()
dif = pi_aproximed - math.pi
print(f"Estimativa de pi: {pi_aproximed}")
print(f"Valor de pi: {math.pi}")
print(f"Diferença: {dif}")


