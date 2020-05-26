'''
Desafio CPF
CPF = 168.995.350-09
--------------------
1 * 10 = 10         #   1 * 11 = 11
6 * 9  = 12         #   6 * 10 = 60
8 * 8  = 24         #   8 * 9  = 72
9 * 7  = 63         #   9 * 8  = 72
9 * 6  = 54         #   9 * 7  = 63
5 * 5  = 25         #   5 * 6  = 30
3 * 4  = 12         #   3 * 5  = 15
5 * 3  = 15         #   5 * 4  = 20
0 * 2  = 0          #   0 * 3  = 0
                    #   0 * 2  = 0
total = 297             total = 343
11 - (297 % 11) = 11    11 - ( 343 % 11) = 9
11 > 9 = 0              
digito 1 = 0            Digito 2 = 9
'''
# cpf = '16899535009'
cpf = input('Digite o numero do CPF: ')
cpf_parc = cpf[:-2]
if len(cpf) != 11:
    print('Tamanho do numero de CPF incorreto!')
else:
    # calculo do primeiro digito
    s = 0
    for c, v in enumerate(range(10, 1, -1)):
        s += (int(cpf_parc[c]) * v )

    r = 11 - (s % 11)

    if r > 9:
        cpf_parc += '0'
    else:
        cpf_parc += str(r)

    # print( cpf_parc )

    # Calculo do segundo digito
    s = 0
    for c, v in enumerate(range(11, 1, -1)):
        s += (int(cpf_parc[c]) * v )

    r = 11 - (s % 11)

    if r > 9:
        cpf_parc += '0'
    else:
        cpf_parc += str(r)

    # print( cpf_parc )

    fcpf = cpf[:3]+'.'+cpf[3:6]+'.'+cpf[6:9]+'-'+cpf[9:11]  # CPF formatado
    if cpf == cpf_parc:
        print(f'Numero de CPF:{fcpf} esta CORRETO.')
    else:
        print(f'Numero de CPF:{fcpf} INCORRETO, favor verifique !')
