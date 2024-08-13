import google.generativeai as genai
import telepot
from telepot.loop import MessageLoop

# API keys
TeleGemini_API_key = '<BOT_API_TOKEN>'
gemini_API_key = '<GEMINI_API_TOKEN>'

# Configure Gemini
genai.configure(api_key=gemini_API_key)
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

# Bot instance
TeleGemini = telepot.Bot(TeleGemini_API_key)

# Function to generate a response using Gemini
def _generate_response(prompt: str) -> str:
    response = model.generate_content(prompt)
    try:
        textualResponse = response.text
        return textualResponse
    except(ValueError) :
        return "Sorry, I could not generate a response."

# Function to display the help message
def _display_help() -> str:
    return '''
    This is TeleGemini (Telegram and Google Gemini get it?). You can discuss with it like you would with any other AI language model. This bot is coded in Python and is currently using the Gemini 1.5 Flash model. The code will be available on my GitHub https://github.com/AnotherMedo (All API keys were hidden... I think. So don't try to get frisky with me >:|)
    This is a help message that can be displayed again with /help
    '''

# Function to handle incoming messages
def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'].startswith('/help'):
            TeleGemini.sendMessage(chat_id, _display_help())
        else:
            prompt = msg['text']
            response = _generate_response(prompt)
            TeleGemini.sendMessage(chat_id, response)

# Start the message loop to handle incoming messages
MessageLoop(TeleGemini, handle_message).run_as_thread()

# Keep the program running
print('TeleGemini is listening...')
while True:
    pass

