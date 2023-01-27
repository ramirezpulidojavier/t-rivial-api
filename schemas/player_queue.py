def queueEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "queue": item["queue"]
    }

def queuesEntity(entity) -> list:
    return [queueEntity(item) for item in entity]