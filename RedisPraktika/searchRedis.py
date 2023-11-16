import redis
import json


def search(text: str) -> list:
    """Search the redis db

    Args:
        text (str): The search term

    Returns:
        list: A list of strings containing all possible results
    """
    searchTerm = f"business:name:{text.lower()}*"
    searchResults = redisConnection.keys(searchTerm)
    searchResults = [searchResult.split(":")[2] for searchResult in searchResults]
    return searchResults


def getByCompanieName(companyName: str) -> str:
    """Looks in the redis db for the company and returns the corallation value

    Args:
        key (str): The name of the company

    Returns:
        str: The value
    """
    key = f"business:name:{companyName}"
    key2 = json.loads(redisConnection.get(key))["id"]
    return json.loads(redisConnection.get(f"business:{key2}"))

redisConnection = redis.Redis(host='localhost', port=6379, decode_responses=True)

text = "null"
while(text != "quit"):
    text = input("Geben sie ein Suchbegriff ein: ")
    results = search(text)
    print("Press the corralating button to get more infos: ")
    for i, result in enumerate(results):
        print(f"\t {i+1} -> {result}")
    result = int(input("Input the corralating button to get more infos: "))
    company = getByCompanieName(results[result-1])
    print(f"Address: {company['address']} {company['postal_code']} {company['city']} {company['state']} \nEvaluation: {company['stars']}")
