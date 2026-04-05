from models.llm import call_llm

def generate_jira_story(prompt):
    template = f"""
    Create a JIRA story:

    Title:
    Description:
    Acceptance Criteria:
    Story Points:

    Input: {prompt}
    """
    return call_llm(template)
