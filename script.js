const slides = document.querySelector(".slide");
const imagem = document.querySelectorAll(".slide img");
const botEsquerdo = document.querySelector(".esquerdo");
const botDireito = document.querySelector(".direito");

let imagens = 0;
const tamanho = imagem.length - 1;

botEsquerdo.addEventListener("click" , () => {
    imagens--
    if (imagens < 0) imagens = tamanho;
    atualizarCarrossel();
})


botDireito.addEventListener("click", () => {
    incrementarImagem();
    atualizarCarrossel();
})

const incrementarImagem = () =>{
    imagens++
    if (imagens > tamanho ) imagens = 0;
}


const atualizarCarrossel = () => {
    slides.style.transform = `translateX(-${imagens * 100}%)`;

}

setInterval(()=>{
    incrementarImagem();
    atualizarCarrossel();
}, 3000);

const formLogin = document.getElementById("formlogin");
const email = document.getElementById("email");
const password = document.getElementById("password");

formLogin.addEventListener("submit", async (event) => {
    event.preventDefault();

    const tabelaDados = {
        email: email.value,
        senha: password.value
    };

    try {                              
        const resposta = await fetch(" http://127.0.0.1:8000/conta", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(tabelaDados)
        });

        const resultado = await resposta.json();

        if (resultado.erro) {
            alert("Senha ou E-mail inválido");
        } else {
            alert("Entrou com sucesso!");
        }

    } catch (erro) {
        console.error("Erro ao conectar:", erro);
        alert("Não foi possível conectar ao servidor.");
    }
       
}); 

