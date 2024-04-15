import shapes.shapes as ShapesModule


class ShapeCreator:
    """
    Класс создание фигур из данных
    """

    @classmethod
    def parse_figures_data(cls, data: dict) -> list:
        """
        Парсинг данных фигур
        """

        figures_list = []

        figures_data = data.get("figures", None)
        image_y_size = data["image_size"]["Y_length"]
        if not figures_data:
            raise ValueError("фигуры для рисования не указаны")

        else:
            for figure_data in figures_data:
                figure_title = list(figure_data.keys())[0]
                figure_data = figure_data[figure_title]
                figure_data["image_y_size"] = image_y_size
                shape = getattr(ShapesModule, figure_title)(**figure_data)
                figures_list.append(shape)

        return figures_list
