import sys
from installer.installer import Installer

if __name__ == "__main__":
    app: Installer = Installer(*sys.argv)
