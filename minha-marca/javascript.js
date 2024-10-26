function Mostrar(){
    var botao = document.getElementById("botao-projetos")
    var projetos = document.getElementById("art-projetos")
    var corpo = document.getElementById("corpo")
    if(projetos.style.display == "none"){
        projetos.style.display = "block"
         botao.innerText = "Ocultar"
         botao.style.color = "blue"
      
      
    }else{
        projetos.style.display = "none"
           botao.innerText = "Veja Mais"
        botao.style.color = "blueviolet"
     
      
    }
}

function mudarTema(){
    var fundo = document.getElementById ("containe-principal")
    botaoTema = document.getElementById ("botao-tema")
    var icone = document.getElementById("icone-tema")
    if (fundo.style.background === "white"){
        fundo.style.background = "black"
        corpo.style.background = "gray"
        botaoTema.style.background = "#4d0897"
        fundo.style.color = "darkgray"
          icone.src = "../imagens/brilho-do-sol.png"
      
    }else{
        fundo.style.background = "white"
        fundo.style.color = "black"
        corpo.style.background = "white"
          botaoTema.style.background = "#721ccd"
         icone.src = "../imagens/lua-crescente.png"
    }
}