from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Use 'query' to find the average price of diamonds by color."}

@app.get("/query")
async def query():
    """Execute a SQL query"""

    result = querydb()
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")