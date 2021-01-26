#Fuel prices

##Spis treści
* [Wprowadzenie](#wprowadzenie)
* [Technologie](#technologie)
* [Uruchomienie](#uruchomienie)
* [Funkcjonalności](#funkcjonalności)
* [Działanie](#działanie)
* [Uwagi](#uwagi)


## Wprowadzenie
Jesty to program używający web scrappingu do odszukania, pobrania i web 
wypisania listy paliw w raz z ich cenami. Ceny odnoszą się do rynku polskiego 
i są pobierane ze strony Orlenu, czołowego dostawcy paliw w Polsce.


## Technologie
* Python 3
* Requests
* BeautifulSoup

## Uruchomienie

```
$ python3 fuel_prices_py
```

## Funkcjonalności

Główną funkcjonalnością programu jest pobranie cen paliw. Jest to robine
automatycznie od razu po uruchomieniu programu. Wyświetlana jaest lista 
paliw z ceniami za litr oraz datą. 

Dodatkową funkcjonalnością jest zapisanie danych do pliku. Aby to zrobić 
należy po uruchomieni programu jako argument przy zapytaniu podać y/Y. 
Wtedy program zapisze ceny do pliku .txt o nazwie "fuels < data >.txt" 

![image](https://user-images.githubusercontent.com/50678871/105915185-b4530080-602f-11eb-82a6-3b3c1684c771.png)

## Działanie 
Po uruchomieniu, program za pomocą metody `get` z biblioteki `requests` pobiera stronę, 
a następnie parsuje ją przy pomocy biblioteki `BeautifulSoup`. Następnie szuka odpowiedniej
tabeli przechowującej dane o paliwach i ich cenach. Po odszukaniu tych danych program
przelicza ceny z **zł/m<sup>3</sup>** na **zł/l** oraz dodaje 22% podatku VAT. Po skończeniu 
wyświetla pobrane dane i pyta czy zapisać do pliku.

## Uwagi
* Ceny są podawanie dla rynku polskiego
* Ceny paliw na stronie są podane w **zł/m<sup>3</sup>**, program przelicza to na **zł/l**
* Ceny paliw na stronie są bez podatku VAT. Przy pobieraniu cen program dolicza 22% podatku 
  (wysokość podatku na styczeń 2021)
