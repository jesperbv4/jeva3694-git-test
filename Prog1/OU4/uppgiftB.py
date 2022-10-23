import matplotlib.pyplot as plt
import re
import csv

#Läser in en csv-fil och returnerar ett lexikon
def load_csv(filename):                 
    with open(filename, 'r') as csvFile:    #Läs in filen som csvFile
        reader = csv.reader(csvFile)        #Skapar ett reader objekt med funktionen reader
        header = next(reader)               #Sparar första raden i header och går vidare till nästa
        data = {row[1].lower(): list(map(float, row[3:])) for row in reader}    #Bygger ett lexikon nyckeln = kolumn 2, värdet = en lista med varje värde från kolumn 4 och frammåt. För varje element i reader objektet
        return data                         #Returnerar lexikonet

#Läser in en .dat fil och returnerar ett lexikon med dess data
def load_dat(filename):
    with open(filename, 'r') as file:       #Läs in filen som file
        lines = file.readlines()            #Sparar en lista med varje rad i filen som ett element i lines
        data =  {}                          #Skapar ett tomt lexikon
        for line in lines:                          #För varje element i lines
            line = list(map(float, line.split()))   #En lista med varje värde konverterat till float  
            if line[0] not in data:                 #Om värdet på första elementet inte finns som nyckel
                data[line[0]] = []                  #Skapa en nyckel utan värde
            if line[1] == 5:                        #Om värdet på andra elementet == 5
                data[line[0]].append(line[3])       #Lägg till värdet som ett par till nyckeln
        
        return data                                 #Returnerar Lexikonet

#Skapar genomsnittsdata för en värdet på en samling element i ett nyckelintervall                           
def mean_data(data):
        
        mean_data1 = [mean(data[year]) for year in data if year in range(1700, 1800)]   #Sparar data för intervall i en lista
        mean_data2 = [mean(data[year]) for year in data if year in range(1800, 1900)]   #Sparar data för intervall i en lista
        mean_data3 = [mean(data[year]) for year in data if year in range(1900, 2000)]   #Sparar data för intervall i en lista
        mean_data4 = [mean(data[year]) for year in data if year in range(2000, 3000)]   #Sparar data för intervall i en lista
        
        return [mean_data1, mean_data2, mean_data3, mean_data4] #Returnerar en lista där varje element fås får ovan

#Returnerar genomsnittsvädet av samtliga element i en lista    
def mean(m):
    return sum(m)/len(m)                 
                    
def smooth_a(a_list,n):
    my_list= [x for x in a_list]
    for i in range(n):
        my_list.insert(0, a_list[0])
        my_list.insert(len(my_list), a_list[len(a_list)-1])
    new_list = [sum(my_list[i-n:i+n+1])/(2*n+1) for i in range(n, len(my_list)-n)]
    return new_list
      
                               
filename = '/home/doez/Prog1/OU4/uppsala_tm_1722-2020.dat'  #Sparar sökvägen för den fil vi vill öppna i variabeln filename
data = mean_data(load_dat(filename))                        #importerar data med load_data till mean_data och sparar i variabeln
xlabels = ['1700', '1800', '1900', '2000']                  #Lista med stängar som etiketter till x axeln
fig, ax = plt.subplots()                                    #Skapar figurens ram med Matplotlib
ax.boxplot(data)                                            #Ritar upp värder på data med funktionen boxplot

ax.set(xlabel='Daily air temperature and pressure series for Uppsala (1722-1998),\nClimate Change, 53:213-252.', ylabel='Temperatursprindnig', title='Medeltemperatur på några platser i maj, 1722-2020.', xticklabels=(xlabels)) #Titlar för axlar

fig.savefig("temp.png")                                     #Sparar figuren som .png
plt.show()                                                  #Visar figuren i ett nytt fönster