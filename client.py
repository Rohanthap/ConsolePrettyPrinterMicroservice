import requests

# Microservice base URL
BASE_URL = "http://localhost:5000"

# Function to print styled text
def print_styled_text(text, color, bold=False, underline=False):
    payload = {
        "text": text,
        "color": color,
        "bold": bold,
        "underline": underline
    }
    response = requests.post(f"{BASE_URL}/print", json=payload)
    print(response.text, end="")  # Print the colored text

# Function to create and display an ASCII graph
def create_graph(values):
    payload = {
        "values": values
    }
    response = requests.post(f"{BASE_URL}/graph", json=payload)
    print(response.text)  # Print the graph

# Main function to demonstrate functionality
def main():
    # Example 1: Print styled text
    print("Printing styled text:")
    print_styled_text("Hello, World!", color="green", bold=True, underline=True)
    print_styled_text("This is a test.", color="blue", bold=True)
    print_styled_text("Goodbye!", color="red")

    # Example 2: Create and display an ASCII graph
    print("\nCreating an ASCII graph:")
    values = [3.5, 7.2, 4.8, 6.1]
    create_graph(values)

if __name__ == '__main__':
    main()