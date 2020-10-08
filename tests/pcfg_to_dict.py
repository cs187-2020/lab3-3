test = {   'name': 'pcfg_to_dict',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(pcfg_to_dict(probabilistic_arithmetic_grammar), dict)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> p_range = True;\n'
                                               '>>> for k, v in pcfg_to_dict(probabilistic_arithmetic_grammar).items():\n'
                                               '...   p_range = p_range and v <= 1.0 and v >= 0.0;\n'
                                               '>>> p_range\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
