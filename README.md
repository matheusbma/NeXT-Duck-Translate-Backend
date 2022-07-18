## <h1 align="center"> Duck Translator </h1>

![Duck](https://user-images.githubusercontent.com/99835081/173959180-198cd1b0-68c2-42e8-8e95-3472a5d78057.jpg)

Idioma: [pt-BR](#Índice)  |  [en-US](#Index)

## Índice

- [Descrição](#Descrição) 
- [Tecnologias](#Tecnologias)
- [Funcionalidades](#Funcionalidades)
- [Instalação](#Instalação)
- [Desenvolvedores](#Desenvolvedores)
- [Licença](#Licença)



## Descrição

Projeto desenvolvido durante o módulo prático do curso NExT 2022, promovido pela Cesar School. O Duck Translate é um sistema de transcrição de áudios e tradução de textos.

O sistema se apresenta como uma ferramenta para:

1. Tradução de textos inseridos no campo de tradução, para uma determinada língua;
2. Transcrição de um arquivo de áudio, seguido, ou não, de uma tradução para uma língua escolhida.



## Tecnologias

- Linguagem de programação: [Python 3.10.5](#https://www.python.org)

- Framework: [Flask](#https://flask.palletsprojects.com/en/2.1.x/)

- [Google Cloud Speech-To-Text API](#https://cloud.google.com/speech-to-text)

- [Google Cloud Translation API](#https://cloud.google.com/translate)

  ![Backlog_Duck_Translator_white_bg](https://user-images.githubusercontent.com/99835081/174130756-ad058121-96a1-4e91-9671-4e915eddf272.png)


## Funcionalidades

### Tradução de texto

Nesta funcionalidade, o usuário irá inserir um texto no campo de tradução e irá informar a língua em que texto seja exibido. Nosso sistema faz uso da Cloud Translation API para produzir o resultado. Utilizando a IA de tradução do Google Cloude, temos a possibilidade de traduzir textos dinamicamente entre milhares de pares de idiomas.

### Transcrição de áudio

Utilizamos a abordagem de reconhecimento assíncrono de fala, aonde são enviados dados de áudio para a Cloud API Speech-to-Text e inicia-se uma operação de longa duração. Usando essa operação, é possível pesquisar periodicamente resultados de reconhecimento. Usamos solicitações assíncronas para dados de áudio de até 59 segundos de duração.

Com isso, o usuário pode fazer o upload de um arquivo de áudio, do tipo WAV ou FLAC, ou ainda gravar sua voz utilizando o recurso de microfone disponível no sistema. Temos como retorno desta funcionalidade o texto de transcrição do áudio fornecido. Caso deseje, o usuário poderá solicitar a tradução do texto para uma outra língua.



## Instalação

### Preparação do ambiente

- Instale o Python (https://www.python.org)
- Instale o Flask (https://flask.palletsprojects.com/en/2.1.x/)
- Obs: caso seu SO for Windows, talvez seja necessário habilitar a política de execução como irestrita. Utilize o comando `Set-ExecutionPolicy Unrestricted -Scope Process`

### Bibliotecas

Para instalar as bibliotecas necessárias para a aplicação, use o comando `pip install -r requirements.txt`

### Credenciais da GCP 

Coloque o arquivo JSON de suas credenciais no diretório /Backend/



## Desenvolvedores

- [Mariana Calado](https://github.com/maricalado)
- [Matheus Araújo](https://github.com/matheusbma)
- [Nathalie Maciel](https://github.com/Nathalie-Maciel)
- [Rodrigo Leão](https://github.com/rodrigoleao111)

- Orientador: [David Santos](https://github.com/davidwilsonfs)

## Licença

Licença de software livre
- Software pode ser modificado, usado comercialmente e distribuído.
- Software pode ser modificado e usado de forma privada.
- A licença e os direitos precisam ser incluídos no software.
- Os autores dos software não provêm garantias.




------




## Index

- [Description](#Description)
- [Technologies](#Technologies)
- [Features](#Features)
- [Installation](#Installation)
- [Developers](#Developers)
- [License](#License)



## Description

Project developed during the practical module of the NExT 2022 course, promoted by Cesar School. Duck Translator is an audio transcription and text translation system.

The system presents itself as a tool for:

1. Translation of texts entered in the translation field, into a given language;
2. Transcription of an audio file, followed or not by a translation into a chosen language.



## Technologies

- Programming language: [Python 3.10.5](#https://www.python.org)

- Framework: [Flask](#https://flask.palletsprojects.com/en/2.1.x/)

- [Google Cloud Speech-To-Text API](#https://cloud.google.com/speech-to-text)

- [Google Cloud Translation API](#https://cloud.google.com/translate)

  ![Backlog_Duck_Translator_white_bg](https://user-images.githubusercontent.com/99835081/174130820-a7c5aabf-d5ad-4506-ae6b-3cae4830a047.png)


## Functionalities

### Text translation

In this functionality, the user will enter a text in the translation field and will inform the language in which the text will be displayed. Our system makes use of the Cloud Translation API to produce the result. Using Google Cloude's translation AI, we have the ability to dynamically translate texts between thousands of language pairs.

### Audio Transcript

We use the asynchronous speech recognition approach, where audio data is sent to the Speech-to-Text Cloud API and a long-running operation is initiated. Using this operation, you can periodically poll for recognition results. We use asynchronous requests for audio data up to 59 seconds long.

With this, the user can upload an audio file, of the WAV or FLAC type, or even record their voice using the microphone feature available in the system. We have as a return of this functionality the text of the audio transcript provided. If desired, the user may request the translation of the text into another language.



## Installation

### Environment Configuration

- Install Python (https://www.python.org)
- Install Flask (https://flask.palletsprojects.com/en/2.1.x/)
- Note: if your OS is Windows, you may need to enable the execution policy as unrestricted. Use the `Set-ExecutionPolicy Unrestricted -Scope Process` command

### Libraries

To install the necessary libraries for the application, use the command `pip install -r requirements.txt`

### GCP Credentials

Place the JSON file of your credentials in the /Backend/ directory



## Developers

- [Mariana Calado](https://github.com/maricalado)
- [Matheus Araújo](https://github.com/matheusbma)
- [Nathalie Maciel](https://github.com/Nathalie-Maciel)
- [Rodrigo Leão](https://github.com/rodrigoleao111)

- Advisor: [David Santos](https://github.com/davidwilsonfs)


## License

Open Souce Software License
- Software may be modified, used commercially and distributed.
- Software may be modified and used privately.
- The license and rights need to be included in the software.
- The authors of the software do not provide guarantees.
