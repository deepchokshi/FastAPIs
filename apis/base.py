from v1 import route_employee
from fastapi import APIRouter

app_router = APIRouter()

tags = [
    {"name": "Employee", "description": "APIs for employe"}
]


app_router.include_router(route_employee.router, prefix="/v1/employee/", tags=tags["Employee"])


