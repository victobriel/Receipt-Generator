import os,sys,zipfile,subprocess,psutil,logging,time

class Installer:
    def __init__(self, *argv) -> None:
        self._pid: str = argv[1]
        self._start: str = argv[2]
        self._end: str = argv[3]
        self._start_log()
        logging.info("Starting install")
        while self._check_pid():
            pass
        install: bool = self._install()
        if install:
            self._update_version()
            self._run_app()

    def _start_log(self) -> None:
        if not os.path.exists('log'):
            os.makedirs('log')
        logging.basicConfig(filename='log/install.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def _check_pid(self) -> bool:
        if not psutil.pid_exists(int(self._pid)):
            return False
        else:
            p = psutil.Process(int(self._pid))
            p.terminate()
        return True

    def _install(self) -> bool:
        try:
            with zipfile.ZipFile(self._start, 'r') as z:
                z.extractall(self._end)
            logging.info("Extracted {0} to {1}".format(self._start, self._end))
            os.remove(self._start)
            logging.info("Removed {0}".format(self._start))
        except:
            logging.error("Error installing from {0} to {1}".format(self._start, self._end))
            return False
        return True

    def _run_app(self) -> None:
        try:
            apptxt: str = os.path.join(self._end, "app.txt")
            with open(apptxt, "r") as f:
                app = f.readline().strip()
            appName: str = os.path.join(self._end, app+".exe")
            logging.info("Starting {0}".format(appName))
            time.sleep(4)
            command: list = [appName]
            subprocess.Popen(command,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            close_fds=True)
            logging.info("Started {0}".format(appName))
        except:
            logging.error("Error starting {0}".format(appName))
        sys.exit()

    def _update_version(self) -> None:
        # input "C:\\Users\\victo\\OneDrive\\Área de Trabalho\\receipt-generator\\temp\\receipt-generator1.0.0.zip"
        version: str = self._start.split("\\")[-1].replace(".zip", "").replace("receipt-generator", "")
        # output: 1.0.0
        logging.info("Updated version to {0}".format(version))
        versionFile: str = os.path.join(self._end, "update.txt")
        if not os.path.exists(versionFile):
            with open(versionFile, "w") as f:
                f.write(version)
            return
        with open(versionFile, "w") as f:
            f.write(version)
