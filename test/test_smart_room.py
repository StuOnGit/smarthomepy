import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom
from mock.senseair_s8 import SenseairS8


class TestSmartRoom(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_something(self, mock_object: Mock):
        # This is an example of test where I want to mock the GPIO.input() function
        pass

    @patch.object(GPIO, "input")
    def test_check_room_occupancy_returns_true(self, mock_gpio: Mock):
        sr = SmartRoom()
        mock_gpio.return_value = True
        occupacy = sr.check_room_occupancy()
        self.assertTrue(occupacy)

    @patch.object(GPIO, "input")
    def test_check_room_occupancy_returns_false(self, mock_gpio: Mock):
        sr = SmartRoom()
        mock_gpio.return_value = False
        occupacy = sr.check_room_occupancy()
        self.assertFalse(occupacy)

    @patch.object(GPIO, "input")
    def test_check_enough_light_returns_true(self, mock_gpio: Mock):
        sr = SmartRoom()
        mock_gpio.return_value = True
        enough_light = sr.check_enough_light()
        self.assertTrue(enough_light)

    @patch.object(GPIO, "input")
    def test_check_enough_light_returns_false(self, mock_gpio: Mock):
        sr = SmartRoom()
        mock_gpio.return_value = False
        enough_light = sr.check_enough_light()
        self.assertFalse(enough_light)

    @patch.object(GPIO, "output")
    def test_manage_light_level_on(self, mock_gpio: Mock):
        sr = SmartRoom()
        mock_gpio.side_effect = [True, True]
        sr.manage_light_level()
        self.assertTrue(sr.light_on)

    @patch.object(GPIO, "output")
    def test_manage_light_level_on(self, mock_gpio: Mock):
        sr = SmartRoom()
        mock_gpio.side_effect = [False, False]
        sr.manage_light_level()
        self.assertFalse(sr.light_on)

    @patch.object(Adafruit_BMP280_I2C,"temperature", new_callable=PropertyMock )
    def test_manage_window_open(self, temperature: PropertyMock):
        sr = SmartRoom()
        temperature.side_effect =  [18, 20]
        sr.manage_window()
        window_is_open = sr.window_open
        print(sr.window_open)
        self.assertTrue(window_is_open)

    @patch.object(Adafruit_BMP280_I2C, "temperature", new_callable=PropertyMock)
    def test_manage_window_closed(self, temperature: PropertyMock):
        sr = SmartRoom()
        temperature.side_effect = [20, 18]
        sr.manage_window()
        window_is_open = sr.window_open
        print(sr.window_open)
        self.assertFalse(window_is_open)