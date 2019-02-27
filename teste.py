assembly = input().split()

def imm_res(assembly):
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

print(imm_res(assembly))
