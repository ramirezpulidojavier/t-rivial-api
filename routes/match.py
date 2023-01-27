from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.match import matchEntity, matchesEntity
from models.match import Match
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

match = APIRouter()



@match.get('/match', response_model=list[Match], tags=["match"])
def find_all_match():
    return matchesEntity(conn.local.match.find())


@match.post('/match', response_model=Match, tags=["match"])
def create_match(match: Match):
    new_match = dict(match)
    del new_match["id"]

    id = conn.local.match.insert_one(new_match).inserted_id

    match = conn.local.match.find_one({"_id": id})

    return matchEntity(match)


@match.get('/match/{id}', response_model=Match, tags=["match"])
def find_match(id: str):

    return matchEntity(conn.local.match.find_one({"_id": ObjectId(id)}))


@match.put('/match/{id}', response_model=Match, tags=["match"])
def update_match(id: str, match: Match):
    conn.local.match.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(match)})
    return matchEntity(conn.local.match.find_one({"_id": ObjectId(id)}))


@ match.delete('/match/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["match"])
def delete_match(id: str):
    matchEntity(conn.local.match.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)