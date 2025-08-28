from fastapi import FastAPI
from pydantic import BaseModel
from src.chains import get_summarize_chain, get_qa_chain, get_learn_path_chain

app = FastAPI(
    title="AI Services API",
    description="Exposes three AI services as REST APIs.",
    version="1.0.0",
)

class SummarizeRequest(BaseModel):
    text: str

class QARequest(BaseModel):
    question: str

class LearnPathRequest(BaseModel):
    profile: str
    goal: str

summarize_chain = get_summarize_chain()
qa_chain = get_qa_chain()
learn_path_chain = get_learn_path_chain()

@app.post("/summarize")
async def summarize(req: SummarizeRequest):
    """Summarizes the provided text."""
    result = summarize_chain.invoke({"text": req.text})
    return {"summary": result}

@app.post("/qa")
async def qa(req: QARequest):
    """Answers a question based on a pre-loaded document (RAG)."""
    result = qa_chain.invoke({"input": req.question})
    return {"answer": result.get("answer", "No answer found.")}

@app.post("/learn-path")
async def learn_path(req: LearnPathRequest):
    """Suggests a learning path based on user profile and goal."""
    result = learn_path_chain.invoke({"profile": req.profile, "goal": req.goal})
    return {"learning_path": result}

