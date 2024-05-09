from cli.main import UniApp
from gui.main import GuiUniApp

if __name__ == "__main__":
    # UniApp().main()
    app = GuiUniApp()
    app.main()
    app.mainloop()
