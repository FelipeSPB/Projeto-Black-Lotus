document.getElementById("formulario").onsubmit=function(event){
    var login=document.getElementById("login");
    var nomeCampo=document.getElementById("nome");
    var email=document.getElementById("email");
    var celular=document.getElementById("celular");
    var nascimento=document.getElementById("nascimento");
    var cpf = document.getElementById("cpf");
    var senha=document.getElementById("senha");
    var confSenha=document.getElementById("confSenha");

    if (nomeCampo.value=="" || login.value=="" || email.value=="" || celular.value=="" || nascimento.value =="" || cpf.value=="" || senha.value==""){
        alert("Campo obrigatório não preenchido");
        return false;
    }
    /* Trabalhando Do nascimento*/
    hoje = new Date();
    ano = hoje.getYear();
    if (nascimento.value-ano<=17){
    alert("Você é menor de 17 anos");
    return false;
    }

    /*Validação da senha */
    if(senha.value==confSenha.value){
        alert("Você logou com sucesso");
        return true;
    }
    if(senha.value!=confSenha.value){
        alert("Você digitou senhas diferentes");
        return false;
    }


        var numeros, digitos, soma, i, resultado, digitos_iguais;
        digitos_iguais = 1;
        if (cpf.length < 11)
            return false;
        for (i = 0; i < cpf.length - 1; i++)
            if (cpf.charAt(i) != cpf.charAt(i + 1))
                    {
                    digitos_iguais = 0;
                    break;
                    }
        if (!digitos_iguais)
            {
            numeros = cpf.substring(0,9);
            digitos = cpf.substring(9);
            soma = 0;
            for (i = 10; i > 1; i--)
                    soma += numeros.charAt(10 - i) * i;
            resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
            if (resultado != digitos.charAt(0))
                    return false;
            numeros = cpf.substring(0,10);
            soma = 0;
            for (i = 11; i > 1; i--)
                    soma += numeros.charAt(11 - i) * i;
            resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
            if (resultado != digitos.charAt(1))
                    return false;
            return true;
            }
        else
            return false;

}
