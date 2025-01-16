import json
from http.server import BaseHTTPRequestHandler
import os

# Load the student marks from the marks.json file
def load_marks():
    with open("marks.json", "r") as f:
        return json.load(f)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters from URL
        query = self.path.split('?')[-1]  # Get the part after '?'
        query_params = query.split('&')
        student_names = [param.split('=')[1] for param in query_params if param.startswith('name=')]

        marks = load_marks()
        result = {"marks": [marks.get(name, None) for name in student_names]}

        # Return JSON response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))
        return
