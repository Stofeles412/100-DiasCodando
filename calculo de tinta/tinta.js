function openMenu(){
    var abrir = document.getElementById("nav-itens")
    var icone = document.getElementById("nav-img")
    if(abrir.style.display == "none"){
        abrir.style.display = "block"
    }else{
        abrir.style.display = "none"
    }
}

function calcular(){
    var n1 = int(document.getElementById("altura"))
    var n2 = int( document.getElementById("largura"))
    res = document.getElementById("resultado")
    var soma = n1 * n2
    res.write (`a soma é = a ${soma}`)
}