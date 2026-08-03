class PaymentMethod:
    def __init__(self,amount):
        self.amount=amount
    def process_payment(self):
        # This forces child classes to override this method.
        # If they don't, Python will throw an error when called.
        raise NotImplementedError( 'Hey you forgot to write this method ')

class CreditcardPayment(PaymentMethod):
    def process_payment(self):
        print(f'Processing credit card payment of ${self.amount} (2% fee applied).')

class PayPalmethod(PaymentMethod):
    def process_payment(self):
      print(f'Logging into PayPal... Processing payment of {self.amount}..')

class BitcoiPayment(PaymentMethod):
    def process_payment(self):
        print(f'Verifying blockchain wallet... Transferring {self.amount} BTC.')

# Creating class where we intentionally forget to write the process _payment method to test NotImplementedError
class StripePayment(PaymentMethod):
    pass        # pass leaves th class completely blank

           
  # Polymorphic function          
def execute_checkout(payment_object):
      payment_object. process_payment()

# Creating objects for each class
C1=CreditcardPayment(1000)
P1=PayPalmethod(2000)
B1=BitcoiPayment(3000)
S1=StripePayment(5000)          # broken object

#Looping through list to watch polymorphism
payment=[C1,P1,B1,S1]
for n in payment:
   execute_checkout(n)