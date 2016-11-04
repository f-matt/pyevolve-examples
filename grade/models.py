# -*- coding:utf-8 -*-

from copy import copy
from genomes import G3DList

import numpy as np


class Disciplina(object):

    def __init__(self, id, nome, periodo, ch):
        self.id = id
        self.nome = nome
        self.periodo = periodo
        self.ch = ch




class Professor(object):

    def __init__(self, id, sigla, ch_max, disciplinas, preferencias):
        self.id = id
        self.sigla = sigla
        self.ch_max = ch_max
        self.disciplinas = copy(disciplinas)
        self.preferencias = copy(preferencias)

    def calculaAptidao(self, grade):

        aptidao = 0

        grade_professor = np.zeros((2, 5))

        for d in self.disciplinas:

            horarios = grade.get_horarios_disciplina(d)

            for h in horarios:
                i = h[0]
                j = h[1]

                if grade_professor[i][j] != 0:
                    aptidao -= 0.5

                grade_professor[i][j] += 1

        return aptidao

        # TODO
        # Verificar preferencia


