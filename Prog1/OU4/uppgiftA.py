import csv
import matplotlib.pyplot as plt

#Läser in en csv-fil och returnerar ett lexikon
def load_csv(filename):                 
    with open(filename, 'r') as csvFile:    #Läs in filen som csvFile
        reader = csv.reader(csvFile)        #Skapar ett reader objekt med funktionen reader
        header = next(reader)               #Sparar första raden i header och går vidare till nästa
        data = {row[1].lower(): list(map(float, row[3:])) for row in reader}    #Bygger ett lexikon nyckeln = kolumn 2, värdet = en lista med varje värde från kolumn 4 och frammåt. För varje element i reader objektet
        return data                         #Returnerar lexikonet

def smooth_a(a_list,n):
    my_list= [x for x in a_list]
    for i in range(n):
        my_list.insert(0, a_list[0])
        my_list.insert(len(my_list), a_list[len(a_list)-1])
    new_list = [sum(my_list[i-n:i+n+1])/(2*n+1) for i in range(n, len(my_list)-n)]
    return new_list
      
                               
filename = '/home/doez/Prog1/OU4/CO2Emissions_filtered.csv'         #Sparar sökvägen för den fil vi vill öppna i variabeln filename
data = load_csv(filename)                                           #Öppnar filen med funktionen load_csv och sparar den i variabeln data
keys = [['dnk', 'b'], ['fin', 'orange'], ['isl', 'g'], ['nor', 'r'], ['swe', 'm']]  #Lista med element för data vid plotning
time = list(range(1960, 2015))                                      #Skapar en lista för värden på x-axeln

fig, ax = plt.subplots()                                            #Skapar figurens ram med Matplotlib
for key in keys:                                                    #För varje element i keys
    ax.plot(time, data[key[0]],color=key[1], linestyle=':')         #Ritar upp data. Första elementet i key ger data, andra ger färg
    ax.plot(time, smooth_a(data[key[0]], 5), color=key[1], label=key[0])    #Ritar upp avrundad data från fnk smooth_a
    
ax.set(xlabel='Year', ylabel='CO2 Emissions (kt)', title='Yearly Emissions of CO2 in the Nordic Countries') #Titlar för axlar

fig.savefig("plot.png")                                             #Sparar figuren som .png
plt.legend()                                                        #Visar etiketter för varje graf
plt.show()                                                          #Visar figuren i ett nytt fönster
