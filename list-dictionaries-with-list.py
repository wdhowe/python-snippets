#!/usr/bin/env python3
"""List of dictionaries, with a list as value for a dict key"""

# Create empty group list
group_list = []

# Create empty member list to be used in the group_list dictionary
member_list = []

# Add a new dictionary with the group names and member list to the group_list
group_list.append({"group_name": "Rebels", "members": member_list})

# Re-initialize the member_list, and create the 2nd dictionary in the group_list
member_list = []
group_list.append({"group_name": "Empire", "members": member_list})

# Display the entire group_list
print("The group list is: ", group_list)

# Show the group_name at group_list position 0
print("The group name at position 0 is: ", group_list[0]["group_name"])
print("The group name at position 1 is: ", group_list[1]["group_name"])

# Append a new member to the members at group_list position 0
group_list[0]["members"].append("yoda")
group_list[0]["members"].append("luke")

# Append a new member to the members at group_list position 1
group_list[1]["members"].append("vader")
group_list[1]["members"].append("maul")

# Show the members at group_list position 0
print("The members at group 0 is: ", group_list[0]["members"])
print("The members at group 1 is: ", group_list[1]["members"])
