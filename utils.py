"""
Utility functions for the chatbot
"""

import os
import platform

def clear_screen():
    """Clear the terminal screen based on the operating system"""
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')

def print_colored(text, color, return_string=False):
    """
    Print colored text in the terminal
    
    Args:
        text (str): Text to print
        color (str): Color to use
        return_string (bool): If True, return the colored string instead of printing
    """
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'yellow': '\033[93m',
        'magenta': '\033[95m',
        'end': '\033[0m'
    }
    
    colored_text = f"{colors.get(color, '')}{text}{colors['end']}"
    
    if return_string:
        return colored_text
    print(colored_text)
