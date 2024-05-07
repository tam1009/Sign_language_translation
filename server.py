import sys
import uvicorn
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from fastapi import FastAPI
from routes.base import router

app = FastAPI()

app.include_router(router)



#if __name__ == " __main__ ":
#   uvicorn.run("app:app ", host =" 0.0.0.0 ", port =8000 , reload = True )