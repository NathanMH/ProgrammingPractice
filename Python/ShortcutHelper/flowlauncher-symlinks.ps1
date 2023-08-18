param([switch]$Elevated)

function Test-Admin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
    $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

if ((Test-Admin) -eq $false)  {
    if ($elevated) {
        # tried to elevate, did not work, aborting
    } else {
        Start-Process powershell.exe -Verb RunAs -ArgumentList ('-noprofile -noexit -file "{0}" -elevated' -f ($myinvocation.MyCommand.Definition))
    }
    exit
}

'running with full privileges'


New-Item -ItemType SymbolicLink -Path "C:\Users\natha\Desktop\PortableApps\FlowLauncher\app-1.16.0\UserData\Plugins\Shortcuts\main.py" -Target "C:\Users\natha\Desktop\GIT REPOS\ProgrammingPractice\Python\ShortcutHelper\main.py";
New-Item -ItemType SymbolicLink -Path "C:\Users\natha\Desktop\PortableApps\FlowLauncher\app-1.16.0\UserData\Plugins\Shortcuts\ShortcutParse.py" -Target "C:\Users\natha\Desktop\GIT REPOS\ProgrammingPractice\Python\ShortcutHelper\ShortcutParse.py";
New-Item -ItemType Junction -Path "C:\Users\natha\Desktop\PortableApps\FlowLauncher\app-1.16.0\UserData\Plugins\Shortcuts\json" -Target "C:\Users\natha\Desktop\GIT REPOS\ProgrammingPractice\Python\ShortcutHelper\json\";
