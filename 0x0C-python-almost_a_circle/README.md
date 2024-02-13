# 0x0C. Python - Almost a circle

## Overview
This project, "Almost a circle", is a part of the Higher level curriculum at ALX, aiming to reinforce Python programming skills, particularly in Object-Oriented Programming (OOP) concepts. It encompasses various aspects such as importing modules, handling exceptions, defining and using classes, implementing inheritance, unit testing with the `unittest` module, file I/O operations, and understanding serialization/deserialization using JSON.

## Background Context
The project is structured around creating classes and methods to manage geometric shapes, primarily rectangles and squares. Each task within the project builds upon the previous ones, gradually expanding functionality and complexity.

## Learning Objectives
- Implement Unit testing for large projects
- Serialization and deserialization of objects
- Reading from and writing to JSON files
- Understanding and utilizing *args and **kwargs in Python functions
- Handling named arguments effectively

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All scripts should be compatible with Python 3.8.5 or above
- Scripts should follow PEP8 guidelines
- All files should end with a new line
- The shebang (`#!/usr/bin/python3`) should be included as the first line in each script
- Scripts should be executable
- Documentation should be provided for modules, classes, and functions

### Python Unit Tests
- Tests should be placed in a folder named `tests`
- Tests should be written using the `unittest` module
- Test files and folders should be named `test_<module>.py` or `test_<module>/test_<class>.py`
- All tests should be discoverable by running `python3 -m unittest discover tests`
- Collaboration on test cases is encouraged

## Repository Structure
- **Directory**: 0x0C-python-almost_a_circle
  - **README.md**: Project overview and instructions
  - **models**:
    - **\_\_init\_\_.py**: Empty file to denote a Python package
    - **base.py**: Contains the `Base` class, the foundation for other classes
    - **rectangle.py**: Implements the `Rectangle` class
    - **square.py**: Implements the `Square` class
  - **tests**: Folder containing unit tests for the project

## Tasks Overview
1. **Base class**: Implementing the base class with a unique id attribute
2. **First Rectangle**: Creating the Rectangle class inheriting from Base with private attributes
3. **Validate attributes**: Adding validation to setters in Rectangle class
4. **Area first**: Implementing the area calculation method for Rectangle
5. **Display #0**: Adding a display method to Rectangle class
6. **__str__**: Overriding the string representation of Rectangle class
7. **Display #1**: Enhancing the display method to consider x and y positions
8. **Update #0**: Implementing an update method for Rectangle class with *args
9. **Update #1**: Updating update method to accept **kwargs
10. **Square class**: Creating Square class inheriting from Rectangle
11. **Square size**: Adding getter and setter for size attribute in Square class
12. **Square update**: Implementing update method for Square class
13. **Rectangle instance to dictionary representation**: Adding method to convert Rectangle to dictionary
14. **Square instance to dictionary representation**: Adding method to convert Square to dictionary
15. **Dictionary to JSON string**: Adding method to convert list of dictionaries to JSON string
16. **JSON string to file**: Adding method to save JSON string to a file
17. **JSON string to dictionary**: Adding method to convert JSON string to list of dictionaries
18. **Dictionary to Instance**: Adding method to create instances from dictionaries

## Repository
- **GitHub Repository**: [alx-higher_level_programming](https://github.com/lamardev/alx-higher_level_programming)
- **Directory**: 0x0C-python-almost_a_circle

## Author
- **Author**: Guillaume
- **Date**: Started on February 8, 2024
- **Deadline**: February 17, 2024

## Status
- Manual QA review pending
- Auto QA review pending

