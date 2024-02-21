import platform, urllib.request, subprocess, os
class DllMerge:
    def __init__(self):
        self.program_name = "ILMerge.exe"
        self.path = os.path.dirname(os.path.abspath(__file__))
    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
    def check_installation(self) -> bool:
        destination = "./ILMerge.exe"
        if os.path.exists(destination):
            return True
        else:
            return False
    def hide_file(self, file_path):
        if platform.system() == 'Windows':
            try:
                os.system("attrib +h \"" + file_path + "\"")
            except Exception as e:
                print(e)
                print("Failed to hide file.")
        else:
            try:
                os.system("chmod 700 \"" + file_path + "\"")
            except Exception as e:
                print(e)
                print("Failed to hide file.")
    def install(self):
        print('Installing ILMerge...')
        url = "https://raw.githubusercontent.com/ethanperrine/downloadbles/main/ILMerge.exe"
        try:
            urllib.request.urlretrieve(url, os.path.join(os.getcwd(), self.program_name))
            print(os.path.join(os.getcwd(), self.program_name))
            self.hide_file(os.path.join(os.getcwd(), self.program_name))
        except Exception as e:
            print(e)
            input("Failed to install ILMerge to the current working directory.\nPress enter to exit.")
            exit(1)
        print('ILMerge has been installed to the current working directory.')
    def merge(self, input_path: str, output: str):
        try:
            list_of_dlls = []
            ILMerge_Path = os.path.join(".", "ILMerge.exe")
            input_dir = os.path.dirname(input_path)
            original_exe = os.path.basename(input_path)
            for filename in os.listdir(input_dir):
                if filename.endswith(".dll"):
                    path = os.path.join(input_dir, filename)
                    path = path.replace('\\\\', '\\')
                    list_of_dlls.append(f'"{path}"')
            full_output_path = os.path.join(input_dir, output)
            if not full_output_path.endswith(".exe"):
                full_output_path += ".exe"
            dlls_string = ' '.join(list_of_dlls)
            command = f"\"{ILMerge_Path}\" /copyattrs /targetplatform:4.0,\"C:\Windows\Microsoft.NET\Framework\\v4.0.30319\" /out:\"{full_output_path}\" \"{os.path.join(input_dir, original_exe)}\" {dlls_string}"
            print("Executing command:", command)
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                print("Error:", result.stderr)
                input("Failed to merge the files.\nPress enter to exit.")
                exit(1)
            else:
                print("Merge successful\nPress Enter to exit.")
        except Exception as e:
            print(e)
            input("Failed to merge the files.\nPress enter to exit.")
            exit(1)
    def main(self):
        if not self.check_installation():
            self.install()
        else:
            print('ILMerge is already installed in PATH, skipping installation')
        self.clear()
        path = input('Enter the path to the folder containing the .exe and .dll files: ')
        output = input('Enter the name of the output file: ')
        self.merge(path, output)
        input()
if __name__ == '__main__':
    DllMerge().main()
