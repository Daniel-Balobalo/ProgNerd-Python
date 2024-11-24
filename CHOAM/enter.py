import getpass

class Enter:
    def __init__(self):
        self.identification = ""

    def enter_password(self):
        password = getpass.getpass("Enter Your Password: ")
        
        if password == "atr":
            self.identification = "Atreides"
            
        elif password == "hrk":
            self.identification = "Harkonnen"
            
        elif password == "crn": 
            self.identification = "Corrino"
            
        elif password == "fnr":
            self.identification == "Fenring"
            
        elif password == "gnz":
            self.identification == "Ginaz"
            
        elif password == "hlk":
            self.identification == "Halleck"
            
        elif password == "mtl":
            self.identification == "Metulli"
            
        elif password == "min":
            self.identification == "Moritani"
            
        elif password == "ord":
            self.identification == "Ordos"
            
        elif password == "vns":
            self.identification == "Vernius"
            
        elif password == "rch":
            self.identification == "Richese"
            
        elif password == "nbr":
            self.identification == "Nebiro"
            
        print(f"You're representing The Great House {self.identification}.")