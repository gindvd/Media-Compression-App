import customtkinter as ctk

from collections.abc import Callable
from typing import Any


class ProgressbarPopup(ctk.CTkToplevel):
    """Pop up for displaying progress bar while background task is preformed"""

    def __init__(
        self, 
        master: Any, 
        title: str, 
        command: Callable[[], Any], 
        **kwargs
    ) -> None:
        super().__init__(master, **kwargs)

        self._master = master

        self.title(title)
        self.resizable(False, False)

        self._width = 250
        self._height = 150

        self._bar_frame = ctk.CTkFrame(self, corner_radius=0)

        self._progressbar = ctk.CTkProgressBar(
            self._bar_frame,
            height=15,
            width=300,
            orientation="horizontal",
            mode="indeterminate",
            determinate_speed=0.75,
        )

        self._progressbar.pack(padx=30, pady=50)

        self._bar_frame.pack(expand=True, fill="both")

        self._cancel_btn = ctk.CTkButton(self, text="Cancel", command=command)

        self._cancel_btn.pack(side="right", padx=10, pady=10)

        self._spawn_x = int(self._master.winfo_width() * .5 + self._master.winfo_x() - .5 * self._width + 7)
        self._spawn_y = int(self._master.winfo_height() * .5 + self._master.winfo_y() - .5 * self._height + 20)

        self._master.update()

        self.after(10)
        self.geometry(f"{self._width}x{self._height}+{self._spawn_x}+{self._spawn_y}")

        self.lift()
        self.focus()
        self.grab_set()

        # Cancels compression if progress bar is closed
        self.protocol("WM_DELETE_WINDOW", command)

    def run_progressbar(self) -> None:
        """Starts the progression bar"""
        self._progressbar.start()
        
        self.update_idletasks() 

    def destroy_window(self) -> None:
        """Destroys the popup window"""
        self._progressbar.stop()
        self.destroy()
