import uvicorn
from apps import apps
from pub import pub

if __name__ == "__main__":
    uvicorn.run(pub, host='localhost', port=8883)

