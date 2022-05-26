# ECM251-2022
Repositório da disciplina de ECM251

# ECM251 - Utilizando Git

Em primeiro lugar, configurar quem é o usuário (***nome***) e qual seu ***e-mail***.

```bash
git config --global user.name "nomeusuario"
git config --global user.email email@email.com
```

Ordem para criar um repositório:
- Inicializar o repositório:
```bash
git init
```

- Adicionar os arquivos com:
```bash
git add .
```

- Commitar (salvar) os arquivos:
```bash
git commit -m "mensagem"
```

- Subir os arquivos:
```bash
git push
```

- Verificar status
```bash
git status
```

- Commitar já existente
```bash
git clone/git pull (na pasta)
git add .
git commit -m "mensagem"
git push
```