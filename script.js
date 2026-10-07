const imagens = document.querySelectorAll("#graficos img");

const modal = document.createElement("div");
modal.classList.add("modal");

const imagemAmpliada = document.createElement("img");

const botaoFechar = document.createElement("button");
botaoFechar.textContent = "×";
botaoFechar.setAttribute("aria-label", "Fechar imagem");

modal.appendChild(botaoFechar);
modal.appendChild(imagemAmpliada);

document.body.appendChild(modal);

imagens.forEach((imagem) => {
    imagem.addEventListener("click", () => {
        imagemAmpliada.src = imagem.src;
        imagemAmpliada.alt = imagem.alt;
        modal.classList.add("ativo");
    });
});

botaoFechar.addEventListener("click", () => {
    modal.classList.remove("ativo");
});

modal.addEventListener("click", (evento) => {
    if (evento.target === modal) {
        modal.classList.remove("ativo");
    }
});

document.addEventListener("keydown", (evento) => {
    if (evento.key === "Escape") {
        modal.classList.remove("ativo");
    }
});

console.log("JavaScript carregado!");

const indicadores = document.querySelectorAll(".indicador");

indicadores.forEach((indicador, indice) => {

    indicador.addEventListener("click", () => {

        let mensagem;

        if (indice === 0) {
            mensagem =
                "A taxa de vitória foi de 54,5% nas 22 partidas analisadas.";
        }

        if (indice === 1) {
            mensagem =
                "Henrique conquistou 12 vitórias nas 22 partidas analisadas.";
        }

        if (indice === 2) {
            mensagem =
                "Nas vitórias, a média foi de 120,25 passes certos.";
        }

        let mensagemExistente =
            indicador.querySelector(".mensagem");

        if (mensagemExistente) {
            mensagemExistente.remove();
            return;
        }

        const texto = document.createElement("p");

        texto.classList.add("mensagem");
        texto.textContent = mensagem;

        indicador.appendChild(texto);

    });

});

const indicadoresChave = document.querySelectorAll(".indicador-chave");

const detalheIndicador = document.querySelector("#detalhe-indicador");

const dadosIndicadores = {
    passes:
        "8 partidas atingiram 120 ou mais passes certos. Todas terminaram em vitória.",

    finalizacoes:
        "7 partidas tiveram 8 ou mais finalizações. Foram 6 vitórias e 1 empate.",

    posse:
        "11 partidas tiveram 50% ou mais de posse de bola. Foram 9 vitórias e 2 empates."
};

indicadoresChave.forEach((indicador) => {

    indicador.addEventListener("click", () => {

        const tipo = indicador.dataset.indicador;

        detalheIndicador.textContent = dadosIndicadores[tipo];

    });

});

function atualizarGrafico(partidasFiltradas) {
    const vitorias = partidasFiltradas.filter(
        (partida) => partida.resultado === "vitoria"
    ).length;

    const empates = partidasFiltradas.filter(
        (partida) => partida.resultado === "empate"
    ).length;

    const derrotas = partidasFiltradas.filter(
        (partida) => partida.resultado === "derrota"
    ).length;

    const total = partidasFiltradas.length;

    document.querySelector("#valor-vitorias").textContent = vitorias;
    document.querySelector("#valor-empates").textContent = empates;
    document.querySelector("#valor-derrotas").textContent = derrotas;

    if (total > 0) {
        document.querySelector("#barra-vitorias").style.width =
            `${(vitorias / total) * 100}%`;

        document.querySelector("#barra-empates").style.width =
            `${(empates / total) * 100}%`;

        document.querySelector("#barra-derrotas").style.width =
            `${(derrotas / total) * 100}%`;
    }
}

const botoesFiltroResultados = document.querySelectorAll(".filtros-resultados button");

const filtroSelecionado = document.querySelector("#filtro-selecionado");
const listaPartidas = document.querySelector("#lista-partidas");

