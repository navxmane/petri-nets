import numpy as np


def define_transicoes_places():
    while True:
        try:
            t = int(input("Digite o número de transições: "))
            p = int(input("Digite o número de places: "))
            if t < 0 or p < 0:
                print("Digite um número maior que zero!")
                continue
            return t, p
        except ValueError:
            print("\n[!] ERRO: Digite um número inteiro!\n")

def define_matriz(p, t):
    matriz = np.zeros((p, t))
    for i in range(p):
        print(f'\n--- Para o Lugar (Place) {i + 1} ---')
        for j in range(t):
            n = input(f'Digite um valor para transição {j + 1}')
            if n.strip() != '':
                try:
                    matriz[i][j] = int(n)
                except ValueError:
                    print('\n[!] ERRO: Digite um valor inteiro!\n')
    return matriz

def initial_mark(places):
    x = []
    for _ in range(places):
        x.append(int(input(f'Dgite a marcação para posição {_ + 1}')))
    return x

def main():
    transicoes, places = define_transicoes_places()
    pre_matriz = define_matriz(places, transicoes)
    post_matriz = define_matriz(places, transicoes)
    x_ = initial_mark(places)


main()