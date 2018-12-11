#TP2 - Automato de Pilha
#Jardel Carvalho, Mariana Lellis

# Dependências
## Python 3.6.7
## GCC 8.2.0

#Módulos
## __main__.py: é o módulo principal onde ocorre todas as subchamadas e é onde o menu é implementado.
## leitura.py: é o módulo onde são efetuadas as operações de leitura dos arquivos contidos em data/
## automato_pilha.py: é onde ocorre a montagem do automato e o processamento das palavras de entrada.
## defs.py: contém variáveis globais utilizadas por todos os módulos implementados.

#Execução
## Para executar o programa basta digitar no seu terminal o seguinte comando sem aspas: "python3 __main__.py". Lembrando que caso se esteja em um diretório deve-se inserir o subcaminho até o módulo principal __main__.py.

#/data
## O diretório /data é onde os automatos a serem utilizados pelo programa devem estar. Estes automatos são especificados por meio de um arquivo .txt

#/data/*.txt
## Abaixo será descrito como deve ser o corpo dos arquivos contidos em /data:
## ->Primeira linha(Descrição dos estados): q0,q1,...,qn q0 q1,...,qn
## Repare que cada item desta linha é separado por espaços. O primeiro item, q0,q1,...,qn, consiste no conjunto de todos os estados existentes no automato. O segundo item, q0, consiste no estado inicial. O terceiro item, q1,...,qn, consiste no conjunto de estados finais.
## Cada conjunto de estados deve ser separado somente por virgulas, já os ítens precisam ser separados por espaços.
## ->Demais linhas(Transições): qx t u v qy
## Repare que qx é o estado de partida, t é o símbolo da fita, u é o símbolo da pilha, v é o símbolo a empilhar e qy é o estado de destino para a transição.

# Símbolo vazio
## Para representar 'vazio' no automato foi utilizado os símbolos de lista vazia, [], do Python.

# Fim de Fita e Pilha Vazia
## Para representar uma transição que necessita da verificação de uma fita ou pilha vazia foi utilizado o caractere ?.

# Exemplo
## Abaixo segue um exemplo de um automato que processa palavras do tipo (a^n)(b^n) | n>=0
q0,q1,qf q0 qf

q0 a [] B q0

q0 b B [] q1

q1 b B [] q1

q1 ? ? [] qf

q0 ? ? [] qf
