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
        print('Tudo tranquilo !')
        pass

    def processa_fita(self, fita):
        self.esvazia()
        fita_tam = len(fita)
        fita_usada = 0
        pilha_execucao = []
        pilha_execucao.append([self.inicial, 0, 0, self.estados[self.inicial].n])
        while pilha_execucao != []:
            c = pilha_execucao.pop()
            for i in range(c[2], c[3]):
                c[2] = i
                if c[1] > fita_usada:
                    fita_usada = c[1]
                adj = self.estados[c[0]].adjacentes[i]
                if c[1] < fita_tam:
                    if adj.fita == fita[c[1]]:
                        if adj.pilha == []:
                            pilha_execucao.append(c)
                            pilha_execucao.append([adj.dest, c[1] + 1, 0, self.estados[adj.dest].n])
                            self.empilha(adj.empilhar)
                        elif self.topo() == adj.pilha:
                            pilha_execucao.append(c)
                            pilha_execucao.append([adj.dest, c[1] + 1, 0, self.estados[adj.dest].n])
                            self.desempilha()
                            self.empilha(adj.empilhar)
                elif adj.fita == defs.ACABOU and adj.pilha == defs.ACABOU:
                    if self.pilha_vazia():
                        if self.estados[adj.dest].tipo == defs.FINAL:
                            pilha_execucao = []
                            print('Aceitou')
                        else:
                            pilha_execucao.append(c)
                            pilha_execucao.append([adj.dest, c[1], 0, self.estados[adj.dest].n])
            print('Pilha de execução: ', pilha_execucao)
            print('Pilha do automato: ', self.pilha, '\n')
            pass
        if self.pilha_vazia() and fita_tam == fita_usada:
            return True
        return False

# estado, simbolo, transicao_ini, transicao_fim