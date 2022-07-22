from Catalogue import Catalogue
from Product import Product

class Wishlist():
    def __init__(self):
        self.productList = []

    def findProductInWishlist(self,productName,sellerUserName):
            for product in self.productList:
                if product.productName == productName and product.seller.userName == sellerUserName:
                    return True, product
            return False, "Product Not Found"

    def deleteItem(self, productName, sellerUserName):
        isProductExist, productFound = self.findProductInWishlist(productName,sellerUserName)
        if not isProductExist:
            return False, "Product not found"
        self.productList.remove(productFound)
        return True, productFound

    def addItem(self, product):
        isProductExist, productFound = self.findProductInWishlist(product.productName,product.seller.userName)
        if isProductExist:
            return False, "Product Already Exist"
        self.productList.append(product)
        return True, "Product Added"