from http.server import BaseHTTPRequestHandler
import json
import os
import urllib.request
import urllib.error


class handler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
            messages = data.get("messages", [])

            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if not api_key:
                self._send_json({"error": "API key not configured"}, status=500)
                return

            payload = json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 1024,
                "system": "You are a helpful, friendly assistant. Be concise and clear.",
                "messages": messages
            }).encode("utf-8")

            req = urllib.request.Request(
                "https://api.anthropic.com/v1/messages",
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": api_key,
                    "anthropic-version": "2023-06-01"
                },
                method="POST"
            )

            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                reply = result["content"][0]["text"]
                self._send_json({"reply": reply})

        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            self._send_json({"error": f"Claude API error: {error_body}"}, status=502)
        except Exception as e:
            self._send_json({"error": str(e)}, status=500)

    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self._send_cors_headers()
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass  # Suppress default logging
