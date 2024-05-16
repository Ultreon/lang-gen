from __future__ import annotations
from overload import overload


 
from builtins import str
import dev.ultreon.quantum.premain.win32.Kernel32 as __Kernel32
__Kernel32 = __Kernel32
from abc import abstractmethod, ABC
 
class Kernel32(ABC):
    """dev.ultreon.quantum.premain.win32.Kernel32"""
 
    @staticmethod
    def __wrap(java_value: __Kernel32) -> 'Kernel32':
        return Kernel32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Kernel32):
        """
        Dynamic initializer for Kernel32.
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
 
    # public static final dev.ultreon.quantum.premain.win32.Kernel32 dev.ultreon.quantum.premain.win32.Kernel32.INSTANCE
    INSTANCE: 'Kernel32' = __wrap(__Kernel32.INSTANCE)


    @abstractmethod
    def SetCurrentDirectoryW(self, arg0: 'char'):
        """public abstract int dev.ultreon.quantum.premain.win32.Kernel32.SetCurrentDirectoryW(char[])"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.premain.win32.Kernel32
from builtins import str
import dev.ultreon.quantum.premain.win32.Kernel32 as __Kernel32
__Kernel32 = __Kernel32
from abc import abstractmethod, ABC
 
class Kernel32(ABC):
    """dev.ultreon.quantum.premain.win32.Kernel32"""
 
    @staticmethod
    def __wrap(java_value: __Kernel32) -> 'Kernel32':
        return Kernel32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Kernel32):
        """
        Dynamic initializer for Kernel32.
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
 
    # public static final dev.ultreon.quantum.premain.win32.Kernel32 dev.ultreon.quantum.premain.win32.Kernel32.INSTANCE
    INSTANCE: 'Kernel32' = __wrap(__Kernel32.INSTANCE)


    @abstractmethod
    def SetCurrentDirectoryW(self, arg0: 'char'):
        """public abstract int dev.ultreon.quantum.premain.win32.Kernel32.SetCurrentDirectoryW(char[])"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.premain.win32.Kernel32