from abc import ABC, abstractmethod
import copy

# Prototype interface

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        ...
        
# Concrete prototype class

class Cell(Prototype):
    def __init__(self, dna: str, cell_type: str, age: int):
        self.dna = dna
        self.cell_type = cell_type
        self.age = age
        self.organs = ["nucleas", "mitochondria", "ribosome"]
        
    def clone(self):
        return copy.deepcopy(self)
    
    def mutate(self, new_dna: str):
        self.dna = new_dna
        
    def __str__(self):
        return f"Cell(type={self.cell_type}, age={self.age}, dna={self.dna}, organs={self.organs})"
    


# Client Code

if __name__ == "__main__":
    # Original Prototype
    
    original_cell = Cell(dna = "ATGC", cell_type = "stem", age = 1)
    print("Original Cell: ", original_cell)
    
    #Cloning the prototype
    clone1 = original_cell.clone()
    clone1.age += 1
    clone1.mutate("ATGA")
    print("Clone 1: ", clone1)
    
    clone2 = clone1.clone()
    clone2.age += 2
    clone2.mutate("ATGC")
    clone2.organs.append("Chloroplast")
    print("Clone 2: ", clone2)