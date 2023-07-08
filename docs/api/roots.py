import json 
import random 
from http.server import BaseHTTPRequestHandler 
from os.path import dirname, abspath, join
from typing import Any

dir = dirname(abspath(__file__))

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        with open(join(dir, '..', 'data', 'roots.txt'), 'r', encoding='utf-8') as file:
            lines = file.readlines()
            random_line = random.choice(lines)
            response = {
                'line': random_line.strip()
            }
            response_json = json.dumps(response, ensure_ascii=False)

            self.wfile.write(response_json.encode('utf-8'))
        return