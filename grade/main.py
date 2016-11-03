# -*- coding:utf-8 -*-

from pyevolve import GSimpleGA
from pyevolve import Selectors

from genomes import G3DList

from random import shuffle, random, randint
from copy import copy

#
# Disciplinas
#

# 1o Período
# 1: Algoritmos Estruturados
# 2: Língua Portuguesa
# 3: Teoria Geral da Administração
# 4: Matemática Básica
# 5: Filosofia
# 6: Introdução à Computação

# 2o Período
# 7: Algoritmos e Linguagens de Programação
# 8: Arquitetura e Organização de Computadores
# 9: Cálculo
# 10: Contabilidade
# 11: Inglês Instrumental
# 12: Sociologia

# 3o Período
# 13: Administração da Produção
# 14: Análise de Sistemas
# 15: Estatística
# 16: Programação Orientada a Objetos
# 17: Sistemas Operacionais

# 4o Período
# 18: Administração de Sistemas Operacionais
# 19: Desenvolvimento de Sistemas Orientado a Objetos
# 20: Engenharia de Software
# 21: Estruturas de Dados
# 22: Redes de Comunicação

# 5o Período
# 23: Bancos de Dados
# 24: Desenvolvimento de Sistemas para Web
# 25: Direito Virtual
# 26: Gerência de Projetos de Software
# 27: Metodologia de Pesquisa Científica
# 28: Redes Wireless
# 29: Sistemas Distribuídos

# 6o Período
# 30: Administração de Bancos de Dados
# 31: Administração e Segurança de Redes
# 32: Comunicações Móveis
# 33: Governança em Tecnologia da Informação
# 34: Interface Homem-Máquina
# 35: Qualidade de Software
# 36: Segurança e Auditoria em Informática

# 7o Período
# 37: Computação Gráfica
# 38: Fundamentos de Hardware e Microcontroladores
# 39: Inteligência Artificial
# 40: Orientação de Estágio
# 41: Projeto Integrado
# 42: Sistemas Embarcados

# 8o Período
# 43: Administração de Comércio Eletrônico
# 44: Empreendedorismo
# 45: Infraestrutura de Tecnologia da Informação
# 46: Inovação e Novas Tecnologias
# 47: Optativa
# 48: Perícia em Informática
# 49: Processamento de Imagens
# 50: TCC

disciplinas = [
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 6],
    [7, 7, 8, 8, 9, 9, 10, 10, 11, 12],
    [13, 13, 14, 14, 15, 15, 16, 16, 17, 17],
    [18, 18, 19, 19, 20, 20, 21, 21, 22, 22],
    [23, 23, 24, 24, 25, 26, 26, 27, 28, 29],
    [30, 30, 31, 31, 32, 33, 33, 34, 35, 36],
    [37, 37, 38, 38, 39, 39, 40, 41, 42, 42],
    [43, 44, 44, 45, 46, 47, 48, 48, 49, 50]
]





def GradeInitializator(genome, **args):
    """ Inicialização da grade """

    for i in xrange(genome.getHeight()):
        d = copy(disciplinas[i])
        shuffle(d)

        for j in xrange(genome.getWidth()):
            for k in xrange(genome.getDepth()):
                genome.setItem(i, j, k, d.pop())


def G3DListCrossover(genome, **args):

    pc = 0.5

    sister = None
    brother = None
    gMom = args["mom"]
    gDad = args["dad"]

    # cut = randint(1, len(gMom) - 1)

    sister = gMom.clone()
    sister.resetStats()

    brother = gDad.clone()
    brother.resetStats()

    # Troca grades de períodos
    if random() < pc:
        index_grade = randint(1, brother.getDepth() - 1)

        sister[:][:][index_grade:] = gDad[:][:][index_grade:]
        brother[:][:][index_grade:] = gMom[:][:][index_grade:]

    return (sister, brother)



def G3DListMutatorSwap(genome, **args):

    if args["pmut"] <= 0.0: return 0

    height = genome.getHeight()
    width = genome.getWidth()
    depth = genome.getDepth()

    mutations = 0

    for i in range(height):
        for j in range(width):
            for k in range(depth):
                if random() < args["pmut"]:
                    index_a = (randint(0, height-1), randint(0, width-1))
                    index_b = (randint(0, height-1), randint(0, width-1))

                    tmp = genome.get(index_a[0], index_a[1], k)
                    genome.setItem(index_a[0], index_a[1], k, (genome.get(index_b[0], index_b[1], k)))
                    genome.setItem(index_b[0], index_b[1], k, tmp)

                    mutations += 1

    return int(mutations)


# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
def eval_func(chromosome):
    score = 1000.0

    for i in xrange(chromosome.getHeight()):
        test_list = copy(disciplinas[i])

        # iterate over the chromosome
        for j in xrange(chromosome.getWidth()):
            for k in xrange(chromosome.getDepth()):

                if j == 0 and chromosome.get(i, j, k) == chromosome.get(i, j+1, k):
                    score -= 0.1

                if j == 1 and chromosome.get(i, j, k) == chromosome.get(i, j-1, k):
                    score -= 0.1

                if test_list.__contains__(chromosome.get(i, j, k)):
                    test_list.remove(chromosome.get(i, j, k))
                else:
                    score -= 0.5


    score -= 0.5 * test_list.__len__()

    return score



# Genome instance
#genome = G2DList.G2DList(2, 5)
# G3DList(periodos, horarios_dia, dias_semana)
genome = G3DList(8, 2, 5)
genome.initializator.set(GradeInitializator)


#genome.setParams(rangemin=0, rangemax=10)

# The evaluator function (objective function)
genome.evaluator.set(eval_func)
#genome.crossover.set(Crossovers.G2DListCrossoverSingleHPoint)
genome.crossover.set(G3DListCrossover)
genome.mutator.set(G3DListMutatorSwap)
#genome.mutator.set(Mutators.G2DListMutatorIntegerGaussian)
#genome.mutator.set(Mutators.G2DListMutatorSwap)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)
ga.selector.set(Selectors.GRouletteWheel)
ga.setGenerations(1200)

# Do the evolution, with stats dump
# frequency of 10 generations
ga.evolve(freq_stats=100)

# Best individual
best =  ga.bestIndividual()

print best

best.printChromossome()