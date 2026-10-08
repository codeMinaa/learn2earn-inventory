
from inventory import resources


def total_units():
    total = 0

    for resource in resources:
        total += resource["total"]

    return total


def available_units():
    total = 0

    for resource in resources:
        total += resource["available"]

    return total


def borrowed_units():
    return total_units() - available_units()


def low_stock_resources():
    results = []

    for resource in resources:
        if resource["available"] < 3:
            results.append(resource)

    return results


def most_borrowed_resources():
    borrowed_resources = []

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        borrowed_resources.append({
            "name": resource["name"],
            "borrowed": borrowed
        })

    if not borrowed_resources:
        return []

    highest = max(resource["borrowed"] for resource in borrowed_resources)

    if highest == 0:
        return []

    return [
        resource
        for resource in borrowed_resources
        if resource["borrowed"] == highest
    ]
