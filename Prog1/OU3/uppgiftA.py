import re

def part2(e):
    return e[1]

#Läser en fil och returnerar den som en lista
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file: #Läs in filen som file
        a_list = file.readlines()                       #Skapar en lista med en sträng(hela texten) som element
    print(a_list)                                       #Skriver ut innehållet i lsitan                         
    return a_list                                       #Returnerar listan 

#Räknar förekomsten av ordkombinationer i en sträng, i samtliga element av a_list
def word_list(a_list):          
    freq = {}                                           #Tomt lexikon  
    for line in a_list:                                 #För varje element i listan
        wordlist = re.findall(r'[a-zA-ZåäöÅÄÖ]+', line) #Skapa en lista med varje ordkombinaion som element
        for count, word in enumerate(wordlist):         #Iterera över alla ord i listan wordlist
            if word in freq:                            #Om ordet finns som nyckel i freq
                freq[word] += 1                         #Öka dess värde med +1
            else:                                       #Annars
                freq[word] = 1                          #Lägg till nyckeln med värde                                  
    print('\n')
    print('Texten innehåller: ',count,'ord, varav: ', len(freq),'unika.')   #Skriver ut antal ord och unika ord
    return freq                                                             #Returnerar lexikonet

#Soreterar en lista efter värdet på nycklarna i fallande eller stigande ordning
def in_order(a_list, reverse=True):
    if reverse == True:
        sorted_list = sorted(a_list.items(), key=part2, reverse=True)
    else:
        sorted_list = sorted(a_list.items(), key=part2, reverse=False)
    return sorted_list                                  



filename = '/home/doez/Prog1/text.txt'                  #Sparar sökvägen för den fil vi vill öppna i variabeln filename
text = read_file(filename)                              #Öppnar filen med funktionen read_file och sparar den i variabeln text
wordlist = word_list(text)                              #Kallar på funktionen word_list och sparar resultatet i variabeln wordlist
n = int(input('Antal av de vanligaste orden: '))        #Variebel för antal av de vanligaste orden
m = int(input('Antal av de ovanligaste orden: '))       #Variabel för antal av de ovanligaste orden

words = in_order(wordlist, True)                        #Sorterar listan med funktionen in_order   
print('De', n ,'vanligaste orden :')                    #
for index,e in enumerate(words[:n], start=1):           # 
    print(f'{e[1]:2d}: {e[0]},', end='')                # Formatering för utskrift av de n vanligaste orden
    if index % 8 == 0:                                  #
        print()                                         #
print('\n\n')                                           #

print('De', m ,'ovanligaste orden :')                   #
for index,e in enumerate(words[-m:], start=1):          #
    print(f'{e[1]:2d}: {e[0]},', end='')                # Formatering för utskrift av de m ovanligaste orden
    if index % 8 == 0:                                  #
        print()                                         #