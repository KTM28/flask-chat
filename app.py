import os
from flask import Flask, redirect

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"]=True 
messages = []

#this will add username and messages to the messages =[] 
def add_messages(username, message):
    """Add messages to the `messages` list"""
    messages.append(f"{username}: {message}")

def get_all_messages():
    """Get all of the messages and seperate them with a `br`"""
    return "<br>".join(messages)

#Main page
@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use: /USERNAME/MESSAGE"

#welcome page
@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return f"<h1>Welcome, {username}</h1>{get_all_messages()}"

#new message page
@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=os.environ.get("PORT"),
    debug=True)