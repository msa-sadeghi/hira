import pygame
pygame.init()
class Dog:
    def __init__(self, name, age, gender,image, sound):
        self.name = name
        self.age = age
        self.gender = gender
        self.image = image
        self.sound = sound
    def bark(self):
        if self.gender == "boy":
            self.sound.set_volume(2)
            self.sound.play()
        elif self.gender == "girl":
            self.sound.set_volume(0.5)
            self.sound.play()
    def move(self):
        pass


class Beagle(Dog):
    def __init__(self, name, age, gender, image, sound, is_hunter):
        super().__init__(name, age, gender,image, sound)
        self.is_hunter = is_hunter

    def hunt(self):
        if self.is_hunter:
            print(f"{self.name} is hunting so good")
        else:
            print(f"{self.name} can not hunt")


beagle1 = Beagle("jessi", 5, "girl", "image0", pygame.mixer.Sound("w1.mp3"), True)
beagle1.bark()
beagle1.hunt()




# dog1 = Dog("jessi", 7, "boy", "image1", pygame.mixer.Sound("w1.mp3"))
# dog2 = Dog("petty", 6, "boy", "image2", pygame.mixer.Sound("w2.mp3"))
# screen = pygame.display.set_mode((500,500))
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 dog1.bark()
#             if event.key == pygame.K_RETURN:
#                 dog2.bark()