from fastapi import APIRouter, Response, status, Depends
from config.db import conn
from schemas.match import matchEntity, matchesEntity
from models.match import Match
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
import auth
from fastapi.security.api_key import APIKey


match = APIRouter()



@match.get('/match', response_model=list, tags=["match"])
def find_all_match():
    return matchesEntity(conn.match.find())


@match.post('/match', response_model=Match, tags=["match"])
def create_match(match: Match, api_key: APIKey = Depends(auth.get_api_key)):
    new_match = dict(match)
    del new_match["id"]
    
    new_pot = conn.pot.find_one({"_id": ObjectId("63daa2459093060ad7b0c669")})
    new_pot["total"] += new_match["pot"]
    conn.pot.find_one_and_update(
        {"_id": ObjectId("63daa2459093060ad7b0c669")}, {"$set": new_pot})

    id = conn.match.insert_one(new_match).inserted_id

    match = conn.match.find_one({"_id": id})

    return matchEntity(match)


@match.get('/match/{id}', response_model=Match, tags=["match"])
def find_match(id: str):

    return matchEntity(conn.match.find_one({"_id": ObjectId(id)}))


@match.put('/match/{id}', response_model=Match, tags=["match"])
def update_match(id: str, match: Match, api_key: APIKey = Depends(auth.get_api_key)):
    conn.match.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(match)})
    return matchEntity(conn.match.find_one({"_id": ObjectId(id)}))


@ match.delete('/match/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["match"])
def delete_match(id: str, api_key: APIKey = Depends(auth.get_api_key)):
    matchEntity(conn.match.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)