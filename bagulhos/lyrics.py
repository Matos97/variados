import sys              #Isso importa o módulo sys, que fornece acesso a algumas variáveis...
from time import sleep  #Isso importa apenas a função sleep do módulo time, que suspende a execução do programa pelo número especificado de segundos.
import time             #Isso importa o módulo time, que fornece várias funções relacionadas ao tempo.

def print_lyrics():     #A função print_lyrics() é definida. Ela contém duas listas: lines e delays.
                        #A lista lines contém tuplas, cada uma contendo uma linha da letra da música e a duração de cada caractere.
    lines = [
        ("Because I can see us holding hands", 0.04),
        ("Walking on the beach, our toes in the sand", 0.05),
        ("I can see us on the country side", 0.06),
        ("Sitting in the grass, laying side by side", 0.1),
        ("You can be my baby", 0.08),
        ("Let me make you my lady, girl, you amaze me", 0.06),
        ("Ain't gotta do nothin' crazy ", 0.07),
        ("See all I want you to do is be my love (so don't give away)", 0.07),
        ("My love (so don't give away)", 0.06),
        ("My love (so don't give away)", 0.08),
        ("Ain't another woman that could take your spot", 0.05)
        
    ]

    delays = [0.03, 0.03, 0.03, 0.03, 0.04, 0.03, 0.03, 0.06, 0.07, 0.08, 0.08]  #A lista delays contém os atrasos entre cada linha.

    for i, (line, char_delay) in enumerate(lines):  #Um loop for é utilizado para percorrer cada linha na lista linhas.
        for char in line:                           #Dentro deste loop, há outro loop que percorre cada caractere na linha atual.
            print(char, end='')        #Isso imprime o caractere atual sem adicionar uma nova linha após a impressão.
            sys.stdout.flush()         #Isso garante que a saída seja exibida imediatamente, sem buffering.
            sleep(char_delay)          #Isso pausa a execução do programa por um período de tempo especificado pela variável char_delay, que representa a duração de cada caractere.


        time.sleep(delays[i])          #Após imprimir cada linha da música, é feita uma pausa usando time.sleep(delays[i]), onde i é o índice da linha atual na lista linhas.
        print('')

print_lyrics()                         #O código termina com uma chamada para a função print_lyrics() para executar a exibição das letras da música.