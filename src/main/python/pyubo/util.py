from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
from abc import abstractmethod, ABC
import dev.ultreon.ubo.util.DataTypeVisitor as __DataTypeVisitor
__DataTypeVisitor = __DataTypeVisitor
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class DataTypeVisitor(ABC):
    """dev.ultreon.ubo.util.DataTypeVisitor"""
 
    @staticmethod
    def __wrap(java_value: __DataTypeVisitor) -> 'DataTypeVisitor':
        return DataTypeVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DataTypeVisitor):
        """
        Dynamic initializer for DataTypeVisitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def visit(self, arg0: 'DataType'):
        """public abstract T dev.ultreon.ubo.util.DataTypeVisitor.visit(dev.ultreon.ubo.types.DataType<?>)"""
        pass

    @staticmethod
    @overload
    def deepCopy(arg0: 'DataType') -> 'types.DataType':
        """public static <T extends dev.ultreon.ubo.types.DataType<?>> T dev.ultreon.ubo.util.DataTypeVisitor.deepCopy(T)"""
        return types.DataType.__wrap(__DataTypeVisitor.deepCopy(arg0))

    @staticmethod
    @overload
    def deepCopy() -> 'DataTypeVisitor':
        """public static dev.ultreon.ubo.util.DataTypeVisitor<dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.util.DataTypeVisitor.deepCopy()"""
        return DataTypeVisitor.__wrap(__DataTypeVisitor.deepCopy())

 
 
 
# CLASS: dev.ultreon.ubo.util.DataTypeVisitor
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.ubo.types.DataType as __DataType
__DataType = __DataType
from abc import abstractmethod, ABC
import dev.ultreon.ubo.util.DataTypeVisitor as __DataTypeVisitor
__DataTypeVisitor = __DataTypeVisitor
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class DataTypeVisitor(ABC):
    """dev.ultreon.ubo.util.DataTypeVisitor"""
 
    @staticmethod
    def __wrap(java_value: __DataTypeVisitor) -> 'DataTypeVisitor':
        return DataTypeVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DataTypeVisitor):
        """
        Dynamic initializer for DataTypeVisitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def visit(self, arg0: 'DataType'):
        """public abstract T dev.ultreon.ubo.util.DataTypeVisitor.visit(dev.ultreon.ubo.types.DataType<?>)"""
        pass

    @staticmethod
    @overload
    def deepCopy(arg0: 'DataType') -> 'types.DataType':
        """public static <T extends dev.ultreon.ubo.types.DataType<?>> T dev.ultreon.ubo.util.DataTypeVisitor.deepCopy(T)"""
        return types.DataType.__wrap(__DataTypeVisitor.deepCopy(arg0))

    @staticmethod
    @overload
    def deepCopy() -> 'DataTypeVisitor':
        """public static dev.ultreon.ubo.util.DataTypeVisitor<dev.ultreon.ubo.types.DataType<?>> dev.ultreon.ubo.util.DataTypeVisitor.deepCopy()"""
        return DataTypeVisitor.__wrap(__DataTypeVisitor.deepCopy())

 
 
 
# CLASS: dev.ultreon.ubo.util.DataTypeVisitor 
 
 
# CLASS: dev.ultreon.ubo.util.StringVisitor
import dev.ultreon.ubo.util.StringVisitor as __StringVisitor
__StringVisitor = __StringVisitor
from abc import abstractmethod, ABC
 
class StringVisitor(ABC):
    """dev.ultreon.ubo.util.StringVisitor"""
 
    @staticmethod
    def __wrap(java_value: __StringVisitor) -> 'StringVisitor':
        return StringVisitor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringVisitor):
        """
        Dynamic initializer for StringVisitor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def visit(self, arg0: str):
        """public abstract T dev.ultreon.ubo.util.StringVisitor.visit(java.lang.String) throws java.io.IOException"""
        pass