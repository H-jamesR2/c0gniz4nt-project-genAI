from fastapi import FastAPI, Request
from db.session import engine, Base
from app.routes import task_routes
from app.models.task import Task  # Import Task model to trigger table creation
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize DB
logger.info(f"Database URL: {engine.url}")
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Tables created successfully.")
except Exception as e:
    logger.error(f"Error creating tables: {e}", exc_info=True)




app = FastAPI(title="Study Planner API")

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include Routes
app.include_router(task_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Study Planner API"}

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response