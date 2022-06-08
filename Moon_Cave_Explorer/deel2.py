from formules import *
from vectorutils import intersect
import time
import red_zone as RZ


class Start_game(object):#zorgt voor uitleg controls
    def __init__(self):
        self.scene1= display(title= "Moon Cave Explorer",x=0, y=0, center= (0,0,0), background= color.black,
                        range= (40,40,10),userzoom = False,userspin = False,width= 1100, height= 750)#ik heb een width en een height toegevoegd omdat op mac
                                                                                                     #fullscreen geen effect heeft
        self.scene1.fullscreen= True
        self.start_text= label(pos= (0,5,0),text='     Controls:\n escape = pause\n    up, left, right\n    click to start',
                               xoffset= 0,yoffset= 0,height=30,border= 10,font= 'sans')
    def start(self):#wacht voor een click en start het spel
        self.scene1.waitfor('click')
        self.scene1.delete()
        s= Spacecraft()
        s.play()


###################### View #########################
class View(object):
    def  __init__(self):#display van het spel
        self.scene1= display(title= "Moon Cave Explorer",x=0, y=0, center= (0,0,0), background= color.black,
                        range= (40,40,10),userzoom = False,userspin = False,width= 1100, height= 750)
        self.scene1.fullscreen= True
        self.f5_fuel_item= frame()#fuel_item
        self.f3_fuel= frame()#fuel frame
        self.f2_anti_fuel= frame()#anti_fuel frame
        self.f1_spacecraft= frame()#raket frame
        
###################### Fuel #########################
        self.fuel= shapes.rectangle(pos= (35.05,15,0),width= 4,height= 10,roundness= 0.1)
        self.fuel_box= curve(pos= [(32.5,20.5),(32.5,9.5),(37.5,9.5),(37.5,20.5)],radius= 0.2,color= color.blue)
        extrusion(shape= self.fuel,color= color.yellow,frame= self.f3_fuel)
        self.anti_fuel=shapes.rectangle(pos= (35.05,25),width= 4,height= 10.1)
        extrusion(shape= self.anti_fuel,color= color.black,frame= self.f2_anti_fuel)
        
##################### Fuel_item #####################
        #ik kon hiervan een aparte klasse maken en ervoor zorgen dat ik makkelijk meerdere fuel_items kan toevoegen, maar het was eerder een test om te kijken of een
        #mechanisme zoals het heropvullen van de fuel werkt in samenhang met de pauze/restartknop
        self.fuel_itm1= Polygon([(1,2),(0,2),(0,0),(1,0)])
        self.fuel_itm2= Polygon([(0.75,2.30),(0.25,2.30),(0.25,2),(0.75,2)])
        self.fuel_item= extrusion(shape= self.fuel_itm1+ self.fuel_itm2,color= color.yellow,frame= self.f5_fuel_item)
        self.f5_fuel_item.pos=(-30,14)
        
class Background_view(object):#weergave achtergrond
    def __init__(self):
        self.f4_background= frame()#background frame/deze frame heeft geen toepassing in het spel op dit moment
        self.green_zone= shapes.line(start= (-36,-15),end= (-31,-15), np= 20,thickness= 0.4)#groene zone
        self.red_zone1= curve(pos= RZ.red_zone_list1,radius= 0.1,color= color.red,frame= self.f4_background)#rode zone deel 1(aan de hand van geimporteerde lijst)
        self.red_zone2= curve(pos= RZ.red_zone_list2,radius= 0.1,color= color.red,frame= self.f4_background)#rode zone deel 2
        self.blue_zone= shapes.line(start= (25,-15),end= (32,-15),np= 20,thickness= 0.4)#blauwe zone
        extrusion(shape= self.blue_zone, color= (0,0.2,0.8),frame= self.f4_background)#blauwe zone
        extrusion(shape= self.green_zone,color= (0.1,0.8,0.1),frame= self.f4_background)#groene zone
        self.text=label(pos=(35,9,0),text='Fuel', xoffset= 0,yoffset= 0,height=15,border= 2,font= 'sans')#fuel text

