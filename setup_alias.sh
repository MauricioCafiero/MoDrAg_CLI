#!/bin/bash

# Find the absolute path of the MODRAG_CLI directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if modrag.py exists in the code subdirectory
if [ ! -f "$SCRIPT_DIR/code/modrag.py" ]; then
  echo "Error: modrag.py not found in $SCRIPT_DIR/code/"
  exit 1
fi

MODRAG_SCRIPT="$SCRIPT_DIR/code/modrag.py"

# Detect the user's current shell
CURRENT_SHELL="$(basename "$SHELL")"

# Function to add alias to a shell config file
add_alias_to_file() {
  local config_file=$1
  local shell_name=$2
  
  # Create file if it doesn't exist
  if [ ! -f "$config_file" ]; then
    touch "$config_file"
    echo "Created $config_file"
  fi
  
  # Check if the alias already exists
  if grep -q "alias modrag=" "$config_file"; then
    echo "Alias already exists in $config_file"
    # Remove the old alias
    sed -i '' '/alias modrag=/d' "$config_file"
    echo "Removed old alias"
  fi
  
  # Add the new alias
  echo "alias modrag=\"python3 '$MODRAG_SCRIPT'\"" >> "$config_file"
  
  echo "✓ Added alias to $config_file:"
  echo "  alias modrag=\"python3 '$MODRAG_SCRIPT'\""
}

# Apply to detected shell's config file
if [ "$CURRENT_SHELL" = "zsh" ]; then
  add_alias_to_file ~/.zshrc "zsh"
  source ~/.zshrc
  echo "✓ Sourced ~/.zshrc"
elif [ "$CURRENT_SHELL" = "bash" ]; then
  add_alias_to_file ~/.bashrc "bash"
  source ~/.bashrc
  echo "✓ Sourced ~/.bashrc"
else
  echo "Unknown shell: $CURRENT_SHELL"
  echo "Attempting to add to both .zshrc and .bashrc..."
  add_alias_to_file ~/.zshrc "zsh"
  add_alias_to_file ~/.bashrc "bash"
  echo "Note: Please manually source your shell config file"
fi

echo ""
echo "You can now use 'modrag' from anywhere to run MoDrAg!"
