recorrido = []
def q0(cadena):
    recorrido.clear()
    recorrido.append('q0')
    posicion = 0
    caracter = cadena[posicion]


    if caracter == "2":
        return q1(cadena, posicion + 1)
    elif "3" <= caracter <= "6":
        return q19(cadena, posicion + 1)
    elif caracter == "7":
        return q21(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    

def q1(cadena, posicion):
    recorrido.append('q1')
    caracter = cadena[posicion]

    if caracter == "-":
        return q2(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}


def q2(cadena, posicion):
    recorrido.append('q2')
    caracter = cadena[posicion]

    if caracter == "T":
        return q3(cadena, posicion + 1)
    elif "U" <= caracter <= "Z":
        return q18(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q3(cadena, posicion):
    recorrido.append('q3')
    caracter = cadena[posicion]
    
    if caracter == "A":
        return q4(cadena, posicion + 1)
    elif "B" <= caracter <= "Z":
        return q12(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q4(cadena, posicion):
    recorrido.append('q4')
    caracter = cadena[posicion]
    
    if caracter == "-":
        return q5(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    

def q5(cadena, posicion):
    recorrido.append('q5')
    caracter = cadena[posicion]
    
    if caracter == "0":
        return q6(cadena, posicion + 1)
    elif "1" <= caracter <= "9":
        return q11(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    

def q6(cadena, posicion):
    recorrido.append('q6')
    caracter = cadena[posicion]
    
    if caracter == "1":
        return q7(cadena, posicion + 1)
    elif "2" <= caracter <= "9":
        return q9(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q7(cadena, posicion):
    recorrido.append('q7')
    caracter = cadena[posicion]
    
    if "P" <= caracter <= "Z":
        recorrido.append('q8')
        return aceptacion()
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
def q9(cadena, posicion):
    recorrido.append('q9')
    caracter = cadena[posicion]
    
    if "A" <= caracter <= "Z":
        recorrido.append('q10')
        return aceptacion()
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q11(cadena, posicion):
    recorrido.append('q11')
    caracter = cadena[posicion]
    
    if "0" <= caracter <= "9":
        return q9(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q12(cadena, posicion):
    recorrido.append('q12')
    caracter = cadena[posicion]
    
    if caracter == "-":
        return q13(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q13(cadena, posicion):
    recorrido.append('q13')
    caracter = cadena [posicion]
    
    if caracter == "0":
        return q14(cadena, posicion + 1)
    elif "1" <= caracter <= "9":
        return q17(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q14(cadena, posicion):
    recorrido.append('q14')
    caracter = cadena[posicion]
    
    if "1" <= caracter <= "9":
        return q15(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q15(cadena, posicion):
    recorrido.append('q15')
    caracter = cadena[posicion]
    
    if "A" <= caracter <= "Z":
        recorrido.append('q16')
        return aceptacion()
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
def q17(cadena, posicion):
    recorrido.append('q17')
    caracter = cadena[posicion]
    
    if "0" <= caracter <= "9":
        return q15(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    

def q18(cadena, posicion):
    recorrido.append('q18')
    caracter = cadena[posicion]
    
    if "A" <= caracter <= "Z":
        return q12(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q19(cadena, posicion):
    recorrido.append('q19')
    caracter = cadena[posicion]
    
    if caracter == "-":
        return q20(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q20(cadena, posicion):
    recorrido.append('q20')
    caracter = cadena[posicion]
    
    if "A" <= caracter <= "Z":
        return q18(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    

def q21(cadena, posicion):
    recorrido.append('q21')
    caracter = cadena[posicion]
    
    if caracter == "-":
        return q22(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q22(cadena, posicion):
    recorrido.append('q22')
    caracter = cadena[posicion]
    
    if "A" <= caracter <= "S":
        return q18(cadena, posicion + 1)
    elif caracter == "T":
        return q23(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    

def q23(cadena, posicion):
    recorrido.append('q23')
    caracter = cadena[posicion]
    
    if "A" <= caracter <= "I":
        return q12(cadena, posicion + 1)
    elif caracter == "J":
        return q24(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q24(cadena, posicion):
    recorrido.append("q24")
    caracter = cadena[posicion]
    
    if caracter == "-":
        return q25(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q25(cadena, posicion):
    recorrido.append("q25")
    caracter = cadena[posicion]
    
    if caracter == "0":
        return q26(cadena, posicion + 1)
    elif "1" <= caracter <= "8":
        return q29(cadena, posicion + 1)
    elif caracter == "9":
        return q30(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}


def q26(cadena, posicion):
    recorrido.append("q26")
    caracter = cadena[posicion]
    
    if "1" <= caracter <= "9":
        return q27(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q27(cadena, posicion):
    recorrido.append("q27")
    caracter = cadena[posicion]
    
    if "A" <= caracter <= "Z":
        recorrido.append("q28")
        return aceptacion()
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q29(cadena, posicion):
    recorrido.append("q29")
    caracter = cadena[posicion]
    
    if "0" <= caracter <= "9":
        return q27(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    

def q30(cadena, posicion):
    recorrido.append("q30")
    caracter = cadena[posicion]
    
    if "0" <= caracter <= "8":
        return q27(cadena, posicion + 1)
    elif caracter == "9":
        return q31(cadena, posicion + 1)
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def q31(cadena, posicion):
    recorrido.append("q31")
    caracter = cadena[posicion]
    
    if "A" <= caracter <= "V":
        recorrido.append("q32")
        return aceptacion()
    else:
        return {"estado": False, "posicion":posicion, "recorrido": recorrido}
    
    
def aceptacion():
    return {"estado": True, "recorrido":recorrido}