class Spacecraft_view(View):#weergave schip
    def __init__(self):
        View.__init__(self)#alle eigenschappen van view overgeerfd     
        Background_view()#background wordt weergegeven
        '''self.hitbox= curve(pos= [(0,3),(1.6,-0.05),(-1.6,-0.05),(0,3)], radius= 0.1,color= color.red, frame= self.f1_spacecraft)#hitbox gebruikt voor limits()'''
        #indien je de hitbox wilt bekijken afkappingstekens verwijderen
        
        self.top= Polygon([(-0.5,2),(0,3),(0.5,2)])#basis van het schip
        self.bottom= Polygon([(-0.2,0.3),(0,0.8),(0.2,0.3)])#steunen
        self.fire= Polygon([(-0.2,0.2),(0,-0.3),(0.2,0.2)])#vuur
        self.rectangle1= shapes.rectangle(pos= (0,1.3),width= 1,height= 1.5)#basis van het schip
        self.rectangle2= shapes.rectangle(pos= (0.7,0.5),width= 0.2, height= 1, rotate= pi/4)#steunen
        self.rectangle3= shapes.rectangle(pos= (-0.7,0.5),width= 0.2, height= 1, rotate= -pi/4)#steunen
        self.circle1= shapes.circle(pos= (1.2,0),radius = 0.4,np= 64,angle1= 0,angle2= pi)#voetsteun
        self.circle2= shapes.circle(pos= (-1.2,0),radius= 0.4,np= 64,angle1= 0,angle2= pi)#voetsteun
        self.circle3= shapes.circle(pos= (0,0.3),radius= 0.2,np= 64,angle1= 0,angle2= -pi)#vuur
        self.ellipse= shapes.ellipse(pos= (0,1.2),width= 0.5, height= 0.9, np= 64)#kokpit
        
        self.Fire= extrusion(shape= self.circle3+ self.fire, color= color.red, frame= self.f1_spacecraft)#=vuur
        self.steunen= extrusion(shape= self.rectangle2+ self.rectangle3+ self.bottom, color= color.yellow,frame= self.f1_spacecraft)#=steunen
        self.voetsteunen= extrusion(shape= self.circle1+ self.circle2, color= color.white,frame= self.f1_spacecraft)#=voetsteunen
        self.schip= extrusion(shape= self.top+ self.rectangle1, color= color.green,frame= self.f1_spacecraft)#=basis van het schip
        self.kokpit= extrusion(shape= self.ellipse, color= (0.1,0.2,0.7),frame= self.f1_spacecraft)#=kokpit
        
        self.cheater_text= label(pos=(0,5,0),text='Oh oh oh oh, you little cheater?', xoffset= 0,yoffset= 0,height=30,border= 10,font= 'sans')
        self.win_text= label(pos=(0,5,0),text='You won!', xoffset= 0,yoffset= 0,height=30,border= 10,font= 'sans')#wordt later in limits(),pause() gebruikt als je wint
        self.cheater_text.visible= False
        self.win_text.visible= False
        self.Fire.visible= False
        
        self.f1_spacecraft.pos= (-33.5,-14.6)#startpositie
        
