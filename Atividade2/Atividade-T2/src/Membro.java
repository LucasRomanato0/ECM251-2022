public abstract class Membro implements PostarMensagem{
    private final String nome;
    private final String email;
    private final String funcao;
    private final EnumHorarios horario;
    
    public Membro(String nome, String email, String funcao, EnumHorarios horario) {
        this.nome = nome;
        this.email = email;
        this.funcao = funcao;
        this.horario = horario;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public String getFuncao() {
        return funcao;
    }

    public EnumHorarios getHorario() {
        return horario;
    }

    @Override
    public String toString() {
        return "Membro [email=" + email + ", funcao=" + funcao + ", horario=" + horario + ", nome=" + nome + "]\n" + mensagem(horario);
    }
}