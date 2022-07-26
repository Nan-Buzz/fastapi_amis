from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request, Body
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from custom_response import ApiResponse
from pagnation import Page, Params, paginate
from schemas import Apple

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
statics = Jinja2Templates(directory="static") # 实例化 Jinja2 对象，并将文件夹路径设置为以 templates 命名的文件夹
# mount 的意思是挂载，它是特定路径中添加的完整"独立"应用程序，负责处理所有子路径
app.mount("/static", StaticFiles(directory="static"), name="static") # 第一个参数表示请求路径例如在static文件夹下有xyn.png图片，那么可以访问 http://127.0.0.1:8000/static/xyn.png，第二个参数是实际的目录，第三个参数是 fastapi内部使用的名称



def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/api/users/", response_model=schemas.User, response_class=ApiResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 创建用户
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/api/users/", response_model=Page[schemas.User], response_class=ApiResponse)
def read_users(db: Session = Depends(get_db), params: Params = Depends()):
    # 批量获取用户
    users = crud.get_users(db)
    return paginate(users, params)


@app.get("/api/users/{user_id}", response_model=schemas.User, response_class=ApiResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    # 获取单个用户信息
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete('/api/users/{user_id}', response_model=schemas.User, response_class=ApiResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    # 删除用户
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/api/users/{user_id}", response_model=schemas.User, response_class=ApiResponse)
def update_user(user_id: int, update_user: schemas.UserUpdate, db: Session = Depends(get_db)):
    # 更新某个用户
    updated_user = crud.update_user(db, user_id, update_user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.post('/api/load_data')
def cvddbbb(apple: Apple = Body(...,)):
    print(apple.editor)
    with open('./static/pages/change.js', 'w') as f:
        f.write(apple.editor)
    out = {
        "data": {
            "token": "cdcvdvnfjvdnjdnjbqajbjcdnjvd"
        },
        "msg": "成功",
        "status": 0
    }
    return out

@app.get('/login')
def evcvbcnllo(request: Request):
    return statics.TemplateResponse('login.html', {'request': request})


@app.get('/index')
def hevcvllo(request: Request):
    return statics.TemplateResponse('index.html', {'request': request})

@app.get('/api/login')
def hello():
    out = {
        "data": {
            "token": "cdcvdvnfjvdnjdnjbqajbjcdnjvd"
        },
        "msg": "成功",
        "status": 0
    }
    return out


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


