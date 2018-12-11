import os
from automato import defs

class Estado_info:
    def __init__(self, label, tipo):
        self.label = label
        self.tipo = tipo
        pass
    
class Transicao_info:
    def __init__(self, origem, fita, pilha, empilhar, dest):
        self. origem = origem
        self.fita = fita
        self.pilha = pilha
        self.empilhar = empilhar
        self.dest = dest
        pass

class Leitura:
    def __init__(self, arquivo):
        self.diretorio = os.path.abspath('../data') + '/' + arquivo
        
    
    def get_info_automato(self):
        arq = open(self.diretorio, 'r')
        linhas = arq.readlines()
        
        cabecalho = linhas[0]
        transicoes = linhas[1: ]
        
        cabecalho = cabecalho.split(' ')
        estados = cabecalho[0].split(',')
        inicial = cabecalho[1]
        finais = (cabecalho[2].split('\n')[0]).split(',')

        estados_info = []
        for e in estados:
            tipo = None
            if e == inicial:
                tipo = defs.INICIAL
            else:
                tipo = defs.COMUM
            for f in finais:
                if e == f:
                    if tipo == defs.INICIAL:
                        tipo = defs.INICIAL_FINAL
                    else:
                        tipo = defs.FINAL
            estados_info += [Estado_info(e, tipo)]

        transicoes_info = []
        for i in range(len(transicoes)):
            transicoes[i] = transicoes[i].split('\n')[0]
            t = transicoes[i].split(' ')
            origem = t[0]
            fita = t[1]
            if fita == '[]':
                fita = []
            elif fita == '?':
                fita = defs.ACABOU
            pilha = t[2]
            if pilha == '?':
                pilha = defs.ACABOU
            elif pilha == '[]':
                pilha = []
            empilhar = t[3]
            if empilhar == '[]':
                empilhar = []
            dest = t[4]
            transicoes_info += [Transicao_info(origem, fita, pilha, empilhar, dest)]
        
        arq.close()

        return estados_info, transicoes_info


            