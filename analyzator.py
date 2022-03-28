# Projekt - textovy analyzator
# texty k analyze

TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply- 
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

# zaregistrovani uzivatele

uzivatele = {
    'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'
}

# definice oddelovace
oddelovac = ('-' * 50)
oddelovac2 = (''*20)


# privitani uzivatelu

print(oddelovac)
print('Welcome to the app. Please log in:')

# vstup uzivatele - jmeno, heslo

uzivatel = input('USERNAME: ')
heslo = input('PASSWORD: ')

# overeni uzivatelu

if uzivatele.get(uzivatel) != heslo:
    print('unregistered user,', 'terminated the program..')
    exit()

# vyber textu

print(oddelovac)
vyber = [1,2,3]

print('We have 3 texts to be analyzed.')

# overeni spravnosti vstupu pri zadani textu

while True:
    vyber_textu = (input('Enter a number btw. 1 and 3 to select: '))
    if vyber_textu.isnumeric() and int(vyber_textu) in range(1, 4):
        break
    else:
        print(''
              'You must enter the correct input:'
              ' 1,2,3'
              )


print(oddelovac)
vyber_textu = int(vyber_textu)
text = TEXTS[vyber_textu - 1]

# cisteni textu

vycistit_text = text.split()
slova = []

while vycistit_text:
    slovo = vycistit_text.pop()
    slovo = slovo.strip('.,:/;-')
    if slovo: slova.append(slovo)

vycisteny_text = dict()
titlecase = 0
lowercase = 0
uppercase = 0
numeric = 0
counts = {}
num_sum = 0

# zjisteni delky
i = 0
while i < len(slova):
    if slova[i].istitle():
        titlecase = titlecase + 1
    elif slova[i].isupper():
        uppercase = uppercase + 1
    elif slova[i].islower():
        lowercase = lowercase + 1
    elif slova[i].isnumeric():
        numeric = numeric + 1
        num_sum = num_sum + int(slova[i])
    l = len(slova[i])

    counts[l] = counts.get(l, 0) + 1
    i = i + 1
print('There are ' + str(len(slova)) + ' words in the selected text.')
print('There are ' + str(titlecase) + ' titlecase words.')
print('There are ' + str(uppercase) + ' uppercase words.')
print('There are ' + str(lowercase) + ' lowercase words.')
print('There are ' + str(numeric) + ' numeric strings.')
print('If we summed all the numbers in this text we would get: ' + str(num_sum))
print(oddelovac)

# vysledky v sloupcovem grafu

#hlavicka
print(oddelovac)
print(f"LEN|     OCCURENCES     |NR.")
print(oddelovac)

#vysledky
lengths = sorted(counts)
i = 0
while i < len(lengths):
    length = lengths[i]
    vyskyt = counts[length]
    if len(str(length)) == 1:
        str_len = ' ' + str(length)
    else:
        str_len = str(length)
    print(" " + str_len + "|" + '*' * vyskyt, " ".center(19-vyskyt) + "|"+ str(vyskyt))
    i = i + 1

