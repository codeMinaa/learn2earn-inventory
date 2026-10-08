
from inventory import (
    add_resource,
    list_resources,
    search_resources,
    filter_by_category
)

from validation import (
    get_positive_integer,
    get_non_empty_input
)

from borrowing import (
    borrow_resource,
    return_resource
)

from reports import (
    total_units,
    available_units,
    borrowed_units,
    low_stock_resources,
    most_borrowed_resources
)


def add_resource_menu():
    resource_id = get_non_empty_input("Enter resource ID: ")
    name = get_non_empty_input("Enter resource name: ")
    category = get_non_empty_input("Enter category: ")
    total_units = get_positive_integer("Enter total units: ")

    success = add_resource(
        resource_id,
        name,
        category,
        total_units
    )

    if success:
        print("Resource added successfully.")
    else:
        print("Error: Resource ID already exists.")


def list_resources_menu():
    resources = list_resources()

    if not resources:
        print("No resources in inventory.")
        return

    print("\n===== Resource Inventory =====")

    for resource in resources:
        print(f"ID: {resource['id']}")
        print(f"Name: {resource['name']}")
        print(f"Category: {resource['category']}")
        print(f"Total units: {resource['total']}")
        print(f"Available units: {resource['available']}")
        print()


def search_resource_menu():
    name = get_non_empty_input("Enter resource name to search: ")

    results = search_resources(name)

    if not results:
        print("No matching resources found.")
        return

    print("\n===== Search Results =====")

    for resource in results:
        print(f"ID: {resource['id']}")
        print(f"Name: {resource['name']}")
        print(f"Category: {resource['category']}")
        print(f"Total units: {resource['total']}")
        print(f"Available units: {resource['available']}")
        print()


def filter_category_menu():
    category = get_non_empty_input("Enter category to filter: ")

    results = filter_by_category(category)

    if not results:
        print("No resources found in this category.")
        return

    print("\n===== Category Results =====")

    for resource in results:
        print(f"ID: {resource['id']}")
        print(f"Name: {resource['name']}")
        print(f"Category: {resource['category']}")
        print(f"Total units: {resource['total']}")
        print(f"Available units: {resource['available']}")
        print()


def borrow_resource_menu():
    fellow_id = get_non_empty_input("Enter fellow ID: ")
    resource_id = get_non_empty_input("Enter resource ID: ")
    quantity = get_positive_integer("Enter quantity: ")

    success = borrow_resource(
        fellow_id,
        resource_id,
        quantity
    )

    if success:
        print("Resource borrowed successfully.")
    else:
        print(
            "Borrowing failed. Check the fellow ID, "
            "resource ID, quantity, or available stock."
        )


def return_resource_menu():
    fellow_id = get_non_empty_input("Enter fellow ID: ")
    resource_id = get_non_empty_input("Enter resource ID: ")
    quantity = get_positive_integer("Enter quantity: ")

    success = return_resource(
        fellow_id,
        resource_id,
        quantity
    )

    if success:
        print("Resource returned successfully.")
    else:
        print(
            "Return failed. Check the fellow ID, "
            "resource ID, quantity, or loan record."
        )


def reports_menu():
    print("\n===== Inventory Reports =====")

    print(f"Total units: {total_units()}")
    print(f"Available units: {available_units()}")
    print(f"Currently borrowed: {borrowed_units()}")

    print("\nLow Stock Resources:")

    low_stock = low_stock_resources()

    if not low_stock:
        print("No resources have fewer than 3 available units.")
    else:
        for resource in low_stock:
            print(
                f"{resource['name']} "
                f"({resource['available']} available)"
            )

    print("\nMost Borrowed Resource(s):")

    most_borrowed = most_borrowed_resources()

    if not most_borrowed:
        print("No resources have been borrowed yet.")
    else:
        for resource in most_borrowed:
            print(
                f"{resource['name']} "
                f"({resource['borrowed']} borrowed)"
            )


def menu():
    while True:
        print("\n===== Learn2Earn Resource System =====")
        print("1. Add Resource")
        print("2. List Resources")
        print("3. Borrow Resource")
        print("4. Return Resource")
        print("5. Search Resources")
        print("6. Filter by Category")
        print("7. View Reports")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_resource_menu()

        elif choice == "2":
            list_resources_menu()

        elif choice == "3":
            borrow_resource_menu()

        elif choice == "4":
            return_resource_menu()

        elif choice == "5":
            search_resource_menu()

        elif choice == "6":
            filter_category_menu()

        elif choice == "7":
            reports_menu()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


menu()
