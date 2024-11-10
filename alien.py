import csv

# Load dictionary from CSV file
def load_dictionary(filename="dictionary.csv"):
    dictionary = {}
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    english, aliench = row
                    dictionary[english.strip().lower()] = aliench.strip().lower()
                    dictionary[aliench.strip().lower()] = english.strip().lower()  # Allow reverse translation
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return dictionary

# Translate text from English to Aliench
def translate_to_aliench(text, dictionary):
    words = text.split()
    translation = []
    for word in words:
        translated_word = dictionary.get(word.lower())
        if translated_word:
            translation.append(translated_word)
        else:
            translation.append(f"[ERROR: '{word}' not found]")
    return ' '.join(translation)

# Translate text from Aliench to English
def translate_to_english(text, dictionary):
    words = text.split()
    translation = []
    for word in words:
        translated_word = dictionary.get(word.lower())
        if translated_word:
            translation.append(translated_word)
        else:
            translation.append(f"[ERROR: '{word}' not found]")
    return ' '.join(translation)

# Check if the word already exists in the dictionary
def word_exists(word, dictionary):
    return word.lower() in dictionary

# Add a new word to the dictionary and update CSV file
def add_to_dictionary(english, aliench, filename="dictionary.csv"):
    dictionary = load_dictionary(filename)
    
    if word_exists(english, dictionary) or word_exists(aliench, dictionary):
        print(f"Error: '{english}' or '{aliench}' already exists in the dictionary.")
    else:
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([english.lower(), aliench.lower()])
        print(f"Added '{english}' as '{aliench}' to the dictionary.")

# Main function for handling text file input/output
def alien_human_interpreter(input_file, output_file, mode="english-to-aliench"):
    dictionary = load_dictionary()
    
    with open(input_file, "r") as file:
        text = file.read()
    
    if mode == "english-to-aliench":
        translated_text = translate_to_aliench(text, dictionary)
    elif mode == "aliench-to-english":
        translated_text = translate_to_english(text, dictionary)
    else:
        raise ValueError("Invalid mode. Use 'english-to-aliench' or 'aliench-to-english'.")
    
    with open(output_file, "w") as file:
        file.write(translated_text)
    print(f"Translation completed. Check '{output_file}' for the result.")

# Example usage
# Load dictionary and start translation or adding functionality
if __name__ == "__main__":
    # Sample operations
    input_text_file = "input.txt"   # Text file to be translated
    output_text_file = "output.txt" # Translated text file
    
    # Translate English to Aliench
    alien_human_interpreter(input_text_file, output_text_file, mode="english-to-aliench")
    
    # Translate Aliench to English
    # alien_human_interpreter(input_text_file, output_text_file, mode="aliench-to-english")
    
    # Adding a new word
    # add_to_dictionary("love", "amor")
