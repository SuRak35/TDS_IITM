import json
from http.server import BaseHTTPRequestHandler
import os

# Load the JSON file
file_path = os.path.join(os.path.dirname(_file_), 'q-vercel-python.json')
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert the list of dictionaries into a dictionary for fast lookup
marks_dict = {entry["name"]: entry["marks"] for entry in data}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = self.path.split('?')[-1]
        params = dict(pair.split('=') for pair in query.split('&') if '=' in pair)

        # Extract names from query parameters
        names = params.get('name', '').split(',')

        # Fetch marks for the given names
        marks = [marks_dict.get(name, None) for name in names]

        # Respond with the marks
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode('utf-8'))
