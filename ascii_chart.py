import argparse

def generate_bar_chart(data):
    max_value = max(data.values())
    scale_factor = 50 / max_value if max_value > 50 else 1  # Scale to fit within 50 characters wide
    
    for label, value in data.items():
        bar_length = int(value * scale_factor)
        print(f"{label:10} | {'#' * bar_length} ({value})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render ASCII bar charts from data points.")
    parser.add_argument("--data", type=str, required=True, help="Comma-separated key:value pairs, e.g., 'A:10,B:20,C:15'")
    
    args = parser.parse_args()
    
    try:
        data_points = {k: int(v) for k, v in (pair.split(":") for pair in args.data.split(","))}
        generate_bar_chart(data_points)
    except ValueError:
        print("Error: Ensure data points are in the format 'label:value' with numeric values.")
