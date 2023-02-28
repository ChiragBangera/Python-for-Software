class Animal:
    fur_color = "Grey"
    friends = []

    def __init__(self, height=100, weight=100) -> None:
        self.height = height
        self.weight = weight

    def print_height(self):
        print("The height is {}".format(self.height))

    def get_color(self):
        return self.fur_color

    def get_friends(self):
        return self.friends


animal_1 = Animal(128, 80)
animal_2 = Animal(70, 150)
animal_3 = Animal(128, 80)

animal_1.fur_color = "Pink"
animal_1.friends.append("chirag")
animal_1.print_height()
print(animal_1.get_color())
print(animal_1.get_friends())


class children(Animal):
    def __init__(self, height=100, weight=100) -> None:
        super().__init__(height, weight)


child_1 = children(20, 50)

print(child_1.get_color())
print(child_1.height)


def response_to_maintain(func):
    def wrapper():
        print("mail man is coming")
        func()

    return wrapper


@response_to_maintain
def bark():
    print("woof")


@response_to_maintain
def cat_responce():
    print("meow")


bark()
cat_responce()
