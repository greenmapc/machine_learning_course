import pygame
import heapq
from PIL import Image as img
from keras.models import load_model
import numpy as np
from pandas import datetime

model = load_model('mnist.h5')


def fix_image(image):
    # датасет содержит картинки размером 28х28, поэтому делаем resize
    image = image.resize((28, 28))
    # делаем картинку черно-белой
    image = image.convert('L')
    image = np.array(image)
    # преобразование изображения в формат модели
    image = image.reshape(1, 28, 28, 1)
    image = image / 255.0
    return image


def predict_digit(image):
    image = fix_image(image)
    result = model.predict([image])[0]

    # выводим топ 3 вероятностей
    p = heapq.nlargest(3, result)
    digits = result.argsort()[-3:][::-1]
    for i in range(3):
        print('[', digits[i], p[i], ']')


def load_image(path):
    image = img.open(path)
    predict_digit(image)


def save_handwritten_digit(screen):
    image_name = "test_" + datetime.now().strftime('%Y-%m-%d %H:%M')
    save_path = './test_data/{}.png'.format(image_name)
    pygame.image.save(screen, save_path)
    load_image(save_path)


screen = pygame.display.set_mode((200, 200))
line_start = None

while True:
    mouse_pos = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            break
        if e.type == pygame.MOUSEBUTTONUP:
            line_start = None if line_start else mouse_pos
        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            save_handwritten_digit(screen)
    else:
        if line_start:
            pygame.draw.line(screen, pygame.color.Color('White'), line_start, mouse_pos, 10)
            line_start = mouse_pos
        pygame.display.flip()
        continue
    break
