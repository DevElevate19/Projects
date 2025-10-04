# TermiBot - AI Chat Interface

A Python-based terminal chat interface that provides access to multiple AI models including Gemini, Grok, Deepseek, and Qwen through a unified command-line interface.

## Overview

This project was created during the holidays of midsems as my midsems were a little messed up, so to get engaged in something productive, I developed this AI chat interface. The main challenge throughout development was implementing proper error handling for different types of API errors across multiple AI services.

## Features

- **Multi-Model Support**: Access to 4 different AI models:
  - Google Gemini (gemini-2.5-flash)
  - Grok (x-ai/grok-4-fast:free)
  - Deepseek (deepseek/deepseek-chat-v3.1:free)
  - Qwen (qwen/qwen3-235b-a22b:free)

- **Dual Operation Modes**:
  - Single model mode: Use one AI model throughout the session
  - Multi-model mode: Switch between models during conversation

- **Interactive CLI Commands**:
  - `/help` - Display available commands
  - `/list` - Show all available AI models
  - `/quit` - Exit the chat
  - `/change <model>` - Switch AI model (multi-model mode only)

- **Smart Response Processing**:
  - Qwen thinking filter: Automatically removes `<think>` tags from Qwen responses
  - Clean output formatting for better readability

- **API Integration**:
  - Google Gemini API integration
  - OpenRouter API for accessing Grok, Deepseek, and Qwen models

## Requirements

- Python 3.x
- `google-generativeai` library
- `openai` library
- Valid API keys for:
  - Google Gemini API
  - OpenRouter API (for other models)

## Installation

1. Install required dependencies:
   ```bash
   pip install google-generativeai openai
   ```

2. Get API keys:
   - Gemini API key from Google AI Studio
   - OpenRouter API key from OpenRouter.ai

3. Run the application:
   ```bash
   python termibot.py
   ```

## Usage

1. **Model Selection**: Choose your preferred AI model from the available options
2. **Mode Selection**: Enable or disable model switching capability
3. **API Setup**: Enter your API keys for the selected services
4. **Chat**: Start conversing with the AI models using natural language
5. **Commands**: Use slash commands for navigation and control

### Example Session
```
Choose AI model: gemini
Enable model switching (yes/no): yes
Gemini API key: your_gemini_key
Other Bots API key: your_openrouter_key

You: Hello, how are you?
Gemini: Hello! I'm doing well, thank you for asking...

You: /change grok
Switched to Grok

You: /quit
User left the chat
```

## Technical Implementation

- **Class-based Architecture**: `Ai_models` class handles all API interactions
- **Error Handling**: Try-catch blocks for API errors and network issues
- **Match-Case Logic**: Efficient command and model selection
- **Response Filtering**: Special handling for Qwen's thinking tokens
- **Session Management**: Persistent chat sessions with command support

## Known Issues & Limitations

### Major Issue: Error Handling
The primary challenge in this project was implementing comprehensive error handling for different API errors. **There could still be some errors that haven't been classified properly**, which will show "Connect to Internet" even if the actual issue is not related to internet connectivity, as this serves as the catch-all exception for the project.

### Other Limitations:
- Basic CLI interface without advanced formatting
- No conversation history persistence
- Limited error classification for edge cases
- No rate limiting implementation
- API keys stored in memory during session

## Error Types Handled

- **401 Errors**: Invalid API Key
- **429 Errors**: Token/Rate limit exhausted (Gemini only)
- **Network Errors**: Connection issues
- **Unclassified Errors**: Default to "Connect to Internet" message

## Future Improvements

- Implement comprehensive error classification system
- Add conversation history and export functionality
- Improve CLI interface with colors and better formatting
- Add configuration file support for API keys
- Implement rate limiting and usage tracking
- Add support for more AI models
- Better error messages for specific failure scenarios

## Development Challenges

1. **API Error Handling**: Different AI services return different error formats and codes
2. **Response Processing**: Handling various response formats across different models
3. **Session Management**: Maintaining state across model switches
4. **User Experience**: Creating intuitive command interface

## Technical Notes

- Uses OpenRouter API as a unified interface for multiple models
- Implements custom response filtering for Qwen's reasoning tokens
- Error handling uses nested try-catch blocks due to varying exception types
- Model switching maintains separate API key management

## Author

Created by **DevElevate19**

## Project Context

This project was developed during midsem holidays as a way to stay engaged and productive after a challenging exam period. The focus was on learning API integration, error handling, and creating a functional CLI application while dealing with the complexities of multiple AI service integrations.