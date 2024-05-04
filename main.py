from app import App

APP: App = App()


def main() -> None:
    APP.update()
    APP.mainloop()


if __name__ == "__main__":
    main()
