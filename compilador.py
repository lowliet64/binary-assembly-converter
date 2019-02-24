'''
Crate by Simei Thander - TADS 2018.2

'''
print("---------------------------")
print("add the binary code in entrada.txt at root folder")
print("---------------------------")
print("Tap 0 for Binaty to Assembly")
print("Tap 1 for Assembly to Binaty")
print("Tap anything key for exit")
option = int(input())

if option == 0:

    texto_saida = []

    #def for converting decimal in binary
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

    # main code

    # Read the binary code in entrada.txt 
    print("Lendo arquivo entrada.txt ...")
    arq = open('entrada.txt', 'r+')
    texto = arq.readlines()

    for linha in texto:

        # captura as variáveis e operações da String e converte em decimal
        op = convertdecimal(linha[:6].rstrip())
        rt = convertdecimal(linha[11:16].rstrip())
        rs = convertdecimal(linha[6:11].rstrip())
        rd = convertdecimal(linha[14:19].rstrip())
        sa = convertdecimal(linha[20:25].rstrip())
        imm = convertdecimal(linha[16:].rstrip())
        func = convertdecimal(linha[26:].rstrip())
        address = convertdecimal(linha[6:].rstrip())

        # if opcode is 0, the functions is verified
        if op == 0:
            if func == 0:
                texto_saida.append("sll ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 2:
                texto_saida.append("srvl ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 3:
                texto_saida.append("sra ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 4:
                texto_saida.append("sllv ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 6:
                texto_saida.append("srl ${}, ${}, ${} \n".format(rd, rs, sa))
            elif func == 7:
                texto_saida.append("srav ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 8:
                texto_saida.append("jr ${} \n".format(rs))
            elif func == 9:
                texto_saida.append("jalr ${}, ${} \n".format(rd, rs))  
            elif func == 12:
                texto_saida.append("syscall \n")
            elif func == 32:
                texto_saida.append("add ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 33:
                texto_saida.append("addu ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 34:
                texto_saida.append("sub ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 36:
                texto_saida.append("addu ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 13:
                texto_saida.append("break \n")
            elif func == 26:
                texto_saida.append("div ${}, ${} \n".format(rs, rt))
            elif func == 27:
                texto_saida.append("dvu ${}, ${} \n".format(rs, rt))     
            elif func == 16:
                texto_saida.append("mfhi ${} \n".format(rd))
            elif func == 18:
                texto_saida.append("mflo ${} \n".format(rd))
            elif func == 24:
                texto_saida.append("mult ${}, ${} \n".format(rs, rt))
            elif func == 25:
                texto_saida.append("multu ${}, ${} \n".format(rs, rt))
            elif func == 19:
                texto_saida.append("mtlo ${} \n".format(rs))
            elif func == 17:
                texto_saida.append("mthi ${} \n".format(rt))
            elif func == 35:
                texto_saida.append("subu ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 36:
                texto_saida.append("and ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 37:
                texto_saida.append("or ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 38:
                texto_saida.append("xor ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 39:
                texto_saida.append("nor ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 42:
                texto_saida.append("slt ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 43:
                texto_saida.append("sltu ${}, ${}, ${} \n".format(rd, rs, rt))
            elif func == 35:
                texto_saida.append("subu ${}, ${}, ${} \n".format(rd, rs, rt))

        # if opcode is greater than 0, he is checked
        if op == 32:
            texto_saida.append("lb {}(${}) \n".format(rt, imm))
        elif op == 33:
            texto_saida.append("ih {}(${}) \n".format(rt, imm))
        elif op == 8:
            texto_saida.append("addi ${}, ${}, {} \n".format(rt, rs, imm))
        elif op == 9:
            texto_saida.append("addiu ${}, ${}, {} \n".format(rt, rs, imm))
        elif op == 10:
            texto_saida.append("slti ${}, ${}, {} \n".format(rt, rs, imm))
        elif op == 11:
            texto_saida.append("sltiu ${}, ${}, {} \n".format(rt, rs, imm))
        elif op == 12:
            texto_saida.append("andi ${}, ${}, {} \n".format(rt, rs, imm))
        elif op == 13:
            texto_saida.append("ori ${}, ${}, {} \n".format(rt, rs, imm))
        elif op == 14:
            texto_saida.append("xori ${}, ${}, {} \n".format(rt, rs, imm))
        elif op == 15:
            texto_saida.append("lui ${}, {} \n".format(rt, imm))
        elif op == 4:
            texto_saida.append("beq ${}, ${} \n".format(rs, rt))
        elif op == 1 and rt == 1:
            texto_saida.append("bgez ${}\n".format(rs,))
        elif op == 7 and rt == 0:
            texto_saida.append("bgtz ${} \n".format(rs))
        elif op == 6 and rt == 0:
            texto_saida.append("blez ${} \n".format(rs))
        elif op == 1 and rt == 0:
            texto_saida.append("bltz ${} \n".format(rs))
        elif op == 5:
            texto_saida.append("bne ${}, ${} \n".format(rs, rt))
        elif op == 36:
            texto_saida.append("lbu ${}, {}(${}) \n".format(rt, imm, rs))
        elif op == 33:
            texto_saida.append("lh ${}, {}(${}) \n".format(rt, imm, rs))
        elif op == 37:
            texto_saida.append("lhu ${}, {}(${}) \n".format(rt, imm, rs))
        elif op == 35:
            texto_saida.append("lw ${}, {}(${}) \n".format(rt, imm, rs))
        elif op == 49:
            texto_saida.append("lwcl ${}, {}(${}) \n".format(rt, imm, rs))
        elif op == 40:
            texto_saida.append("sb ${}, {}(${}) \n".format(rt, imm, rs))       
        elif op == 41:
            texto_saida.append("sh ${}, {}(${}) \n".format(rt, imm, rs))
        elif op == 43:
            texto_saida.append("sw ${}, {}(${}) \n".format(rt, imm, rs))
        elif op == 57:
            texto_saida.append("swcl ${}, {}(${}) \n".format(rt, imm, rs))

        # if Opcode is 2 or 3, the function J is used
        if op == 2:
            texto_saida.append("j {} \n".format(address))
        elif op == 3:
            texto_saida.append("jal {} \n".format(address))

    #fecha a leitura do arquivo entrada.txt
    arq.close()

    print("Converting binary to Assembly ...")

    #Insert the output in saida.txt
    arq_saida = open('saida.txt', 'w')
    arq_saida.writelines(texto_saida)
    arq_saida.close()
    print("File saida.txt created!")

    #keep terminal in display
    input()
elif option == 1:
    print("Function in development")
    #keep terminal in display
    input()


