# Funciones:

# valores por defecto
def suma(x=10,y=20):
	r = x + y
	return r

num1 = int(input("Nº 1: "))
num2 = int(input("Nº 2: "))

resultado = suma(num1,num2)

print(f"El resultado es {resultado}")