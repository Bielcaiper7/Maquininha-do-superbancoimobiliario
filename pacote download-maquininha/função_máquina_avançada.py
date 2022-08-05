from Função import *
cartões = []
msg('Máquina', 6)
msg('Registro de cartões', 3)
lercartão(cartões)
msg('Cartões cadastrados', 2)
for c in cartões:
    print(f'{c[0]:<28}R${c[1]:.2f}')
print('-=' * 19)
while True:
    while True:
        try:
            escolha = int(input('''[0] Receber do banco
[1] Pagar ao banco
[2] Transferir dinheiro para jogador
escolha: '''))
        except:
            print('\033[1;31mERRO:Digite um número válido\033[m')
        else:
            break
        finally:
            print()
    if escolha == 0:
        recban(cartões)
        print('-=' * 19)
    elif escolha == 1:
        pagban(cartões)
        print('-=' * 19)
    elif escolha == 2:
        trandin(cartões)
        print('-=' * 19)
    else:
        print('\033[1;31mERRO:Digite um número válido !\033[m')
