import TOKENS

recognizedTokens = [] 


# def scanner():   
#     try:
#         file = open('inputfile.txt', 'r')

#         nextCharacter = file.read(1)
#         while True:
#             state_q0( nextCharacter, file, recognizedTokens)

#             nextCharacter = file.read(1)
#             print(nextCharacter, "main")
#             if(nextCharacter == ""):
#                 recognizedTokens.append('EOF')
#                 break
            
#         file.close()
#     except:
#         print("Error opening file")


def nextCharacterIs( token, nextCharacter  ):
    return TOKENS.TOKENS[token].find(nextCharacter)

def state_q0( nextCharacter, file, recognizedTokens ):
    # print("q0")
    if( nextCharacter == '#'):
        recognizedTokens.append('HST')

    elif( nextCharacter == '<'):
        recognizedTokens.append('MENOR')

    elif( nextCharacter == '>'):
        recognizedTokens.append('MAIOR')

    elif( nextCharacter == '('):
        # nextCharacter = file.read(1)
        recognizedTokens.append('AP')
        # state_q0(nextCharacter, file, recognizedTokens)

    elif( nextCharacter == ')'):
        recognizedTokens.append('FP')

    elif( nextCharacter == '{'):
        recognizedTokens.append('ACH')
    
    elif( nextCharacter == '}'):
        recognizedTokens.append('FCH')
    
    elif( nextCharacter == '"'):
        recognizedTokens.append('ASP')

    elif( nextCharacter == ';'):
        recognizedTokens.append('PNTVIRG')

    elif( nextCharacter == ':'):
        recognizedTokens.append('DPT')

    elif( nextCharacter == '='):
        recognizedTokens.append('ATRIB')

    elif( nextCharacter == 'c'):
        nextCharacter = file.read(1)
        state_c2(nextCharacter, file, recognizedTokens)
    
    elif( nextCharacter == 'i'):
        nextCharacter = file.read(1)
        state_q2(nextCharacter, file, recognizedTokens)
        
    elif( nextCharacter == 's'):
        nextCharacter = file.read(1)
        state_s2(nextCharacter, file, recognizedTokens)

    elif( nextCharacter == 'm'):
        nextCharacter = file.read(1)
        state_m2(nextCharacter, file, recognizedTokens)

    elif( nextCharacter == 'p'):
        nextCharacter = file.read(1)
        state_p2(nextCharacter, file, recognizedTokens)
    
    elif( nextCharacter == 'r'):
        nextCharacter = file.read(1)
        state_r2(nextCharacter, file, recognizedTokens)

    elif( nextCharacter == 'b'):
        nextCharacter = file.read(1)
        state_b2(nextCharacter, file, recognizedTokens)

    elif( (nextCharacterIs( 'VARIAVEL', nextCharacter) != -1) and ( nextCharacter != 'b' or nextCharacter != 'c' or nextCharacter != 'i' or nextCharacter != 'm' or nextCharacter != 's' or nextCharacter != 'p' or nextCharacter != 'r' )):
        state_v1(nextCharacter, file, recognizedTokens)
        
    

def state_v0(nextCharacter, file, recognizedTokens):
    print(nextCharacter,"varia")
    nextCharacter = file.read(1)
    if( nextCharacterIs( 'VARIAVEL', nextCharacter) != -1 ):
        recognizedTokens.pop()
        recognizedTokens.append("VARIAVEL")
        state_v0(nextCharacter, file, recognizedTokens)
    else:
        state_q0(nextCharacter, file, recognizedTokens)
    
def state_v1(nextCharacter, file, recognizedTokens):
    nextCharacter = file.read(1)
    if( nextCharacterIs( 'VARIAVEL', nextCharacter) != -1):
        nextCharacter = file.read(1)
        recognizedTokens.append("VARIAVEL")
        state_v1(nextCharacter, file, recognizedTokens)



def state_q2(nextCharacter, file, recognizedTokens ):
    if( nextCharacter == 'n'):
        nextCharacter = file.read(1)
        state_q3(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'n' ):
        state_v0( nextCharacter, file, recognizedTokens )  

def state_q3(nextCharacter, file, recognizedTokens ):
    if( nextCharacter == 'c'):
        nextCharacter = file.read(1)
        state_q4(nextCharacter, file, recognizedTokens)
    elif( nextCharacter == 't'):
        recognizedTokens.append('INT')
        state_v0(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'w' ):
        state_v0( nextCharacter, file, recognizedTokens )          

def state_q4(nextCharacter, file, recognizedTokens ):
    if( nextCharacter == 'l'):
        nextCharacter = file.read(1)
        state_q5(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'l' ):
        state_v0( nextCharacter, file, recognizedTokens )  

