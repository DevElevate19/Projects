# File Compressor

A Python-based file compression and decompression tool that uses ASCII character substitution and word optimization techniques to reduce file size.

## Overview

This project was started just before midsem examinations and developed somewhat during the midsem period. The main challenge was handling ASCII code substitution for word optimization - while implementing the compression was straightforward, undoing those changes during decompression proved to be quite difficult.

## Features

- File compression using double space replacement with ASCII characters
- Word optimization for formal documents with repeating words
- Support for both custom compression and 7-Zip integration
- Automatic file extension recognition
- Error handling for various file operations

## Requirements

- Python 3.x
- 7-Zip (optional, for enhanced compression)

## Installation

1. Clone this repository
2. Run the application:
   ```
   python file_compressor.py
   ```

## Usage

The application will prompt you for:

1. Operation type (Compression or Decompression)
2. Whether to use 7-Zip compression
3. File path for compression/decompression
4. Word optimization preference (for formal documents)

## Development Challenges

The primary challenge was ASCII code handling during word optimization. The compression process replaces frequently used words with non-printable ASCII characters, but reversing this process during decompression required careful string parsing and character handling.

## Known Issues

- Word optimization may sometimes increase file size for small files, as the word mapping list can be larger than the space saved by ASCII substitution
- The program may encounter errors if the input file already contains the specific ASCII characters used for compression
- Limited to single file processing currently

## Limitations

- External modules like pickle were not used due to project constraints, making data serialization more complex
- Limited experience with argparse resulted in basic command-line interface
- Currently exhausted from development and not in condition to continue adding features like multiple file input support

## Future Improvements

- Add support for multiple file compression
- Implement better command-line argument parsing
- Use pickle for more efficient data serialization
- Add file size analysis to determine if word optimization is beneficial
- Improve ASCII character conflict detection

## Author

Created by DevElevate19