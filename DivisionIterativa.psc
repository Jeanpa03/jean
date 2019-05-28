Algoritmo Division
	divisor = -1
	dividendo = -1
	Mientras divisor <=0 o dividendo<=0 Hacer
		Escribir "digite el divisor"
		Leer divisor
		Escribir "digite el dividendo: "
		Leer dividendo
		Si divisor > 0 y dividendo >0 Entonces
			resultado = DivisionIterativa(divisor, dividendo)
			Escribir resultado
		SiNo
			Escribir "solo positivos"
		FinSi
	FinMientras
FinAlgoritmo

Funcion resultado = divisionIterativa(divisor, dividendo)
	resultado = 0 
	Mientras divisor>0 Hacer
		resultado = resultado + 1 
		divisor = divisor - dividendo
	FinMientras
FinFuncion

