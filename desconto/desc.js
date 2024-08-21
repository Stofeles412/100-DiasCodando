function desconto(){


    var valor = parseFloat(document.getElementById("valor").value, 10);



des5 = valor * 5/100
des10 = valor * 10/100
des20 = valor * 20/100
valorFinal5 = valor - des5
valorFinal10 = valor - des10
valorFinal20 = valor - des20


res = document.getElementById("res").textContent = ` o produto que antes custava ${valor} com 5% ${des5}  - R$ Reais de desconto o produto ficará por ${valorFinal5} R$`

res2 = document.getElementById("res2").textContent = ` o produto que antes custava ${valor} com 10%  ${des10}R$ Reais de desconto o produto ficará por ${valorFinal10} R$`


res3 = document.getElementById("res3").textContent = ` o produto que antes custava ${valor} com 20% - R$ Reais ${des20} de desconto o produto ficará por ${valorFinal20} R$`




}