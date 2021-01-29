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
while True:
  opt = int(input("\nEscolha a opção desejada: \n"))

  if(opt>0 and opt<5):
    a = int(input("\nDigite o primeiro número:"))
    b = int(input("\nDigite o segundo número:"))

#Definir as funções resumidas (não é necessário adicionar print (\n) sempre)
    if(opt==1):
      print(a,"+",b,"=",add(a,b))
    elif(opt==2):
      print(a,"-",b,"=",subtract(a,b))
    elif(opt==3):
      print(a,"*",b,"=",multiply(a,b))
    elif(opt==4):
      print(a,"/",b,"=",divide(a,b))
    else:
      print(error())
  elif(opt==0):
    break
  else:
    print(error())

print("Obrigado por usar a Calculator Obamis!")
