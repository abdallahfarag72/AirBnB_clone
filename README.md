# AirBnB Clone Console Project

This project is an AirBnB clone console application that serves as the first step towards building a full web application. It provides a command interpreter to manage AirBnB objects and implements a storage engine for serialization and persistence.

## Getting Started

These instructions will guide you on how to set up and run the AirBnB clone console project on your local machine for development and testing purposes.

### Prerequisites

To run this project, you need to have Python installed on your machine.

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/YoussefMorad1/AirBnB_clone.git
```

2. Navigate to the project directory:

```bash
cd AirBnB_clone
```

## Usage

To use the AirBnB clone console, follow the instructions below:

1. Run the console script:

```bash
./console.py
```

2. Once the console is running, you will see the prompt `(hbnb)`. You can now enter commands to manage AirBnB objects.

3. Use the `help` command to view the available commands and their usage.

4. Enter the desired commands to create, update, destroy, or retrieve AirBnB objects.

5. To exit the console, use the `quit` command or press Ctrl + C.

## Example

Here's an example of how you can use the AirBnB clone console:

```bash
$ python console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create User
184cf151-4d53-4c5f-9f91-3c6d44c6c9ef
(hbnb) show User 184cf151-4d53-4c5f-9f91-3c6d44c6c9ef

[User] (184cf151-4d53-4c5f-9f91-3c6d44c6c9ef) {'id': '184cf151-4d53-4c5f-9f91-3c6d44c6c9ef', 'created_at': datetime.datetime(2023, 7, 16, 10, 0, 0), 'updated_at': datetime.datetime(2023, 7, 16, 10, 0, 0)}

(hbnb) quit
$
```

## Authors

- [Youssef Morad](https://github.com/YoussefMorad1)
- [Abdallah Azzam](https://github.com/abdallahfarag72)
