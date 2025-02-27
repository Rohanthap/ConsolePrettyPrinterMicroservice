from flask import Flask, request
from termcolor import colored

app = Flask(__name__)

# Helper function to create an ASCII bar graph
def create_ascii_graph(data):
    graph = ""
    for value in data:
        rounded_value = round(value, 2)  # Round to 2 decimal places
        bar = "█" * int(rounded_value)  # Use block characters for the bar
        graph += f"{bar} {rounded_value}\n"
    return graph

# REST API endpoint for printing styled text
@app.route('/print', methods=['POST'])
def print_text():
    data = request.json

    # Extract text, color, and style from the request
    text = data.get('text', '')
    color = data.get('color', 'white')
    bold = data.get('bold', False)
    underline = data.get('underline', False)

    # Prepare attributes list, excluding None
    attrs = []
    if bold:
        attrs.append('bold')
    if underline:
        attrs.append('underline')

    # Apply styles using termcolor
    styled_text = colored(text, color, attrs=attrs)

    # Add a newline character to the styled text
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

    # Generate the ASCII graph
    graph = create_ascii_graph(values)

    # Return the graph to the client
    return graph

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)