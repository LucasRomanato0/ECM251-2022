public class HeavyLifters extends Membro{

    public HeavyLifters(String nome, String email, String funcao, EnumHorarios horario) {
        super(nome, email, funcao, horario);
    }

    @Override
    public String mensagem(EnumHorarios horario) {
        if(horario == EnumHorarios.REGULAR){
            return "Podem contar conosco!";
        }
        else{
            return "N00b_qu3_n_Se_r3pita.bat";
        }
    }
}
