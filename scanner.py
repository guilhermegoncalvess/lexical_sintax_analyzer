def scanner():   
    try:
        file = open('inputfile.txt', 'r')

        nextCharacter = file.read()
        file.close()
        return nextCharacter
    except:
        print("Error opening file")

scanner()