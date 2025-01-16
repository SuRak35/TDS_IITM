import json
from http.server import BaseHTTPRequestHandler
import os

# Load the JSON data
file_path = os.path.join(os.path.dirname(_file_), 'q-vercel-python.json')
with open(file_path) as f:
    data = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = self.path.split('?')[-1]
        params = dict(qc.split('=') for qc in query.split('&') if '=' in qc)

        # Extract the names from the query
        names = params.get('name')
        if names:
            names = names.split(',')

        # Find marks for the given names
        marks = [data.get(name, 0) for name in names]

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"marks": marks}).encode('utf-8'))
