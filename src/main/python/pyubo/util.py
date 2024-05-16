from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from abc import abstractmethod, ABC
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import dev.ultreon.ubo.util.DataTypeVisitor as _DataTypeVisitor
_DataTypeVisitor = _DataTypeVisitor
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

 
class DataTypeVisitor():
    """dev.ultreon.ubo.util.DataTypeVisitor"""
 
    @staticmethod
    def _wrap(java_value: _DataTypeVisitor) -> 'DataTypeVisitor':
        return DataTypeVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DataTypeVisitor):
        """
        Dynamic initializer for DataTypeVisitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DataTypeVisitor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DataTypeVisitor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def deepCopy(arg0: 'DataType') -> 'types.DataType':
        """public static <T extends dev.ultreon.ubo.types.DataType<?>> T dev.ultreon.ubo.util.DataTypeVisitor.deepCopy(T)"""
        return types.DataType._wrap(_DataTypeVisitor.deepCopy(arg0))

    @abstractmethod
    def visit(self, arg0: 'DataType'):
        """public abstract T dev.ultreon.ubo.util.DataTypeVisitor.visit(dev.ultreon.ubo.types.DataType<?>)"""
        pass

    @staticmethod
    @overload
    def deepCopy() -> 'DataTypeVisitor':
        """public static dev.ultreon.ubo.util.DataTypeVisitor<dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.util.DataTypeVisitor.deepCopy()"""
        return DataTypeVisitor._wrap(_DataTypeVisitor.deepCopy())

 
 
 
# CLASS: dev.ultreon.ubo.util.DataTypeVisitor
from pyquantum_helper import import_once as _import_once
from abc import abstractmethod, ABC
import dev.ultreon.ubo.types.DataType as _DataType
_DataType = _DataType
import dev.ultreon.ubo.util.DataTypeVisitor as _DataTypeVisitor
_DataTypeVisitor = _DataTypeVisitor
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

 
class DataTypeVisitor():
    """dev.ultreon.ubo.util.DataTypeVisitor"""
 
    @staticmethod
    def _wrap(java_value: _DataTypeVisitor) -> 'DataTypeVisitor':
        return DataTypeVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DataTypeVisitor):
        """
        Dynamic initializer for DataTypeVisitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DataTypeVisitor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DataTypeVisitor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def deepCopy(arg0: 'DataType') -> 'types.DataType':
        """public static <T extends dev.ultreon.ubo.types.DataType<?>> T dev.ultreon.ubo.util.DataTypeVisitor.deepCopy(T)"""
        return types.DataType._wrap(_DataTypeVisitor.deepCopy(arg0))

    @abstractmethod
    def visit(self, arg0: 'DataType'):
        """public abstract T dev.ultreon.ubo.util.DataTypeVisitor.visit(dev.ultreon.ubo.types.DataType<?>)"""
        pass

    @staticmethod
    @overload
    def deepCopy() -> 'DataTypeVisitor':
        """public static dev.ultreon.ubo.util.DataTypeVisitor<dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.util.DataTypeVisitor.deepCopy()"""
        return DataTypeVisitor._wrap(_DataTypeVisitor.deepCopy())

 
 
 
# CLASS: dev.ultreon.ubo.util.DataTypeVisitor 
 
 
# CLASS: dev.ultreon.ubo.util.StringVisitor
import dev.ultreon.ubo.util.StringVisitor as _StringVisitor
_StringVisitor = _StringVisitor
from abc import abstractmethod, ABC
 
class StringVisitor():
    """dev.ultreon.ubo.util.StringVisitor"""
 
    @staticmethod
    def _wrap(java_value: _StringVisitor) -> 'StringVisitor':
        return StringVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringVisitor):
        """
        Dynamic initializer for StringVisitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringVisitor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringVisitor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def visit(self, arg0: str):
        """public abstract T dev.ultreon.ubo.util.StringVisitor.visit(java.lang.String) throws java.io.IOException"""
        pass