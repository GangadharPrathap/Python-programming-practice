class Member:
    def __init__(self, customerId, customerName, emailId):
        self.customerId = customerId
        self.customerName = customerName
        self.emailId = emailId

class GoldMember(Member):
    def __init__(self, customerId, customerName, emailId):
        super().__init__(customerId, customerName, emailId)
        self.discountAmount = 0.0

    def calculateDiscount(self, purchaseAmount):
        self.discountAmount = purchaseAmount - (purchaseAmount * 0.10)
        return self.discountAmount

class DiamondMember(Member):
    def __init__(self, customerId, customerName, emailId):
        super().__init__(customerId, customerName, emailId)
        self.discountAmount = 0.0

    def calculateBalance(self, purchaseAmount):
        self.discountAmount = purchaseAmount - (purchaseAmount * 0.20)
        return self.discountAmount


print("1.GoldMembership")
print("2.DiamondMembership")
choice = int(input("Enter the choice\n"))

print("Enter the Details:")
customerId = input("Customer Id\n")
customerName = input("Customer Name\n")
emailId = input("EmailId\n")
purchaseAmount = float(input("Enter the Purchase Amount\n"))

print("Member Details")

if choice == 1:
    g_account_obj = GoldMember(customerId, customerName, emailId)
    amount = g_account_obj.calculateDiscount(purchaseAmount)
    print(customerId, customerName, emailId, amount)
elif choice == 2:
    d_account_obj = DiamondMember(customerId, customerName, emailId)
    amount = d_account_obj.calculateBalance(purchaseAmount)
    print(customerId, customerName, emailId, amount)
