# -*- coding: utf-8 -*-
{
    'name': 'Display Language Switcher',
    'author': 'Rida Louchachha',
    'category': 'Tools',
    'summary': 'The Display Language Switcher is an Odoo app that adds a convenient language selector dropdown in the system tray. This allows users to quickly switch between different languages, improving accessibility and user experience within the Odoo platform. Quick Language Changer, Quick Language Selector, Change Language, Select Language, Switch Language, Odoo Language Changer, Odoo Language Selector.',
    'description': """
    """,
    'maintainer': 'Rida Louchachha',
    'version': '1.0',
    'depends': ['web'],
    'post_init_hook': 'activate_languages',
    'assets': {
        'web.assets_backend': [
            'display_language_switcher/static/src/**/*',
        ],
    },
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
