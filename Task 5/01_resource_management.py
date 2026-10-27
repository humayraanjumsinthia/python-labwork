resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2],
]


def display_resources(resources):
    if resources == []:
        print("No resources found.")
    else:
        for resource in resources:
            print(resource)


def search_by_category(resources, category):
    found = False
    for resource in resources:
        if resource[2] == category:
            print(resource)
            found = True
    if found == False:
        print("No resources found.")


def find_unavailable(resources):
    found = False
    for resource in resources:
        if resource[3] == 0:
            print(resource)
            found = True
    if found == False:
        print("No unavailable resources.")


display_resources(resources)
print("Electronics:")
search_by_category(resources, "Electronics")
print("Unavailable resources:")
find_unavailable(resources)
display_resources([])
