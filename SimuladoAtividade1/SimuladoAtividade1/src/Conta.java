public class Conta {
       //Atributos da nossa classe
       private double idConta;
       private double saldo;
       Usuarios usuarios;

       //Construtor
       public Conta(Usuarios usuarios){
              idConta = Math.random();
              this.usuarios = usuarios;
              saldo = 0;
       }

       //Métodos da classe
       public String visualizarConta(){
              usuarios.visualizarUsuarios();
              System.out.println("Dados da conta: ");
              System.out.println("\tID: " + idConta);
              return String.format("\tR$%.2f", saldo);
       }
       public boolean depositar(double valor){
              if(valor < 0)
                     return false;
              this.saldo += valor;
              return true;
       }
       public boolean sacar(double valor){
              if(valor > saldo) return false;
              if(valor < 0) return false;
              this.saldo -= valor;
              return true;
       }
}
