# Click Games

## Descrição do Projeto
"Click Games" é um aplicativo Django que possui o jogo "Pedra, Papel ou Tesoura".
Para este desafio o tema principal foi login e autenticação de usuários. Neste projeto, é possível:
- Jogar "Pedra, Papel ou Tesoura" contra o Computador
- Ver seu histórico de logins e partidas

## URLs
- **admin/:** Template padrão de admin do Django
- **login/:** Página de login da pessoa usuária
- **logout/:** Link para o logout
- **criar-conta/:** Página para criação de conta na plataforma
- **home/:** Página inicial onde é possível iniciar um novo jogo
- **historico-login/:** Página para consulta do histórico de logins
- **historico-jogos/:** Página para consulta do histórico de jogos

## Models
### Jogo
O model que gerencia a escolha do usuário, gera a escolha do computador, calcula o resultado da partida e registra a data e hora dela. Com os parâmetros:
- **usuario:** model, o usuário autenticado na plataforma, referenciado como ForeignKey (relação 1:N, usuário:jogos). Herda do model padrão User do Django
- **opcao_usuario:** string, a opção de jogo escolhida pelo usuário entre as opções oferecidas pela constante ESCOLHAS_JOGO
- **opcao_computador:** string, a opção de jogo escolhida pelo computador através de uma função do model Jogo
- **resultado:** string, o resultado do jogo pela visão do usuário
- **data:** datetime, a data e hora do jogo

### HistoricoLogin
O model que salva a data e hora do login feito pelo usuário. Com os parâmetros:
- **usuario**: model, o usuário autenticado na plataforma, referenciado como ForeignKey (relação 1:N, usuário:logins). Herda do model padrão User do Django
- **data**: datetime, a data e hora do login

## Forms
### LoginForm
O form que gerencia o login do usuário, com os parâmetros:
- **usuario:** CharField, o usuário a ser logado, passado para o form como TextInput
- **senha:** CharField, a senha do usuário, passada para o form como PasswordInput

### CriarContaForm
O form que gerencia a criação de novas contas, herdada do form padrão do Django **UserCreationForm** com os parâmetros:
- **username:** CharField, o nome do usuário a ser criado, passado para o form como TextInput
- **password1:** CharField, a senha do usuário, passada para o form como PasswordInput
- **password2:** CharField, a confirmação de senha do usuário, passada para o form como PasswordInput. Deve ser igual a **password1**

### JogoForm
O form que gerencia a opção escolhida pelo usuário para o jogo "Pedra, Papel ou Tesoura", com o parâmetro:
- **opcao_usuario:** ChoiceField, a escolha do usuário entre as opções definidas na constante ESCOLHAS_JOGO, passado para o form como Select

### Pré-requisitos
- Python 3.x
- pip (Python package installer)
- Virtualenv (opcional, mas recomendado)

### Passo a Passo

1. **Clone o repositório:**
    ```bash
    git clone https://git.raroacademy.com.br/gabriel.monteiro/desafio-semana-7.git
    cd desafio-semana-7
    ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Realize as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5. **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

6. **Acesse o aplicativo no navegador:**
    Abra `http://127.0.0.1:8000/` no seu navegador.

## Funcionalidades
- **Login:** Faça login na plataforma com nome de usuário e senha
- **Criação de conta:** Crie uma nova conta para ter acesso ao jogo e aos históricos
- **Histórico de login:** Veja o histórico de entradas no sistema
- **Histórico de jogos:** Veja o histórico de jogos com a sua escolha, escolha do computador, resultado e a data da jogo

## Contribuição
Sinta-se à vontade para contribuir com o projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

## Licença
Este projeto está licenciado sob os termos da licença MIT.