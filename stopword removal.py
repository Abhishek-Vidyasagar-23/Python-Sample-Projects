# get the phrase from the user
def acronym():
    phrase = input('Enter phrase for acronym')
    stopwords= ['in', 'on', 'the', 'at', 'is', 'of']



    # split the phrase
    phrase_split = phrase.split()
    result_words= [word for word in phrase_split if word.lower() not in stopwords]
    result =' '.join(result_words)
    #print(result)
    result_split = result.split()



    acronym = ""
    # iterate through substring
    for i in result_split:
        acronym = acronym + i[0].upper()

    print("Acronym for your phrase is ", acronym+".")


acronym()
