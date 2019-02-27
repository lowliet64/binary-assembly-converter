assembly = input().split()
#Get instructions
instruction = assembly[0]

def fsa():
    sa = assembly[4]
    sa = sa.replace("$","")
    sa = sa.replace(",","")
    sa = bin(int(sa))
    sa = sa.replace("0b","")
    while len(sa) <= 4:
        sa = "0"+sa
    return sa

def imm_res():
    assembly[1] = assembly[1].replace("$","")
    assembly[2] = assembly[2].replace("$","")
    rs = assembly[1]
    rs = rs.replace(",","")
    rs = bin(int(rs))
    rs = rs.replace("0b","")
    while len(rs) <= 4:
        rs = "0"+rs


    assembly2 = assembly[2].split("(")
    rt = assembly2[0]
    rt = bin(int(rt))
    rt = rt.replace("0b","")
    while len(rt) <= 4:
        rt = "0"+rt


    imm = assembly[1].replace(")","")
    imm = imm.replace(",","")
    imm = bin(int(imm))
    imm = imm.replace("0b","")
    while len(imm) <= 15:
        imm = "0"+imm

    return rs+rt+imm

#Type R array
instructions_r = ['sll','srvl','sra','sllv','srl','srav','jr','jalr','syscall',
'add','addu','sub','break','div','divu','mfhi','mflo','subu','mult','multu',
'mtlo','mthi','subu','and','or','xor','nor','slt','sltu']

#Type I

instruction_i = ['addi','addiu','andi','beq','bgez','bgtz','blez','bltz',
'bne','lb','lbu','lh','lhu','lui','lw','lwcl','ori','sb','slti','sltiu',
'sh','sw','swcl','xori']

#Instructions type R
if instruction in instructions_r:
    #remove $ from registrator
    rd = assembly[1]
    rd = rd.replace("$","")
    rd = rd.replace(",","")

    rs = assembly[2]
    rs = rs.replace("$","")
    rs = rs.replace(",","")
    rs = rs.replace("(","")
    rs = rs.replace(")","")

    rt = assembly[3]
    rt = rt.replace("$","")
    rt = rt.replace(",","")

    #Transform RD, RS, RT in binary and add 0 if the registrator is less than 5 bits
    rd = bin(int(rd))
    rd = rd.replace("0b","")
    while len(rd) <= 4:
        rd = "0"+rd

    rs = bin(int(rs))
    rs = rs.replace("0b","")
    while len(rs) <= 4:
        rs = "0"+rs

    rt = bin(int(rt))
    rt = rt.replace("0b","")
    while len(rt) <= 4:
        rt = "0"+rt

    if instruction == "sll":
        binary_code = "00000000000{}{}{}000000".format(rd,rt,fsa())
    elif instruction == "srlv":
        binary_code = "000000{}{}{}00000000110".format(rd,rt,rs)
    elif instruction == "sra":
        binary_code = "00000000000{}{}{}000011".format(rd,rt,fsa())
    elif instruction == "sllv":
        binary_code = "000000{}{}{}00000000011".format(rd,rt,rs)
    elif instruction == "srl":
        binary_code = "00000000000{}{}{}000010".format(rd,rt,fsa())
    elif instruction == "srav":
        binary_code = "000000{}{}{}00000000111".format(rd,rt,rs)
    elif instruction == "jr":
        binary_code = "000000{}000000000000000001000".format(rs)
    elif instruction == "jalr":
        binary_code = "000000{}{}0000000000001001".format(rd,rs)
    elif instruction == "syscall":
        binary_code = "00000000000000000000000000001100"
    elif instruction == "add":
        binary_code = "000000{}{}{}00000100000".format(rd,rs,rt)
    elif instruction == "addu":
        binary_code = "000000{}{}{}00000100001".format(rd,rs,rt)
    elif instruction == "sub":
        binary_code = "000000{}{}{}00000100010".format(rd,rs,rt)    
    elif instruction == "break":
        binary_code = "00000000000000000000000000001101"
    elif instruction == "div":
        binary_code = "000000{}{}0000000000011010".format(rs,rt)  
    elif instruction == "dvu":
        binary_code = "000000{}{}0000000000100010".format(rs,rt) 
    elif instruction == "mfhi":
        binary_code = "000000{}000000000000000010000".format(rd) 
    elif instruction == "mflo":
        binary_code = "000000{}000000000000000010010".format(rd) 
    elif instruction == "mult":
        binary_code = "000000{}{}0000000000011000".format(rs,rt) 
    elif instruction == "multu":
        binary_code = "000000{}{}0000000000011001".format(rs,rt) 
    elif instruction == "mtlo":
        binary_code = "000000{}000000000000000010011".format(rs) 
    elif instruction == "mthi":
        binary_code = "000000{}000000000000000010001".format(rs) 
    elif instruction == "subu":
        binary_code = "000000{}{}{}00000100011".format(rd,rs,rt)
    elif instruction == "and":
        binary_code = "000000{}{}{}00000100100".format(rd,rs,rt)  
    elif instruction == "or":
        binary_code = "000000{}{}{}00000100101".format(rd,rs,rt) 
    elif instruction == "xor":
        binary_code = "000000{}{}{}00000100011".format(rd,rs,rt) 
    elif instruction == "nor":
        binary_code = "000000{}{}{}00000100011".format(rs,rt,rd) 
    elif instruction == "slt":
        binary_code = "000000{}{}{}00000101010".format(rd,rs,rt) 
    elif instruction == "sltu":
        binary_code = "000000{}{}{}00000101011".format(rd,rs,rt) 

