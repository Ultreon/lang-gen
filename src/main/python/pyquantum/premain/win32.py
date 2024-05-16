from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.premain.win32.Kernel32 as _Kernel32
_Kernel32 = _Kernel32
from builtins import str
from abc import abstractmethod, ABC
 
class Kernel32():
    """dev.ultreon.quantum.premain.win32.Kernel32"""
 
    @staticmethod
    def _wrap(java_value: _Kernel32) -> 'Kernel32':
        return Kernel32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Kernel32):
        """
        Dynamic initializer for Kernel32.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Kernel32__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Kernel32__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def SetCurrentDirectoryW(self, arg0: 'char'):
        """public abstract int dev.ultreon.quantum.premain.win32.Kernel32.SetCurrentDirectoryW(char[])"""
        pass


Kernel32.INSTANCE = Kernel32._wrap(_INSTANCE.INSTANCE)

 
 
 
# CLASS: dev.ultreon.quantum.premain.win32.Kernel32
import dev.ultreon.quantum.premain.win32.Kernel32 as _Kernel32
_Kernel32 = _Kernel32
from builtins import str
from abc import abstractmethod, ABC
 
class Kernel32():
    """dev.ultreon.quantum.premain.win32.Kernel32"""
 
    @staticmethod
    def _wrap(java_value: _Kernel32) -> 'Kernel32':
        return Kernel32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Kernel32):
        """
        Dynamic initializer for Kernel32.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Kernel32__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Kernel32__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def SetCurrentDirectoryW(self, arg0: 'char'):
        """public abstract int dev.ultreon.quantum.premain.win32.Kernel32.SetCurrentDirectoryW(char[])"""
        pass


Kernel32.INSTANCE = Kernel32._wrap(_INSTANCE.INSTANCE)

 
 
 
# CLASS: dev.ultreon.quantum.premain.win32.Kernel32