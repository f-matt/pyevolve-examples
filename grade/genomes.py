# -*- coding:utf-8 -*-

import numpy as np

from pyevolve.GenomeBase import GenomeBase

class G3DList(GenomeBase):

    def __init__(self, height, width, depth):

        GenomeBase.__init__(self)

        self.gens = np.zeros((height, width, depth))

        self.height = height
        self.width = width
        self.depth = depth


    def copy(self, g):
        """ Copy genome to 'g' """
        GenomeBase.copy(self, g)
        g.height = self.height
        g.width = self.width
        g.depth = self.depth


    def clone(self):
        """ Return a new instace copy of the genome """
        newcopy = G3DList(self.height, self.width, self.depth)
        self.copy(newcopy)
        return newcopy


    def setItem(self, i, j, k, item):
        self.gens[i, j, k] = item


    def get(self, i, j, k):
        return self.gens[i][j][k]


    def __getitem__(self, i):
        return self.gens[i]

    def printChromossome(self):
        print self.gens




    def getWidth(self):
        return self.width


    def getHeight(self):
        return self.height


    def getDepth(self):
        return self.depth
