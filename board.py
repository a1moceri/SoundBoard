import pygame
import os

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(10)

class Board:
    def __init__(self):
        self.__win = pygame.display.set_mode((750, 400))
        self.__button_coordinates = [
            (30, 200), (275, 200), (520, 200),
            (30, 130), (275, 130), (520, 130),
            (30, 50), (275, 50), (520, 50)
        ]
        self.__zero = (275, 275)
        self.white = (255, 255, 255)
        self.green = (51, 204, 51)
        self.buttonFont = pygame.font.SysFont('comicsans', 20)
        self.textFont = pygame.font.SysFont('comicsans', 20)

        self.button_labels = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ]
        self.sounds = []


    def drawButtons(self):
        for cords in self.__button_coordinates:
            pygame.draw.circle(self.__win, self.green, cords, 20, width=0)

        pygame.draw.circle(self.__win, self.green, self.__zero, 20, width=0)

        return

    def drawText(self):
        for i in range(len(self.__button_coordinates)):
            pygame.draw.rect(self.__win, self.white,
                             [(self.__button_coordinates[i][0] + 35), (self.__button_coordinates[i][1] - 20), 175, 40],
                             0)
            # box text
            try:
                self.__win.blit(self.textFont.render(self.sounds[i][7:], True, (0, 0, 0)), ((self.__button_coordinates[i][0] + 40), 
                    (self.__button_coordinates[i][1] - 20)))
            except IndexError:
                self.__win.blit(self.textFont.render('', True, (0, 0, 0)), ((self.__button_coordinates[i][0] + 40), 
                    (self.__button_coordinates[i][1] - 20)))

            # button labels
            self.__win.blit(self.buttonFont.render(self.button_labels[i], True, (0, 0, 0)),
                            ((self.__button_coordinates[i][0] - 5), (self.__button_coordinates[i][1] - 15)))

        pygame.draw.rect(self.__win, self.white, [(self.__zero[0] + 35), (self.__zero[1] - 20), 175, 40], 0)
        self.__win.blit(self.textFont.render('Silence', True, (0, 0, 0)), ((self.__zero[0] + 40), 
                    (self.__zero[1] - 20)))
        self.__win.blit(self.buttonFont.render('0', True, (0, 0, 0)),
                        ((self.__zero[0] - 5), (self.__zero[1] - 15)))

        return

    def playSounds(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP1] and self.sounds[0] != '':
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(self.sounds[0]))
        if keys[pygame.K_KP2] and self.sounds[1] != '':
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(self.sounds[1]))
        if keys[pygame.K_KP3] and self.sounds[2] != '':
            pygame.mixer.Channel(3).play(pygame.mixer.Sound(self.sounds[2]))
        if keys[pygame.K_KP4] and self.sounds[3] != '':
            pygame.mixer.Channel(4).play(pygame.mixer.Sound(self.sounds[3]))
        if keys[pygame.K_KP5] and self.sounds[4] != '':
            pygame.mixer.Channel(5).play(pygame.mixer.Sound(self.sounds[4]))
        if keys[pygame.K_KP6] and self.sounds[5] != '':
            pygame.mixer.Channel(6).play(pygame.mixer.Sound(self.sounds[5]))
        if keys[pygame.K_KP7] and self.sounds[6] != '':
            pygame.mixer.Channel(7).play(pygame.mixer.Sound(self.sounds[6]))
        if keys[pygame.K_KP8] and self.sounds[7] != '':
            pygame.mixer.Channel(8).play(pygame.mixer.Sound(self.sounds[7]))
        if keys[pygame.K_KP9] and self.sounds[7] != '':
            pygame.mixer.Channel(9).play(pygame.mixer.Sound(self.sounds[8]))

        if keys[pygame.K_KP0]:
            pygame.mixer.quit()
            pygame.mixer.init()
            pygame.mixer.set_num_channels(10)


    def readDir(self):
        dir_list = os.listdir('./Sounds')
        for file in dir_list:
            if file[-4:] == '.wav' and len(self.sounds) < 9:
                self.sounds.append('Sounds/' + file)


def main():
    b = Board()
    b.readDir()
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
