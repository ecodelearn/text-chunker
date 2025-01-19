import sys
import os

def split_text_into_chunks(text, chunk_size=4000):
    # Dividir o texto em palavras
    words = text.split()
    
    # Dividir o texto em chunks de 4000 palavras
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    
    return chunks

def add_embeddings_to_chunks(chunks):
    embedded_chunks = []
    for i, chunk in enumerate(chunks):
        if i == len(chunks) - 1:
            embedded_chunks.append(f"### Start of Chunk {i+1} (Last Chunk) ###\n{chunk}\n### End of Chunk {i+1} (Last Chunk) ###")
        else:
            embedded_chunks.append(f"### Start of Chunk {i+1} ###\n{chunk}\n### End of Chunk {i+1} ###")
    return embedded_chunks

def process_text(text):
    # Dividir o texto em chunks de 4000 palavras
    chunks = split_text_into_chunks(text)
    
    # Adicionar embeddings a cada chunk
    embedded_chunks = add_embeddings_to_chunks(chunks)
    
    return embedded_chunks

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def write_chunks_to_file(chunks, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for chunk in chunks:
            file.write(chunk)
            file.write("\n" + "="*50 + "\n")
    print(f"Chunks escritos no arquivo: {output_file_path}")

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <caminho_do_arquivo_de_texto>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Ler o texto do arquivo
    text = read_text_file(file_path)
    
    # Processar o texto
    embedded_chunks = process_text(text)
    
    # Determinar o nome do arquivo de saída
    base_name = os.path.splitext(file_path)[0]
    output_file_path = f"{base_name}_chunks.txt"
    
    # Escrever os chunks no arquivo de saída
    write_chunks_to_file(embedded_chunks, output_file_path)
    
    # Iniciar interação
    print("Agora, você pode começar a interagir sobre o texto.")

if __name__ == "__main__":
    main()
