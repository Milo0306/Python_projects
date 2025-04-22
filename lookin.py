
x = "milosz banana"
   
while True :
    tekst = input("Podaj wartość do wyszukania w milosz banana:")
    if tekst == ("exit") :
        print('Wychodzę z programu')
        break  
    elif tekst in x: 
        print ('Znalazłem!')
    else :
        print ("nie znalazłem")
