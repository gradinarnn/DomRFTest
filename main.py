import os

from configuration.Config import Config
from configuration.Configurator import Configurator
from services.imager import Imager
from services.shape_creator import ShapeCreator
from utils.utils import parse_image_file


def draw_image():

    Configurator.parse_config()
    for filename in os.listdir(Config.data_root_folder):

        image_data = parse_image_file(filename)

        image_size = image_data.get("image_size", None)
        if not isinstance(image_size, dict):
            raise ValueError("неверный формат указания размеров изображения")
        image = Imager.create_image(**image_size)
        drawer = Imager.get_drawer(image)
        figures_list = ShapeCreator.parse_figures_data(data=image_data)

        Imager.drawing(figures=figures_list, drawer=drawer)

        Imager.save_image(image, Config.output_folder, image_data["name"])


if __name__ == "__main__":
    draw_image()
