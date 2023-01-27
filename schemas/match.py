def matchEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "player1": item["player1"],
        "player2": item["player2"],
        "result": item["result"],
        "date": item["date"]
    }

def matchesEntity(entity) -> list:
    return [matchEntity(item) for item in entity]