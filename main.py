import tkinter as tk
from watermark_processor import WatermarkProcessor

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkProcessor(root)
    root.mainloop()
