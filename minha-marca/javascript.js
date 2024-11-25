function Mostrar(){
    var botao = document.getElementById("botao-projetos")
    var projetos = document.getElementById("art-projetos")
    var corpo = document.getElementById("corpo")
    if(projetos.classList.contains("show")){
        projetos.classList.remove ("show")
         botao.innerText = "Ocultar"
         botao.style.color = "blue"
      
      
    }else{
        projetos.classList.add("show")
           botao.innerText = "Veja Mais"
        botao.style.color = "blueviolet"
     
      
    }
}

function mudarTema() {
    const corpo = document.getElementById("corpo");
    const fundo = document.getElementById("containe-principal");
    const botaoTema = document.getElementById("botao-tema");
    const icone = document.getElementById("icone-tema");

    if (corpo.classList.contains("tema-claro")) {
        // Alterar para tema escuro
        corpo.classList.remove("tema-claro");
        corpo.classList.add("tema-escuro");

        fundo.classList.add("fundo-escuro");
        fundo.classList.remove("fundo-claro");

        botaoTema.style.background = "#4d0897";
        icone.src = "../imagens/brilho-do-sol.png";
    } else {
        // Alterar para tema claro
        corpo.classList.remove("tema-escuro");
        corpo.classList.add("tema-claro");

        fundo.classList.add("fundo-claro");
        fundo.classList.remove("fundo-escuro");

        botaoTema.style.background = "#721ccd";
        icone.src = "../imagens/lua-crescente.png";
    }
}