#Instructions type I
if instruction in instruction_i:
    if instruction != "lb" and instruction != "lbu" and instruction != "lh" and instruction != "lhu" and instruction != "lw" and instruction != "lqcl" and instruction != "sb" and instruction != "sh" and instruction != "sw" and instruction != "swcl":
        rs = assembly[1].replace("$","")
        rs = rs.replace(",","")
        rs = bin(int(rs))
        rs = rs.replace("0b","")
        while len(rs) <= 4:
            rs = "0"+rs

        rt = assembly[2].replace("$","")
        rt = rt.replace(",","")
        rt = bin(int(rt))
        rt = rt.replace("0b","")
        while len(rt) <= 4:
            rt = "0"+rt
        
        imm = assembly[3].replace("$","")
        imm = imm.replace(",","")
        imm = bin(int(imm))
        imm = imm.replace("0b","")
        while len(imm) <= 15:
            imm = "0"+imm

    if instruction == "addi":
        binary_code = "001000{}{}{}".format(rt,rs,imm) 
    elif instruction == "addiu":
        binary_code = "001001{}{}{}".format(rt,rs,imm) 
    elif instruction == "andi":
        binary_code = "001100{}{}{}".format(rt,rs,imm) 
    elif instruction == "beq":
        binary_code = "000100{}{}0000000000000000".format(rs,rt) 
    elif instruction == "bgez":
        binary_code = "000001{}000000000000000000000".format(rs) 
    elif instruction == "bgtz":
        binary_code = "000001{}000000000000000000000".format(rs)         
    elif instruction == "blez":
        binary_code = "000001{}000000000000000000000".format(rs) 
    elif instruction == "bltz":
        binary_code = "000001{}000000000000000000000".format(rs) 
    elif instruction == "bne":
        binary_code = "000101{}{}0000000000000000".format(rs,rt)
    elif instruction == "lb":
        binary_code = "100000{}".format(imm_res())
    elif instruction == "lbu":
        binary_code = "100001{}{}{}".format(rt,imm,rs)
    elif instruction == "lh":
        binary_code = "100100{}{}{}".format(rt,imm,rs)
    elif instruction == "lhu":
        binary_code = "100100{}{}{}".format(rt,imm,rs)
    elif instruction == "lui":
        binary_code = "001111{}{}".format(rt,imm)
    elif instruction == "lw":
        binary_code = "100011{}{}{}".format(rt,imm,rs)
    elif instruction == "lwcl":
        binary_code = "110001{}{}{}".format(rt,imm,rs)
    elif instruction == "ori":
        binary_code = "001101{}{}{}".format(rt,rs,imm)
    elif instruction == "slti":
        binary_code = "001010{}{}{}".format(rt,imm,rs)
    elif instruction == "sb":
        binary_code = "101000{}{}{}".format(rt,imm,rs)
    elif instruction == "sltiu":
        binary_code = "001111{}{}{}".format(rt,rs,imm)
    elif instruction == "sh":
        binary_code = "101001{}{}{}".format(rt,imm,rs)
    elif instruction == "sw":
        binary_code = "101011{}{}{}".format(rt,imm,rs)
    elif instruction == "swcl":
        binary_code = "111001{}{}{}".format(rt,imm,rs)
    elif instruction == "xori":
        binary_code = "001110{}{}{}".format(rt,rs,imm)

print(binary_code)
