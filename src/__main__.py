from automato.automato_pilha import Automato
from automato.leitura import Leitura
from automato import defs
import os

#(a^n)(b^m)(a^(n + m)).txt
#(a^n)(b^n).txt
#(w)(w^r).txt

def imprime_processamento(processamento, estados, palavra):
    print('Aceitou: ', processamento[0])
    strproc = ''
    if processamento[0] == True:
        for p in range(len(processamento[1]) - 1):
            strproc += str(estados[processamento[1][p][0]].label) + '-->'
        strproc += str(estados[processamento[1][len(processamento[1]) - 1][0]].label)
        print(strproc)

def menu():
    executar = True
    while executar:
        print('Automato de Pilha\n-Obs: arquivos de entrada no formato foobar.txt')
        arq = input('Arquivo de descrição: ')
        l = Leitura(arq)
        estados_info, transicoes_info = l.get_info_automato()
        ap = Automato(estados_info, transicoes_info)
        processar = True
        while processar:
            palavra = input('Palavra: ')
            imprime_processamento(ap.processa_fita(palavra), ap.estados, palavra)
            opt = input('\n(1) Repetir, (2) Encerrar: ')
            if(opt == '1'):
                processar = True
            elif(opt == '2'):
                processar = False
        opt = input('(1) Outro arquivo de descrição, (2) Encerrar: ')
        if(opt == '1'):
            executar = True
        elif(opt == '2'):
            executar = False
        os.system('clear')

menu()