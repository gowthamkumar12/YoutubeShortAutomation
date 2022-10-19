from imports import *
from GenerateQuote import *
from QuoteImage import *

class Main:
    def getQuote(self, data, checks):
        global quote, author
        GetQuote = GenerateQuote()
        quote, author = GetQuote.setQuote(data, checks)
        
        
    def getImage(self, quote, author, fg, image, border_color, font_file=None, font_size=None,width=None,height=None):
        GetImage = QuoteImage()
        img = GetImage.quoteToImage(
            quote = quote,
            author = author,
            fg = "White",
            image = "data/background_img.jpg",
            border_color = "black",
            font_size = 64,
            font_file = None,
            width = 1080,
            height = 1920
        )
        
        img.save("output/quote.png")

data = pd.read_csv("data/Motivational_Quotes_Database.csv")
checks = "output/checks.csv"
obj = Main()
obj.getQuote(data, checks)
obj.getImage(quote, author, "white", "background_img.jpg", "black")