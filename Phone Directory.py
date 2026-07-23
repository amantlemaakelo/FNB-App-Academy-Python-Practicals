# phone_directory.py

# Task Overview
# Create a mini phone directory using a Dictionary.
# The program stores contacts and allows the user
# to search for a friend's phone number.

# Requirements
# • Create a dictionary called contacts where:
#   - Keys are friend names.
#   - Values are phone numbers (stored as strings).
# • Store at least 3 contacts.
# • Ask the user to enter the name of the friend to search for.
# • Use a conditional statement to check if the name exists.
# • If found, display:
#   "Found! [Name]'s number is [Number]"
# • Otherwise, display:
#   "Contact not found."

# Create the contacts dictionary
contacts = {
    "Amara": "0821112222",
    "Sipho": "0733334444",
    "Lerato": "0715556666"
}

# Ask the user for the friend's name
friend_name = input("Enter your friend's name: ")

# Check if the contact exists
if friend_name in contacts:
    print(f"Found! {friend_name}'s number is {contacts[friend_name]}")
else:
    print("Contact not found.")