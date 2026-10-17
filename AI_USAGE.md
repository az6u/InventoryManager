# AI Usage Report

## Tools Used

The main tool that was used to help in this project was the VS code assistant which helped me debug my code and fix errors that were found inside of it.

## How AI Was Used

the main parts that needed AI were small parts of all of it, it would find random things to correct or make better on its own and I allowed it to contribute where it was fit.

## Example Prompts

it wasnt used heavily mainly in the starting lines of each thing then it would add on like 
item = {"name": name, "category": category, "quantity": quantity}
            inventory.append(item)

for example or 

        for item in inventory:
            file.write(item["name"] + "|" + item["category"] + "|" + str(item["quantity"]) + "\n")

was another one that would get added as it saw what i was trying to write.

## Suggestions Accepted

it would recommend for files that it should be written a better way.

example:

Each item stored as a dictionary like:
{"name": "Laptop Charger", "category": "Electronics", "quantity": 8}

## Suggestions Rejected or Modified

One suggestion was to store each inventory item in a CSV-style format with commas instead of the required pipe-delimited format. That idea was changed before use because the assignment specifically requires the file to use `Name|Category|Quantity`, and the project must be consistent with the assignment instructions. Another suggestion was to auto-create a more advanced menu system with extra options that were not needed for this project, so I simplified it to the required 7-option menu and kept the program focused.

## Verification

I checked the AI-assisted code by running the program and testing actual inputs in the terminal. This included adding items, viewing the inventory, updating quantities, removing items, searching for names, and verifying that the inventory file saved changes correctly after each action. I also confirmed that invalid selections and bad numeric data were handled without crashing the program.

## Code Understanding

One function the AI helped with was `load_inventory()`. It reads each line of the inventory file, splits the line using the `|` separator, converts the quantity into an integer, and builds a list of dictionaries. I reviewed this carefully and kept the logic simple so it matched the required file format and worked correctly when the file was missing or empty.

Another helpful suggestion was the way to save each item, using a consistent format: each dictionary is written back to the file as `name|category|quantity` on one line. I accepted the idea because it matches the assignment and I verified that reopening the file showed the saved data in the correct structure.