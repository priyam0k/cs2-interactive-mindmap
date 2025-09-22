import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. Initialize your FastAPI app
app = FastAPI()

# 2. Add CORS Middleware
# This allows a web application from a different domain to request data from this API.
origins = [
    "*",  # Allow all origins for simplicity
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Load the mind map data from the cs2.json file
try:
    with open('cs2.json', 'r', encoding='utf-8') as f:
        mindmap_data = json.load(f)
except FileNotFoundError:
    mindmap_data = {"error": "cs2.json not found"}
except json.JSONDecodeError:
    mindmap_data = {"error": "Could not decode cs2.json"}


# 4. Create your API endpoint
@app.get("/api/mindmap")
def get_mindmap_data():
    """This endpoint returns the entire mind map data structure from cs2.json."""
    return mindmap_data

