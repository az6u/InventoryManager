# Inventory Manager Testing

| # | Feature | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Missing inventory file | Start the program without an `inventory.txt` file present | Program starts with an empty inventory and does not crash | Verified by removing the file and launching the program in a temp directory | Pass |
| 2 | View empty inventory | Select option 1 when no items exist | Message says `No inventory items found.` | Verified in a temporary empty inventory run | Pass |
| 3 | Add valid item | Enter `Desk Lamp`, `Electronics`, and `7` | Item is saved to the file with the correct format | Confirmed after adding and reopening the file | Pass |
| 4 | Reject empty item name | Enter an empty item name | Program displays an error and does not add the item | Verified with blank input | Pass |
| 5 | Reject duplicate item name | Add `Laptop Charger` twice with different capitalization | Duplicate is rejected | Verified with `laptop charger` after initial creation | Pass |
| 6 | Reject nonnumeric quantity | Enter `six` for quantity | Program prints a validation message | Verified by running the add-item path with a text value | Pass |
| 7 | Reject negative quantity | Enter `-1` when adding an item | Program rejects the negative value | Verified in the interactive validation path | Pass |
| 8 | Update valid item quantity | Select an existing item and set a new quantity | Item quantity updates and file is saved | Verified by updating `Printer Paper` to 18 | Pass |
| 9 | Reject invalid item number | Enter `99` when updating or removing | Program shows an invalid item number message | Verified in both update and remove flows | Pass |
| 10 | Remove an item | Choose an existing item number | Item disappears from the inventory and file is rewritten | Verified by removing `Keyboard` | Pass |
| 11 | Case-insensitive partial search | Search for `charger` | Both matching item names are shown | Verified with `Laptop Charger` and `USB-C Charger` entries | Pass |
| 12 | No-match search | Search for `zzz` | Program prints `No inventory items matched your search.` | Verified using a non-existing item name | Pass |
| 13 | Inventory summary | Select option 6 | Summary includes unique items, total quantity, low-stock count, and category counts | Verified after a working dataset was loaded | Pass |
| 14 | Restart persistence | Close the program and reopen it | Previous changes remain in `inventory.txt` | Verified by restarting the program after file changes | Pass |
| 15 | Invalid menu option | Enter `9` or `abc` | Program prints an invalid option message and continues | Verified in the menu loop | Pass |
| 16 | Empty search term | Enter a blank search string | Program prints `Search term cannot be empty.` | Verified with whitespace-only input | Pass |

## Notes

- The test list above reflects the behavior of the final program after validation.
- All required tests were run in the project environment, and the final results were recorded accurately.
- The sample file includes multiple categories and low-stock items to satisfy the project requirements.
