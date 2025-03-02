# Colored Text and ASCII Graph Microservice

This project provides a simple microservice that allows you to print colored text and create ASCII graphs using a REST API. The server (`server.py`) handles requests and returns styled text or graphs, while the client (`client.py`) is an optional test script to demonstrate the functionality.

---

## Table of Contents

1. Features
2. Requirements
3. Setup
4. Usage
   - Server Endpoints
   - Using `client.py`
   - Using `curl`
5. Example Output

---

## Features

- **Colored Text**: Print text to the client with custom colors, bold, and underline styles.
- **ASCII Graphs**: Generate simple bar graphs using ASCII characters from a list of float values.
- **REST API**: Interact with the microservice using HTTP POST requests.
- **Client Script**: Optional `client.py` script to test the server functionality.

---

## Requirements

- Python 3.x
- Flask (`pip install Flask`)
- termcolor (`pip install termcolor`)
- requests (for `client.py`, `pip install requests`)

---

## Setup

1. Clone the repository:
git clone https://github.com/your-username/colored-text-graph-microservice.git
cd colored-text-graph-microservice

2. Install the required Python libraries:
pip install Flask termcolor requests

3. Start the server:
python server.py

The server will run on `http://localhost:5000`.

---

## Usage

### Server Endpoints

The server provides two endpoints:

1. **Print Styled Text**:
- **Endpoint**: `/print`
- **Method**: `POST`
- **Request Body**:
  ```
  {
    "text": "Your text here",
    "color": "green",
    "bold": true,
    "underline": true
  }
  ```
- **Response**: Returns the styled text with ANSI escape codes for colors and styles.

2. **Create ASCII Graph**:
- **Endpoint**: `/graph`
- **Method**: `POST`
- **Request Body**:
  ```
  {
    "values": [3.5, 7.2, 4.8, 6.1]
  }
  ```
- **Response**: Returns an ASCII bar graph as plain text.

---

### Using `client.py`

The `client.py` script is an optional test file that demonstrates how to interact with the server. It sends requests to the server and prints the responses.

1. Run the server:
python server.py

2. In a separate terminal, run the client script:
python client.py

The script will:
- Print styled text in green (bold and underlined), blue (bold), and red.
- Generate and display an ASCII graph.

You can modify `client.py` to test different inputs or integrate its functions into your own code.

---

### Using `curl`

If you prefer to use `curl` instead of `client.py`, you can send requests directly to the server. Below are examples of how to use `curl` to interact with the server.

1. **Print Styled Text**:
curl -X POST http://localhost:5000/print
-H "Content-Type: application/json"
-d '{
"text": "Hello, World!",
"color": "green",
"bold": true,
"underline": true
}'

2. **Create ASCII Bar Graph**:
curl -X POST http://localhost:5000/graph/bar
-H "Content-Type: application/json"
-d '{
"values": [3.5, 7.2, 4.8, 6.1]
}'

3. **Create ASCII Bar Graph**:
curl -X POST http://localhost:5000/graph/line
-H "Content-Type: application/json"
-d '{
"values": [[0,10], [1,30], [2,20], [3,50], [4,40]]
}'

---

## Example Output

### Styled Text
Hello, World! # Green, bold, and underlined
This is a test. # Blue and bold
Goodbye! # Red

### ASCII Bar Graph
███ 3.5
███████ 7.2
█████ 4.8
██████ 6.1

### ASCII Line Graph
 50.00 |                                      ****
 46.00 |                                    **    ******
 42.00 |                                  **            ***
 38.00 |                                 *
 34.00 |                               **
 30.00 |            ****              *
 26.00 |          **    ****        **
 22.00 |        **          ****  **
 18.00 |     ***                **
 14.00 |   **
 10.00 | **
       --------------------------------------------------
        0.00  0.50  1.00  1.50  2.00  2.50  3.00  3.50  4.00

---

![alt text](https://github.com/Rohanthap/ConsolePrettyPrinterMicroservice/blob/main/image.png)
