'''
Feito por Simei Thander - TADS 2018.2
'''

texto_saida = []

#def para converter em decimal
def convertdecimal(n):
    n_invert = n[::-1]
    cont_n = 1
    cont_n_total = 0

    for i in range(len(n_invert)):
        if i != 0:
            cont_n *= 2
        if int(n_invert[i]) == 1:
            cont_n_total += 1 * cont_n
    return cont_n_total

#def para print da instrução
def op_r(inst):
    global rt, rs, rt, texto_saida
    texto_saida.append("{} ${}, ${}, ${} \n".format(inst, rd, rs, rt))

def op_i(inst):
    global rt, imm, rs, texto_saida
    texto_saida.append("{} {}$, {}(${}) \n".format(inst, rt, imm, rs))

def op_j(inst, address):
    global texto_saida
    texto_saida.append("{} {} \n".format(inst, address))

# main code

# leitura do codigo binário no arquivo .txt 
print("Lendo arquivo entrada.txt ...")
arq = open('entrada.txt', 'r+')
texto = arq.readlines()

for linha in texto:

    # captura as variáveis e operações da String e converte em decimal
    op = convertdecimal(linha[:6].rstrip())
    rt = convertdecimal(linha[11:16].rstrip())
    rs = convertdecimal(linha[6:11].rstrip())
    rd = convertdecimal(linha[14:19].rstrip())
    imm = convertdecimal(linha[16:].rstrip())
    func = convertdecimal(linha[26:].rstrip())
    address = convertdecimal(linha[6:].rstrip())

    # Caso o OPcode for 0, ele chega as funções do operador R
    if op == 0:
        if func == 32:
            op_r("add")
        elif func == 0:
            op_r("sll")
        elif func == 33:
            op_r("addu")
        elif func == 34:
            op_r("sub")
        elif func == 36:
            op_r("and")
        elif func == 13:
            op_r("break")
        elif func == 26:
            op_r("div")
        elif func == 27:
            op_r("divu")
        elif func == 9:
            op_r("jalr")
        elif func == 8:
            op_r("jr")
        elif func == 16:
            op_r("mfhi")
        elif func == 18:
            op_r("mflo")
        elif func == 24:
            op_r("mult")
        elif func == 25:
            op_r("multu")
        elif func == 19:
            op_r("mtlo")
        elif func == 17:
            op_r("mthi")
        elif func == 35:
            op_r("subu")
        elif func == 36:
            op_r("and")
        elif func == 37:
            op_r("or")
        elif func == 38:
            op_r("xor")
        elif func == 39:
            op_r("nor")
        elif func == 42:
            op_r("slt")
        elif func == 43:
            op_r("sltu")

    # Caso as operações forem acima de 0, é obtido a instrução do tipo i
    if op == 32:
        op_i("lb")
    elif op == 33:
        op_i("ih")
    elif op == 8:
        op_i("addi")
    elif op == 9:
        op_i("addiu")
    elif op == 10:
        op_i("slti")
    elif op == 11:
        op_i("sltiu")
    elif op == 12:
        op_i("andi")
    elif op == 13:
        op_i("ori")
    elif op == 14:
        op_i("xori")
    elif op == 15:
        op_i("lui")
    elif op == 4:
        op_i("beq")
    elif op == 1 and rt == 1:
        op_i("bgez")
    elif op == 7:
        op_i("bgtz")
    elif op == 6:
        op_i("blez")
    elif op == 1:
        op_i("bltz")
    elif op == 5:
        op_i("bne")
    elif op == 36:
        op_i("lbu")
    elif op == 33:
        op_i("lh")
    elif op == 37:
        op_i("lhu")
    elif op == 35:
        op_i("lw")
    elif op == 49:
        op_i("lwcl")
    elif op == 40:
        op_i("sb")
    elif op == 41:
        op_i("sh")
    elif op == 43:
        op_i("sw")
    elif op == 57:
        op_i("swcl")

    # Caso o Opcode for 2 e 3, é utilizado a instrução do tipo J
    if op == 2:
        op_j("j",address)
    elif op == 3:
        op_j("jal",address)

#fecha a leitura do arquivo entrada.txt
arq.close()

print("Convertendo o código binário em Assembly ...")

#Saida das instruções para saida.txt
arq_saida = open('saida.txt', 'w')
arq_saida.writelines(texto_saida)
arq_saida.close()
print("Arquivo saida.txt gerado")

#apenas mantem o terminal aberto
input()
