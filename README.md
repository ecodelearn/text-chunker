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
Feel free to contribute or raise issues in the repository!
