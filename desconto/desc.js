function desconto(){


    var valor = parseFloat(document.getElementById("valor").value);
    var desconto = parseFloat(document.getElementById("des").value)
if(isNaN(valor) || isNaN(desconto)){
    erro = document.getElementById("erro").textContent = `insira valores validos !`
}
    
  
    var desc2 = desconto.toFixed(2)

    var vDes = (valor * desconto) / 100;
    var vFinal = valor - vDes;



    res = document.getElementById("res").innerText = `O produto que custava ${valor.toFixed(2)}R$ com  ${vDes.toFixed(1)}% de desconto, fica por ${vFinal.toFixed(2)}R$`




 






}