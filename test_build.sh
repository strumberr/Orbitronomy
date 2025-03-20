#!/bin/bash

# Get the first file in the dist/ directory
file=$(ls dist/ | head -n 1)

# Check if a file was found
if [ -z "$file" ]; then
    echo "No files found in dist/ directory."
    exit 1
fi

# Install the package
echo "Installing dist/$file..."
pip install "dist/$file"
