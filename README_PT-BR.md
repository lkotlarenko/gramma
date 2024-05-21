**Note:** [Read the english version of this file](https://github.com/lkotlarenko/gramma/blob/main/README.md)

# Gramma: Revolucione sua Escrita em Qualquer Lugar com IA

Gramma é uma aplicação Python inovadora que transforma sua área de transferência em um assistente de texto inteligente. O app identifica prefixos de comando específicos dentro do texto copiado. Após o reconhecimento, ele interage com a API GROQ, utilizando prompts personalizados para melhorar e refinar seu texto. Seja para corrigir erros gramaticais, condensar artigos longos ou processar conteúdo de maneira criativa, Gramma é a sua solução ideal. É muito fácil adicionar novos comandos e formas de processamento!

Projetado com eficiência em mente, o app garante um impacto mínimo no desempenho do seu sistema. Eleve sua escrita e criação de conteúdo com Gramma – onde conveniência encontra inteligência.

## Comandos Padrão

Gramma vem com um conjunto de comandos padrão para aprimorar sua experiência de processamento de texto. Abaixo está uma lista dos comandos padrão que você pode usar:

- `!gf` - **Correção Gramatical**: Melhora a gramática do seu texto.
  ```
  !gf Eu não possu acredita que etou vendo isso!
  ```
  Resultado:
  ```
  Eu não posso acreditar que estou vendo isso!
  ```

- `!sm` - **Resumir**: Gera um resumo conciso do texto.
  ```
  !sm A degradação do meio ambiente...
  ```
  Resultado:
  ```
  Texto resumido.
  ```

- `!tl` - **Traduzir**: Traduza o texto fornecido. (Por padrão o comando traduz de qualquer lingua para Inglês, voce pode editar isso em `commands.py`)
  ```
  !tl Oi, como vai o seu dia?
  ```
  Resultado:
  ```
  Hi, how is your day?
  ```

- `!df` - **Definir**: Fornece uma definição de uma palavra ou expressão.
  ```
  !df serendipity
  ```
  Resultado:
  ```
  A ocorrência de eventos por acaso de uma maneira feliz ou benéfica.
  ```

## Adicionando ou Editando Comandos

Adicionar novos comandos ou editar os existentes no Gramma é simples. Siga estes passos:

1. **Adicionar ou Editar Comandos**:
    - **Localize o arquivo `commands.py`.**
    - Para adicionar um novo comando, adicione uma nova entrada ao dicionário `commands` com a chave e o prompt apropriados. A chave deve seguir o formato `PROMPT_<COMANDO>`.
    - Para editar um comando existente, localize o comando desejado no dicionário `commands` e modifique seu prompt.

    Exemplo:
    ```python
    commands = {
        "PROMPT_GF": "You are a multi-language grammar enhancement tool...",
        "PROMPT_SM": "You are a multi-language AI designed to summarize text...",
        "PROMPT_TL": "You are a multi-language AI designed to translate text...",
        "PROMPT_DF": "You are a multi-language AI designed to define words...",
        "PROMPT_MW": "Você é uma ferramenta que transforma texto em uma forma felina, output o texto recebido em uma forma semelhante a um gato."
    }
    ```

2. **Salvar o Arquivo**: Após adicionar ou editar o comando, salve o arquivo `commands.py`.
3. **Reiniciar o Gramma**: Para que as mudanças tenham efeito, reinicie o Gramma fechando o aplicativo e executando-o novamente.
4. **Invocar seu novo comando**: Agora você pode usar o novo prefixo de comando. Por exemplo, copiando:
    ```
    !mw Eu sou muito legal, gosto de livros, filmes e jogos.
    ```
    Resultará em algo semelhante a:
    ```
    Miauu, eu sou muito legal, gosto de livroz, filmez e jogoz! *esfrega na perna*
    ```

Seguindo estes passos, você pode facilmente personalizar o Gramma para atender às suas necessidades específicas e adicionar novas funcionalidades conforme necessário.

## Como Funciona

1. **Monitoramento da Área de Transferência**: Monitora continuamente a área de transferência para mudanças.
2. **Detecção de Comandos**: Verifica se o texto da área de transferência começa com algum prefixo de comando predefinido.
3. **Interação com API**: Envia o texto (excluindo o prefixo do comando) para a API GROQ com um prompt personalizado correspondente.
4. **Processamento de Texto**: A IA processa o texto e retorna a versão modificada.
5. **Atualização da Área de Transferência**: O texto processado é copiado de volta para a área de transferência.
6. **Notificação**: Exibe uma notificação sobre o processamento bem-sucedido do texto.

## Funcionalidades

- **Carregamento Dinâmico de Comandos**: Adicione novos comandos facilmente via `commands.py`.
- **Totalmente Gratuito e Open Source**: Veja e modifique qualquer coisa sem limites.
- **Foco na Privacidade**: Nenhum dado da área de transferência é processado fora dos prefixos de comando.
- **Chamadas de API Assíncronas**: Manipule solicitações de API eficientemente sem bloquear a thread principal.
- **Design Minimalista**: Sem interface, apenas um ícone na bandeja do sistema com uma opção de saída.
- **Tratamento de Erros e Notificações**: Notificações informativas para erros e limitação de taxa.

## Requisitos

- Python 3.7+
- Chave de API do Groq (obtenha uma gratuitamente [aqui](https://console.groq.com/keys))

## Instalação

1. **Instale o Python**

Certifique-se de ter a versão mais recente do Python instalada. Baixe-a do [site oficial do Python](https://www.python.org/downloads/).

1.5. **(Opcional) Instale o GIT**

Certifique-se de ter a versão mais recente do GIT instalada. Baixe-a do [site oficial do GIT](https://git-scm.com/downloads).

#### Abra um terminal (digite `cmd` no caminho do Explorer de qualquer pasta onde você deseja instalar o Gramma no Windows) para executar as seguintes instruções:

1. **Clone o Repositório** (se você não instalou o git, pode baixá-lo manualmente clicando em `<> Code` e `Download ZIP` (no topo desta página), e extraia tudo em uma pasta)

```sh
git clone https://github.com/lkotlarenko/gramma.git
cd gramma
```

3. **Crie e Ative um Ambiente Virtual**

```sh
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

4. **Instale os Pacotes Necessários**

```sh
pip install -r requirements.txt
```

5. **Configure Variáveis de Ambiente**

Renomeie `.env.example` para `.env`:

```sh
mv .env.example .env
```

Edite o arquivo `.env` com sua API_KEY do Groq, substituindo `YOUR_GROQ_API_KEY` pela sua chave real disponivel no [console GROQ](https://console.groq.com/keys) (você pode editá-lo usando o notepad).

```env
GROQ_API_KEY=gsk_y**********************************************
```

## Uso

### Inicie o Gramma

No Windows você pode criar um atalho para o arquivo `gramma_starter.bat` e movê-lo para qualquer lugar para executar o Gramma.
E no Linux e Mac você pode rodar ou diretamente pelo script `gramma.py` em um terminal, ou usar o shell script `gramma_starter_linux.sh`.

### Ícone da Bandeja

O app será minimizado para a bandeja do sistema. Clique com o botão direito do mouse no ícone da bandeja para sair.

### Usando Comandos

Copie o texto para sua área de transferência com um dos prefixos de comando (por exemplo, `!gf Seu texto aqui` para correção gramatical).

#### Como alterar o modelo Groq usado no Gramma:

Por padrão, o Gramma usa o modelo llama3-70b-8192, você pode editar isso no arquivo `.env` substituindo o modelo dentro de `GROQ_MODEL` por qualquer outro modelo disponível no [console GROQ](https://console.groq.com/docs/models).

## Estrutura do Projeto

```plaintext
gramma/
│
├── src/
│    ├── images/            # Pasta para armazenar imagens do aplicativo (apenas o ícone no momento)
│    └── config.py          # Variáveis como nome do aplicativo e mais
├── .env                    # Variáveis de ambiente (onde você coloca sua chave API)
├── commands.py             # Onde você edita ou adiciona comandos
├── gramma.py               # Script principal
├── gramma_starter.bat      # Arquivo bat para iniciar o Gramma na bandeja do sistema (crie um atalho para ele para iniciar mais rápido)
├── gramma_starter_linux.sh # Shell script pra rodar Gramma no Linux or Mac 
├── README.md               # Documentação do projeto em inglês
├── README_PT-BR.md         # Documentação do projeto em Português Brasileiro (o que você está lendo agora)
└── requirements.txt        # Dependências do projeto
```

## Contribuindo

Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request.

## Autor

Criado por [lkotlarenko](https://github.com/lkotlarenko).

### Support me

Se você gostou do meu trabalho e quer me apoiar, você pode me patrocinar aqui no GitHub. Seu apoio me permitirá focar mais em projetos de código aberto. Essas contribuições me ajudarão a continuar aprendendo, crescendo e contribuindo para o ecossistema de código aberto 💚.

[![GitHub Sponsors](https://img.shields.io/github/sponsors/lkotlarenko?style=social)](https://github.com/sponsors/lkotlarenko)

## Licença

Este projeto é licenciado sob a Licença MIT.

## Links

- [Site do GROQ](https://groq.com/)
