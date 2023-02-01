from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.player_queue import queueEntity, queuesEntity
from schemas.couple import coupleEntity, couplesEntity
from models.player_queue import Queue
from models.couple import Couple
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

pot = APIRouter()


@pot.post('/pot', response_model=dict, tags=["pot"])
def create_pot():

    id = conn.pot.insert_one(dict({"total": 0})).inserted_id
    queue = conn.pot.find_one({"_id": ObjectId(id)})

    return queue


@pot.get('/pot', response_model=int, tags=["pot"])
def create_pot():

    queue = conn.pot.find_one({"_id": ObjectId("63daa2459093060ad7b0c669")})

    return queue["total"]

