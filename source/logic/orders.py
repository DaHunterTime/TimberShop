from uuid import uuid4


class OrderGenerator:
    def __init__(self, path):
        self.path = path

    def write_order(self, info):
        id_ = uuid4().hex

        with open(self.path, "a", encoding="utf-8") as file:
            file.write(f"{info['user']},{info['products']},{info['quantities']},{id_}\n")
