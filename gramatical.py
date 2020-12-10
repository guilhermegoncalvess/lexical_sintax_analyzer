import lexical_analyzer
import TOKENS

lexical_analyzer.scanner()
recognizedTokens = lexical_analyzer.recognizedTokens
positionToken = 0

# print(recognizedTokens)
def nextToken( positionToken ):
    positionToken += 1
    return positionToken

def recognizeToken( token, positionToken ):
    if token in TOKENS.TOKENS:
        positionToken = nextToken(positionToken)
        print(positionToken)


def includeCommand(positionToken):
    if recognizedTokens[positionToken] == "MENOR":
        positionToken = nextToken(positionToken)
        if recognizedTokens[positionToken] == "MAIOR":
            positionToken = nextToken(positionToken)
            print("INCLUDE")

def commandList( positionToken ):
    if recognizedTokens[positionToken] == 'HST':
        print("HST")
        positionToken = nextToken(positionToken)
        if recognizedTokens[positionToken] == "INCLUDE":
            positionToken = nextToken(positionToken)
            includeCommand(positionToken)
   
    elif recognizedTokens[positionToken] == "INT":
        positionToken = nextToken(positionToken)
        if recognizedTokens[positionToken] == 'MAIN':
            if recognizedTokens[positionToken] == '{':
                positionToken = nextToken(positionToken)
                commandList(positionToken)
        elif recognizedTokens[positionToken] == "VARIAVEL":
            positionToken = nextToken(positionToken)
            if recognizedTokens[positionToken] == 'PNTVIRG':
                commandList(positionToken)
            elif recognizedTokens[positionToken] == 'ATRIB':
                commandList(positionToken)




commandList(positionToken)

