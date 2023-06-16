
# Real-time Pi Digits Printer

This Python program prints the digits of π (pi) in real-time.

This project is inspired by: 

[![](https://yt3.ggpht.com/Ix1t-egztS9ShZu47IHd2crBzrwd3xeXBQ0nW-Del_Gw0Pw51Bli23K3wjJCpjdawlGI_qW8=s48-c-k-c0x00ffffff-no-rj)](https://www.youtube.com/@winningsequence)
[WinningSequence's](https://www.youtube.com/@winningsequence) "CAN THE NUMBER π BEAT POKÉMON?" where the number π controls Pokémon Sapphire via its digits. Which is streamed live on [twitch](https://www.twitch.tv/winningsequence). I wanted to make something similar to this with some different games, so naturally I asked for the source code on the stream and left a comment on the latest video from the channel. After getting no response I just decided to make it myself! So here I am trying to do something that I actually like in my summer holidays. My predictions are that this project would be ready in about a two weeks from now that is roughly 31st of June, 2023. The project started on 7th of June, 2023 for context.


The .ipynb file gets updated regularly after making changes but the .py file gets updated at the end of my coding hours, because I code primary in jupyter notebook and keep on pushing the files to GitHub as I make small changes (I know it is not the best and can be improved but it is what it is) and when I am off for the day I just download it as .py and upload them to this repository. So yeah, that's how this works. Contact me if you want to use my code and read the MIT License below!

## Prerequisites

- Python 3.x
- `mpmath` library (install using `pip3 install mpmath`)

## Usage

1. Clone the repository or download the `pi.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `pi.py` file is located.
4. Run the program.
5. The program will start printing the digits of π in real-time, with a sliding window of digits and a stationary pointer.
6. Edit the code as per your needs!

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
This program utilizes the ``mpmath`` library to generate the digits of π. The library provides a high-precision arithmetic module for Python.
