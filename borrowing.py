from inventory import resources


fellows = {
    "F001": "Mina",
    "F002": "David",
    "F003": "Ada"
}

loans = {}


def borrow_resource(fellow_id, resource_id, quantity):
    if fellow_id not in fellows:
        return False

    if quantity <= 0:
        return False

    for resource in resources:
        if resource["id"] == resource_id:
            if quantity > resource["available"]:
                return False

            resource["available"] -= quantity

            if fellow_id not in loans:
                loans[fellow_id] = {}

            loans[fellow_id][resource_id] = quantity

            return True

    return False
    
def return_resource(fellow_id, resource_id, quantity):
    if fellow_id not in fellows:
        return False

    if fellow_id not in loans:
        return False

    if resource_id not in loans[fellow_id]:
        return False

    if quantity <= 0:
        return False

    if quantity > loans[fellow_id][resource_id]:
        return False
    for resource in resources:
        if resource["id"] == resource_id:
            resource["available"] += quantity
    loans[fellow_id][resource_id] -= quantity

    if loans[fellow_id][resource_id] == 0:
        del loans[fellow_id][resource_id]

    return True
