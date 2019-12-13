#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(format ='# %(levelname)-8s [%(asctime)s]  %(message)s',
                level=logging.INFO, filename=u'logs.py')
# Сообщение отладочное
logging.debug(u'This is a debug message')
# Сообщение информационное
logging.info(u'This is an info message')
# Сообщение предупреждение
logging.warning(u'This is a warning')
# Сообщение ошибки
logging.error(u'This is an error message')
# Сообщение критическое
logging.critical(u'FATAL!!!')