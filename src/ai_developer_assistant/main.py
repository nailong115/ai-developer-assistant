from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Developer Assistant")


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None


projects = []


@app.get("/")
def read_root():
    return {"message": "AI Developer Assistant is running"}


@app.post("/projects")
def create_project(project: ProjectCreate):
    new_project = {
        "id": len(projects) + 1,
        "name": project.name,
        "description": project.description,
    }

    projects.append(new_project)
    return new_project


@app.get("/projects")
def list_projects():
    return projects