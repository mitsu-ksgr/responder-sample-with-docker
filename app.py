#
# responder sample app
#
# see: https://responder.kennethreitz.org/en/latest/quickstart.html
#
import responder
import time


api = responder.API()

@api.route("/")
def hello_world(req, resp):
    resp.text = "Hello, FirstApp v2!"

@api.route("/hello/{who}")
def hello_to(req, resp, *, who):
    resp.text = f"Hello, {who}!"

@api.route("/hello/{who}/json")
def hello_json(req, resp, *, who):
    resp.media = {
        "hello": who
    }

@api.route("/hello/{who}/html")
def hello_html(req, resp, *, who):
    resp.html = api.template('hello.html', who=who)

@api.route("/416")
def teapot(req, resp):
    resp.status_code = api.status_code = api.status_codes.HTTP_416
    # ... or
    # resp.status_code = 416

@api.route("/pizza")
def pizza_pizza(req, resp):
    resp.headers['X-Pizza'] = '42'

@api.route("/incoming")
async def receive_incoming(req, resp):
    @api.background.task
    def process_data(data):
        """Just sleeps for three seconds, as a demo."""
        time.sleep(3)

    # Parse the incoming data as form-encoded.
    # Note: 'json' and 'yaml' formats are also automatically supported.
    data = await req.media()

    # Process the data (in the background)
    process_data(data)

    # Immediately respond that upload was successful.
    resp.media = {
        "success": True
    }

@api.route("/file")
async def upload_file(req, resp):
    @api.background.task
    def process_data(data):
        f = open('./{}'.format(data['file']['filename']), 'w')
        f.write(data['file']['contrent'].decode('utf-8'))
        f.close()

    data = await req.media(format='files')
    process_data(data)
    resp.media = {
        "success": True
    }

if __name__ == '__main__':
    api.run()

