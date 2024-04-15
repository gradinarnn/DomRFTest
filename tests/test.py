import os
import unittest

from PIL.Image import Image
from PIL.ImageDraw import ImageDraw

from services.imager import Imager
from services.shape_creator import ShapeCreator
from shapes.shapes import Circle, Rectangle
from utils.utils import read_data_from_json


class ReadJSONFileTest(unittest.TestCase):
  def setUp(self):
    self.path = './tests/tests_files/test_config.json'
    self.reader = read_data_from_json

  def test_read_json_config_file(self):
    data = self.reader(self.path)
    self.assertTrue( isinstance(data, dict))
    self.assertIn('data_root_folder', data)
    self.assertIn('output_folder', data)



class CreateImageTest(unittest.TestCase):
  def setUp(self):
    self.path = './tests/tests_files/test_image_data.json'
    image_data = read_data_from_json(self.path)
    self.figures_list = ShapeCreator.parse_figures_data(data=image_data)

  def test_parse_circle(self):

    circle = self.figures_list[0]
    self.assertTrue(isinstance(circle, Circle))
    self.assertEqual(circle.Radius, 9)






