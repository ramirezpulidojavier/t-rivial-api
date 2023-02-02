from fastapi import APIRouter, Response, status, Depends
from config.db import conn
from schemas.player_queue import queueEntity, queuesEntity
from schemas.couple import coupleEntity, couplesEntity
from models.player_queue import Queue
from models.couple import Couple
from passlib.hash import sha256_crypt
from bson import ObjectId
import auth
from starlette.status import HTTP_204_NO_CONTENT
from fastapi.security.api_key import APIKey

pot = APIRouter()


# @pot.post('/pot', response_model=dict, tags=["pot"])
# def create_pot():

#     id = conn.pot.insert_one(dict({"total": 0})).inserted_id
#     queue = conn.pot.find_one({"_id": ObjectId(id)})

#     return queue

@pot.get('/pot_from_database', response_model=int, tags=["pot"])
def get_pot():

    pot = conn.pot.find_one({"_id": ObjectId("63daa2459093060ad7b0c669")})

    return pot["total"]


@pot.get('/pot', response_model=int, tags=["pot"])
def calculate_pot():

    matches = conn.match.find()
    pot = 0

    for match in matches:
        pot += 1
        if "player2" in match.keys() and not match["player2"] is None:
            pot += 1

    new_pot = conn.pot.find_one({"_id": ObjectId("63daa2459093060ad7b0c669")})
    new_pot["total"] = pot
    conn.pot.find_one_and_update(
        {"_id": ObjectId("63daa2459093060ad7b0c669")}, {"$set": new_pot})

    return pot + 2


@pot.put('/pot/{amount}', response_model=int, tags=["pot"])
def create_pot(amount: int, api_key: APIKey = Depends(auth.get_api_key)):

    new_pot = conn.pot.find_one({"_id": ObjectId("63daa2459093060ad7b0c669")})
    new_pot["total"] = amount
    conn.pot.find_one_and_update(
        {"_id": ObjectId("63daa2459093060ad7b0c669")}, {"$set": new_pot})

    pot = conn.pot.find_one({"_id": ObjectId("63daa2459093060ad7b0c669")})

    return pot["total"]
