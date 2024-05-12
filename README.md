# 2D Shooter game in python

## Introduction
This project is a simple shooter game developed using the Pygame library in Python. The game features a player character navigating through levels, shooting enemies, collecting items, and completing objectives.

### What is your application?
The application is a 2D shooter game built in Python using the Pygame library. Player controls a character who must navigate through levels, defeat enemies, and accomplish objectives.

### How to run the program?
To run the program, ensure you have Python installed on your system along with the Pygame library. Clone the repository to your local machine and execute the main Python file `Shooter.py`.

### How to use the program?
- Use the 'A  and 'D' to move the player character left or right.
- Press the 'W' to jump.
- Press the 'ARROW_UP' key to shoot bullets.
- Press the 'ARROW_DOWN' key to throw grenades.
- Collect health, ammo, and grenade boxes to replenish health, ammo, and grenades, respectively.
- Complete each level by reaching the exit.


# Body/Analysis

The program implements the functions:

    1. Player movement and actions
    2. Enemy AI behavior
    3. Collision detection with the environment
    4. Shooting bullets and throwing grenades
    5. Collecting items
    6. Level completion and progression

The implementation utilizes object-oriented programming (OOP) principles to organize the codebase effectively.

## 4 OOP Pillars

### Polymorphism
Polymorphism allows objects to be treated as instances of their parent class or any of their subclasses interchangeably. In the code, polymorphism can be observed in the way different types of game entities, such as the player character and enemies, are treated uniformly when updating, drawing, or performing other actions. For example, the `Soldier` class handles both player and enemy entities, enabling polymorphic behavior.

```bash
class Soldier(pygame.sprite.Sprite):
    # ...
    def update(self):
        self.update_animation()
        self.check_alive()
        # ...
```

### Abstraction
Abstraction is achieved by hiding the complex implementation details and exposing only the necessary functionalities to the outside world. In the code, abstraction is demonstrated in various ways, such as encapsulating player and enemy behavior within the `Soldier` class, which hides the underlying logic while providing methods to interact with these entities.

```bash
class Soldier(pygame.sprite.Sprite):
    # ...  
	def move(self, moving_left, moving_right):
		#reset movement variables
		screen_scroll = 0
		dx = 0
		dy = 0

		#assign movement variables if moving left or right
		if moving_left:
			dx = -self.speed
			self.flip = True
			self.direction = -1
		if moving_right:
			dx = self.speed
			self.flip = False
			self.direction = 1

		#jump
		if self.jump == True and self.in_air == False:
			self.vel_y = -14
			self.jump = False
			self.in_air = True

		#apply gravity
		self.vel_y += GRAVITY
		if self.vel_y > 10:
			self.vel_y
		dy += self.vel_y
        # ...
```

### Inheritance
Inheritance allows classes to inherit attributes and methods from their parent class, promoting code reuse and creating a hierarchy of related classes. In the code, inheritance is seen where certain classes inherit from the pygame.sprite.Sprite class, which provides basic functionality for representing game objects in Pygame.

```bash
class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades):
        pygame.sprite.Sprite.__init__(self)
        # ...
```

### Encapsulation
Encapsulation involves bundling data and methods that operate on the data within a single unit, controlling access to the internal state of objects. In the code, encapsulation is evident in the classes such as `Soldier`, `World`, `HealthBar`, `Bullet`, `Grenade`, `Explosion`, `ScreenFade`, `ItemBox`, `Decoration`, `Water`, and `Exi`t. These classes encapsulate attributes and methods related to specific entities or functionalities in the game.

```bash
class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades):
        pygame.sprite.Sprite.__init__(self)
        # Encapsulated attributes
        self.alive = True
        self.dead = False
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.shoot_cooldown = 0
        self.grenades = grenades
        self.health = 100
        # ...
```

## Design Patterns

### Singleton Pattern
The Singleton Pattern ensures that a class has only one instance and provides a global point of access to that instance. Although not explicitly implemented in the provided code, the Singleton Pattern could be suitable for managing global game state or resources, ensuring that there is only one instance of critical components like the game world or score manager.

### Factory Method Pattern
The Factory Method Pattern provides an interface for creating objects but allows subclasses to alter the type of objects that will be created. In the context of the game, the Factory Method Pattern could be employed to create different types of game entities dynamically, such as generating various enemy types or spawning different item boxes based on certain conditions.

## File Handling

File handling functionalities for reading from and writing to files are incorporated into the program. The `ScoreManager` class manages reading and writing the player's score to a text file ("score.txt"). This functionality ensures that the player's progress is saved and can be retrieved across different game sessions.

### Example Code Snippet (ScoreManager):

```python
# Writing score to file
def write_score(self):
    with open('score.txt', 'w') as file:
        file.write(str(self.score))

# Reading score from file
def read_score(self):
    try:
        with open('score.txt', 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 0
```



## Testing

The core functionality of the program is covered with unit tests using the unittest framework. The tests ensure that individual components, such as player movement, enemy behavior, and collision detection, function correctly and meet the specified requirements.

Snippet:
```bash
import os
import unittest
import pygame
from Shooter import *


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.display.set_mode((1, 1))
        pygame.init()

    @classmethod
    def tearDownClass(cls):
        pygame.quit()
        
    def test_initial_score(self):
        score_manager = ScoreManager()
        self.assertEqual(score_manager.score, 0)
```
To run tests launch this command in terminal:
```bash
python test.py
```
# Results

- Successfully implemented player movement, shooting, and enemy AI behavior.
- Achieved functional collision detection and item collection mechanics.
- Completed multiple levels with increasing difficulty.
- Faced challenges in fine-tuning gameplay balance and optimizing performance.

# Conclusion

- The coursework has demonstrated proficiency in game development with Pygame.
- The implemented game features provide an engaging user experience.
- Future enhancements could include additional levels, enemy types, and power-ups to enrich gameplay.


# Documentation

[Pygame Documentation](https://www.pygame.org/docs/)\
[Python Official Documentation](https://docs.python.org/)\
[CSV](https://docs.python.org/3/library/csv.html)\
[Unit test framework](https://docs.python.org/3/library/unittest.html)

