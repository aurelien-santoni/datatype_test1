import random
import string
v=0
j=0
replay = "oui"
while replay == "oui" :
    x = random.randint (1,3)
    if x == 1 : 
        y = random.randint(-100,100) 
        real_type= "1"
    if x == 2 :
        y= random.uniform (-100.0,100.0)
        y=y*100
        y= int(y)
        y= y/100 
        real_type = "2"
    if x == 3:
        r= random.randint (1,10)
        def random_character (t) :
            return''.join(random.choice(string.ascii_lowercase) for i in range (t))
        y = random_character(r)
        real_type = "3"
    print ("quel est le type de ",y,"1, 2 ou 3 ?")
    type1= str(input("1 pour int, 2 pour float et 3 pour string "))
    while type1 != "1" and type1 != "2" and type1 != "3":
        type1 = str(input("merci de répondre par 1, 2 ou 3 "))
    if type1 == real_type :
        print ("bravo")
        v=v+1
    else :
        print ("faux dommage")
    j=j+1
    print ("tu as ",v,"bonnes réponses pour",j,"essais")
    replay= str(input("on continue? oui ou non "))
    while replay != "oui" and replay != "non" :
        replay= str(input("merci de répondre par oui ou non"))
print("ta note final est donc",v,"/",j)