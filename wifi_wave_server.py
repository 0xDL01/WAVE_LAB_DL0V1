#!/usr/bin/env python3
import http.server
import socketserver
import json
import subprocess
import time

PORT = 5050

AIRPORT_PATH = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"


def get_wifi_metrics():
    """
    Returns (rssi, noise, snr) or (None, None, None) if not connected / error.
    RSSI & noise are in dBm (negative numbers).
    """
    try:
        output = subprocess.check_output([AIRPORT_PATH, "-I"]).decode("utf-8", "ignore")
    except Exception:
        return None, None, None

    rssi = None
    noise = None

    for line in output.splitlines():
        line = line.strip()
        if line.startswith("agrCtlRSSI:"):
            # e.g. "agrCtlRSSI: -57"
            try:
                rssi = int(line.split(":")[1].strip())
            except ValueError:
                pass
        elif line.startswith("agrCtlNoise:"):
            # e.g. "agrCtlNoise: -90"
            try:
                noise = int(line.split(":")[1].strip())
            except ValueError:
                pass

    snr = None
    if rssi is not None and noise is not None:
        snr = rssi - noise

    return rssi, noise, snr


class WifiHandler(http.server.BaseHTTPRequestHandler):
    def _send_json(self, obj, status=200):
        data = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        # allow browser from other port
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path.startswith("/wifi"):
            rssi, noise, snr = get_wifi_metrics()
            now = time.time()

            resp = {
                "timestamp": now,
                "rssi": rssi,
                "noise": noise,
                "snr": snr,
            }
            self._send_json(resp)
        else:
            self._send_json({"error": "not found"}, status=404)

    def log_message(self, format, *args):
        # keep server output clean
        return


if __name__ == "__main__":
    print(f"[wifi_wave_server] Starting on http://localhost:{PORT}/wifi")
    with socketserver.TCPServer(("localhost", PORT), WifiHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server.")
