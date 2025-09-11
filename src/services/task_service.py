from sqlmodel import Session,select
from src.models.model import Subtask, Task


# ---------------------------------------------------------task-----------------------------------------------------------
def query_task_by_id(db_session : Session,user_id: int) -> list[Task]:
    """
    Lấy tất cả các task của người dùng bằng id.
    """
    statement= select(Task).where(Task.user_id == user_id)
    tasks = db_session.exec(statement).all()
    return tasks


def query_task_by_name(db_session: Session, taskname: str)->list[Task]:
    """
    Lấy task bằng tên task.
    """
    statement = select(Task).where(Task.name == taskname)
    tasks = db_session.exec(statement).all()
    return tasks

def query_task_by_project_id(db_session: Session, id_project:int) -> list[Task]:
    """
    Lấy task từ project
    """
    statement = select(Task).where(Task.project_id == id_project)
    tasks = db_session.exec(statement).all()
    return tasks

def create_task(db_session : Session, name_task: str, id_user: int, id_color: int = 11, id_project : int = None, description :str = None, id_priority: int = 2)-> Task:
    """
    Tạo task mới vào table.
    """
    
    new_task = Task(user_id=id_user,name= name_task,color_id= id_color, project_id= id_project, description= description, priority_id = id_priority)
    db_session.add(new_task)
    db_session.commit()
    db_session.refresh(new_task)
    return new_task
# ----------------------------------------------------------------subtask---------------------------------------------------------

def query_sub_task(db_session: Session, task_id: int)-> list[Subtask]:
    """  
    Hàm dùng để truy xuất các task con của task mẹ.
    """
    
    statemnet = select(Subtask).where(Subtask.task_id == task_id)
    subtasks = db_session.exec(statemnet).all()
    
    return subtasks 

def create_subtask(db_session : Session, id_task:int, name_subtask: str, description: str = None, id_priority : int = 2, id_color: int = 11 )->Subtask:
    """
    Hàm tạo subtask
    """
    new_sub = Subtask(name=name_subtask,description=description, task_id= id_task, priority_id= id_priority,color_id= id_color )
    db_session.add(new_sub)
    db_session.commit()
    db_session.refresh(new_sub)
    return new_sub