from apps.db import Session


class ServiceBase:
    """
    dbのセッションを管理するクラスで、子オブジェクトにセッションの管理を意識させないようにしています
    """
    def __init__(self):
        self.session = Session()
    print("start session")

    def __del__(self):
        self.session.close()
        print("close session")
