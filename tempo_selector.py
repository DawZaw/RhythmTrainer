import tkinter as tk
import customtkinter as ctk


class TempoSelector:
    def __init__(self, root: ctk.CTk) -> None:
        self.root: ctk.CTk = root
        self.bpm: tk.IntVar = tk.IntVar(self.root, value=60)

        # Range for BPM slider
        self.low: int = 30
        self.high: int = 200
        self.steps: int = self.high - self.low

        self.bpm_text: ctk.CTkLabel = ctk.CTkLabel(
            self.root,
            font=("", 25, "bold"),
            text=f"{self.bpm.get()}",
        )
        self.bpm_text.grid(row=1, column=0, columnspan=4, pady=(10, 0), padx=(0, 35))

        self.bpm_label: ctk.CTkLabel = ctk.CTkLabel(
            self.root,
            font=("", 12),
            text=f"BPM",
        )
        self.bpm_label.grid(row=1, column=0, columnspan=4, pady=(18, 0), padx=(35, 0))

        self.decrease = ctk.CTkButton(
            self.root,
            width=25,
            height=25,
            text="-",
            font=("", 16, "bold"),
            command=lambda: self.decrease_bpm(),
        )
        self.decrease.grid(row=2, column=0)

        self.bpm_slider: ctk.CTkSlider = ctk.CTkSlider(
            self.root,
            variable=self.bpm,
            number_of_steps=self.steps,
            width=330,
            from_=self.low,
            to=self.high,
            command=lambda _: self.set_bpm(),
        )
        self.bpm_slider.grid(row=2, column=1, columnspan=2)
        self.increase = ctk.CTkButton(
            self.root,
            width=25,
            height=25,
            text="+",
            font=("", 16, "bold"),
            command=lambda: self.increase_bpm(),
        )
        self.increase.grid(row=2, column=3)

    def increase_bpm(self) -> None:
        value: int = int(self.bpm_slider.get()) + 1
        self.update_bpm(value)

    def decrease_bpm(self) -> None:
        value: int = int(self.bpm_slider.get()) - 1
        self.update_bpm(value)

    def set_bpm(self) -> None:
        value: int = int(self.bpm_slider.get())
        self.update_bpm(value)

    def update_bpm(self, value: int) -> None:
        self.bpm.set(value)
        self.bpm_text.configure(text=f"{value}")

    def get(self) -> int:
        return self.bpm.get()
