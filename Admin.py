from ast import Delete
from gettext import Catalog
from User import User
from Seller import Seller
from Customer import Customer
from Order import Order
from Catalogue import Catalogue

class Admin(User):
    def __init__(self, userName, name, age, gender):
        super().__init__(userName, name, age, gender)
        self.customerList = []
        self.sellerList = []
    
    @staticmethod
    def createAdmin(userName, name, age, gender):
        print("Admin Created")
        return Admin(userName, name, age, gender)

    def printCustomers(self, userName = None):
        if userName == None:
            for cust in self.customerList:
                cust.display()
            return

        isCustExist, customer = self.findCustomer(userName)
        if not isCustExist:
            print("Customer Not Found")
        customer.display()

    def printSeller(self, userName = None):
        if userName == None:
            for seller in self.sellerList:
                seller.display()
            return
        
        isSellerExist, seller = self.findSeller(userName)
        if not isSellerExist:
            print("Seller Not Found")
        seller.display()

    def dispAll(self):
        for pro in Catalogue.allProducts:
            print(pro.categoryName)
            for p in pro.productList:
                p.displayProduct()

    def addCatalogue(self, categoryName):
        isCategoryExist, categoryFound = Catalogue.findCategory(categoryName)
        if isCategoryExist:
            return False, "Category Already Present"

        category = Catalogue(self, categoryName)
        Catalogue.allProducts.append(category)
        return True, "Category Added"

    def findSeller(self, userName):
        for seller in self.sellerList:
            if seller.userName == userName:
                return True, seller
        return False, None

    def createSeller(self,userName, name, age, gender):
        isSellerExist, sellerFound = self.findSeller(userName)
        if isSellerExist:
            return False, "Cannot create seller! Already exists"
        
        newSeller = Seller(userName, name, age, gender)
        self.sellerList.append(newSeller)
        return True, newSeller

    def findCustomer(self,userName):
            for customer in self.customerList:
                if customer.userName == userName:
                    return True, customer
            return False, None
    
    def createCustomer(self,userName, name, age, gender):
        isCustomerExist, customerFound = self.findCustomer(userName)
        if isCustomerExist:
            return False, "Cannot create customer! Username already exists."
        
        newCustomer = Customer(userName, name, age, gender)
        self.customerList.append(newCustomer)
        return True, newCustomer

    def deleteCustomer(self,userName):
        isCustomerExist, customerFound = self.findCustomer(userName)
        if not isCustomerExist:
            return False, "Customer does not exist"
        
        self.customerList.remove(customerFound)
        return True, "Customer Deleted"

    def deleteSeller(self,userName):
        isSellerExist, sellerFound = self.findSeller(userName)
        if not isSellerExist:
            return False, "Seller does not exist"
        
        self.customerList.remove(sellerFound)
        return True, "Seller Deleted"


