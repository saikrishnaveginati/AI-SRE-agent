import boto3
from datetime import datetime, timedelta

logs = boto3.client("logs", region_name="us-east-1")

LOG_GROUP = "/aws/lambda/rag-monitor-wrapper"


def fetch_recent_errors(limit=20):

    end_time = int(datetime.utcnow().timestamp() * 1000)
    start_time = int((datetime.utcnow() - timedelta(minutes=30)).timestamp() * 1000)

    response = logs.filter_log_events(
        logGroupName=LOG_GROUP,
        startTime=start_time,
        endTime=end_time,
        limit=limit
    )

    results = []

    for event in response.get("events", []):
        results.append(event["message"])

    return results