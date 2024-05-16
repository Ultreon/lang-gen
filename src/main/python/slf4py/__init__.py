from __future__ import annotations
from overload import overload


 
from abc import abstractmethod, ABC
import org.slf4j.IMarkerFactory as _IMarkerFactory
_IMarkerFactory = _IMarkerFactory
 
class IMarkerFactory():
    """org.slf4j.IMarkerFactory"""
 
    @staticmethod
    def _wrap(java_value: _IMarkerFactory) -> 'IMarkerFactory':
        return IMarkerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IMarkerFactory):
        """
        Dynamic initializer for IMarkerFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IMarkerFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IMarkerFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def detachMarker(self, arg0: str):
        """public abstract boolean org.slf4j.IMarkerFactory.detachMarker(java.lang.String)"""
        pass

    @abstractmethod
    def exists(self, arg0: str):
        """public abstract boolean org.slf4j.IMarkerFactory.exists(java.lang.String)"""
        pass

    @abstractmethod
    def getMarker(self, arg0: str):
        """public abstract org.slf4j.Marker org.slf4j.IMarkerFactory.getMarker(java.lang.String)"""
        pass

    @abstractmethod
    def getDetachedMarker(self, arg0: str):
        """public abstract org.slf4j.Marker org.slf4j.IMarkerFactory.getDetachedMarker(java.lang.String)"""
        pass

 
 
 
# CLASS: org.slf4j.IMarkerFactory
from abc import abstractmethod, ABC
import org.slf4j.IMarkerFactory as _IMarkerFactory
_IMarkerFactory = _IMarkerFactory
 
class IMarkerFactory():
    """org.slf4j.IMarkerFactory"""
 
    @staticmethod
    def _wrap(java_value: _IMarkerFactory) -> 'IMarkerFactory':
        return IMarkerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IMarkerFactory):
        """
        Dynamic initializer for IMarkerFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IMarkerFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IMarkerFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def detachMarker(self, arg0: str):
        """public abstract boolean org.slf4j.IMarkerFactory.detachMarker(java.lang.String)"""
        pass

    @abstractmethod
    def exists(self, arg0: str):
        """public abstract boolean org.slf4j.IMarkerFactory.exists(java.lang.String)"""
        pass

    @abstractmethod
    def getMarker(self, arg0: str):
        """public abstract org.slf4j.Marker org.slf4j.IMarkerFactory.getMarker(java.lang.String)"""
        pass

    @abstractmethod
    def getDetachedMarker(self, arg0: str):
        """public abstract org.slf4j.Marker org.slf4j.IMarkerFactory.getDetachedMarker(java.lang.String)"""
        pass

 
 
 
