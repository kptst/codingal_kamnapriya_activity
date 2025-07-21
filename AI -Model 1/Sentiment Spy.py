import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()
print(f"{Fore.CYAN}WELCOME TO THE TEXTBLOB SENTIMENT ANALYSIS TOOL!{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"  # Default name

conversation_history = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a sentence and I will analyze the sentiment for you.")
print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, or {Fore.YELLOW}'exit'{Fore.CYAN} to QUIT.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter a sentence.{Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}Exiting sentiment spy. Farewell, Agent {user_name}!{Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}Conversation history cleared.{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if conversation_history:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f"{idx}. {color}{emoji} {text} (Polarity: {polarity:.2f}){Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}No conversation history available.{Style.RESET_ALL}")
        continue

    # Sentiment Analysis
    polarity = TextBlob(user_input)
