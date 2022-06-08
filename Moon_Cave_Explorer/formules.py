from visual import *
from math import *

'''sphere().visible=false#dubbele restart bug'''

#vraag A
v0= vector()
def inc_speed(v,a,dt):
    v= vector(v)
    v0.x= v.x
    v0.y= v.y#vorige snelheid(=vt-1)wordt v0 waardoor je nieuwe v berekent.
    return v0+ vector(a)*dt

#vraag B
p0= vector()
def inc_position(p,v,dt):
    p= vector(p)#ik had het idee om een aparte hulpfunctie te maken om de startende p een vector te maken.
                #hierdoor zouden we later bij calc_postions minder stappen moeten verichten bij grote n(omdat je maar 1 keer p=vector(p) doet)
                #want nu doen we bij elke inc_position berekening p=vector(p) maar dit is niet nodig als het al een vector is
                #vanaf de 2de keer in calc_positions. Ik heb het uitgeprobeerd en voor 1 of andere rede krijg ik
                #totaal andere getallen op mijn grafiek dus heb ik het verwaarloosd.
    p0.x= p.x#vorige positie(=pt-1)wordt p0 waardoor je nieuwe p berkent.
    p0.y= p.y
    return p0+ v*dt

#vraag C
def calc_speeds(v,a,dt,n):
    list_calc_speeds= []#een lege lijst binnen de functie maken.
    for i in range(n):
        v= inc_speed(v,a,dt)#er wordt altijd een nieuwe v gebruikt aan de hand van v0= v
                            #omdat het binnen de for-loop zit.
        list_calc_speeds.append(v)
    return list_calc_speeds#nadat de for-loop gedaan is, toont hij de lijst.


#vraag D
def calc_positions(p,v,dt,n):
    list_calc_positions= []
    help_speed_list = calc_speeds(v,(0,-1.622),dt,n)#we berekenen eerst de snelheidlijst en onthouden het door het een naam te geven.
                                                #hierdoor kunnen we makkelijk een getal uit de lijst kiezen bij het berekenen van de positie.
    for i in range(n):
        p= inc_position(p,help_speed_list[i],dt)
        list_calc_positions.append(p)
    return list_calc_positions

####################################################################################
#deel2 extra formules

def acceleration(F_fire=0):
    a= vector(0,-1.622*10)+ vector(F_fire)
    return a
    
def F_fire(angle):
    return vector(200*cos(angle),200*sin(angle))

