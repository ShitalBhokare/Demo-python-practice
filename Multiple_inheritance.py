# This code demonstrates multiple inheritance in Python.
# Class C inherits from two parent classes: A and B.
# Class A has an attribute varA.
# Class B has an attribute varB.
# Class C has its own attribute varC.
# An instance c1 of class C can access varC directly.
# Additionally, c1 can access varB inherited from class B.
# Similarly, c1 can access varA inherited from class A.
# This shows how a child class can inherit attributes and methods from multiple parent classes.
# Python uses method resolution order (MRO) to determine the order of inheritance.


class A: 
    varA="Welcome to class A"
    
class B: 
     varB="Welcome to class B"
     
class C(A, B):
    varC="Welcome to class C"
    
c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)