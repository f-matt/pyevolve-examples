import Tkinter

from random import choice
from pyevolve import GAllele
from pyevolve import G1DList
from pyevolve import Mutators
from pyevolve import Crossovers
from pyevolve import GSimpleGA
from pyevolve import Consts

from math import sqrt, pow

RADIUS = 3

points = []
canvas = None

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = chr(65 + len(points))

    def draw(self):
        canvas.create_oval(self.x - RADIUS, self.y - RADIUS, self.x + RADIUS, self.y + RADIUS, fill="blue")
        canvas.create_text(self.x, self.y - 3*RADIUS, text=self.label)

    def distanceTo(self, otherPoint):
        return sqrt(pow(self.x - otherPoint.x, 2) + pow(self.y - otherPoint.y, 2))


def tsp_initializator(genome, **args):
    genome.clearList()

    lst = [i for i in xrange(genome.getListSize())]

    for i in xrange(genome.getListSize()):
        ch = choice(lst)
        lst.remove(ch)
        genome.append(ch)


def eval_func(chromosome):

    d = 0
    for i in range(len(chromosome) - 1):
        d += points[chromosome[i]].distanceTo(points[chromosome[i+1]])

    return d


def canvas_click(event):
    p = Point(event.x, event.y)
    points.append(p)
    p.draw()



def solve():

    setOfAlleles = GAllele.GAlleles(homogeneous=True)
    lst = [i for i in xrange(len(points))]
    a = GAllele.GAlleleList(lst)
    setOfAlleles.add(a)

    genome = G1DList.G1DList(len(points))
    genome.setParams(allele=setOfAlleles)

    genome.evaluator.set(eval_func)
    genome.mutator.set(Mutators.G1DListMutatorSwap)
    genome.crossover.set(Crossovers.G1DListCrossoverOX)
    genome.initializator.set(tsp_initializator)

    ga = GSimpleGA.GSimpleGA(genome)
    ga.setGenerations(1000)
    ga.setMinimax(Consts.minimaxType["minimize"])
    ga.setCrossoverRate(1.0)
    ga.setMutationRate(0.03)
    ga.setPopulationSize(80)

    ga.evolve(freq_stats=100)
    best = ga.bestIndividual()

    best.append(best[0])
    for i in range(len(best) - 1):
        canvas.create_line(points[best[i]].x, points[best[i]].y, points[best[i+1]].x, points[best[i+1]].y)



if __name__ == "__main__":

    root = Tkinter.Tk()

    canvas = Tkinter.Canvas(root, width=500, height=500, bg="white")
    canvas.bind("<Button-1>", canvas_click)
    canvas.pack()

    btn_solve = Tkinter.Button(root, text="Solve!", command=solve)
    btn_solve.pack()

    root.mainloop()
