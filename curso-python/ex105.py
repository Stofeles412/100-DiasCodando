def notas(*n, sit=False):
    """> função para analisar notas e situações de varios alunos
    param n: uma ou mais notas dos alunos (aceita várias)
    param sit: valor opcional, indicado se deve ou não adicionar a situação
    : return: dicionario com varias informações sobre a situação da turma"""
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["média"] = sum(n)/len(n)
    if sit:
        if r["média"] >= 7:
            r["Situação"] = "boa"
        elif r["média"] >= 5:
            r["média"] = "razoavel"
        else:
            r["média"] = "ruim"
    return r


#programa principal
res = notas(5, 10, 5, 10, sit =True)
print(res)
help(notas)