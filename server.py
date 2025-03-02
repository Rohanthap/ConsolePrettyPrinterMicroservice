from flask import Flask, request, jsonify
from os import environ
from termcolor import colored
import numpy as np

app = Flask(__name__)

def create_ascii_bar_graph(data):
    graph = ""
    for value in data:
        rounded_value = round(value, 2)
        bar = "█" * int(rounded_value)  # Create bar from block characters
        graph += f"{bar} {rounded_value}\n"
    return graph

def create_ascii_line_graph(data):
    if not data:
        return "Error: No data provided\n"

    # Sort data for correct plotting
    data = sorted(data, key=lambda point: point[0])
    x_values, y_values = zip(*data)

    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)

    height = 10
    width = 50  

    y_scale = (max_y - min_y) / max(1, height)

    x_positions = np.interp(np.linspace(0, width - 1, num=width), np.linspace(0, width - 1, num=len(x_values)), x_values)

    graph_matrix = np.full((height + 1, width), ' ', dtype=str)

    prev_x, prev_y = None, None
    for x, y in data:
        scaled_x = np.argmin(np.abs(x_positions - x))  # Match closest x-tick
        scaled_y = round((y - min_y) / (max_y - min_y) * height)

        graph_matrix[height - scaled_y, scaled_x] = '*'

        # Line interpolation for better connectivity
        if prev_x is not None:
            x1, y1 = prev_x, prev_y
            x2, y2 = scaled_x, scaled_y

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            sx = 1 if x1 < x2 else -1
            sy = 1 if y1 < y2 else -1
            err = dx - dy

            while (x1, y1) != (x2, y2):
                graph_matrix[height - y1, x1] = '*'
                e2 = 2 * err
                if e2 > -dy:
                    err -= dy
                    x1 += sx
                if e2 < dx:
                    err += dx
                    y1 += sy

        prev_x, prev_y = scaled_x, scaled_y

    graph = ""
    for i, row in enumerate(graph_matrix):
        graph += f"{max_y - i * y_scale:6.2f} | {''.join(row)}\n"

    graph += "       " + "-" * width + "\n"

    x_label_str = "  ".join(f"{x:.2f}" for x in np.linspace(min_x, max_x, num=9))
    graph += "        " + x_label_str + "\n"

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

# REST API endpoint for creating an ASCII bar graph
@app.route('/graph/bar', methods=['POST'])
def create_bar_graph():
    data = request.json

    # Extract float values from the request
    values = data.get('values', [])
    if not all(isinstance(val, (int, float)) for val in values):
        return "Error: All values must be numbers\n", 400

    graph = create_ascii_bar_graph(values)

    return graph

# REST API endpoint for creating an ASCII line graph with (x, y) tuples
@app.route('/graph/line', methods=['POST'])
def create_line_graph():
    data = request.json

    # Extract (x, y) tuples from the request
    values = data.get('values', [])
    if not all(isinstance(val, (list, tuple)) and len(val) == 2 and all(isinstance(n, (int, float)) for n in val) for val in values):
        return "Error: All values must be tuples of (x, y) coordinates with numbers\n", 400

    graph = create_ascii_line_graph(values)

    return graph

# Run the Flask app
if __name__ == '__main__':
    app.run(host='localhost', port=int(environ.get('PORT', 5000)))
