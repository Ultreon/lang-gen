from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import org.slf4j.spi.LoggingEventBuilder as __LoggingEventBuilder
__LoggingEventBuilder = __LoggingEventBuilder
try:
    from slf4py import event
except ImportError:
    event = __import_once__("slf4py.event")

try:
    from slf4py import spi
except ImportError:
    spi = __import_once__("slf4py.spi")

import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
from builtins import object
from builtins import bool
import org.slf4j.Logger as __Logger
__Logger = __Logger
 
class Logger(ABC):
    """org.slf4j.Logger"""
 
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

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String org.slf4j.Logger.getName()"""
        pass

    @abstractmethod
    def trace(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Object...)"""
        pass

    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atWarn()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(Logger, self).atWarn())

    @abstractmethod
    def isDebugEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled(org.slf4j.Marker)"""
        pass

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

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__Logger, self).atLevel(arg0))

    @abstractmethod
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(Logger, self).atError())

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

    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(Logger, self).atDebug())

    @abstractmethod
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public abstract void org.slf4j.Logger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Object)"""
        pass

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

    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(Logger, self).atTrace())

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
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, arg0: 'Marker', arg1: str):
        """public abstract void org.slf4j.Logger.warn(org.slf4j.Marker,java.lang.String)"""
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
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(Logger, self).atInfo())

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

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__Logger, self).makeLoggingEventBuilder(arg0))

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

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled()"""
        pass

    @abstractmethod
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public abstract void org.slf4j.Logger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool.__wrap(super(__Logger, self).isEnabledForLevel(arg0))

 
 
 
# CLASS: org.slf4j.Logger
from pyquantum_helper import import_once as __import_once__
import org.slf4j.spi.LoggingEventBuilder as __LoggingEventBuilder
__LoggingEventBuilder = __LoggingEventBuilder
try:
    from slf4py import event
except ImportError:
    event = __import_once__("slf4py.event")

try:
    from slf4py import spi
except ImportError:
    spi = __import_once__("slf4py.spi")

import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
from builtins import object
from builtins import bool
import org.slf4j.Logger as __Logger
__Logger = __Logger
 
class Logger(ABC):
    """org.slf4j.Logger"""
 
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

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String org.slf4j.Logger.getName()"""
        pass

    @abstractmethod
    def trace(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Object...)"""
        pass

    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atWarn()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(Logger, self).atWarn())

    @abstractmethod
    def isDebugEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled(org.slf4j.Marker)"""
        pass

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

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__Logger, self).atLevel(arg0))

    @abstractmethod
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(Logger, self).atError())

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

    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(Logger, self).atDebug())

    @abstractmethod
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public abstract void org.slf4j.Logger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Object)"""
        pass

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

    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(Logger, self).atTrace())

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
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, arg0: 'Marker', arg1: str):
        """public abstract void org.slf4j.Logger.warn(org.slf4j.Marker,java.lang.String)"""
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
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(Logger, self).atInfo())

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

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__Logger, self).makeLoggingEventBuilder(arg0))

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

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled()"""
        pass

    @abstractmethod
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public abstract void org.slf4j.Logger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool.__wrap(super(__Logger, self).isEnabledForLevel(arg0))

 
 
 
# CLASS: org.slf4j.Logger 
 
 
# CLASS: org.slf4j.LoggerFactoryFriend
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.slf4j.LoggerFactoryFriend as __LoggerFactoryFriend
__LoggerFactoryFriend = __LoggerFactoryFriend
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LoggerFactoryFriend():
    """org.slf4j.LoggerFactoryFriend"""
 
    @staticmethod
    def __wrap(java_value: __LoggerFactoryFriend) -> 'LoggerFactoryFriend':
        return LoggerFactoryFriend(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerFactoryFriend):
        """
        Dynamic initializer for LoggerFactoryFriend.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.slf4j.LoggerFactoryFriend()"""
        val = __LoggerFactoryFriend()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.slf4j.LoggerFactoryFriend()"""
        val = __LoggerFactoryFriend()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def setDetectLoggerNameMismatch(arg0: bool):
        """public static void org.slf4j.LoggerFactoryFriend.setDetectLoggerNameMismatch(boolean)"""
        __LoggerFactoryFriend.setDetectLoggerNameMismatch(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

        @staticmethod
        @overload
        def reset():
            """public static void org.slf4j.LoggerFactoryFriend.reset()"""
            __LoggerFactoryFriend.reset()

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
 
 
# CLASS: org.slf4j.LoggerFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.slf4j.Logger as __Logger
__Logger = __Logger
import org.slf4j.ILoggerFactory as __ILoggerFactory
__ILoggerFactory = __ILoggerFactory
import org.slf4j.LoggerFactory as __LoggerFactory
__LoggerFactory = __LoggerFactory
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LoggerFactory():
    """org.slf4j.LoggerFactory"""
 
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getLogger(arg0: 'Class') -> 'Logger':
        """public static org.slf4j.Logger org.slf4j.LoggerFactory.getLogger(java.lang.Class<?>)"""
        return Logger.__wrap(__LoggerFactory.getLogger(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
        return Logger.__wrap(__LoggerFactory.getLogger(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getILoggerFactory() -> 'ILoggerFactory':
        """public static org.slf4j.ILoggerFactory org.slf4j.LoggerFactory.getILoggerFactory()"""
        return ILoggerFactory.__wrap(__LoggerFactory.getILoggerFactory()) 
 
 
# CLASS: org.slf4j.Marker
import org.slf4j.Marker as __Marker
__Marker = __Marker
from abc import abstractmethod, ABC
 
class Marker(ABC):
    """org.slf4j.Marker"""
 
    @staticmethod
    def __wrap(java_value: __Marker) -> 'Marker':
        return Marker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Marker):
        """
        Dynamic initializer for Marker.
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
 
 
# CLASS: org.slf4j.MDC$MDCCloseable
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import org.slf4j.MDC as __MDC_MDCCloseable
__MDCCloseable = __MDC_MDCCloseable.MDCCloseable
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MDCCloseable():
    """org.slf4j.MDC.MDCCloseable"""
 
    @staticmethod
    def __wrap(java_value: __MDCCloseable) -> 'MDCCloseable':
        return MDCCloseable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MDCCloseable):
        """
        Dynamic initializer for MDCCloseable.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def close(self):
        """public void org.slf4j.MDC$MDCCloseable.close()"""
        super(MDCCloseable, self).close() 
 
 
# CLASS: org.slf4j.MarkerFactory
import org.slf4j.MarkerFactory as __MarkerFactory
__MarkerFactory = __MarkerFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.slf4j.Marker as __Marker
__Marker = __Marker
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.slf4j.IMarkerFactory as __IMarkerFactory
__IMarkerFactory = __IMarkerFactory
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MarkerFactory():
    """org.slf4j.MarkerFactory"""
 
    @staticmethod
    def __wrap(java_value: __MarkerFactory) -> 'MarkerFactory':
        return MarkerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MarkerFactory):
        """
        Dynamic initializer for MarkerFactory.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getDetachedMarker(arg0: str) -> 'Marker':
        """public static org.slf4j.Marker org.slf4j.MarkerFactory.getDetachedMarker(java.lang.String)"""
        return Marker.__wrap(__MarkerFactory.getDetachedMarker(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getMarker(arg0: str) -> 'Marker':
        """public static org.slf4j.Marker org.slf4j.MarkerFactory.getMarker(java.lang.String)"""
        return Marker.__wrap(__MarkerFactory.getMarker(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getIMarkerFactory() -> 'IMarkerFactory':
        """public static org.slf4j.IMarkerFactory org.slf4j.MarkerFactory.getIMarkerFactory()"""
        return IMarkerFactory.__wrap(__MarkerFactory.getIMarkerFactory())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.slf4j.MDC
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.slf4j.MDC as __MDC
__MDC = __MDC
from pyquantum_helper import override
import java.lang.Object as __object
import org.slf4j.MDC as __MDC_MDCCloseable
__MDCCloseable = __MDC_MDCCloseable.MDCCloseable
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.slf4j.spi.MDCAdapter as __MDCAdapter
__MDCAdapter = __MDCAdapter
import java.util.Deque as Deque
import java.util.Deque as __Deque
__Deque = __Deque
try:
    from slf4py import spi
except ImportError:
    spi = __import_once__("slf4py.spi")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class MDC():
    """org.slf4j.MDC"""
 
    @staticmethod
    def __wrap(java_value: __MDC) -> 'MDC':
        return MDC(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MDC):
        """
        Dynamic initializer for MDC.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

        @staticmethod
        @overload
        def clear():
            """public static void org.slf4j.MDC.clear()"""
            __MDC.clear()

    @staticmethod
    @overload
    def popByKey(arg0: str) -> str:
        """public static java.lang.String org.slf4j.MDC.popByKey(java.lang.String)"""
        return str.__wrap(__MDC.popByKey(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def pushByKey(arg0: str, arg1: str):
        """public static void org.slf4j.MDC.pushByKey(java.lang.String,java.lang.String)"""
        __MDC.pushByKey(arg0, arg1)

    @overload
    def getCopyOfDequeByKey(self, arg0: str) -> 'Deque':
        """public java.util.Deque<java.lang.String> org.slf4j.MDC.getCopyOfDequeByKey(java.lang.String)"""
        return 'Deque'.__wrap(super(__MDC, self).getCopyOfDequeByKey(arg0))

    @staticmethod
    @overload
    def put(arg0: str, arg1: str):
        """public static void org.slf4j.MDC.put(java.lang.String,java.lang.String) throws java.lang.IllegalArgumentException"""
        __MDC.put(arg0, arg1)

    @staticmethod
    @overload
    def get(arg0: str) -> str:
        """public static java.lang.String org.slf4j.MDC.get(java.lang.String) throws java.lang.IllegalArgumentException"""
        return str.__wrap(__MDC.get(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def remove(arg0: str):
        """public static void org.slf4j.MDC.remove(java.lang.String) throws java.lang.IllegalArgumentException"""
        __MDC.remove(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getMDCAdapter() -> 'spi.MDCAdapter':
        """public static org.slf4j.spi.MDCAdapter org.slf4j.MDC.getMDCAdapter()"""
        return spi.MDCAdapter.__wrap(__MDC.getMDCAdapter())

    @staticmethod
    @overload
    def getCopyOfContextMap() -> 'Map':
        """public static java.util.Map<java.lang.String, java.lang.String> org.slf4j.MDC.getCopyOfContextMap()"""
        return Map.__wrap(__MDC.getCopyOfContextMap())

    @staticmethod
    @overload
    def putCloseable(arg0: str, arg1: str) -> 'MDCCloseable':
        """public static org.slf4j.MDC$MDCCloseable org.slf4j.MDC.putCloseable(java.lang.String,java.lang.String) throws java.lang.IllegalArgumentException"""
        return MDCCloseable.__wrap(__MDC.putCloseable(arg0, arg1))

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

    @staticmethod
    @overload
    def setContextMap(arg0: 'Map'):
        """public static void org.slf4j.MDC.setContextMap(java.util.Map<java.lang.String, java.lang.String>)"""
        __MDC.setContextMap(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.slf4j.IMarkerFactory
import org.slf4j.IMarkerFactory as __IMarkerFactory
__IMarkerFactory = __IMarkerFactory
from abc import abstractmethod, ABC
 
class IMarkerFactory(ABC):
    """org.slf4j.IMarkerFactory"""
 
    @staticmethod
    def __wrap(java_value: __IMarkerFactory) -> 'IMarkerFactory':
        return IMarkerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IMarkerFactory):
        """
        Dynamic initializer for IMarkerFactory.
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
 
 
# CLASS: org.slf4j.ILoggerFactory
import org.slf4j.ILoggerFactory as __ILoggerFactory
__ILoggerFactory = __ILoggerFactory
from abc import abstractmethod, ABC
 
class ILoggerFactory(ABC):
    """org.slf4j.ILoggerFactory"""
 
    @staticmethod
    def __wrap(java_value: __ILoggerFactory) -> 'ILoggerFactory':
        return ILoggerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ILoggerFactory):
        """
        Dynamic initializer for ILoggerFactory.
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
    def getLogger(self, arg0: str):
        """public abstract org.slf4j.Logger org.slf4j.ILoggerFactory.getLogger(java.lang.String)"""
        pass