import json
import os

from configuration.Config import Config


def read_data_from_json(path: str) -> dict:
    with open(path) as json_file:
        data = json.load(json_file)

        return data


def parse_image_file(filename: str) -> dict:
    """
    :param filename: имя файла в папке с данными
    :return: данные для изображения
    """
    path = os.path.abspath(os.path.join(Config.data_root_folder, filename))
    image_data = read_data_from_json(path)
    if not isinstance(image_data, dict):
        raise ValueError("Неверный формат файла")
    image_data["name"] = filename.split(".")[0]
    return image_data
