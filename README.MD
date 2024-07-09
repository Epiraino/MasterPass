# MasterPass Password Manager

MasterPass is a secure and easy-to-use password manager that helps you store and manage your passwords in a secure manner. Built with Python and utilizing advanced encryption standards, MasterPass ensures that your passwords are stored safely and are accessible only to you.

## Features

- **Secure Storage**: Encrypts and stores passwords securely using AES encryption.
- **Password Generation**: Generates strong, customizable passwords.
- **Easy Management**: Add, retrieve, delete, and list passwords for different services.
- **Command-Line Interface**: Simple and intuitive command-line interface for managing passwords.

## Installation

To get started with MasterPass, follow these steps:

1. Ensure you have Python installed on your system. MasterPass requires Python 3.6 or later.
2. Clone the repository to your local machine:
3. Navigate to the MasterPass directory:
4. Install the required Python packages:
## Usage

To use MasterPass, run the `password_manager.py` script from the command line:
Follow the on-screen prompts to manage your passwords. The options include:

1. **Add Password**: Add a new password for a service. You can choose to input your own password or generate a new one.
2. **Get Password**: Retrieve a password for a specific service.
3. **Delete Password**: Delete a stored password for a service.
4. **List Services**: List all services for which passwords are stored.
5. **Change Master Password**: Securely change the master password.
6. **Exit**: Exit the application.

## Security

MasterPass uses AES encryption for securing your passwords. The encryption key is generated and stored securely on your system. It's crucial to not share or lose the encryption key as it is essential for decrypting your passwords.

## Contributing

Contributions to MasterPass are welcome! If you have suggestions for improvements or bug fixes, please open an issue or submit a pull request.

## License

MasterPass is released under the MIT License. See the LICENSE file for more details.