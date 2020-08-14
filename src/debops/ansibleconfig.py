# -*- coding: utf-8 -*-

# Copyright (C) 2020 Maciej Delmanowski <drybjed@gmail.com>
# Copyright (C) 2020 DebOps <https://debops.org/>
# SPDX-License-Identifier: GPL-3.0-or-later

from .constants import DEBOPS_PACKAGE_DATA
import os
import pkgutil
import jinja2
try:
    import configparser
except ImportError:
    import ConfigParser as configparser


class AnsibleConfig(object):

    def __init__(self, path, user_config=None, project_type=None,
                 refresh=False):
        self.path = os.path.abspath(path)
        self.user_config = user_config
        self.project_type = project_type

        self.config = configparser.ConfigParser()
        self._template_config(project_type=self.project_type)

        if self.user_config:
            if (os.path.exists(self.user_config)
                    and os.path.isfile(self.user_config)):
                self._parse_user_config(self.user_config)

        if (os.path.exists(self.path) and os.path.isfile(self.path)
                and not refresh):
            self.config.read(self.path)

    def _parse_user_config(self, config_file):
        debops_config = configparser.ConfigParser()
        debops_config.read(config_file)

        parsed_config = dict((sect.split(None, 1)[1], pairs)
                             for sect, pairs in debops_config.items()
                             if sect.startswith('ansible '))
        for section, pairs in parsed_config.items():
            if not self.config.has_section(section):
                self.config.add_section(section)
            for option, value in pairs.items():
                self.config.set(section, option, value)

    def _template_config(self, project_type=None):
        template_vars = {}
        template_vars['collections'] = [
                '/usr/share/ansible/collections',
                '~/.ansible/collections',
                os.path.join(DEBOPS_PACKAGE_DATA, 'ansible', 'collections')
                .replace(os.path.expanduser('~'), '~', 1),
                'ansible/collections'
        ]

        template_vars['roles'] = [
                '/etc/ansible/roles',
                '/usr/share/ansible/roles',
                '~/.ansible/roles',
                os.path.join(DEBOPS_PACKAGE_DATA, 'ansible', 'collections',
                             'ansible_collections', 'debops', 'debops',
                             'roles')
                .replace(os.path.expanduser('~'), '~', 1),
                'ansible/roles',
        ]

        if project_type == 'legacy':
            template_vars['plugin_types'] = ['modules', 'action', 'callback',
                                             'connection', 'filter', 'lookup',
                                             'vars']

        if template_vars.get('plugin_types'):
            template_vars['plugins'] = {}
            for plugin in template_vars['plugin_types']:
                template_vars['plugins'][plugin] = [
                    '/usr/share/ansible/plugins/' + plugin,
                    '~/.ansible/plugins/' + plugin,
                    os.path.join(DEBOPS_PACKAGE_DATA, 'ansible', 'collections',
                                 'ansible_collections', 'debops', 'debops',
                                 'plugins', plugin)
                    .replace(os.path.expanduser('~'), '~', 1),
                    'ansible/plugins/' + plugin
                ]

        template = jinja2.Template(
                pkgutil.get_data('debops',
                                 os.path.join('_data',
                                              'templates',
                                              'projectdir',
                                              'legacy',
                                              'ansible.cfg.j2'))
                .decode('utf-8'), trim_blocks=True)
        self.config.read_string(template.render(template_vars))

    def get_option(self, section, option):
        return self.config.get(section, option)

    def write_config(self):
        with open(self.path, 'w') as configfile:
            self.config.write(configfile)
