# Estruturando um projeto de dados

 
 O objetivo desse repositório é apresentar a estruturação de um projeto de dados do zero: extração, transformação e carregamento. O case consiste em concatenar vários arquivos em Excel em um único arquivo.
 
 Foram aplicadas técnicas de refatorização, melhorando a qualidade do código e otimizando a performance.

Aqui foi possível:

* entender a estrutura padrão de projetos, com a organização dos diretórios, funções e módulos, documentação e testes;
* compreender ferramentas de desenvolvimento como PIP e Poetry;
* realizar testes unitários utilizando o Pytest;
* fazer o versionamento com Git e Github;
* compreender o que cada arquivo do projeto representa;
* documentar o projeto usando o Mkdocs. [Clique aqui para acessar a documentação](https://almeidamariana.github.io/estrutura_projeto/)


### Passo a passo para instalação e configuração

1. Clonar o repositório:

```bash
git clone https://github.com/almeidamariana/estrutura_projeto.git
cd estrutura_projeto
```

2. Configurar a versão do Python com `pyenv` e instalar as dependências:

```bash
pyenv install 3.11.3
pyenv local 3.11.3
```

```bash
poetry install
```

3. Ativar o ambiente virtual:

```bash
poetry shell
```

4. Executar os testes:

```bash
task test
```

5. Ver a documentação do projeto:

```bash
task doc
```

6. Executar a pipeline para realizar a ETL:

```bash
task run
```

7. Verificar se o arquivo na pasta data/output foi gerado.
