# Gramma: processamento de texto rápido com AI usando [GROQ API](https://groq.com/).

Gramma é um app que fica "escutando" a área de transferência e detecta prefixos de comandos personalizados. Quando um comando é detectado, ele envia o texto para a GROQ API usando um prompt personalizado para processar o texto e, em seguida, copia o texto processado de volta para a área de transferência. Este projeto é projetado para ser leve e eficiente, garantindo impacto mínimo no desempenho.

## Como Funciona

1. **Monitoramento da Área de Transferência**: O script monitora continuamente a área de transferência em busca de alterações.
2. **Detecção de Comando**: Quando uma alteração é detectada, ele verifica se o texto da área de transferência começa com algum dos prefixos de comando predefinidos.
3. **Interação com a API**: Se um comando for detectado, o script envia o texto (excluindo o prefixo do comando) para a GROQ API com um prompt personalizado correspondente.
4. **Processamento de Texto**: A IA processa o texto e retorna a versão modificada de acordo com o comando usado.
5. **Atualização da Área de Transferência**: O texto processado é copiado de volta para a área de transferência.
6. **Notificação**: O usuário recebe uma notificação sobre o processamento bem-sucedido do texto.

## Funcionalidades

- **Carregamento Dinâmico de Comandos**: Adicione novos comandos facilmente via variáveis de ambiente no arquivo `.env`.
- **Chamadas de API Assíncronas**: Gerencie eficientemente as solicitações de API sem bloquear o thread principal.
- **Minimalismo**: O aplicativo não tem interface, apenas um ícone na bandeja do sistema com uma opção para sair, já que o aplicativo foi projetado para ser usado a qualquer momento, sem interferir no seu foco.
- **Tratamento de Erros e Notificações**: Notificações informativas para erros e limitações de taxa.

## Requisitos

- Python 3.7+
- `pyperclip`
- `python-dotenv`
- `groq`
- `pystray`
- `pillow`
- `plyer`

## Instalação

### 1. Instalar Python

Certifique-se de ter a versão mais recente do Python instalada. Baixe-o no [site oficial do Python](https://www.python.org/downloads/).

### 1.5. (OPCIONAL) Instalar GIT

Certifique-se de ter a versão mais recente do GIT instalada. Baixe-o no [site oficial do GIT](https://git-scm.com/).

### 2. Clonar o Repositório

Clone este repositório usando o comando:

```sh
git clone https://github.com/seu_usuario/gramma.git
cd gramma
```

### 3. Criar e Ativar um Ambiente Virtual

Crie e ative um ambiente virtual:

```sh
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

### 4. Instalar Dependências

Instale as dependências do projeto:

```sh
pip install -r requirements.txt
```

### 5. Configurar Variáveis de Ambiente

Renomeie `.env.example` para `.env`:

```sh
mv .env.example .env
```

Edite o arquivo `.env` com sua API_KEY da Groq, substituindo `YOUR_GROQ_API_KEY` pela sua chave real do [console da GROQ](https://console.groq.com/keys):

### Deve ficar assim após a edição:

```env
GROQ_API_KEY=gsk_y**********************************************
```

## Uso

### Iniciar o Listener de Área de Transferência

Você pode criar um atalho para o arquivo `gramma_starter.bat` e movê-lo para qualquer lugar para executar o Gramma.

### Ícone na Bandeja

O script será minimizado para a bandeja do sistema. Clique com o botão direito no ícone da bandeja para sair.

### Usando Comandos

Copie texto para sua área de transferência com um dos prefixos de comando (por exemplo, `!gf Seu texto aqui` para correção gramatical).

## Adicionando Novos Comandos

Para adicionar novos comandos, basta adicionar novas variáveis de ambiente em seu arquivo `.env` com o prefixo `PROMPT_`. Por exemplo:

```env
PROMPT_MW=Você é uma ferramenta que transforma texto como se tivesse escrito por um gato, responda com o texto recebido em forma de gato.
```

Salve o arquivo e execute o Gramma novamente, você deverá ser capaz de invocá-lo com seu novo prefixo, neste caso `!mw`. Aqui está em ação:

```plaintext
!mw Eu sou muito legal, gosto de livros, filmes e jogos.
```

Deveria gerar algo como:

```plaintext
Miaaau, eu sou miauuito legal, eu amoo livrosss, filmeeesss e joguinhos! *se esfrega na perna*
```

## Estrutura do Projeto

```plaintext
gramma/
│
├── .env              # Variáveis de ambiente
├── requirements.txt  # Dependências do projeto
├── script.py         # Script principal
├── gramma_starter.bat # Arquivo bat para iniciar o Gramma na bandeja do sistema
└── README.md         # Documentação do projeto (o que você está lendo agora)
```

## Contribuindo

Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request.

## Autor

Criado por [lkotlarenko](https://github.com/lkotlarenko).

## Licença

Este projeto está licenciado sob a Licença MIT.

## Links

- [Site da GROQ](https://groq.com/)
