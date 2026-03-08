from typing import TypedDict, Optional

class AgentState(TypedDict):
    repo: str
    metrics_result: Optional[str]
    logs: Optional[str]
    commits: Optional[str]
    analysis: Optional[str]
    report: Optional[str]
    next_action: Optional[str]