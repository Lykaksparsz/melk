from sys import *

TokenPrint = True

def open_file(filename):
    data = open(filename, "r").read()
    return data

def lex(filecontents):
    tok = ""
    string = ""
    isexpr = 0
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ":
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n" or tok == "<EOF>":
            if expr != "" and isexpr:
                tokens.append("EXPR:" + expr)
                expr = ""
            elif expr != "" and isexpr == 0:
                tokens.append("NUM:"  + expr)
                expr = ""
            tok = ""
        elif tok == "pr":
            tokens.append("PRINT")
            tok = ""
        elif tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9":
            expr += tok
            tok = ""
        elif tok == "+":
            isexpr
            expr += tok
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING:" + string + "\"")
                string = ""
                state = 0
        elif state == 1:
            string += tok
            tok = ""
    if TokenPrint == true:
        print(tokens)
    return tokens

def parse(toks):
    i = 0
    while(i < len(toks)):
        if toks[i] + " " + toks[i+1][0:6] == "PRINT STRING" or toks[i] + " " + toks[i+1][0:3] == "PRINT NUM" or toks[i] + " " + toks[i+1][0:4] == "PRINT EXPR":
            if toks[i+1][0:6] == "STRING":
                print(toks[i+1][7:])
            elif toks[i+1][0:3] == "NUM":
                print(toks[i+1][4:])
            elif toks[i+1][0:4] == "EXPR":
                print(toks[i+1][5:])
            i+=2
            
def run():
    data = open_file(argv[1])
    lex(data)
