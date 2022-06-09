public class BigBrothers extends Membro{

    public BigBrothers(String nome, String email, String funcao, EnumHorarios horario) {
        super(nome, email, funcao, horario);
    }

    @Override
    public String mensagem(EnumHorarios horario) {
        if(horario == EnumHorarios.REGULAR){
            return "“Sempre ajudando as pessoas membros ou não S2!";
        }
        else{
            return "...";
        }
    }
}
