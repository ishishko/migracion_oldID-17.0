{
    'name': 'Migracion res.partner.old_id ',
    'description': 'Modulo para guardar Id de campo de BBDD de origen para poder realizar migraciones de datos historicos.',
    'author': 'Ignacio Shishko',
    'website': 'https://www.hitofusion.com/',
    'version': '17.0.0.0.0.0',
    'category': 'Categoría del Módulo',
    'depends': ['base'],
    'data': [
        'views/respartner_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,

}
