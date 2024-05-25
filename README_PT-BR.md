🌐 Leia a versão em inglês deste arquivo [aqui](https://github.com/lkotlarenko/gramma/blob/main/README.md).

# Gramma: Transforme seu CTRL-C / CTRL-V em um Assistente de Texto Inteligente

O Gramma é um app inovador em Python que transforma sua área de transferência em um assistente de texto inteligente. Com suas avançadas capacidades de monitoramento da área de transferência, o Gramma identifica prefixos de comandos específicos dentro do texto copiado. E, ao reconhecer esses prefixos, ele interage com a API GROQ, utilizando prompts personalizados para aprimorar e refinar seu texto usando IA. Seja para corrigir erros gramaticais, condensar artigos longos ou processar criativamente textos de várias maneiras, o Gramma é a ferramenta ideal.

## Funcionalidades

- **Carregamento Dinâmico de Comandos**: Adicione novos comandos facilmente através de uma interface gráfica intuitiva.
- **Totalmente Gratuito e Open Source**: Explore e modifique qualquer parte do código sem restrições.
- **Foco na Privacidade**: Seus dados da área de transferência são processados **SOMENTE** se um prefixo de comando for detectado.
- **Design Minimalista**: Interface leve e focada na usabilidade.
- **Notificações**: Receba notificações informativas e úteis.

## Requisitos

- Python 3.7 ou superior
- Chave de API do Groq (obtenha uma gratuitamente [aqui](https://console.groq.com/keys))

## Instalação

1. **Instale o Python**

   Garanta que você tenha a versão mais recente do Python instalada. Baixe-a do [site oficial do Python](https://www.python.org/downloads/).

2. **Baixe o Código Fonte**
   
   Acesse a [última versão](https://github.com/lkotlarenko/gramma/releases/latest) e baixe o arquivo "Source code (zip)".
   
3. **Extraia o Arquivo Zip**
   
   Descompacte o conteúdo do arquivo zip baixado em um diretório de sua preferência.
   
4. **Instale o Gramma**
   
   Para Windows:
   - Abra a pasta descompactada e dê um duplo clique em `install_windows.bat`.
   - Um terminal será aberto e instalará automaticamente as dependências necessárias, além de criar um atalho na área de trabalho para o Gramma.
   
   Para Linux/macOS:
   - Abra um terminal e navegue até a pasta descompactada.
   - Execute o comando: `bash install_linux.sh`
   - Isso instalará as dependências necessárias e criará um atalho na área de trabalho para o Gramma.

## Configuração

Após a instalação, execute o atalho do Gramma na sua área de trabalho. Você encontrará o ícone do Gramma na bandeja do sistema (área de notificação).

1. **Clique com o botão direito** no ícone do Gramma na bandeja do sistema.
2. Selecione **"Setup"**.
3. Insira sua **Chave de API GROQ** (obtenha uma gratuitamente [aqui](https://console.groq.com/keys)).
4. (Opcional) Altere o **Modelo de IA** se desejar (confira os disponíveis [aqui](https://console.groq.com/docs/models)).
5. Clique em **"Save"**.
6. Confirme

O Gramma está pronto para ser utilizado!

## Uso

1. **Copie o texto** para sua área de transferência com um dos prefixos de comando (por exemplo, `!gf Seu texto aqui` para correção gramatical).
2. **Aguarde a notificação** que indica que o texto foi processado.
3. O texto processado será automaticamente copiado de volta para sua área de transferência.

## Comandos Padrão

O Gramma vem com um conjunto de comandos padrão para otimizar sua experiência de processamento de texto:
_(por padrão as prompts não especificam língua, mas os modelos tendem a usar inglês, você pode alterar isso facilmente adicionando algo como "Responda apenas em PT-BR" no final delas)_

- `!gf` - **Correção Gramatical**: Melhora a gramática do seu texto.
- `!sm` - **Resumo**: Cria um resumo conciso do texto.
- `!tl` - **Tradução**: Traduz o texto fornecido.
- `!df` - **Definir**: Oferece a definição de uma palavra ou expressão.

## Adicionando ou Editando Comandos

Adicionar novos comandos ou editar os existentes no Gramma é fácil:

1. **Clique com o botão direito** no ícone do Gramma na bandeja do sistema.
2. Selecione **"Edit Commands"**.
3. Na janela "Editar Comandos", você pode:
   - **Adicionar um novo comando**: Clique no botão "Add Command" e insira o prefixo e o prompt do comando (o prefixo deve ter apenas duas letras que não estejam em uso por outros prefixos).
   - **Editar um comando existente**: Modifique o prefixo ou o prompt do comando conforme desejar.
   - **Excluir um comando**: Exclua qualquer comando da lista clicando no botão vermelho "X".
4. Clique em **"Save"** para aplicar as alterações.
5. Confirme

Os novos comandos ou comandos editados estarão disponíveis imediatamente para uso.

## Como Funciona

1. **Monitoramento da Área de Transferência**: O Gramma monitora continuamente a área de transferência em busca de alterações.
2. **Detecção de Comandos**: Verifica se o texto copiado inicia com algum dos prefixos de comandos predefinidos.
3. **Interação com a API**: O Gramma envia o texto (excluindo o prefixo do comando) para a API GROQ AI com um prompt personalizado correspondente.
4. **Processamento de Texto**: A IA processa o texto e retorna a versão aprimorada.
5. **Atualização da Área de Transferência**: O texto aprimorado é copiado de volta para a área de transferência.
6. **Notificação**: Uma notificação é exibida informando sobre o sucesso no processamento do texto.

## Contribuindo

Contribuições são sempre bem-vindas! Faça um fork do repositório e envie um pull request.

## Autor

Desenvolvido por [lkotlarenko](https://github.com/lkotlarenko).

### Apoie-me

Se você gostou do meu trabalho e quer me apoiar, você pode me patrocinar aqui no GitHub. Seu apoio me permitirá focar mais em projetos de código aberto. Essas contribuições me ajudarão a continuar aprendendo, crescendo e contribuindo para o ecossistema de código aberto 💚.

[![GitHub Sponsors](https://img.shields.io/github/sponsors/lkotlarenko?style=social)](https://github.com/sponsors/lkotlarenko)

## Licença

Este projeto está sob a [Licença MIT](LICENSE).

## Links

- [Site do Groq](https://groq.com/)
- [Console do Groq](https://console.groq.com/)

## Estrutura do Projeto

```plaintext
gramma/
│
├── src/
│   ├──core/
│   │  ├── clipboard_listener.py
│   │  ├── command_processor.py
│   │  ├── instance_manager.py
│   │  └── tray_icon.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   └── data_manager.py
│   │
│   ├── gui/
│   │   ├── base_page.py
│   │   ├── edit_commands_page.py
│   │   └── setup_page.py
│   │
│   ├── images/
│   │   ├── app_icon.ico
│   │   └── tray_icon.png
│   │
│   ├── managers/
│   │   └── instance_manager.py
│   │
│   ├── utils.py
│   └── config.py
│
├── tests/
│   ├──core/
│   │  └── __init__.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   └── test_data_manager.py
│   │
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── edit_commands_page.py
│   │   └── setup_page.py
│   ├── __init__.py
│   └── conftest.py
│
├── commands.json
├── gramma.py
├── install_linux.sh
├── install_windows.bat
├── gramma_starter_linux.sh
├── gramma_starter.bat
├── gramma_to_tray_win.vbs
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
├── README_PT-BR.md
└── settings.json
```