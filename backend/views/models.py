class Product:
    def __init__(self, ID, Name, CatID, Price, Image, Description, Brand, Model, Colour, Details):
        self.ID =   ID
        self.Name = Name
        self.CatID = CatID
        self.Price = Price
        self.Image = Image
        self.Description = Description
        self.Brand = Brand
        self.Model = Model
        self.Colour = Colour
        self.Details = Details
        
class Category:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name
        
class Inventory:
    def __init__(self, ID, Prod_ID, Inv):
        self.ID = ID
        self.Prod_ID = Prod_ID
        self.Inv = Inv