def main():

    admin = Admin.createAdmin("rohit19","Rohit",23,"M")
    
    print("------ Category Creation --------")

    print(admin.addCatalogue("Electronics"))
    print(admin.addCatalogue("Furniture"))
    print()

    print("------ Seller and Customer Creation -------------")
    _, seller1 = admin.createSeller("jash29","Jash",21,"M")
    _, cust1 = admin.createCustomer("hari32","Hari",25,"M")
    _, seller2 = admin.createSeller("ashley29","Ashley",30,"F")
    _, cust2 = admin.createCustomer("snita32","snita",35,"F")

    print("------- Printing All Customers ---------------")
    admin.printCustomers()
    print("------- Printing All Sellers ---------------")
    admin.printSeller()

    print("------- Address Function ---------------")
    print(cust1.addAddress("Home","Hari Bhai", 230, "circle street", "Mumbai", 400001, 9234432145))
    print(cust1.updateAddress("Home","Hari Krishna", 230, "Square Street", "Mumbai", 400001, 9234432145))
    print(cust1.addAddress("Work","Hari Ram", 250, "koi bhi street", "Mumbai", 400021, 9234431145))
    print(cust1.deleteAddress("Home"))

    print("---------- Print Customer by Username ----------------")
    admin.printCustomers("hari32")

    print("---------- Print Seller by Username ----------------")
    admin.printSeller("jash29")  

    print("---------- Product Creation --------------")
    print(seller1.createProduct("Mobile",200,15000,"Electronics"))
    print(seller2.createProduct("Sofa",25,3000,"Furniture"))

    print()
    print("----------- Seller1 Products ----------------")
    seller1.displaySellerProductList()
    
    print()
    print("----------- Seller2 Products ----------------")
    seller2.displaySellerProductList()

    print()
    print("----------- All Products ------------------")
    cust1.printAllProducts()

    print()
    print("------------ Add to Cart -----------------")
    print(cust1.addToCart("Electronics","Mobile","jash29", 10))

    print()
    print("------------ Cart ----------------")
    cust1.printCart()
    
    print()
    print("------------ Add to Wishlist -----------------")
    print(cust1.addToWishlist("Furniture","Sofa","ashley29"))

    print()
    print("------------ Wishlist ----------------")
    cust1.printWishlist()

    print()
    print("------------ Place Order ----------------")
    print(cust1.placeOrder("Work","Credit"))

    print()
    print("------------ Print Order ----------------")
    cust1.printOrder(0)

    print()
    print("------------ Display All Products ----------------")
    admin.dispAll()

    print()
    print("------------ Wishlist ----------------")
    cust1.printWishlist()

    print()
    print("------------ Wishlist to Cart ----------------")
    print(cust1.moveWishlistToCart("Sofa","ashley29",2))

    print()
    print("------------ Wishlist ----------------")
    cust1.printWishlist()

    print()
    print("------------ Cart ----------------")
    cust1.printCart()

    print()
    print("------------ Cart to Wishlist ----------------")
    print(cust1.moveCartToWishlist("Sofa","ashley29"))

    print()
    print("------------ Wishlist ----------------")
    cust1.printWishlist()

    print()
    print("------------ Cart ----------------")
    cust1.printCart()

    print()
    print("------------ Delete from Wishlist ----------------")
    print(cust1.deleteFromWishlist("Sofa", "ashley29"))
    
    print()
    print("------------ Wishlist ----------------")
    cust1.printWishlist()

    print()
    print("----------- All Products ------------------")
    cust2.printAllProducts()

    print()
    print("------------ Add to Cart -----------------")
    print(cust2.addToCart("Electronics","Mobile","jash29", 100))

    print()
    print("------------ Cart ----------------")
    cust2.printCart()

    print(cust2.addAddress("Work","snita32", 100, "koi bhi street2", "Mumbai", 400021, 9234411115))

    print()
    print("------------ Place Order ----------------")
    print(cust2.placeOrder("Work","Credit"))

    print()
    print("------------ Print Order ----------------")
    cust2.printOrder(1)

    print()
    print("------------ Display All Products ----------------")
    admin.dispAll()

    print()
    print("------------ Update Stock ----------------")
    print(seller1.updateStock("Mobile",150))

    print()
    print("------------ Display All Products ----------------")
    admin.dispAll()

    print()
    print("------------ Seller1 Orders ----------------")
    seller1.displayOrderList()

    print()
    print("------------ Seller2 Orders ----------------")
    seller2.displayOrderList()

    print()
    print("------------ Fullfill order 0 ----------------")
    print(seller1.fullfillOrder(0))

    print()
    print("------------ Seller1 Orders ----------------")
    seller1.displayOrderList()

    print()
    print("------------ Cancel Order ----------------")
    print(cust2.cancelOrder(1))

    print()
    print("------------ Seller1 Orders ----------------")
    seller1.displayOrderList()

    print()
    print("------------ Display All Products ----------------")
    admin.dispAll()

if __name__=="__main__":
    main()