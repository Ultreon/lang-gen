def import_once(name: str) -> object:
    import importlib
    import sys

    val: str = ""

    for part in name.split("."):
        if not part.islower():
            break

        val += part + "."

    val = val[:-1]

    print(f"importing {val} ...")

    if name not in sys.modules:
        return importlib.import_module(val)
    try:
        return importlib.import_module(val, sys.modules[val].__package__)
    except ImportError:
        return sys.modules[val]
    except AttributeError:
        return sys.modules[val]


def transform(value: object) -> object:
    if value is int:
        import java.lang.Long as Long
        return Long.valueOf(value)

    if value is float:
        import java.lang.Double as Double
        return Double.valueOf(value)

    if value is bool:
        import java.lang.Boolean as Boolean
        return Boolean.valueOf(value)

    if value is str:
        import java.lang.String as String
        return String.valueOf(value)

    return value


# Aesthetics for Java + Python interop.
def override(func: object) -> object:
    """
    Marks a function as overriding another function in the superclass.

    :param func: The function to decorate
    :return: the decorated function
    """
    return func
