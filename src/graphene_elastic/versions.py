# """
# Contains information about the current Elasticsearch version in use,
# including (LTE and GTE).
# """
#
# from distutils.version import LooseVersion
#
# from .compat import get_elasticsearch_version
#
# __title__ = 'graphene_elastic.versions'
# __author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
# __copyright__ = '2019 Artur Barseghyan'
# __license__ = 'GPL 2.0/LGPL 2.1'
# __all__ = [
#     'LOOSE_ELASTICSEARCH_VERSION',
#     'LOOSE_ELASTICSEARCH_MINOR_VERSION',
# ]
#
# LOOSE_ELASTICSEARCH_VERSION = LooseVersion(
#     '.'.join([str(__n) for __n in get_elasticsearch_version()])
# )
# LOOSE_ELASTICSEARCH_MINOR_VERSION = LooseVersion(
#     '.'.join([str(i) for i in LOOSE_ELASTICSEARCH_VERSION.version[0:2]])
# )
#
# # Loose versions
# LOOSE_VERSIONS = (
#     '2.0',
#     '2.1',
#     '2.2',
#     '5.0',
#     '5.1',
#     '5.2',
#     '5.3',
#     '5.4',
#     '6.0',
#     '6.1',
#     '6.2',
#     '7.0',
#     '8.0',
#     '9.0',
# )
#
# for __v in LOOSE_VERSIONS:
#     __var_name = 'LOOSE_VERSION_{0}'.format(__v.replace('.', '_'))
#     globals()[__var_name] = LooseVersion(__v)
#     __all__.append(__var_name)
#
# # Exact versions
# EXACT_VERSIONS = LOOSE_VERSIONS[:-1]
#
# for __i, __v in enumerate(EXACT_VERSIONS):
#     __l_cur = globals()['LOOSE_VERSION_{0}'
#                         ''.format(LOOSE_VERSIONS[__i].replace('.', '_'))]
#     __l_nxt = globals()['LOOSE_VERSION_{0}'
#                         ''.format(LOOSE_VERSIONS[__i+1].replace('.', '_'))]
#     __var_name = 'ELASTICSEARCH_{0}'.format(__v.replace('.', '_'))
#     globals()[__var_name] = (__l_cur <= LOOSE_ELASTICSEARCH_VERSION < __l_nxt)
#     __all__.append(__var_name)
#
# # LTE list
# LTE_VERSIONS = LOOSE_VERSIONS[:-1]
#
# for __i, __v in enumerate(EXACT_VERSIONS):
#     __l_cur = globals()['LOOSE_VERSION_{0}'
#                         ''.format(LOOSE_VERSIONS[__i].replace('.', '_'))]
#     __var_name = 'ELASTICSEARCH_LTE_{0}'.format(__v.replace('.', '_'))
#     globals()[__var_name] = (LOOSE_ELASTICSEARCH_MINOR_VERSION <= __l_cur)
#     __all__.append(__var_name)
#
# # GTE list
# GTE_VERSIONS = LOOSE_VERSIONS[:-1]
#
# for __i, __v in enumerate(EXACT_VERSIONS):
#     __l_cur = globals()['LOOSE_VERSION_{0}'
#                         ''.format(LOOSE_VERSIONS[__i].replace('.', '_'))]
#     __var_name = 'ELASTICSEARCH_GTE_{0}'.format(__v.replace('.', '_'))
#     globals()[__var_name] = (
#         LOOSE_ELASTICSEARCH_MINOR_VERSION >= __l_cur
#     )
#     __all__.append(__var_name)
#
# __all__ = tuple(__all__)
#
# # Clean up
# try:
#     del __l_cur
#     del __l_nxt
#     del __var_name
#     del __i
#     del __v
# except NameError:
#     pass
#
# del LooseVersion
# del get_elasticsearch_version
