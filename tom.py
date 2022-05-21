import random
import discord
from transformers import pipeline
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

client = discord.Client(status=discord.Status.online, activity=discord.Game(name="Epok Bus Sim 2"))

@client.event
async def on_ready():
    print("I'm ready :D")

    # Sentences were suggested by these people:
    # Tha Muffin
    # hellory4n (me :D )
    # Rubi
    # RThreeFive
    sentences = [
        "Pizza",
        "Walmart is an epok place",
        "Mexico is Mexico",
        "Windows 11 brings you closer to the thing you love.",
        "I have commited several warcrimes in Winchestertonville, USA",
        "I like to eat my chair",
        "What is apple"
    ]

    prompt = random.choice(sentences)
    res = generator(prompt, max_length=100, do_sample=True, temperature=0.9)
    message = res[0]['generated_text']

    send_message_on = client.get_channel() # Put a channel id here
    await send_message_on.send(message)

client.run("token")
