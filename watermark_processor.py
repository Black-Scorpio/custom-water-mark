import tkinter as tk
from tkinter import filedialog, Canvas
from PIL import Image, ImageDraw, ImageFont, ImageTk
from font_style_selector import FontStyleSelector


class WatermarkProcessor:
    def __init__(self, root):
        """
        Initialize the WatermarkProcessor application.

        Args:
            root (tk.Tk): The root window for the Tkinter application.
        """
        self.root = root
        self.img = None
        self.original_img = None  # Keep the original image without watermark
        self.tk_img = None
        self.font_color = "#FFFFFF"  # Default font color

        self.root.title("Watermark Processor")
        self.root.geometry("1000x800")
        self.root.minsize(1000, 800)

        # Create a frame for the buttons and entry
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        open_button = tk.Button(self.frame, text="Open Image", padx=10, pady=5, fg="white", bg="#263D42", command=self.open_image)
        open_button.grid(row=0, column=0, padx=5)

        self.watermark_text = tk.Entry(self.frame, width=30)
        self.watermark_text.grid(row=0, column=1, padx=5)
        self.watermark_text.insert(0, "Enter watermark text here")
        self.watermark_text.bind("<FocusIn>", self.clear_placeholder)
        self.watermark_text.bind("<FocusOut>", self.add_placeholder)

        watermark_button = tk.Button(self.frame, text="Add Text Watermark", padx=10, pady=5, fg="white", bg="#263D42", command=self.add_text_watermark)
        watermark_button.grid(row=0, column=2, padx=5)

        logo_button = tk.Button(self.frame, text="Add Logo Watermark", padx=10, pady=5, fg="white", bg="#263D42", command=self.add_logo_watermark)
        logo_button.grid(row=0, column=3, padx=5)

        save_button = tk.Button(self.frame, text="Save Image", padx=10, pady=5, fg="white", bg="#263D42", command=self.save_image)
        save_button.grid(row=0, column=4, padx=5)

        self.canvas = Canvas(root, bg="gray")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Configure>", self.resize_canvas)

        self.font_style_selector = FontStyleSelector(root, self.apply_font_style)

    def open_image(self):
        """
        Open an image file and display it, resized to fit within 700x500 while maintaining aspect ratio.
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            self.img = Image.open(file_path)
            self.img = self.img.convert("RGBA")
            self.original_img = self.img.copy()
            self.img = self.resize_image(self.img, (700, 500))
            self.display_image(self.img)

    def add_text_watermark(self):
        """
        Add a text watermark to the currently opened image, replacing any existing watermark.
        """
        if self.original_img:
            self.img = self.original_img.copy()
            text = self.watermark_text.get()
            if text == "Enter watermark text here":
                return
            width, height = self.img.size
            draw = ImageDraw.Draw(self.img)

            base_font_size = 20
            font_size = int(base_font_size * (width / 700))
            font = ImageFont.truetype("static/PlaywriteFRModerne-Thin.ttf", font_size)
            textbbox = draw.textbbox((0, 0), text, font=font)
            textwidth, textheight = textbbox[2] - textbbox[0], textbbox[3] - textbbox[1]

            x = 50
            y = height - textheight - 50

            outline_color = "black"
            draw.text((x - 1, y - 1), text, font=font, fill=outline_color)
            draw.text((x + 1, y - 1), text, font=font, fill=outline_color)
            draw.text((x - 1, y + 1), text, font=font, fill=outline_color)
            draw.text((x + 1, y + 1), text, font=font, fill=outline_color)

            draw.text((x, y), text, font=font, fill=self.font_color)
            self.img = self.resize_image(self.img, (700, 500))
            self.display_image(self.img)

    def add_logo_watermark(self):
        """
        Add a logo watermark to the currently opened image, replacing any existing watermark.
        """
        if self.original_img:
            logo_path = filedialog.askopenfilename()
            if logo_path:
                self.img = self.original_img.copy()
                logo = Image.open(logo_path)
                logo = logo.convert("RGBA")

                logo_width, logo_height = logo.size
                max_width = self.img.size[0] // 5
                scaling_factor = max_width / logo_width
                new_size = (int(logo_width * scaling_factor), int(logo_height * scaling_factor))
                logo = logo.resize(new_size, Image.LANCZOS)

                width, height = self.img.size
                logo_x = 4
                logo_y = height - new_size[1] - 4

                self.img.paste(logo, (logo_x, logo_y), logo)
                self.img = self.resize_image(self.img, (700, 500))
                self.display_image(self.img)

    def save_image(self):
        """
        Save the currently edited image to a file.
        """
        if self.img:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.img.save(file_path)

    def resize_image(self, img, size):
        """
        Resize the image to fit within the given size while maintaining the aspect ratio.

        Args:
            img (PIL.Image): The image to resize.
            size (tuple): The desired size as (width, height).

        Returns:
            PIL.Image: The resized image.
        """
        img.thumbnail(size, Image.LANCZOS)
        return img

    def display_image(self, img):
        """
        Display the given image in the Tkinter window, centered.

        Args:
            img (PIL.Image): The image to display.
        """
        self.tk_img = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        img_width, img_height = img.size
        x = (canvas_width - img_width) // 2
        y = (canvas_height - img_height) // 2
        self.canvas.create_image(x, y, anchor=tk.NW, image=self.tk_img)

    def resize_canvas(self, event):
        """
        Resize the canvas to fit the window, adjusting the displayed image size.
        """
        if self.img:
            new_width = event.width
            new_height = event.height
            resized_img = self.resize_image(self.img.copy(), (new_width, new_height))
            self.display_image(resized_img)

    def clear_placeholder(self, event):
        """
        Clear the placeholder text when the entry field gains focus.
        """
        if self.watermark_text.get() == "Enter watermark text here":
            self.watermark_text.delete(0, tk.END)

    def add_placeholder(self, event):
        """
        Add the placeholder text when the entry field loses focus.
        """
        if not self.watermark_text.get():
            self.watermark_text.insert(0, "Enter watermark text here")

    def apply_font_style(self, color):
        """
        Apply the selected font color.

        Args:
            color (str): The selected font color in hex format.
        """
        self.font_color = color
        self.add_text_watermark()

