from uuid import uuid1
import json

class Product:
    def __init__(self,productName,productStock,productPrice, category, seller):
        self.productId = str(uuid1())
        self.productName = productName
        self.productStock = productStock
        self.productPrice = productPrice
        self.category = category
        self.seller = seller

    def displayProduct(self):
        #print(json.dumps(self, indent=5, default=lambda o: o.__dict__))
        print(self.productId,
                             "\t", self.productName,
                              "\t", self.productStock,
                              "\t",self.productPrice,
                              "\t",self.seller.userName,
                              "\t",self.category
                     )