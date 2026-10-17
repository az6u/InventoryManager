# AI Usage Report

## Tools Used

This project was created with the assistance of an AI coding assistant. The final implementation was reviewed, adjusted, and tested manually to ensure it satisfied the assignment requirements.

## How AI Was Used

AI support was used to help structure the menu-driven Python project, draft the validation logic, and produce the supporting documentation in a clear format. The AI also helped review the program flow and suggest test cases that covered valid and invalid scenarios.

## Example Prompts

- "Create a Python inventory manager with menu options, validation, and file persistence."
- "Write a case-insensitive search function that supports partial matches and empty-input validation."
- "Draft a README and a testing table for a command-line inventory tracker."

## Suggestions Accepted

- A menu-driven structure with functions for loading, saving, viewing, adding, updating, removing, searching, and summarizing inventory.
- A validation approach for empty names, duplicate names, negative quantities, and invalid menu choices.
- A testing document formatted as the required markdown table.

## Suggestions Rejected or Modified

One suggestion proposed a CSV-style file format instead of the required `Name|Category|Quantity` format, so it was rejected and replaced with the required pipe-delimited storage format. Another suggestion used a more complicated object model than necessary, so the simpler dictionary-based list model was kept to match the project requirements.

## Verification

All AI-assisted code and documentation were checked by running the program in the terminal with real input and by inspecting the file output. This included verifying the inventory list, search behavior, invalid input handling, and persistence after restarting the program.

## Code Understanding

The main implementation in `inventory_manager.py` was reviewed carefully before acceptance. The `load_inventory` function reads each line from `inventory.txt`, splits it on `|`, converts the quantity to an integer, and returns a list of dictionaries. The `search_inventory` function checks whether the user’s search text appears anywhere in an item name, ignoring capitalization and supporting partial matches. These behaviors were tested directly with real input to confirm they work as expected.
