from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    name = request.query_params.get('n', 'Bhai/Behen')
    return {"Hello": name}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
