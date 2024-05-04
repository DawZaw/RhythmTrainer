import glob
from PIL import Image
from random import randint
import customtkinter as ctk


class NoteDisplay:
    def __init__(self, root: ctk.CTk) -> None:
        self.root: ctk.CTk = root
        self.images: list[ctk.CTkImage] = self.load_images()

        self.current: ctk.CTkLabel = ctk.CTkLabel(
            self.root,
            text="",
            image=self.images[1],
        )
        self.current.grid(row=0, column=0, columnspan=2)

        self.next: ctk.CTkLabel = ctk.CTkLabel(
            self.root,
            text="",
            image=self.images[1],
        )
        self.next.grid(row=0, column=2, columnspan=2)

    def load_images(self) -> list[ctk.CTkImage]:
        # Preloads all subdivision images
        return [
            ctk.CTkImage(
                dark_image=Image.open(subdivision),
                size=(200, 150),
            )
            for subdivision in glob.glob("subdivisions/*")
        ]

    def update_image(self) -> None:
        # Replace current subdivision with next, generate new next
        index: int = randint(0, len(self.images) - 1)
        self.current.configure(image=self.next._image)
        self.next.configure(image=self.images[index])
