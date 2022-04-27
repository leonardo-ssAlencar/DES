"""
Algoritmo usado para encriptar o texto
"""
from util.Chave import *
from util.Texto import *
import codecs

TAM_TEXTO = 8
SEPARADOR = 64*"-"

def hexToBin(texto): # Formata a string de entrada para binario
  textoA = ""

  hexToBin = {"0" : "0000", "1" : "0001", "2" : "0010", "3" : "0011", 
              "4" : "0100", "5" : "0101", "6" : "0110", "7" : "0111", 
              "8" : "1000", "9" : "1001", "a" : "1010", "b" : "1011", 
              "c" : "1100", "d" : "1101", "e" : "1110", "f" : "1111" } # Tabela para passa hexadecimal para binario
  for i in texto:
    textoA = textoA + (hexToBin.get(i))
  
  return textoA

def binToHex(texto): # Formata para hexadecimal
  textoA = ""
  binToHex = { "0000": "0", "0001" : "1" ,"0010" : "2", "0011" : "3", 
               "0100": "4" ,"0101" : "5", "0110" : "6", "0111" : "7", 
              "1000" : "8", "1001" : "9", "1010" : "a", "1011" : "b", 
              "1100" : "c", "1101" : "d", "1110" : "e", "1111" : "f"} # Tabela para passa hexadecimal para binario
  sep = ""
  cont = 0
  
  for i in range(len(texto)):
    sep = sep + texto[i]
    cont+=1

    if cont == 4:
      textoA = textoA + binToHex.get(sep)
      cont = 0
      sep = ""
  
  return textoA

def gerarChaves(chaveBin): # Recebe a chave em binario e gera as chaves das 16 rodadas
   chaveA, chaveB = permutacaoChave(chaveBin)
   listaChaves = []
   for i in range(RODADA):
       esqC = circularChaves(chaveA, i)
       dirC = circularChaves(chaveB, i)
       
       chavePemutada = permutacaoChaveB(esqC, dirC)
       listaChaves.append(chavePemutada)
       chaveA = esqC
       chaveB = dirC
    
   return listaChaves


def feistel(texto, lChaves): 
    ladoE, ladoD = permutacaoInicial(texto)

    for i in range(RODADA):
     saida = expansaoDeBits(ladoD)
     saida = operacaoXor(lChaves[i], saida)
     saida = separarBits(saida)
     saida = tranSsBox(saida)
     saida = permutacaoFinal(saida)
    
     temp = ladoD
     ladoD = operacaoXor(ladoE, saida)
     ladoE = temp
   
    return verdadeiraPermutacaoFinal(ladoE, ladoD)

def feistelReverso(textoCifrado, lChaves):
    ladoE, ladoD = permutacaoInicial(textoCifrado)

    for i in range(RODADA - 1, -1, -1):
     saida = expansaoDeBits(ladoD)
     saida = operacaoXor(lChaves[i], saida)
     saida = separarBits(saida)
     saida = tranSsBox(saida)
     saida = permutacaoFinal(saida)
    
     temp = ladoD
     ladoD = operacaoXor(ladoE, saida)
     ladoE = temp 

    return verdadeiraPermutacaoFinal(ladoE, ladoD)


def encriptar(textoEmBin, chaveEmBin): #Encripta um texto em binario
  chavesGeradas = gerarChaves(chaveEmBin)
  textoCriptografado = feistel(textoEmBin, chavesGeradas)

  return textoCriptografado

def descriptar(textoEmBin, chaveEmBin): #Desencripta um texto em binario
  chavesGeradas = gerarChaves(chaveEmBin)
  textoDescriptografado = feistelReverso(textoEmBin, chavesGeradas)

  return textoDescriptografado