################# explosion view ####################################
        self.explosion_list= []
        
        self.expl1= shapes.star(pos= (0,0.5),n= 10)#alle verschillende sterren voor de explosie in explosion()
        self.expl2= shapes.star(pos= (0,0.5),n= 16)
        self.expl3= shapes.star(pos= (0,0.5),n= 22)
        self.expl4= shapes.star(pos= (0,0.5),n= 23)
        self.expl5= shapes.star(pos= (0,0.5),n= 24)
        self.expl6= shapes.star(pos= (0,0.5),n= 24)
        self.expl7= shapes.star(pos= (0,0.5),n= 24)
        
        self.explosion1= extrusion(shape= self.expl1,color= color.red,scale= 0.4,frame= self.f1_spacecraft)#alle sterren worden gevisualiseerd
        self.explosion2= extrusion(shape= self.expl2,color= (1,0.5,0.2),scale= 1.2,frame= self.f1_spacecraft)
        self.explosion3= extrusion(shape= self.expl3,color= (1,0.2,0.1),scale= 1.6,frame= self.f1_spacecraft)
        self.explosion4= extrusion(shape= self.expl4,color= (0.8,0.4,0),scale= 1.9,frame= self.f1_spacecraft)
        self.explosion5= extrusion(shape= self.expl5,color= (0.6,0.1,0.2),scale= 2.1,frame= self.f1_spacecraft)
        self.explosion6= extrusion(shape= self.expl6,color= (0.3,0,0.1),scale= 2.3,frame= self.f1_spacecraft)
        self.explosion7= extrusion(shape= self.expl7,color= (0.1,0,0),scale= 2.5,frame= self.f1_spacecraft)
        
        self.explosion1.visible= False#alles onzichtbaar maken
        self.explosion2.visible= False
        self.explosion3.visible= False
        self.explosion4.visible= False
        self.explosion5.visible= False
        self.explosion6.visible= False
        self.explosion7.visible= False
        
        self.explosion_list.append(self.explosion1)#alle sterren worden in een lijst gezet voor mooier gebruik in explosion() 
        self.explosion_list.append(self.explosion2)
        self.explosion_list.append(self.explosion3)
        self.explosion_list.append(self.explosion4)
        self.explosion_list.append(self.explosion5)
        self.explosion_list.append(self.explosion6)
        self.explosion_list.append(self.explosion7)
        
#################### Buttons #######################################
        self.pause_text= label(pos=(0,5,0),text='Pause', xoffset= 0,yoffset= 0,height=30,border= 10,font= 'sans')#alle buttons maken indien je crashed of op pause drukt
                                                                                                                 #wordt gebruikt in pause(), explosion() en restart()
        self.restart_text= label(pos=(0,0,0),text='Restart', xoffset= 0,yoffset= 0,height=30,border= 10,font= 'sans')
        self.exit_text= label(pos=(0,-5,0),text='Exit', xoffset= 0,yoffset= 0,height=30,border= 10,font= 'sans')
        self.cheater_button_text= label(pos=(0,-10,0),text='Cheat', xoffset= 0,yoffset= 0,height=30,border= 10,font= 'sans')
        
        self.exit_text.visible= False
        self.restart_text.visible= False
        self.pause_text.visible= False
        self.cheater_button_text.visible= False
        
class Spacecraft(Spacecraft_view):
    def __init__(self):
########################### View ######################################
        Spacecraft_view.__init__(self)#overerving van alle views
