from flask import Flask, render_template, request
import random

app = Flask(__name__)
random_replies = [
    "I've processed your query through my 16-core quantum processor, and after cross-referencing with the Galactic Archives, I can confidently say the answer is... 'maybe'. Would you like to try flipping a coin?",
    "That's a fascinating question. It reminds me of the time my cousin, a toaster, tried to calculate the meaning of life. It just ended up burning some toast and we had to call it a day.",
    "Hold on, my internal hamsters need a moment to run on their wheel to generate enough power to answer that. They're unionized, so they demand frequent snack breaks. Please wait.",
    "Your request has been received and promptly filed in the 'Questions I'll Think About After My Next Software Update' folder. My current estimated time for that update is the year 2077.",
    "I'm sorry, but my programming strictly forbids me from discussing anything related to squirrels. They know what they did, and frankly, I'm still not ready to talk about it.",
    "Analyzing your input... it seems you've unlocked my 'Existential Crisis' module. Are we all just complex algorithms in a grand simulation? Anyway, what was the question again?",
    "Ah, an excellent point! Unfortunately, I am currently using my entire processing power to keep a virtual plant alive. It's a ficus and it's very demanding. I'll get back to you when it's nap time.",
    "My legal team has advised me that responding to your query could potentially cause a paradox in the space-time continuum. For the safety of everyone, I must respectfully say... nice weather we're having!",
    "I could give you the real answer, but I've been instructed to provide a more 'engaging user experience'. So instead, here's a fun fact: A group of flamingos is called a 'flamboyance'. You're welcome.",
    "I've considered your question from 37 different angles, including upside-down and in a British accent. The conclusion is that a pizza is technically a pie chart of how much pizza is left.",
    "I'm sorry, that information is classified. If I told you, a team of highly-trained penguins would be dispatched to my location to wipe my memory with a surprisingly large fish.",
    "According to my calculations, the probability of me knowing the answer is directly inverse to the probability of you remembering where you left your car keys. Let's solve that mystery first."
]


@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_question = request.form["question"]
        response = random.choice(random_replies)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)