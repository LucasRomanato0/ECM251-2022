public class App {
    public static void main(String[] args) throws Exception {
        Cliente c1 = new Cliente("Lucas",
            "229.214.258-90",
            "20.00313-7@maua.br",
            new Conta(1234)
        );

        System.out.println("\nNome do cliente: " + c1.getNome());
        System.out.println("\nCPF do cliente: " + c1.getCpf());
        System.out.println("\nE-mail do cliente: " + c1.getEmail());

        c1.getConta().visualizarSaldo();
    }
}
