__author__ = "Rómulo Nogueira"

### 1

def carregarVocabulario(filename):
  dic = set()
  for line in open(filename, 'r', encoding='utf8'):
    dic.add(line.rstrip().lower())
  return sorted(dic)

dic = carregarVocabulario('vocabulario.txt')


### 2


import re

def gerarPalavras(texto):
    frase = []
    r = '[`@\=~!-#$%^&*)(_+\[\]{};\'\\:"|<,./<>?\s01234567890]'
    caracteres = re.split(r,texto)
    for x in caracteres:
        if x != '':
            frase.append(x)
    return frase



### 3

def mmLetras(palavra1, palavra2):
    tamanho1 = len(palavra1)
    tamanho2 = len(palavra2)
    stringAux = ''
    if tamanho1 == tamanho2:
        for x in range (len(palavra1)):
            if palavra1[x] != palavra2[x]:
                stringAux = stringAux + ''
            else:
                stringAux = stringAux + palavra1[x]
            tamanhoStringAux = len(stringAux)
        if palavra1 == palavra2:
            return 0
        else:
            return tamanho1 - tamanhoStringAux
    else:
        for x in range(min(tamanho1,tamanho2)):
            if palavra1[x] != palavra2[x]:
                stringAux = stringAux + ''
            else: 
                stringAux = stringAux + palavra1[x]
        tamanhoStringAux = len(stringAux)
        return max(tamanho1,tamanho2) - tamanhoStringAux

### 4

def edicoes(palavra1, palavra2):
    tamanho1 = len(palavra1)
    tamanho2= len(palavra2)
    colunas = tamanho1 + 1
    linhas = tamanho2 + 1
    matriz = [[0 for j in range(tamanho1 + 1)] 
              for i in range (tamanho2 + 1)]
    
    i = 0
    while i < linhas:
        matriz[i][0] = i
        i += 1
    j=0
    while j < colunas:
        matriz[0][j] = j
        j += 1
    
    for i in range (1, linhas):
        for j in range (1, colunas):
            if palavra1[j-1] != palavra2[i-1]:
                matriz[i][j] = min([matriz[i-1][j], 
                                    matriz[i][j-1], 
                                    matriz[i-1][j-1]]) + 1
            else:
                matriz[i][j] = matriz[i-1][j-1]
    return matriz[tamanho2][tamanho1]
        


### 5
  
def sugerir(dic, palavra, distancia, maxSugestoes=5):
    listaAux=[]
    listaNova=[]
    listaDistancia=[]
    for abc in dic:
        if distancia(palavra,abc) < len(palavra):
            checkmmletras=distancia(palavra,abc)
            listaAux.extend([[checkmmletras,abc]])
    listaAux.sort(key = lambda i: i[0])
    contador=0
    for listaNova in listaAux:
        if contador < maxSugestoes:
            listaDistancia.append(listaNova[1])
            contador=contador+1
    listaDistancia.sort()   
    return listaDistancia[:maxSugestoes]



### 6

def corretor(dic, texto, distancia, maxSugestoes=5): 
    for palavra in gerarPalavras(texto):
        if palavra not in dic:
            print("{palavraErrada} --> {sugestoes}".format(palavraErrada = palavra, sugestoes = sugerir(dic, palavra, distancia, maxSugestoes)))