from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.premain.posix.CLibrary as __CLibrary
__CLibrary = __CLibrary
from abc import abstractmethod, ABC
 
class CLibrary(ABC):
    """dev.ultreon.quantum.premain.posix.CLibrary"""
 
    @staticmethod
    def __wrap(java_value: __CLibrary) -> 'CLibrary':
        return CLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CLibrary):
        """
        Dynamic initializer for CLibrary.
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
 
    # public static final dev.ultreon.quantum.premain.posix.CLibrary dev.ultreon.quantum.premain.posix.CLibrary.INSTANCE
    INSTANCE: 'CLibrary' = __wrap(__CLibrary.INSTANCE)


    @abstractmethod
    def chdir(self, arg0: str):
        """public abstract int dev.ultreon.quantum.premain.posix.CLibrary.chdir(java.lang.String)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.premain.posix.CLibrary
import dev.ultreon.quantum.premain.posix.CLibrary as __CLibrary
__CLibrary = __CLibrary
from abc import abstractmethod, ABC
 
class CLibrary(ABC):
    """dev.ultreon.quantum.premain.posix.CLibrary"""
 
    @staticmethod
    def __wrap(java_value: __CLibrary) -> 'CLibrary':
        return CLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CLibrary):
        """
        Dynamic initializer for CLibrary.
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
 
    # public static final dev.ultreon.quantum.premain.posix.CLibrary dev.ultreon.quantum.premain.posix.CLibrary.INSTANCE
    INSTANCE: 'CLibrary' = __wrap(__CLibrary.INSTANCE)


    @abstractmethod
    def chdir(self, arg0: str):
        """public abstract int dev.ultreon.quantum.premain.posix.CLibrary.chdir(java.lang.String)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.premain.posix.CLibrary