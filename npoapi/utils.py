import os
import logging
import re
from typing import Final

logger: Final = logging.getLogger("Npo.Utils")
pattern: Final = re.compile('[a-z0-9]{2,}', re.IGNORECASE)


def looks_like_form(form: str):
    """
    Checks if the given string looks like a form. E.g. it represents json, xml, a file, or 'stdin'.

    Otherwise it can e.g. be interpreted as the text for search
    """
    if form.startswith("{") or form.startswith("<"):
        logger.debug("Detected a string that look like either json or xml")
        return True
    if os.path.isfile(form):
        logger.debug("Detected existing file %s" % form)
        return True
    if form.endswith(".json") or form.endswith(".xml"):
        logger.warning("Form %s looks like a file name, but it is not a file." % form)
        return True
    if form == "-":
        logger.debug("Detected explicit stdin")
        return True
    if not pattern.match(form):
        logger.warning("Form does not look like a credible text search. It doesn't look like a file either though")
        return False

    return False

