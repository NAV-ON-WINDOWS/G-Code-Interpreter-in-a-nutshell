import math

# Step 1: Collect G-Code from user input
gcode_lines = []
print("Enter G-Code lines (e.g., 'G01 X0 Y0'). Type 'done' to finish:")
while True:
    line = input("G-Code: ").strip()
    if line.lower() == 'done':
        break
    if line:  # Only append non-empty lines
        gcode_lines.append(line)
    else:
        print("Warning: Empty line ignored.")

# Step 2: Setup
previous_x = None
previous_y = None
total_distance = 0
move_count = 0

# Step 3: Parse each line
print("Processing G-Code lines:")
for line in gcode_lines:
    line = line.strip()
    print(f"Line: '{line}'")  # Debug: Show each line
    if not line or line.startswith(';'):
        print("  Skipping: Empty or comment line")
        continue

    # Check for valid G-Code commands (G01 to G05)
    if line.startswith(('G01', 'G02', 'G03', 'G04', 'G05')):
        parts = [p for p in line.split() if p]  # Split and filter empty parts
        x = None
        y = None

        for part in parts:
            if part.startswith('X'):
                try:
                    x = float(part[1:].replace(' ', ''))  # Remove any extra spaces
                    print(f"  X coordinate: {x}")
                except ValueError:
                    print(f"  Warning: Invalid X coordinate in line: {line}")
                    x = None
            elif part.startswith('Y'):
                try:
                    y = float(part[1:].replace(' ', ''))  # Remove any extra spaces
                    print(f"  Y coordinate: {y}")
                except ValueError:
                    print(f"  Warning: Invalid Y coordinate in line: {line}")
                    y = None

        # Only process if both X and Y are valid
        if x is not None and y is not None:
            move_count += 1
            print(f"  Valid move #{move_count}: ({x}, {y})")
            if previous_x is not None and previous_y is not None:
                distance = math.sqrt((x - previous_x) ** 2 + (y - previous_y) ** 2)
                total_distance += distance
                print(f"  Distance from ({previous_x}, {previous_y}) to ({x}, {y}): {distance:.2f}")
            else:
                print("  First valid point, no distance calculated")
            previous_x = x
            previous_y = y
        else:
            print(f"  Skipping: Missing or invalid coordinates in line: {line}")
    else:
        print(f"  Skipping: Unrecognized command in line: {line}")

# Step 4: Output
print(f"\nFinal Results:")
print(f"Total moves made: {move_count}")
print(f"Total distance traveled: {total_distance:.2f} units")