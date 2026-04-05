from models.llm import call_llm

def generate_jira_story(prompt: str):
    template = f"""
Create a JIRA user story:

Title:
Description:
Acceptance Criteria:
Story Points:

Input: {prompt}
"""
    return call_llm(template)
