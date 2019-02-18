'''
Feito por Simei Thander - TADS 2018.2
'''

def convert_dec(n):
    n = (str(n)[::-1])
    total = 0
    for i in range(len(n)):
        total += (int(n[i]) * (2 ** i))
    return total

#calcular o código address
def calc_address(str):
    cont_address = 1
    cont_address_total = 0

    for i in range(len(address_inver)):
        if i != 0:
            cont_address *= 2 
        
        if int(address_inver[i]) == 1:
            cont_address_total += 1 * cont_address
    return cont_address_total

codigo_bin = input("Digite o codigo binário: ")
op = convert_dec(codigo_bin[:6])
rt = convert_dec(codigo_bin[11:16])
rs =  convert_dec(codigo_bin[6:11])
rd = convert_dec(codigo_bin[14:19])
imm = convert_dec(codigo_bin[16:])
func = convert_dec(codigo_bin[26:])
address = codigo_bin[6:]
address_inver = address[::-1]

if op == 32:
    #instrução l
    if op == 33:  
        print("ih {}$, {}(${})".format(rt, imm, rs))      
    else:
        print("lb {}$, {}(${})".format(rt, imm, rs))

elif op == 0:
    #Operação do tipo R
    if func == 34:
        print("sub ${}, ${}, ${}".format(rd, rs, rt))

elif op == 2:
    #Operação do tipo J
    print("j {}".format(calc_address(address_inver)))

