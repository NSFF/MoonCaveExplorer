from vis import *

################# background points ###################################
red_zone_list1= [(-36,-15),(-36,-1),(-28,-1),(-10,-3),(-13,4),(-15,4),
 (-17,5),(-22,6),(-26,5),(-32,8),(-36,13),(-36,16),(-34,18),
 (-30,21),(-24,20),(-16,19),(-10,17),(-8,19),(-6,16),(-2,12),
 (3,9),(8,1),(9,-5),(11,-6),(13,-3),(11,6),(8,11),(5,16),
 (4,19),(5,20),(10,19),(15,18),(18,17),(26,15),(28,10),(32,0),(32,-15)]
red_zone_list2= [(25,-15),(24,0),(21,6),(19,10),(16,11),(18,8),(21,-1),(19,-4),(15,-10),
 (12,-11),(8,-12),(2,-6),(-2,-1),(-3,4),(-9,11),(-19,13),(-9,11),(-3,4),
 (-2,-1),(-6,-12),(-9,-15),(-13,-12),(-20,-15),(-27,-9),(-31,-15)]

##################### intersect lists #############################

def red_zone_list_split(lst,a,b,c,d):#functie om kleinere lijsten te maken, deze functie is echter niet waterdicht voor alle lijsten.
                                     #maar ik vind het handiger als ik mijn achtergrond aanpas en in 4 kwadranten verdeel waardoor het spel sneller verloopt
    help_end_list= lst
    r_help= len(lst)
    lst1= []
    for i in range(len(lst)):
        if a== 1:
            if lst[i][0]<=0:
                if lst[i][1]<5:
                    lst1.append(lst[i])#lijst van x<=0 en y<5
                    r=i+1#hiermee onthouden we de plaats van het laatste element in de lijst
        if b== 1:
            if lst[i][0]<=0:
                if lst[i][1]>=5:
                    lst1.append(lst[i])#lijst van x<=0 en y>=5
                    r=i+1
        if c== 1:
            if lst[i][0]>0:
                if lst[i][1]<5:
                    lst1.append(lst[i])#lijst van x>0 en y<5
                    r=i+1
        if d== 1:
            if lst[i][0]>0:
                if lst[i][1]>=5:
                    lst1.append(lst[i])#lijst van x> en y>=5
                    r=i+1
    if r<r_help:
        lst1.append(help_end_list[r])#ik voeg er nog 1 bij zodat het interval overschreden wordt en geen lijnstukken over laat
        return lst1
    else:
        return lst1

RZL1= red_zone_list_split(red_zone_list1,1,0,0,0)#ik maak al op voorhand allerlij lijsten zodat
                                                 #ik minder stappen moet doen bij het berekenen van limits()
RZL2= red_zone_list_split(red_zone_list1,0,1,0,0)
RZL3= red_zone_list_split(red_zone_list1[:len(red_zone_list1)-2],0,0,1,0)#er ontstont een bug waardoor er een onzichtbare lijn
                                                                         #ontstond midden in de achtergrond omdat 2 punten van red_zone_list1(13,-6) en (32,0)
                                                                         #niet opeenvolgend zijn van elkaar waardoor er een lijn tussen beide wordt gemaakt
                                                                         #in mijn all_points functie
RZL3.insert(0,(3,9))
RZL3_anti_bug= [(32,0),(32,-15)]
RZL4= red_zone_list_split(red_zone_list1,0,0,0,1)
RZL4.insert(1,(8,1))
RZL5= red_zone_list_split(red_zone_list2,1,0,0,0)
RZL6= red_zone_list_split(red_zone_list2,0,1,0,0)
RZL7= red_zone_list_split(red_zone_list2,0,0,1,0)
RZL8= red_zone_list_split(red_zone_list2,0,0,0,1)

