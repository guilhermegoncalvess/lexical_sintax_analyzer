import TOKENS

def nextPosition(positionFile):
    positionFile +=1
    return positionFile 

def nextCharacterIs( token, nextCharacter  ):
    return TOKENS.TOKENS[token].find(nextCharacter)
# def state_q0( file[positionFile], file, recognizedToken ):
def state_q0(positionFile, file, recognizedToken ):

    if( file[positionFile] == '#'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.HST

    elif( file[positionFile] == '<'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.MENOR

    elif( file[positionFile] == '>'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.MAIOR

    
    elif( file[positionFile] == '('):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.AP


    elif( file[positionFile] == ')'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.FP

    elif( file[positionFile] == '{'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.ACH
    
    elif( file[positionFile] == '}'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.FCH
    
    elif( file[positionFile] == '"'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.ASP

    elif( file[positionFile] == "'"):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.ASPS

    elif( file[positionFile] == ';'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.PNTVIRG

    elif( file[positionFile] == ':'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.DPT

    elif( file[positionFile] == '='):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.ATRIB

    elif( file[positionFile] == 'c'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_c2(positionFile, file, recognizedToken)
    
    elif( file[positionFile] == 'i'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_q2(positionFile, file, recognizedToken)
        
    elif( file[positionFile] == 's'):
       positionFile = nextPosition(positionFile)
       positionFile, recognizedToken = state_s2(positionFile, file, recognizedToken)

    elif( file[positionFile] == 'm'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_m2(positionFile, file, recognizedToken)

    elif( file[positionFile] == 'p'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_p2(positionFile, file, recognizedToken)

    
    elif( file[positionFile] == 'r'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_r2(positionFile, file, recognizedToken)

    elif( file[positionFile] == 'b'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_b2(positionFile, file, recognizedToken)

    elif( (nextCharacterIs( TOKENS.VARIAVEL, file[positionFile]) != -1) and ( file[positionFile] != 'b' or file[positionFile] != 'c' or file[positionFile] != 'i' or file[positionFile] != 'm' or file[positionFile] != 's' or file[positionFile] != 'p' or file[positionFile] != 'r' )):
        positionFile, recognizedToken = state_v1(positionFile, file, recognizedToken)
        print(positionFile, recognizedToken, "DA STATE")

    elif( (nextCharacterIs( TOKENS.NUMERO, file[positionFile]) != -1) ):
        positionFile, recognizedToken = state_n0(positionFile, file, recognizedToken)
        print(positionFile, recognizedToken, "DA STATE")
    

    return positionFile, recognizedToken

def state_v0(positionFile, file, recognizedToken):
    positionFile = nextPosition(positionFile)
    if( nextCharacterIs( TOKENS.VARIAVEL, file[positionFile]) != -1 ):
        recognizedToken = TOKENS.VARIAVEL
        state_v0(positionFile, file, recognizedToken)

    return positionFile, recognizedToken 
    # else:
    #     state_q0(positionFile, file, recognizedToken)
    
def state_v1(positionFile, file, recognizedToken):
    if( nextCharacterIs( TOKENS.VARIAVEL, file[positionFile]) != -1):
        positionFile = nextPosition(positionFile)
        # positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_v1(positionFile, file, recognizedToken)
        recognizedToken = TOKENS.VARIAVEL

    return positionFile, recognizedToken

def state_n0(positionFile, file, recognizedToken):
    if( nextCharacterIs( TOKENS.NUMERO, file[positionFile]) != -1):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_n0(positionFile, file, recognizedToken)
        recognizedToken = TOKENS.NUMERO
        print("NUMEROOOO")
    return positionFile, recognizedToken



def state_q2(positionFile, file, recognizedToken ):
    if( file[positionFile] == 'n'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_q3(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'n' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )
        return positionFile, recognizedToken  

def state_q3(positionFile, file, recognizedToken ):
    if( file[positionFile] == 'c'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_q4(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( file[positionFile] == 't'):
        recognizedToken = TOKENS.INT
        positionFile, recognizedToken = state_v0(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'w' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken      

def state_q4(positionFile, file, recognizedToken ):
    if( file[positionFile] == 'l'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_q5(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'l' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )
        return positionFile, recognizedToken  

def state_q5(positionFile, file, recognizedToken ):
    if( file[positionFile] == 'u'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_q6(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'u' ):
        positionFile, recognizedToken =  state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

def state_q6(positionFile, file, recognizedToken ):
    if( file[positionFile] == 'd'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_q7(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'd' ):
        positionFile, recognizedToken =  state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

def state_q7(positionFile, file, recognizedToken ):
    if( file[positionFile] == 'e'):
        recognizedToken = TOKENS.INCLUDE 
        positionFile, recognizedToken = state_v0(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'e' ):
        positionFile, recognizedToken =  state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken
        

def state_s2(positionFile, file, recognizedToken):
    if( file[positionFile] == 'w'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_s3(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
        
    else:
        if( nextCharacterIs( TOKENS.VARIAVEL, file[positionFile]) != -1 ):
            positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
            return positionFile, recognizedToken   

def state_s3(positionFile, file, recognizedToken):
    if( file[positionFile] == 'i'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_s4(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'i' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken  

def state_s4(positionFile, file, recognizedToken):
    if( file[positionFile] == 't'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_s5(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 't' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken  

def state_s5(positionFile, file, recognizedToken):
    if( file[positionFile] == 'c'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_s6(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'c' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken 

def state_s6(positionFile, file, recognizedToken):
    if( file[positionFile] == 'h'):
        recognizedToken = TOKENS.SWITCH
        positionFile, recognizedToken = state_v0(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'h' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken 


def state_m2(positionFile, file, recognizedToken):
    if( file[positionFile] == 'a'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_m3(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'a' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

def state_m3(positionFile, file, recognizedToken):
    if( file[positionFile] == 'i'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_m4(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( nextCharacterIs(('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'i' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

def state_m4(positionFile, file, recognizedToken):
    if( file[positionFile] == 'n'):
        recognizedToken = TOKENS.MAIN  
        positionFile, recognizedToken = state_v0(positionFile, file, recognizedToken)  
        return positionFile, recognizedToken 
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'n' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken


def state_p2(positionFile, file, recognizedToken):
    if( file[positionFile] == 'r'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_p3(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'r' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

def state_p3(positionFile, file, recognizedToken):
    if( file[positionFile] == 'i'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_p4(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'i' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

def state_p4(positionFile, file, recognizedToken):
    if( file[positionFile] == 'n'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_p5(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'n' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

def state_p5(positionFile, file, recognizedToken):
    if( file[positionFile] == 't'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_p6(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 't' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

def state_p6(positionFile, file, recognizedToken):
    if( file[positionFile] == 'f'):
        recognizedToken = TOKENS.PRINTF 
        positionFile, recognizedToken = state_v0(positionFile, file, recognizedToken)
        return positionFile, recognizedToken 
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'f' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken


def state_r2(positionFile, file, recognizedToken):
    if( file[positionFile] == 'e'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_r3(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'e' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken


def state_r3(positionFile, file, recognizedToken):
    if( file[positionFile] == 't'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_r4(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 't' ):
       positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
       return positionFile, recognizedToken

def state_r4(positionFile, file, recognizedToken):
    if( file[positionFile] == 'u'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_r5(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'u' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

def state_r5(positionFile, file, recognizedToken):
    if( file[positionFile] == 'r'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_r6(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'r' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

def state_r6(positionFile, file, recognizedToken):
    if( file[positionFile] == 'n'):
        recognizedToken = TOKENS.RETURN
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

    

def state_b2(positionFile, file, recognizedToken):
    if( file[positionFile] == 'r'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_b3(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    else:
        recognizedToken = TOKENS.VARIAVEL
        return positionFile, recognizedToken

def state_b3(positionFile, file, recognizedToken):
    if( file[positionFile] == 'e'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken =  state_b4(positionFile, file, recognizedToken)
        return positionFile, recognizedToken

def state_b4(positionFile, file, recognizedToken):
    if( file[positionFile] == 'a'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_b5(positionFile, file, recognizedToken)
        return positionFile, recognizedToken

def state_b5(positionFile, file, recognizedToken):
    if( file[positionFile] == 'k'):
        recognizedToken = TOKENS.BREAK
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken


def state_c2(positionFile, file, recognizedToken):
    if( file[positionFile] == 'h'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_c3(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    elif( file[positionFile] == 'a'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_c6(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'h' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

def state_c3(positionFile, file, recognizedToken):
    if( file[positionFile] == 'a'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_c4(positionFile, file, recognizedToken)
        return positionFile, recognizedToken

    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'r' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )
        return positionFile, recognizedToken

def state_c4(positionFile, file, recognizedToken):
    if( file[positionFile] == 'r'):
        recognizedToken = TOKENS.CHAR
        positionFile, recognizedToken = state_v0(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
        
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 'r' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )
        return positionFile, recognizedToken

def state_c6(positionFile, file, recognizedToken):
    if( file[positionFile] == 's'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_c7(positionFile, file, recognizedToken)
        return positionFile, recognizedToken
    elif( (nextCharacterIs('VARIAVEL', file[positionFile]) != -1) and file[positionFile] != 's' ):
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )
        return positionFile, recognizedToken

def state_c7(positionFile, file, recognizedToken):
    if( file[positionFile] == 'e'):
        recognizedToken = TOKENS.CASE
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )
        return positionFile, recognizedToken         