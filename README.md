# LLM Emotion & Color Parser

### A proof of concept for Craftwork Studios "Ancient Futures" project that uses LLM magic to parse emotion and colors from someone's confessed "secret"

Running this script with a sentence / secret:

`python src/claude_instructor_test/__init__.py --secret "I like dancing in the dark" --output-file ~/workspace/emotions.json`

will produce a JSON file at `~/workspace/emotions.json` with the following structure:

```.json
{
    "emotion": {
        "name": "Happiness",
        "color": [
            {
                "name": "Spring Green",
                "rgb": [
                    0,
                    255,
                    127
                ]
            },
            {
                "name": "Sunflower Yellow",
                "rgb": [
                    255,
                    215,
                    0
                ]
            },
            {
                "name": "Sky Blue",
                "rgb": [
                    118,
                    215,
                    255
                ]
            },
            {
                "name": "Rose Quartz",
                "rgb": [
                    223,
                    111,
                    139
                ]
            },
            {
                "name": "Violet",
                "rgb": [
                    146,
                    52,
                    146
                ]
            }
        ]
    },
    "original_sentence": "I believe I can communicate with plants and I have a secret garden where I talk to rare species to help them grow."
}
```



## Set up PC

1. Install python 3.12.3: https://www.python.org/downloads/release/python-3123/

2. Update your PATH to make sure this version runs when you run 

   ```
   python
   ```

    from the command prompt

   - In windows search, `Edit the system variables`
   - Click `Environment Variables` in the `Advanced` tab
   - Edit `path`
   - Add `C:\\Users\\USERNAME\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\`
   - Add `C:\\Users\\USERNAME\\AppData\\Local\\Programs\\Python\\Python312\\`

3. Install Rust (needed for certain dependencies that this project uses): https://www.rust-lang.org/tools/install -- you'll need to use the installer

4. cd into directory

   - `cd C:\\ancient_futures\\LLM-emotion-color-parser`

5. Run the following once: `python -m venv C:\\ancient_futures\\LLM-emotion-color-parser\\venv`

6. Inside the project directory, run `venv\\Scripts\\activate`

7. Run the following once: Inside the project directory, run `pdm install`

8. Inside the project directory run `set CO_API_KEY=<your api key>`



## Set up MAC

1. Install [pdm](https://pdm-project.org/en/latest/#__tabbed_1_2)
--> This is a tool like npm for managing dependencies since default dependency management in Python is terrible
1. Run `pdm install` to install dependencies needed for this project to run
1. Copy `.envrc.sample` to `.envrc` and fill out the value for the Cohere API key (you'll have to make an account but its free to use their API)
1. Install [`direnv`](https://direnv.net/docs/installation.html).
--> This is a tool that helps manage envrionemnt variables set per project.
1. Run `direnv allow` in your shell to set the necessary env variables in your environment
1. Run the python script using the command above
