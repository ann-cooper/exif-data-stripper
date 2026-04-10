# Exif Stripper with Copyright
Remove exif data (which can include things like location and date) from photos and add copyright info. 

My repos are all human coded. There is no AI-generated code anywhere in this project, or in any of my projects.

## References

- This article inspired the addition of artist and copyright info to the exif data: https://medium.com/@ssjewcw/unlocking-image-metadata-5-ways-to-read-and-modify-image-exif-metadata-with-python-933fb5418b43
- This repo heavily informed the core functionality: https://github.com/stefmolin/exif-stripper

## Usage
### Note
- This is for photographers processing their own images.
- This tool displays the original and updated exif data as it works. Non-standard exif tags might have values that don't display legibly.

### In a virtual environment
- Install the package in a virtual environment
    - For help setting up a virtual environment, see [Virtual environment](#local-python-environment)
- Activate the virtual environment 
    - Make sure that the package has been installed in the [Virtual environment](#virtual-environment) 
- Run `exif-cli` in a terminal
    - To display the help text for the cli options, run `exif-cli --help`

### In a Docker container
- Make sure Docker is running if you're doing this locally!
- In a terminal, cd into the project directory and run `docker build -t exiftool.`
- Then run `docker run --rm -it exiftool`
## Testing

## Local Python environment
- Installing and using Pyenv tutorial: https://realpython.com/intro-to-pyenv
- Pyenv docs: https://github.com/pyenv/pyenv#readme

### Updating Requirements
- To output a new requirements.txt from updates in requirements.in: `pip-compile requirements.in --output-file=- > requirements.txt`

### Virtual environment
- Activate the virtual environment and install the requirements and the project
`pip install -r requirements.txt`
`pip install .`

