class JsonTools:
    @staticmethod
    def save(dest: str, content: dict):
        import json
        with open(dest, "w") as f:
            json.dump(content, f, indent=4)

    @staticmethod
    def load(src: str) -> object:
        import json
        with open(src, "r") as f:
            return json.load(f)
