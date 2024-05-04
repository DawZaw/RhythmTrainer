import winsound
import customtkinter as ctk


class Metronome:
    def __init__(self, root: ctk.CTk) -> None:
        self.root: ctk.CTk = root

        self.pitch: int = 440
        self.duration: int = 50

    def beep(self) -> None:
        winsound.Beep(self.pitch, self.duration)
