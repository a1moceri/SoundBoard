import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(8)

class Board:
    def __init__(self):
        self.__win = pygame.display.set_mode((750, 400))
        self.__button_coordinates = [
            (30, 50),
            (30, 150),
            (30, 250),
            (400, 50),
            (400, 150),
            (400, 250)
        ]
        self.white = (255, 255, 255)
        self.green = (51, 204, 51)
        self.buttonFont = pygame.font.SysFont('comicsans', 20)
        self.textFont = pygame.font.SysFont('comicsans', 20)
        self.loaded_sounds = [
            'BABABOOEY', 'AIR HORN', 'VINE BOOM', 'WHAT?', 'RELOAD', 'GUNSHOT'
        ]
        self.button_labels = [
            '1', '2', '3', '4', '5', '6'
        ]
        self.sound1 = pygame.mixer.Sound('bababooey.wav')
        self.sound2 = pygame.mixer.Sound('airhorn.wav')
        self.sound3 = pygame.mixer.Sound('vineboom.wav') #gunshot
        self.sound4 = pygame.mixer.Sound('russWhat.wav') 
        self.sound5 = pygame.mixer.Sound('reload.wav')
        self.sound6 = pygame.mixer.Sound('gunshot1.wav') #vineboom


    def drawButtons(self):
        for cords in self.__button_coordinates:
            pygame.draw.circle(self.__win, self.green, cords, 20, width=0)

        return

    def drawText(self):
        for i in range(len(self.__button_coordinates)):
            pygame.draw.rect(self.__win, self.white,
                             [(self.__button_coordinates[i][0] + 35), (self.__button_coordinates[i][1] - 20), 300, 45],
                             0)
            # box text
            self.__win.blit(self.textFont.render(self.loaded_sounds[i], True, (0, 0, 0)),
                            ((self.__button_coordinates[i][0] + 40), (self.__button_coordinates[i][1] - 20)))
            # button labels
            self.__win.blit(self.buttonFont.render(self.button_labels[i], True, (0, 0, 0)),
                            ((self.__button_coordinates[i][0] - 5), (self.__button_coordinates[i][1] - 15)))

        return

    def playSounds(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP1]:
            pygame.mixer.Channel(1).play(self.sound1)
        if keys[pygame.K_KP2]:
            pygame.mixer.Channel(2).play(self.sound2)
        if keys[pygame.K_KP3]:
            pygame.mixer.Channel(3).play(self.sound3)
        if keys[pygame.K_KP4]:
            pygame.mixer.Channel(4).play(self.sound4)
        if keys[pygame.K_KP5]:
            pygame.mixer.Channel(5).play(self.sound5)
        if keys[pygame.K_KP6]:
            pygame.mixer.Channel(6).play(self.sound6)


def main():
    b = Board()
    run = True
    while run:
        pygame.time.delay(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        b.drawButtons()
        b.drawText()
        b.playSounds()
        pygame.display.update()


main()
