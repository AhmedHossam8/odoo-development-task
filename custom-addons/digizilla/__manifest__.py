{
    'name': 'Digizilla',
    'version': '1.0',
    'category': 'Operations',
    'summary': 'Digizilla Management System',
    'description': 'Custom addon for managing Digizilla records',
    'author': 'Ahmed Emara',
    'depends': ['base', 'sale', 'mail'],
    'data': [
        'security/digizilla_security.xml',
        'security/ir.model.access.csv',
        'reports/digizilla_report.xml',
        'reports/digizilla_report_template.xml',
        'views/digizilla_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'digizilla/static/src/js/hide_create_button.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}