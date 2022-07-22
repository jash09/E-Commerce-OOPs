from Catalogue import Catalogue
from Product import Product

class Cart:
    def __init__(self):
        self.productList = []

    def findProductInCart(self,productName,sellerUserName):
            for product in self.productList:
                if product.productName == productName and product.seller.userName == sellerUserName:
                    if product.productStock < 1:
                        return False, "Out of Stock"
                return True, product
            return False, "Product Not Found"
        
    def updateQuantity(self, productName, sellerUserName, newQuantity):
        isProductExist, productFound = self.findProductInCart(productName,sellerUserName)
        if not isProductExist:
            return False, "Product not found"
        productFound.productStock = newQuantity
        return True, str(productFound.productStock)+"is the updated stock"

    def deleteItem(self, productName, sellerUserName):
        isProductExist, productFound = self.findProductInCart(productName,sellerUserName)
        if not isProductExist:
            return False, "Product not found"
        self.productList.remove(productFound)
        return True, productFound

    def addItem(self, product):
        isProductExist, productFound = self.findProductInCart(product.productName,product.seller.userName)
        if isProductExist:
            return False, "Product Already Exist"
        self.productList.append(product)