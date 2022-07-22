from math import prod

class Catalogue():
    allProducts = []
    def __init__(self, admin, categoryName):
        admin = admin
        self.categoryName = categoryName
        self.productList = []

    @staticmethod
    def findCategory(categoryName):
        for category in Catalogue.allProducts :
            if category.categoryName == categoryName:
                return True, category
        return False, None
        
    # @staticmethod
    # def addCatalogue(categoryName):
    #     isCategoryExist, categoryFound = Catalogue.findCategory(categoryName)
    #     if isCategoryExist:
    #         return False, "Category Already Present"

    #     category = Catalogue(categoryName)
    #     Catalogue.allProducts.append(category)
    #     return True, "Category Added"
    
    @staticmethod
    def findProductInCategory(categoryName, productName, sellerUserName):
        isCategoryExist, category = Catalogue.findCategory(categoryName)
        if not isCategoryExist:
            return False, "Category Not Found"
        isProductExist, product = category.findProduct(productName, sellerUserName)
        if not isProductExist:
            return False, "Product Not Found"
        return True, product

    @staticmethod
    def getSellersProducts(sellerUserName):
        productList = []
        for category in Catalogue.allProducts:
            for product in category.productList:
                if product.seller.userName == sellerUserName:
                    productList.append(product)
        return True, productList

    def findProduct(self, productName, sellerUserName):
        for product in self.productList:
            if product.productName == productName and product.seller.userName == sellerUserName:
                if product.productStock < 1:
                    return False, "Out of Stock"
                return True, product
        return False, "Product Not Found"

    def addProduct(self, product):
        
        isProductExist, productFound = self.findProduct(product.productName, product.seller.userName)
        if isProductExist:
            return False, "Product Already Present"
        
        self.productList.append(product)
        return True, "Product Added"