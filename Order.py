from ctypes import addressof
from itertools import product
from uuid import uuid1
from Catalogue import Catalogue
from Bill import Bill
import json

class Order:
    currentId = -1
    def __init__(self, customerName, address, productList, paymentMethod, orderId = None):
        if orderId == None:
            Order.currentId+=1
            self.orderId = Order.currentId
        else:
            self.orderId = orderId

        self.customer = customerName
        self.address = address
        self.bill = Bill(paymentMethod)
        self.productList = productList
        self.isFullfilled = False

    def display(self):
        #print(json.dumps(self, indent=5, default=lambda o: o.__dict__))
        print(self.orderId,end="\t")
        print(self.isFullfilled)
        self.address.printAddress()
        for pro in self.productList:
            pro.displayProduct()

    def addOrderToSeller(self):
        dictionary = {}
        for product in self.productList:
            if product.seller.userName not in dictionary:
                list = []
                list.append(product)
                dictionary[product.seller.userName] = list
            else:
                dictionary[product.seller.userName].append(product)

        for seller in dictionary:
            order = Order(self.customer,self.address,dictionary[seller],self.bill.paymentMethod, self.orderId)
            dictionary[seller][0].seller.orderList.append(order)

    def createBill(self):
        return self.bill.fillBill(self)
        

    # def findInProductList(self,productName,sellerUserName):
    #     for product in self.productList:
    #         if product.name == productName and product.seller.userName == sellerUserName:
    #             if product.stock < 1:
    #                 return False, "Out of Stock"
    #             return True, product
    #     return False, "Product Not Found"


    # def updateQuantity(self,productName,sellerUserName,newQuantity):
    #     isProductExist, productFound = self.findInProductList(productName, sellerUserName)
    #     if isProductExist:
    #         productFound.productStock = newQuantity
    #         return True, productFound.productStock+ "is the updated stock"
    #     else:
    #         return False, "Product not found"

    # def deleteInProductList(self,productName,sellerUserName):
    #     isProductExist, productFound = self.findInProductList(productName,sellerUserName)
    #     if not isProductExist:
    #         return False, "Product does not exist"
        
    #     self.productList.remove(productFound)
    #     return True, productFound