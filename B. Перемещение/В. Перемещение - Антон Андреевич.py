import pygame as pg

#Создаём окно размером 300 на 300
pg.init()
screen = pg.display.set_mode((300, 300))
pg.display.set_caption("Перемещение")

#Создаём квадрат размером 50 на 50 и задаём ему начальные координаты
squareX = 0
squareY = 0
pg.draw.rect(screen, (255, 0, 255), pg.Rect(squareX, squareY, 50, 50))

running = True

#Создаём флаг для проверки нажата ли кнопка
ButtonPressed = False

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        #Если кнопка мыши нажата в пределах квадрата, то флаг = true
        elif event.type == pg.MOUSEBUTTONDOWN:
            if squareX <= event.pos[0] <= squareX + 50 and squareY <= event.pos[1] <= squareY + 50:
                ButtonPressed = True

        #Когда кнопка отжата флаг = False
        elif event.type == pg.MOUSEBUTTONUP:
            ButtonPressed = False

        #Если кнопка нажата в координатах квадрата и мышь двинулась, то координаты квадрата будут равны координатам курсора в конце движения
        elif event.type == pg.MOUSEMOTION:
            if ButtonPressed:
                squareX = event.pos[0] - 25
                squareY = event.pos[1] - 25

        #Очищаем экран
        screen.fill((0, 0, 0))

        #Рисуем квадрат с новыми координатами
        pg.draw.rect(screen, (255, 0, 255), pg.Rect(squareX, squareY, 50, 50))

    #Обновляем экран
    pg.display.flip()

pg.quit()