from Projekt.fuels import *
from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.orlen.pl/PL/DlaBiznesu/HurtoweCenyPaliw/Strony/default.aspx")


def parse_float(number):
    number = number[0] + number[2:5]
    return float(number) / 1000


def get_fuels_table(page):
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find_all("table", class_=["tableLight", "orlen-styled-table"])[0]


def get_fuel_table_rows(fuel_table):
    return fuel_table.find_all("tr")[1:]


def get_fuel_data(row):
    data = row.text.strip().splitlines()
    data[1] = parse_float(data[1])
    return data


def get_fuels():
    fuel_table = get_fuels_table(page)
    fuel_table_rows = get_fuel_table_rows(fuel_table)

    fuels = []
    for row in fuel_table_rows:
        fuel_data = get_fuel_data(row)
        fuels.append(Fuel(fuel_data[0], fuel_data[1]))

    return fuels


print(get_fuels())
