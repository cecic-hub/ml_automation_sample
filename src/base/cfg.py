import configparser
import glob, os
from src.base import get_rootdir

root = get_rootdir.root_path()
my_config = {}


def read_config(path):
    config = configparser.ConfigParser()
    config.read(path, encoding="utf8")
    return config


def read_config_data(section, key):
    if "config_data" not in my_config:
        my_config["config_data"] = read_config(root + "/src/config_file/config.cfg")
    return my_config["config_data"].get(section, key)


def pages_obj():
    page = {}
    for file in glob.iglob(root + "/src/pages/" + "**/*.cfg", recursive=True):
        page[os.path.basename(file).replace('.cfg', '')] = read_config(file)
    return page


my_page = pages_obj()


def pages(page_name, key):
    return my_page[page_name].get(page_name, key)
