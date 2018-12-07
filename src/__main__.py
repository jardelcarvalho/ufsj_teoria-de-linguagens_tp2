from automato.automato_pilha import Automato
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

estados_info = []
estados_info.append(Estado_info('q0', defs.INICIAL))
estados_info.append(Estado_info('q1', defs.COMUM))
estados_info.append(Estado_info('qf', defs.FINAL))
transicoes_info = []
transicoes_info.append(Transicao_info('q0', 'a', [], 'B', 'q0'))
transicoes_info.append(Transicao_info('q0', 'b', 'B', [], 'q1'))
transicoes_info.append(Transicao_info('q1', 'b', 'B', [], 'q1'))
transicoes_info.append(Transicao_info('q1', defs.ACABOU, defs.ACABOU, [], 'qf'))
transicoes_info.append(Transicao_info('q0', defs.ACABOU, defs.ACABOU, [], 'qf'))
ap = Automato(estados_info, transicoes_info)

for e in ap.estados:
    print(e.label)
    for t in e.adjacentes:
        print(t.fita, ', ', t.pilha, ', ', t.empilhar, ', ', t.dest)
    print('\n')

print(ap.processa_fita('aaaabbbb'))