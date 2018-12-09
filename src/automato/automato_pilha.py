from . import defs

class Estado:
    def __init__(self, label, tipo, adjacentes):
        self.label = label
        self.tipo = tipo
        self.adjacentes = adjacentes
        self.n = 0
        pass

class Transicao:
    def __init__(self, fita, pilha, empilhar, dest):
        self.fita = fita
        self.pilha = pilha
        self.empilhar = empilhar
        self.dest = dest
        pass

class Pilha:
    def __init__(self):
        self.pilha = []
        pass

    def pilha_vazia(self):
        return self.pilha == []

    def empilha(self, simbolo):
        if simbolo == []:
            return
        self.pilha.append(simbolo)
        pass
    
    def desempilha(self):
        if self.pilha == []:
            return []
        return self.pilha.pop()
    
    def topo(self):
        if self.pilha == []:
            return []
        return self.pilha[len(self.pilha) - 1]
    
    def esvazia(self):
        self.pilha = []
        pass

class Grafo:
    def __init__(self, estados_info, transicoes_info):
        if estados_info == [] or transicoes_info == []:
            pass
        self.estados = [Estado(e.label, e.tipo, []) for e in estados_info]
        for t in transicoes_info:
            for i in range(len(self.estados)):
                if t.origem == self.estados[i].label:
                    dest = None
                    for j in range(len(self.estados)):
                        if self.estados[j].label == t.dest:
                            dest = j
                            break
                    self.estados[i].adjacentes.append(Transicao(t.fita, t.pilha, t.empilhar, dest))
                    self.estados[i].n += 1
                    break
        pass

class Automato(Grafo, Pilha):
    def __init__(self, estados_info, transicoes_info):
        Grafo.__init__(self, estados_info, transicoes_info)
        Pilha.__init__(self)
        self.inicial = None
        for i in range(len(self.estados)):
            if self.estados[i].tipo == defs.INICIAL:
                self.inicial = i
                break
        pass

    def processa_fita(self, fita):
        self.esvazia()
        tam_fita, caminho, aceitou = len(fita), [], False
        pilha_execucao = [[self.inicial, 0, 0, self.estados[self.inicial].n, None, None, 0]]
        while pilha_execucao != []:
            e = pilha_execucao.pop()
            if e[4] != None:
                self.desempilha()
            if e[5] != None:
                self.empilha(e[5])
            
            # print('Pilha de execução: ', pilha_execucao)
            # print('Tirado da pilha: ', e)
            # print('Pilha do automato: ', self.pilha, '\n')
            celulas = []
            for i in range(e[2], e[3]):
                e[2] = e[2] + 1
                t = self.estados[e[0]].adjacentes[i]
                if e[1] < tam_fita:
                    if t.fita == fita[e[1]]:
                        if t.pilha == []:
                            celulas += [[t.dest, e[1] + 1, 0, self.estados[t.dest].n, None, t.empilhar, e[0]]]
                        elif t.pilha == self.topo():
                            celulas += [[t.dest, e[1] + 1, 0, self.estados[t.dest].n, self.topo(), t.empilhar, e[0]]]
                if t.fita == []:
                    if t.pilha == []:
                        celulas += [[t.dest, e[1], 0, self.estados[t.dest].n, None, t.empilhar, e[0]]]
                    elif t.pilha == self.topo():
                        celulas += [[t.dest, e[1], 0, self.estados[t.dest].n, self.topo(), t.empilhar, e[0]]]
                elif t.fita == defs.ACABOU and t.pilha == defs.ACABOU:                 
                    if self.pilha_vazia() and e[1] == tam_fita and self.estados[t.dest].tipo == defs.FINAL:
                        celulas += [[t.dest, e[1], 0, self.estados[t.dest].n, None, None, e[0]]]
                        caminho = pilha_execucao + [e] + celulas
                        pilha_execucao = []
                        celulas = []
                        aceitou = True
            if celulas != []:
                pilha_execucao += [e] + celulas
            else:
                if e[5] != None and e[5] != []:
                    self.desempilha()
                if e[4] != None:
                    self.empilha(e[4])
        return aceitou, caminho
        
# s, s
# s, []
# [], s
# [], []
# ??, ??