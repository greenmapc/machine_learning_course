import numpy as np
import pygame
import sklearn.svm as svm

min_x = 0
max_x = 600
min_y = 0
max_y = 400


pygame.init()
display = pygame.display.set_mode((max_x, max_y))
display.fill((255, 255, 255))
pygame.display.update()

clock = pygame.time.Clock()
FPS = 60

points = []
clusters = []

play = True
while play:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False
            pygame.quit()
            break
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pygame.draw.circle(display, (255, 0, 0), i.pos, 10)
                clusters.append(1)
                points.append((i.pos[0], i.pos[1]))
            elif i.button == 3:
                pygame.draw.circle(display, (0, 255, 0), i.pos, 10)
                clusters.append(0)
                points.append((i.pos[0], i.pos[1]))
            elif i.button == 2:
                display.fill((255, 255, 255))
                points = []
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_r:
                print("Start algorithm")
                clf = svm.SVC(kernel='linear', C=1.0)
                clf.fit(points, clusters)

                # получение веса  w из (w * x - b = 0)
                w = clf.coef_[0]
                # преобразование формулы на a * x = 0
                a = -w[0] / w[1]

                xx = np.linspace(0, 600, 2)

                # подставляем значения в решающую функцию, чтобы получить ее значение
                # где clf.intercept_[0] - коэффициенты в уравнении разделяющей гиперплоскости
                yy = a * xx - (clf.intercept_[0]) / w[1]

                pygame.draw.line(display, (0, 0, 0),
                                 (xx[0], yy[0]),
                                 (xx[len(xx) - 1], yy[len(yy) - 1]))
    pygame.display.update()
    clock.tick(FPS)
