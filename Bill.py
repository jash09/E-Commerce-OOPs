from importlib.metadata import SelectableGroups
from uuid import uuid1
import json

class Bill:
    def __init__(self,paymentMethod):
        self.billId = str(uuid1())
        self.productNames = []
        self.prices = []
        self.quantity = []
        self.sellerName = None
        self.paymentMethod = paymentMethod
        self.totalBill = 0

    def fillBill(self, order):
        amount = 0

        for product in order.productList:
            self.productNames.append(product.productName)
            self.prices.append(product.productPrice)
            self.quantity.append(product.productStock)
            amount+= product.productStock*product.productPrice
        
        self.totalBill = amount
        self.sellerName = order.productList[0].seller.name

    def display(self):
        print(json.dumps(self, indent=5, default=lambda o: o.__dict__))
        