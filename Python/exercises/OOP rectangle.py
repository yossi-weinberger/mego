class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

    def user_input(self):
        self.length = float(input("Type the length of your rectangle: "))
        self.width = float(input("Type the width of your rectangle: "))

    def parameter(self):
        return (self.width * 2) + (self.length * 2)

    def area(self):
        return self.length * self.width

    def result_print(self):
        print("The parameter of your rectangle is: {0} \nThe area of your rectangle is: {1} "
              .format(Rectangle.parameter(self), Rectangle.area(self)))

    def rec_paint(self):
        print(" *" * int(self.width))
        for i in range(int(self.length)):
            print("*" + "  " * int(self.width) + "*")
        print(" *" * int(self.width))


rec_1 = Rectangle()
rec_1.user_input()
rec_1.result_print()
rec_1.rec_paint()
