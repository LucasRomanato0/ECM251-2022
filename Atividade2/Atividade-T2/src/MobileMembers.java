public class MobileMembers extends Membro{

    public MobileMembers(String nome, String email, String funcao, EnumHorarios horario) {
        super(nome, email, funcao, horario);
    }

    @Override
    public String mensagem(EnumHorarios horario) {
        if(horario == EnumHorarios.REGULAR){
            return "Happy Coding!";
        }
        else{
            return "Happy_C0d1ng. Maskers";
        }
    }
}
