# Depuracao-Automatos-Finitos
Teoria da Computação


Este trabalho tem como objetivo simular o processamento de uma palavra de entrada através de um Autômato Finito
Determinístico, AFD. O programa desenvolvido recebe como argumento o nome de um arquivo texto com as especificações
de um autômato, seguido de uma sequência de palavras testes para que sejam validadas se pertencem ou não a linguagem
proposta. Para a implementação do trabalho prático, foi utilizado a linguagem Python 3.9.0.


Programa
O programa desenvolvido consiste de dois arquivos, sendo eles: main.py e utils.py. O arquivo main.py é onde ocorrem
todas as chamadas de funções necessárias para para o processamento da palavra. Já o arquivo utils.py é composto por todas
as implementações das funções usadas, sendo elas:
1. leituraDoArquivoDeEntrada(arquivo): Essa função é responsável por ler o arquivo de entrada escolhido, que será
passado por parâmetro, e depois realizará todas as separações dos dados em conjuntos que constituem o autômato
e as palavras teste. A função retornará os seguintes conjuntos: conjunto dos estados iniciais, conjunto dos estados
finais, conjuntos de transições, conjuntos de palavras para teste, alfabeto e conjuntos de estados.
2. verifica_AFD_AFN(conjuntoTransicoes): Essa função recebe como parâmetro o conjunto de transições do
autômato e, a partir deste conjunto, irá verificar se há algum estado processando algum símbolo do alfabeto com
mais de um estado de destino. Caso ocorra, o retorno da função será uma string “AFN”, representando que o
autômato é não determinístico e caso contrário retornará “AFD”, representando que o autômato é determinístico.
3. criandoMatrizTransicao(conjuntoTransicao, alfabeto, conjuntoEstado): Essa função tem o objetivo de gerar e
retornar uma matriz de transição preenchida para auxiliar no processamento das palavras. Além disso, ela também
gera um dicionário, chamado “mapa”, que irá auxiliar no acesso dos índices matriz.
4. processamento_da_palavra(matrizDeTransicoes, mapa, palavraTeste, conjuntoEstadosIniciais,
conjuntoEstadosFinais): Essa função é responsável por todo o retorno dos resultados do processamento da
palavra.