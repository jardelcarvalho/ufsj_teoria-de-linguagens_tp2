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

# (a^n)(b^n)
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
print(ap.processa_fita('aaaaabbbbb'))

# w(w^r)
# estados_info = []
# estados_info.append(Estado_info('q0', defs.INICIAL))
# estados_info.append(Estado_info('q1', defs.COMUM))
# estados_info.append(Estado_info('qf', defs.FINAL))
# transicoes_info = []
# transicoes_info.append(Transicao_info('q0', 'a', [], 'a', 'q0'))
# transicoes_info.append(Transicao_info('q0', 'b', [], 'b', 'q0'))
# transicoes_info.append(Transicao_info('q0', [], [], [], 'q1'))
# transicoes_info.append(Transicao_info('q1', 'a', 'a', [], 'q1'))
# transicoes_info.append(Transicao_info('q1', 'b', 'b', [], 'q1'))
# transicoes_info.append(Transicao_info('q1', defs.ACABOU, defs.ACABOU, [], 'qf'))
# ap = Automato(estados_info, transicoes_info)
# print(ap.processa_fita('aabbaa'))

# (a^n)(b^m)(a^(n + m))
# estados_info = []
# estados_info.append(Estado_info('q0', defs.INICIAL))
# estados_info.append(Estado_info('q1', defs.COMUM))
# estados_info.append(Estado_info('q2', defs.COMUM))
# estados_info.append(Estado_info('qf', defs.FINAL))
# transicoes_info = []
# transicoes_info.append(Transicao_info('q0', 'a', [], 'X', 'q0'))
# transicoes_info.append(Transicao_info('q0', [], [], [], 'q1'))
# transicoes_info.append(Transicao_info('q1', 'b', [], 'X', 'q1'))
# transicoes_info.append(Transicao_info('q1', [], [], [], 'q2'))
# transicoes_info.append(Transicao_info('q2', 'a', 'X', [], 'q2'))
# transicoes_info.append(Transicao_info('q2', defs.ACABOU, defs.ACABOU, [], 'qf'))
# ap = Automato(estados_info, transicoes_info)
# print(ap.processa_fita('abbaaa'))

for e in ap.estados:
    print(e.label)
    for t in e.adjacentes:
        print(t.fita, ', ', t.pilha, ', ', t.empilhar, ', ', t.dest)
    print('\n')