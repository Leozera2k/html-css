extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite o número que deseja que seja escrito por extenso (Entre 0 e 20): '))
    if num > 0 and num < 20:
        print(f'Você digitou o número {extenso[num]}')
        break
    else:
        print('Número invalido. Tente novamente.')