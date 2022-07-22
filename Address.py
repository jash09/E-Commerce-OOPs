import json

class Address:
    def __init__(self,label,name,houseNo,street,city,pinCode,contact):
        self.label = label
        self.name = name
        self.houseNo = houseNo
        self.street = street
        self.city = city
        self.pinCode = pinCode
        self.contact = contact

    def printAddress(self):
        print(json.dumps(self, indent=5, default=lambda o: o.__dict__))
        # print("The label is",self.label,"\nhouse no.", self.houseNo,
        #                 self.street,"street \n",self.city,"- ",self.pinCode,
        #                 "\nContact -",self.contact
        #                 )

    