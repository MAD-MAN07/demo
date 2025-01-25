# Insecure Python Script Example

This repository contains a Python script that demonstrates various security vulnerabilities commonly found in software development. The script includes examples of insecure file access, weak hashing algorithms, unsanitized user input, command injection vulnerabilities, and predictable random number generation.

## Table of Contents

- [Overview](#overview)
- [Vulnerabilities](#vulnerabilities)
- [Usage](#usage)
- [License](#license)

## Overview

The script showcases the following functions, each containing a specific security hotspot:

1. **Insecure File Read**: Reads a file without proper validation or error handling.
2. **Weak Hashing**: Uses MD5 for hashing passwords, which is considered insecure.
3. **Insecure Input**: Accepts user input without sanitization, making it vulnerable to injection attacks.
4. **Command Injection**: Executes system commands based on user input, which can lead to arbitrary command execution.
5. **Insecure Random**: Uses a predictable method for generating random bytes.

## Vulnerabilities

### 1. Insecure File Access
The `insecure_file_read` function reads a file without checking if the file path is safe or valid.

### 2. Weak Hashing Algorithm
The `weak_hashing` function uses MD5, which is not suitable for secure password storage due to its vulnerability to collision attacks.

### 3. Unsanitized User Input
The `insecure_input` function directly uses user input in a print statement, which can lead to injection attacks.

### 4. Command Injection Vulnerability
The `command_injection` function executes system commands without validation, allowing for potential command injection.

### 5. Predictable Random Number Generation
The `insecure_random` function uses `os.urandom`, which is generally secure, but the context of its use may lead to predictability if not handled properly.

## Usage

To run the script, ensure you have Python installed on your machine. You can execute the script using the following command:

```bash
python script.py
