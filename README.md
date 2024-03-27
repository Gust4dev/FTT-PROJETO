Bem-vindo ao Projeto FTT, uma aplicação para gerenciamento de personagens de desenhos animados! Este manual fornece instruções passo a passo sobre como configurar e utilizar o projeto em seu próprio computador.

Pré-requisitos
Python 3.x
MySQL Server
Um navegador da web moderno (como Chrome, Firefox, ou similar)
Configuração do Ambiente

Clone o repositório do projeto para o seu computador:

```git clone https://github.com/seu-usuario/projeto-ftt.git```

Navegue até o diretório do projeto:

```cd projeto-ftt ```

Crie e ative um ambiente virtual Python (opcional, mas recomendado):

```python3 -m venv venv```
```source venv/bin/activate  # no Windows: venv\Scripts\activate```

Instale as dependências do Python:

```pip install -r requirements.txt```

Importe o banco de dados fornecido (dump.sql) para o seu servidor MySQL.
Atualize as configurações do banco de dados no arquivo app.py com suas credenciais:

```app.config['MYSQL_HOST'] = 'localhost'```
```app.config['MYSQL_USER'] = 'seu_usuario'```
```app.config['MYSQL_PASSWORD'] = 'sua_senha'```
```app.config['MYSQL_DB'] = 'bdftt'```

Executando o Projeto
Execute o aplicativo Flask:

```app.py```

Acesse a aplicação em seu navegador:

```http://localhost:5000```

Funcionalidades
Adicionar Novo Personagem: Clique no link "Adicionar Personagem" na página inicial para adicionar um novo personagem. Preencha o formulário e clique em "Adicionar".

Listar Personagens: Clique no link "Lista de Personagens" na página inicial para ver a lista de todos os personagens cadastrados.

Limpar Lista de Personagens: Na lista de personagens, você pode clicar no botão "Limpar Lista de Personagens" para remover todos os personagens do banco de dados.
