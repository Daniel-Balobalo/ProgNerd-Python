class Car:
    
    #init method or object constructor
    def __init__(self, make, model, year, color):
        #Attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    #Methods
    def drive(self):
        print(f"This {self.model} is driving.")
        
    def stop(self):
        print(f"This {self.model} is stopped")