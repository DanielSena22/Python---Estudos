#String
numero = int(input('Digite um numero de 0 a 9999: '))
#n = str(numero)
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Analisando o número {numero}')
#Calculos
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print((f'Milhar: {milhar}'))




#print(f'Unidade: {numero[3]}')
#print(f'Dezena: {numero[2]}')
#print(f'Centena: {numero[1]}')
#print((f'Milhar: {numero[0]}'))
