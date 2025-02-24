import argparse
from colorama import Fore, Style, init

def render_text(text, color, styles):
    init(autoreset=True)
    
    color_map = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }
    
    style_map = {
        "bold": Style.BRIGHT,
        "dim": Style.DIM,
        "underline": '\033[4m',
        "normal": Style.NORMAL
    }
    
    chosen_color = color_map.get(color.lower(), Fore.RESET)
    chosen_styles = "".join([style_map.get(s.lower(), "") for s in styles])
    
    print(f"{chosen_styles}{chosen_color}{text}{Style.RESET_ALL}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render text with colors and styles.")
    parser.add_argument("--text", type=str, required=True, help="Text to display")
    parser.add_argument("--color", type=str, choices=["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"], required=True, help="Text color")
    parser.add_argument("--style", type=str, nargs="*", choices=["bold", "dim", "underline", "normal"], default=[], help="Text styles")
    
    args = parser.parse_args()
    render_text(args.text, args.color, args.style)
