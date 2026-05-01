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
    for i in range(places):
        while True:
            try:
                mark = int(input(f'Digite a marcação inicial para posição {i + 1}'))
                if mark < 0:
                    print('Digite um núero maior que zero!')
                    continue
                x.append(mark)
                break
            except ValueError:
                print('\n[!] ERRO: Digite um valor inteiro!\n')

    return np.array(x)


def pode_disparar(A_out, x, transicao):
    for p in range(x):
        if x[p] >= A_out[p][transicao]:
            return True
    return False


def disparo(A_out, A_in, x, t):
    x_next = list(x)
    for p_idx in range(len(x)):
        if x[p_idx] != float('inf'):
            x_next[p_idx] += A_in[p_idx][t] - A_out[p_idx][t]
    return tuple(x_next)



def main():
    transicoes, places = define_transicoes_places()
    A_out = define_matriz(places, transicoes)
    A_in = define_matriz(places, transicoes)
    x_ = initial_mark(places)


main()