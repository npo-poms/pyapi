import os



def looks_like_form(form: str):
    return os.path.isfile(form) or form.startswith("{") or form.startswith("<") or form.endswith(".json") or form.endswith(".xml") or form == "-"

