from __future__ import annotations
from overload import overload


 
import org.slf4j.spi.LoggerFactoryBinder as __LoggerFactoryBinder
__LoggerFactoryBinder = __LoggerFactoryBinder
from abc import abstractmethod, ABC
 
class LoggerFactoryBinder(ABC):
    """org.slf4j.spi.LoggerFactoryBinder"""
 
    @staticmethod
    def __wrap(java_value: __LoggerFactoryBinder) -> 'LoggerFactoryBinder':
        return LoggerFactoryBinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerFactoryBinder):
        """
        Dynamic initializer for LoggerFactoryBinder.
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
    def getLoggerFactoryClassStr(self, ):
        """public abstract java.lang.String org.slf4j.spi.LoggerFactoryBinder.getLoggerFactoryClassStr()"""
        pass

    @abstractmethod
    def getLoggerFactory(self, ):
        """public abstract org.slf4j.ILoggerFactory org.slf4j.spi.LoggerFactoryBinder.getLoggerFactory()"""
        pass

 
 
 
# CLASS: org.slf4j.spi.LoggerFactoryBinder
import org.slf4j.spi.LoggerFactoryBinder as __LoggerFactoryBinder
__LoggerFactoryBinder = __LoggerFactoryBinder
from abc import abstractmethod, ABC
 
class LoggerFactoryBinder(ABC):
    """org.slf4j.spi.LoggerFactoryBinder"""
 
    @staticmethod
    def __wrap(java_value: __LoggerFactoryBinder) -> 'LoggerFactoryBinder':
        return LoggerFactoryBinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerFactoryBinder):
        """
        Dynamic initializer for LoggerFactoryBinder.
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
    def getLoggerFactoryClassStr(self, ):
        """public abstract java.lang.String org.slf4j.spi.LoggerFactoryBinder.getLoggerFactoryClassStr()"""
        pass

    @abstractmethod
    def getLoggerFactory(self, ):
        """public abstract org.slf4j.ILoggerFactory org.slf4j.spi.LoggerFactoryBinder.getLoggerFactory()"""
        pass

 
 
 
# CLASS: org.slf4j.spi.LoggerFactoryBinder 
 
 
# CLASS: org.slf4j.spi.SLF4JServiceProvider
from abc import abstractmethod, ABC
import org.slf4j.spi.SLF4JServiceProvider as __SLF4JServiceProvider
__SLF4JServiceProvider = __SLF4JServiceProvider
 
