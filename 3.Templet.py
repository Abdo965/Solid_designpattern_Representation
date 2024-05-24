class GameCharacter:
    def __init__(self, name):
        self.name = name

    def move(self):
        # Template method defines the overall movement flow
        self.check_environment()
        self.plan_movement()
        self.perform_movement()

    def check_environment(self):
        print(f"{self.name} is checking the environment for obstacles.")

    def plan_movement(self):
        # Abstract method, subclasses define specific movement plan
        pass

    def perform_movement(self):
        print(f"{self.name} is performing the planned movement.")


class Warrior(GameCharacter):
 def plan_movement(self):
     print(f"{self.name} (warrior) plans a direct attack move.")

class Archer(GameCharacter):
 def plan_movement(self):
    print(f"{self.name} (archer) plans a strategic flanking move.")

# Example Usage
warrior = Warrior("Aragorn")
archer = Archer("Legolas")

warrior.move()
# Output:
# Aragorn is checking the environment for obstacles.
# Aragorn (warrior) plans a direct attack move.
# Aragorn is performing the planned movement.

archer.move()
# Output:
# Legolas is checking the environment for obstacles.
# Legolas (archer) plans a strategic flanking move.
# Legolas is performing the planned movement.
