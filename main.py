import utils
import sys
import argparse

# Aluno: Felipe Augusto Vasconcelos e Silva
# Matricula: 16.2.4358

def main():

    parser = argparse.ArgumentParser(description='args')
    parser.add_argument('--file')
    arg = parser.parse_args()

    #Separando os conjuntos 
    conjuntoEstadosIniciais, conjuntoEstadosFinais, conjuntoTransicoes, conjuntoTeste, alfabeto, estados = utils.leituraDoArquivoDeEntrada(arg.file)

    # Verificação se o automato é AFD ou AFN
    tipo = utils.Verifica_AFD_AFN(conjuntoTransicoes, conjuntoEstadosIniciais)
    
    if(tipo == 'AFD'):

        #Criando matriz de transições
        matrizTransicoes, mapa = utils.criandoMatrizTransicoes(conjuntoTransicoes, alfabeto, estados)
        
        # Executando o processamento da palavra
        for i in range(len(conjuntoTeste)):
            print(f'Teste {i+1}')
            utils.processamentoDaPalavra(matrizTransicoes, mapa, conjuntoTeste[i], conjuntoEstadosIniciais, conjuntoEstadosFinais)
            print(50*'-')

    if(tipo == 'AFN'):
        print("Não é possível executar um AFN")
        


if __name__ == '__main__':
    sys.exit(main())