{
    'name': 'Nombre del Módulo',
    'description': 'Modulo para guardar Id de campo de BBDD de origen para poder realizar migraciones de datos historicos.',
    'author': 'Ignacio Shishko',
    'version': '1.0.0',
    'category': 'Categoría del Módulo',
    'depends': ['base', 'res.partner'],
    'data': [
        'views/respartner_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,

}