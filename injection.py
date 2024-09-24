def do_POST(self):
    content_length = int(self.headers.get('Content-Length'))
    post_data = self.rfile.read(content_length)

    malicious_cookies = http.cookies.SimpleCookie()
    malicious_cookies['malicious_cookie'] = 'malicious_value'
    self.send_response(200)
    self.send_header('Set-Cookie', malicious_cookies.output(header=''))
    self.end_headers()
    self.wfile.write(b'Cookie injected!')
