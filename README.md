# Junkfile organizer

Junkfile organizer is a Software to arrange files

## Installation

Clone the repository in any local folder
```bash
git clone https://github.com/IvanFrezzaJr/singleton.git
```
I used package manager [pipenv](https://pipenv.readthedocs.io/en/latest/). You could execute the following command to install:

```bash
pip install pipenv
```

Enter in the cloned directory and execute:

### pipenv
```bash
pipenv install
```
### pip
```bash
pip install -r requirements.txt
```

To add path module into Python path execute:
###pipenv
```bash
pipenv install -e  "."
```

###pip
```bash
pip install -e  "."
```

## Usage
You could execute by different styles:

### Standalone
```bash
python standalone.py -h
```

### UI
```bash
python src/junkfile/ui.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)