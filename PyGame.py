import pygame

Running = False


# Global_score = 0


def Game(Running):
    global Global_score
    Score = 0
    pygame.init()
    Screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("BOXED FRUIT")
    Icon = pygame.image.load('Images/Icon.png')
    pygame.display.set_icon(Icon)
    while Running:
        Score += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
                Global_score = Score
                print(Global_score)
                print(Score)
        pygame.display.flip()
    print(Global_score)
    pygame.quit()

