class Monarch():
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    
    monarch = get_monarch()
    
    if monarch.name == "Daemon":
        monarch.house = "Targaryen"

    print(f"\n{monarch.name} of House {monarch.house}.\n")

def get_monarch():
    name = input("\nName: ")
    house = input("House: ")
    monarch = Monarch(name, house)
    return monarch

if __name__ == "__main__":
    main()