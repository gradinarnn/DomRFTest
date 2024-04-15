import os

from configuration.Config import Config
from utils.utils import read_data_from_json


class Configurator:
    """
    Класс создания конфигурации скрипта
    """

    @classmethod
    def parse_config(cls, path="") -> None:

        config_path = path if path else "./config.json"

        try:
            data = read_data_from_json(path=config_path)
            Config.path = os.path.abspath(config_path)

        except FileNotFoundError:
            raise FileNotFoundError(
                f"файл конфигурации по пути {config_path} не найден"
            )

        data_root_folder = data.get("data_root_folder", None)
        if data_root_folder is None:
            raise ValueError(f"в конфигурации не указан data_root_folder")
        output_folder = data.get("output_folder", None)
        if output_folder is None:
            raise ValueError(f"в конфигурации не указан output_folder")

        Config.data_root_folder = data_root_folder
        Config.output_folder = output_folder
