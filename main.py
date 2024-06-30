#code

from flask import Flask, request, jsonify, send_from_directory

import openai

app = Flask(__name__, static_folder='static')

# Set your OpenAI API key
openai.api_key = "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"

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        user_input = data['message']

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        chatbot_response = response['choices'][0]['message']['content'].strip()

        return jsonify({'response': chatbot_response})

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error during API request: {e}")
        return jsonify({'error': 'Failed to process your request'}), 500

if __name__ == '__main__':
    app.run(debug=True)
