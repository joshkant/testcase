from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    x_forwarded_for = request.headers.get('X-Forwarded-For', 'no header')
    return f'X-Forwarded-For: {x_forwarded_for}'
    proxy_headers = ['Via', 'X-Forwarded-For', 'Forwarded', 'Client-IP', 'Proxy-Connection', 'proxy_set_header']
    # for header in proxy_headers:
    #     if header in request.headers:
    #         return f"Request is proxypassed. Detected header: {header} and {request.headers.get(header)}"
    # return "Request is not proxypassed."
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
