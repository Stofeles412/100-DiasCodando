function desconto(){


    var valor = parseFloat(document.getElementById("valor").value);
    var desconto = parseFloat(document.getElementById("des").value)



/*des5 = valor * 5/100
des10 = valor * 10/100
des20 = valor * 20/100
valorFinal5 = valor - des5
valorFinal10 = valor - des10
valorFinal20 = valor - des20*/

vDes = (valor * desconto) / 100;
var vFinal = valor - desconto;



res = document.getElementById("res").textContent = `O produto que custava ${valor}R$ com  %${vDes} de desconto, fica por ${vFinal}R$`

/*res2 = document.getElementById("res2").textContent = ` o produto que antes custava ${valor} com 10%  ${des10}R$ Reais de desconto o produto ficará por ${valorFinal10} R$`*/


/*res3 = document.getElementById("res3").textContent = ` o produto que antes custava ${valor} com 20% - R$ Reais ${des20} de desconto o produto ficará por ${valorFinal20} R$`*/




}