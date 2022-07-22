from hashlib import new
from Catalogue import Catalogue
from Product import Product
from User import User
class Seller(User):
    def __init__(self, userName, name, age, gender, address = None):
        super().__init__(userName, name, age, gender)
        self.orderList = []
        self.address = address

    def displayOrderList(self):
        for order in self.orderList:
            order.display()

    def createProduct(self, productName, productStock, productPrice, category):
        isCategoryExist, categoryFound = Catalogue.findCategory(category)
        
        if not isCategoryExist:
            return False, "Category Not Found"
        isProductExist, product = categoryFound.findProduct(productName,self.userName)
        if isProductExist:
            return False, "Product Already Exist"
        
        
        product = Product(productName, productStock, productPrice, category, self)
        categoryFound.addProduct(product)
        
        return True, "Product Added"

    def displaySellerProductList(self):
        isProductList, sellerProductList = Catalogue.getSellersProducts(self.userName)
        if isProductList:
            for product in sellerProductList:
                product.displayProduct()
        else:
            return print("Cannot generate product list for seller")
        
    def updatePrice(self,productName,newPrice):
        isProductList, sellerProductList = Catalogue.getSellersProducts(self.userName)
        if not isProductList:
            return False, "Not Found"

        for product in sellerProductList:
            if product.productName == productName:
                product.productPrice = newPrice
                return True, print(product.productPrice,"is the updated price") 
        else:
            return False, print("Product not found")
        
    def getStock(self, productName):
        isProductList, sellerProductList = Catalogue.getSellersProducts(self.userName)
        if not isProductList:
            return False, "Not Found"

        for product in sellerProductList:
            if product.productName == productName:
                return True, product.productStock
        return False, "Product not found"

    def updateStock(self,productName,newStock):
        isProductList, sellerProductList = Catalogue.getSellersProducts(self.userName)
        if not isProductList:
            return False, "Not Found"

        for product in sellerProductList:
            if product.productName == productName:
                product.productStock = newStock
                return True, product.productStock,"is the updated stock"
        else:
            return False, "Product not found"

    def findOrderInOrderList(self,orderId):
        for order in self.orderList:
            if order.orderId == orderId:
                return True, order
        return False, "Order Id not present in order list"

    def cancelOrder(self,id):
        isOrderExist, order = self.findOrderInOrderList(id)
        if not isOrderExist:
            return False, "Order Not Found"
        self.orderList.remove(order)
        return True, "Cancelled"

    def fullfillOrder(self,orderId):
        isOrderExist, orderFound =  self.findOrderInOrderList(orderId)  
        if not isOrderExist:
            return False, "Order Not Found"
        orderFound.isFullfilled = True
        orderFound.createBill()
        print("------ Bill ------")
        orderFound.bill.display()
        return True, "Fullfiled"
    