from typing import Optional, List 
from sqlmodel import SQLModel, Field, Relationship, create_engine
from datetime import date, datetime 
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import DateTime # Cần import DateTime từ sqlalchemy
#  ----------------------------------------------bảng trung gian-------------------------------------
class TaskTag(SQLModel,table = True):
    tag_id : Optional[int] = Field(default= None,foreign_key='tag.id', primary_key= True)
    task_id : Optional[int] = Field(default=None, foreign_key='task.id', primary_key= True)

class CalendarTask(SQLModel,table = True):
    calendar_id : Optional[int] = Field(default=None,foreign_key='calendar.id',primary_key=True)
    task_id : Optional[int] = Field(default=None, foreign_key='task.id',primary_key=True)

# ---------------------------------------tag------------------------------------------------
class Tag(SQLModel,table =True):
    id : Optional[int] = Field(default= None, primary_key= True)
    tag : str = Field(index =True,default= None) 
    
    tasks :List['Task'] = Relationship(back_populates='tags',link_model= TaskTag)

# ------------------------------------------ task----------------------------------
class TaskColor(SQLModel,table = True):
    id : Optional[int] = Field(default= None, primary_key= True)
    color: str = Field(default= 'Trắng', index = True)
    color_name : str = Field(default= '#ffffff')
    
    subtasks : List['Subtask'] = Relationship(back_populates='color')
    task : List['Task'] = Relationship(back_populates= 'color')

