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

    return tuple(x)


def pode_disparar(A_out, x, transicao):
    for p in range(len(x)):
        if x[p] < A_out[p][transicao]:
            return False
    return True


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

    queue = [x_]
    visited = {x_}
    edges = []
    ancestors = {x_: None}

    while queue:
        current_mrk = queue.pop(0)

        for t in range(transicoes):
            if pode_disparar(A_out, current_mrk, t):
                next_x = disparo(A_out, A_in, current_mrk, t)

                prox_mark = list(next_x)
                father = current_mrk

                while father is not None:
                    if all(prox_mark[i] >= father[i] for i in range(places)) and any(prox_mark[i] > father[i] for i in range(places)):
                        for j in range(places):
                            if prox_mark[j] > father[j]:
                                prox_mark[j] = float('inf')
                    father = ancestors.get(father)

                next_x = tuple(prox_mark)
                edges.append((current_mrk, f'{t + 1}', next_x))

                if next_x not in visited:
                    visited.add(next_x)
                    ancestors[next_x] = current_mrk
                    queue.append(next_x)

    print("\n--- Árvore de Cobertura Final ---")
    if not edges:
        print("Nenhuma transição habilitada")

    for x, trans, x_prime in edges:
        # Função para limpar a marcação: remove np.float, converte inf para ω e remove .0
        def limpar_marcacao(m):
            elementos = []
            for val in m:
                if val == float('inf'):
                    elementos.append('ω')
                else:
                    # int(val) remove o .0 e o rótulo do numpy
                    elementos.append(str(int(val)))
            return "(" + ", ".join(elementos) + ")"

        print(f"{limpar_marcacao(x)} --({trans})--> {limpar_marcacao(x_prime)}")


main()