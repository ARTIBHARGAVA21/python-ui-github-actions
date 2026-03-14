# Python Sample Project

This is a simple Python project demonstrating a basic program structure using a `src` directory. The project is configured to run automatically using GitHub Actions for continuous integration.

## Project Structure

```
.
├── src
│   └── main.py
├── LICENSE
├── MAKEFILE
└── README.md
```

## Description

This project contains a basic Python script located inside the `src` folder. The script can be executed locally or through a CI workflow using GitHub Actions.

## Requirements

* Python 3.8 or above

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/your-username/python-sample-project.git
```

2. Navigate to the project directory

```
cd python-sample-project
```

3. Run the Python program

```
python src/main.py
```

## Continuous Integration

This project uses GitHub Actions to automatically run the Python script whenever code is pushed to the repository.

Workflow file location:

```
.github/workflows/python.yml
```

## License

This project is licensed under the MIT License.
