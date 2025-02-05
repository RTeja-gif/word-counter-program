import re
from collections import Counter
import tkinter as tk
from tkinter import filedialog, messagebox

def count_words(text):
    """Counts the number of words in the given text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Counts the total number of characters in the text, including spaces."""
    return len(text)

def count_sentences(text):
    """Counts the number of sentences based on punctuation."""
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def count_paragraphs(text):
    """Counts the number of paragraphs in the text."""
    paragraphs = text.split("\n\n")  # Paragraphs separated by double newlines
    return len([p for p in paragraphs if p.strip()])

def most_frequent_words(text, n=5):
    """Finds the most common words in the text."""
    words = re.findall(r'\b\w+\b', text.lower())  # Extract words using regex
    word_counts = Counter(words)
    return word_counts.most_common(n)

def analyze_text(text):
    """Performs a full analysis on the text."""
    results = {
        "Words": count_words(text),
        "Characters": count_characters(text),
        "Sentences": count_sentences(text),
        "Paragraphs": count_paragraphs(text),
        "Frequent Words": most_frequent_words(text, 5),
    }
    return results

def load_file():
    """Loads a text file and analyzes it."""
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    
    update_results(analyze_text(text))

def analyze_input():
    """Analyzes user input from the text field."""
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Please enter some text.")
        return
    update_results(analyze_text(text))

def update_results(results):
    """Updates the GUI with the analysis results."""
    output_text.set(f"Words: {results['Words']}\n"
                    f"Characters: {results['Characters']}\n"
                    f"Sentences: {results['Sentences']}\n"
                    f"Paragraphs: {results['Paragraphs']}\n"
                    "Most Frequent Words:\n" +
                    "\n".join(f"{word}: {count}" for word, count in results["Frequent Words"]))

# GUI Setup
root = tk.Tk()
root.title("Advanced Word Counter")
root.geometry("500x600")

# Text Input
tk.Label(root, text="Enter Text or Load File:", font=("Arial", 12)).pack()
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# Buttons
tk.Button(root, text="Analyze", command=analyze_input, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Load File", command=load_file, bg="green", fg="white").pack(pady=5)

# Output
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, font=("Arial", 12), justify="left")
output_label.pack(pady=10)

# Run the GUI
root.mainloop()
