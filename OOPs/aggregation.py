class Professor:
    def __init__(self, professor_name, subject):
        self.professor_name = professor_name
        self.subject = subject
    
    def teach(self):
        print(f"{self.professor_name} teaches {self.subject}")

class University:
    def __init__(self, uni_name):
        self.uni_name = uni_name
        self.professors = []
        
    def add_professor(self, professor):
        self.professors.append(professor)
        
    def show_professors(self):
        print(f"Professors at {self.uni_name}:")
        for professor in self.professors:
            print(f"- {professor.professor_name}")
        
        
if __name__ =="__main__":
    prof1 = Professor("Sreeram Aasam", "Python")
    prof2 = Professor("Deepak", "java")
    
    university = University("SRM University")
    university.add_professor(prof1)
    university.add_professor(prof2)
    
    university.show_professors()

    prof1.teach()
    prof2.teach()