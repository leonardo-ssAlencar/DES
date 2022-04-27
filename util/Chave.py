RODADA = 16

def permutacaoChave(chave): # Primeira permutação da chave usando a tabela tansformando 64 bits em 56 em duas partes de 28
  tabela = [ 57, 49, 41, 33, 25, 17, 9, 
             1, 58, 50, 42, 34, 26, 18,
             10, 2, 59, 51, 43, 35, 27,
             19, 11, 3, 60, 52, 44, 36,
             63, 55, 47, 39, 31, 23, 15,
             7, 62, 54, 46, 38, 30, 22,
             14, 6, 61, 53, 45, 37, 29,
             21, 13, 5, 28, 20, 12, 4 ] # tabela de permutação
             
  chaveE = "" # Chave da esquerda
  chaveD = "" # Chave da direita 
 
  cont = 1
  for i in tabela:
   if cont <= 28:
    chaveE = chaveE + chave[i-1]
   else:
     chaveD = chaveD + chave[i-1]
   
   cont+=1
  
  return chaveE, chaveD


def circularChaves(chave, rodada): # Circulando os bits das chaves
 circulacao = [1 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ] # Tabela da quantidade de bits deslocados para a 
                                                                #esquerda em uma determinada rodada
 chaveR = ""
 for j in range(circulacao[rodada], len(chave) + circulacao[rodada]): # basicamente aqui é uma lista circular
   if j >= len(chave):
     chaveR = chaveR + chave[j - len(chave)]
   else:
     chaveR = chaveR + chave[j]
 
 return chaveR


def permutacaoChaveB(chaveA, chaveB): #transformando os 56 bits das duas chaves em 48 bits
  
  tabelaB = [14, 17, 11, 24, 1, 5,
             3, 28, 15, 6, 21, 10,
             23, 19, 12, 4, 26, 8,
             16, 7, 27, 20, 13, 2,
             41, 52, 31, 37, 47, 55,
             30, 40, 51, 45, 33, 48,
             44, 49, 39, 56, 34, 53,
             46, 42, 50, 36, 29, 32 ] # tabela da permutação, aqui vai reduzir os bits de uma chave de 56 bits para 48
                                      # em cada rodada.
  chave = chaveA + chaveB  
  chaveSaida = ""
  for i in tabelaB:
    chaveSaida = chaveSaida + chave[i-1]
  
  return chaveSaida