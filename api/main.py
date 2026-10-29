from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List
import crud, models, schemas
from database import SessionLocal,engine


app = FastAPI()
origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/api/clients/')
def read_clients(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)) -> List[schemas.Client]:
    result = crud.get_clients(db, skip=skip, limit=limit)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.post('/api/clients/')
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    # db_user = crud.get_user_by_email(db, email=user.email)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_client(db=db, client=client)
            
        
@app.get('/api/employees/')
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> List[schemas.Employee]:
    result = crud.get_employees(db, skip=skip, limit=limit)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# @app.route('/timeslots/', methods=['GET'])
# def timeslots():
#     employee  = request.args.get('id')
#     start  = request.args.get('start_time')
#     timeslots = []
#     conn = ApiSQLEngine.connect()
#     stmt = text("SELECT * FROM timeslots WHERE employee_id = :employee AND start_time >= :start")
#     result = conn.execute(stmt, {'employee': employee, 'start': start} )
#     if result:
#         for row in result.all():
#             timeslots.append({"id": row[0],"employee_id": row[1], "start_time": row[2].strftime('%m/%d/%y %I:%M %p'), "end_time": row[3].strftime('%m/%d/%y %I:%M:%S %p')})
#     return jsonify(timeslots)