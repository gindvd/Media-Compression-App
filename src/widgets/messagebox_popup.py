import customtkinter as ctk


class MessageboxPopup(ctk.CTkToplevel):
    """Top level popup for displaying text from text files"""

    def __init__(self, master, title: str, message: str, **kwargs) -> None:
        super().__init__(master=master, **kwargs)
        self._master = master

        self.title(title)
        self.resizable(False, False)

        self._width = 500
        self._height = 600

        self._messagebox = ctk.CTkTextbox(self, wrap="word")
        self._messagebox.pack(expand=True, fill="both", padx=10, pady=10)

        self._messagebox.tag_config("center", justify="center")
        self._messagebox.insert("1.0", message)
        self._messagebox.configure(state="disabled")

        self._close_btn = ctk.CTkButton(self, text="Close", command=self.destroy)

        self._close_btn.pack(side="right", padx=10, pady=10)

        self._master.update()

        self._spawn_x = int(self._master.winfo_width() * .5 + self._master.winfo_x() - .5 * self._width + 7)
        self._spawn_y = int(self._master.winfo_height() * .5 + self._master.winfo_y() - .5 * self._height + 20)

        self.after(10)
        self.geometry(f"{self._width}x{self._height}+{self._spawn_x}+{self._spawn_y}")

        self.lift()
