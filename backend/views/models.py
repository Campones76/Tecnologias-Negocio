class Product:
    def __init__(self, ID, Name, CatID, Price, Image):
        self.ID =   ID
        self.Name = Name
        self.CatID = CatID
        self.Price = Price
        self.Image = Image
        
class Category:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name