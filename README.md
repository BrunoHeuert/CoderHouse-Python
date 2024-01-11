# Projeto Final PokeAPI

Esse projeto foi desenvolvido para ser um protótipo de uma Pokedex, na qual busca por dados de diversos pokémons consultados através da api "PokeAPI".

# Pré-requisitos

Para a execução desse projeto, é necessário a utilização das seguintes bibliotecas:

- requests
- pandas
- plyer
- sqlite3

O arquivo "requirements.txt" está disponível no projeto com todas a bibliotecas e suas versões, incluindo o próprio ipykernel.

# Instalação

Para facilitar a execução do projeto, pode estar replicando o requirements.txt no Virtual Enviroment através do comando: "pip install -r requirements.txt". 

Esse arquivo de texto possui todas as bibliotecas utilizadas para a criação e execução do projeto, facilitando a replicação em outros ambientes.

Para conferir se a instalação das bibliotecas e dll's deu certo após rodar o comando descrito ácima, é necessário utilizar o comando: "pip freeze"

Compare as informações do "requirements.txt" e certifique-se que as bibliotecas e suas versões no seu Virtual Enviroment de testes estão todas idênticas.

# Executando os testes

Agora, basta estar abrindo o arquivo do projeto disponibilizado no jupyter notebook e estar executando passo a passo. 

Nele terão diversas funções utilizadas para a criação de DataFrames através da PokeAPI que vão simular uma Pokedéx, trazendo informações especificas sobre os Pokémons.

# Código Explicação

Para realizar o get do JSON dentro da PokeApi teve que ser criada diversas funções, sendo essas utilizadas na criação dos DataFrames com os resultados buscados pela API.

Funções:
- get_id: Essa função é responsável por trazer o respectivo id de cada Pokémon. Para fazer isso, na chamda da mesma ela acessa o dicionário "results" da API "https://pokeapi.co/api/v2/pokemon?offset=0&limit=151" e acessa cada endpoint dando um get no "id" de cada URL de pokémon.
- get_info: Assim como a função "get_id", a função "get_info" acesso o "results" da API "https://pokeapi.co/api/v2/pokemon?offset=0&limit=151" e busca pelos campos "id", "base_experience", "height" e "weight" de cada respectivo Pokémon.
- get_stats: Da mesma forma que as funções acima, essa vai pegar os status dos Pokémon, sendo eles "hp", "attack", "defense", "special_attack", "special_defense" e "speed". Dessa vez, como os dados pegos estão dentro da lista "stats", teve-se que percorrer um for dentro da lista pegando o valor do "base_stat" de cada status.
- get_types: Seguinto exatamente a mesma fórmula do get_stats, dessa vez acessando a lista "types" foram pegos os tipos dos Pokémons. Porém, como nem todos Pokémons tem um tipo secundário, foi utilizado o método "try - except", no qual quando o tipo secundário não existisse ele traria preenchido como "None".
- tabelas_bd: Função que busca na database MASTER todas as tabelas cadastradas no Banco de Dados.
- salva_bd: Função responsável por salvar os dados de um DataFrame dentro de uma nova tabela gerada junto a ela.
- carrega_bd: Função responsável por executar o select da tabela selecionada, dessa forma mostrando os dados da mesma.

Tabelas/Dataframes:
- df_pokemon: Nessa tabela, foi criado um DataFrame que possui os dados de "id" e "name" de cada respectivo Pokémon. Para consulta do "id" foi utilizado um get da função "get_id", já o name foi pego do dicionário "results" pertecente a API "https://pokeapi.co/api/v2/pokemon?offset=0&limit=151".
- df_poke_info: Já aqui, o DataFrame foi criado com os dados puxados da API "get_info", na qual pegava o "id", "base_experience", "height" e "weight" de cada Pokémon, sendo replicados em colunas no DataFrame.
- df_poke_stats: Para a criação desse DataFrame, foi dado um get na função "get_stats", sendo essa responsável por trazer os status dos Pokémons, sendo eles "hp", "attack", "defense", "special_attack", "special_defense" e "speed". Assim como anteriormente, esses dados foram replicados em colunas para o DataFrame.
- df_poke_types: Nesse DataFrame, os dados foram pego através da função "get_types". Nela foram pegos os tipos primário e secundário de cada pokémon, caso algum dos mesmos não possuísse tipo secundario, o mesmo vem como "None", sendo esse substituido por "" posteriormente através do tratamento "fillna".

Tratamentos:
- .info: Utilizado em todas as tabelas para consultar as informações de cada tabela.
- isna: Utilizado em todas as tabelas para consultar se as tabelas possuem dados nulos.
- fillna: Utilizado somente nas tabelas onde foram identificados valores nulos ("None") para substitui-los por "".

Para facilitar todo o código encontra-se comentado.

# Fim

O projeto foi desenvolvido com bastante carinho, então aproveite!
