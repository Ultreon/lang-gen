from __future__ import annotations
from overload import overload


 
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
import dev.ultreon.quantum.log.Logger as _Logger
_Logger = _Logger
 
class Logger():
    """dev.ultreon.quantum.log.Logger"""
 
    @staticmethod
    def _wrap(java_value: _Logger) -> 'Logger':
        return Logger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Logger):
        """
        Dynamic initializer for Logger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Logger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Logger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def error(self, arg0: str, arg1: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.error(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.debug(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: object):
        """public abstract void dev.ultreon.quantum.log.Logger.error(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: object, arg2: object):
        """public abstract void dev.ultreon.quantum.log.Logger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, arg0: str):
        """public abstract void dev.ultreon.quantum.log.Logger.warn(java.lang.String)"""
        pass

    @abstractmethod
    def error(self, arg0: str):
        """public abstract void dev.ultreon.quantum.log.Logger.error(java.lang.String)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: object):
        """public abstract void dev.ultreon.quantum.log.Logger.info(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.warn(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.debug(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.info(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public abstract void dev.ultreon.quantum.log.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.info(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: object):
        """public abstract void dev.ultreon.quantum.log.Logger.debug(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.warn(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, arg0: str):
        """public abstract void dev.ultreon.quantum.log.Logger.info(java.lang.String)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: object):
        """public abstract void dev.ultreon.quantum.log.Logger.warn(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.error(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str):
        """public abstract void dev.ultreon.quantum.log.Logger.debug(java.lang.String)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public abstract void dev.ultreon.quantum.log.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: object, arg2: object):
        """public abstract void dev.ultreon.quantum.log.Logger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.log.Logger
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
import dev.ultreon.quantum.log.Logger as _Logger
_Logger = _Logger
 
class Logger():
    """dev.ultreon.quantum.log.Logger"""
 
    @staticmethod
    def _wrap(java_value: _Logger) -> 'Logger':
        return Logger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Logger):
        """
        Dynamic initializer for Logger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Logger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Logger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def error(self, arg0: str, arg1: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.error(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.debug(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: object):
        """public abstract void dev.ultreon.quantum.log.Logger.error(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: object, arg2: object):
        """public abstract void dev.ultreon.quantum.log.Logger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, arg0: str):
        """public abstract void dev.ultreon.quantum.log.Logger.warn(java.lang.String)"""
        pass

    @abstractmethod
    def error(self, arg0: str):
        """public abstract void dev.ultreon.quantum.log.Logger.error(java.lang.String)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: object):
        """public abstract void dev.ultreon.quantum.log.Logger.info(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.warn(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.debug(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.info(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public abstract void dev.ultreon.quantum.log.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.info(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: object):
        """public abstract void dev.ultreon.quantum.log.Logger.debug(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.warn(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, arg0: str):
        """public abstract void dev.ultreon.quantum.log.Logger.info(java.lang.String)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: object):
        """public abstract void dev.ultreon.quantum.log.Logger.warn(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: object, arg2: 'Throwable'):
        """public abstract void dev.ultreon.quantum.log.Logger.error(java.lang.String,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str):
        """public abstract void dev.ultreon.quantum.log.Logger.debug(java.lang.String)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public abstract void dev.ultreon.quantum.log.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: object, arg2: object):
        """public abstract void dev.ultreon.quantum.log.Logger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.log.Logger 
 
 
# CLASS: dev.ultreon.quantum.log.LoggerFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import dev.ultreon.quantum.log.LoggerFactory as _LoggerFactory
_LoggerFactory = _LoggerFactory
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.log.Logger as _Logger
_Logger = _Logger
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoggerFactory():
    """dev.ultreon.quantum.log.LoggerFactory"""
 
    @staticmethod
    def _wrap(java_value: _LoggerFactory) -> 'LoggerFactory':
        return LoggerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoggerFactory):
        """
        Dynamic initializer for LoggerFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoggerFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoggerFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.log.LoggerFactory()"""
        val = _LoggerFactory()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getLogger(arg0: str) -> 'Logger':
        """public static dev.ultreon.quantum.log.Logger dev.ultreon.quantum.log.LoggerFactory.getLogger(java.lang.String)"""
        return Logger._wrap(_LoggerFactory.getLogger(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getLogger(arg0: 'Class') -> 'Logger':
        """public static dev.ultreon.quantum.log.Logger dev.ultreon.quantum.log.LoggerFactory.getLogger(java.lang.Class<?>)"""
        return Logger._wrap(_LoggerFactory.getLogger(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.log.LoggerFactory()"""
        val = _LoggerFactory()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())