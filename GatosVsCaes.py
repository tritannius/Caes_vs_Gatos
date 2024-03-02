from random import randint
from time import sleep
cores = {'limpa': '\033[m',
         'azul': '\033[0;34m',
         'vermelho': '\033[0;31m',
         'amarelo': '\033[0;33m',
         'verde': '\033[0;32m',
         'roxo': '\033[0;35m'
         }

Gato = 20
Cao = 20
print(f'{cores["vermelho"]}')
print('=' * 140)
print(f'{cores["amarelo"]}Nos confins da galáxia, há um gato patrulheiro que mantém a ordem dos enfurecidos cães que '
      f'buscam a destruição do universo.\nEm um fatídico dia, um cão tenta atravessar a fronteira intergaláctica e da de'
      f' cara com o gato.\nUma batalha irrompe, ajude o gato a vencer nessa luta!')
print(f'{cores["vermelho"]}')
print('=' * 140)
sleep(1)

while Gato > 0 and Cao > 0:
    danog = randint(0,5)
    danoc = randint(0,5)

    atq = input(f'{cores["amarelo"]}Digite "atq" para atacar o inimigo! \n')

    if danoc == 0:
        print(f'{cores["azul"]}O gato tenta acertar o cão com sua arma laser, porém ele desvia milagrosamente! Causando {danoc} de dano!{cores["limpa"]}')

    elif danoc <= 3:
        print(f'{cores["azul"]}O gato acerta o cão com sua arma laser, porém o tiro foi de raspão! Causando {danoc} de dano!{cores["limpa"]}')

    elif danoc == 4 or 5:
        print(f'{cores["roxo"]}Ataque crítico, o seu gato manda um tiro laser poderoso, machucando gravemente o cão! Causando {danoc} de dano!{cores["limpa"]}')

    Cao = Cao - danoc
    print(f'O cão possui {Cao} de vida!')

    if danog == 0:
        print(f'{cores["verde"]}Após uma esquiva incrível, seu gato desviou do ataque e saiu ileso!{cores["limpa"]}')

    elif danog <= 3:
            print(
                f'{cores["verde"]}O cão tenta te acertar com suas unhas, porém ele não consegue um ataque em cheio.{cores["limpa"]}')

    elif danog == 4 or 5:
        print(f'{cores["vermelho"]}Ataque crítico, o cão consegue te morder causando diversos sangramentos!{cores["limpa"]}')

    Gato = Gato - danog

    print(f'O seu gato possui {Gato} de vida!')


if Cao<=0:
        print(f'{cores["amarelo"]}O gato venceu, a galáxia continua em paz, mande o cão para a cadeia espacial!{cores["limpa"]}')
elif Gato <= 0:
            print(f'{cores["amarelo"]}O cão ganhou, a paz na galáxia será DESTRUÍDA!!!')

