import re
import keyword

#Läser en fil och returnerar den som en lista
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file: #Läs in filen som file
        a_list = file.readlines()                       #Skapar en lista med varje rad som ett stärngelement
    return a_list                                       #Returnerar listan

#Räknar förekomsten av ordkombinationer i en sträng, i samtliga element av a_list
def ref_list(a_list, in_order=False):
    freq = {}                                           #Tomt lexikon
    for index, line in enumerate(a_list, start=1):      #För varje element(rad) i a_list
        line = re.sub(r'#.*$', '', line)                #Ta bort oönskade tecken 
        wordlist = re.findall(r'[a-zA-ZåäöÅÄÖ]+', line) #Hitta alla ordkombinationer
        for word in wordlist:                           #För varje element i wordlist
            if word in freq:                            #Om det finns som nyckel i freq
                freq[word].append(index)                #Lägg till värdet för index 
            elif keyword.iskeyword(word) == False:      #Om inte, kolla att det inte är ett ett keyword
                freq[word] = [index]                    #Lägg till nyckeln i lexikonet med värde index
    if in_order == True:                                #Om argumentet in_order == True 
        freq = sorted(freq.items())                     #Sortera lexikonet                   
    return freq                                         #Returnerar lexikonet


filename = '/home/doez/Prog1/OU3/freq.py'               #Sparar sökvägen för den fil vi vill öppna i variabeln filename
text = read_file(filename)                              #Öppnar filen med funktionen read_file och sparar den i variabeln text

for index, line in enumerate(text, start=1):            #För varje element i text med start index = 1
        print(index,' ',line, end='')                   #Skriv ut index följt av elementet
print('\n\n')

print('Referenslista: ')                                  
for e in ref_list(text, in_order=True):                 #För varje element givet av funtionen ref_list
    print('\t',f'{e[0]}      \t{e[1]}', end='\n')       #Skriv ut nyckeln och dess värdepar(idexeringen)
    
    