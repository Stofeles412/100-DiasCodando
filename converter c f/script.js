// script.js

document.addEventListener('DOMContentLoaded', () => {
    const tilesContainer = document.getElementById('tilesContainer');
    const addTileButton = document.getElementById('addTileButton');

    // Função para criar um tile
    function createTile(url, image, description) {
        const tile = document.createElement('div');
        tile.classList.add('tile');
        
        tile.innerHTML = `
            <a href="${url}" target="_blank">
                <img src="${image}" alt="${description}">
                <p>${description}</p>
            </a>
        `;
        
        return tile;
    }

    // Função para carregar tiles do backend (simulado)
    function loadTiles() {
        // Simulação de chamada a um backend
        const tilesData = [
            { url: 'https://somoskudasai.com/wp-content/uploads/2021/09/kimetsu.jpg', image: 'imagem1.jpg', description: 'Site Exemplo 1' },
            { url: 'https://www.outroexemplo.com', image: 'imagem2.jpg', description: 'Outro Exemplo' }
        ];

        // Adiciona os tiles ao contêiner
        tilesData.forEach(tileData => {
            const tile = createTile(tileData.url, tileData.image, tileData.description);
            tilesContainer.appendChild(tile);
        });
    }

    // Adicionar um novo tile ao clicar no botão
    addTileButton.addEventListener('click', () => {
        const url = prompt('Digite o URL do site:');
        const image = prompt('Digite o URL da imagem:');
        const description = prompt('Digite a descrição do site:');
        
        if (url && image && description) {
            const newTile = createTile(url, image, description);
            tilesContainer.appendChild(newTile);
        } else {
            alert('Por favor, preencha todos os campos.');
        }
    });

    // Carregar tiles ao iniciar
    loadTiles();
});
