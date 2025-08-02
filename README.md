# ChatBot - Python Tkinter GUI Application

A friendly chatbot application built with Python and Tkinter GUI library. The chatbot uses hardcoded responses and provides an interactive chat interface.

## Features

- **Modern GUI Interface**: Clean and user-friendly Tkinter-based interface
- **Hardcoded Responses**: No API dependencies - all responses are built-in
- **Real-time Chat**: Instant responses with timestamps
- **Math Calculator**: Basic mathematical operations (+, -, *, /)
- **Time & Date**: Current time and date information
- **Jokes & Entertainment**: Built-in jokes and fun responses
- **Conversation History**: Scrollable chat history
- **Clear Chat**: Option to clear conversation history

## Capabilities

The chatbot can handle various types of conversations:

- **Greetings**: Hi, hello, hey, greetings
- **Personal Questions**: How are you, what's your name
- **Time & Date**: Current time and date queries
- **Math Operations**: Basic calculations
- **Jokes**: Funny responses and humor
- **Help**: Information about capabilities
- **Weather**: Friendly responses about weather
- **Goodbyes**: Farewell messages
- **Thanks**: Appreciation responses

## Installation

1. **Prerequisites**: Python 3.x (tkinter is included with Python)
2. **Clone or download** the project files
3. **Run the application**:
   ```bash
   python chatbot.py
   ```

## Usage

1. **Launch the application** by running `python chatbot.py`
2. **Type your message** in the input field at the bottom
3. **Press Enter** or click the "Send" button to send your message
4. **View responses** in the chat area above
5. **Clear chat** using the "Clear Chat" button when needed

## Example Conversations

- "Hello" → Friendly greeting response
- "What time is it?" → Current time
- "Calculate 5 + 3" → Math result
- "Tell me a joke" → Funny response
- "What can you do?" → List of capabilities
- "Goodbye" → Farewell message

## File Structure

```
├── chatbot.py          # Main application file
├── requirements.txt    # Dependencies
└── README.md          # This file
```

## Technical Details

- **GUI Framework**: Tkinter
- **Pattern Matching**: Regular expressions for response selection
- **Math Engine**: Built-in calculation capabilities
- **Timestamp**: Real-time message timestamps
- **Responsive Design**: Modern UI with proper styling

## Customization

You can easily customize the chatbot by:

1. **Adding new responses**: Modify the `responses` dictionary in the `Chatbot` class
2. **Changing patterns**: Update regex patterns for different triggers
3. **Modifying UI**: Adjust colors, fonts, and layout in the `ChatbotGUI` class
4. **Adding features**: Extend functionality with new capabilities

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## License

This project is open source and available under the MIT License.
