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

usernames = ["bob", "ann", "mike", "liz"]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

separator = "----------------------------------------"

user = input("username:")
password = input("password:")

while user not in usernames:
    try: 
        password == users[user]
    except KeyError:
        print("unregistered user, terminating the program..")
        break
else: 
    if password == users[user]:
        print(separator)
        print(f"Welcome to the app, {user}. \nWe have 3 texts to be analyzed.")
        print(separator)

        num_analysed_text = input("Enter a number btw. 1 and 3 to select: ")

        if not num_analysed_text.isnumeric():
            print("input is not number, terminating the program..") 
        elif int(num_analysed_text) in (1,2,3):
            print(separator)
            chosen_text = TEXTS[int(num_analysed_text) - 1] 
            split_words = chosen_text.split()
            clean_words = [slovo.strip(".,;:") for slovo in split_words]
            num_words = len(clean_words)
            print(f"There are {num_words} words in the selected text.")

            titlecase_words = []
            for word in clean_words:
                if word.istitle() and word.isalpha():
                    titlecase_words.append(word)
            num_titlecase_words = len(titlecase_words)
            print(f"There are {num_titlecase_words} titlecase words.")

            uppercase_words = []
            for word in clean_words:
                if word.isupper() and word.isalpha():
                    uppercase_words.append(word)
            num_uppercase_words = len(uppercase_words)
            print(f"There are {num_uppercase_words} uppercase words.")

            lowercase_words = []
            for word in clean_words:
                if word.islower() and word.isalpha():
                    lowercase_words.append(word)
            num_lowercase_words = len(lowercase_words)
            print(f"There are {num_lowercase_words} lowercase words.")

            numeric_strings = []
            for word in clean_words:
                if word.isdigit():
                    numeric_strings.append(word)
            num_numeric_strings = len(numeric_strings)
            print(f"There are {num_numeric_strings} numeric strings.")

            sum_number_in_text = sum([int(number) for number in numeric_strings])
            print(f"The sum of all the numbers {sum_number_in_text}.")

            print(separator)
            print("LEN|","OCCURES".center(20),"|NR.")
            print(separator)

            len_words = sorted([len(word) for word in clean_words])
            occures = {}

            for lenght in len_words:
                if lenght not in occures:
                    occures[lenght] = 1
                else: 
                    occures[lenght] += 1

            for lenght, occur in occures.items():
                stars = "*" * occur
                starts_left = stars.ljust(20)
                lenght_right = str(lenght).rjust(2)
                print(f"{lenght_right} | {starts_left} | {occur}")
        else:
            print("entered number is not btw. 1 and 3, terminating the program..")
    else:   
        print("unregistered user, terminating the program..")