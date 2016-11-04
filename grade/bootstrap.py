# -*-coding:utf-8-*-

from models import Professor, Disciplina


disciplinas = [
    Disciplina(id=1, nome=u"ALGORITMOS ESTRUTURADOS", periodo=1, ch=2),
    Disciplina(id=2, nome=u"ARQUITETURA E ORGANIZAÇÃO DE COMPUTADORES", periodo=1, ch=1),
    Disciplina(id=3, nome=u"CÁLCULO PARA COMPUTAÇÃO", periodo=1, ch=2),
    Disciplina(id=4, nome=u"FILOSOFIA E ÉTICA", periodo=1, ch=1),
    Disciplina(id=5, nome=u"INTRODUÇÃO À COMPUTAÇÃO", periodo=1, ch=1),
    Disciplina(id=6, nome=u"PORTUGUÊS INSTRUMENTAL", periodo=1, ch=1),
    Disciplina(id=7, nome=u"REDES DE COMUNICAÇÃO", periodo=1, ch=2)
]
#
# Disciplinas
#

# 1o Período
# 1: Algoritmos Estruturados
# 2: Arquitetura e Organização de Computadores
# 3: Teoria Geral da Administração
# 4: Matemática Básica
# 5: Filosofia
# 6: Introdução à Computação

# 2o Período
# 7: Algoritmos e Linguagens de Programação
# 8:
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


rc = Professor(id=1, sigla='RC', ch_max=10, disciplinas=[1], preferencias=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
es = Professor(id=2, sigla='ES', ch_max=10, disciplinas=[2, 5], preferencias=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
br = Professor(id=3, sigla='BR', ch_max=8, disciplinas=[3], preferencias=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
cr = Professor(id=4, sigla='CR', ch_max=5, disciplinas=[4], preferencias=[[-1, 1, 1, -1, 1], [-1, -1, 1, -1, 1]])
ar = Professor(id=5, sigla='AR', ch_max=6, disciplinas=[6], preferencias=[[1, 1, 1, -1, -1], [1, 1, 1, -1, -1]])
dm = Professor(id=6, sigla='DM', ch_max=6, disciplinas=[7], preferencias=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])


professores = [
    rc, es, br, cr, ar, dm
]



class Bootstrap:

    def __init__(self):
        pass

    def get_disciplinas_por_periodo(self):
        disciplinas_ids = [[] for i in range(8)]

        for d in disciplinas:

            for i in range(d.ch):
                disciplinas_ids[d.periodo - 1].append(d.id)

        return disciplinas_ids

    def get_professores(self):
        return professores