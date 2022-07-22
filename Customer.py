import copy
from email import message
import imp
from math import prod
from unittest import addModuleCleanup
from Order import Order
from User import User
from Catalogue import Catalogue
from Address import Address
from Cart import Cart
from Wishlist import Wishlist

class Customer(User):
    def __init__(self, userName, name, age, gender):
        super().__init__(userName, name, age, gender)
        self.cart = Cart()
        self.addresses = []
        self.wishlist = Wishlist()
        self.orderList = []

    def printAllProducts(self):
        for category in Catalogue.allProducts:
            print(category.categoryName)
            for product in category.productList:
                product.displayProduct()

    def printWishlist(self):
        for product in self.wishlist.productList:
                product.displayProduct()

    def printCart(self):
        for product in self.cart.productList:
                product.displayProduct()

    def printProductListForCategory(self, categoryName):
        isCategoryExist, categoryFound = Catalogue.findCategory(categoryName)
        if not isCategoryExist:
            print("Category Not Found")
            
        for product in categoryFound.productList:
            product.displayProduct()

    
    def findAddress(self,label):
        for address in self.addresses:
            if address.label == label:
                return True, address
        return False, "Address not found"

    def addAddress(self, label, name, houseNo, street, city, pinCode, contact):
        isAddressExist, address = self.findAddress(label)
        if isAddressExist:
            return False, "Address with same label already exist"

        address = Address(label, name, houseNo, street, city, pinCode, contact)
        self.addresses.append(address)
        return True, "Address Added"
    
    def updateAddress(self, label, name, houseNo, street, city, pinCode, contact):
        isAddressExist, address = self.findAddress(label)
        if not isAddressExist:
            return False, "Address with given label not found"
        address.name = name
        address.houseNo = houseNo
        address.street = street
        address.city = city
        address.pinCode = pinCode
        address.contact = contact
        return True, "Address Updated"
    
    def deleteAddress(self, label):
        isAddressExist, address = self.findAddress(label)
        if not isAddressExist:
            return False, "Address with given label not found"
        self.addresses.remove(address)
        return True, "Address Deleted"
    

    def printAddressByLabel(self,label):
        isAddressExist, addressFound = self.findAddress(label)
        if not isAddressExist:
            return False, "Address not found"
        addressFound.printAddress()
        return True, None

    def printAllAddresses(self):
        for address in self.addresses:
            address.printAddress()
    
    def addToCart(self, categoryName, productName, sellerUserName, quantity):
        isProductExist, product = Catalogue.findProductInCategory(categoryName, productName, sellerUserName)
        if not isProductExist:
            return False, product

        isInCart, productFound = self.cart.findProductInCart(product.productName, product.seller.userName)
        if isInCart:
            return self.cart.updateQuantity(productFound.productName,productFound.seller.userName,productFound.productStock+quantity)

        product = copy.copy(product)
        product.productStock = quantity
        self.cart.productList.append(product)
        return True, "Item Added to Cart"

    def deleteFromCart(self, productName, sellerUserName):
        return self.cart.deleteItem(productName, sellerUserName)

    def addToWishlist(self, categoryName, productName, sellerUserName):
        isProductExist, product = Catalogue.findProductInCategory(categoryName, productName, sellerUserName)
        if not isProductExist:
            return False, product

        product = copy.copy(product)
        if product.productStock<1:
            product.productStock = "Out of Stock"
        else:
            product.productStock = "In Stock"

        self.wishlist.addItem(product)
        return True, "Item Added to wishlist"

    def deleteFromWishlist(self, productName, sellerUserName):
        return self.wishlist.deleteItem(productName, sellerUserName)

    def placeOrder(self, addressLabel, paymentMethod):
        if len(self.cart.productList) == 0:
            return False, "Cart Empty"

        isAddressExist, address = self.findAddress(addressLabel)
        if not isAddressExist:
            return False, "Address with given label not found"

        productListForOrder = []
        for product in self.cart.productList:
            isCategory, categoryFound = Catalogue.findCategory(product.category)
            if not isCategory:
                continue

            isProduct, productFound = categoryFound.findProduct(product.productName, product.seller.userName)
            if isProduct and product.productStock <= productFound.productStock:
                self.cart.productList.remove(product)
                productListForOrder.append(product)
                productFound.productStock -= product.productStock

        order = Order(self.name ,address, productListForOrder, paymentMethod)
        order.addOrderToSeller()
        #Catalogue.addOrderToSeller(order)
        self.orderList.append(order)
        return True, "Order Placed", "Order Id: " +str(Order.currentId)

    # def addOrderToSeller(self, order):
    #     dictionary = {}
    #     for product in order.productList:
    #         if product.seller.userName not in dictionary:
    #             list = []
    #             list.append(product)
    #             dictionary[product.seller.userName] = list
    #         else:
    #             dictionary[product.seller.userName].append(product)

    #     for seller in dictionary:
    #         order = Order(self.name,order.address,dictionary[seller],order.bill.paymentMethod, order.orderId)
    #         dictionary[seller][0].seller.orderList.append(order)

    def moveCartToWishlist(self, productName, sellerUserName):
        isDeleted, product = self.cart.deleteItem(productName, sellerUserName)
        if not isDeleted:
            return False, product
        
        return self.addToWishlist(product.category,product.productName,product.seller.userName)
    
    def moveWishlistToCart(self, productName, sellerUserName, quantity):
        isDeleted, product = self.wishlist.deleteItem(productName, sellerUserName)
        
        if not isDeleted:
            return False, product

        return self.addToCart(product.category,product.productName,product.seller.userName, quantity)

    def findOrder(self,id):
        for order in self.orderList:
            if order.orderId == id:
                return True, order
            return False, "Order not found"
        
    def printOrder(self,id):
        isOrderExist, order = self.findOrder(id)
        if not isOrderExist:
            print(order)
        order.display()

    def cancelOrder(self,id):
        isOrderExist, order = self.findOrder(id)
        if not isOrderExist:
            return False, "Order Not Found"   
        # order.display()
        self.orderList.remove(order)

        for product in order.productList:
            _, currentStock = product.seller.getStock(product.productName)
            product.seller.updateStock(product.productName, currentStock + product.productStock)
        
        list = []
        for product in order.productList:
            if product.seller.userName not in list:
                list.append(product.seller.userName)
                product.seller.cancelOrder(id)

        return True, "Order Removed"