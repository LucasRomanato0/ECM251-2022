public class Sistema {
    
    public static void executar(){
        Carro c1 = new Carro(1234, "Patinete");
        Usuario u1 = new Usuario("Lucas");

        c1.testar();
        u1.toString();
    }
}
