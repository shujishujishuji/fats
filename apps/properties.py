import configparser


def create_prop():
    conf = configparser.ConfigParser()
    conf.read('settings/app.conf')
    return conf


props = create_prop()