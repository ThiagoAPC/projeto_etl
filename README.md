
# Estudo Aplicado de ETL com aplicação em Relatório de Dados

Este projeto consiste em um estudo aplicado de ETL (Extração, Transformação e Carga) com Python e banco de dados SQLite, além de um dashboard em Power BI para a criação de relatórios dinâmicos baseados em dados de vendas. A ideia aqui não é se prender aos valores dos dados em si, já que eles são fictícios, mas sim entender os conceitos básicos de uma ETL sem arquitetura que gera utilidade e praticidade ao processo de Análise de Dados via Power BI.

## Arquivos do Projeto

- **`banco_dados.py`**: Script responsável pela conexão e manipulação do banco de dados. Ele contém funções para realizar operações no banco de dados SQLite, como inserção, exclusão, atualização e leitura de dados.
  
- **`consulta.py`**: Script de consulta aos dados do banco de dados de vendas. Ele executa consultas SQL para buscar informações relevantes para análise e transformação durante o processo de ETL.

- **`etl.py`**: Script responsável pelo processo de ETL, que realiza a extração dos dados de `vendas_com_problemas.db`, aplica as transformações necessárias e carrega os dados corrigidos no banco de dados `vendas_transformadas.db`.

- **`Relatório de Vendas.pbix`**: Arquivo do Power BI que contém o dashboard com as métricas e visualizações das vendas. Este arquivo usa os dados transformados para gerar gráficos e relatórios dinâmicos.

- **`vendas_com_problemas.db`**: Banco de dados inicial contendo os dados de vendas com problemas, como inconsistências e dados faltantes, que serão tratados no processo de ETL.

- **`vendas_transformadas.db`**: Banco de dados final contendo os dados de vendas após o processo de transformação e correção, utilizado pelo Power BI para gerar os relatórios.

## Como Utilizar

### Pré-requisitos

- Python 3.8 ou superior
- Instalação das bibliotecas necessárias (executar `pip install -r requirements.txt`)
- Power BI Desktop para abrir o arquivo `.pbix`

### Execução

1. **Preparar o ambiente**:
   - Verifique se o Python está instalado e que o banco de dados `vendas_com_problemas.db` está disponível no diretório raiz do projeto.

2. **Executar o processo de ETL**:
   - Execute o script `etl.py` para realizar a extração, transformação e carga dos dados no banco `vendas_transformadas.db`.

   ```bash
   python etl.py
   ```

3. **Consultar os dados**:
   - Utilize o script `consulta.py` para realizar consultas no banco de dados `vendas_transformadas.db`.

   ```bash
   python consulta.py
   ```

4. **Analisar os dados no Power BI**:
   - Abra o arquivo `Relatório de Vendas.pbix` no Power BI Desktop e conecte-se ao banco de dados `vendas_transformadas.db` para visualizar os gráficos e relatórios.

## Contribuição

Sinta-se à vontade para contribuir com o projeto, seja relatando problemas ou propondo melhorias por meio de pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
