def CalcularResiduo(divisor, dividendo):
    while divisor > dividendo:
        divisor = divisor - dividendo

    return divisor


divisor =-1
dividendo=-1

while divisor < 0 or  dividendo < 0:
    divisor = int(input("digite el dividendo:" ))
    dividendo = int(input("digite el dividendo: " ))

    if divisor < 0 or dividendo <0:
        print("solo positivos.")
    else:
        resultado = CalcularResiduo(divisor,dividendo)
print(resultado)
    
