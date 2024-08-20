function openMenu(){
    var abrir = document.getElementById("nav-itens")
    var icone = document.getElementById("nav-img")
    if(abrir.style.display == "none"){
        abrir.style.display = "block"
        icone.src = '../imagens/menu-fechado.png'
    }else{
        abrir.style.display = "none"
         icone.src = '../imagens/menu.png'
          
    }
}


function calcular() {
    // Obtém e converte os valores
    var altura = parseInt(document.getElementById("altura").value, 10);
    var largura = parseInt(document.getElementById("largura").value, 10);
    var tinta = (parseFloat( area/2).value, 10)

    // Verifica se os valores são números válidos
    if (isNaN(altura) || isNaN(largura)) {
        document.getElementById("resultado").textContent = "Por favor, insira valores válidos.";
        return;
    }

   

    // Calcula a área
    var area = altura * largura;
    var tinta = area/2
    document.getElementById("resultado").textContent = `A Sua Área é de:  ${area}m².`

    var res = document.getElementById("res").textContent = `você prescisaria de ${tinta}L de tinta para pintar sua parede, considerando 1L de tinta para cada 2m²;`

   
}


