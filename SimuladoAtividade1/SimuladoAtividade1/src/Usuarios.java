public class Usuarios{
       //Atributos
       private String nome;
       private String senha;
       private String email;

       public Usuarios(String nome, String senha, String email){
              this.nome = nome;
              this.senha = senha;
              this.email = email;
       }

       //Métodos
       public void visualizarUsuarios(){
              System.out.println("Dados do cliente: ");
              System.out.println("\tNome: " + nome);
              System.out.println("\tSenha: " + senha);
              System.out.println("\tE-mail: " + email);
       }

       //Pegar os atributos e setar
       public String getNome(){
              return nome;
       }
       public String getSenha(){
              return senha;
       }
       public String getEmail(){
              return email;
       }

       public void setNome(String nome){
              this.nome = nome;
       }
       public void setSenha(String senha){
              this.senha = senha;
       }
       public void setEmail(String email){
              this.email = email;
       }
}
