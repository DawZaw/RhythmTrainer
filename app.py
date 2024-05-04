import time
import ctypes
import customtkinter as ctk

from metronome import Metronome
from note_display import NoteDisplay
from tempo_selector import TempoSelector

ctk.set_appearance_mode("Dark")

class App:
    def __init__(self) -> None:
        self.root: ctk.CTk = ctk.CTk()
        self.width: int = 400
        self.height: int = 230

        self.root.geometry(self.center_window())
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")
        self.root.title("Rhythm Trainer")

        # Components
        self.notes: NoteDisplay = NoteDisplay(self.root)
        self.tempo: TempoSelector = TempoSelector(self.root)
        self.metronome: Metronome = Metronome(self.root)

    def update(self) -> None:
        # Get bpm from tempo selector
        # schedule next image update and beep
        start: float = time.perf_counter()
        bpm: int = self.tempo.get()
        tick: int = self.bpm_to_ms(bpm)
        self.notes.update_image()
        self.metronome.beep()
        delta: int = int(time.perf_counter() - start) * 1000
        self.root.after(tick - delta, self.update)

    def get_screensize(self) -> tuple[int, int]:
        # Gets main monitor resolution
        user32: ctypes.WinDLL = ctypes.windll.user32
        width: int = int(user32.GetSystemMetrics(0))
        height: int = int(user32.GetSystemMetrics(1))
        return width, height

    def center_window(self) -> str:
        # Calculates app window position
        screensize: tuple[int, int] = self.get_screensize()
        x_offset: int = (screensize[0] - self.width) // 2
        y_offset: int = (screensize[1] - self.height) // 2
        return f"{self.width}x{self.height}+{x_offset}+{y_offset}"

    def bpm_to_ms(self, bpm: int) -> int:
        return round(60000 / bpm)

    def mainloop(self) -> None:
        self.root.mainloop()
