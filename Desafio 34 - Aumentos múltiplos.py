salario = float(input('Qual o salário do funcionario? R$ '))
aumento = salario
if salario <= 1.250: #Se o salario for menor ou igual 
    novo = salario + (salario * 15 / 100) #Calculo de porcetagem salario + 15% do salario
else: #Se não
    novo = salario + (salario * 10 / 100) #calculo de porcetagem salario + 10% do salario
print('Quem ganhava R${:.2f} passa a ganhar R${} agora.' .format(salario, novo))