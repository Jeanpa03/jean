Algoritmo ModuloIteratiamente
	Escribir "digite su divisor:"
	Leer divisor
	Escribir "digite su dividendo:"
	Leer dividendo
	Si dividendo>0 y divisor >0 Entonces
		resultado = CalcularResiduo(divisor, dividendo)
	SiNo
		Escribir "solo positivos"
	FinSi
	Escribir resultado
FinAlgoritmo

Funcion result = calcularresiduo(divisor, dividendo)
	Repetir
	Hasta Que divisor > dividendo
	divisor = divisor - dividendo
FinFuncion

