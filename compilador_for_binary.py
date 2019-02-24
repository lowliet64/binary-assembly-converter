assembly = input().split()
#Get instructions
instruction = assembly[0]

#Type R array
instructions_r = ['sll','srvl','sra','sllv','srl','srav','jr','jalr','syscall','add','addu','sub','break','div','divu','mfhi','mflo','subu','mult','multu',
'mtlo','mthi','subu','and','or','xor','nor','slt','sltu']

#Instructions type R
if instruction in instructions_r:

    #remove $ from registrator
    rd = assembly[1]
    rd = rd.replace("$","")
    rd = rd.replace(",","")
    rs = assembly[2]
    rs = rs.replace("$","")
    rs = rs.replace(",","")
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
        print()
    elif instruction == "srvl":
        print()
    elif instruction == "sra":
        print()
    elif instruction == "sllv":
        print()
    elif instruction == "srl":
        print()
    elif instruction == "srav":
        print()
    elif instruction == "jr":
        print()
    elif instruction == "jalr":
        print()
    elif instruction == "syscall":
        print()
    elif instruction == "add":
        print("000000{}{}{}00000100000".format(rd,rs,rt))
    elif instruction == "addu":
        print()
    elif instruction == "sub":
        print("000000{}{}{}00000100010".format(rd,rs,rt))      
    elif instruction == "break":
        print()
    elif instruction == "div":
        print()
    elif instruction == "dvu":
        print()
    elif instruction == "mfhi":
        print()
    elif instruction == "mflo":
        print()
    elif instruction == "mult":
        print()
    elif instruction == "multu":
        print()
    elif instruction == "mtlo":
        print()
    elif instruction == "mthi":
        print()
    elif instruction == "subu":
        print()
    elif instruction == "and":
        print()
    elif instruction == "or":
        print()
    elif instruction == "xor":
        print()
    elif instruction == "nor":
        print()
    elif instruction == "slt":
        print()
    elif instruction == "sltu":
        print()
