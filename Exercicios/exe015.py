def checarAnoBissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('é bissexto')


ano = int(input('Digite um ano: '))
checarAnoBissexto(ano)
