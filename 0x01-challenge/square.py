#!/usr/bin/python3

class square():

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def print_square(self):
        """ Prints the square """
        for i in range(0, self.width):
            for j in range(0, self.height):
                print("#", end="")
            print("")

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
    s.print_square()
