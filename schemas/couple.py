def coupleEntity(item) -> dict:
    return {
        "player1": item["player1"],
        "player2": item["player2"]
    }

def couplesEntity(entity) -> list:
    return [coupleEntity(item) for item in entity]