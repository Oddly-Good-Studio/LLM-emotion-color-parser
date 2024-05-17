import instructor
import cohere
import sys
from pydantic import BaseModel
from typing import List
import json
import argparse

# Parse command line arguments for output file
parser = argparse.ArgumentParser()
parser.add_argument('--output-file', type=str, required=True, help="The output file path for the emotions data.")
parser.add_argument('--secret', type=str, required=True, help="Your secret")
args = parser.parse_args()

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

client = instructor.from_cohere(cohere.Client())

task = f"""\
Given the following sentence, create a Response object that contains an Emotion object with an associated list of 5 Color objects to describe the emotion.

The Emotion name should be a real emotion, and only one word.

Sentence: {args.secret}
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

final_response = resp.dict()
final_response['original_sentence'] = args.secret

# Convert the Pydantic model to a dictionary and then serialize it to JSON with indentation
json_data = json.dumps(final_response, indent=4)
print(json_data)

# Write to file
with open(args.output_file, "w") as write_file:
    write_file.write(json_data)
