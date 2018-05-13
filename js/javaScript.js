document.getElementById("tabela").onsubmit=function(event){
  var alunos = document.getElementsByName("avaliacao");
  var aprovados = 0;
  var reprovados = 0;
  for(var i = 0; i < alunos.length; i++){
    if(alunos[i].type == 'radio' && alunos[i].value == 'aprovado' && alunos[i].checked){
      aprovados++;
    }
    else if(alunos[i].type == 'radio' && alunos[i].value == 'reprovado' && alunos[i].checked){
      reprovados++;
    }
  }
  var x = confirm(aprovados + " alunos aprovados \n" + reprovados + " alunos reprovados\nConfirmar envio?");
  if(x==true){
    if(aprovados <= 60 && aprovados >= 20){
      alert("Aprovados: " + aprovados +"\n Cancelados: " + reprovados);
      return true;
    }else if(aprovados >= 60 || aprovados <= 20){
      alert("Número de aprovados inválido: \nMínimo de aprovados: 20 \nMáximo de aprovados: 60");
      return false;
    }
  }
}
