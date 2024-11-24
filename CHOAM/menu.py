from enter import Enter

class Menu:
    def __init__(self):
        self.enter = Enter()

    def present_menu(self):
        print("""              Enter [E]
              About [A]
              Settings [S]
              Exit [X]""")
        
        option = input("\nEnter Option: ")
        
        if option.lower() == "e":
            self.enter_choam()
        elif option.lower() == "x":
            self.exit_choam()
        
    def enter_choam(self):
        self.enter.enter_password()
        
    def exit_choam(self):
        exit()
