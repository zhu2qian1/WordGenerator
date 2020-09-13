import json


class JsonTools:
    @staticmethod
    def save(dest: str, obj: object):
        """saves an object as a json file.
        refer to json.dump for more information.

        dest: str - the path where the json file will be saved
        obj: object - the object to be saved"""

        with open(dest, "w") as f:
            json.dump(obj, f, indent=4)

    @staticmethod
    def load(src: str) -> object:
        """loads json from given path.

        src: str - path to the source json file"""

        with open(src, "r") as f:
            return json.load(f)
