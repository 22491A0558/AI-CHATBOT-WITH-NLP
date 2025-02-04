#!/usr/bin/env python3
"""
AI Chatbot with NLP
Main entry point for the chatbot application
"""

import sys
from nlp_processor import NLPProcessor
from response_manager import ResponseManager
from utils import clear_screen, print_colored

def main():
    """Main function to run the chatbot"""
    try:
        clear_screen()
        print_colored("\n=== AI Chatbot with NLP ===\n", "blue")
        print_colored("Type 'quit' or 'exit' to end the conversation", "yellow")
        print_colored("Type 'help' for available commands\n", "yellow")

        nlp = NLPProcessor()
        response_manager = ResponseManager()

        context = {}  # Store conversation context

        while True:
            try:
                # Get user input
                user_input = input(print_colored("You: ", "green", return_string=True)).strip()

                if not user_input:
                    print_colored("Please type something!", "yellow")
                    continue

                # Check for commands
                if user_input.lower() in ['quit', 'exit']:
                    print_colored("\nGoodbye! Have a great day!", "blue")
                    break
                elif user_input.lower() == 'help':
                    print_colored("\nAvailable commands:", "cyan")
                    print_colored("- help: Show this help message", "cyan")
                    print_colored("- quit/exit: End the conversation", "cyan")
                    print_colored("Just type normally to chat with me!\n", "cyan")
                    continue

                # Process the input
                processed_input = nlp.process_text(user_input)

                # Generate response
                response = response_manager.generate_response(processed_input, context)

                # Update context
                context['last_input'] = user_input
                context['last_response'] = response

                # Display response
                print_colored(f"Bot: {response}", "cyan")

            except KeyboardInterrupt:
                print_colored("\nGoodbye! Have a great day!", "blue")
                break
            except Exception as e:
                print_colored(f"An error occurred: {str(e)}", "red")
                print_colored("Please try again!", "yellow")
                continue

    except Exception as e:
        print_colored(f"Fatal error: {str(e)}", "red")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print_colored(f"Fatal error: {str(e)}", "red")
        sys.exit(1)