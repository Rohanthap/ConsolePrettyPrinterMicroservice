from flask import Flask, request
from os import environ
from termcolor import colored

app = Flask(__name__)

def create_ascii_graph(data):
    graph = ""
    for value in data:
        rounded_value = round(value, 2)
        bar = "█" * int(rounded_value)  # Create bar from block characters
        graph += f"{bar} {rounded_value}\n"
    return graph

# REST API endpoint for printing styled text
@app.route('/print', methods=['POST'])
def print_text():
    data = request.json

    # Extract text and styles from the request
    text = data.get('text', '')
    color = data.get('color', 'white')
    bold = data.get('bold', False)
    underline = data.get('underline', False)

    attrs = []
    if bold:
        attrs.append('bold')
    if underline:
        attrs.append('underline')

    # Apply styles using termcolor
    styled_text = colored(text, color, attrs=attrs)

    styled_text_with_newline = styled_text + "\n"

    # Return the raw ANSI-colored text to the client
    return styled_text_with_newline

# REST API endpoint for creating an ASCII graph
@app.route('/graph', methods=['POST'])
def create_graph():
    data = request.json

    # Extract float values from the request
    values = data.get('values', [])
    if not all(isinstance(val, (int, float)) for val in values):
        return "Error: All values must be numbers\n", 400

    graph = create_ascii_graph(values)

    return graph

# Run the Flask app
if __name__ == '__main__':
    app.run(host='localhost', port=environ['PORT'] or 5000)