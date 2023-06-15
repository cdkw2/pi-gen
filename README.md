# Real-time Pi Digits Printer

This Python program prints the digits of π (pi) in real-time, displaying a sliding window of digits with a stationary pointer.

## Prerequisites

- Python 3.x
- `mpmath` library (install using `pip3 install mpmath`)

## Usage

1. Clone the repository or download the `pi.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `pi.py` file is located.
4. Run the program using the following command:
5. The program will start printing the digits of π in real-time, with a sliding window of digits and a stationary pointer.
6. By default, it will display the next 7 digits of π and update every second. You can modify the num_digits and update_interval parameters in the code to adjust the number of digits and the update interval.

## Example Output
Here's an example of the program's output:

``` 
1 |4 |1 |5 |9 |2 |6
         ^
4 |1 |5 |9 |2 |6 |5
         ^
1 |5 |9 |2 |6 |5 |3
         ^
5 |9 |2 |6 |5 |3 |5
         ^
9 |2 |6 |5 |3 |5 |8
         ^
2 |6 |5 |3 |5 |8 |9
         ^
6 |5 |3 |5 |8 |9 |7
         ^
5 |3 |5 |8 |9 |7 |9
         ^
3 |5 |8 |9 |7 |9 |3
         ^
 ```
 
# License
This project is licensed under the MIT License which can be viewed by entering this string in your browser:
```
data:text/html;base64,PHA+Ck1JVCBMaWNlbnNlCjxicj4KPGJyPgpDb3B5cmlnaHQgKGMpIDIwMjMgQ0RLVzIKPGJyPgo8YnI+ClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCjwvcD4=
```

Feel free to modify and use this code according to your needs.

## Acknowledgements
This program utilizes the mpmath library to generate the digits of π. The library provides a high-precision arithmetic module for Python.