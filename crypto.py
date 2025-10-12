import pathlib


def get_env_path():
    path = pathlib.Path(__file__)
    return path.parent.absolute() / ".env"


def get_env():
    path = get_env_path()
    env_dict = {}

    with open(path, "rt+") as f:
        for line in f.readlines():
            if line.startswith("#"):
                continue
            item = line.split("=")
            if len(item) <= 1:
                continue
            env_dict[item[0]] = item[1]
    return env_dict


def encrypt(message: str, password: str):
    pass


def decrypt(message: str, password: str):
    pass
