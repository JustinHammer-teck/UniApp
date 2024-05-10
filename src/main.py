#!/usr/bin/env python3

import argparse
from cli.main import UniApp
from gui.main import GuiUniApp


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Run the application with or without GUI."
    )
    parser.add_argument(
        "-g", "--gui", action="store_true", help="Run the application with GUI."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    if args.gui:
        app = GuiUniApp()
        app.main()
        app.mainloop()
    else:
        UniApp().main()
