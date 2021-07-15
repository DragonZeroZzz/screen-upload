from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.datastructures import UploadFile
from fastapi.param_functions import Depends, File, Form
import uvicorn

app = FastAPI()

app.mount('/static',StaticFiles(directory="static"),name="static")


@app.post('/')
def post_screen(screen:UploadFile=File(...)):
    contents = screen.file.read()
    with open(f"./static/"+screen.filename,'wb') as f:
        f.write(contents)
    return 'none'

@app.post('/data')
async def post_data(request:Request):
    data = await request.json()
    print(data)
    return "data"

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0',port=5000)


