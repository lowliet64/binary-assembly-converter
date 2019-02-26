assembly = input().split()
#Get instructions
instruction = assembly[0]
#remove $ from registrator

rs = assembly[1]
rs = rs.replace("$","")
rs = rs.replace(",","")
rs = rs.replace("(","")
rs = rs.replace(")","")

rs = bin(int(rs))
rs = rs.replace("0b","")
while len(rs) <= 4:
    rs = "0"+rs


print(rd,rs,rt)