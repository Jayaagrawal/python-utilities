class Package():
    def __init__(self,weight):
        #Initializes a package with its weight in kg"
        self.weight=weight

    def calculate_cost(self):
        # calculate base shipping based on Rs 100/kg
        return self.weight*100
    
#The first child without super (causes a crash)

class StandardExpress(Package):
    def calculate_cost(self):
        express_fee=50
        return self.calculate_cost()+express_fee
        
# the Second child with super (runs perfectely)
class PriorityExpress(Package):
    def calculate_cost(self):
        express_fee=150
        # safely grabs the calcualtion from parent class
        base_cost=super().calculate_cost()
        return base_cost+express_fee

# Execution block
if __name__=='__main__':
    print('Testing Shipping charges options')

    # Test 1 Base class 
    base_pck=Package(weight=3)
    print(f'Base Package cost (3kg):              {base_pck.calculate_cost()}')

    """# Test 2 Crash case without super
    print("Testing cost calculation without super")
    broken_pck=StandardExpress(weight=3)
    try:
        # The loop happens here ,crashes and is cleanly caught in one place! 
        print(broken_pck.calculate_cost())    
    except RecursionError:
        # catching the error
        print("Success!Caught expected crash")"""
            
    # Test 3 Test Success Case with super
    priority_pck=PriorityExpress(weight=3)
    print(f'Priority package cost (with Super):{priority_pck.calculate_cost()}')

