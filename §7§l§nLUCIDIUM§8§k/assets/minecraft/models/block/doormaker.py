import os

# List of door types
door_types = [
    "bamboo", "cherry", "copper", "crimson", "dark_oak", "mangrove", "oak",
    "oxidized_copper", "spruce", "warped", "weathered_copper", "exposed_copper", 
    "iron", "jungle"
]

# List of original filenames to be copied and renamed
original_files = [
    "birch_door_bottom_left.json", "birch_door_bottom_left_open.json", 
    "birch_door_bottom_right.json", "birch_door_bottom_right_open.json",
    "birch_door_top_left.json", "birch_door_top_left_open.json",
    "birch_door_top_right.json", "birch_door_top_right_open.json",
    "birch_trapdoor_bottom.json", "birch_trapdoor_open.json", 
    "birch_trapdoor_top.json"
]

# Directory containing the original files (current directory)
source_dir = os.path.dirname(os.path.abspath(__file__))

# Function to create copies and replace content
def create_copies_and_replace(door_type):
    for original_file in original_files:
        # Read the content of the original file
        with open(os.path.join(source_dir, original_file), 'r') as file:
            content = file.read()
        
        # Replace references within the content
        new_content = content.replace("birch", door_type)
        
        # Create a new filename by replacing 'birch' with the door_type
        new_filename = original_file.replace("birch", door_type)
        
        # Save the new file in the same directory
        with open(os.path.join(source_dir, new_filename), 'w') as new_file:
            new_file.write(new_content)

# Process each door type
for door_type in door_types:
    create_copies_and_replace(door_type)

print("Files have been copied and renamed successfully.")
