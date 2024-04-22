{
    'name': 'Campo Old_id Migracion',
    'description': 'Modulo para guardar Id de campo de BBDD de origen para Optimizar migraciones de datos historicos. Valor encontrado en pestaña "Informacion Adicional"',
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