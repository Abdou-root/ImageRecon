import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from ttkbootstrap import Style
from PIL import ImageTk, Image
import utils.prediction as prediction


def run_gui():
    # Creating a new tkinter window
    window = tk.Tk()
    window.title("ReconAI")

    # Styling of the labels, frames and buttons
    style = Style(theme='minty')
    style.configure("custom.TButton", bordercolor="#0c6e03",
                    relief="raised", padding=10, extra=['shadow'], font=('Sukar', 14, "bold"),
                    bd=3, padx=10, pady=15)
    style.configure("custom.TFrame", borderless=True)
    style.configure("custom.TLabel", font=("Sukar", 14, "bold"),
                    padx=10, pady=15)
    style.configure("custom.Horizontal.TProgressbar", troughcolor="white", bordercolor="gray", dark=(0.3, 0.3, 0.3),
                    borderwidth=3)

    # Welcome message
    welcome_label = ttk.Label(window, text="Welcome to ReconAI, your AI tool!", font=("Sukar", 24, "bold"),
                              style="custom.TLabel")
    welcome_label.pack()

    # Create file_label before using it in browse_files function
    file_label = ttk.Label(window, text="Select a file to proceed!", style="custom.TLabel", relief="raised")
    file_label.pack(pady=0)

    # Handling image selection and display
    def browse_files():
        file_path = filedialog.askopenfilename()
        if file_path:
            file_label.config(text="Selected file: " + file_path)

            # Display the selected image
            img = Image.open(file_path)
            img = img.resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            image_label.config(image=photo)
            image_label.image = photo  # Save a reference to prevent garbage collection
        else:
            file_label.config(text="No file selected")

    def start_analysis():
        file_path = file_label.cget("text").replace("Selected file: ", "")
        if not file_path:
            messagebox.showwarning("Warning", "No image selected.")
            return

        # Animation for progress bar
        start_analysis_button.config(state="disabled")
        progress_bar.config(mode="determinate", maximum=100)
        animate_progress_bar(0, file_path)
        start_analysis_button.config(state="normal")

    def animate_progress_bar(value, file_path):
        if value <= 100:
            progress_bar["value"] = value
            value += 1
            window.after(20, animate_progress_bar, value, file_path)
        else:
            predicted_class = prediction.predict(file_path)
            feedback_label.config(text=f"Result: {predicted_class}")
            start_analysis_button.config(state="normal")

    # Creating the GUI components
    image_frame = ttk.Frame(window, width=200, height=200, style="custom.TFrame")
    image_frame.pack(fill="both", expand=True, pady=20)

    image_label = ttk.Label(image_frame, text="Image", font=("Sukar", 14, "bold"), style="custom.TLabel")
    image_label.pack()

    file_selection_button = ttk.Button(window, text="Browse", command=browse_files, style="custom.TButton")
    file_selection_button.pack()

    results_label = ttk.Label(window, text="Recognition Results:", font=("Sukar", 14, "bold"), style="custom.TLabel")
    results_label.pack(pady=20)

    progress_bar = ttk.Progressbar(window, length=200, style="custom.Horizontal.TProgressbar")
    progress_bar.pack(pady=10)

    feedback_label = ttk.Label(window, text="The Results will appear HERE!", font=("Sukar", 12, "bold"),
                               style="custom.TLabel")
    feedback_label.pack(pady=20)

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


# Running GUI with main script
if __name__ == "__main__":
    run_gui()
