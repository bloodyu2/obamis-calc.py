# Calculadora simples em Python comentada

# Definir as funções da calculadora
print("\n******************* Python Calculator *******************")


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

# Chamar os prints das funções iniciais
print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Adicionar as funções input
opt = input("\nEscolha a opção desejada: \n")

numInput1 = int(input("\nDigite o primeiro número:"))
numInput2 = int(input("\nDigite o segundo número:"))

# Definir cada operação:
if opt == '1':
    print("\n")
    print(numInput1, "+", numInput2, "=", add(numInput1, numInput2))
    print("\n")

elif opt == '2':
    print("\n")
    print(numInput1, "-", numInput2, "=", subtract(numInput1, numInput2))
    print("\n")

elif opt == '3':
    print("\n")
    print(numInput1, "x", numInput2, "=", multiply(numInput1, numInput2))
    print("\n")

elif opt == '4':
    print("\n")
    print(numInput1, "/", numInput2, "=", divide(numInput1, numInput2))
    print("\n")

else:
    while opt > '4':
        opt = input("\nOpção inválida, escolha novamente: \n")
        numInput1 = int(input("\nDigite o primeiro número:"))
        numInput2 = int(input("\nDigite o segundo número:"))
        if opt == '1':
            print("\n")
            print(numInput1, "+", numInput2, "=", add(numInput1, numInput2))
            print("\n")

        elif opt == '2':
            print("\n")
            print(numInput1, "-", numInput2, "=", subtract(numInput1, numInput2))
            print("\n")

        elif opt == '3':
            print("\n")
            print(numInput1, "x", numInput2, "=", multiply(numInput1, numInput2))
            print("\n")

print ("Obrigado por usar a Calculator Obamis!")