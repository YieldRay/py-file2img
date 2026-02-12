# py-file2img

```sh
git clone https://github.com/YieldRay/py-file2img
cd py-file2img

# install dependencies with uv
uv sync
```

## CLI

```sh
uv run file2img-cli encode <file_path> <image_path>
uv run file2img-cli decode <image_path> <file_path>
```

## GUI

```sh
uv run file2img-gui
```

or build the GUI to an executable by command `pyinstaller gui.py -w`  
then the executable file should be in `./dist` after the build
