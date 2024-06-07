# Efesto
Build CLI/API toolkits

## Project structure
```text
src/
├── cmd
│   ├── gitlab_group_owners.py
│   ├── gitlab_terraform_modules.py
│   └── ...
├── data_sources
│   ├── confluence.py
│   ├── gitlab.py
│   └── ...
├── utils
│   ├── logger.py
│   ├── objects.py
│   └── ...
│
├── main.py
```
### data_sources
Contains the logic to connect, authenticate, get and manipulate information of the different sources (like confluence or gitlab).

### cmd
This folder contains command definitions which use data_sources and utils to run repeatable and parameterizable tasks.

### utils
Offers generic functions and tool configurations to be used across the project.

### main.py
The main entry point of the project. Use [click](https://click.palletsprojects.com) to run the cmd definitions and handle parameters.

## Contributing
- Every function must be documented by using docstrings.
- Test are optional.
- Run `make lint` before commiting to ensure that the code is clean and there are no errors.
- Run `make docs` to generate the documentation.

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

