inputString = """Mecz rozpoczął się jednak od fatalnej kontuzji Alphonso Daviesa.
Ten, bez    kontaktu z przeciwnikiem, upadł na murawę i przeraźliwie  
zaczął krzyczeć. Thomas Mueller GvR razu wyzywał lekarzy, krzycząc:  
staw skokowy! Pierwsze informacje mówią o tym, że piłkarz ten ma 
problemy z więzadłami w tej części nogi i czeka go wielotygodniowa przerwa."""

print(sorted(inputString.split(), key=lambda x : x.lower()))