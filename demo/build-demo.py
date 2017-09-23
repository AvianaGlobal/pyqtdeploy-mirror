# Copyright (c) 2017, Riverbank Computing Limited
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


import argparse
import os
import sys


def run(*args):
    """ Run a command and terminate if it fails. """

    ec = os.system(' '.join(args))

    if ec:
        sys.exit(ec)


# Parse the command line.
parser = argparse.ArgumentParser()
parser.add_argument('--target', help="the target platform", default='')
parser.add_argument('--no-sysroot', help="do not build the sysroot",
        action='store_true')
cmd_line_args = parser.parse_args()
target = cmd_line_args.target
build_sysroot = not cmd_line_args.no_sysroot

# Anchor everything from the directory containing this script.
sysroot_dir = 'sysroot'
build_dir = 'build'
if target:
    sysroot_dir += '-' + target
    build_dir += '-' + target

os.chdir(os.path.dirname(os.path.abspath(__file__)))
source_dir = os.path.join('..', 'test', 'src')

# Build sysroot.
if build_sysroot:
    args = ['pyqtdeploy-sysroot', '--sysroot', sysroot_dir, '--source-dir',
            source_dir]

    if target:
        args.extend(['--target', target])

    args.append('sysroot.json')

    run(*args)

# Build the demo.
run('pyqtdeploy-build', '--sysroot', sysroot_dir, '--build-dir', build_dir,
        'pyqt-demo.pdy')

# Tell the user where the demo is.
if target.startswith('android'):
    print("TODO")
elif target.startswith('ios'):
    print("TODO")
elif target.startswith('win') or sys.platform == 'win32':
    print("TODO")
else:
    print("The pyqt-demo executable can be found in the '{0}' directory.".format(build_dir))
