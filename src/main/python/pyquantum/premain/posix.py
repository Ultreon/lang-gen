from __future__ import annotations
from overload import overload


 
from abc import abstractmethod, ABC
import dev.ultreon.quantum.premain.posix.CLibrary as _CLibrary
_CLibrary = _CLibrary
 
class CLibrary():
    """dev.ultreon.quantum.premain.posix.CLibrary"""
 
    @staticmethod
    def _wrap(java_value: _CLibrary) -> 'CLibrary':
        return CLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CLibrary):
        """
        Dynamic initializer for CLibrary.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CLibrary__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CLibrary__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def chdir(self, arg0: str):
        """public abstract int dev.ultreon.quantum.premain.posix.CLibrary.chdir(java.lang.String)"""
        pass


CLibrary.INSTANCE = CLibrary._wrap(_INSTANCE.INSTANCE)

 
 
 
# CLASS: dev.ultreon.quantum.premain.posix.CLibrary
from abc import abstractmethod, ABC
import dev.ultreon.quantum.premain.posix.CLibrary as _CLibrary
_CLibrary = _CLibrary
 
class CLibrary():
    """dev.ultreon.quantum.premain.posix.CLibrary"""
 
    @staticmethod
    def _wrap(java_value: _CLibrary) -> 'CLibrary':
        return CLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CLibrary):
        """
        Dynamic initializer for CLibrary.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CLibrary__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CLibrary__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def chdir(self, arg0: str):
        """public abstract int dev.ultreon.quantum.premain.posix.CLibrary.chdir(java.lang.String)"""
        pass


CLibrary.INSTANCE = CLibrary._wrap(_INSTANCE.INSTANCE)

 
 
 
# CLASS: dev.ultreon.quantum.premain.posix.CLibrary