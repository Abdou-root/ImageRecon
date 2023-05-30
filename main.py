import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from ttkbootstrap import Style
from PIL import ImageTk, Image

# Creating a new tkinter window
window = tk.Tk()
window.title("Image Recognition Tool")

# Styling of the labels, frames and buttons
style = Style(theme='minty')
style.configure("custom.TButton", bordercolor="#0c6e03",
                relief="raised", padding=10, extra=['shadow'], font=('Sukar', 14, "bold"),
                bd=3, padx=10, pady=15)
style.configure("custom.TFrame", borderless=True)
style.configure("custom.Tlabel", font=("Sukar", 14, "bold"), relief="raised", padding=10, extra=['shadow'],
                bd=3, padx=10, pady=15)
style.configure("custom.Horizontal.TProgressbar", troughcolor="white", bordercolor="gray", dark=(0.3, 0.3, 0.3),
                borderwidth=3)

# Welcome message
welcome_label = ttk.Label(window, text="Welcome to ReconAI, your AI tool!", font=("Sukar", 20, "bold"),
                          style="custom.tlabel")
welcome_label.pack()
# Create file_label before using it in browse_files function
file_label = tk.Label(window, text="Select a file to proceed!", )
file_label.pack(pady=0)


# Handling image selection and display
def browse_files():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text="Selected file: " + file_path)

        # Display the selected image
        img = Image.open(file_path)
        img = img.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo  # Save a reference to prevent garbage collection
    else:
        file_label.config(text="No file selected")


# Function to be defined somewhere in the code (will take file path later)
def process_images():
    return 0


# Creating the GUI components

image_frame = ttk.Frame(window, width=200, height=200, style="custom.TFrame")
image_frame.pack(fill="both", expand=True, pady=20)

image_label = ttk.Label(image_frame, text="Image", font=("Sukar", 14, "bold"), style="custom.tlabel")
image_label.pack()

file_selection_button = ttk.Button(window, text="Browse", command=browse_files, style="custom.TButton")
file_selection_button.pack()

results_label = ttk.Label(window, text="Recognition Results:", font=("Sukar", 14, "bold"), style="custom.tlabel")
results_label.pack(pady=20)

progress_bar = ttk.Progressbar(window, length=200, style="custom.Horizontal.TProgressbar")
progress_bar.pack(pady=10)

feedback_label = ttk.Label(window, text="Feedback Messages:", font=("Sukar", 12, "bold"), style="custom.tlabel")
feedback_label.pack(pady=20)


# Function to handle the "Start Analysis" button click (will be updated)
def start_analysis(file_paths=None):
    # Check if images have been selected
    if not file_paths:
        messagebox.showwarning("Warning", "No images selected.")
        return


# "Start Analysis" button
start_analysis_button = ttk.Button(window, text="Start Analysis", command=start_analysis, style="custom.TButton")
start_analysis_button.pack(pady=20)

# Analysis process and updating progress bar and display results


# Create a menu bar
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=browse_files)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

# Window size
window.geometry("800x700")
window.resizable(True, True)

# Run the GUI
window.mainloop()
