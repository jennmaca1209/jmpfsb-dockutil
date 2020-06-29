#!/tmp/python

import os
import os
import subprocess

dockpy = 'curl -o /tmp/dockutil "https://raw.githubusercontent.com/kcrawford/dockutil/master/scripts/dockutil"'
# movefile = 'sudo cp /tmp/dockutil /tmp/'
chngowner = 'chown root /tmp/dockutil'
chngperm = 'chmod +x /tmp/dockutil'

os.system(dockpy)
# os.system(movefile)
os.system(chngowner)
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
        '/System/Applications/Utilities/Terminal.app',
        '/Applications/Visual Studio Code.app',
        '/Applications/VMware Fusion.app',
        '/Applications/Microsoft Edge.app',
        ]
    for itempath in applist:
        if os.path.isdir(itempath):
            dockutil('--add', itempath, True)

    # Tell dockutil to restart and finally update the dock.
    dockutilFolder('--add', '/System/Downloads', False, 'name')


if __name__ == '__main__':
    main()