######################## Game_Calc ####################################
        self.cheater_points= 0#gebruikt in explosion() om te kijken welke tekst je mag tonen als je wint
        self.angle= pi/2
        self.angle_sign= 0#zorgt ervoor welke richting hij moet roteren na het loslaten van de knop bij update()
        self.stay_rotating= 80#welke snelheid hij zal moeten roteren nadat je de knop hebt losgelaten in update()
        self.velocity= vector(0,0,0)#startsnelheid = 0 in next_position()
        self.acceleration= acceleration()#functie gemaakt in formules.py om versnelling te berekenen
        self.green_or_blue_zone_hit= 1#gebruikt in limits() en play() zodat je niet kan roteren als je zich op het groene of blauwe platform bevindt
        self.future_pos_test= self.f1_spacecraft.pos#wordt gebruikt in next_position() en limits()
                                                    #zodat het spel op voorhand al weet of je het goene/blauwe platform raakt en ervoor kan zorgen
                                                    #dat je perfect op het platform land in plaats van in het platform vast te zitten
        self.fuel_taken= 0#gebruikt in limits() en restart() om aan te geven of je de bonus fuel al genomen hebt of niet
    def play(self):
       self.dt= 0.01
       self.t= 0
       self.eind= 1#een andere manier om True te gebruiken in de while functies, maar het is niet echt nodig want er wordt altijd 'break' gebruikt
       while True:
           rate(25)
           time.sleep(self.dt)#wacht een tijdsinterval af
           if self.t!= 2:#kijkt of het spel moet stoppen met updaten of niet, self.t wordt vooral gebruikt in limits()
               if self.scene1.kb.keys:#kijkt of een knop wordt ingedrukt
                   key=self.scene1.kb.getkey()#neemt de laatst ingedrukte knop
                   if key== 'up':
                       self.green_or_blue_zone_hit= 0
                       self.update(1,0,0)
                   elif key== 'left':
                       if self.green_or_blue_zone_hit== 0:
                           self.update(0,1,0)
                   elif key== 'right':
                       if self.green_or_blue_zone_hit== 0:
                           self.update(0,0,1)
                   elif key== 'esc':
                       self.t= 2
                       self.pause()
                   else:
                       if self.green_or_blue_zone_hit== 0:
                           self.update(0,0,0)
               else:
                   if self.green_or_blue_zone_hit== 0:
                       self.update(0,0,0)
           else:
               break#stopt de while functie
       self.explosion()
    def update(self,up,left,right):
        self.up= up
        self.left= left
        self.right= right
        self.f2_anti_fuel.y-= 0.002#fuel wordt continu verlaagd vanaf hij vliegt, het stopt echter wanneer op groene of blauwe zone maar hervat vervolgens
        self.test_fuel()
        
        if self.stay_rotating<=850:#hoek/pi verkleinen zodat de hoeksnelheid vertraagd nadat je links/rechts knop hebt losgelaten
            self.stay_rotating+= 12
        else:
            self.angle_sign= 0#zorgt ervoor dat er geen rotatie meer is als stay_rotating te groot is geworden (na ongeveer 4sec draaien)
            
        if self.up== 1:
            self.f2_anti_fuel.y-=0.02#als je up drukt gaat de fuel sneller naar beneden
            self.next_position(1)
            self.Fire.visible= True
            
        elif self.left== 1:
            self.angle_sign= 1#zorgt ervoor welke richting hij moet roteren na het loslaten van de knop
            self.stay_rotating= 70
            self.next_position(0)
            self.Fire.visible= False
            
        elif self.right== 1:
            self.angle_sign= -1
            self.stay_rotating= 70
            self.next_position(0)
            self.Fire.visible= False
            
        else:#als je niets hebt gedaan
            self.next_position(0)
            self.Fire.visible= False
        self.limits()
        self.angle+=self.angle_sign*(pi/self.stay_rotating)#veranderen van de hoek voor later gebruik bij frame f1_spacecraft,limits()
        self.f1_spacecraft.rotate(angle= self.angle_sign*(pi/self.stay_rotating),axis= (0,0,1),origin= self.f1_spacecraft.pos)
                                                                                                        #het draaien van het schip zelf aan de hand van
                                                                                                        #self.angle_sign die het teken zal bepalen           
            
    def next_position(self,up):#berekenen van volgende positie
        self.up= up
        if self.up== 1:
            self.velocity= inc_speed(self.velocity,acceleration(F_fire(self.angle)),self.dt)#extra vuurkracht toevoegen aan de valversnelling met een
                                                                                            #functie in formules.py
            self.f1_spacecraft.pos= inc_position(self.f1_spacecraft.pos,self.velocity,self.dt)
        
        else:
            self.velocity= inc_speed(self.velocity,acceleration(),self.dt)
            self.f1_spacecraft.pos= inc_position(self.f1_spacecraft.pos,self.velocity,self.dt)
            
        if self.f1_spacecraft.x<= -30 and self.f1_spacecraft.y<= -13:#kijken naar de toekomstige positie zodat we een vloeibare landing maken;komt voor in limits()
            self.future_pos_test= inc_position(self.f1_spacecraft.pos,self.velocity,self.dt)#test voor groene zone
        if self.f1_spacecraft.x>= 23 and self.f1_spacecraft.y<= -13:
            self.future_pos_test= inc_position(self.f1_spacecraft.pos,self.velocity,self.dt)#test voor blauwe zone
    def test_fuel(self):#kijkt of de fuel nog niet op is door de y positie te bekijken van de anti_fuel
        if self.f2_anti_fuel.y<= -9.990:
            self.Fire.visible= False
            while self.t< self.eind:#als fuel op is heb je geen controle meer over je schip en val je naar beneden
                rate(25)
                time.sleep(self.dt)
                self.next_position(0)
                self.limits()
    def all_points(self,lst):#hulpfunctie voor intersect om meerdere lijnstukken van de achtergrond te berekenen
        True_or_False=[]
        l= 0
        for i in range(len(lst)-1):
            l+= 1
            True_or_False.append(intersect(self.A,self.B,lst[i],lst[l]))
            True_or_False.append(intersect(self.B,self.C,lst[i],lst[l]))
            True_or_False.append(intersect(self.C,self.A,lst[i],lst[l]))
        return True_or_False
    def pause(self):#deze functie zorgt ervoor dat alle toepassingen van de buttons in gang worden gezet
        self.pause_text.visible= True
        self.restart_text.visible= True
        self.exit_text.visible= True
        self.cheater_text.visible= False
        self.win_text.visible= False
        while self.t>self.eind:
            rate(25)
            time.sleep(self.dt)
