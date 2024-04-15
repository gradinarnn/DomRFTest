"""
Сервис для создания и сохранения изображения
"""

import os
from pathlib import Path

from PIL import Image, ImageDraw


class Imager:
    """Класс для работы с изображением"""

    @classmethod
    def create_image(
        cls, X_length: int, Y_length: int, background_color: str = "white"
    ) -> Image:
        """
        Создание пустого изображения
        :return: пустое изображения
        """
        image = Image.new(mode="RGB", size=(X_length, Y_length), color=background_color)

        return image

    @classmethod
    def get_drawer(cls, image):
        """
        Создание ImageDraw
        :param image: изображения
        :return: ImageDraw
        """
        drawer = ImageDraw.Draw(im=image)

        return drawer

    @classmethod
    def save_image(cls, image, path: str, image_name: str) -> None:
        """
        Сохранение изображения
        :param image: изображение
        :param path: директория для сохранения
        :param image_name: название файла
        """
        if not os.path.isdir(path):
            os.mkdir(path)
        path = os.path.abspath(os.path.join(path, f"{image_name}.jpg"))

        image.save(path, quality=95)

    @classmethod
    def drawing(cls, figures: list, drawer) -> None:
        """
        Рисование фигур на изображении
        :param figures: список фигур
        :param drawer: объект ImageDraw
        :return: None
        """
        for figure in figures:
            figure.draw(draw=drawer)
