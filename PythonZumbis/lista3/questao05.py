num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")

while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp
print num1
