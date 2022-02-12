from datetime import datetime
from http.server import BaseHTTPRequestHandler
import datetime as dt
import numpy as np
import pytz


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        days_off = 1
        start = dt.date(2022, 2, 1)
        end = dt.datetime.now(pytz.timezone('Africa/Johannesburg')).date()
        days_since = np.busday_count(start, end) - days_off

        message = f"{days_since}"
        self.wfile.write(message.encode())
        return
