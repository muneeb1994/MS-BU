class Movie:
    __price_with_gst = 0

    def __init__(self,name, category, description, price):
        """this is the constructor which is used to initialize the attributes"""
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def __calculatePriceWithGST(self,price):
        """ this private method is used to calculate the price with gst"""
        return (float(self.price) * 1.07)

    def getName(self):
        """ this method is used to return the name of movie"""
        return self.name

    def getCategory(self):
        """ this method is used to return the category of movie"""
        return self.category

    def getDescription(self):
        """ this method is used to return the description of movie"""
        return self.description

    def getPrice(self):
        """ this method is used to return the price of movie"""
        return self.price

    def getPriceWithGST(self):
        """ this method is used to return the price with gst of movie"""
        self.__price_with_gst =  self.__calculatePriceWithGST(self.price)
        return self.__price_with_gst

    def __repr__(self):
        """this method return the detail of movie in the form of list"""
        return [self.name,self.category,self.description,self.price]

    def __add__(self, more_price):
        """ this magic method is used when we need to increase the price of movie """
        return float(self.price) + float(more_price)

# Testing
if __name__ == "__main__":

    mov = Movie("Avengers","Adventure","Action based super hero movie","2")
    assert mov.getName() == "Avengers", "This is not the right movie name"
    assert mov.getCategory() == "Adventure","Wrong Category"
    assert mov.getDescription() == "Action based super hero movie","Wrong info."
    assert mov.getPrice() == "2"
    assert mov.getPriceWithGST() == 2.14, "Wrong Price"
    assert mov + 20 == 22 # test __add__ method
