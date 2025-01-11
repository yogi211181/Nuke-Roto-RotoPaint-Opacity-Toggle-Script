import nuke

def toggle_opacity():
    node = nuke.selectedNode()

    if node.Class() not in ["Roto", "RotoPaint"]:
        nuke.message("Please select a Roto or RotoPaint node.")
        return

    opacity_knob = node["opacity"]

    # Get the current frame
    current_frame = nuke.frame()

    # Check if the knob is animated
    if not opacity_knob.isAnimated():
        opacity_knob.setAnimated()

    # Get the current value at the current frame
    current_value = opacity_knob.getValueAt(current_frame)

    # Toggle between 1 and 0
    new_value = 1.0 if current_value == 0.0 else 0.0

    # Set the new value with a keyframe
    opacity_knob.setValueAt(new_value, current_frame)

# Add the shortcut key to the menu
nuke.menu("Nuke").addCommand("Edit/Toggle Roto Opacity", toggle_opacity, "Ctrl+Shift+O")
