# -*- coding: utf-8 -*-
"""4.1 - Reto 4(final).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VQCt-6ysGwKCyFhPPaRgyrk9VP_tva1Y
"""

# Funciones:
def LeerDatos():
  NumeroDeBaldosas_N, MemoriaSensor_K = input().split() 
  NumeroDeBaldosas_N = int(NumeroDeBaldosas_N)
  MemoriaSensor_K = int(MemoriaSensor_K)
  SerieDeBaldosas_B = [int(Elementos)for Elementos in list(input().split())]
  return NumeroDeBaldosas_N,MemoriaSensor_K,SerieDeBaldosas_B

def VerificarFallas(SerieDeBaldosas_B, MemoriaSensor_K):
  FallasTotales = 0
  FallasDetectadas = 0
  Diccionario = dict()
  
  for Veces_OrdenLectura, TipoDeBaldosa in enumerate(SerieDeBaldosas_B):   
    if (TipoDeBaldosa in Diccionario and Veces_OrdenLectura - Diccionario.get(TipoDeBaldosa) <= MemoriaSensor_K):
      FallasDetectadas = FallasDetectadas + 1
    if (TipoDeBaldosa in Diccionario):
      FallasTotales = FallasTotales + 1
    Diccionario[TipoDeBaldosa]= Veces_OrdenLectura 
    

  return FallasTotales, FallasDetectadas

# Programa principal:
NumeroDeBaldosas_N, MemoriaSensor_K, SerieDeBaldosas_B = LeerDatos()
FallasTotales,FallasDetectadas = VerificarFallas(SerieDeBaldosas_B,MemoriaSensor_K)
print(FallasTotales, FallasDetectadas,NumeroDeBaldosas_N)