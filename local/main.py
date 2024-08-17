import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from fastapi import FastAPI
from app.routes import route1, route2

app = FastAPI()

app.include_router(route1.router)
app.include_router(route2.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)