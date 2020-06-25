$ErrorActionPreference = "Stop"
# fix vmware tools install
# |out-null is used to wait for the process to finish.
e:\setup64 /x|Out-Null
$tmp = [System.IO.Path]::GetTempPath()
cd $tmp
cd *setup
msiexec /fa "VMware Tools64.msi" REBOOT=R /norestart |Out-Null

    
# Switch network connection to private mode
# Required for WinRM firewall rules
$profile = Get-NetConnectionProfile
Set-NetConnectionProfile -Name $profile.Name -NetworkCategory Private

# Enable WinRM service
winrm quickconfig -quiet
winrm set winrm/config/service '@{AllowUnencrypted="true"}'
winrm set winrm/config/service/auth '@{Basic="true"}'

# Reset auto logon count
# https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-shell-setup-autologon-logoncount#logoncount-known-issue
Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon' -Name AutoLogonCount -Value 0
