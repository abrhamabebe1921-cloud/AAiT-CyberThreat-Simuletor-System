import pty, os, subprocess
master, slave = pty.openpty()
subprocess.Popen('bash', stdin=slave, stdout=slave, stderr=slave, close_fds=True, start_new_session=True)
