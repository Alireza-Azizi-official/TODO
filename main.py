from bson import ObjectId
from fastapi import APIRouter, FastAPI, HTTPException, status

from config import collection
from models import Task
from schemas import individual_task, list_task
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="todo app")
router = APIRouter(prefix="/api", tags=["TODO"])


@router.get("/list")
async def todo_list():
    try:
        result = list (collection.find())
        if not result:
            raise Exception(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return list_task(result)
    except HTTPException as e:
        return f"there is a problem: {str(e)}"


@router.post("/new_task")
async def creat_task(task: Task):
    try:
        result = collection.insert_one(task.model_dump())
        new_task = collection.find_one({"_id": result.inserted_id})
        return individual_task(new_task)
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@router.get("/get_solo/{id}")
async def get_task(id: str):
    try:
        result = collection.find_one({"_id": ObjectId(id)})
        if not result:
            return Exception(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return individual_task(result)
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@router.put("/modify/{id}")
async def update_task(id: str, task: Task):
    try:
        result = collection.update_one(
        {"_id": ObjectId(id)}, {"$set": task.model_dump()})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        updated = collection.find_one({"_id": ObjectId(id)})
        return individual_task(updated)
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@router.delete("/soft_delete/{id}")
async def soft_delete(id: str):
    try:
        result = collection.update_one({"_id": ObjectId(id)}, {'$set': {'is_deleted': True}})
        if result.modified_count == 0 :
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return HTTPException(status_code=404, detail='task not found')
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@router.delete("/hard_delete/{id}")
async def hard_delete(id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return {"message": "deleted successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


app.include_router(router)
