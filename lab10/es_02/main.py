if __name__ == '__main__':
    input_file_name = input('Input file name: ') # Prendo in input il nome del file con il testo
    output_file_name = input('Output file name: ') # Scrivo il nome del file su cui dovrò scrivere il testo al contrario

    input_file = open(input_file_name, 'r') #Apro in lettura il file input.txt

    input_text = input_file.readlines() # Leggo tutto il testo e lo memorizzo in una lista

    input_file.close() # Chiudo il file di input
    input_text.reverse() # 'rovescio' il contenuto della lista
    output_file = open(output_file_name, 'w') # Apro il file di output
    output_file.writelines(input_text) # Scrivo tutte le linee di testo nel file di output
    output_file.close() # Chiudo il file di output