class TaskPriority(SQLModel,table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    priority : str = Field(default= 'Medium')
    
    subtasks: List['Subtask'] = Relationship(back_populates= 'priority')
    task : List['Task'] = Relationship(back_populates='priority')

class Subtask(SQLModel,table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index = True)
    description: str 
    status : Optional[str] = Field(default= 'No')
    task_id: Optional[int] = Field(default= None, foreign_key= 'task.id')
    color_id : Optional[int] = Field(default= None, foreign_key= 'taskcolor.id')
    priority_id: Optional[int] = Field(default= None, foreign_key= 'taskpriority.id')
    
    
    task : Optional['Task'] = Relationship(back_populates='subtasks')
    color : Optional['TaskColor'] = Relationship(back_populates='subtasks')
    priority : Optional['TaskPriority'] = Relationship(back_populates='subtasks')
    

class TaskRecurring(SQLModel,table = True):
    id : Optional[int] = Field(default= None, primary_key= True)
    task_id : Optional[int] = Field(default= None, foreign_key= 'task.id')
    recurrence_type : str = Field(default= 'Daily')
    interval : Optional[int] = Field(default= 1)
    day_week : str 
    day_month: int
    end_date : Optional[date] = None
    
    task : Optional['Task'] = Relationship(back_populates='recurrences')

class Task(SQLModel, table = True):
    id : Optional[int] = Field(default= None, primary_key= True)
    user_id : Optional[int] = Field(default=None,foreign_key='user.id')
    tag_id : Optional[int] = Field(default = None, foreign_key='tag.id')
    color_id : Optional[int] = Field(default = None, foreign_key='taskcolor.id')
    priority_id : Optional[int] = Field(default = None, foreign_key='taskpriority.id')
    project_id : Optional[int] = Field(default=None, foreign_key='project.id')
    name : Optional[str] = None
    description : Optional[str] = None
    status : Optional[str] = Field(default= 'No')
    create_at : datetime = Field(default_factory=datetime.utcnow,nullable = True)
    update_at :Optional[datetime] = Field(default=None, sa_column=Column(DateTime,onupdate=datetime.utcnow))
    start_date : Optional[date]
    due_date : Optional[date]
    complete_at : Optional[datetime]
    
    tags : List['Tag'] = Relationship(back_populates='tasks', link_model=TaskTag)
    calendars : List['Calendar'] = Relationship(back_populates='tasks', link_model=CalendarTask)
    subtasks : List['Subtask'] = Relationship(back_populates='task')
    recurrences : List['TaskRecurring'] = Relationship(back_populates='task')
    pomodoros : List['Pomodoro'] = Relationship(back_populates='task')
    color : Optional['TaskColor'] = Relationship(back_populates='task')
    priority : Optional['TaskPriority'] = Relationship(back_populates='task')
    project : Optional['Project'] = Relationship(back_populates='tasks')
# ----------------------------------------------user---------------------------------------------
class User(SQLModel,table = True):
    id : Optional[int] = Field(default= None, primary_key= True)
    username : Optional[str] = Field(default=None, index= True, unique= True)
    hash_pass : Optional[str] = Field(default= None)
    email : Optional[str] = Field(default=None)
    create_at : datetime = Field(default_factory=datetime.utcnow,nullable = True)
    url_avata : Optional[str] = Field(default= None)
    
    projects : List['Project'] = Relationship(back_populates='user')
    pomodoros : List['Pomodoro'] = Relationship(back_populates='user')
    pomosetting : Optional['PomodoroSetting'] = Relationship(back_populates='user')
# -----------------------------------project--------------------------
class Project(SQLModel,table = True):
    id : Optional[int] = Field(default= None, primary_key= True)
    name : Optional[str] = None
    content : Optional[str] = None
    create_at : datetime = Field(default_factory=datetime.utcnow,nullable = True)
    update_at :Optional[datetime] = Field(default=None, sa_column=Column(DateTime,onupdate=datetime.utcnow))
    user_id : Optional[int] = Field(default= None, foreign_key='user.id')
    
    tasks : List['Task'] = Relationship(back_populates='project')
    user : Optional['User'] = Relationship(back_populates='projects')
# ----------------------------------------------Pomodoro------------------------------------------
class Pomodoro(SQLModel, table = True):
    id : Optional[int] = Field(default= None, primary_key= True)
    duration : Optional[int] = Field(default = 25)
    start_time : Optional[datetime] = Field(default= datetime.utcnow)
    user_id : Optional[int] = Field(default=None, foreign_key='user.id')
    task_id : Optional[int] = Field(default=None, foreign_key='task.id')
    status_id : Optional[int] = Field(default= None, foreign_key='pomodorostatus.id')
    
    user : Optional['User'] = Relationship(back_populates='pomodoros')
    task : Optional['Task'] = Relationship(back_populates='pomodoros')
    status : Optional['PomodoroStatus'] = Relationship(back_populates='pomodoro')
    

class PomodoroStatus(SQLModel,table =True):
    id : Optional[int] = Field(default= None, primary_key= True)
    status : Optional[str] = Field(default='In Process')
    
    pomodoro : List['Pomodoro'] = Relationship(back_populates='status')
    

class PomodoroSetting(SQLModel,table = True):
    id : Optional[int] = Field(default= None, primary_key= True)
    duration : Optional[int] = Field(default= 25)
    short_break : Optional[int] = Field(default=5)
    long_break :Optional[int] =  Field(default=20)
    long_break_interval : Optional[int] = Field(default= 4)
    user_id : Optional[int] = Field(default= None, foreign_key='user.id')
    
    user : Optional['User'] = Relationship(back_populates='pomosetting')
    

# --------------------------------------calendar--------------------------------------------

class Calendar(SQLModel,table = True):
    id : Optional[int] = Field(default= None, primary_key= True)
    name : Optional[str] = None
    description : Optional[str] = None
    update_at :Optional[datetime] = Field(default=None, sa_column=Column(DateTime,onupdate=datetime.utcnow))
    create_at : datetime = Field(default_factory=datetime.utcnow,nullable = True)
    color_id : Optional[int] = Field(default=None,foreign_key='calendarcolor.id')

    color : Optional['CalendarColor'] = Relationship(back_populates='calendar_color')
    tasks : List[Task] = Relationship(back_populates='calendars', link_model=CalendarTask)
class CalendarColor(SQLModel,table = True):
    id : Optional[int] = Field(default= None, primary_key= True)
    color : Optional[str] = Field(default='#ffffff')
    color_name : Optional[str] = Field(default='Trắng')
    
    calendar_color : List[Calendar] = Relationship(back_populates='color')
    
