from . import defs

"""
@Descrição: Módulo contendo classes para a construção
    de um automato de pilha.
@Classes: Estado, Transicao, Grafo, Pilha, Automato.
"""

class Estado:
    """
    @Descrição: Esta classe agrega os atributos que 
        correspondem a um estado de um automato.
    @Subclasses: Não possui.
    @Atributos:
        label: Nome do estado
        tipo: Tipo do estado (inicial, final, comum).
        adjacentes: Transições que saem do estado,
                são objetos da classe Transicao.
        n: Número de transições que saem do estado.
    """
    def __init__(self, label, tipo, adjacentes):
        """
        @Descrição: É o construtor da classe Estado.
            Recebe seus parâmetros de construtor
            e atribui às variáveis do objeto.
        @Parâmetros: 
            label: Nome do estado.
            tipo: Tipo do estado.
            adjacentes: Transições saindo do estado.
        @Retorno: Não possui.
        """
        self.label = label
        self.tipo = tipo
        self.adjacentes = adjacentes
        self.n = 0
        pass

class Transicao:
    """
    @Descrição: Esta classe armazena os atributos
        correspondentes a uma transição que sai de
        um estado do automato para outro.
    @Subclasses: Não possui.
    @Atributos:
        fita: Símbolo que deve ser satisfeito na
            fita para que a transição ocorra.
        pilha: Símbolo no topo da pilha que deve
            ser satisfeito para que a transição ocorra.
        empilhar: Símbolo que deve ser empilhado quando 
            a transição ocorrer.
        dest: Índice do estado de destino quando a 
            transição ocorrer.
    """
    def __init__(self, fita, pilha, empilhar, dest):
        """
        @Descrição: É o construtor da classe Transição.
            Recebe seus parâmetros de construtor
            e atribui às variáveis do objeto. 
        @Parâmetros:
            fita: Símbolo da fita a ser processado.
            pilha: Simbolo que deve ser desempilhado.
            empilhar: Símbolo a empilhar durante a transição.
            dest: Índice do estado de destino.
        @Retorno: Não possui.
        """
        self.fita = fita
        self.pilha = pilha
        self.empilhar = empilhar
        self.dest = dest
        pass

class Pilha:
    """
    @Descrição: Esta classe é uma representação
        de uma pilha para o automato de pilha.
    @Subclasses: Não possui.
    @Atributos:
        pilha: A pilha do automato.
    """
    def __init__(self):
        """
        @Descrição: Construtor da classe Pilha.
            Apenas define o atributo pilha como vazio.
        @Parâmetros: Não possui.
        @Retorno: Não possui.
        """
        self.pilha = []
        pass

    def pilha_vazia(self):
        """
        @Descrição: Retorna uma valor booleano indicando se
            a pilha está vazia.
        @Parâmetros: Não possui.
        @Retorno: Valor booleano (True/False)
        """
        return self.pilha == []

    def empilha(self, simbolo):
        """
        @Descrição: Recebe um símbolo como parâmetro e o 
            insere no topo da pilha.
        @Parâmetros: 
            simbolo: Símbolo a ser empilhado.
        @Retorno: Não possui.
        """
        if simbolo == []:
            return
        self.pilha.append(simbolo)
        pass

    def desempilha(self):
        """
        @Descrição: Remove o elemento existente no topo da pilha.
            Se a pilha estiver vazia, a função retorna vazio ([]).
        @Parâmetros: Não possui.
        @Retorno: Elemento removido do topo da pilha.
        """
        if self.pilha == []:
            return []
        return self.pilha.pop()

    def topo(self):
        """
        @Descrição: Retorna uma cópia do símbolo existente no topo
            da pilha sem remove-lo.
        @Parâmetros: Não possui.
        @Retorno: Cópia do elemento existente no topo da pilha.
        """
        if self.pilha == []:
            return []
        return self.pilha[len(self.pilha) - 1]

    def esvazia(self):
        """
        @Descrição: Esvazia toda a pilha.
        @Parâmetros: Não possui.
        @Retorno: Não possui.
        """
        self.pilha = []
        pass

