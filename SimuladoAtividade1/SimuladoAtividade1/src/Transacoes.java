public class Transacoes{
       //Métodos
       public boolean transferirDinheiro(double valor, Conta inicial, Conta destino){
              if(!inicial.sacar(valor)) return false;
              if(!destino.depositar(valor)) return false;
              return true;
       }

       //public String QRCode(Conta inicial, Usuarios conta, Conta valor){
              //System.out.println(String.format("%;%;%.2f", inicial.idConta));
       //}
}
