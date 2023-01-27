def potEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "total": item["total"]
    }

def potesEntity(entity) -> list:
    return [potEntity(item) for item in entity]