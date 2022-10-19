from imports import *

class GenerateQuote:
    def setQuote(self, data, checks):
        number = random.randrange(len(data))
        
        isPresent = False
        reader = csv.DictReader(open(checks))
        for row in reader:
            if(str(number) in row['quoteNumbers']):
                isPresent = True
        if(isPresent):
            print("present")
            self.setQuote(data)            
        quoteNumber = data.iloc[number]
        quote = quoteNumber.Quotes
        author = quoteNumber.Author
        
        byte = quote.encode('utf-8')
        salt = bcrypt.gensalt(10)
        hashedQuote = bcrypt.hashpw(byte, salt)
        
        data = [number, hashedQuote]
        toCsv = str(number)
        csvFile = open(f"output/checks.csv", "a",  newline = '')
        writer = csv.writer(csvFile)
        writer.writerow(data)
        
        return quote, author
        
        