import TOKENS

def nextPosition(positionFile):
    positionFile +=1
    return positionFile 

def nextCharacterIs( token, nextCharacter  ):
    return TOKENS.TOKENS[token].find(nextCharacter)
# def state_q0( file[positionFile], file, recognizedToken ):
def state_q0(positionFile, file, recognizedToken ):
    
    # if( file[positionFile] == " "):
    #     positionFile = nextPosition(positionFile)
    #     positionFile, recognizeToken = state_q0( positionFile, file, recognizedToken )
    #     return positionFile, recognizeToken

    if( file[positionFile] == '#'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.HST

    elif( file[positionFile] == '<'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.MENOR

    elif( file[positionFile] == '>'):
        positionFile = nextPosition(positionFile)
        recognizedToken = TOKENS.MAIOR

    
    # elif( file[positionFile] == '('):
    #     # positionFile = nextPosition(positionFile)
    #     recognizedToken.append('AP')
    #     # state_q0(file[positionFile], file, recognizedToken)

    # elif( file[positionFile] == ')'):
    #     recognizedToken.append('FP')

    # elif( file[positionFile] == '{'):
    #     recognizedToken.append('ACH')
    
    # elif( file[positionFile] == '}'):
    #     recognizedToken.append('FCH')
    
    # elif( file[positionFile] == '"'):
    #     recognizedToken.append('ASP')

    # elif( file[positionFile] == ';'):
    #     recognizedToken.append('PNTVIRG')

    # elif( file[positionFile] == ':'):
    #     recognizedToken.append('DPT')

    # elif( file[positionFile] == '='):
    #     recognizedToken.append('ATRIB')

    # elif( file[positionFile] == 'c'):
    #     positionFile = nextPosition(positionFile)
    #     state_c2(file[positionFile], file, recognizedToken)
    
    elif( file[positionFile] == 'i'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_q2(positionFile, file, recognizedToken)
        
    # elif( file[positionFile] == 's'):
    #    positionFile = nextPosition(positionFile)
    #    state_s2(file[positionFile], file, recognizedToken)

    elif( file[positionFile] == 'm'):
        positionFile = nextPosition(positionFile)
        state_m2(positionFile, file, recognizedToken)

    # elif( file[positionFile] == 'p'):
    #     positionFile = nextPosition(positionFile)
    #     state_p2(file[positionFile], file, recognizedToken)

    
    # elif( file[positionFile] == 'r'):
    #     positionFile = nextPosition(positionFile)
    #     state_r2(file[positionFile], file, recognizedToken)

    # elif( file[positionFile] == 'b'):
    #     positionFile = nextPosition(positionFile)
    #     state_b2(file[positionFile], file, recognizedToken)

    # elif( (nextCharacterIs( 'VARIAVEL', file[positionFile]) != -1) and ( file[positionFile] != 'b' or file[positionFile] != 'c' or file[positionFile] != 'i' or file[positionFile] != 'm' or file[positionFile] != 's' or file[positionFile] != 'p' or file[positionFile] != 'r' )):
    #     state_v1(file[positionFile], file, recognizedToken)
    # print(positionFile, recognizedToken)
    # print(positionFile)
    # positionFile = nextPosition(positionFile)

    return positionFile, recognizedToken

def state_v0(positionFile, file, recognizedToken):
    positionFile = nextPosition(positionFile)
    if( nextCharacterIs( 'VARIAVEL', file[positionFile]) != -1 ):
        recognizedToken = TOKENS.VARIAVEL
        state_v0(positionFile, file, recognizedToken)

    return positionFile, recognizedToken 
    # else:
    #     state_q0(positionFile, file, recognizedToken)
    
def state_v1(positionFile, file, recognizedToken):
    positionFile = nextPosition(positionFile)
    if( nextCharacterIs( 'VARIAVEL', file[positionFile]) != -1):
        positionFile = nextPosition(positionFile)
        recognizedToken.append("VARIAVEL")
        state_v1(positionFile, file, recognizedToken)



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
        # positionFile = nextPosition(positionFile)
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
        if( nextCharacterIs( 'VARIAVEL', file[positionFile]) != -1 ):
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
        recognizedToken.append('SWITCH')  
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
        recognizedToken.append('PRINTF')
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
        # positionFile, recognizedToken = state_q0( positionFile, file, recognizedToken )
        # return positionFile, recognizedToken

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
        recognizedToken.append('RETURN')
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )  
        return positionFile, recognizedToken

    

def state_b2(positionFile, file, recognizedToken):
    if( file[positionFile] == 'r'):
        positionFile = nextPosition(positionFile)
        positionFile, recognizedToken = state_b3(positionFile, file, recognizedToken)
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
        recognizedToken.append('BREAK')
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
        state_c4(positionFile, file, recognizedToken)
        return positionFile, recognizedToken

def state_c4(positionFile, file, recognizedToken):
    if( file[positionFile] == 'r'):
        recognizedToken.append('CHAR')
        positionFile, recognizedToken = state_v0(positionFile, file, recognizedToken)
        
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
        recognizedToken.append('CASE')
        positionFile, recognizedToken = state_v0( positionFile, file, recognizedToken )
        return positionFile, recognizedToken         