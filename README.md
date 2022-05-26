# Apriori-Algorithm
Association Rules Mining using the Apriori Algorithm

This Apriori-Algorithm based program is done to generate association rules from a set of 10 items and 20 transactions based on these items. There is five different transactions record (five database) generated randomly and reviewed manually.
The program asks the user to input the number of transaction DB to use. This is a number between 1 and 5. Based on this number, the program chooses the right DB (which is a .txt file) to read from. The files are DB1.txt, DB2.txt, DB3.txt, DB4.txt and DB5.txt (see Input Section). The items are also stored in items.txt (also, see Input section).
After selecting the transaction DB to use, the user is prompted to choose a minimum support percentage (which is a number between 0 and 100), and after doing so, the same happens to select the minimum confidence percentage (between 0 and 100).
The program will then display the transactions found in the selected DB, followed by the association rules. Each rule is displayed along its support and confidence. (see Output Section).
At the end, the program asks  users if they want to re-run the program. If the user chooses to do so, the program will re-start from the beginning (asking user to enter DB number, support and confidence).

## Input

The input consists of the five Transactions Files (five transactions DB), in which every line designates a purchase or a transaction and contains a list of items separated by a comma. Another file called items.txt which corresponds to the items. Each item is written on a line.
items.txt
DB1.txt
DB2.txt
DB3.txt
DB4.txt
DB5.txt
