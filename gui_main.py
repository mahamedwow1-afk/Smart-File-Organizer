import customtkinter as ctk
from tkinter import filedialog, messagebox
from pathlib import Path
from core.scanner import scan_files
from core.organizer import build_organization_plan, execute_organization, undo_last

ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue")

class SmartOrganizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart Organizer Pro - by Mahamed Yasser")
        self.geometry("700x550")
        
        # محاولة وضع الأيقونة لو الملف موجود
        try:
            self.iconbitmap("icon.ico")
        except:
            pass

        # --- Header ---
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(pady=20, padx=20, fill="x")

        self.title_label = ctk.CTkLabel(self.header_frame, text="✨ Smart Organizer", font=("Segoe UI", 28, "bold"))
        self.title_label.pack(side="left")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.header_frame, values=["Dark", "Light"],
                                                      command=self.change_appearance_mode)
        self.appearance_mode_menu.pack(side="right")

        # --- Main Frame ---
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=10, padx=30, fill="both", expand=True)

        self.path_var = ctk.StringVar(value="No folder selected...")
        self.entry_path = ctk.CTkEntry(self.main_frame, textvariable=self.path_var, width=450)
        self.entry_path.grid(row=0, column=0, padx=20, pady=30)

        self.browse_btn = ctk.CTkButton(self.main_frame, text="📁 Browse", command=self.browse_folder, width=100)
        self.browse_btn.grid(row=0, column=1, padx=10)

        self.btn_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.btn_frame.grid(row=1, column=0, columnspan=2, pady=10)

        self.organize_btn = ctk.CTkButton(self.btn_frame, text="🚀 Start Organizing", command=self.run_organizer, 
                                          fg_color="#2ecc71", hover_color="#27ae60", font=("Segoe UI", 16, "bold"))
        self.organize_btn.pack(side="left", padx=10)

        self.undo_btn = ctk.CTkButton(self.btn_frame, text="↩️ Undo Cleanup", command=self.run_undo,
                                      fg_color="#e74c3c", hover_color="#c0392b")
        self.undo_btn.pack(side="left", padx=10)

        self.log_box = ctk.CTkTextbox(self.main_frame, width=600, height=120)
        self.log_box.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
        
        # --- Footer (Your Name) ---
        self.footer_label = ctk.CTkLabel(self, text="Developed with ❤️ by Mahamed Yasser", font=("Segoe UI", 12, "italic"), text_color="gray")
        self.footer_label.pack(side="bottom", pady=10)

    def change_appearance_mode(self, mode):
        ctk.set_appearance_mode(mode)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_var.set(folder)

    def run_organizer(self):
        folder = self.path_var.get()
        if folder == "No folder selected...": return
        files = scan_files(folder)
        if not files: return
        plan = build_organization_plan(files, folder)
        execute_organization(plan, folder)
        messagebox.showinfo("Success", f"Done! Organized by Mahamed Yasser")

    def run_undo(self):
        folder = self.path_var.get()
        if folder == "No folder selected...": return
        undo_last(folder)
        messagebox.showinfo("Undo", "Action reversed successfully.")

if __name__ == "__main__":
    app = SmartOrganizerApp()
    app.mainloop()