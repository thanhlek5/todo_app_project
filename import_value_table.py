from sqlmodel import SQLModel, Session, create_engine 
from src.models.model import TaskColor,TaskPriority


color_1 = TaskColor(color = '#FFD1DC', color_name= 'Hồng phấn')
color_2 = TaskColor(color = '#FFDAB9', color_name= 'Cam đào')
color_3 = TaskColor(color = '#FFFACD', color_name= 'Vàng kem')
color_4 = TaskColor(color = '#BDECB6', color_name= 'Xanh bạc hà')
color_5 = TaskColor(color = '#ADD8E6', color_name= 'Xanh da trời')
color_6 = TaskColor(color = '#E6E6FA', color_name= 'Tím oải hương')
color_7 = TaskColor(color = '#F08080', color_name= 'Cam san hô nhạt')
color_8 = TaskColor(color = '#F5F5DC', color_name= 'Be')
color_9 = TaskColor(color = '#D3D3D3', color_name= 'Xám nhạt')
color_10 = TaskColor(color = '#CCCCFF', color_name= 'Xanh tím nhạt')

color_11 = TaskColor(color = '#FFFFFF', color_name= 'Trắng')


priority_1 = TaskPriority(priority='Ưu tiên cao', color_priority='#753C3D')
priority_2 = TaskPriority(priority='Ưu tiên vừa', color_priority='#e0911b')
priority_3 = TaskPriority(priority='Ưu tiên thấp', color_priority='#2147cf')
priority_4 = TaskPriority(priority='Không ưu tiên', color_priority='#8f929c')


engine = create_engine(r'sqlite:///D:\\todo_app\\Instance\\database.db')

with Session(engine) as session:
    session.add(color_1)
    session.add(color_2)
    session.add(color_3)
    session.add(color_4)
    session.add(color_5)
    session.add(color_6)
    session.add(color_7)
    session.add(color_8)
    session.add(color_9)
    session.add(color_10)
    session.add(priority_1)
    session.add(priority_2)
    session.add(priority_3)
    session.add(priority_4)
    session.add(color_11)
    session.commit() 
    print('Thêm màu và sự ưu tiên thành công.')