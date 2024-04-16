import abc
from abc import ABC

from PIL.Image import Image
from PIL.ImageDraw import ImageDraw


class BaseShape(ABC):
    """
    Базовый класс фигуры
    """

    def __init__(self, *args, **kwargs):
        """
        Парсинг параметров для украшения фигур: толщина линии, цвет обводки, прозрачность
        :param line_width: толщина линии
        :param transparency: прозрачность
        """
        self.width = kwargs.get("line_width", 1)
        self.fill = self.__get_fill(**kwargs)
        image_y_size = kwargs.get("image_y_size")
        self.figure_xy = self.get_figure_xy(y_size=image_y_size)
        self.outline = kwargs.get("outline", (0,0,0))

    def __get_fill(self, **kwargs):
        transparency = kwargs.get("transparency", None)
        fill = kwargs.get("Color", None)
        if fill is None and transparency == "off":
            return "white"

        else:
            return fill

    @abc.abstractmethod
    def get_figure_xy(self, y_size):
        pass


class Circle(BaseShape):
    """
    Класс круга
    """

    def __init__(self, *args, **kwargs):
        self.X_center = kwargs.get("X_center")
        self.Y_center = kwargs.get("Y_center")
        self.Radius = kwargs.get("Radius")
        super().__init__(*args, **kwargs)

    def get_figure_xy(self, y_size: int) -> tuple:
        """
        Границы круга
        :param y_size: размеры листа по оси y
        :return: кортеж с границами круга
        """

        x0 = self.X_center - self.Radius
        y0 = y_size - (self.Y_center + self.Radius)
        x1 = self.X_center + self.Radius
        y1 = y_size - (self.Y_center - self.Radius)

        return x0, y0, x1, y1

    def draw(self, draw: ImageDraw) -> None:
        """
        Рисование круга
        :param draw: объект ImageDraw
        """

        draw.ellipse(
            self.figure_xy,
            fill=self.fill,
            width=self.width,
            outline=self.outline
        )


class Rectangle(BaseShape):
    """
    Класс прямоугольника
    """

    def __init__(self, *args, **kwargs):
        self.X_upper_left = kwargs.get("X_upper_left")
        self.Y_upper_left = kwargs.get("Y_upper_left")
        self.X_lower_right = kwargs.get("X_lower_right")
        self.Y_lower_right = kwargs.get("Y_lower_right")
        super().__init__(*args, **kwargs)

    def get_figure_xy(self, y_size: int) -> tuple:
        """
        Границы прямоугольника
        :param y_size: размеры листа по оси y
        :return: кортеж с границами прямоугольника
        """
        x0 = self.X_upper_left
        y0 = y_size - self.Y_upper_left
        x1 = self.X_lower_right
        y1 = y_size - self.Y_lower_right

        return x0, y0, x1, y1

    def draw(self, draw: ImageDraw) -> None:
        """
        Рисование прямоугольника
        :param image: изображение
        :param draw: объект ImageDraw
        """

        draw.rectangle(
            self.figure_xy,
            fill=self.fill,
            width=self.width,
            outline=self.outline
        )


class Triangle(BaseShape):
    """
    Класс треугольника
    """

    def __init__(self, *args, **kwargs):
        self.points = kwargs.get("Shape", [])
        if not len(self.points) == 3:
            raise ValueError(
                "Для треугольника неверно указано количество точек. Необходимо указать 3 точки"
            )
        super().__init__(*args, **kwargs)

    def get_figure_xy(self, y_size: int) -> list:
        """
        Границы треугольника
        :param y_size: размеры листа по оси y
        :return: список с координатами точек треугольника
        """
        points_list = []

        for point in self.points:
            point_dict = point.get("Point")
            x = point_dict["X"]
            y = y_size - point_dict["Y"]
            points_list.append((x, y))

        return points_list

    def draw(self, draw: ImageDraw) -> None:
        """
        Рисование треугольника
        :param draw: объект ImageDraw
        """

        draw.polygon(
            self.figure_xy,
            fill=self.fill,
            width=self.width,
            outline=self.outline
        )


class Square(BaseShape):
    """
    Клас квадрата
    """

    def __init__(self, *args, **kwargs):
        self.X_upper_left = kwargs.get("X_upper_left")
        self.Y_upper_left = kwargs.get("Y_upper_left")
        self.side_length = kwargs.get("side_length")
        super().__init__(*args, **kwargs)

    def get_figure_xy(self, y_size: int) -> tuple:
        """
        Границы квадрата
        :param y_size: размеры листа по оси y
        :return: кортеж с границами квадрата
        """
        x0 = self.X_upper_left
        y0 = y_size - self.Y_upper_left
        x1 = x0 + self.side_length
        y1 = y0 + self.side_length

        return x0, y0, x1, y1

    def draw(self, draw: ImageDraw) -> None:
        """
        Рисование квадрата
        :param draw: объект ImageDraw
        """

        draw.rectangle(
            self.figure_xy,
            fill=self.fill,
            width=self.width,
            outline=self.outline
        )
