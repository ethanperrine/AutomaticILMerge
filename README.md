# AutomaticILMerge
Automatically detects all dll in an exe's folder and attempts to merge exe framework applications.

This is a helper tool is designed to handle the merging of DLL files with a .NET framework executable.

## Features
Check if ILMerge is installed in cwd; if not, it will automatically install it from my GitHub. And attempts to hide the ILMerge executable (for a cleaner interface). 
Then, it will prompt the user to enter the path of the folder, OR you can enter the exe itself, and it will automatically detect everything.

If there are any problems, open an issue or make a pull request if you want to update. 
