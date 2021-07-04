import pexpect
import sys

child = pexpect.spawn('python3.8 bot.py', encoding='utf-8')
child.logfile = sys.stdout
child.expect('Number: ')
child.sendline('10')
child.expect('Number: ')
child.sendline('1')
child.expect(pexpect.EOF, timeout=None)
