import scanner
import states
import TOKENS




file = scanner.scanner()
positionFile = 0
recognizedToken = ''


# def nextTokenIs(recognizedToken):
#     recognizedToken
def ignoreSpace(positionFile):
    while file[positionFile] ==  ("\n" or " " or "\t"):
        positionFile += 1
    return positionFile

def nextToken(positionFile, file, recognizedToken):
        positionFile = ignoreSpace(positionFile)
        positionFile, recognizedToken = states.state_q0(positionFile, file, recognizedToken)
        # positionFile = ignoreSpace(positionFile)
        return  positionFile, recognizedToken

def recognize( token, positionFile,  recognizedToken ):
    if token == recognizedToken:
        print("TokenReconhecido", token)
        positionFile, recognizedToken = nextToken( positionFile, file, recognizedToken)
        print("-->", recognizedToken)
        return positionFile, recognizedToken
       

def init(positionFile, recognizedToken):
    positionFile, recognizedToken = nextToken(positionFile, file, recognizedToken)
    # print(positionFile, recognizedToken)
    positionFile, recognizedToken = includeLib(positionFile, recognizedToken)
    positionFile, recognizedToken = mainFunction(positionFile, recognizedToken)

def includeLib(positionFile, recognizedToken):
    positionFile, recognizedToken = includeCommand(positionFile, recognizedToken)
    positionFile, recognizedToken = includeCommand(positionFile, recognizedToken)
    # print(positionFile, recognizedToken)
    return positionFile, recognizedToken 

def mainFunction(positionFile, recognizedToken):
    positionFile, recognizedToken = recognize(TOKENS.INT, positionFile, recognizedToken)
    print(recognizedToken)
    positionFile, recognizedToken = states.state_q0(positionFile, file, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.MAIN, positionFile, recognizedToken)
    # positionFile, recognizedToken = recognize(TOKENS.AP, positionFile, recognizedToken)
    # positionFile, recognizedToken = recognize(TOKENS.FP, positionFile, recognizedToken)
    # positionFile, recognizedToken = recognize(TOKENS.ACH, positionFile, recognizedToken)
    # positionFile, recognizedToken = mainBody(positionFile, recognizedToken)
    return positionFile, recognizedToken

def mainBody():
    commandBlock()
    # returnCommand()
    recognize(TOKENS.PNTVIRG)

def commandBlock():
    switchCommand()
    # declaration()
    attribution()
    printfCommand()
    recognize(TOKENS.PNTVIRG)

# def returnCommand():
#     recognize(TOKENS.NUMERO)

def switchCommand():
    recognize(TOKENS.SWITCH)
    recognize(TOKENS.AP)
    recognize(TOKENS.VARIAVEL)
    recognize(TOKENS.FP)
    recognize(TOKENS.ACH)
    caseBlock()
    recognize(TOKENS.FCH)

# def declaration():
#     if next(TOKENS.CHAR) or recognize(TOKENS.INT):

def attribution():
    recognize(TOKENS.VARIAVEL)
    recognize(TOKENS.ATRIB)
    recognize(TOKENS.VARIAVEL)


def caseBlock():
    recognize(TOKENS.CASE, recognizedToken)
    recognize(TOKENS.VARIAVEL)
    recognize(TOKENS.DPT)
    printfCommand()
    recognize(TOKENS.BREAK)
    recognize(TOKENS.PNTVIRG)


def printfCommand():
    recognize(TOKENS.PRINTF)
    recognize(TOKENS.ASP)
    recognize(TOKENS.VARIAVEL)
    recognize(TOKENS.ASP)
    recognize(TOKENS.PNTVIRG)

def includeCommand(positionFile, recognizedToken):
    positionFile, recognizedToken = recognize(TOKENS.HST, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.INCLUDE, positionFile, recognizedToken)
    
    positionFile, recognizedToken = recognize(TOKENS.MENOR, positionFile, recognizedToken)
    # positionFile, recognizedToken = recognize(TOKENS.VARIAVEL, positionFile, recognizedToken)
    positionFile, recognizedToken = recognize(TOKENS.MAIOR, positionFile, recognizedToken)
    return positionFile, recognizedToken



init(positionFile, recognizedToken)
# positionFile, recognizedToken = nextToken(positionFile, file, recognizedToken)
# if file[10] == "\n":
    # print(file[10],recognizedToken, "AQUi")
# print(recognizedTokens)

