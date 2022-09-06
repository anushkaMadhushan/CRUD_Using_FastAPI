# import statement

from fastapi import FastAPI
from routes.student import student_router

# crete app

app = FastAPI()
# register Router
app.include_router(student_router)