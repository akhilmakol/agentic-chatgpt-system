from agents.sql_agent import query_sql
from agents.api_agent import call_api
from agents.jira_agent import generate_jira_story
from agents.rag_agent import retrieve_context
from models.llm import call_llm

def run_agent(user_input: str):
    text = user_input.lower()

    try:
        if "sql" in text:
            data = query_sql(user_input)
            return call_llm(f"Explain this SQL result:\n{data}")

        elif "jira" in text:
            return generate_jira_story(user_input)

        elif "api" in text:
            return call_api(user_input)

        else:
            context = retrieve_context(user_input)
            return call_llm(f"Context:\n{context}\n\nQuestion: {user_input}")

    except Exception as e:
        return f"Agent Error: {str(e)}"
