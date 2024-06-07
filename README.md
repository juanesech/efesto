# Efesto
Build CLI/API toolkits

## CLI binary requirements
- Python
- [Nuikta](https://nuitka.net/doc/download.html)
   - `pip3 install nuitka`
- patchelf
- gcc
- clang
- ccache (Optional but recommended for faster re-build)

### Building binary
```sh
python3 -m nuitka --onefile cli.py
```
