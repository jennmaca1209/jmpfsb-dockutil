#!/tmp/python

import os
import os
import subprocess

# download dockutil script
dockpy = 'curl -o /tmp/dockutil "https://raw.githubusercontent.com/kcrawford/dockutil/master/scripts/dockutil"'
os.system(dockpy)

# change owner of dockutil
chngowner = 'chown root /tmp/dockutil'
os.system(chngowner)

# make dockutil executable
chngperm = 'chmod +x /tmp/dockutil'
os.system(chngperm)

def dockutil(type, itempath, norestart):
    if norestart is True:
        cmd = ['/tmp/dockutil', type, itempath, '--no-restart']
    else:
        cmd = ['/tmp/dockutil', type, itempath]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        output, err = proc.communicate()
        return output
    except Exception:
        return None


def dockutilFolder(type, itempath, norestart, sorttype):
    if norestart is True:
        cmd = ['/tmp/dockutil', type, itempath, '--sort', sorttype,
               '--no-restart']
    else:
        cmd = ['/tmp/dockutil', type, itempath, '--sort', sorttype]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        output, err = proc.communicate()
        return output
    except Exception:
        return None


def main():
    # Remove all dock items.
    dockutil('--remove', 'all', True)

    # Add the paths of the items you want to add to the dock here.
    applist = [
        "/Applications/Google Chrome.app",
        "/System/Applications/App Store.app",
        "/System/Applications/Managed Software Center.app",
        "/System/Applications/System Preferences.app",
        "/System/Applications/Utilities/Activity Monitor.app",
        "/System/Applications/Utilities/Console.app",
        "/System/Applications/Utilities/Disk Utility.app",
        "/System/Applications/Utilities/Migration Assistant.app",
        "/System/Applications/Utilities/Terminal.app",
        ]
    for itempath in applist:
        if os.path.isdir(itempath):
            dockutil('--add', itempath, True)

    # Tell dockutil to restart and finally update the dock.
    dockutilFolder('--add', '~/Downloads', False, 'name')


if __name__ == '__main__':
    main()