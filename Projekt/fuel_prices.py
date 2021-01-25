from bs4 import BeautifulSoup
from requests import get as http_get

from Projekt.fuels import *

URL = "https://www.orlen.pl/PL/DlaBiznesu/HurtoweCenyPaliw/Strony/default.aspx"


def get_page(url):
    page = http_get(url)
    if page.status_code != 200:
        print("Nie można pobrać strony! Błąd ", page.status_code)
        exit(1)
    else:
        return page


def parse_float_fuel_price(number):
    try:
        number = number[0] + number[2:5]
        return float(number) / 1000

    except ValueError as e:
        print("Błąd przy konwertowaniu ceny: ", e)
        return 0


def add_vat(price):
    return round(price / 0.78, 2)


def get_fuels_table(page):
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find("table", class_=["tableLight", "orlen-styled-table"])


def get_table_rows(fuel_table):
    return fuel_table.find_all("tr")[1:]


def get_fuel_data_from_row(row):
    data = row.text.strip().splitlines()
    price = parse_float_fuel_price(data[1])
    fuel = Fuel(data[0], add_vat(price))
    return fuel


def get_fuels_data(rows):
    fuels = []
    for row in rows:
        fuel_data = get_fuel_data_from_row(row)
        fuels.append(fuel_data)

    return fuels


def get_fuels():
    page = get_page(URL)
    fuel_table = get_fuels_table(page)
    rows = get_table_rows(fuel_table)
    fuels = get_fuels_data(rows)

    return fuels


def get_date():
    page = get_page(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.findAll("table",
                          {
                              "class": "s4-wpTopTable",
                              "border": "0",
                              "cellpadding": "0",
                              "width": "100%"
                          })
    date_paragraph = tables[1].findChildren("p")[0]
    spans = date_paragraph.findChildren("span")
    return spans[0].text


def store_fuels_to_file(fuels):
    current_date = get_date()
    with open("fuels {}.txt".format(current_date), "w", encoding="utf-8") as file:
        for fuel in fuels:
            file.write(str(fuel) + "\n")


if __name__ == '__main__':
    date = get_date()
    fuels = get_fuels()

    print("\n\nCeny paliw z dnia {}\n".format(date))

    for fuel in fuels:
        print(fuel)

    store = input("Zapisać ceny do pliku? y/n : ")

    if store.lower() == "y":
        store_fuels_to_file(fuels)
