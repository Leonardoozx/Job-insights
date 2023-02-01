# Boas-vindas ao repositório do Job Insights!

<strong>👨‍💻 O que foi desenvolvido</strong><br />

  <p align="center">
    <img src="/.images/job.png" alt="Logo Aplicação" width="300"/>
  </p>
  
  Neste projeto foram implementadas análises a partir de um conjunto de dados sobre empregos. Implementações incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python). Também foram escritos testes para a implementação de uma análise de dados. E uma rota e view para um recurso novo usando Flask!

Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

🚵 Habilidades trabalhadas:

  <ul>
    <li>Utilizar o terminal interativo do Python.</li>
    <li>Utilizar estruturas condicionais e de repetição.</li>
    <li>Utilizar funções built-in do Python.</li>
    <li>Utilizar tratamento de exceções.</li>
    <li>Realizar a manipulação de arquivos.</li>
    <li>Escrever funções.</li>
    <li>Escrever testes com Pytest.</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos.</li>
  </ul>

# Como rodar o projeto

1. Clone o repositório

- Use o comando: `git clone git@github.com:tryber/sd-021-b-project-job-insights.git`.
- Entre na pasta do repositório que você acabou de clonar:
  - `cd sd-021-b-project-job-insights`

2. Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências

- `python3 -m pip install -r dev-requirements.txt`

4. Rode o comando `flask run` na raíz do prejeto

- O projeto estará disponivel aqui: [http://127.0.0.1:5000/jobs](http://127.0.0.1:5000/jobs)

5. Aproveite :)

<strong>🛠 Testes</strong><br />

Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

<strong>Executar os testes</strong>

```bash
$ python3 -m pytest
```

O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

```bash
python3 -m pytest -s -vv
```

Caso precise executar apenas um arquivo de testes basta executar o comando:

```bash
python3 -m pytest tests/nomedoarquivo.py
```

Caso precise executar apenas uma função de testes basta executar o comando:

```bash
python3 -m pytest -k nome_da_func_de_tests
```

Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

```bash
python3 -m pytest -x tests/test_jobs.py
```

Para executar um teste específico de um arquivo, basta executar o comando:

```bash
python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
```
