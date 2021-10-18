# TEXT
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

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
garpike and stingray are also present.'''
]

# Login credentials
LOGIN = {
    "Bob": "123",
    "Ann": "pass123",
    "Mike": "password123",
    "Liz": "pass123",
    "Vojta": "heslo123"
}

# Separator
# Used to separate parts of the program

SEPARATOR = "-" * 50


### START OF APP

print(SEPARATOR, "                TEXT ANALYZER APP", SEPARATOR, sep="\n")

# Login form
print("Please enter your username and password", SEPARATOR, sep="\n")

username = input("Username: ").title()
password = input("Password: ")

if LOGIN.get(username) == password:
    print(SEPARATOR, "Welcome to the app, " + username, sep="\n")
    print("We have 3 texts to be analyzed.")
else:
    print("Username or password is incorrect..")
    exit()

# Selecting text that we want to analyze
print(SEPARATOR, "Enter a number btw. 1 and 3.", sep="\n")
input_text = int(input("To select: "))

if input_text not in range(1,4):    # Zde jeste dodelat tak aby odpovidalo poctu indexu v listu, aktualne na pevno receno rozmezi, kdyz se prida dalsi text do listu nebude to fungovat spravne.
    print(SEPARATOR, "Your selection is out of range. Qutting..", SEPARATOR, sep="\n")
    exit()
else:
    print(SEPARATOR)

# Clear specific text - chtelo by predelat do comprehension zapisu
list_words = TEXTS[input_text - 1].split()
                                                #### POTREBA SE ZBAVIT V TEXTU 1 30N!

without_numbers = []

for number in list_words:
    clear_number = number.strip("0123456789")   # ocisteni cisel
    without_numbers.append(clear_number)

clear_text = []

for word in without_numbers:
    clear_word = word.strip(",.-_)(")   # ocisteni znaku
    clear_text.append(clear_word)

without_empty_strings = []

for string in clear_text:
    if string != "":
        without_empty_strings.append(string)




number_of_words = len(without_empty_strings)    # POCET SLOV V TEXTU
######################################

title_words = []

for letter in without_empty_strings:
    if letter.istitle():
        title_words.append(letter)
        if len(letter) < 2:
            title_words.remove(letter)


number_of_title_words = len(title_words)    # POCET SLOV ZACINAJICICH NA VELKE PISMENO
######################################

upper_string = []

for upper in without_empty_strings:
    if upper.isupper():
        upper_string.append(upper)
        if len(upper) <= 1:
            upper_string.remove(upper)


number_of_upper_strings = len(upper_string)     # POCET SLOV KTERE JSOU PSANE VELKYMI PISMENY
######################################

lower_string = []

for lower in without_empty_strings:
    if lower.islower():
        lower_string.append(lower)


number_of_lower_strings = len(lower_string)     # POCET SLOV KTERE JSOU PSANE MALYMI PISMENY
######################################

number_count = []

for count in list_words:
    if count.isdigit():
        number_count.append(count)



count_of_numbers = len(number_count)    # POCET CISEL KTERE JSOU V TEXTU
######################################

list_sum_numbers = []

for prevod in number_count:
    list_sum_numbers.append(int(prevod))


sum_numbers = sum(list_sum_numbers)     # SOUCET VSECH CISEL V TEXTU
######################################


### Statistics of text, counts of words, numbers, etc.

print(f"""
There are {number_of_words} words in the selected text.
There are {number_of_title_words} titlecase words.
There are {number_of_upper_strings} uppercase words.
There are {number_of_lower_strings} lowercase words.
There are {count_of_numbers} numeric strings.
The sum of all the numbers {sum_numbers}.
""")
print(SEPARATOR)

## counting lenght of lettes in stringis, saving to dict keys vs values.
count_letters = []

for table in without_empty_strings:
    lenght = 0

    for char in table:
        lenght += 1
    count_letters.append(lenght)

numbers_sorted = {}

for i in count_letters:
    if i in numbers_sorted:
        continue
    numbers_sorted[i] = count_letters.count(i)


## Print result of counting as star "*"
## That means key | numbers of "*" as representation of value | value

for k, v in sorted(numbers_sorted.items()):      # k = count, v = value
    print(f"{k}   | {'*' * v } | {v} ")





print(SEPARATOR)