class Grafo:
    """
    @Descrição: Esta classe é uma representação do grafo
        correspondente ao automato descrito.
    @Subclasses: Não possui.
    @Atributos:
        estados: todos os estados (vértices) do automato
        assim como as suas transições (arcos).
    """
    def __init__(self, estados_info, transicoes_info):
        """
        @Descrição: Construtor da classe Grafo.
            A partir dos atributos recebidos como parâmetro
            cria os estados e as transições que correspondem
            ao grafo do automato.
        @Parâmetros:
            estados_info: Lista de objetos do tipo Estado_info
                que armazenam as informações sobre os estados
                criados na interface e que farão parte da 
                topologia do automato.
            transicoes_info: Lista de objetos do tipo Transicoes_info
                que armazenam as informações correspondentes
                a todas as transições do automato que foram
                criadas na interface.
        @Retorno: Não possui.
        """
        # Verifica se as variáveis de parâmetro estão vazias (inválidas).
        if estados_info == [] or transicoes_info == []:
            pass
        self.estados = [Estado(e.label, e.tipo, []) for e in estados_info]
        
        # Percorre as transições e preenche os arcos (transições) no grafo nos respectivos vértices (estados).
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
    """
    @Descrição: Esta classe é uma abstração de um automato de pilha
        propriamente dito.
    @Subclasses: Grafo, Pilha
    @Atributos:
        inicial: Guarda o índice do estado inicial do automato.
    """
    def __init__(self, estados_info, transicoes_info):
        """
        @Descrição: Construtor da classe Automato.
            Chama contrutores das classes Grafo e Pilha
            passando seus respectivos atributos. 
            Procura o estado inicial e atribui o seu índice
            para o atributo "inicial".
        @Parâmetros:
            estados_info: Lista de objetos do tipo Estado_info
                que armazenam as informações sobre os estados
                criados na interface e que farão parte da 
                topologia do automato.
            transicoes_info: Lista de objetos do tipo Transicoes_info
                que armazenam as informações correspondentes
                a todas as transições do automato que foram
                criadas na interface.
        @Retorno: Não possui.
        """
        # Chama construtores das classes herdadas.
        Grafo.__init__(self, estados_info, transicoes_info)
        Pilha.__init__(self)
        self.inicial = None
        
        # Procura o estado inicial.
        for i in range(len(self.estados)):
            if self.estados[i].tipo == defs.INICIAL:
                self.inicial = i
                break
        pass

    def processa_fita(self, fita):
        """
        @Descrição: Recebe uma fita como parâmetro e realiza o processamento
            da mesma indicando se esta é aceita ou não.
        @Parâmetros: 
            fita: Fita a ser processada pelo automato de pilha.
        @Retorno: Retorna uma lista contendo um valor booleano (aceita) 
            e uma lista de transições (celula) indicando o caminho percorrido
            no grafo do automato.
            Condições de retorno para aceita e celulas ([aceita, celulas]):
                aceita | celulas | retorno = [aceita, celulas]
                True   | [[x, x, x, x, x, x, x], ... , [x, x, x, x, x, x, x]]
                False  | [[]]    
        """
        # Esvazia a pilha do automato.
        self.esvazia()
        tam_fita, caminho, aceitou = len(fita), [], False

        # pilha_execução = [estado atual, 
        #                   posição na fita, 
        #                   índice do estado adjacente, 
        #                   numero de adjacentes, 
        #                   item desempilhado, 
        #                   item a empilhar, 
        #                   índide do estado de origem]
        pilha_execucao = [[self.inicial, 0, 0, self.estados[self.inicial].n, None, None, 0]]
        while pilha_execucao != []:
            # Remove um elemento da pilha de execução
            e = pilha_execucao.pop()
            # Executa operações pendentes
            if e[4] != None:
                self.desempilha()
            if e[5] != None:
                self.empilha(e[5])
            celulas = []
            for i in range(e[2], e[3]):
                e[2] = e[2] + 1
                # Seleciona a transição "i" a partir do estado de origem em "e[0]".
                t = self.estados[e[0]].adjacentes[i]
                # Verifica se a fita ainda não está no final.
                if e[1] < tam_fita:
                    # Se não está no final verificar se o símbolo da fita bate com o da transição.
                    if t.fita == fita[e[1]]:
                        # Se o símbolo da fita bater, verificar se o símbolo da pilha também bate.
                        # Caso algum desvio condicional seja satisfeito anexar as informações da iteração
                        #   atual na pilha de execução.
                        if t.pilha == []:
                            celulas += [[t.dest, e[1] + 1, 0, self.estados[t.dest].n, None, t.empilhar, e[0]]]
                        elif t.pilha == self.topo():
                            celulas += [[t.dest, e[1] + 1, 0, self.estados[t.dest].n, self.topo(), t.empilhar, e[0]]]
                # Verifica se existe um movimento vazio para o símbolo da fita na transição atual.
                if t.fita == []:
                    # Se existe, realizar o mesmo para o símbolo da pilha da transição atual.
                    # Caso algum desvio condicional seja satisfeito anexar as informações da iteração
                    #   atual na pilha de execução.
                    if t.pilha == []:
                        celulas += [[t.dest, e[1], 0, self.estados[t.dest].n, None, t.empilhar, e[0]]]
                    elif t.pilha == self.topo():
                        celulas += [[t.dest, e[1], 0, self.estados[t.dest].n, self.topo(), t.empilhar, e[0]]]
                elif t.fita == defs.ACABOU and t.pilha == defs.ACABOU:
                    # Verifica se existe uma transição de finalização da execução para a iteração
                    #   atual.
                    if self.pilha_vazia() and e[1] == tam_fita and self.estados[t.dest].tipo == defs.FINAL:
                        # Se existe, verificar se a pilha está vazia, se a fita acabou e se o estado de
                        #   destino é um estado final.
                        # Entrando neste escopo é possível afirmar que a fita foi aceita.
                        # Realizando atribuições para finalização da execução.
                        celulas += [[t.dest, e[1], 0, self.estados[t.dest].n, None, None, e[0]]]
                        caminho = pilha_execucao + [e] + celulas
                        pilha_execucao = []
                        celulas = []
                        aceitou = True
            # Se existe uma transição que satisfaça o símbolo da fita e do topo da pilha.
            # Senão, realizar o backtracking e continuar a execução.
            if celulas != []:
                # Adicionar nova transição a pilha de execução.
                pilha_execucao += [e] + celulas
            else:
                # Backtracking
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
