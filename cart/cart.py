
from decimal import Decimal

from store.models import Product

class Cart():

    def __init__(self, request):

        self.session = request.session

    def __len__(self):

        return sum(item['qty'] for item in self.cart.values())
   
    def get_total(self):

        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())




  


