THANKS FOR TAKING YOUR TIME AND READING THIS :)

This is a very simple working model of a G-Code interpreter. G-Code are the commands used in CNC (Computer Numeric Control) manufacturing.

The G-Code gives details to the machine on how to process the raw material in order to obtain a highly precised component.

The program accepts user-input G-Code lines, extracts 2D coordinates, stores them in a matrix, and calculates the total number of moves and toolpath distance.

It’s designed to process linear move commands and provide clear output for CNC toolpath analysis.

The interpreter prompts users to enter G-Code lines (e.g., G01 X0 Y0) interactively, stopping when the user types "done".

It supports commands G01 to G05, treating them as linear moves. Each line is parsed to extract X and Y coordinates, which are stored in a matrix as [x, y] lists. 

The program calculates the Euclidean distance between consecutive points to determine the total toolpath length. Invalid inputs, such as non-numeric coordinates or malformed commands, are skipped with warning messages, ensuring robust operation.
