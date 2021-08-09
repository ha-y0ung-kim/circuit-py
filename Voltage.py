from typing import Union


numeric = Union[int, float]


class Node:
    def __init__(self):
        self.V: numeric


class Element:
    def __init__(self, n1: Node, n2: Node):
        self.n1 = n1
        self.n2 = n2


class Resistor(Element):
    def __init__(self, n1: Node, n2: Node, R):
        super.__init__(n1, n2)
        # node1, node2, resistance
        self.R = R
        self.set_current()

    def set_current(self):
        self.I = (self.n1.V-self.n2.V)/self.R


class Vsource(Element):
    def __init__(self, n1: Node, n2: Node, V):
        super.__init__(n1, n2)
        # node1, node2, Voltage
        self.set_voltage(V)

    def set_voltage(self, V):
        self.n2.V = self.n1.V + V


class Ground:
    def __init__(self, n: Node):
        self.n = n
        self.set_ground(n)

    def set_ground(self, n: Node):
        self.n.V = 0


n1 = Node()
n2 = Node()

G = Ground(n1)
Vs = Vsource(n1, n2, 5)
Res = Resistor(n2, n1, 2.5)
print(Res.I)
