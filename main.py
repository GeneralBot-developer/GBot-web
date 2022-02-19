from sanic import Sanic
from sanic.response import file

app = Sanic(__name__)

app.static('/static', './static')
@app.route("/")
async def test(request):
    return await file('index.html')

if "__main__" == __name__:
    app.run(host = "0.0.0.0", port = 8080, auto_reload=True)