import instructor
import cohere
import sys
from pydantic import BaseModel
from typing import List
import json

sentence = sys.argv[1]

if not sentence:
    raise RuntimeError("Please provide a sentence as the first arugment to this script")

from pydantic import BaseModel
from typing import List, Tuple

class Color(BaseModel):
    name: str
    rgb: Tuple[int, int, int]

class Emotion(BaseModel):
    name: str
    color: List[Color]

class Response(BaseModel):
    emotion: Emotion
    original_sentence: str

client = instructor.from_cohere(cohere.Client())

task = f"""\
Given the following sentence, create a Response object that contains an Emotion object with an associated list of 5 Color objects to describe the emotion.

The Emotion name should be a real emotion, and only one word.

Sentence: {sentence}
"""
resp = client.chat.completions.create(
    model="command-r-plus",
    max_tokens=1024,

    messages=[
        {
            "role": "user",
            "content": task
        }
    ],
    response_model=Response
)

# Convert the Pydantic model to a dictionary and then serialize it to JSON with indentation
json_data = json.dumps(resp.dict(), indent=4)
print(json_data)

# Write to file
with open("emotions.json", "w") as write_file:
    write_file.write(json_data)
