# codeGuru - Google PaLM Text Generation
codeGuru is a Python script that leverages the Google PaLM (Probabilistic and Logical Modeling) API to generate text responses based on user input or content provided in files. It provides both command-line and interactive modes for convenient use.

# Requirements
Python 3.x
Google PaLM API key

# Installation
Install the required Python packages:

<code>pip install google.generativeai</code>

Configure your Google PaLM API key:
Replace 'YOUR_API_KEY' with your actual API key
palm.configure(api_key='YOUR_API_KEY')

# Usage
Command Line Mode
Run the script with command-line arguments to specify input files and optional instructions:

<code>python codeGuru.py file1.txt file2.txt instruction</code>

# Interactive Mode
Launch interactive mode to ask questions and receive text responses:

python codeGuru.py
Examples
Command Line Example

<code>python codeGuru.py question.txt answer.txt explain</code>

Interactive Mode Example

<code>python codeGuru.py</code>

# Instructions
In command-line mode, provide file paths for input and output along with an optional instruction.
In interactive mode, type your questions, code queries, or type 'exit' to quit.

