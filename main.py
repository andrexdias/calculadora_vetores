# -*- coding: utf-8 -*-

"""
:file main.py
:brief Projeto mae do ficheiro.
:details Importar tudo .
"""

import math
import itertools

def validar_entrada(valor):
    """
    Valida se o valor está no intervalo permitido (9 a 28).
    """
    return 9 <= valor <= 28

def calcular_raiz_quadrada(vetor):
    """
    Calcula a raiz quadrada de todos os elementos no vetor.
    """
    return [math.sqrt(valor) for valor in vetor]

def identificar_minimo(vetor):
    """
    Identifica o mínimo de todos os elementos do vetor.
    """
    return min(vetor)

def valores_posicoes_multiplos_tres(vetor):
    """
    Retorna os valores em posições múltiplas de três do vetor.
    """
    return [vetor[i] for i in range(0, len(vetor), 3)]

def vetor_segunda_metade_ordenada(vetor):
    """
    Retorna o vetor com a segunda metade dos valores ordenada por ordem crescente.
    """
    meio = len(vetor) // 2
    return vetor[:meio] + sorted(vetor[meio:])

def divisao_elementos_por_2(vetor):
    """
    Calcula a divisão de todos os elementos no vetor por 2.
    """
    return [valor / 2 for valor in vetor]

def construir_matriz_permutacoes(vetor):
    """
    Constrói uma matriz 14x14 com permutações dos valores do vetor.
    """
    matriz = [vetor] + list(itertools.permutations(vetor))
    return matriz

def main():
    """
    Função principal que interage com o usuário.
    """
    vetor = []

    # Pedir ao usuário 14 números inteiros
    for i in range(14):
        while True:
            try:
                valor = int(input(f"Digite o {i+1}º número (entre 9 e 28): "))
                if validar_entrada(valor):
                    vetor.append(valor)
                    break
                else:
                    print("Valor fora do intervalo permitido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Tente novamente.")

    while True:
        # Mostrar menu ao usuário
        print("\nMenu:")
        print("1 - Cálculo da raiz quadrada de todos os elementos no vetor")
        print("2 - Identificação do mínimo de todos os elementos do vetor")
        print("3 - Devolução dos valores em posições múltiplas de três do vetor")
        print("4 - Devolução do vetor, com a segunda metade dos valores ordenada por ordem crescente")
        print("5 - Cálculo da divisão de todos os elementos no vetor por 2")
        print("6 - Construção de uma matriz 14 por 14 com permutações dos valores do vetor")
        print("0 - Abrir menu mais completo.")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Resultado:", calcular_raiz_quadrada(vetor))
        elif escolha == "2":
            print("Resultado:", identificar_minimo(vetor))
        elif escolha == "3":
            print("Resultado:", valores_posicoes_multiplos_tres(vetor))
        elif escolha == "4":
            print("Resultado:", vetor_segunda_metade_ordenada(vetor))
        elif escolha == "5":
            print("Resultado:", divisao_elementos_por_2(vetor))
        elif escolha == "6":
            print("Resultado:")
            for linha in construir_matriz_permutacoes(vetor):
                print(linha)
        elif escolha == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

def misturar_vetores(vetor1, vetor2):
    """
    Mistura metade do primeiro vetor com metade do segundo vetor.
    """
    meio1 = len(vetor1) // 2
    meio2 = len(vetor2) // 2
    return vetor1[:meio1] + vetor2[meio2:]

def numeros_compostos(vetor):
    """
    Identifica todos os números compostos (não primos) no vetor inicial.
    """
    compostos = [valor for valor in vetor if any(valor % i == 0 for i in range(2, valor))]
    return compostos

def produto_matriz(vetor1, vetor2):
    """
    Calcula e retorna a matriz resultante do produto do vetor1 com o vetor2.
    """
    matriz = [[a * b for b in vetor2] for a in vetor1]
    return matriz

def matriz_transposta(matriz):
    """
    Calcula e retorna a matriz transposta da matriz fornecida.
    """
    transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return transposta

def ajuda():
    """
    Apresenta uma página de ajuda com informações sobre o programa.
    """
    print("\nBem-vindo ao Programa de Estatísticas!")
    print("Este programa permite calcular várias estatísticas e realizar operações com vetores.")
    print("Menu de Ajuda:")
    # Adicione informações adicionais conforme necessário.

if __name__ == "__main__":
    # (Continuação do código anterior)

    while True:
        # Mostrar menu ao usuário
        print("\nMenu:")
        print("1 - Cálculo da raiz quadrada de todos os elementos no vetor")
        print("2 - Identificação do mínimo de todos os elementos do vetor")
        print("3 - Devolução dos valores em posições múltiplas de três do vetor")
        print("4 - Devolução do vetor, com a segunda metade dos valores ordenada por ordem crescente")
        print("5 - Cálculo da divisão de todos os elementos no vetor por 2")
        print("6 - Construção de uma matriz 14 por 14 com permutações dos valores do vetor")
        print("7 - Leitura de um novo vetor e devolução de um vetor que mistura metade do primeiro vetor e metade do segundo")
        print("8 - Identificação de todos os números compostos no vetor inicial")
        print("9 - Leitura de um novo vetor 1x14, cálculo e devolução da matriz 14x14 resultante do produto do vetor inicial com o novo vetor gerado")
        print("10 - Cálculo e apresentação da matriz transposta referida no ponto anterior")
        print("11 - Ajuda")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "7":
            novo_vetor = []
            for i in range(14):
                while True:
                    try:
                        valor = int(input(f"Digite o {i + 1}º número para o novo vetor (entre 9 e 28): "))
                        if validar_entrada(valor):
                            novo_vetor.append(valor)
                            break
                        else:
                            print("Valor fora do intervalo permitido. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Tente novamente.")
            print("Resultado:", misturar_vetores(vetor, novo_vetor))
        elif escolha == "8":
            print("Resultado:", numeros_compostos(vetor))
        elif escolha == "9":
            novo_vetor = []
            for i in range(14):
                while True:
                    try:
                        valor = int(input(f"Digite o {i + 1}º número para o novo vetor (entre 9 e 28): "))
                        if validar_entrada(valor):
                            novo_vetor.append(valor)
                            break
                        else:
                            print("Valor fora do intervalo permitido. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Tente novamente.")
            resultado_matriz = produto_matriz(vetor, novo_vetor)
            print("Resultado:")
            for linha in resultado_matriz:
                print(linha)
        elif escolha == "10":
            resultado_transposta = matriz_transposta(resultado_matriz)
            print("Matriz Transposta:")
            for linha in resultado_transposta:
                print(linha)
        elif escolha == "11":
            print("Olá, tem que inserir 14 números inteiros entre 9 e 28, e depois selecionar qual opção que quer.")
        elif escolha == "0":
            print("Programa encerrado. Obrigado por usar.😊")
            break
        else:
            print("Opção inválida. Tente novamente.")
