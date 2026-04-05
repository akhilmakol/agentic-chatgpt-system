from agents.sql_agent import query_sql
from agents.api_agent import call_api
from agents.jira_agent import generate_jira_story
from agents.rag_agent import retrieve_context
from models.llm import call_llm

def route_query(text: str):
    text = text.lower()

    if "sql" in text or "database" in text:
        return "sql"
    elif "jira" in text or "user story" in text:
        return "jira"
    elif "api" in text:
        return "api"
    else:
        return "rag"

def run_agent(user_input: str):
    route = route_query(user_input)

    if route == "sql":
        data = query_sql(user_input)
        return call_llm(f"Explain this SQL result:\n{data}")

    elif route == "jira":
        return generate_jira_story(user_input)

    elif route == "api":
        return call_api(user_input)

    else:
        context = retrieve_context(user_input)
        return call_llm(f"Context:\n{context}\n\nQuestion: {user_input}")
