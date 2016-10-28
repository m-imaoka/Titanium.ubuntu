#!/usr/bin/python

from ansible.module_utils.basic import *
import subprocess

def main():
    module = AnsibleModule(
        argument_spec = dict(
            dev = dict(required=True)
        )
    )

    need_change = subprocess.call(['parted', '-s', '-m', module.params['dev'], 'print'])
    if need_change:
        subprocess.call(['parted', '-s', '-a', 'optimal', module.params['dev'], '--', 'mklabel', 'gpt', 'mkpart', 'untitled', '1', '-1'])

    module.exit_json(changed=need_change)

if __name__ == '__main__':
    main()