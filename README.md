# Nuke-Roto-RotoPaint-Opacity-Toggle-Script
This Python script provides a convenient way to toggle the opacity of selected Roto or RotoPaint nodes in Nuke between 1 (fully visible) and 0 (completely hidden) with animated keyframes. It also integrates into the Nuke interface with a custom keyboard shortcut (Ctrl+Shift+O).
Features
Toggle Opacity: Quickly switch the opacity of a Roto or RotoPaint node between 1 and 0.
Animated Keyframes: Ensures the opacity is toggled with keyframes for smooth animation.
Shortcut Integration: Accessible through the Ctrl+Shift+O shortcut or from the Edit menu in Nuke.
Error Handling: Prompts the user if no Roto or RotoPaint node is selected.
Installation
Place the script in your Nuke plugin directory or a custom tools directory.

Add the following line to your menu.py file to register the script:

python
Copy code
import toggle_opacity  # Adjust the path as needed
Alternatively, add the following code for integration:

python
Copy code
import sys
sys.path.append("/path/to/your/script_directory")  # Replace with your actual path
import toggle_opacity
Restart Nuke.

Usage
Open your Nuke project.
Select a Roto or RotoPaint node.
Press Ctrl+Shift+O or use the Edit > Toggle Roto Opacity menu option to toggle the opacity.
Example Workflow
Animate a Roto node's opacity with keyframes using this script.
Seamlessly switch between fully visible and hidden states to manage animations and transitions effectively.
