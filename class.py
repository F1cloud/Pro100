class Atm:
    def __init__(self, cardnumber,pin): 
        self.cardnumber = cardnumber
        self.pin = pin
    
    def check_balance(self):
        print("Your balance is 10,000")
    def cashWithdrawl(self):
        print("This is a cash withdrawl")
    def balanceEnquiry(self):
        print("This is a balance enquiry")