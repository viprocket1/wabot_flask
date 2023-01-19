from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def incoming_message():
    # Get the message body
    body = request.values.get("Body", None)

    # Create a TwiML response
    resp = MessagingResponse()

    # Add a message to the response
    if body.lower() == "hello":
        resp.message("Hello! How can I help you today?")
    else:
        resp.message("I'm sorry, I didn't understand that.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)