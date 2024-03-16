#Classes and Objects and Constructors.

class Person_details:     # class
    def __init__(self, name, m1, m2, m3, m4):    #Parameterized Constructor.
        self.name = name
        self.math = m1
        self.Eng = m2
        self.SST = m3
        self.Hindi = m4

    def Percentage(self):             # compulsary to use Self in all functions present in class
        S = self.math + self.Eng + self.SST + self.Hindi
        P = (S/400)*100
        print(f"Percentage of {self.name} is {P}")

A = Person_details("Pankaj",50,60,75,89)    # Object 
A.Percentage()                              # Calling Function
B = Person_details("Sachin", 67,89,91,56)
B.Percentage()