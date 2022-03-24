public class Cliente {
       //Atributos
       private String nome;
       private String cpf;
       private String email;

       public Cliente(String nome, String cpf, String email){
              this.nome = nome;
              this.cpf = cpf;
              this.email = email;
       }

       //Métodos
       public void visualizarCliente(){
              System.out.println("Dados do Cliente: ");
              System.out.println("Nome: " + nome);
              System.out.println("CPF: " + cpf);
              System.out.println("E-mail: " + email);
       }

       public String getNome(){
              return nome;
       }
       public String getCpf(){
              return cpf;
       }
       public String getEmail(){
              return email;
       }

       public void setNome(String nome){
              this.nome = nome;
       }
       public void setEmail(String email){
              this.email = email;
       }
}
