from django.db import models

# Create your models here.

class Aluno(models.Model):
    ID = models.AutoField("ID", primary_key=True)
    Login = models.CharField("Login", max_length=50)
    Senha = models.CharField("Senha", max_length=50)
    Nome = models.CharField("Nome", max_length=100)
    Email = models.CharField("Email", max_length=100)
    Celular = models.CharField("Celular", max_length=20)
    DtExpiracao = models.DateField("DtExpiracao", max_length=10)
    RA = models.CharField("RA", max_length=7)
    Foto = models.CharField("Foto", null=True, blank=True, max_length=100)

    def __str__(self):
        return self.Login

class Professor(models.Model):
    ID = models.AutoField("ID", primary_key=True)
    Login = models.CharField("Login", max_length=50)
    Senha = models.CharField("Sena", max_length=50)
    Nome = models.CharField("Nome", max_length=100)
    Email = models.CharField("Emil", max_length=100)
    Celular = models.CharField("Celular", max_length=20)
    DtExpiracao = models.DateField("DtExpiracao", max_length=10)
    Apelido = models.CharField("Apelido", max_length=25)

    def __str__(self):
        return self.login

class Coordenador(models.Model):
    ID = models.AutoField("ID", primary_key=True)
    Login = models.CharField("Login", max_length=50)
    Senha = models.CharField("Senha", max_length=50)
    Nome = models.CharField("Nome", max_length=100)
    Email = models.CharField("Email", max_length=100)
    Celular = models.CharField("Celular", max_length=20)
    DtExpiracao = models.DateField("DataExpiracao", max_length=10)

    def __str__(self):
        return self.login

class Disciplina(models.Model):
	ID = models.AutoField("ID", primary_key=True)
	Nome = models.CharField("Nome", max_length=255)
	Data = models.DateField("Data")
	Status = models.CharField("Status", max_length=255)
	PlanoDeEnsino= models.CharField("PlanoDeEnsino", max_length=255)
	CargaHoraria = models.SmallIntegerField("Carga Horaria")
	Competencias = models.CharField("Competencias", max_length=255)
	Habilidades = models.CharField("Habilidades", max_length=255)
	Ementa = models.CharField("Ementa", max_length=255)
	ConteudoProgramatico = models.CharField("ConteudoProgramatico", max_length=255)
	BibliografiaBasica = models.CharField("BibliografiaBasica", max_length=255)
	BibliografiaComplementar = models.CharField("BibliografiaComplementar", max_length=255)
	PercentualPratico = models.SmallIntegerField("PercentualPratico")
	PercentualTeorico = models.SmallIntegerField("PercentualTeorico")
	IdCoordenador = models.ForeignKey('Coordenador', on_delete=models.CASCADE)

	def __str__(self):
		return self.Nome

class Curso(models.Model):
    ID = models.AutoField("ID", primary_key=True)
    Nome = models.CharField("Nome", max_length=100)
    def __str__(self):
        return self.nome

class DisciplinaOfertada(models.Model):
	ID = models.AutoField("ID", primary_key=True)
	IdCoordenador = models.ForeignKey('Coordenador', on_delete=models.CASCADE)
	DtInicioMatricula = models.DateField("Data Inicio Matricula", null=True)
	DtFimMatricula = models.DateField("Data Fim Matricula", null=True)
	IdDisciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
	IdCurso = models.ForeignKey('Curso', on_delete=models.CASCADE)
	Ano = models.SmallIntegerField("Ano")
	Semestre = models.SmallIntegerField("Semestre")
	Turma = models.CharField("Turma", max_length=255)
	IdProfessor = models.ForeignKey('Professor', on_delete=models.CASCADE, null=True)
	Metodologia = models.CharField("Metodologia", max_length=255, null=True)
	Recursos = models.CharField("Recursos", max_length=255, null=True)
	CriterioAvaliacao = models.CharField("Criterio de Avaliacao", max_length=255, null=True)
	PlanoDeAulas = models.CharField("Plano De Aulas", max_length=255, null=True)

	def __str__(self):
		return self.ID

class Mensagem(models.Model):
    ID = models.AutoField("ID", primary_key=True)
    assunto = models.CharField("Assunto", max_length=255)
    referencia = models.CharField("Referencia", max_length=255)
    conteudo = models.CharField("Conteudo", max_length=255)
    status = models.CharField("Status", max_length=50)
    dtEnvio = models.DateTimeField("Data Envio", max_length=10)
    dtResposta = models.DateField("Data Resposta", max_length=10)
    resposta  = models.CharField("Resposta", max_length=255)
    Aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    professor=models.ForeignKey('Professor', on_delete=models.CASCADE)

    def __str__(self):
        return self.assunto

class Atividade(models.Model):
    ID = models.AutoField("ID", primary_key=True)
    titulo= models.CharField("Titulo", max_length=255)
    decricao= models.CharField("Descricao", max_length=255)
    conteudo = models.CharField("Conteudo", max_length=255)
    tipo= models.CharField("Tipo", max_length=255)
    extras= models.CharField("Extras", max_length=255)
    Professor=models.ForeignKey('Professor', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class AtividadeVinculada(models.Model):
    ID = models.AutoField("ID", primary_key=True)
    IdAtividade= models.ForeignKey('Atividade',on_delete=models.CASCADE)
    IdProfessor= models.ForeignKey('Professor',on_delete=models.CASCADE)
    IdDisciplinaOfertada = models.ForeignKey('DisciplinaOfertada',on_delete=models.CASCADE)
    Rotulo= models.CharField("Rotulo", max_length=255)
    Status= models.CharField("Status", max_length=255)
    DtInicioRespostas= models.DateField("DtInicioRespostas", max_length=10)
    DtFimRespostas= models.DateField("DtFimRespostas", max_length=10)

    def __str__(self):
        return self.Atividade


class SolicitacaoMatricula(models.Model):
    ID = models.AutoField("ID", primary_key=True)
    IdAluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    IdDisciplinaOfertada = models.ForeignKey('DisciplinaOfertada',on_delete=models.CASCADE)
    DtSolicitacao = models.DateField('DtSolicitacao')
    IdCoordenador = models.ForeignKey('Coordenador',on_delete=models.CASCADE)
    Status = models.CharField('Status', max_length=255)

    def __str__(self):
        return self.IdAluno

class Entrega(models.Model):
    ID = models.AutoField("ID", primary_key=True)
    Titulo = models.CharField("Titulo", max_length=50)
    Resposta = models.CharField("Resposta", max_length=50)
    DtEntrega = models.DateField("Data Entrega", max_length=10)
    Status = models.CharField("Status", max_length=50)
    Nota = models.DecimalField("Nota",max_digits=5, decimal_places=2)
    DtAvaliacao = models.DateField("DtAvaliacao", max_length=10)
    Obs = models.CharField("Obs", max_length=50)
    IdProfessor = models.ForeignKey("Professor", on_delete=models.CASCADE)
    IdAluno = models.ForeignKey("Aluno", on_delete=models.CASCADE)
    IdAtividadeVinculada = models.ForeignKey("AtividadeVinculada", on_delete=models.CASCADE)

    def __str__(self):
        return self.Aluno
