from time import sleep
def maior(* num):
    cont = maior = 0
    print("-=" *30)
    print("Analisando os valores passados....")
    for valor in num:
        print(f" {valor} ", end="", flush=True)
        sleep (0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
        print(f"Foram informados {cont} valores ao todo")
        print(f"E o maior valor informado foi o {maior}")
      
    
  
        
    
    
#programa principal
maior(2,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()