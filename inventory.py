
resources = [
    {
        "id": "lap001",
        "name": "laptop",
        "category": "computer",
        "total": 5,
        "available": 5
    },
    {
        "id": "cam001",
        "name": "camera",
        "category": "media",
        "total": 3,
        "available": 3
    },
    {
        "id": "mic001",
        "name": "microphone",
        "category": "audio",
        "total": 4,
        "available": 4
    },
    {
        "id": "pro001",
        "name": "projector",
        "category": "presentation",
        "total": 2,
        "available": 2
    },
    {
        "id": "tab001",
        "name": "tablet",
        "category": "computer",
        "total": 6,
        "available": 6
    }
]


def add_resource(resource_id, name, category, total_units):
    for resource in resources:
        if resource["id"] == resource_id:
            return False

    resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total_units,
        "available": total_units
    }

    resources.append(resource)
    return True


def list_resources():
    return resources


def search_resources(name):
    results = []

    for resource in resources:
        if name.lower() in resource["name"].lower():
            results.append(resource)

    return results


def filter_by_category(category):
    results = []

    for resource in resources:
        if resource["category"].lower() == category.lower():
            results.append(resource)

    return results
