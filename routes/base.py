from fastapi import APIRouter
from .predict import router as transtext_route

router = APIRouter ()
router.include_router (transtext_route, prefix ="/yolo")