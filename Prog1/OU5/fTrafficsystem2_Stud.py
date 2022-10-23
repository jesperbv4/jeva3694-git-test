# Given studentversion av:
# Trafik system 1
# Två filer (lane1, lane2) och ett trafikljus (light) mellan dem.
# Och en kö, före lane2..
# lane1 - light - lane2 - kö
# Uppgift:
# I klassen TrafficSystem1 skall metoden number_in_system()
# modifieras.

from fVehicleAndLane_Stud import Lane, Vehicle
from fLight_Stud import Light
from fDestinations import Destinations
from time import sleep  # behövs för sleep-fkn
import statistics

class TrafficSystem2:
    """Representerar ett trafik system"""

    # Konstruktorn
    def __init__(self):
        self.time = 0                       # Tiden är noll, initialt
        self.lane = Lane(11)                # Fil innan delning
        self.lane_west = Lane(8)            # Fil för att svänga west
        self.lane_south = Lane(8)           # Fil för att svänga south
        self.light_west = Light(14, 6)      # Trafikljus för west
        self.light_south = Light(14, 4)     # Trafikljus för south
        self.queue = []                     # Kön längst till höger är initialt tom
        self.generator = Destinations()     # Skapar ett Destinations-objekt
        self.south = []                     # Lista för att spara värden från fordon som lämnar södra filen
        self.west = []                      # Lista för att spara värden från fordon som lämnar den västra filen
        self.time_queue = 0                 # Variabel för antal tidssteg det varit kö
        self.time_blocked = 0               # Variabel för antal tidssteg det varit stopp 
        self.blocked = False                # Boolean för att vis om det är stopp 
        
    # Skriver ut trafiksystemet vid aktuell tid som exvis
    # "26: [WSSSW](G)[SWWSW]  ['W', 'S']""
    # dvs tiden, filen efter trafikljuset, trafikljuset, filen framför trafikljuset, kön
    def snapshot(self):
        # Skapa en sträng som representerar kön
        sq = str([x.get_destination() for x in self.queue])
        # Skapa en sträng med värdet på self.time högerjusterat över 4 positioner
        stime = '%4d' % (self.time) + ": "
        snr = '%2d' % (self.number_in_system())
        # Bygg upp strängen med alla dess beståndsdelar
        blocked = ' ' 
        # Skriver "*" om det är stopp i fildelningspunkten
        if self.blocked == True:
            blocked = '*'
        # Strängformatering för utskrift av systemet
        s = stime + '('+snr+') ' + str(self.light_west) + str(self.lane_west) + blocked + str(self.lane) + "  " + sq 
        b =   str(self.light_south) + str(self.lane_south) 
        print(s)
        print('\t  ', b)    
        
    # Stegar trafiksystemet från vänster till höger
    def step(self):
        self.time += 1          # Nytt tidssteg
        self.traffic_lights()   # Är det grönt 
        self.step_lanes()       # Stega resten av systemet
        self.new_vehicle()      # Skapa ett nytt fordon 
        self.in_queue()
        self.step_lights()

    # Beräknar och returnerar hur många fordon som för tillfället finns i trafikssystemet
    # dvs summan av fordon i de båda filerna (lane1, lane2) och i kön (queue).    
    def number_in_system(self):
        return self.lane_south.number_in_lane() + self.lane_west.number_in_lane() + self.lane.number_in_lane() + len([i for i in self.queue if i != None])
    
    # Kontrollerar om respektive tarfikljus är grönt
    # Om grönt ta bort första fordeonet i filen
    def traffic_lights(self):
        if self.light_west.is_green(): # Om trafikljuset är grönt...
            w = self.lane_west.remove_first()
            if w != None:
                self.west.append(self.time-w.get_borntime())    # Sparar tiden fordonet varit i systemet
        if self.light_south.is_green():
            s = self.lane_south.remove_first()                  
            if s != None:
                self.south.append(self.time-s.get_borntime())   # Sparar tiden fordonet varit i systemet

    # Stegar systemet där plats finns från vänster till höger
    def step_lanes(self):
        self.blocked = False    
        self.lane_west.step()               # Stega västra filen
        self.lane_south.step()              # Stega södra filen
        if self.lane.get_first() != None:   # Om det finns ett fordon innan fildelning
            s = self.lane.get_first()       # Skapa en referens till fordonet
            # Om fordonet ska W och det är ledigt i filen
            if s.get_destination() == 'W' and self.lane_west.last_free():
                # Flytta det till filen
                self.lane_west.enter(self.lane.remove_first())
            # Om det inte är ledigt och trafikljuset är rött(stopp i systemet)
            elif s.get_destination() == 'W' and self.lane_west.last_free()== False and self.light_west.is_green() == False:
                self.time_blocked += 1      # Addera 1 tidssteg till räknaren
                self.blocked = True         # Syetemet är blockerat
            # Om fordonet ska S och det är ledigt i filen
            if s.get_destination() == 'S' and self.lane_south.last_free():
                # Flytta det till filen
                self.lane_south.enter(self.lane.remove_first())
            # Om det inte är ledigt och trafikljuset är rött(stopp i systemet)
            elif s.get_destination() == 'S' and self.lane_south.last_free() == False and self.light_west.is_green() == False:
                self.time_blocked += 1      # Addera ett tidssteg till ränkaren
                self.blocked = True         # Systemet är blockerat
        self.lane.step()                    # Stega filen innan delning

    # Skapa ett nytt fordon med generatorn
    def new_vehicle(self):
        destination = self.generator.step() # Ger S, W eller None från generatorn
        if destination != None: # Om nytt fordon:
            # Skapa fordonet och lägg det sist i kön
            self.queue.append(Vehicle(destination, self.time))

    # Kontrollera kön till lane
    def in_queue(self):
        # Om det finns minst ett fordon i kön OCH sista positionen i lane är ledig:
        if len(self.queue) > 0 and self.lane.last_free():
            # Flytta fordonet från första position i kön till sista position i lane.
            self.lane.enter(self.queue.pop(0))
        # Om det finns fordon i kön
        if len(self.queue) > 0:
            # Addera ett tidssteg till räknaren för kötid
            self.time_queue += 1 

    # Stega trafikljusen        
    def step_lights(self):
        self.light_south.step()
        self.light_west.step()

    # Skriver ut statistik från körningen
    def print_statistics(self):
        # Antal fordon som lämnat systemet + fordonen i systemet
        created_vehicles = len(self.south)+len(self.west)+self.number_in_system()
        # Tidssteg som systemet varit blockerat
        time_blocked = round((self.time_blocked/self.time)*100, 1)
        # Tidssteg som det varit fordon i kön
        time_queue = round((self.time_queue/self.time)*100, 1)
        # Formatering för utskrift
        print('')
        print(f'Statistics after ', self.time ,' timesteps:')
        print('')
        print(f'Created vehicles: ', created_vehicles)
        print(f'In system\t: ', self.number_in_system())
        print('')
        print(f'At exit\t\t' 'West' '\t' 'South')
        print(f'Vehicles out: \t', len(self.west), '\t' , len(self.south))
        print(f'Minimal time: \t', min(self.west), '\t' , min(self.south))
        print(f'Maximal time: \t', max(self.west), '\t' , max(self.south))
        print(f'Mean time: \t', round(statistics.mean(self.west), 1), '\t' , round(statistics.mean(self.south), 1))
        print(f'Median time: \t', round(statistics.median(self.west), 1), '\t' , round(statistics.median(self.south), 1))
        print('')
        print(f'Blocked\t: ',time_blocked,'%')
        print(f'Queue\t: ',time_queue,'%')
        

# Funktion som testkör TrafficSystem2
def main():
    ts = TrafficSystem2()   # En referens till ett Trafficsystem2
    for i in range(100):    # Iterara 100 gånger
        ts.snapshot()       # Kallar på funktionnen snapshot
        ts.step()           # Kallar på funktionen step
        sleep(0.1)          # Vänta 100 ms
    print('\nFinal state:')
    ts.snapshot()
    ts.print_statistics()
    
    

# Testkör main
if __name__ == '__main__':
    main() 