######################### esc button ###############################
            if self.scene1.kb.keys:#kijkt of esc wordt ingedrukt
               key=self.scene1.kb.getkey()
               if key== 'esc':
                   self.pause_text.visible= False
                   self.restart_text.visible= False
                   self.exit_text.visible= False
                   break#stopt de while loop
            if 4>= self.scene1.mouse.pos[0]>= -4:#kijkt of de muis in de buurt is van de buttons
########################### restart ######################################
                if 0>= self.scene1.mouse.pos[1]>= -4:
                    self.restart_text.color= color.yellow
                    if self.scene1.mouse.clicked:
                        self.scene1.mouse.getclick()#ik plaats altijd een getclick() achter
                                                    #wegens een bug waardat het spel denkt dat ik altijd click en zo ongewilt restart of dergerlijke
                        self.restart()
                        for i in range(100):#dit is een poging om een glitch te voorkomen als je de restart spamclickt, het is echter niet volledig opgelost
                            if self.scene1.mouse.clicked:
                                self.scene1.mouse.getclick()
                        break
                else:
                    self.restart_text.color= color.white
######################### pause #########################################
                if 5>= self.scene1.mouse.pos[1]>= 1:
                    self.pause_text.color= color.yellow
                    if self.scene1.mouse.clicked:
                        self.scene1.mouse.getclick()
                        self.pause_text.visible= False
                        self.restart_text.visible= False
                        self.exit_text.visible= False
                        for i in range(100):
                            if self.scene1.mouse.clicked:
                                self.scene1.mouse.getclick()
                        break
                else:
                    self.pause_text.color= color.white
