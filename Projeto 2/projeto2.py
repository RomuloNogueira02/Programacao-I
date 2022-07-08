__author__ = "Rómulo Nogueira"

import matplotlib.pyplot as plt
import numpy as np
import math

def criarDados(k, ns, mus, covs, seed=-1):
  """
  k    : número de aglomerados
  ns   : lista com os tamanhos de cada aglomerado
  mus  : lista dos centros de cada aglomerado
  covs : lista com as matrizes de covariância
  seed : valor para controlar a aleatoriadade (default -1 -> imprevísivel)
  
  retorna uma lista de pares com coordenadas (x,y)
  """
  if seed != -1:
    np.random.seed(seed)
  xs = []
  ys = []
  for i in range(k):
    x,y = np.random.multivariate_normal(mus[i], covs[i], ns[i]).T
    xs.extend(x)
    ys.extend(y)
  
  return (xs,ys)

def criarPontos(ns, seed=-1):
  """
  requires: len(ns) < 8
  """
  k    = len(ns)
  mus  = [[0, 0], [5,5], [4,-5],[-5,-5],[-4,5],[-7.5,0],[0,8]]
  covs = [
      [[2,    0], [    0,  2]],
      [[1, -0.5], [ -0.5,  1]],
      [[2, 0.75], [ 0.75, .5]],
      [[2, 0.75], [ 0.75, .5]],
      [[2,-0.75], [-0.75,  1]],
      [[1, -0.5],  [-0.5,  1]],
      [[1, -0.5], [ -0.5,  1]],
    ]

  x,y = criarDados(k, ns[:k], mus[:k], covs[:k], seed)
  pts = [ (x[i],y[i]) for i in range(len(x))]
  return pts


pts = criarPontos([140, 50, 100, 160, 120], 101)

for pt in pts:
  plt.scatter(pt[0], pt[1], marker=".", color='k')
plt.show()  


### 1

def distancia(pt1, pt2):
    x1 = float(pt1[0])
    x2 = float(pt2[0])
    y1 = float(pt1[1])  
    y2 = float(pt2[1])
    distancia = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    return distancia


### 2

centroides = [(10,10), (20,10), (0,0)]
# centroides = [(10,10), (0,0)]

def sugerirCentroide(centros, pt):
    listaCentroides = []
    for ponto in centroides:
        verificarDistancia = distancia(ponto, pt) 
        listaCentroides.append(verificarDistancia)
        minimo = min(listaCentroides)
    return listaCentroides.index(minimo)


### 3

def encontrarCentroMassa(pts):
    tamanhoPts = len(pts)
    listaX = []
    listaY = []
    listaSumX = []
    listaSumY = []
    for ponto in pts:
        listaX.append(ponto[0])
        listaY.append(ponto[1])
    listaSumX = sum(listaX) / tamanhoPts
    listaSumY = sum(listaY) / tamanhoPts
    centro = (listaSumX , listaSumY)
    return centro

### 4

def aglomerar(k, pts, tol=0.001, maxIter=500):
    centroides = pts[:k]
    for x in pts:
        pontosProx = pts[sugerirCentroide(centroides , x)]
    return 

### 5

def custear(centros, pts):
    distancias=[]
    for ponto in pts:
       pontosProx = centros[sugerirCentroide(centros,ponto)]
       distancias.append(distancia(pontosProx,ponto)**2)
    return sum(distancias)


### 6

def sugerirK(pts, minK=2, maxK=10):
    associar=[]
    listaCusto =[]
    for k in range(minK,maxK):
        centros = aglomerar(k,pts)
        custo = custear(centros,pts)*(k**1.5)
        listaCusto.append(custo)
        minimo = min(listaCusto)
        associar.append([k, custo])
    for ponto in associar:
        if ponto[1] == minimo:
            return ponto[0]

