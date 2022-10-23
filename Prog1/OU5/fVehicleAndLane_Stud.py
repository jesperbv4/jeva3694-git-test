# Studentversion av filen.
# Klassen Vehicle är helt klar och skall ej ändras
# Klassen Lane är nästan klar, där skall...
#     metoden number_in_lane uppdateras av dig!


# Denna klass är helt färdig
class Vehicle:
    """Representerar fordon i en trafiksimulering"""

    def __init__(self, destination, borntime):   # ex på anrop: v = Vehicle('W',time)
        self.destination = destination
        self.borntime = borntime

    def __str__(self):  # returnerar en strängrepresentation av Vehicle-objektet.
        return f'Vehicle({self.destination}, {self.borntime})'
    
    def get_destination(self):
        return self.destination
    
    def get_borntime(self):
        return self.borntime


# Klassen Lane är nästan klar, metoden number_in_lane skall uppdateras.
class Lane:
    """Representerar en fil med positioner för ev. fordon"""

    #Skapar en fil som är tom, dvs inga fordon
    def __init__(self, length):     
        # Initiera alla element till None (tomma positioner)
        self._the_lane = [None for x in range(length)]

    # returnerar en strängrepresentation av filen, exvis [ WSW S WSW]
    def __str__(self):   
        res = '' 
        for s in self._the_lane:
            if s == None:
                res = res + '.'
            else:
                res = res + s.get_destination()
        return '[' + res + ']'

    # Lägger in ett fordon sist i filen, om det är ledigt där.
    def enter(self, vehicle):
        if self.last_free():
            self._the_lane[-1] = vehicle
        else: # Programmet avbryts med följande felmeddelande:
            raise Exception('Impossible to enter lane: position not free')

    # returnerar True om sista positionen är tom (ledig), annars False
    def last_free(self):
        return self._the_lane[-1] == None

    # Flyttar alla fordon ett steg framåt i filen, men bara om det är möjligt
    def step(self):
        for i in range(len(self._the_lane)-1):
            if self._the_lane[i] == None:  # position i är ledig?
                self._the_lane[i] = self._the_lane[i+1]  # Ja, flytta från pos i+1 till i
                self._the_lane[i+1] = None               # och gör pos i+1 ledig.

    def get_first(self):
        return self._the_lane[0]
    
    # Tar bort fordonet som är i filens första position och
    # returnera det fordonet
    def remove_first(self):
        v = self._the_lane[0]
        self._the_lane[0] = None # Första pos sätts till ledig
        return v

    # DENNA METODS KROPP MÅSTE ÄNDRAS
    # Räknar och returnerar antalet fordon som finns i filen
    def number_in_lane(self):
        return len([i for i in self._the_lane if i != None]) 


def demo_lane():
    """För att demonstera klassen Lane"""
    a_lane = Lane(10)   # Skapa ett Lane-objekt med plats för 10 fordon
    print(a_lane)       # Skriv ut Lane-objektet (filen) för att se hur det ser ut
    print('  Antal fordon i filen:', a_lane.number_in_lane())
    t = 0               # tiden är initialt noll
    v = Vehicle('N', t) # Skapa ett fordon med borntime 0 och destination N
    a_lane.enter(v)     # Placera fordonet sist i filen
    print(a_lane)       # Skriv ut Lane-objektet
    print('  Antal fordon i filen:', a_lane.number_in_lane())

    a_lane.step()       # Flytta fordonen ett steg framåt i filen
    print(a_lane)       # Skriv ut Lane-objektet
    print('  Number in lane:', a_lane.number_in_lane())
    # Simulera 20 tidssteg mha en loop
    while t <= 20:
        t += 1
        print('\nt =',t)  # Skriv ut värdet av tiden
        # Vid vartannat tidssteg gör följande...
        if t % 2 == 0:
            u = Vehicle('S', t) # Skapa ett fordon, borntime t och destination S
            a_lane.enter(u)     # Placera fordonet sist i filen
        a_lane.step()           # Flytta fordonen ett steg framåt i filen
        
        # Vid vart 3:e tidssteg, gör följande ...
        if t % 3 == 0:
            # Ta bort fordonet i första pos i filen och skriv ut det fordonet
            print('  out: ', a_lane.remove_first())
        # Skriv ut hur många fordon det är totalt i filen
        print(a_lane)           # Skriv ut Lane-objektet
        print('  Number in lane:', a_lane.number_in_lane())

def main():
    print('\nLane demonstration')
    demo_lane() 

if __name__ == '__main__':  # If this file is the main program, you are running:
    main()                  # Call the main function above
    
# When the Python interpreter reads a python file, it defines
# the special variable __name__
# If you are running your module as the main program,
# the interpreter will assign the hard-coded string "__main__" to the __name__ variable
# If this python file is demo_light() imported by another program, and they run that program, the
# main function is not called
