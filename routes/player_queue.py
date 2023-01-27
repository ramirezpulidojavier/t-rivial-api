from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.player_queue import queueEntity, queuesEntity
from schemas.couple import coupleEntity, couplesEntity
from models.player_queue import Queue
from models.couple import Couple
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

queue = APIRouter()




@queue.post('/queue', response_model=Queue, tags=["queue"])
def create_queue(queue: Queue):
    new_queue = dict(queue)
    del new_queue["id"]

    id = conn.queue.insert_one(new_queue).inserted_id

    queue = conn.queue.find_one({"_id": id})

    return queueEntity(queue)


@queue.get('/queue', response_model=list, tags=["queue"])
def find_queue():

    queue_db = queueEntity(conn.local.queue.find_one({"_id": ObjectId("63d3a7e7b613180e171c8702")}))

    return queue_db["queue"]


@queue.put('/queue', response_model=Queue, tags=["queue"])
def add_couple(couple: Couple):
    
    queue_db = queueEntity(conn.local.queue.find_one({"_id": ObjectId("63d3a7e7b613180e171c8702")}))
    queue_db["queue"].append(dict(couple))
    
    conn.local.queue.find_one_and_update(
        {"_id": ObjectId("63d3a7e7b613180e171c8702")}, {"$set": dict(queue_db)})
    return queueEntity(conn.queue.find_one({"_id": ObjectId("63d3a7e7b613180e171c8702")}))


@queue.put('/pop_queue', response_model=Queue, tags=["queue"])
def remove_first_couple():
    
    queue_db = queueEntity(conn.queue.find_one({"_id": ObjectId("63d3a7e7b613180e171c8702")}))
    queue_db["queue"].pop(0)
    
    conn.queue.find_one_and_update(
        {"_id": ObjectId("63d3a7e7b613180e171c8702")}, {"$set": dict(queue_db)})
    return queueEntity(conn.queue.find_one({"_id": ObjectId("63d3a7e7b613180e171c8702")}))

@queue.put('/pop_index_queue', response_model=Queue, tags=["queue"])
def remove_concrete_couple(index: int):
    
    queue_db = queueEntity(conn.queue.find_one({"_id": ObjectId("63d3a7e7b613180e171c8702")}))
    if index < len(queue_db["queue"]):
        queue_db["queue"].pop(index)
    
        conn.queue.find_one_and_update(
            {"_id": ObjectId("63d3a7e7b613180e171c8702")}, {"$set": dict(queue_db)})
    return queueEntity(conn.queue.find_one({"_id": ObjectId("63d3a7e7b613180e171c8702")}))
     