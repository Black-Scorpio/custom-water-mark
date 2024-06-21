import tkinter as tk
from tkinter import colorchooser

class FontStyleSelector:
    def __init__(self, root, apply_callback):
        """
        Initialize the FontStyleSelector.

        Args:
            root (tk.Tk): The root window for the Tkinter application.
            apply_callback (function): A callback function to apply the selected font style.
        """
        self.root = root
        self.apply_callback = apply_callback
        self.color = "#FFFFFF"  # Default color white

        # Create a frame for the font style controls
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Font Color Button
        color_button = tk.Button(self.frame, text="Choose Font Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT, padx=5)

        # Apply Style Button
        apply_button = tk.Button(self.frame, text="Apply Style", command=self.apply_style)
        apply_button.pack(side=tk.LEFT, padx=5)

    def choose_color(self):
        """
        Open a color chooser dialog to select the font color.
        """
        self.color = colorchooser.askcolor()[1]

    def apply_style(self):
        """
        Apply the selected font style by invoking the callback function.
        """
        self.apply_callback(self.color)
