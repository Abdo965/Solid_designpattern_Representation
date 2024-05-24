# Example demonstrating Liskov Substitution Principle

# Base class defining a Bird
class Bird:
    def fly(self):
        pass

# Subclass defining a Duck
class Duck(Bird):
    def fly(self):
        return "Duck flying"

# Subclass defining an Ostrich
class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich cannot fly")

# Function to make a bird fly
def make_bird_fly(bird):
    return bird.fly()

# Usage
if __name__ == "__main__":
    duck = Duck()
    ostrich = Ostrich()

    # Making the duck fly
    print(make_bird_fly(duck))

    # Attempting to make the ostrich fly
    try:
        print(make_bird_fly(ostrich))
    except NotImplementedError as e:
        print(e)