const partidas = [
    { partida: 1, golsMarcados: 1, golsSofridos: 3, finalizacoes: 6, posse: 40, passes: 134, passesCertos: 99, desarmes: 9 },
    { partida: 2, golsMarcados: 4, golsSofridos: 3, finalizacoes: 7, posse: 30, passes: 94, passesCertos: 86, desarmes: 4 },
    { partida: 3, golsMarcados: 2, golsSofridos: 6, finalizacoes: 4, posse: 44, passes: 112, passesCertos: 90, desarmes: 6 },
    { partida: 4, golsMarcados: 1, golsSofridos: 2, finalizacoes: 4, posse: 47, passes: 117, passesCertos: 74, desarmes: 2 },
    { partida: 5, golsMarcados: 0, golsSofridos: 4, finalizacoes: 5, posse: 45, passes: 128, passesCertos: 90, desarmes: 6 },
    { partida: 6, golsMarcados: 2, golsSofridos: 1, finalizacoes: 3, posse: 53, passes: 161, passesCertos: 139, desarmes: 4 },
    { partida: 7, golsMarcados: 4, golsSofridos: 3, finalizacoes: 12, posse: 57, passes: 169, passesCertos: 139, desarmes: 7 },
    { partida: 8, golsMarcados: 3, golsSofridos: 2, finalizacoes: 14, posse: 54, passes: 185, passesCertos: 157, desarmes: 4 },
    { partida: 9, golsMarcados: 4, golsSofridos: 3, finalizacoes: 8, posse: 36, passes: 94, passesCertos: 66, desarmes: 7 },
    { partida: 10, golsMarcados: 4, golsSofridos: 1, finalizacoes: 4, posse: 50, passes: 156, passesCertos: 124, desarmes: 6 },
    { partida: 11, golsMarcados: 2, golsSofridos: 2, finalizacoes: 7, posse: 52, passes: 141, passesCertos: 105, desarmes: 6 },
    { partida: 12, golsMarcados: 4, golsSofridos: 3, finalizacoes: 14, posse: 57, passes: 169, passesCertos: 139, desarmes: 9 },
    { partida: 13, golsMarcados: 2, golsSofridos: 1, finalizacoes: 6, posse: 55, passes: 161, passesCertos: 130, desarmes: 3 },
    { partida: 14, golsMarcados: 3, golsSofridos: 3, finalizacoes: 11, posse: 51, passes: 144, passesCertos: 108, desarmes: 7 },
    { partida: 15, golsMarcados: 5, golsSofridos: 3, finalizacoes: 8, posse: 59, passes: 170, passesCertos: 140, desarmes: 5 },
    { partida: 16, golsMarcados: 1, golsSofridos: 3, finalizacoes: 6, posse: 40, passes: 134, passesCertos: 99, desarmes: 9 },
    { partida: 17, golsMarcados: 4, golsSofridos: 3, finalizacoes: 7, posse: 30, passes: 94, passesCertos: 86, desarmes: 4 },
    { partida: 18, golsMarcados: 2, golsSofridos: 6, finalizacoes: 4, posse: 44, passes: 112, passesCertos: 90, desarmes: 6 },
    { partida: 19, golsMarcados: 1, golsSofridos: 2, finalizacoes: 4, posse: 47, passes: 117, passesCertos: 74, desarmes: 2 },
    { partida: 20, golsMarcados: 0, golsSofridos: 4, finalizacoes: 5, posse: 45, passes: 128, passesCertos: 90, desarmes: 6 },
    { partida: 21, golsMarcados: 2, golsSofridos: 1, finalizacoes: 3, posse: 53, passes: 161, passesCertos: 139, desarmes: 4 },
    { partida: 22, golsMarcados: 4, golsSofridos: 3, finalizacoes: 19, posse: 54, passes: 125, passesCertos: 98, desarmes: 7 }
];

// Classifica cada partida
partidas.forEach((partida) => {
    if (partida.golsMarcados > partida.golsSofridos) {
        partida.resultado = "vitoria";
    } else if (partida.golsMarcados === partida.golsSofridos) {
        partida.resultado = "empate";
    } else {
        partida.resultado = "derrota";
    }
});

// Calcula os resultados gerais
const totalVitorias = partidas.filter(
    (partida) => partida.resultado === "vitoria"
).length;

const totalEmpates = partidas.filter(
    (partida) => partida.resultado === "empate"
).length;

const totalDerrotas = partidas.filter(
    (partida) => partida.resultado === "derrota"
).length;

// Mostra os números iniciais
document.querySelector("#valor-vitorias").textContent = totalVitorias;
document.querySelector("#valor-empates").textContent = totalEmpates;
document.querySelector("#valor-derrotas").textContent = totalDerrotas;

// Preenche as barras iniciais
const totalPartidas = partidas.length;

document.querySelector("#barra-vitorias").style.width =
    `${(totalVitorias / totalPartidas) * 100}%`;

document.querySelector("#barra-empates").style.width =
    `${(totalEmpates / totalPartidas) * 100}%`;

document.querySelector("#barra-derrotas").style.width =
    `${(totalDerrotas / totalPartidas) * 100}%`;

// Filtros
botoesFiltroResultados.forEach((botao) => {
    botao.addEventListener("click", () => {

        botoesFiltroResultados.forEach((botaoAtual) => {
            botaoAtual.classList.remove("ativo");
        });

        botao.classList.add("ativo");

        const filtro = botao.dataset.filtro;

        const partidasFiltradas =
            filtro === "todos"
                ? partidas
                : partidas.filter(
                    (partida) => partida.resultado === filtro
                );

        atualizarGrafico(partidasFiltradas);

        filtroSelecionado.textContent =
            `Mostrando ${partidasFiltradas.length} partidas.`;

        listaPartidas.innerHTML = "";

        partidasFiltradas.forEach((partida) => {
            const card = document.createElement("div");

            card.classList.add("partida-filtro");

            card.innerHTML = `
                <strong>Partida ${partida.partida}</strong>
                <span>⚽ ${partida.golsMarcados} × ${partida.golsSofridos}</span>
                <span>🎯 ${partida.finalizacoes} finalizações</span>
                <span>📊 ${partida.posse}% posse</span>
                <span>🔄 ${partida.passesCertos} passes certos</span>
            `;

            listaPartidas.appendChild(card);
        });
    });
});