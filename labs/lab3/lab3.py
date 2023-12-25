from lab3_oop.rectangle import Rectangle 
from lab3_oop.square import Square
from lab3_oop.circle import Circle
from lab3_oop.color import Color
import requests
import json

color = Color(255, 255, 255)
rect = Rectangle(10, 3, color)
print(rect)

square = Square(3, color)
print(square)

circle = Circle(3, color)
print(circle)

def get_time():
    response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")
    return json.loads(response.text)["datetime"]
print("Current time: " + get_time()+"\n")