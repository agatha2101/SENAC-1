// AULA 01 — DESENVOLVIMENTO DE SOFTWARE APOIADO POR IA
// Este arquivo começa incompleto de propósito.
// A dupla vai usar IA para completar cada TODO de forma controlada.

const form = document.querySelector("#formChamado");
const titulo = document.querySelector("#titulo");
const categoria = document.querySelector("#categoria");
const prioridade = document.querySelector("#prioridade");
const descricao = document.querySelector("#descricao");
const mensagemErro = document.querySelector("#mensagemErro");

const listaChamados = document.querySelector("#listaChamados");
const filtroStatus = document.querySelector("#filtroStatus");
const totalChamados = document.querySelector("#totalChamados");
const totalAbertos = document.querySelector("#totalAbertos");

// Começamos com uma lista vazia.
// TODO 5: depois esta lista deverá ser carregada do localStorage.
let chamados = JSON.parse(localStorage.getItem("chamados")) || [];

// TODO 1
function criarChamado() {
    return {
        id: Date.now(),
        titulo: titulo.value,
        categoria: categoria.value,
        prioridade: prioridade.value,
        descricao: descricao.value,
        status: "Aberto"
    };
}

// TODO 2
function renderizarChamados() {
    const filtro = filtroStatus.value;

    const chamadosFiltrados = filtro === "Todos"
        ? chamados
        : chamados.filter(chamado => chamado.status === filtro);[]
        
    totalChamados.textContent = chamados.length;
    totalAbertos.textContent = chamados.filter(chamado => chamado.status === "Aberto").length;
    
    if (chamadosFiltrados.length === 0) {
        listaChamados.innerHTML = "<p>Nenhum chamado cadastrado.</p>";
        return;
    }

    listaChamados.innerHTML = chamadosFiltrados.map(chamado => `
        <div class="card">
            <h3>${chamado.titulo}</h3>
            <p><strong>Categoria:</strong> ${chamado.categoria}</p>
            <p><strong>Prioridade:</strong> ${chamado.prioridade}</p>
            <p><strong>Descrição:</strong> ${chamado.descricao}</p>
            <p><strong>Status:</strong> ${chamado.status}</p>
            <button onclick="avancarStatus(${chamado.id})">Avançar status</button>
            <button onclick="editarChamado(${chamado.id})">Editar</button>
        </div>
    `).join("");
}

// TODO 3
function avancarStatus(id) {
    const chamado = chamados.find(chamado => chamado.id === id);

    if (chamado.status === "Aberto") {
        chamado.status = "Em andamento";
    } else if (chamado.status === "Em andamento") {
        chamado.status = "Concluído";
    } else if (chamado.status === "Concluído") {
        chamado.status = "Concluído";
    }

    salvarChamados();
    renderizarChamados();
}

function editarChamado(id) {
    const chamado = chamados.find(chamado => chamado.id === id);

    if (!chamado) return;

    const novoTitulo = prompt("Digite o novo título:", chamado.titulo);
    const novaDescricao = prompt("Digite a nova descrição:", chamado.descricao);

    if (novoTitulo === null || novaDescricao === null) {
        return;
    }

    if (novoTitulo.trim() === "" || novaDescricao.trim() === "") {
        alert("Título e descrição não podem ficar vazios.");
        return;
    }

    chamado.titulo = novoTitulo.trim();
    chamado.descricao = novaDescricao.trim();

    salvarChamados();
    renderizarChamados();
}

// TODO 4
form.addEventListener("submit", function (event) {
    event.preventDefault();

    if (titulo.value.trim() === "" || descricao.value.trim() === "") {
        mensagemErro.textContent = "Preencha título e descrição.";
        return;
    }

    mensagemErro.textContent = "";

    const chamado = criarChamado();
    chamados.push(chamado);
    salvarChamados();

    form.reset();
    renderizarChamados();

});

// TODO 5
function salvarChamados() {
    localStorage.setItem("chamados", JSON.stringify(chamados));
}


// O filtro deve redesenhar a lista quando mudar.
filtroStatus.addEventListener("change", () => {
  renderizarChamados();
});

renderizarChamados();

 
// TODO FINAL
// Atualize os indicadores:
// totalChamados = quantidade total;
// totalAbertos = quantidade de chamados com status "Aberto".
