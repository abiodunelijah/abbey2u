import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import datetime
import json
import re

class Chatbot:
    def __init__(self):
        self.responses = {
            # Greetings
            r'\b(hi|hello|hey|greetings)\b': [
                "Hello! How can I help you today?",
                "Hi there! Nice to meet you!",
                "Hey! What can I do for you?",
                "Greetings! How are you doing?"
            ],
            
            # How are you
            r'\b(how are you|how do you do|are you ok)\b': [
                "I'm doing great, thank you for asking! How about you?",
                "I'm functioning perfectly! How's your day going?",
                "All systems operational! How's your day going?",
                "I'm good, thanks! How are you feeling today?"
            ],
            
            # Name
            r'\b(what is your name|who are you|your name)\b': [
                "My name is ChatBot! Nice to meet you!",
                "I'm ChatBot, your friendly AI assistant!",
                "You can call me ChatBot! What's your name?",
                "I'm ChatBot! How can I assist you today?"
            ],
            
            # Weather
            r'\b(weather|temperature|hot|cold|sunny|rainy)\b': [
                "I can't check real-time weather, but I hope it's nice where you are!",
                "Weather forecasting isn't my specialty, but I'm sure it's lovely!",
                "I don't have access to weather data, but I hope you're enjoying your day!",
                "Weather updates aren't available, but I'm here for other questions!"
            ],
            
            # Time
            r'\b(time|what time|current time|clock)\b': [
                f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}",
                f"It's {datetime.datetime.now().strftime('%I:%M %p')} right now",
                f"Current time: {datetime.datetime.now().strftime('%H:%M')}",
                f"The time is {datetime.datetime.now().strftime('%I:%M:%S %p')}"
            ],
            
            # Date
            r'\b(date|today|what day|calendar)\b': [
                f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')}",
                f"It's {datetime.datetime.now().strftime('%B %d, %Y')} today",
                f"Today's date is {datetime.datetime.now().strftime('%m/%d/%Y')}",
                f"The date today is {datetime.datetime.now().strftime('%A, %d %B %Y')}"
            ],
            
            # Help
            r'\b(help|what can you do|capabilities|features)\b': [
                "I can help you with:\n• Greetings and conversations\n• Time and date information\n• Basic questions and answers\n• Simple calculations\n• General knowledge questions\n• Entertainment and jokes",
                "Here's what I can do:\n• Chat and have conversations\n• Tell you the time and date\n• Answer general questions\n• Perform basic math\n• Share interesting facts\n• Tell jokes and stories",
                "My capabilities include:\n• Friendly conversations\n• Time and date queries\n• General knowledge\n• Basic calculations\n• Fun facts and trivia\n• Entertainment options"
            ],
            
            # Math
            r'\b(calculate|math|add|subtract|multiply|divide|plus|minus|times)\b': [
                "I can help with basic math! Try asking something like 'calculate 5 + 3' or 'what is 10 * 2'",
                "Sure! I can do basic calculations. Try: 'calculate 15 - 7' or 'what is 8 * 4'",
                "I'm ready for math! Examples: 'calculate 20 / 4' or 'what is 12 + 8'"
            ],
            
            # Jokes
            r'\b(joke|funny|humor|laugh)\b': [
                "Why don't scientists trust atoms? Because they make up everything! 😄",
                "What do you call a fake noodle? An impasta! 😂",
                "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
                "What do you call a bear with no teeth? A gummy bear! 🐻",
                "Why don't eggs tell jokes? They'd crack each other up! 🥚"
            ],
            
            # Goodbye
            r'\b(bye|goodbye|see you|farewell|exit|quit)\b': [
                "Goodbye! It was nice chatting with you! 👋",
                "See you later! Have a great day! 😊",
                "Take care! Come back anytime! 👋",
                "Goodbye! Thanks for the conversation! 😄"
            ],
            
            # Thanks
            r'\b(thank you|thanks|thx|appreciate)\b': [
                "You're welcome! I'm happy to help! 😊",
                "No problem at all! Anytime! 😄",
                "My pleasure! Feel free to ask more questions! 😊",
                "You're very welcome! I enjoy our conversations! 😄"
            ],
            
            # Default responses
            r'.*': [
                "That's interesting! Tell me more about that.",
                "I'm not sure I understand. Could you rephrase that?",
                "Interesting question! What made you think of that?",
                "I'd love to hear more about your thoughts on this.",
                "That's a good point! What else would you like to discuss?",
                "I'm here to chat! What's on your mind?",
                "That's fascinating! How do you feel about that?",
                "I'm curious to hear more! What's your perspective?"
            ]
        }
        
        # Math patterns for calculations
        self.math_patterns = [
            r'calculate\s+(\d+)\s*([+\-*/])\s*(\d+)',
            r'what\s+is\s+(\d+)\s*([+\-*/])\s*(\d+)',
            r'(\d+)\s*([+\-*/])\s*(\d+)'
        ]

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Check for math calculations first
        for pattern in self.math_patterns:
            match = re.search(pattern, user_input)
            if match:
                try:
                    num1 = float(match.group(1))
                    operator = match.group(2)
                    num2 = float(match.group(3))
                    
                    if operator == '+':
                        result = num1 + num2
                    elif operator == '-':
                        result = num1 - num2
                    elif operator == '*':
                        result = num1 * num2
                    elif operator == '/':
                        if num2 == 0:
                            return "Sorry, I can't divide by zero!"
                        result = num1 / num2
                    else:
                        continue
                    
                    return f"The result is: {result}"
                except:
                    continue
        
        # Check for pattern matches
        for pattern, responses in self.responses.items():
            if re.search(pattern, user_input):
                import random
                return random.choice(responses)
        
        # If no pattern matches, return a default response
        return random.choice(self.responses[r'.*'])

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot - Your Friendly AI Assistant")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Initialize chatbot
        self.chatbot = Chatbot()
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            self.main_frame,
            text="🤖 ChatBot Assistant",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        title_label.pack(pady=(0, 20))
        
        # Chat display area
        self.chat_frame = tk.Frame(self.main_frame, bg="white", relief=tk.RAISED, bd=2)
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=(0, 0, 0, 10))
        
        # Chat text area
        self.chat_area = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg="white",
            fg="#2c3e50",
            state=tk.DISABLED,
            padx=10,
            pady=10
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Input frame
        self.input_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.input_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Input field
        self.input_field = tk.Entry(
            self.input_frame,
            font=("Arial", 12),
            bg="white",
            fg="#2c3e50",
            relief=tk.SOLID,
            bd=2
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.input_field.bind("<Return>", self.send_message)
        self.input_field.focus()
        
        # Send button
        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            font=("Arial", 11, "bold"),
            bg="#3498db",
            fg="white",
            relief=tk.FLAT,
            command=self.send_message,
            width=10
        )
        self.send_button.pack(side=tk.RIGHT)
        
        # Clear button
        self.clear_button = tk.Button(
            self.main_frame,
            text="Clear Chat",
            font=("Arial", 10),
            bg="#e74c3c",
            fg="white",
            relief=tk.FLAT,
            command=self.clear_chat,
            width=12
        )
        self.clear_button.pack(pady=(10, 0))
        
        # Welcome message
        self.display_message("ChatBot", "Hello! I'm your friendly AI assistant. How can I help you today? 😊", "bot")
        
    def send_message(self, event=None):
        user_message = self.input_field.get().strip()
        if user_message:
            # Display user message
            self.display_message("You", user_message, "user")
            
            # Get bot response
            bot_response = self.chatbot.get_response(user_message)
            self.display_message("ChatBot", bot_response, "bot")
            
            # Clear input field
            self.input_field.delete(0, tk.END)
    
    def display_message(self, sender, message, msg_type):
        self.chat_area.config(state=tk.NORMAL)
        
        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        # Format message based on type
        if msg_type == "user":
            self.chat_area.insert(tk.END, f"\n[{timestamp}] {sender}: {message}\n", "user")
        else:
            self.chat_area.insert(tk.END, f"\n[{timestamp}] {sender}: {message}\n", "bot")
        
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)
        
        # Configure tags for different message types
        self.chat_area.tag_config("user", foreground="#2980b9", font=("Arial", 11, "bold"))
        self.chat_area.tag_config("bot", foreground="#27ae60", font=("Arial", 11, "bold"))
    
    def clear_chat(self):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state=tk.DISABLED)
        self.display_message("ChatBot", "Chat cleared! How can I help you? 😊", "bot")

def main():
    root = tk.Tk()
    app = ChatbotGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()