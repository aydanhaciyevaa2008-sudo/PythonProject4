Password Security Analyzer

A Python-based cybersecurity project that analyzes password security and provides a security score and recommendations.

Features

* Password length analysis
* Uppercase letter detection
* Lowercase letter detection
* Number detection
* Special character detection
* Security score calculation
* Password strength classification
* Common password detection

Project Structure

Password-Security-Analyzer/
│
├── main.py
├── analyzer.py
└── README.md

How It Works

The program asks the user to enter a password and analyzes several security characteristics.

It checks:

* Password length
* Character diversity
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Whether the password is commonly used

The program then calculates a security score and classifies the password as:

* Very Weak
* Weak
* Moderate
* Strong
* Very Strong

Example

Enter your password: HelloWorld123!
Password Analysis
-----------------
Length >= 12: True
Uppercase: True
Lowercase: True
Digit: True
Special character: True
Security Score: 75 / 85
Strength: Strong

Technologies

* Python
* Git
* GitHub

Security & Privacy

Passwords should not be stored or logged.

This project is intended for educational purposes and demonstrates basic password-security analysis concepts.

Future Improvements

* Entropy calculation
* Better password-strength estimation
* Larger common-password database
* Personal-information pattern detection
* Password recommendations
* Flask web interface
* Client-side password analysis
* Unit tests

Disclaimer

This project is intended for educational and defensive cybersecurity purposes.