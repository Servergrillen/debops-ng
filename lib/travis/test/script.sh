#!/bin/bash

# Copyright (C) 2018 Maciej Delmanowski <drybjed@gmail.com>
# Copyright (C) 2018 DebOps <https://debops.org/>
# SPDX-License-Identifier: GPL-3.0-or-later

set -o nounset -o pipefail -o errexit

make clean-tests
# Disable debops script testing for now, until new unit tests are developed
#make test-debops-tools test-debops-ansible_plugins
make test-debops-ansible_plugins
make check
