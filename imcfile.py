with open('imc1.txt', 'r') as filestream:
    for line in filestream:
        linha=line.split(",")
        # print (linha)
        # print (linha[0],linha[1], linha[2])
        #print ('Nome:%s, altura:%f, peso:%i' % linha[0], float(linha[1]), linha[2]))
        nome=linha[0]
        altura=float(linha[1])
        peso=float(linha[2])
        imc = peso / (altura ** 2.)
        print('Nome: {0}, Altura: {1}, peso: {2}, imc: {3}'. format(nome, altura, peso, imc))