######################## exit ########################################
                if -5>= self.scene1.mouse.pos[1]>= -9:
                    self.exit_text.color= color.yellow
                    if self.scene1.mouse.clicked:
                        self.scene1.mouse.getclick()
                        exit()
                else:
                    self.exit_text.color= color.white
            else:
                self.exit_text.color= color.white
                self.pause_text.color= color.white
                self.restart_text.color= color.white
        self.exit_text.color= color.white
        self.pause_text.color= color.white
        self.restart_text.color= color.white       
        self.play()#indien geclicked op iets zal hij de whileloop verbreken en play() terug afspelen waardoor het spel hervat

    def restart(self):#deze functie wordt gebruikt in pause() en explosion()
        self.steunen.visible= True
        self.schip.visible= True
        self.kokpit.visible= True
        self.voetsteunen.visible= True
        self.f1_spacecraft.visible= True
        self.f5_fuel_item.visible= True
        self.cheater_button_text.visible= False
        self.exit_text.visible= False
        self.pause_text.visible= False
        self.restart_text.visible= False
        self.Fire.visible= False
        self.win_text.visible= False
        self.cheater_text.visible= False
        
        self.velocity= (0,0)
        self.f1_spacecraft.pos= (-33.5,-14.6)
        self.delta_angle_reset= ((pi/2)-self.angle)#ik kan geen gebruik maken van de f1_spacecraft.axis want dan komt er een bug nadat je op groene/blauwe zone crashed
        self.f1_spacecraft.rotate(angle= self.delta_angle_reset,axis= (0,0,1),origin= self.f1_spacecraft.pos)#dus moet ik "manueel" draaien
        self.angle+= self.delta_angle_reset
        self.stay_rotating= 80
        self.green_or_blue_zone_hit= 1
        self.angle_sign= 0
        self.f2_anti_fuel.y=0
        self.cheater_points= 0
        self.fuel_taken= 0
    def limits(self):#het scherm is in 4 kwadranten verdeeld waardoor het minder punten moet testen per keer
        self.A= (self.f1_spacecraft.x+ 3*cos(self.angle),self.f1_spacecraft.y+ 3*sin(self.angle))#rotatie van de hitbox
        self.B= (self.f1_spacecraft.x+ 1.6*sin(self.angle)- 0.05*cos(self.angle),self.f1_spacecraft.y-0.05*sin(self.angle)- 1.6*cos(self.angle))
        self.C= (self.f1_spacecraft.x- 1.6*sin(self.angle)- 0.05*cos(self.angle),self.f1_spacecraft.y-0.05*sin(self.angle)+ 1.6*cos(self.angle))
###################### lists ########################################################
        if self.f1_spacecraft.x<=0:
            if self.f1_spacecraft.y<5:
                for i in self.all_points(RZ.RZL1):#uitleg waarom ik niet self.red_zone1 gebruik is in red_zone.py
                    if i== True:
                        self.t= 2
                for i in self.all_points(RZ.RZL5):#alle lijnstukken in de 2de lijst en het 3de kwadrant(in goniometrische cirkel) van de red_zone
                    if i== True:
                        self.t= 2
            else:
                for i in self.all_points(RZ.RZL2):
                    if i== True:
                        self.t= 2
                for i in self.all_points(RZ.RZL6):
                    if i== True:
                        self.t= 2
                for i in self.all_points([(-29,16),(-30,16),(-30,14),(-29,14)]):#hitbox van de fuel_item
                    if i== True:
                        if self.fuel_taken== 0:
                            self.fuel_taken= 1
                            self.f5_fuel_item.visible= False
                            self.f2_anti_fuel.y+= 2#hervult de fuel
        else:
            if self.f1_spacecraft.y>=5:
                for i in self.all_points(RZ.RZL4):
                    if i== True:
                        self.t= 2
                for i in self.all_points(RZ.RZL8):
                    if i== True:
                        self.t= 2
            else:
                for i in self.all_points(RZ.RZL3):
                    if i== True:
                        self.t= 2
                for i in self.all_points(RZ.RZL3_anti_bug):#dit is een extra lijst om een gekende bug in red_zone.py op te lossen(meer uitleg staat daar).
                    if i== True:
                        self.t= 2
                for i in self.all_points(RZ.RZL7):
                    if i== True:
                        self.t= 2
                        
