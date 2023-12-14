#!/bin/bash

# Does the symlink in public directory exist?  If not, create it
if [ ! -L public/dataset ]; then
    echo "Creating symlink to dataset directory since it doesn't exist"
    ln -s ../../../dataset public/dataset
fi

# Define the dataset file path
filePath="public/dataset/dataset.json"

# If the dataset file doesn't exist, create it so the UI doesn't show
# a confusing error message
if [ ! -f "$filePath" ]; then
    # File does not exist, create the directory if it doesn't exist
    mkdir -p "$(dirname "$filePath")"
    
    # Create the file with the initial content
    echo '{"entries": []}' > "$filePath"
fi

# Run the server in dev mode
npm run dev
