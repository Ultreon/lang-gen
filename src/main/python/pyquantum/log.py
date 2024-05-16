from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.log.Logger as __Logger
__Logger = __Logger
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class Logger(ABC):
    """dev.ultreon.quantum.log.Logger"""
 
    @staticmethod
    def __wrap(java_value: __Logger) -> 'Logger':
        return Logger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Logger):
        """
        Dynamic initializer for Logger.
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
import dev.ultreon.quantum.log.Logger as __Logger
__Logger = __Logger
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class Logger(ABC):
    """dev.ultreon.quantum.log.Logger"""
 
    @staticmethod
    def __wrap(java_value: __Logger) -> 'Logger':
        return Logger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Logger):
        """
        Dynamic initializer for Logger.
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
import dev.ultreon.quantum.log.LoggerFactory as __LoggerFactory
__LoggerFactory = __LoggerFactory
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.log.Logger as __Logger
__Logger = __Logger
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LoggerFactory():
    """dev.ultreon.quantum.log.LoggerFactory"""
 
    @staticmethod
    def __wrap(java_value: __LoggerFactory) -> 'LoggerFactory':
        return LoggerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerFactory):
        """
        Dynamic initializer for LoggerFactory.
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.log.LoggerFactory()"""
        val = __LoggerFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.log.LoggerFactory()"""
        val = __LoggerFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getLogger(arg0: str) -> 'Logger':
        """public static dev.ultreon.quantum.log.Logger dev.ultreon.quantum.log.LoggerFactory.getLogger(java.lang.String)"""
        return Logger.__wrap(__LoggerFactory.getLogger(arg0))

    @staticmethod
    @overload
    def getLogger(arg0: 'Class') -> 'Logger':
        """public static dev.ultreon.quantum.log.Logger dev.ultreon.quantum.log.LoggerFactory.getLogger(java.lang.Class<?>)"""
        return Logger.__wrap(__LoggerFactory.getLogger(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))