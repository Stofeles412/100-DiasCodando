function Mostrar(){
    var botao = document.getElementById("botao-projetos")
    var projetos = document.getElementById("art-projetos")
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
    if (fundo.style.background == "white"){
        fundo.style.background = "black"
        fundo.style.color = "darkgray"
        botaoTema.innerText = "claro"
    }else{
        fundo.style.background = "white"
        fundo.style.color = "black"
        botaoTema.innerText = "escuro"
    }
}