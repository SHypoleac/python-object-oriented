# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: define a class to represent a stock symbol

# Challenge: create a class to represent stock information.
# Your class should have properties for:
# Ticker (string)
# Price (float)
# Company (string)
# And a method get_description() which returns a string in the form
# of "Ticker: Company -- $Price"

class Stock:
    def __init__(self,Ticker: str="Unknown",price: float=0,Company: str="Unknown"):
        self.Ticker = Ticker
        if price>0:
            self.price = price
        else:
            raise ValueError("You can't create a stock without price value!")
        self.Company = Company
    def get_description(self):
        return (f"{self.Ticker} :{self.Company} -- {self.price}")

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())
