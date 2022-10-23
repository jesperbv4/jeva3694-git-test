
freq = {}               # Skapa ett tomt lexikon
for c in text:          # Iterera över tecknen
    if c.isalpha():        # Vi intresserar oss bara för bokstäver
        c = c.lower()      # Skiljer inte på små och stora
        if c in freq:      # Om denna bokstav redan finns som nyckel
            freq[c] += 1   # Öka dess frekvens
        else:              # annars
            freq[c] = 1    # Lägg in den med frekvensen 1
print(freq)	