"""
The function works like a simple calculator, performing addition, subtraction, multiplication and division after entering any two numbers.
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def calculator():
  działanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1-Dodawanie, 2-Odejmowanie, 3-Mnożenie, 4-Dzielenie: "))
  if 0 < działanie < 5:
    a = float(input("Podaj pierwszy składnik: "))
    b = float(input("Podaj drugi składnik: "))
    if działanie == 1:
      dodawanie = a + b
      logging.info(f"Dodaję {a} i {b}.")
      print(f"Wynik to: {dodawanie}")
    elif działanie == 2:
      odejmowanie = a - b
      logging.info(f"Odejmuję {b} od {a}.")
      print(f"Wynik to: {odejmowanie}")
    elif działanie == 3:
      mnożenie = a * b
      logging.info(f"Mnożę {a} i {b}")
      print(f"Wynik to: {mnożenie}")
    elif działanie == 4:
      dzielenie = a / b
      logging.info(f"Dzielę {a} przez {b}")
      print(f"Wynik to: {dzielenie}")
  else:
    print("Podaj liczbę od 1 do 4!!!")
    calculator()

calculator()