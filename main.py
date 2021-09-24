from fastapi import FastAPI
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "similarity",
        "description": "Finds the similarity between 2 sentences using their word vectors.",
    },
    {
        "name": "tokenize",
        "description": "Takes in word, sentences e.t.c and return lexical infromation about each of words. e.g Nouns, Abstract Nouns, Co-ordinating conjunction.",
    },
    {
        "name": "synonyms",
        "description": "Takes in a word or a group of words separated by commas and return a list of English language synonyms for the words.",
    },
    {
        "name": "antonyms",
        "description": "Takes in a word or a group of words separated by commas and return a list of English language antonyms for the words.",
    },
    {
        "name": "tospeech",
        "description": "Takes in a string and returns an audio file of the text.",
    },
]

app = FastAPI(
    title="Skana",
    description="Form validation API for a Jamstack application",
    openapi_tags=tags_metadata,
)


@app.get("/")
def home():
    return "Welcome here"
