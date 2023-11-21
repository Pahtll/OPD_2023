import pygame  

size = int(input())
CountOfSquares = int(input())
SizeOfSquare = size / CountOfSquares

if size % CountOfSquares != 0:
    print("Error")
    pygame.quit()

pygame.init()
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Шахматная доска")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    SquareX = 0
    SquareY = 0
    Sdvig = 0

    while SquareY < size:
        while SquareX < size:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(SquareX, SquareY, SizeOfSquare, SizeOfSquare))
            SquareX += 2*SizeOfSquare
        SquareY += SizeOfSquare
        Sdvig += 1
        if Sdvig % 2 != 0:
            SquareX = SizeOfSquare
        else:
            SquareX = 0
                
    pygame.display.flip()
    clock.tick(60)

pygame.quit()