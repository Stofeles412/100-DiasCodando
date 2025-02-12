try:
    a = int(input("Numerador:"))
    b = int(input("denominador: "))
    r = a/b

except (ValueError, TypeError):
    print("Infelizmente tivemos o problema com tipo de daods q vc digitou : (")
except (ZeroDivisionError):
    print("Erro não é possiovel dividir um numero por 0")
except KeyboardInterrupt:
    print(" O usuario não informou os dados")
else:
    
    print(f"o resultado é = {r:.1f}")
finally:
    print("Volte sempre muito obrigado")