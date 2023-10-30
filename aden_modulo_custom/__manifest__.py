{
    'name': 'Aden',
    'version': '1.0',
    'summary': 'Challenge técnico de Aden',
    'description': 'Challenge técnico de Aden que consiste en crear un módulo de Odoo para inscribir alumnos a diferentes programas',
    'author': 'Gaston Valles',
    'website': 'https://gastonvalles-portfolio.vercel.app/',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'views/alumno_view.xml',
        'views/programa_view.xml',
        'views/inscripcion_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
