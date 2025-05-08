yoo 

generate a gemini api key from 

https://aistudio.google.com/

then make a .env file in the root of this project and add these 2 lines 

GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE

then install uv in your system.. i think you are in windows only so
run the first command from here in powershell administrator terminal

 https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2

then in new terminal check if uv is installed by typing uv in the terminal 

if it is installed open the git cloned folder again and type uv sync (make sure the pyproject.toml is in the same path)

great 

now just type adk web and you can see the project work 