class SLF4JServiceProvider(ABC):
    """org.slf4j.spi.SLF4JServiceProvider"""
 
    @staticmethod
    def __wrap(java_value: __SLF4JServiceProvider) -> 'SLF4JServiceProvider':
        return SLF4JServiceProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SLF4JServiceProvider):
        """
        Dynamic initializer for SLF4JServiceProvider.
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
    def getMarkerFactory(self, ):
        """public abstract org.slf4j.IMarkerFactory org.slf4j.spi.SLF4JServiceProvider.getMarkerFactory()"""
        pass

    @abstractmethod
    def getMDCAdapter(self, ):
        """public abstract org.slf4j.spi.MDCAdapter org.slf4j.spi.SLF4JServiceProvider.getMDCAdapter()"""
        pass

    @abstractmethod
    def getRequestedApiVersion(self, ):
        """public abstract java.lang.String org.slf4j.spi.SLF4JServiceProvider.getRequestedApiVersion()"""
        pass

    @abstractmethod
    def getLoggerFactory(self, ):
        """public abstract org.slf4j.ILoggerFactory org.slf4j.spi.SLF4JServiceProvider.getLoggerFactory()"""
        pass

    @abstractmethod
    def initialize(self, ):
        """public abstract void org.slf4j.spi.SLF4JServiceProvider.initialize()"""
        pass 
 
 
# CLASS: org.slf4j.spi.DefaultLoggingEventBuilder
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
import org.slf4j.spi.LoggingEventBuilder as __LoggingEventBuilder
__LoggingEventBuilder = __LoggingEventBuilder
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.slf4j.spi.DefaultLoggingEventBuilder as __DefaultLoggingEventBuilder
__DefaultLoggingEventBuilder = __DefaultLoggingEventBuilder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from slf4py import event
except ImportError:
    event = __import_once__("slf4py.event")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DefaultLoggingEventBuilder():
    """org.slf4j.spi.DefaultLoggingEventBuilder"""
 
    @staticmethod
    def __wrap(java_value: __DefaultLoggingEventBuilder) -> 'DefaultLoggingEventBuilder':
        return DefaultLoggingEventBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultLoggingEventBuilder):
        """
        Dynamic initializer for DefaultLoggingEventBuilder.
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
    def log(self):
        """public void org.slf4j.spi.DefaultLoggingEventBuilder.log()"""
        super(DefaultLoggingEventBuilder, self).log()

    @overload
    def setCause(self, arg0: 'Throwable') -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.DefaultLoggingEventBuilder.setCause(java.lang.Throwable)"""
        return 'LoggingEventBuilder'.__wrap(super(__DefaultLoggingEventBuilder, self).setCause(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setCallerBoundary(self, arg0: str):
        """public void org.slf4j.spi.DefaultLoggingEventBuilder.setCallerBoundary(java.lang.String)"""
        super(__DefaultLoggingEventBuilder, self).setCallerBoundary(arg0)

    @override
    @overload
    def log(self, arg0: str, arg1: object):
        """public void org.slf4j.spi.DefaultLoggingEventBuilder.log(java.lang.String,java.lang.Object)"""
        super(__DefaultLoggingEventBuilder, self).log(arg0, arg1)

    @overload
    def addKeyValue(self, arg0: str, arg1: object) -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.DefaultLoggingEventBuilder.addKeyValue(java.lang.String,java.lang.Object)"""
        return 'LoggingEventBuilder'.__wrap(super(__DefaultLoggingEventBuilder, self).addKeyValue(arg0, arg1))

    @overload
    def addArgument(self, arg0: 'Supplier') -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.DefaultLoggingEventBuilder.addArgument(java.util.function.Supplier<?>)"""
        return 'LoggingEventBuilder'.__wrap(super(__DefaultLoggingEventBuilder, self).addArgument(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def log(self, arg0: str, *arg1: object):
        """public void org.slf4j.spi.DefaultLoggingEventBuilder.log(java.lang.String,java.lang.Object...)"""
        super(__DefaultLoggingEventBuilder, self).log(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Logger', arg1: 'Level'):
        """public org.slf4j.spi.DefaultLoggingEventBuilder(org.slf4j.Logger,org.slf4j.event.Level)"""
        val = __DefaultLoggingEventBuilder(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def log(self, arg0: 'Supplier'):
        """public void org.slf4j.spi.DefaultLoggingEventBuilder.log(java.util.function.Supplier<java.lang.String>)"""
        super(__DefaultLoggingEventBuilder, self).log(arg0)

    @override
    @overload
    def log(self, arg0: str):
        """public void org.slf4j.spi.DefaultLoggingEventBuilder.log(java.lang.String)"""
        super(__DefaultLoggingEventBuilder, self).log(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setMessage(self, arg0: 'Supplier') -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.DefaultLoggingEventBuilder.setMessage(java.util.function.Supplier<java.lang.String>)"""
        return 'LoggingEventBuilder'.__wrap(super(__DefaultLoggingEventBuilder, self).setMessage(arg0))

    @override
    @overload
    def log(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.spi.DefaultLoggingEventBuilder.log(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__DefaultLoggingEventBuilder, self).log(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def addMarker(self, arg0: 'Marker') -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.DefaultLoggingEventBuilder.addMarker(org.slf4j.Marker)"""
        return 'LoggingEventBuilder'.__wrap(super(__DefaultLoggingEventBuilder, self).addMarker(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def addArgument(self, arg0: object) -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.DefaultLoggingEventBuilder.addArgument(java.lang.Object)"""
        return 'LoggingEventBuilder'.__wrap(super(__DefaultLoggingEventBuilder, self).addArgument(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setMessage(self, arg0: str) -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.DefaultLoggingEventBuilder.setMessage(java.lang.String)"""
        return 'LoggingEventBuilder'.__wrap(super(__DefaultLoggingEventBuilder, self).setMessage(arg0))

    @overload
    def addKeyValue(self, arg0: str, arg1: 'Supplier') -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.DefaultLoggingEventBuilder.addKeyValue(java.lang.String,java.util.function.Supplier<java.lang.Object>)"""
        return 'LoggingEventBuilder'.__wrap(super(__DefaultLoggingEventBuilder, self).addKeyValue(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.slf4j.spi.LoggingEventAware
from pyquantum_helper import import_once as __import_once__
import org.slf4j.spi.LoggingEventAware as __LoggingEventAware
__LoggingEventAware = __LoggingEventAware
try:
    from slf4py import event
except ImportError:
    event = __import_once__("slf4py.event")

from abc import abstractmethod, ABC
 
class LoggingEventAware(ABC):
    """org.slf4j.spi.LoggingEventAware"""
 
    @staticmethod
    def __wrap(java_value: __LoggingEventAware) -> 'LoggingEventAware':
        return LoggingEventAware(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggingEventAware):
        """
        Dynamic initializer for LoggingEventAware.
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
    def log(self, arg0: 'LoggingEvent'):
        """public abstract void org.slf4j.spi.LoggingEventAware.log(org.slf4j.event.LoggingEvent)"""
        pass 
 
 
# CLASS: org.slf4j.spi.MarkerFactoryBinder
import org.slf4j.spi.MarkerFactoryBinder as __MarkerFactoryBinder
__MarkerFactoryBinder = __MarkerFactoryBinder
from abc import abstractmethod, ABC
 
class MarkerFactoryBinder(ABC):
    """org.slf4j.spi.MarkerFactoryBinder"""
 
    @staticmethod
    def __wrap(java_value: __MarkerFactoryBinder) -> 'MarkerFactoryBinder':
        return MarkerFactoryBinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MarkerFactoryBinder):
        """
        Dynamic initializer for MarkerFactoryBinder.
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
    def getMarkerFactoryClassStr(self, ):
        """public abstract java.lang.String org.slf4j.spi.MarkerFactoryBinder.getMarkerFactoryClassStr()"""
        pass

    @abstractmethod
    def getMarkerFactory(self, ):
        """public abstract org.slf4j.IMarkerFactory org.slf4j.spi.MarkerFactoryBinder.getMarkerFactory()"""
        pass 
 
 
# CLASS: org.slf4j.spi.NOPLoggingEventBuilder
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
import org.slf4j.spi.NOPLoggingEventBuilder as __NOPLoggingEventBuilder
__NOPLoggingEventBuilder = __NOPLoggingEventBuilder
import org.slf4j.spi.LoggingEventBuilder as __LoggingEventBuilder
__LoggingEventBuilder = __LoggingEventBuilder
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NOPLoggingEventBuilder():
    """org.slf4j.spi.NOPLoggingEventBuilder"""
 
    @staticmethod
    def __wrap(java_value: __NOPLoggingEventBuilder) -> 'NOPLoggingEventBuilder':
        return NOPLoggingEventBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NOPLoggingEventBuilder):
        """
        Dynamic initializer for NOPLoggingEventBuilder.
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
    def log(self, arg0: str, *arg1: object):
        """public void org.slf4j.spi.NOPLoggingEventBuilder.log(java.lang.String,java.lang.Object...)"""
        super(__NOPLoggingEventBuilder, self).log(arg0, arg1)

    @override
    @overload
    def log(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.spi.NOPLoggingEventBuilder.log(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__NOPLoggingEventBuilder, self).log(arg0, arg1, arg2)

    @staticmethod
    @overload
    def singleton() -> 'LoggingEventBuilder':
        """public static org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.NOPLoggingEventBuilder.singleton()"""
        return LoggingEventBuilder.__wrap(__NOPLoggingEventBuilder.singleton())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def addArgument(self, arg0: 'Supplier') -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.NOPLoggingEventBuilder.addArgument(java.util.function.Supplier<?>)"""
        return 'LoggingEventBuilder'.__wrap(super(__NOPLoggingEventBuilder, self).addArgument(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setMessage(self, arg0: str) -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.NOPLoggingEventBuilder.setMessage(java.lang.String)"""
        return 'LoggingEventBuilder'.__wrap(super(__NOPLoggingEventBuilder, self).setMessage(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def addArgument(self, arg0: object) -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.NOPLoggingEventBuilder.addArgument(java.lang.Object)"""
        return 'LoggingEventBuilder'.__wrap(super(__NOPLoggingEventBuilder, self).addArgument(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def log(self, arg0: str):
        """public void org.slf4j.spi.NOPLoggingEventBuilder.log(java.lang.String)"""
        super(__NOPLoggingEventBuilder, self).log(arg0)

    @override
    @overload
    def log(self, arg0: str, arg1: object):
        """public void org.slf4j.spi.NOPLoggingEventBuilder.log(java.lang.String,java.lang.Object)"""
        super(__NOPLoggingEventBuilder, self).log(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setCause(self, arg0: 'Throwable') -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.NOPLoggingEventBuilder.setCause(java.lang.Throwable)"""
        return 'LoggingEventBuilder'.__wrap(super(__NOPLoggingEventBuilder, self).setCause(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def addMarker(self, arg0: 'Marker') -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.NOPLoggingEventBuilder.addMarker(org.slf4j.Marker)"""
        return 'LoggingEventBuilder'.__wrap(super(__NOPLoggingEventBuilder, self).addMarker(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setMessage(self, arg0: 'Supplier') -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.NOPLoggingEventBuilder.setMessage(java.util.function.Supplier<java.lang.String>)"""
        return 'LoggingEventBuilder'.__wrap(super(__NOPLoggingEventBuilder, self).setMessage(arg0))

    @override
    @overload
    def log(self, arg0: 'Supplier'):
        """public void org.slf4j.spi.NOPLoggingEventBuilder.log(java.util.function.Supplier<java.lang.String>)"""
        super(__NOPLoggingEventBuilder, self).log(arg0)

    @overload
    def addKeyValue(self, arg0: str, arg1: 'Supplier') -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.NOPLoggingEventBuilder.addKeyValue(java.lang.String,java.util.function.Supplier<java.lang.Object>)"""
        return 'LoggingEventBuilder'.__wrap(super(__NOPLoggingEventBuilder, self).addKeyValue(arg0, arg1))

    @override
    @overload
    def log(self):
        """public void org.slf4j.spi.NOPLoggingEventBuilder.log()"""
        super(NOPLoggingEventBuilder, self).log()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addKeyValue(self, arg0: str, arg1: object) -> 'LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.NOPLoggingEventBuilder.addKeyValue(java.lang.String,java.lang.Object)"""
        return 'LoggingEventBuilder'.__wrap(super(__NOPLoggingEventBuilder, self).addKeyValue(arg0, arg1)) 
 
 
# CLASS: org.slf4j.spi.LocationAwareLogger
from pyquantum_helper import import_once as __import_once__
import org.slf4j.spi.LoggingEventBuilder as __LoggingEventBuilder
__LoggingEventBuilder = __LoggingEventBuilder
from pyquantum_helper import override
try:
    from slf4py import event
except ImportError:
    event = __import_once__("slf4py.event")

import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

from builtins import object
from abc import abstractmethod, ABC
import org.slf4j.spi.LocationAwareLogger as __LocationAwareLogger
__LocationAwareLogger = __LocationAwareLogger
from builtins import bool
import org.slf4j.Logger as __Logger
__Logger = __Logger
 
class LocationAwareLogger(ABC):
    """org.slf4j.spi.LocationAwareLogger"""
 
    @staticmethod
    def __wrap(java_value: __LocationAwareLogger) -> 'LocationAwareLogger':
        return LocationAwareLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LocationAwareLogger):
        """
        Dynamic initializer for LocationAwareLogger.
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

    @override
    @overload
    def atTrace(self) -> 'LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atTrace())

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
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).makeLoggingEventBuilder(arg0))

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool.__wrap(super(__slf4py.Logger, self).isEnabledForLevel(arg0))

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

    @override
    @overload
    def atWarn(self) -> 'LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atWarn()"""
        return 'LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atWarn())

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

    @abstractmethod
    def log(self, arg0: 'Marker', arg1: str, arg2: int, arg3: str, arg4: 'Object', arg5: 'Throwable'):
        """public abstract void org.slf4j.spi.LocationAwareLogger.log(org.slf4j.Marker,java.lang.String,int,java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        pass

    @override
    @overload
    def atInfo(self) -> 'LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atInfo())

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

    @overload
    def atLevel(self, arg0: 'Level') -> 'LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).atLevel(arg0))

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

    @override
    @overload
    def atError(self) -> 'LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atError())

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

    @override
    @overload
    def atDebug(self) -> 'LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atDebug())

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled()"""
        pass

    @abstractmethod
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public abstract void org.slf4j.Logger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        pass 
 
 
# CLASS: org.slf4j.spi.CallerBoundaryAware
import org.slf4j.spi.CallerBoundaryAware as __CallerBoundaryAware
__CallerBoundaryAware = __CallerBoundaryAware
from abc import abstractmethod, ABC
 
class CallerBoundaryAware(ABC):
    """org.slf4j.spi.CallerBoundaryAware"""
 
    @staticmethod
    def __wrap(java_value: __CallerBoundaryAware) -> 'CallerBoundaryAware':
        return CallerBoundaryAware(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CallerBoundaryAware):
        """
        Dynamic initializer for CallerBoundaryAware.
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
    def setCallerBoundary(self, arg0: str):
        """public abstract void org.slf4j.spi.CallerBoundaryAware.setCallerBoundary(java.lang.String)"""
        pass 
 
 
# CLASS: org.slf4j.spi.LoggingEventBuilder
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import org.slf4j.spi.LoggingEventBuilder as __LoggingEventBuilder
__LoggingEventBuilder = __LoggingEventBuilder
import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

from abc import abstractmethod, ABC
from builtins import object
 
class LoggingEventBuilder(ABC):
    """org.slf4j.spi.LoggingEventBuilder"""
 
    @staticmethod
    def __wrap(java_value: __LoggingEventBuilder) -> 'LoggingEventBuilder':
        return LoggingEventBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggingEventBuilder):
        """
        Dynamic initializer for LoggingEventBuilder.
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
    def log(self, arg0: str):
        """public abstract void org.slf4j.spi.LoggingEventBuilder.log(java.lang.String)"""
        pass

    @abstractmethod
    def addArgument(self, arg0: 'Supplier'):
        """public abstract org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.LoggingEventBuilder.addArgument(java.util.function.Supplier<?>)"""
        pass

    @abstractmethod
    def setMessage(self, arg0: str):
        """public abstract org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.LoggingEventBuilder.setMessage(java.lang.String)"""
        pass

    @abstractmethod
    def setCause(self, arg0: 'Throwable'):
        """public abstract org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.LoggingEventBuilder.setCause(java.lang.Throwable)"""
        pass

    @abstractmethod
    def addKeyValue(self, arg0: str, arg1: 'Supplier'):
        """public abstract org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.LoggingEventBuilder.addKeyValue(java.lang.String,java.util.function.Supplier<java.lang.Object>)"""
        pass

    @abstractmethod
    def log(self, arg0: 'Supplier'):
        """public abstract void org.slf4j.spi.LoggingEventBuilder.log(java.util.function.Supplier<java.lang.String>)"""
        pass

    @abstractmethod
    def log(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.spi.LoggingEventBuilder.log(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def addMarker(self, arg0: 'Marker'):
        """public abstract org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.LoggingEventBuilder.addMarker(org.slf4j.Marker)"""
        pass

    @abstractmethod
    def setMessage(self, arg0: 'Supplier'):
        """public abstract org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.LoggingEventBuilder.setMessage(java.util.function.Supplier<java.lang.String>)"""
        pass

    @abstractmethod
    def log(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.spi.LoggingEventBuilder.log(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def addKeyValue(self, arg0: str, arg1: object):
        """public abstract org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.LoggingEventBuilder.addKeyValue(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def addArgument(self, arg0: object):
        """public abstract org.slf4j.spi.LoggingEventBuilder org.slf4j.spi.LoggingEventBuilder.addArgument(java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, ):
        """public abstract void org.slf4j.spi.LoggingEventBuilder.log()"""
        pass

    @abstractmethod
    def log(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.spi.LoggingEventBuilder.log(java.lang.String,java.lang.Object)"""
        pass 
 
 
# CLASS: org.slf4j.spi.MDCAdapter
import org.slf4j.spi.MDCAdapter as __MDCAdapter
__MDCAdapter = __MDCAdapter
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class MDCAdapter(ABC):
    """org.slf4j.spi.MDCAdapter"""
 
    @staticmethod
    def __wrap(java_value: __MDCAdapter) -> 'MDCAdapter':
        return MDCAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MDCAdapter):
        """
        Dynamic initializer for MDCAdapter.
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
    def pushByKey(self, arg0: str, arg1: str):
        """public abstract void org.slf4j.spi.MDCAdapter.pushByKey(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def get(self, arg0: str):
        """public abstract java.lang.String org.slf4j.spi.MDCAdapter.get(java.lang.String)"""
        pass

    @abstractmethod
    def getCopyOfDequeByKey(self, arg0: str):
        """public abstract java.util.Deque<java.lang.String> org.slf4j.spi.MDCAdapter.getCopyOfDequeByKey(java.lang.String)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.slf4j.spi.MDCAdapter.clear()"""
        pass

    @abstractmethod
    def popByKey(self, arg0: str):
        """public abstract java.lang.String org.slf4j.spi.MDCAdapter.popByKey(java.lang.String)"""
        pass

    @abstractmethod
    def setContextMap(self, arg0: 'Map'):
        """public abstract void org.slf4j.spi.MDCAdapter.setContextMap(java.util.Map<java.lang.String, java.lang.String>)"""
        pass

    @abstractmethod
    def clearDequeByKey(self, arg0: str):
        """public abstract void org.slf4j.spi.MDCAdapter.clearDequeByKey(java.lang.String)"""
        pass

    @abstractmethod
    def put(self, arg0: str, arg1: str):
        """public abstract void org.slf4j.spi.MDCAdapter.put(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def remove(self, arg0: str):
        """public abstract void org.slf4j.spi.MDCAdapter.remove(java.lang.String)"""
        pass

    @abstractmethod
    def getCopyOfContextMap(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.slf4j.spi.MDCAdapter.getCopyOfContextMap()"""
        pass