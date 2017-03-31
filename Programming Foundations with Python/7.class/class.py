class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print(self.last_name)


class Child(Parent):
    def __init__(self, last_name, eye_color, no_toys):
        print ("Child Constructor Created")
        Parent.__init__(self, last_name, eye_color)
        self.no_toys = no_toys

    def show_info(self):
        print(self.last_name)
        print(self.no_toys)


miley = Parent("Cyrus", "Blue")
# miley.show_info()
minny = Child("Cyrus", "red", 6)
minny.show_info()