def state_q5(nextCharacter, file, recognizedTokens ):
    if( nextCharacter == 'u'):
        nextCharacter = file.read(1)
        state_q6(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'u' ):
        state_v0( nextCharacter, file, recognizedTokens )  

def state_q6(nextCharacter, file, recognizedTokens ):
    if( nextCharacter == 'd'):
        nextCharacter = file.read(1)
        state_q7(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'd' ):
        state_v0( nextCharacter, file, recognizedTokens )  

def state_q7(nextCharacter, file, recognizedTokens ):
    if( nextCharacter == 'e'):
        # nextCharacter = file.read(1)
        recognizedTokens.append('INCLUDE')        
        state_v0(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'e' ):
        state_v0( nextCharacter, file, recognizedTokens )  


def state_s2(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'w'):
        nextCharacter = file.read(1)
        state_s3(nextCharacter, file, recognizedTokens)
        
    else:
        if( nextCharacterIs( 'VARIAVEL', nextCharacter) != -1 ):
            state_v0( nextCharacter, file, recognizedTokens )    

def state_s3(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'i'):
        nextCharacter = file.read(1)
        state_s4(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'i' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_s4(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 't'):
        nextCharacter = file.read(1)
        state_s5(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 't' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_s5(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'c'):
        nextCharacter = file.read(1)
        state_s6(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'c' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_s6(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'h'):
        recognizedTokens.append('SWITCH')  
        state_v0(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'h' ):
        state_v0( nextCharacter, file, recognizedTokens )


def state_m2(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'a'):
        nextCharacter = file.read(1)
        state_m3(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'a' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_m3(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'i'):
        nextCharacter = file.read(1)
        state_m4(nextCharacter, file, recognizedTokens)
    elif( nextCharacterIs(('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'i' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_m4(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'n'):
        recognizedTokens.append('MAIN')  
        state_v0(nextCharacter, file, recognizedTokens)     
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'n' ):
        state_v0( nextCharacter, file, recognizedTokens )


def state_p2(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'r'):
        nextCharacter = file.read(1)
        state_p3(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'r' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_p3(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'i'):
        nextCharacter = file.read(1)
        state_p4(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'i' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_p4(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'n'):
        nextCharacter = file.read(1)
        state_p5(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'n' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_p5(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 't'):
        nextCharacter = file.read(1)
        state_p6(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 't' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_p6(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'f'):
        recognizedTokens.append('PRINTF')
        state_v0(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'f' ):
        state_v0( nextCharacter, file, recognizedTokens )


def state_r2(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'e'):
        nextCharacter = file.read(1)
        state_r3(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'e' ):
        state_v0( nextCharacter, file, recognizedTokens )
    state_q0( nextCharacter, file, recognizedTokens )


def state_r3(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 't'):
        nextCharacter = file.read(1)
        state_r4(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 't' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_r4(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'u'):
        nextCharacter = file.read(1)
        state_r5(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'u' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_r5(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'r'):
        nextCharacter = file.read(1)
        state_r6(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'r' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_r6(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'n'):
        recognizedTokens.append('RETURN')
        state_v0(nextCharacter, file, recognizedTokens)
    

def state_b2(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'r'):
        nextCharacter = file.read(1)
        state_b3(nextCharacter, file, recognizedTokens)

def state_b3(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'e'):
        nextCharacter = file.read(1)
        state_b4(nextCharacter, file, recognizedTokens)

def state_b4(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'a'):
        nextCharacter = file.read(1)
        state_b5(nextCharacter, file, recognizedTokens)

def state_b5(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'k'):
        recognizedTokens.append('BREAK')
        state_v0(nextCharacter, file, recognizedTokens)



def state_c2(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'h'):
        nextCharacter = file.read(1)
        state_c3(nextCharacter, file, recognizedTokens)
    elif( nextCharacter == 'a'):
        nextCharacter = file.read(1)
        state_c6(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'h' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_c3(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'a'):
        nextCharacter = file.read(1)
        state_c4(nextCharacter, file, recognizedTokens)

def state_c4(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'r'):
        recognizedTokens.append('CHAR')
        state_v0(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 'r' ):
        state_v0( nextCharacter, file, recognizedTokens )


def state_c6(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 's'):
        nextCharacter = file.read(1)
        state_c7(nextCharacter, file, recognizedTokens)
    elif( (nextCharacterIs('VARIAVEL', nextCharacter) != -1) and nextCharacter != 's' ):
        state_v0( nextCharacter, file, recognizedTokens )

def state_c7(nextCharacter, file, recognizedTokens):
    if( nextCharacter == 'e'):
        recognizedTokens.append('CASE')
        state_v0( nextCharacter, file, recognizedTokens )

scanner()
print(recognizedTokens)