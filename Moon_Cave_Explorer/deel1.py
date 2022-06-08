from formules import *
from matplotlib.pyplot import *

#vraag E
def calc_speeds_plot():#met deze hulpfunctie zorg ik ervoor dat ik de afstand van elke vector in de lijst bereken en in een nieuwe lijst plaats
    list_calc_speeds_plot= []
    for i in calc_speeds((37.5,64.95),(0,-1.622),0.2,400):
        list_calc_speeds_plot.append(mag(i))
    return list_calc_speeds_plot

subplot(2,1,1)
title("snelheid in functie van de tijd",fontsize=12)#de grafiek moet best in fullscreen bekeken worden of anders overlappen de namen van de titel en de x-as
xlabel("tijd")
ylabel("snelheid")
grid(True)
plot(calc_speeds_plot())

#vraag F
list_calc_positions= calc_positions((0,0),(37.5,64.95),0.2,400)

def calc_positions_plot_x():#ik maak deze hulpfuncties omdat ik de z coordinaten van de vector niet op mijn grafiek wil zien
    list_calc_positions_plot_x= []
    for i in list_calc_positions:
        list_calc_positions_plot_x.append(i[0])
    return list_calc_positions_plot_x

def calc_positions_plot_y():
    list_calc_positions_plot_y= []
    for i in list_calc_positions:
        list_calc_positions_plot_y.append(i[1])
    return list_calc_positions_plot_y

subplot(212)
title("positie in functie van de tijd",fontsize=12)
xlabel("tijd")
ylabel("positie")
grid(True)
text(220,2200,"$x-coordinaten$")#gebruik van LaTeX
text(350,850,"$y-coordinaten$")#ik weet dat er een spelfout is maar dubbelpunt op de o accepteren ze niet op de grafiek
                               #en ik heb al aan de hand van LaTeX geprobeerd een dubbele punt op de O te krijgen maar er loopt iets mis.
plot(calc_positions_plot_x())#ik vind dat het plotten van de x en y waarden apart mooier weergeeft wat de beweging zal zijn dan plot(x,y)
plot(calc_positions_plot_y())
show()

