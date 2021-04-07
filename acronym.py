# get the phrase from the user
def acronym():
    phrase = input('Enter phrase for acronym')


    # split the phrase
    phrase_split = phrase.split()

    acronym = ""
    # iterate through substring
    for i in phrase_split:
        acronym = acronym + i[0].upper()

    print("Acronym for your phrase is ", acronym+".")


acronym()
