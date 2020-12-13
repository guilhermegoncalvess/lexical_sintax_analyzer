import scanner
import states
import TOKENS
import sys

file = scanner.scanner()
positionFile = 0
recognizedToken = ''

def ignoreSpace(positionFile):
        while positionFile < len(file) and (file[positionFile] in ["\n", " ", "\t"]):
            positionFile += 1
        return positionFile
    
def nextToken(positionFile, file, recognizedToken):
        positionFile = ignoreSpace(positionFile)
        if positionFile == len(file):
            print("Finished reading")
            exit()
        positionFile, recognizedToken = states.state_q0(positionFile, file, recognizedToken)
        return  positionFile, recognizedToken

def recognize( token, positionFile,  recognizedToken ):
    actualToken = token
    if token == recognizedToken:
        print("Recognized token:", token)
        positionFile, recognizedToken = nextToken( positionFile, file, recognizedToken)
        print( "Token read:", recognizedToken)
        return positionFile, recognizedToken
    else:
        print("Expected token:", actualToken)
        # return positionFile, recognizedToken

def init(positionFile, recognizedToken):
    try:    
        positionFile, recognizedToken = includeLibrary(positionFile, recognizedToken)
        positionFile, recognizedToken = mainFunction(positionFile, recognizedToken)
        return positionFile, recognizedToken
    except:
        exit()
def includeLibrary(positionFile, recognizedToken):
    try:
        positionFile, recognizedToken = includeCommand(positionFile, recognizedToken)
        positionFile, recognizedToken = includeCommand(positionFile, recognizedToken)
        return positionFile, recognizedToken 
    except:
        exit()

def includeCommand(positionFile, recognizedToken):
    try:
        positionFile, recognizedToken = recognize(TOKENS.HST, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.INCLUDE, positionFile, recognizedToken)
        
        positionFile, recognizedToken = recognize(TOKENS.MENOR, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.MAIOR, positionFile, recognizedToken)
        return positionFile, recognizedToken
    except:
        exit()

def mainFunction(positionFile, recognizedToken):
    try:
        positionFile, recognizedToken = recognize(TOKENS.INT, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.MAIN, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.AP, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.FP, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.ACH, positionFile, recognizedToken)
        positionFile, recognizedToken = mainBody(positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.FCH, positionFile, recognizedToken)

        return positionFile, recognizedToken
    except:
        exit()


def mainBody(positionFile, recognizedToken):
    try:
        positionFile, recognizedToken = commandBlock(positionFile, recognizedToken)
        positionFile, recognizedToken = returnCommand(positionFile, recognizedToken)
        return positionFile, recognizedToken
    except:
        exit()

def commandBlock(positionFile, recognizedToken):
    try:
        positionFile, recognizedToken = declaration(positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.PNTVIRG, positionFile, recognizedToken)
        positionFile, recognizedToken = attribution(positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.PNTVIRG, positionFile, recognizedToken)
        positionFile, recognizedToken = switchCommand(positionFile, recognizedToken)
        return positionFile, recognizedToken
    except:
        exit()

def switchCommand(positionFile, recognizedToken):
    try:
        positionFile, recognizedToken = recognize(TOKENS.SWITCH, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.AP, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken )
        positionFile, recognizedToken = recognize(TOKENS.FP, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.ACH, positionFile, recognizedToken)
        positionFile, recognizedToken = caseBlock(positionFile, recognizedToken)
        positionFile, recognizedToken = caseBlock(positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.FCH, positionFile, recognizedToken)
        return positionFile, recognizedToken
    except:
        exit()

def declaration(positionFile, recognizedToken):
    try:
        positionFile, recognizedToken = recognize(TOKENS.CHAR, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
        return positionFile, recognizedToken
    except:
        exit()

def attribution(positionFile, recognizedToken):
    try:
        positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.ATRIB, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.ASPS, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.ASPS, positionFile, recognizedToken)
        return positionFile, recognizedToken
    except:
        exit()


def caseBlock(positionFile, recognizedToken):
    try:
        positionFile, recognizedToken = recognize(TOKENS.CASE, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.ASPS, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.ASPS, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.DPT, positionFile, recognizedToken)
        positionFile, recognizedToken = printfCommand(positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.BREAK, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.PNTVIRG, positionFile, recognizedToken)

        return positionFile, recognizedToken
    except:
        exit()

def printfCommand(positionFile, recognizedToken):
    try:
        positionFile, recognizedToken = recognize(TOKENS.PRINTF, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.AP, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.ASP, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.ASP, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.FP, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.PNTVIRG, positionFile, recognizedToken)

        return positionFile, recognizedToken
    except:
        exit()

def returnCommand(positionFile, recognizedToken):
    try:
        positionFile, recognizedToken = recognize(TOKENS.RETURN, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.NUMERO, positionFile, recognizedToken)
        positionFile, recognizedToken = recognize(TOKENS.PNTVIRG, positionFile, recognizedToken)
        return positionFile, recognizedToken
    except:
        exit()


# print(file)
positionFile, recognizedToken = nextToken(positionFile, file, recognizedToken)
init(positionFile, recognizedToken)


