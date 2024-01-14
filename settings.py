#!usr/bin/python
import configparser
import os

config = configparser.ConfigParser()
config_filename = 'settings.ini'
config_main_section = 'settings'


def write_file():
    config.write(open(config_filename, 'w'))


def get_timeout_duration():
    return float(config.get(config_main_section, 'timeout_duration'))


def get_toast_notification():
    return bool(config.get(config_main_section, 'toast_notification_on_timeout'))


# Startup functions
if not os.path.exists(config_filename):
    config[config_main_section] = {'timeout_duration': '60', 'toast_notification_on_timeout': 'True'}
    print("Settings file not found, created.")
    write_file()
else:
    print("Reading settings...")
    config.read(config_filename)
    if not (config.has_section(config_main_section)):
        config.add_section(config_main_section)
        if not (config.has_option(config_main_section, 'timeout_duration')):
            config[config_main_section]['timeout_duration'] = '60'
        if not (config.has_option('settings', 'toast_notification_on_timeout')):
            config[config_main_section]['toast_notification_on_timeout'] = 'True'
    write_file()
