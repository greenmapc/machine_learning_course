from cv2 import cv2

HAAR_FRONTALFACE_XML_PATH = "haarcascade_frontalface_default.xml"


# загружаем фотографию в черно-белом цвете
def load_black_white_img(image_path):
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


# загрузка модели, обученной на тренировочных данных из файла haarcascade_frontalface_default.xml
def get_frontface_cascade_classifier():
    return cv2.CascadeClassifier(HAAR_FRONTALFACE_XML_PATH)


def detect_face_on_img(image_path):
    image = load_black_white_img(image_path)
    classifier = cv2.CascadeClassifier(HAAR_FRONTALFACE_XML_PATH)
    # запускаем функцию для поиска лиц
    image_with_detected_faces = classifier.detectMultiScale(image)

    # вписываем каждое найденное лицо в квадрат
    for face in image_with_detected_faces:
        x, y, width, height = face
        x2, y2 = x + width, y + height
        # рисуем белый квадрат
        cv2.rectangle(image, (x, y), (x2, y2), (255, 255, 255), 1)

    # отображение полученной картинки
    cv2.imshow('face detection', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_face_on_img("test.jpg")