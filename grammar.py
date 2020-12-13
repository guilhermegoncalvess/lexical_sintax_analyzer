import scanner
import states
import TOKENS




file = scanner.scanner()
positionFile = 0
recognizedToken = ''


# def nextTokenIs(recognizedToken):
#     recognizedToken
def ignoreSpace(positionFile):
    while file[positionFile] ==  "\n" or file[positionFile] ==  " " or file[positionFile] ==  "\t" or file[positionFile] ==  "" :
        positionFile += 1
    return positionFile

def nextToken(positionFile, file, recognizedToken):
        print(positionFile,"RR")
        print(positionFile)
        positionFile = ignoreSpace(positionFile)
        print(positionFile)
        positionFile, recognizedToken = states.state_q0(positionFile, file, recognizedToken)
        return  positionFile, recognizedToken

def recognize( token, positionFile,  recognizedToken ):
    if token == recognizedToken:
        print("TokenReconhecido", token)
        positionFile, recognizedToken = nextToken( positionFile, file, recognizedToken)
        print( positionFile,"-->", recognizedToken)
        return positionFile, recognizedToken
       

def init(positionFile, recognizedToken):
    positionFile, recognizedToken = nextToken(positionFile, file, recognizedToken)
    # print(positionFile, recognizedToken)
    positionFile, recognizedToken = includeLib(positionFile, recognizedToken)
    positionFile, recognizedToken = mainFunction(positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.EOF, positionFile, recognizedToken)


def includeLib(positionFile, recognizedToken):
    positionFile, recognizedToken = includeCommand(positionFile, recognizedToken)
    positionFile, recognizedToken = includeCommand(positionFile, recognizedToken)
    # print(positionFile, recognizedToken)
    return positionFile, recognizedToken 

def includeCommand(positionFile, recognizedToken):
    positionFile, recognizedToken = recognize(TOKENS.HST, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.INCLUDE, positionFile, recognizedToken)
    
    positionFile, recognizedToken = recognize(TOKENS.MENOR, positionFile, recognizedToken)
    # positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.MAIOR, positionFile, recognizedToken)
    return positionFile, recognizedToken

def mainFunction(positionFile, recognizedToken):
    positionFile, recognizedToken = recognize(TOKENS.INT, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.MAIN, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.AP, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.FP, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.ACH, positionFile, recognizedToken)
    positionFile, recognizedToken = mainBody(positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.FCH, positionFile, recognizedToken)
    return positionFile, recognizedToken


def mainBody(positionFile, recognizedToken):
    positionFile, recognizedToken = commandBlock(positionFile, recognizedToken)
    positionFile, recognizedToken = returnCommand(positionFile, recognizedToken)
    return positionFile, recognizedToken
    # positionFile, recognizedToken = recognize(TOKENS.PNTVIRG, positionFile, recognizedToken)

def commandBlock(positionFile, recognizedToken):
    # declaration()
    positionFile, recognizedToken = declaration(positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.PNTVIRG, positionFile, recognizedToken)
    positionFile, recognizedToken = attribution(positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.PNTVIRG, positionFile, recognizedToken)
    positionFile, recognizedToken = switchCommand(positionFile, recognizedToken)
    # positionFile, recognizedToken =printfCommand(positionFile, recognizedToken)

# def returnCommand():
#     recognize(TOKENS.NUMERO)
    return positionFile, recognizedToken

def switchCommand(positionFile, recognizedToken):
    positionFile, recognizedToken = recognize(TOKENS.SWITCH, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.AP, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken )
    positionFile, recognizedToken = recognize(TOKENS.FP, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.ACH, positionFile, recognizedToken)
    positionFile, recognizedToken = caseBlock(positionFile, recognizedToken)
    positionFile, recognizedToken = caseBlock(positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.FCH, positionFile, recognizedToken)
    return positionFile, recognizedToken

def declaration(positionFile, recognizedToken):
    positionFile, recognizedToken = recognize(TOKENS.CHAR, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
    return positionFile, recognizedToken

def attribution(positionFile, recognizedToken):
    positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.ATRIB, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.ASPS, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.ASPS, positionFile, recognizedToken)

    return positionFile, recognizedToken

def caseBlock(positionFile, recognizedToken):
    positionFile, recognizedToken = recognize(TOKENS.CASE, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.ASPS, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.ASPS, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.DPT, positionFile, recognizedToken)
    positionFile, recognizedToken = printfCommand(positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.BREAK, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.PNTVIRG, positionFile, recognizedToken)

    return positionFile, recognizedToken

def printfCommand(positionFile, recognizedToken):
    positionFile, recognizedToken = recognize(TOKENS.PRINTF, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.AP, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.ASP, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.ASP, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.FP, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.PNTVIRG, positionFile, recognizedToken)

    return positionFile, recognizedToken

def returnCommand(positionFile, recognizedToken):
    positionFile, recognizedToken = recognize(TOKENS.RETURN, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.NUMERO, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.PNTVIRG, positionFile, recognizedToken)
    return positionFile, recognizedToken


print(file[260] == "\n")
init(positionFile, recognizedToken)
# positionFile, recognizedToken = nextToken(positionFile, file, recognizedToken)
# if file[26] == " ":

