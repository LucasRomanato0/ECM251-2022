public class App {
    public static void main(String[] args) throws Exception {
        Usuarios u1 = new Usuarios("Lucas", "sakhj", "20.00313-7@maua.br");
        Usuarios u2 = new Usuarios("Ronaldo", "jjj", "0313-7@maua.br");
        Usuarios u3 = new Usuarios("Pedro", "aaa", "aaa-7@maua.br");
        Conta c1 = new Conta(u1);
        Conta c2 = new Conta(u2);
        Conta c3 = new Conta(u3);

        System.out.println(c1.visualizarConta());
        System.out.println(c2.visualizarConta());
        System.out.println(c3.visualizarConta());
    }
}