# CLASS: org.slf4j.IMarkerFactory 
 
 
# CLASS: org.slf4j.LoggerFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import org.slf4j.Logger as _Logger
_Logger = _Logger
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.slf4j.ILoggerFactory as _ILoggerFactory
_ILoggerFactory = _ILoggerFactory
import org.slf4j.LoggerFactory as _LoggerFactory
_LoggerFactory = _LoggerFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoggerFactory():
    """org.slf4j.LoggerFactory"""
 
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
 
    @staticmethod
    @overload
    def getILoggerFactory() -> 'ILoggerFactory':
        """public static org.slf4j.ILoggerFactory org.slf4j.LoggerFactory.getILoggerFactory()"""
        return ILoggerFactory._wrap(_LoggerFactory.getILoggerFactory())

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

    @staticmethod
    @overload
    def getLogger(arg0: 'Class') -> 'Logger':
        """public static org.slf4j.Logger org.slf4j.LoggerFactory.getLogger(java.lang.Class<?>)"""
        return Logger._wrap(_LoggerFactory.getLogger(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getLogger(arg0: str) -> 'Logger':
        """public static org.slf4j.Logger org.slf4j.LoggerFactory.getLogger(java.lang.String)"""
        return Logger._wrap(_LoggerFactory.getLogger(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.slf4j.ILoggerFactory
import org.slf4j.ILoggerFactory as _ILoggerFactory
_ILoggerFactory = _ILoggerFactory
from abc import abstractmethod, ABC
 
class ILoggerFactory():
    """org.slf4j.ILoggerFactory"""
 
    @staticmethod
    def _wrap(java_value: _ILoggerFactory) -> 'ILoggerFactory':
        return ILoggerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ILoggerFactory):
        """
        Dynamic initializer for ILoggerFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ILoggerFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ILoggerFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getLogger(self, arg0: str):
        """public abstract org.slf4j.Logger org.slf4j.ILoggerFactory.getLogger(java.lang.String)"""
        pass 
 
 
# CLASS: org.slf4j.Logger
from pyquantum_helper import import_once as _import_once
import org.slf4j.spi.LoggingEventBuilder as _LoggingEventBuilder
_LoggingEventBuilder = _LoggingEventBuilder
try:
    from slf4py import event
except ImportError:
    event = _import_once("slf4py.event")

try:
    from slf4py import spi
except ImportError:
    spi = _import_once("slf4py.spi")

import java.lang.Throwable as Throwable
import org.slf4j.Logger as _Logger
_Logger = _Logger
from abc import abstractmethod, ABC
from builtins import object
from builtins import bool
 
class Logger():
    """org.slf4j.Logger"""
 
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
    def debug(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.debug(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def isTraceEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isTraceEnabled(org.slf4j.Marker)"""
        pass

    @abstractmethod
    def trace(self, arg0: 'Marker', arg1: str):
        """public abstract void org.slf4j.Logger.trace(org.slf4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public abstract void org.slf4j.Logger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public abstract void org.slf4j.Logger.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def isInfoEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isInfoEnabled(org.slf4j.Marker)"""
        pass

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_Logger, self).atLevel(arg0))

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String org.slf4j.Logger.getName()"""
        pass

    @abstractmethod
    def trace(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def isDebugEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled(org.slf4j.Marker)"""
        pass

    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'._wrap(super(Logger, self).atInfo())

    @abstractmethod
    def error(self, arg0: 'Marker', arg1: str):
        """public abstract void org.slf4j.Logger.error(org.slf4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def isDebugEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled()"""
        pass

    @abstractmethod
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public abstract void org.slf4j.Logger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.debug(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.error(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, arg0: str):
        """public abstract void org.slf4j.Logger.error(java.lang.String)"""
        pass

    @abstractmethod
    def trace(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public abstract void org.slf4j.Logger.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public abstract void org.slf4j.Logger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Object)"""
        pass

    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'._wrap(super(Logger, self).atError())

    @abstractmethod
    def error(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isInfoEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isInfoEnabled()"""
        pass

    @abstractmethod
    def isWarnEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled(org.slf4j.Marker)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, arg0: str):
        """public abstract void org.slf4j.Logger.trace(java.lang.String)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public abstract void org.slf4j.Logger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def isErrorEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isErrorEnabled()"""
        pass

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_Logger, self).makeLoggingEventBuilder(arg0))

    @abstractmethod
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public abstract void org.slf4j.Logger.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public abstract void org.slf4j.Logger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: str):
        """public abstract void org.slf4j.Logger.info(java.lang.String)"""
        pass

    @abstractmethod
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public abstract void org.slf4j.Logger.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isErrorEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isErrorEnabled(org.slf4j.Marker)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public abstract void org.slf4j.Logger.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def isTraceEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isTraceEnabled()"""
        pass

    @abstractmethod
    def warn(self, arg0: 'Marker', arg1: str):
        """public abstract void org.slf4j.Logger.warn(org.slf4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.error(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public abstract void org.slf4j.Logger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public abstract void org.slf4j.Logger.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str):
        """public abstract void org.slf4j.Logger.debug(java.lang.String)"""
        pass

    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atWarn()"""
        return 'spi.LoggingEventBuilder'._wrap(super(Logger, self).atWarn())

    @abstractmethod
    def debug(self, arg0: 'Marker', arg1: str):
        """public abstract void org.slf4j.Logger.debug(org.slf4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public abstract void org.slf4j.Logger.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public abstract void org.slf4j.Logger.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: 'Marker', arg1: str):
        """public abstract void org.slf4j.Logger.info(org.slf4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.debug(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public abstract void org.slf4j.Logger.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public abstract void org.slf4j.Logger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public abstract void org.slf4j.Logger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, arg0: str):
        """public abstract void org.slf4j.Logger.warn(java.lang.String)"""
        pass

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool._wrap(super(_Logger, self).isEnabledForLevel(arg0))

    @abstractmethod
    def error(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.error(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public abstract void org.slf4j.Logger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public abstract void org.slf4j.Logger.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'._wrap(super(Logger, self).atDebug())

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled()"""
        pass

    @abstractmethod
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public abstract void org.slf4j.Logger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'._wrap(super(Logger, self).atTrace()) 
 
 
# CLASS: org.slf4j.LoggerFactoryFriend
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import org.slf4j.LoggerFactoryFriend as _LoggerFactoryFriend
_LoggerFactoryFriend = _LoggerFactoryFriend
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoggerFactoryFriend():
    """org.slf4j.LoggerFactoryFriend"""
 
    @staticmethod
    def _wrap(java_value: _LoggerFactoryFriend) -> 'LoggerFactoryFriend':
        return LoggerFactoryFriend(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoggerFactoryFriend):
        """
        Dynamic initializer for LoggerFactoryFriend.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoggerFactoryFriend__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoggerFactoryFriend__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @overload
    def __init__(self, ):
        """public org.slf4j.LoggerFactoryFriend()"""
        val = _LoggerFactoryFriend()
        self.__wrapper = val

    @staticmethod
    @overload
    def setDetectLoggerNameMismatch(arg0: bool):
        """public static void org.slf4j.LoggerFactoryFriend.setDetectLoggerNameMismatch(boolean)"""
        _LoggerFactoryFriend.setDetectLoggerNameMismatch(_boolean.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

        @staticmethod
        @overload
        def reset():
            """public static void org.slf4j.LoggerFactoryFriend.reset()"""
            _LoggerFactoryFriend.reset()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.slf4j.LoggerFactoryFriend()"""
        val = _LoggerFactoryFriend()
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
 
 
# CLASS: org.slf4j.MDC$MDCCloseable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.slf4j.MDC as _MDC_MDCCloseable
_MDCCloseable = _MDC_MDCCloseable.MDCCloseable
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MDCCloseable():
    """org.slf4j.MDC.MDCCloseable"""
 
    @staticmethod
    def _wrap(java_value: _MDCCloseable) -> 'MDCCloseable':
        return MDCCloseable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MDCCloseable):
        """
        Dynamic initializer for MDCCloseable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MDCCloseable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MDCCloseable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def close(self):
        """public void org.slf4j.MDC$MDCCloseable.close()"""
        super(MDCCloseable, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.slf4j.MarkerFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.slf4j.MarkerFactory as _MarkerFactory
_MarkerFactory = _MarkerFactory
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.slf4j.Marker as _Marker
_Marker = _Marker
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import org.slf4j.IMarkerFactory as _IMarkerFactory
_IMarkerFactory = _IMarkerFactory
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MarkerFactory():
    """org.slf4j.MarkerFactory"""
 
    @staticmethod
    def _wrap(java_value: _MarkerFactory) -> 'MarkerFactory':
        return MarkerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MarkerFactory):
        """
        Dynamic initializer for MarkerFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MarkerFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MarkerFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getMarker(arg0: str) -> 'Marker':
        """public static org.slf4j.Marker org.slf4j.MarkerFactory.getMarker(java.lang.String)"""
        return Marker._wrap(_MarkerFactory.getMarker(arg0))

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

    @staticmethod
    @overload
    def getIMarkerFactory() -> 'IMarkerFactory':
        """public static org.slf4j.IMarkerFactory org.slf4j.MarkerFactory.getIMarkerFactory()"""
        return IMarkerFactory._wrap(_MarkerFactory.getIMarkerFactory())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getDetachedMarker(arg0: str) -> 'Marker':
        """public static org.slf4j.Marker org.slf4j.MarkerFactory.getDetachedMarker(java.lang.String)"""
        return Marker._wrap(_MarkerFactory.getDetachedMarker(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.slf4j.MDC
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.util.Deque as Deque
try:
    from slf4py import spi
except ImportError:
    spi = _import_once("slf4py.spi")

import java.lang.String as _String
_String = _String
import org.slf4j.MDC as _MDC
_MDC = _MDC
import java.lang.String as _string
import java.util.Deque as _Deque
_Deque = _Deque
import java.lang.Integer as _int
import org.slf4j.spi.MDCAdapter as _MDCAdapter
_MDCAdapter = _MDCAdapter
import org.slf4j.MDC as _MDC_MDCCloseable
_MDCCloseable = _MDC_MDCCloseable.MDCCloseable
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MDC():
    """org.slf4j.MDC"""
 
    @staticmethod
    def _wrap(java_value: _MDC) -> 'MDC':
        return MDC(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MDC):
        """
        Dynamic initializer for MDC.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MDC__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MDC__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def popByKey(arg0: str) -> str:
        """public static java.lang.String org.slf4j.MDC.popByKey(java.lang.String)"""
        return str._wrap(_MDC.popByKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getCopyOfDequeByKey(self, arg0: str) -> 'Deque':
        """public java.util.Deque<java.lang.String> org.slf4j.MDC.getCopyOfDequeByKey(java.lang.String)"""
        return 'Deque'._wrap(super(_MDC, self).getCopyOfDequeByKey(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def remove(arg0: str):
        """public static void org.slf4j.MDC.remove(java.lang.String) throws java.lang.IllegalArgumentException"""
        _MDC.remove(arg0)

    @staticmethod
    @overload
    def pushByKey(arg0: str, arg1: str):
        """public static void org.slf4j.MDC.pushByKey(java.lang.String,java.lang.String)"""
        _MDC.pushByKey(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def put(arg0: str, arg1: str):
        """public static void org.slf4j.MDC.put(java.lang.String,java.lang.String) throws java.lang.IllegalArgumentException"""
        _MDC.put(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

        @staticmethod
        @overload
        def clear():
            """public static void org.slf4j.MDC.clear()"""
            _MDC.clear()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def get(arg0: str) -> str:
        """public static java.lang.String org.slf4j.MDC.get(java.lang.String) throws java.lang.IllegalArgumentException"""
        return str._wrap(_MDC.get(arg0))

    @staticmethod
    @overload
    def putCloseable(arg0: str, arg1: str) -> 'MDCCloseable':
        """public static org.slf4j.MDC$MDCCloseable org.slf4j.MDC.putCloseable(java.lang.String,java.lang.String) throws java.lang.IllegalArgumentException"""
        return MDCCloseable._wrap(_MDC.putCloseable(arg0, arg1))

    @staticmethod
    @overload
    def getCopyOfContextMap() -> 'Map':
        """public static java.util.Map<java.lang.String, java.lang.String> org.slf4j.MDC.getCopyOfContextMap()"""
        return Map._wrap(_MDC.getCopyOfContextMap())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def setContextMap(arg0: 'Map'):
        """public static void org.slf4j.MDC.setContextMap(java.util.Map<java.lang.String, java.lang.String>)"""
        _MDC.setContextMap(arg0)

    @staticmethod
    @overload
    def getMDCAdapter() -> 'spi.MDCAdapter':
        """public static org.slf4j.spi.MDCAdapter org.slf4j.MDC.getMDCAdapter()"""
        return spi.MDCAdapter._wrap(_MDC.getMDCAdapter())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.slf4j.Marker
from abc import abstractmethod, ABC
import org.slf4j.Marker as _Marker
_Marker = _Marker
 
class Marker():
    """org.slf4j.Marker"""
 
    @staticmethod
    def _wrap(java_value: _Marker) -> 'Marker':
        return Marker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Marker):
        """
        Dynamic initializer for Marker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Marker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Marker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def hasReferences(self, ):
        """public abstract boolean org.slf4j.Marker.hasReferences()"""
        pass

    @abstractmethod
    def remove(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Marker.remove(org.slf4j.Marker)"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<org.slf4j.Marker> org.slf4j.Marker.iterator()"""
        pass

    @abstractmethod
    def contains(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Marker.contains(org.slf4j.Marker)"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean org.slf4j.Marker.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int org.slf4j.Marker.hashCode()"""
        pass

    @abstractmethod
    def hasChildren(self, ):
        """public abstract boolean org.slf4j.Marker.hasChildren()"""
        pass

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String org.slf4j.Marker.getName()"""
        pass

    @abstractmethod
    def add(self, arg0: 'Marker'):
        """public abstract void org.slf4j.Marker.add(org.slf4j.Marker)"""
        pass

    @abstractmethod
    def contains(self, arg0: str):
        """public abstract boolean org.slf4j.Marker.contains(java.lang.String)"""
        pass