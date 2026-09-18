"""
Vercel serverless entry — thin wrapper around web_api.handle
"""
from http.server import BaseHTTPRequestHandler
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

try:
    from src.interfaces.web_api import handle
except ImportError:
    def handle(req):
        return {"error": "src not found", "status": "degraded"}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._respond({"status": "ok", "version": "2.6", "action": "status"})

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b"{}"
        try:
            req = json.loads(body.decode() or "{}")
        except Exception:
            req = {}
        result = handle(req)
        self._respond(result)

    def _respond(self, data):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
