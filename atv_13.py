# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.
def verificar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Zero"

numero = float(input("Digite um número: "))

print(f"O número é: {verificar_numero(numero)}")
