#################################################
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

#Kod jest poprawny pod wzgledem skladni, jednak mozna
# poprawic kilka rzeczy aby bylo to napisane zgodnie ze sztua.
# Chodzi o usuniecie sredniow, nawiasu przy if oraz rozdzielenie
# zmiennych x i y do osobnych lini


#################################################
# for i in "qwerty": if ord(i) < 100: print (i)

# Kod sie nie skompiluje poniewaz jezeli kod w "bloku" petli
# jest dluzszy niz jedna linijka powinien byc zapisany w nowej
# linii z odpowiednim wcieciem. TO taj jakby odpowidnik {} z innych
# jezykow. NIe trzeba ich dawac jezeli kod bloku jest jednolinijkowy


#################################################

for i in "axby": print (ord(i) if ord(i) < 100 else i)

#Kod jest poprawnie napisanyy
