import json
import redis

def putBusinesstoRedis(jsonObject: dict):
    """Puts a business to redis

    Args:
        jsonObject (dict): The business json object
    """
    idKey = f"business:{jsonobject['business_id']}"
    idPayload = json.dumps(jsonobject)
    nameKey = f"business:name:{jsonobject['name'].lower()}"
    namePayload = json.dumps({"id" :jsonobject["business_id"]})

    redisConnection.set(idKey, idPayload)
    redisConnection.set(nameKey, namePayload)


redisConnection = redis.Redis(host='localhost', port=6379, decode_responses=True)

file = open("RedisPraktika/businessS.json", "r")
lines = file.readlines()
for line in lines:
    jsonobject = json.loads(line)
    putBusinesstoRedis(jsonobject)


