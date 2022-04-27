from util.Encriptar import *

def inicio():
    checkTexto = False
    checkChave = False
    texto = ""
    chave = ""

    while True:
     if checkTexto == False:
       texto = input("Digite o texto a ser criptografado(8 caracteres): ")
       if len(texto) != TAM_TEXTO:
         continue
       else:
         checkTexto = True
     if checkChave == False:
       chave = input("Digite uma chave(8 caracteres): ")
       if len(chave) != TAM_TEXTO:
         print("Tamanho de chave invalido por favor digite outra vez.")
         continue
       else:
         checkChave = True
         break
    

    textoHex = texto.encode(FORMATO).hex()
    chaveHex = chave.encode(FORMATO).hex()
    textoBin = hexToBin(textoHex)
    chaveBin = hexToBin(chaveHex)

    print(SEPARADOR,end="\n\n")
    print("Chave ultilizada pra criptografar: " + chave)
    print(27*".", ": ", chaveHex ,end="")
    
    print()
    print("Texto a ser criptografado: " + texto)
    print(18*".", ": ", chaveHex , end=" ")
    

    textoCriptografado = encriptar(textoBin, chaveBin)
    
    print(SEPARADOR,end="\n\n")
    textoCripHex = binToHex(textoCriptografado)
    
    try:

     print("Texto criptografado: {}".format(codecs.decode(textoCripHex,"hex")))
    except UnicodeDecodeError as err: 
      print("Deu problema ao decodar o texto", err)
    print(13*"."+ "Em hex: " + textoCripHex)
    
    
    print(SEPARADOR)

    opcao = input("Quer descifrar? (S/N)")  

    if opcao.upper() == "S":
      while True:
       chaveDeRetirada = input("Digite a chave: ")
       if len(chave) != TAM_TEXTO:
         print("Tamanho de chave invalido por favor digite outra vez.")
       else:
         break
      chaveDeRetirada = chaveDeRetirada.encode("utf-8").hex()
      binChaveRet = hexToBin(chaveDeRetirada)
      
      textoDescriptado = descriptar(textoCriptografado, binChaveRet)

      tdEmHex = binToHex(textoDescriptado)
      textoPleno = codecs.decode(tdEmHex, "hex")
      textoPleno = str(textoPleno,"utf-8","ignore")
      if texto != textoPleno:
        print("Chave Errada!")
      else:
        print("O texto decifrado é: ", textoPleno)
      
    else:
      return textoCriptografado   # retornar o texto criptografado em Hexadecimal
    
    
inicio()