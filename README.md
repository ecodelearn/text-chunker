# Text Chunker

## Language Selector
- [English](#text-chunker)
- [Portugues](#Divisor-de-Texto)

---

# Text Chunker

This Python script processes large text files by dividing their content into smaller chunks of a specified size (default: 4000 words). Each chunk is labeled with headers and footers for better identification, and the processed text is saved to an output file. This is particularly useful when dealing with large documents that need to be analyzed or processed in smaller parts.

## Features

1. **Text Splitting**: Splits the input text into smaller chunks based on a specified word limit.
2. **Chunk Labeling**: Adds headers and footers to each chunk for clear identification.
3. **File Input and Output**: Reads text from a file and writes the processed chunks to a new file.

## Usage

### Prerequisites
- Python 3.x

### Installation
Clone the repository or download the script file.
```bash
git clone <repository_url>
cd <repository_directory>
```

### Running the Script
Use the following command:
```bash
python script.py <path_to_text_file>
```
- `<path_to_text_file>`: Path to the input text file that you want to process.

Example:
```bash
python script.py example.txt
```

### Output
The script will generate a new file named `<original_file_name>_chunks.txt` in the same directory as the input file. This file will contain the processed chunks with headers and footers.

### Example Output Format
```
### Start of Chunk 1 ###
<chunk content>
### End of Chunk 1 ###
==================================================
### Start of Chunk 2 ###
<chunk content>
### End of Chunk 2 ###
==================================================
...
```

## Functions Overview

1. `split_text_into_chunks(text, chunk_size=4000)`:
   - Splits the input text into chunks of specified size (default: 4000 words).

2. `add_embeddings_to_chunks(chunks)`:
   - Adds headers and footers to each chunk for better readability.

3. `read_text_file(file_path)`:
   - Reads and returns the content of the specified text file.

4. `write_chunks_to_file(chunks, output_file_path)`:
   - Writes the processed chunks to the output file with separators.

5. `process_text(text)`:
   - Combines text splitting and embedding functions for complete text processing.

6. `main()`:
   - Entry point of the script. Manages file I/O and calls processing functions.

## Error Handling
- If the script is run without specifying a file, it will display the usage instructions and terminate.
- Ensure the input file exists and is readable.

## License
This project is licensed under the MIT License.

---

# Divisor de Texto

Este script Python processa arquivos de texto grandes, dividindo seu conteúdo em partes menores de um tamanho especificado (padrão: 4000 palavras). Cada parte é rotulada com cabeçalhos e rodapés para melhor identificação, e o texto processado é salvo em um arquivo de saída. Isso é úteis quando se trabalha com documentos extensos que precisam ser analisados ou processados em partes menores.

## Funcionalidades

1. **Divisão de Texto**: Divide o texto de entrada em partes menores com base em um limite especificado de palavras.
2. **Rotulagem de Partes**: Adiciona cabeçalhos e rodapés a cada parte para identificação clara.
3. **Entrada e Saída de Arquivos**: Lê o texto de um arquivo e escreve as partes processadas em um novo arquivo.

## Uso

### Requisitos
- Python 3.x

### Instalação
Clone o repositório ou baixe o arquivo do script.
```bash
git clone <repository_url>
cd <repository_directory>
```

### Executando o Script
Use o seguinte comando:
```bash
python script.py <caminho_do_arquivo_de_texto>
```
- `<caminho_do_arquivo_de_texto>`: Caminho para o arquivo de texto que você deseja processar.

Exemplo:
```bash
python script.py exemplo.txt
```

### Saída
O script gerará um novo arquivo chamado `<nome_do_arquivo_original>_chunks.txt` no mesmo diretório do arquivo de entrada. Este arquivo conterá as partes processadas com cabeçalhos e rodapés.

### Formato de Saída Exemplo
```
### Início da Parte 1 ###
<conteúdo da parte>
### Fim da Parte 1 ###
==================================================
### Início da Parte 2 ###
<conteúdo da parte>
### Fim da Parte 2 ###
==================================================
...
```

## Visão Geral das Funções

1. `split_text_into_chunks(text, chunk_size=4000)`:
   - Divide o texto de entrada em partes do tamanho especificado (padrão: 4000 palavras).

2. `add_embeddings_to_chunks(chunks)`:
   - Adiciona cabeçalhos e rodapés a cada parte para melhor legibilidade.

3. `read_text_file(file_path)`:
   - Lê e retorna o conteúdo do arquivo de texto especificado.

4. `write_chunks_to_file(chunks, output_file_path)`:
   - Escreve as partes processadas no arquivo de saída com separadores.

5. `process_text(text)`:
   - Combina as funções de divisão e de adicição de cabeçalhos para o processamento completo do texto.

6. `main()`:
   - Ponto de entrada do script. Gerencia a entrada e saída de arquivos e chama as funções de processamento.

## Tratamento de Erros
- Se o script for executado sem especificar um arquivo, ele exibirá as instruções de uso e será encerrado.
- Certifique-se de que o arquivo de entrada existe e é legível.

## Licença
Este projeto está licenciado sob a Licença MIT.