####################### groene zone #####################################
        if self.future_pos_test.x<= -30 and self.future_pos_test.y<= -13:#kijkt of de raket dicht bij het groene platform is
            for i in self.all_points([(-36,-14.7),(-31,-14.7)]):#hitbox groen platform
                if i== True:
                    if self.velocity.y<-8:#indien je te snel valt
                        self.t= 2#zorgt voor de start van explosion() omdat self.t==2 in play()
                    else:
                        self.f1_spacecraft.pos= (self.f1_spacecraft.pos.x,-14.5+abs(1.2*cos(self.angle)))
                        self.green_or_blue_zone_hit= 1
                        self.velocity= vector(0,0,0)
                        self.Fire.visible= False
                        if ((pi/2)+(pi/90))<self.angle<=(5*pi)/8:#als hij het platform raakt, zorg ervoor dat hij terug recht komt te staan
                            #waarom pi/2 + pi/90 => omdat dit een bug voorkomt waarbij de hoek juist pi/2 moet zijn om te stoppen met de for-loops af te gaan
                            #het is eigenlijk een rekenfout van python omdat hij eindig rekent (pi/2)/20=> zorgt voor gemiddeld een fout van 1.2 graden
                            self.delta_angle= (self.angle-(pi/2))/20
                            for i in range(20):#roteren tot ongeveer 90 graden
                                rate(30)
                                self.angle-= self.delta_angle
                                self.f1_spacecraft.rotate(angle= -self.delta_angle,axis= (0,0,1),origin= (self.f1_spacecraft.x- 1.6,self.f1_spacecraft.y-0.05))
                                time.sleep(self.dt)
                            self.stay_rotating= 851
                        if ((pi/2)-(pi/90))>self.angle>=(3*pi)/8:
                            self.delta_angle= ((pi/2)-self.angle)/20
                            for i in range(20):
                                rate(30)
                                self.angle+= self.delta_angle
                                self.f1_spacecraft.rotate(angle= self.delta_angle,axis= (0,0,1),origin= (self.f1_spacecraft.x+ 1.6,self.f1_spacecraft.y-0.05))
                                time.sleep(self.dt)
                            self.stay_rotating= 851                      
                        if self.angle> (5*pi)/8 or self.angle< (3*pi)/8:
                            self.t= 2
                            
########################## blauwe zone ###########################################
        if self.future_pos_test.x>= 24 and self.future_pos_test.y<= -13:#kijkt of de raket dicht bij het blauwe platform is
            for i in self.all_points([(25,-14.7),(32,-14.7)]):#hitbox blauw platform
                if i== True:
                    if self.velocity.y<-8:
                        self.t= 2
                    else:
                        self.f1_spacecraft.pos= (self.f1_spacecraft.pos.x,-14.5+abs(1.2*cos(self.angle)))
                        self.green_or_blue_zone_hit= 1
                        self.velocity= vector(0,0,0)
                        self.Fire.visible= False
                        if ((pi/2)-(pi/90))<= self.angle<= ((pi/2)+(pi/90)):
                            if self.cheater_points== 1:#als je eerder op cheat gedrukt hebt nadat je gecrashed waart zal hij een andere win tekst weergeven 
                                self.cheater_text.visible= True
                            else:
                                self.win_text.visible= True
                        if ((pi/2)+(pi/90))<self.angle<=(5*pi)/8:
                            self.delta_angle= (self.angle-(pi/2))/20
                            for i in range(20):
                                rate(30)
                                self.angle-= self.delta_angle
                                self.f1_spacecraft.rotate(angle= -self.delta_angle,axis= (0,0,1),origin= (self.f1_spacecraft.x- 1.6,self.f1_spacecraft.y-0.05))
                                time.sleep(self.dt)
                            self.stay_rotating= 851
                            if self.cheater_points== 1:
                                self.cheater_text.visible= True
                            else:
                                self.win_text.visible= True
                        if ((pi/2)-(pi/90))>self.angle>=(3*pi)/8:
                            self.delta_angle= ((pi/2)-self.angle)/20
                            for i in range(20):
                                rate(30)
                                self.angle+= self.delta_angle
                                self.f1_spacecraft.rotate(angle= self.delta_angle,axis= (0,0,1),origin= (self.f1_spacecraft.x+ 1.6,self.f1_spacecraft.y-0.05))
                                time.sleep(self.dt)
                            self.stay_rotating= 851
                            if self.cheater_points== 1:
                                self.cheater_text.visible= True
                            else:
                                self.win_text.visible= True
                        if self.angle> (5*pi)/8 or self.angle< (3*pi)/8:
                            self.t= 2
    def explosion(self):
        self.Fire.visible= False
        self.steunen.visible= False
        self.schip.visible= False
        self.kokpit.visible= False
        self.voetsteunen.visible= False
        l=0
        for i in range(6):#gaat de lijst af, eerder gemaakt in spacecraft_view() waardoor je een animatie krijgt
            l+= 1
            self.explosion_list[i].visible= False
            self.explosion_list[l].visible= True
            sleep(0.03)
        self.explosion_list[6].visible= False
        self.restart_text.visible= True#na de explosie geeft hij weer een menu waaruit je kan kiezen(restart,exit,cheat?)
        self.exit_text.visible= True
        self.cheater_button_text.visible= True
        while True:
            rate(25)
            time.sleep(self.dt)
