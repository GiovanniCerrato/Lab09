from dataclasses import dataclass

@dataclass
class Arco:
    a1:int
    a2:int
    distanzaMediaPercorsa:float

    def __str__(self):
        return f"a1: {self.a1}, a2: {self.a2}, distanzaMedia: {self.distanzaMediaPercorsa}"