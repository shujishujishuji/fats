from apps.properties import props


class DBProp:
    def __init__(self):
        """コンストラクタ"""
        dialect = props.get('db', 'dialect')
        driver = props.get('db', 'driver')
        username = props.get('db', 'username')
        password = props.get('db', 'password')
        host = props.get('db', 'host')
        port = props.get('db', 'port')
        database = props.get('db', 'database')
        self._url = f'{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}'
        self._pool_size = int(props.get('db', 'pool_size'))
        self._max_overflow = int(props.get('db', 'max_overflow'))
        self._isolation_level = props.get('db', 'isolation_level')

    @property
    def url(self):
        return self._url

    @property
    def pool_size(self):
        return self._pool_size

    @property
    def max_overflow(self):
        return self._max_overflow

    @property
    def isolation_level(self):
        return self._isolation_level
