'''
Feito por Simei Thander - TADS 2018.2
'''

def convert_dec(n):
    n = (str(n)[::-1])
    total = 0
    for i in range(len(n)):
        total += (int(n[i]) * (2 ** i))
    return total

codigo_bin = input("Digite o codigo binário: ")
op = convert_dec(codigo_bin[:6])
rt = convert_dec(codigo_bin[11:16])
rs =  convert_dec(codigo_bin[6:11])
imm = convert_dec(codigo_bin[16:])
func = convert_dec(codigo_bin[26:])

if op == 32:
    #instrução l
    if op == 33:  
        print("ih {}$, {}(${})".format(rt, imm, rs))      
    else:
        print("lb {}$, {}(${})".format(rt, imm, rs))


elif op == 0:
    #Operação do tipo R
    print("OP: R")

elif op == 2:
    #Operação do tipo J
    print("OP: J")

