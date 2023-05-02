import threading
import pickle
import os


class ConfigManager:
    def __init__(self, filename):
        self.lock = threading.RLock()
        self.filename = filename
        try:
            with open(filename, 'rb') as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            self.data = {}

        self.properties = {}
        self.apis = {}

    def load(self):
        with self.lock:
            try:
                with open(self.filename, 'rb') as f:
                    self.data = pickle.load(f)
                    self.properties.update(self.data)
            except FileNotFoundError:
                self.data = {}

    def save(self):
        with self.lock:
            try:
                with open(self.filename, 'wb') as f:
                    # 将self.properties字典中的内容合并至self.data字典中
                    for k, v in self.properties.items():
                        self.data[k] = v
                    # 将self.apis字典中的函数状态保存至self.data字典中
                    for k, v in self.apis.items():
                        if v is not None:
                            self.data[k] = v
                    pickle.dump(self.data, f)
            except Exception as e:
                print('Error saving config data:', repr(e))
                raise

    def register_property(self, name, default_value):
        self.properties[name] = default_value

        def getter(self, default_value=default_value):
            with self.lock:
                return self.data.get(name, default_value)

        def setter(self, value):
            with self.lock:
                self.data[name] = value

        setattr(ConfigManager, name, property(getter, setter))

    def register_api(self, name, func, default_value=None):
        self.apis[name] = default_value

        def wrapper(*args, **kwargs):
            with self.lock:
                return func(*args, **kwargs)

        setattr(ConfigManager, name, wrapper)


c = ConfigManager("test.dat")

# c.register_property("bot_off_list", [999, 777])
# def send_message(self, message):
#     print("Sending message:", message)

# c.register_api("send_message", send_message, default_value="Hello, world!")

# c.save()
c.load()
print(c.properties,c.properties['bot_off_list'],c.apis)
