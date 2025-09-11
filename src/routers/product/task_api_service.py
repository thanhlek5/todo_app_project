from src.services.task_service import query_task_by_id 
from src.schema import Task, Subtask, Read_Task,Create_Task 
from fastapi.responses import JSONResponse 
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import session
from src.database import get_session
from json import json


router = APIRouter()

@router.get('/{user_id}/tasks',response_model=list[Read_Task])
def task_id_user_endpoint(user_id:int, db: session = Depends(get_session)):
    """
    endpoint truy task từ id người dùng.
    """
    is_task = query_task_by_id(
        db_session= db,
        user_id= user_id
    ) 
    if not is_task: 
        print(f'Người dùng chưa có task.')
    return 