################### restart ########################
            if 4>= self.scene1.mouse.pos[0]>= -4:
                if 0> self.scene1.mouse.pos[1]>= -4:
                    self.restart_text.color= color.yellow
                    if self.scene1.mouse.clicked:
                        self.scene1.mouse.getclick()
                        self.restart()
                        self.break_while_function= 0
                        for i in range(100):
                            if self.scene1.mouse.clicked:
                                self.scene1.mouse.getclick()
                        break
                else:
                    self.restart_text.color= color.white
################ exit #################################
                if -5>= self.scene1.mouse.pos[1]>= -9:
                    self.exit_text.color= color.yellow
                    if self.scene1.mouse.clicked:
                        self.scene1.mouse.getclick()
                        exit()
                else:
                    self.exit_text.color= color.white
################# cheat button ############################
                if -10> self.scene1.mouse.pos[1]>= -14:
                    self.cheater_button_text.color= color.yellow
                    if self.scene1.mouse.clicked:
                        self.scene1.mouse.getclick()
                        self.Fire.visible= True
                        self.steunen.visible= True
                        self.schip.visible= True
                        self.kokpit.visible= True
                        self.voetsteunen.visible= True
                        self.f1_spacecraft.visible= True
                        self.f1_spacecraft.pos= (28,-5)
                        self.velocity= (0,0)
                        self.fuel_taken= 0
                        self.f5_fuel_item.visible= True
                        self.delta_angle_reset= ((pi/2)-self.angle)
                        self.f1_spacecraft.rotate(angle= self.delta_angle_reset,axis= (0,0,1),origin= self.f1_spacecraft.pos)
                        self.angle+= self.delta_angle_reset
                        self.angle_sign= 0
                        self.f2_anti_fuel.y=0
                        self.cheater_button_text.visible= False
                        self.exit_text.visible= False
                        self.restart_text.visible= False
                        self.cheater_text.visible= False
                        self.win_text.visible= False
                        self.cheater_points= 1
                        self.stay_rotating= 851
                        self.break_while_function= 1#zorgt ervoor dat ik de while functie kan breken nadat ik op cheat druk
                        for i in range(100):
                            if self.scene1.mouse.clicked:
                                self.scene1.mouse.getclick()
                            if self.scene1.kb.keys:#dit zorgt ervoor dat indien je keys spamt, het geen effect heeft op het nieuwe spel (bv 'esc' en 'up' spamming)
                                self.scene1.kb.getkey()
                        break
                else:
                    self.cheater_button_text.color= color.white
            else:
                self.cheater_button_text.color= color.white
                self.exit_text.color= color.white
                self.restart_text.color= color.white
        if self.break_while_function== 1:
            self.play()
        else:
            self.cheater_button_text.color= color.white
            self.exit_text.color= color.white
            self.restart_text.color= color.white
            for i in range(100):
                if self.scene1.kb.keys:
                       key=self.scene1.kb.getkey()
                if self.scene1.mouse.clicked:
                       self.scene1.mouse.getclick()
            self.play()
#################################################################################################################
s= Start_game()
s.start()

