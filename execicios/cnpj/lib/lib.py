def validaint(variavel):
    try:
        ret = int(variavel)
    except:
        print(f'O parametro {variavel} não é formado por numeros.')
        return False
    else:
        return True


def validatamanho(variavel):
    if len(variavel) != 14:
        print(f'O numero "{variavel}" passado tem que ter 14 digitos.')
        return False
    else:
        return True


def pegarpartes(variavel,tamanho):
    parte = list(variavel) 
    return parte[:tamanho]


def calculo(variavel):
    num = pegarpartes(variavel,12)
    mutiplicador1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    dig1 = calculos(num,mutiplicador1)

    mutiplicador2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    dig2 = calculos(dig1,mutiplicador2)
    ret = ''.join(dig2)
    return ret


def calculos(variavel,mutiplicador):
    s = 0
    for k,item in enumerate(variavel):
        s += int(item) * int(mutiplicador[k])
    dig = (11 - (s % 11))
    if dig > 9:
        dig = 0
        variavel.append(str(dig))
        return variavel
    else:
        variavel.append(str(dig))
        return variavel


def formataCNPJ(cnpj):
    ret = cnpj[:2]+'.'+cnpj[2:5]+'.'+cnpj[5:8]+'/'+cnpj[8:12]+'-'+cnpj[12:14]  # CPF formatado
    return ret

def validaCNPJ(cnpj):
    if validaint(cnpj):
        if validatamanho(cnpj):
            if cnpj == calculo(cnpj):
                ret = formataCNPJ(calculo(cnpj))
                print(f'CNPJ: {ret} válido.')
            else:
                ret = formataCNPJ(calculo(cnpj))
                print(f'O cnpf: {ret} esta inválido.')
