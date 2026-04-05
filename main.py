from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This defines what a BugReport looks like
class BugReport(BaseModel):
    title: str
    severity: int
    platform: str
    description: str

@app.get("/hello")
def say_hello():
    return {"message": "Server is running!"}

@app.post("/submit-bug")
def submit_bug(bug: BugReport):
    return {
        "received": bug.title,
        "severity": bug.severity,
        "message": f"Bug '{bug.title}' received on {bug.platform}"
    }

# Global state - server remembers this
game_state = {
    "current_bug": None,
    "score": 0,
    "steps": 0
}

@app.post("/reset")
def reset():
    game_state["current_bug"] = {
        "title": "Payment fails for all users",
        "platform": "web",
        "severity": 1
    }
    game_state["score"] = 0
    game_state["steps"] = 0
    return {"observation": game_state["current_bug"]}

@app.post("/step")
def step(action: BugReport):
    game_state["steps"] += 1
    # Score the action
    score = 1.0 if action.severity == 1 else 0.0
    game_state["score"] += score
    return {
        "reward": score,
        "done": game_state["steps"] >= 3,
        "total_score": game_state["score"]
    }