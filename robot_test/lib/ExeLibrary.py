import os.path
import subprocess
import sys


class ExeLibrary(object):

    def __init__(self):
        self._ham_path = os.path.join(os.path.dirname(__file__),
                                      '..', 'ham', 'login.py')
        self._status = ''

    def start_ham(self, username, password):
        self._run_command('start', username, password)

    def status_should_be(self, expected_status):
        if expected_status != self._status:
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (expected_status, self._status))

    def _run_command(self, command, *args):
        command = [sys.executable, self._ham_path, command] + list(args)
        process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        self._status = process.communicate()[0].strip()
