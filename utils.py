def leituraDoArquivoDeEntrada(arquivo):

    #Leitura do arquivo armazenando em uma variável
    f = open(arquivo, 'r', encoding='utf8')
    dados = (f.readlines())

    #Eliminando "\n"
    newData = []
    for linha in dados:
        newData.append(linha.replace("\n", ""))
    

    #Separando conjuntos de estados iniciais e finais
    conjuntoEstadosIniciaisFinais = (newData[0].split(sep=" ; "))
    conjuntoEstadosIniciais = list(conjuntoEstadosIniciaisFinais[0].split(sep=" "))
    conjuntoEstadosFinais = list(conjuntoEstadosIniciaisFinais[1].split(sep=" "))

    #Separando conjuntos com funções de transições e conjunoto de teste
    conjuntoTransicoes = []
    conjuntoTeste = []

    for i in range(1, len(newData)):
        if("test" in newData[i]): 
            conjuntoTeste.append(newData[i].replace("test: ", ""))
        else:    
            conjuntoTransicoes.append(newData[i].replace(" ", ""))

    # Separando conjunto de alfabeto
    alfabeto = []
    estados = []

    for i in range(0, len(conjuntoTransicoes)):
        if conjuntoTransicoes[i][1] not in alfabeto:
            alfabeto.append(conjuntoTransicoes[i][1])      

        if conjuntoTransicoes[i][0] not in estados:
            estados.append(conjuntoTransicoes[i][0]) 
        
        if conjuntoTransicoes[i][2] not in estados:
            estados.append(conjuntoTransicoes[i][2]) 
       

    return conjuntoEstadosIniciais, conjuntoEstadosFinais, conjuntoTransicoes, conjuntoTeste, alfabeto, estados

#-----------------------------------------------------------------------------------------------
def Verifica_AFD_AFN(conjuntoTransicoes, conjuntoEstadosIniciais):
    
    if(len(conjuntoEstadosIniciais) > 1):
        return 'AFN'

    contador = 0
    for i in range(len(conjuntoTransicoes)):
        for j in range(i+1, len(conjuntoTransicoes)):
            if(conjuntoTransicoes[i][0] == conjuntoTransicoes[j][0] and conjuntoTransicoes[i][1] == conjuntoTransicoes[j][1]):
                contador+=1

    if contador > 0:
        return 'AFN'
    else:
        return 'AFD'        

#-----------------------------------------------------------------------------------------------
def criandoMatrizTransicoes(conjuntoTransicoes, alfabeto, estados):
    
    matriz = []
    mapa = {}

    # Criando matriz de transições e mapa
    for i in range(len(estados)+1):
        linha = []
        for j in range(len(alfabeto)+1):
            if(i == 0 and j > 0):
                linha.append(alfabeto[j-1])
                mapa[alfabeto[j-1]] = j 
            elif(i > 0 and j == 0):  
                linha.append(estados[i-1])
                mapa[estados[i-1]] = i 
            else:
                linha.append('e')
        matriz.append(linha) 
     

    # Preenchendo a matriz de transições com o mapa
    for i in range(len(conjuntoTransicoes)):
        posicaoEstadoDePartida = conjuntoTransicoes[i][0]
        posicaoSimboloDoAlfabeto = conjuntoTransicoes[i][1]
        matriz[int(mapa[posicaoEstadoDePartida])][int(mapa[posicaoSimboloDoAlfabeto])] = conjuntoTransicoes[i][2]

    return matriz, mapa

#-------------------------------------------------------------------------------------------------
def processamentoDaPalavra(matrizTransicoes, mapa, palavra, conjuntoEstadosIniciais, conjuntoEstadosFinais):

    print(f'Iniciando processamento de {palavra}')
    print(f'Configurações iniciais: [{conjuntoEstadosIniciais[0]}, {palavra}]')

    estadoAtual = conjuntoEstadosIniciais[0]
    palavraProcessada = palavra 

    if(palavra != 'lambda'):
        for i in range(len(palavra)):

            print(f'Executando a transição {estadoAtual} -{palavra[0]}-> {matrizTransicoes[mapa[estadoAtual]][mapa[palavra[0]]]} resulta em [{matrizTransicoes[mapa[estadoAtual]][mapa[palavra[0]]]}, {palavra[1:] if len(palavra)-1 > 0 else "lambda"}]')
            
            estadoAtual = matrizTransicoes[mapa[estadoAtual]][mapa[palavra[0]]]
            
            # Estado de Erro do automato
            if(estadoAtual == 'e'):
                break
            
            palavra = palavra[1:]      

    if(estadoAtual in conjuntoEstadosFinais):
        print(f'{estadoAtual} é um estado final')
        print(f'A palavra {palavraProcessada} é aceita pelo AF')

    else:
        if estadoAtual == 'e':
            print(f'{estadoAtual} é um estado de erro')

        else: 
            print(f'{estadoAtual} não é estado final')
        
        print(f'A palavra {palavraProcessada} não é aceita pelo AF')
        

#-----------------------------------------------------------------------------------------------
