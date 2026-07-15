const formCadastro = document.getElementById("formCadastro");
const inputNome = document.getElementById("nome");
const inputEmail = document.getElementById("email");
const inputPassword = document.getElementById("password");

formCadastro.addEventListener("submit", async (event) => {
    event.preventDefault();

    // Monta o objeto idêntico ao UsuarioSchema do back-end
    const dadosCadastro = {
        nome: inputNome.value,
        email: inputEmail.value,
        senha: inputPassword.value
    };

                                        //pegando o rota do main em python
    try {                              
        const resposta = await fetch(" https://login-iqyw.onrender.com/criar_conta", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dadosCadastro)
        });

        const resultado = await resposta.json();

        if (resultado.erro) {
            alert(`Erro: ${resultado.erro}`);
        } else {
            alert("Conta criada com sucesso!");
            // Após cadastrar, manda o usuário de volta para a tela de login
            window.location.href = "/index.html";
        }

    } catch (erro) {
        console.error("Erro ao conectar:", erro);
        alert("Não foi possível conectar ao servidor.");
    }
});