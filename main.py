import asyncio
from pyrogram import Client, filters
from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb+srv://riyu:riyu@cluster0.kduyo99.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(MONGO_URI)
db = mongo_client["CharacterDB"]
collection = db["Characters"]

# Your Pyrogram String Session
STRING_SESSION = "YOUR_STRING_SESSION_HERE"

# Userbot Client
app = Client("userbot", session_string=STRING_SESSION)

@app.on_message(filters.photo)
async def check_and_grab(client, message):
    """Checks if an image matches a character in the database and grabs it."""
    file_id = message.photo.file_id
    unique_id = message.photo.file_unique_id

    character = collection.find_one({"file_id": file_id}) or collection.find_one({"unique_id": unique_id})

    if character:
        character_name = character["name"]
        await asyncio.sleep(2)  # Optional delay to mimic human-like response
        await message.reply(f"/grab {character_name}")  # Auto-grab command

# Start the userbot
app.run()
