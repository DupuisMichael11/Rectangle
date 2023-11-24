# Michael Dupuis CIS261 Rectangle Project

from dataclasses import dataclass

@dataclass
class Rectangle:
    height: int
    width: int
    
    def get_perimeter(self):
        perimeter = self.height * 2 + self.width * 2
        return perimeter
    
    def get_area(self):
        area = self.height * self.width
        return area
    
    def get_str(self):
        s = ""
        w = "* " * self.width + "\n"
        s += w
        for i in range(self.height - 2):
            s += "* "
            s += "  " * (self.width - 2)
            s += "* \n"
        s += w
        return s
def main():
    print("Rectangle Calculator\n")
    
    again = "y"
    while again.lower() == "y":
        height = int(input("Height:  "))
        width = int(input("Width:  "))
        
        rectangle = Rectangle(height, width)
        print("Perimeter: ", rectangle.get_perimeter())
        print("Area: ", rectangle.get_area())
        print(rectangle.get_str())

        again = input("Continue? (y/n): \n").lower()
        
    print("Thank you, Goodbye!")
    
if __name__ == "__main__":
    main()
        
    