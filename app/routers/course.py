from fastapi import HTTPException, status, Depends, APIRouter
from .. import models, schemas
from sqlalchemy.orm import Session
from ..database import get_db
from .. import oauth2




# while True:
#     try:
#         conn = psycopg2.connect(
#             host = 'localhost',
#             database = 'postgres',
#             user = 'postgres',
#             password = '1009',
#             cursor_factory= RealDictCursor
#         )
#         cursor = conn.cursor()
#         print('Database connected successfully')
#         break
#     except Exception as e:
#         print('Error connecting to databse:',e)
#         time.sleep(2)


router = APIRouter()

# models.Base.metadata.create_all(bind=engine)

# @app.get("/course")
# def get_courses():
#     cursor.execute("SELECT * FROM course;")
#     courses = cursor.fetchall()  # list of dicts
#     return {"courses": courses}

#get course data using sqlalchemy
@router.get('/coursealchemy', response_model=list[schemas.CourseResponse])
def course(db:Session = Depends(get_db), current_user:models.User=Depends(oauth2.get_current_user)) :
    course = db.query(models.Course).all()
    return course


# @app.post("/post")
# def add_new_post(post: schemas.Course):
#     cursor.execute("""INSERT INTO course(name, instructor, duration) VALUES(%s, %s, %s) RETURNING*""" ,(post.name, post.instructor, post.duration))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return{'data':post}

#add new course using sqlalchemy
@router.post('/course/create', response_model= schemas.CourseResponse)
def create_course(course:schemas.Course, db: Session = Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    course_data = course.model_dump()
    course_data['website']=str(course_data['website'])
    new_course = models.Course(**course_data,creator_id = current_user.id)

    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

# @app.get("/course/{id}")
# def get_course_by_id(id:int):
#     cursor.execute("""SELECT * FROM course WHERE id = %s""", (str(id)))
#     course = cursor.fetchone()
#     if not course:
#         raise HTTPException(
#             status_code= status.HTTP_404_NOT_FOUND,
#             detail= f"Course with id:{id} was not found"
#         )
#     return {"course_ddetail": course}

#get course data by id using sqlalchemy
@router.get("/course/{id}", response_model=schemas.CourseResponse)
def get_course_by_id(id:int, db:Session = Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    course = db.query(models.Course).filter(models.Course.id == id).first()
    if not course:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"Course with id:{id} was not found"
        )
    return course


# @app.delete("/course/delete/{id}") #status_code= status.HTTP_204_NO_CONTENT)
# def delete_course_by_id(id:int):
#     cursor.execute("""DELETE FROM course WHERE id = %s RETURNING * """, ((str(id))))
#     deleted_course = cursor.fetchone()
#     conn.commit()
#     if not deleted_course:
#         raise HTTPException(
#             status_code= status.HTTP_404_NOT_FOUND,
#             detail= f"Course with id:{id} does not exist"
#         )
#     return {
#         "message": "course deleted successfully"
#     }

# delete course item using sqlalchemy
@router.delete("/course/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(id:int, db:Session = Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    course = db.query(models.Course).filter(models.Course.id == id).first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f'course with id:{id} not exist'
        )
    db.delete(course )
    db.commit()
    return {
        'status' : 'success',
        'message': f'course with id:{id}deleted successfully'
    }
    

# @app.put("/course/update/{id}", status_code=status.HTTP_200_OK)
# def update_course_by_id(id: int, course: Course ):

#     #check if course exist
#     cursor.execute("SELECT 1 FROM course WHERE id = %s",(id,))
#     if cursor.fetchone() is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Course with id:{id} doesn't exist "
#         )
    
#     #update course
#     cursor.execute(
#         """UPDATE course SET name=%s, instructor=%s, duration=%s WHERE id=%s RETURNING * """,(course.name, course.instructor, course.duration,id)
#     )
#     conn.commit()
    
#     return {
#         "message":"course updated successfully",
#         "course_id": id
#     }

# update course using sqlalchemy
@router.put("/course/update/{id}")
def update_course(id:int, updated_course:schemas.Course, db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    course_query = db.query(models.Course).filter(models.Course.id == id)
    course = course_query.first()
    if not course:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"course with id:{id} not found"
        )
    update_data = updated_course.model_dump(exclude_unset=True)
    update_data['website'] = str(update_data['website'])
    course_query.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(course)
    return {
        'status' : 'Success',
        'message' : f'course with id:{id} updated successfully',
        'course_details': course
    }


    

# @app.put("/course/update/{id}", status_code=status.HTTP_200_OK)
# def update_course_by_id(id: int, course: UpdateCourse):

#     # check if course exists
#     cursor.execute(
#         "SELECT 1 FROM course WHERE id = %s",
#         (id,)
#     )
#     if cursor.fetchone() is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Course with id:{id} doesn't exist"
#         )

#     # update course
#     cursor.execute(
#         """
#         UPDATE course
#         SET name = %s,
#             instructor = %s,
#             duration = %s
#         WHERE id = %s
#         """,
#         (course.name, course.instructor, course.duration, id)
#     )

#     conn.commit()

#     return {
#         "message": "course updated successfully",
#         "course_id": id
#     }