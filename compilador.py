'''
Feito por Simei Thander - TADS 2018.2
'''


def convert_dec(n):
    n = (str(n)[::-1])
    total = 0
    for i in range(len(n)):
        total += (int(n[i]) * (2 ** i))
    return total


# calcular o código address
def calc_address(str):
    cont_address = 1
    cont_address_total = 0

    for i in range(len(address_inver)):
        if i != 0:
            cont_address *= 2

        if int(address_inver[i]) == 1:
            cont_address_total += 1 * cont_address
    return cont_address_total


def op_r(inst):
    global rt, rs, rt
    print("{} ${}, ${}, ${}".format(inst, rd, rs, rt))


def op_i(inst):
    global rt, imm, rs
    print("{} {}$, {}(${})".format(inst, rt, imm, rs))


# leitura do codigo binário
codigo_bin = input("Digite o codigo binário: ")

# captura as variáveis e operações da String e converte em decimal
op = convert_dec(codigo_bin[:6])
rt = convert_dec(codigo_bin[11:16])
rs = convert_dec(codigo_bin[6:11])
rd = convert_dec(codigo_bin[14:19])
imm = convert_dec(codigo_bin[16:])
func = convert_dec(codigo_bin[26:])
address = codigo_bin[6:]
address_inver = address[::-1]

# main code

# Operação do tipo R
if op == 0:
    if func == 32:
        op_r("add")
    if func == 33:
        op_r("addu")
    if func == 34:
        op_r("sub")
    if func == 36:
        op_r("and")
    if func == 13:
        op_r("break")
    if func == 26:
        op_r("div")
    if func == 27:
        op_r("divu")
    if func == 9:
        op_r("jalr")
    if func == 8:
        op_r("jr")
    if func == 16:
        op_r("mfhi")
    if func == 18:
        op_r("mflo")
    if func == 24:
        op_r("mult")
    if func == 25:
        op_r("multu")
    if func == 19:
        op_r("mtlo")
    if func == 17:
        op_r("mthi")
    if func == 35:
        op_r("subu")
    if func == 36:
        op_r("and")
    if func == 37:
        op_r("or")
    if func == 38:
        op_r("xor")
    if func == 39:
        op_r("nor")
    if func == 42:
        op_r("slt")
    if func == 43:
        op_r("sltu")

# Operação do tipo I
if op == 32:
    op_i("lb")
if op == 33:
    op_i("ih")
if op == 8:
    op_i("addi")
if op == 9:
    op_i("addiu")
if op == 10:
    op_i("slti")
if op == 11:
    op_i("sltiu")
if op == 12:
    op_i("andi")
if op == 13:
    op_i("ori")
if op == 14:
    op_i("xori")
if op == 15:
    op_i("lui")
if op == 4:
    op_i("beq")
if op == 1 and rt == 1:
    op_i("bgez")
if op == 7:
    op_i("bgtz")
if op == 6:
    op_i("blez")
if op == 1:
    op_i("bltz")
if op == 5:
    op_i("bne")
if op == 36:
    op_i("lbu")
if op == 33:
    op_i("lh")
if op == 37:
    op_i("lhu")
if op == 35:
    op_i("lw")
if op == 49:
    op_i("lwcl")
if op == 40:
    op_i("sb")
if op == 41:
    op_i("sh")
if op == 43:
    op_i("sw")
if op == 57:
    op_i("swcl")


# Operação do tipo J
if op == 2:
    print("j {}".format(calc_address(address_inver)))
