
class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return ("My name is "+self.name+".")
    
#Case I Automatic Inheritance (No Child Constructor) 
"""Python automatically passes all initialization duties straight up to the parent."""
class Sub1(Super):
    pass  # No constructor written here

#Case II Standard Delegation (best practise)
"""child safely executes its own setup logic while ensuring the
 parent class gets to construct all its hidden variables, rules, and foundations."""
class Sub2(Super):
    def __init__(self,name):
        Super.__init__(self,name)          

# Case III Manual Assignment
""" child class completely overrides parent constructor runs without error but 
If the parent class ever updates its initialization rules in the future, the child will completely miss those updates. ."""
class Sub3(Super):
    def __init__(self,name):
        self.name=name

# Case IV Constructor Blindout
"""The program instantly crashes when print(obj) triggers. Because the child constructor did not call 
the parent and did not assign anything locally, the instance attribute name is never created in memory."""
class Sub4(Super):
    def __init__(self, name):
        pass

# Executing and testing
if __name__=='__main__':
    print("Testing Constructor Inhertitance possibilties")

    # testing Case I
    obj1=Sub1('John')
    print(obj1)
    #Testing Case II
    obj2=Sub2('Allen')
    print(obj2)
    # Testing Case III
    obj3=Sub3('Katy')
    print(obj3)
    #Testing case IV
    try:
     obj4=Sub4('Peter')
     print(obj4)
    except AttributeError as error:
        print(f'Success ! caught expected inhertance error:\n ')
