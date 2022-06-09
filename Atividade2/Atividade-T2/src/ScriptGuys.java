public class ScriptGuys extends Membro{

    public ScriptGuys(String nome, String email, String funcao, EnumHorarios horario) {
        super(nome, email, funcao, horario);
    }

    @Override
    public String mensagem(EnumHorarios horario) {
        if(horario == EnumHorarios.REGULAR){
            return "Prazer em ajudar novos amigos de código!";
        }
        else{
            return "QU3Ro_S3us_r3curs0s.py";
        }
    }
}
