def invertir(num):
    acumulado = 0
    while num>0:
        acumulado = acumulado *10 + (num%10)
        num = num // 10

    return acumulado

valor = -1
while valor<=0:
    valor = int(input("digite un valor:"))

    if valor <=0:
        print("solo positivos" )

invertido = invertir(valor)
print(invertido)
