import os
import pathlib

python_folder = pathlib.Path(__file__)
folder = python_folder.parent.parent.resolve()
assets_folder = os.path.join(folder, "assets")