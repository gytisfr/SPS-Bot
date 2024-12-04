import json

closedViolationFoundListID = "65e8341cb30a495d92a3c931"
closedViolationNotFoundListID = "65e8341cb30a495d92a3c932"
archiveListID = "65e8341cb30a495d92a3c933"
closedAppealsListID = "65e8341cb30a495d92a3c934"

with open("D:\\Ridgeway\\SPS\\Bot\\j.json", "r+", encoding="utf8") as f:
    data = json.load(f)
    """
    data = {"cards": [card for card in data["cards"] if card["idList"] in [closedViolationFoundListID, closedViolationNotFoundListID, archiveListID, closedAppealsListID]]}
    f.seek(0)
    f.truncate()
    json.dump(data, f, indent=4)
    """
    print(len(data["cards"]))

input()

"""
126 Cards in the lists "Closed - Violation Found" through "Closed - Appeals"
8 Cards are Titles/Sectioners
30 Cards in "Archives"
3 Cards in "Closed - Appeals"
6 Cases are missing (14, 15, 16, 24, 89, 90)
3 Cases are "In Progress" (81, 85, 87)
"""