import java.util.ArrayList;
import java.util.List;

public class Sistema{
    
    public static void executar(){
        List<Membro> membros = new ArrayList<Membro>();
        EnumHorarios turno = EnumHorarios.REGULAR;

        membros.add(new MobileMembers("Lucas", "hacker.mm@gmail.com", "Mobile Members", turno));
        membros.add(new HeavyLifters("Rafael", "hacker.hf@gmail.com", "Heavy Lifters", turno));
        membros.add(new ScriptGuys("Thiago", "hacker.sg@gmail.com", "Script Guys", turno));
        membros.add(new BigBrothers("Caio", "hacker.bb@gmail.com", "Big Brothers", turno));

        mostraMembros(membros, turno);
        System.out.println("\n-----MUDANÇA DE TURNO-----\n");
        turno = EnumHorarios.EXTRA;

        membros.add(new MobileMembers("Lucas", "hacker.mm@gmail.com", "Mobile Members", turno));
        membros.add(new HeavyLifters("Rafael", "hacker.hf@gmail.com", "Heavy Lifters", turno));
        membros.add(new ScriptGuys("Thiago", "hacker.sg@gmail.com", "Script Guys", turno));
        membros.add(new BigBrothers("Caio", "hacker.bb@gmail.com", "Big Brothers", turno));

        mostraMembros(membros, turno);
    }

    public static void mostraMembros(List<Membro> membros, EnumHorarios turno){
        for (Membro membro : membros) {
            System.out.println(membro);
        }
    }
}