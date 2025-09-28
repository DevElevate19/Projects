# File Compressor

A Python-based file compression and decompression tool that uses ASCII character substitution and word optimization techniques to reduce file size, with optional 7-Zip integration.

## Overview

This project was started just before midsem examinations and developed during the midsem period. The main challenge was handling ASCII code substitution for word optimization - while implementing the compression was straightforward, undoing those changes during decompression proved to be quite difficult.

## Features

- **Custom Compression Algorithm**: Uses double space replacement with ASCII characters (`\x1f`)
- **Word Optimization**: Replaces the 10 most frequent words with non-printable ASCII characters (`\x00` to `\x09`)
- **7-Zip Integration**: Optional external compression using 7-Zip or WinRAR
- **Dual Compression Modes**: Choose between custom algorithm or 7-Zip compression
- **Automatic File Extension Recognition**: Maintains original file extensions with compression suffixes
- **Interactive CLI**: User-friendly prompts for all operations
- **Error Handling**: Comprehensive exception handling for file operations

## Requirements

- Python 3.x
- 7-Zip (optional, for enhanced compression)
- WinRAR (alternative to 7-Zip, optional)

## Installation

1. Clone this repository
2. Ensure 7-Zip is installed in default location (`C:\Program Files\7-Zip\7z.exe`) or have custom path ready
3. Run the application:
   ```
   python file_compressor.py
   ```

## Usage

The application provides an interactive interface that prompts for:

1. **Operation Type**: Choose between 'Compression' or 'Decompression'
2. **Compression Method**: Option to use 7-Zip for better compression ratios
3. **File Path**: Input file for compression or compressed file for decompression
4. **Word Optimization**: Enable for formal documents with repetitive words (custom compression only)
5. **Custom 7-Zip Path**: If 7-Zip is not in default location

### Custom Compression Features
- Replaces double spaces with `\x1f` character
- Identifies and replaces 10 most frequent words with ASCII codes
- Stores word mapping at end of file for decompression

### 7-Zip Integration
- Uses subprocess to call 7-Zip executable
- Supports both compression and extraction
- Fallback to custom path if default installation not found

## Development Challenges

1. **ASCII Code Handling**: The primary challenge was managing ASCII character substitution during word optimization and ensuring proper reversal during decompression
2. **String Parsing**: Converting word lists to strings and back without using pickle module
3. **7-Zip Size Detection**: **Major Issue** - Unable to programmatically determine the size of decompressed files from 7-Zip archives, which limits size comparison functionality
4. **Character Conflicts**: Handling cases where input files contain the specific ASCII characters used for compression

## Known Issues

- **7-Zip Size Limitation**: Cannot determine decompressed file size from 7-Zip archives programmatically, preventing accurate compression ratio calculations
- Word optimization may increase file size for small files due to word mapping overhead
- Program may fail if input files contain compression ASCII characters (`\x00`-`\x09`, `\x1f`)
- Limited to single file processing
- Decompression only works for files compressed by this specific program

## Technical Implementation

- **Word Counter Function**: Analyzes text frequency and returns sorted word list
- **Compression Class**: Handles both custom and 7-Zip compression methods
- **Subprocess Integration**: Uses `subprocess.run()` for 7-Zip operations
- **File Extension Handling**: Automatic recognition and preservation of file types
- **Error Handling**: Try-catch blocks for robust operation

## Limitations

- No external compression modules used (project constraint)
- Basic CLI interface due to limited argparse experience
- No pickle module for data serialization (project constraint)
- Single file processing only
- **7-Zip size detection not implemented** due to complexity in parsing 7-Zip output

## Future Improvements

- Implement 7-Zip archive size analysis for compression ratio calculations
- Add support for multiple file compression
- Implement proper command-line argument parsing with argparse
- Use pickle for efficient word mapping serialization
- Add pre-compression analysis to determine if word optimization is beneficial
- Improve ASCII character conflict detection and resolution
- Add progress bars for large file operations
- Implement compression ratio reporting

## Author

Created by DevElevate19

## Notes

- The 7-Zip size detection issue remains unresolved - while compression and decompression work perfectly, getting the exact decompressed size from 7-Zip archives programmatically proved challenging
- Project constraints prevented use of external modules that could have simplified implementation