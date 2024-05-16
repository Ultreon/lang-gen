from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.net.URI as URI
import org.apache.logging.log4j.spi.LoggerContext as _LoggerContext
_LoggerContext = _LoggerContext
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.spi.LoggerContextFactory as _LoggerContextFactory
_LoggerContextFactory = _LoggerContextFactory
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
try:
    from log4py import spi
except ImportError:
    spi = _import_once("log4py.spi")

import java.lang.Integer as _int
import java.lang.ClassLoader as ClassLoader
import org.apache.logging.log4j.simple.SimpleLoggerContextFactory as _SimpleLoggerContextFactory
_SimpleLoggerContextFactory = _SimpleLoggerContextFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleLoggerContextFactory():
    """org.apache.logging.log4j.simple.SimpleLoggerContextFactory"""
 
    @staticmethod
    def _wrap(java_value: _SimpleLoggerContextFactory) -> 'SimpleLoggerContextFactory':
        return SimpleLoggerContextFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleLoggerContextFactory):
        """
        Dynamic initializer for SimpleLoggerContextFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleLoggerContextFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleLoggerContextFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getContext(self, fqcn: str, loader: 'ClassLoader', externalContext: object, currentContext: bool) -> 'spi.LoggerContext':
        """public org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.simple.SimpleLoggerContextFactory.getContext(java.lang.String,java.lang.ClassLoader,java.lang.Object,boolean)"""
        return 'spi.LoggerContext'._wrap(super(_SimpleLoggerContextFactory, self).getContext(fqcn, loader, externalContext, _boolean.valueOf(currentContext)))

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
    def removeContext(self, removeContext: 'LoggerContext'):
        """public void org.apache.logging.log4j.simple.SimpleLoggerContextFactory.removeContext(org.apache.logging.log4j.spi.LoggerContext)"""
        super(_SimpleLoggerContextFactory, self).removeContext(removeContext)

    @overload
    def getContext(self, fqcn: str, loader: 'ClassLoader', externalContext: object, currentContext: bool, configLocation: 'URI', name: str) -> 'spi.LoggerContext':
        """public org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.simple.SimpleLoggerContextFactory.getContext(java.lang.String,java.lang.ClassLoader,java.lang.Object,boolean,java.net.URI,java.lang.String)"""
        return 'spi.LoggerContext'._wrap(super(_SimpleLoggerContextFactory, self).getContext(fqcn, loader, externalContext, _boolean.valueOf(currentContext), configLocation, name))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def hasContext(self, fqcn: str, loader: 'ClassLoader', currentContext: bool) -> bool:
        """public default boolean org.apache.logging.log4j.spi.LoggerContextFactory.hasContext(java.lang.String,java.lang.ClassLoader,boolean)"""
        return bool._wrap(super(_spi.LoggerContextFactory, self).hasContext(fqcn, loader, _boolean.valueOf(currentContext)))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.simple.SimpleLoggerContextFactory()"""
        val = _SimpleLoggerContextFactory()
        self.__wrapper = val

    @override
    @overload
    def isClassLoaderDependent(self) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLoggerContextFactory.isClassLoaderDependent()"""
        return bool._wrap(super(SimpleLoggerContextFactory, self).isClassLoaderDependent())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def shutdown(self, fqcn: str, loader: 'ClassLoader', currentContext: bool, allContexts: bool):
        """public default void org.apache.logging.log4j.spi.LoggerContextFactory.shutdown(java.lang.String,java.lang.ClassLoader,boolean,boolean)"""
        super(_spi.LoggerContextFactory, self).shutdown(fqcn, loader, _boolean.valueOf(currentContext), _boolean.valueOf(allContexts))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.simple.SimpleLoggerContextFactory()"""
        val = _SimpleLoggerContextFactory()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.logging.log4j.simple.SimpleLoggerContextFactory
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.net.URI as URI
import org.apache.logging.log4j.spi.LoggerContext as _LoggerContext
_LoggerContext = _LoggerContext
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.spi.LoggerContextFactory as _LoggerContextFactory
_LoggerContextFactory = _LoggerContextFactory
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
try:
    from log4py import spi
except ImportError:
    spi = _import_once("log4py.spi")

import java.lang.Integer as _int
import java.lang.ClassLoader as ClassLoader
import org.apache.logging.log4j.simple.SimpleLoggerContextFactory as _SimpleLoggerContextFactory
_SimpleLoggerContextFactory = _SimpleLoggerContextFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleLoggerContextFactory():
    """org.apache.logging.log4j.simple.SimpleLoggerContextFactory"""
 
    @staticmethod
    def _wrap(java_value: _SimpleLoggerContextFactory) -> 'SimpleLoggerContextFactory':
        return SimpleLoggerContextFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleLoggerContextFactory):
        """
        Dynamic initializer for SimpleLoggerContextFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleLoggerContextFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleLoggerContextFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getContext(self, fqcn: str, loader: 'ClassLoader', externalContext: object, currentContext: bool) -> 'spi.LoggerContext':
        """public org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.simple.SimpleLoggerContextFactory.getContext(java.lang.String,java.lang.ClassLoader,java.lang.Object,boolean)"""
        return 'spi.LoggerContext'._wrap(super(_SimpleLoggerContextFactory, self).getContext(fqcn, loader, externalContext, _boolean.valueOf(currentContext)))

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
    def removeContext(self, removeContext: 'LoggerContext'):
        """public void org.apache.logging.log4j.simple.SimpleLoggerContextFactory.removeContext(org.apache.logging.log4j.spi.LoggerContext)"""
        super(_SimpleLoggerContextFactory, self).removeContext(removeContext)

    @overload
    def getContext(self, fqcn: str, loader: 'ClassLoader', externalContext: object, currentContext: bool, configLocation: 'URI', name: str) -> 'spi.LoggerContext':
        """public org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.simple.SimpleLoggerContextFactory.getContext(java.lang.String,java.lang.ClassLoader,java.lang.Object,boolean,java.net.URI,java.lang.String)"""
        return 'spi.LoggerContext'._wrap(super(_SimpleLoggerContextFactory, self).getContext(fqcn, loader, externalContext, _boolean.valueOf(currentContext), configLocation, name))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def hasContext(self, fqcn: str, loader: 'ClassLoader', currentContext: bool) -> bool:
        """public default boolean org.apache.logging.log4j.spi.LoggerContextFactory.hasContext(java.lang.String,java.lang.ClassLoader,boolean)"""
        return bool._wrap(super(_spi.LoggerContextFactory, self).hasContext(fqcn, loader, _boolean.valueOf(currentContext)))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.simple.SimpleLoggerContextFactory()"""
        val = _SimpleLoggerContextFactory()
        self.__wrapper = val

    @override
    @overload
    def isClassLoaderDependent(self) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLoggerContextFactory.isClassLoaderDependent()"""
        return bool._wrap(super(SimpleLoggerContextFactory, self).isClassLoaderDependent())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def shutdown(self, fqcn: str, loader: 'ClassLoader', currentContext: bool, allContexts: bool):
        """public default void org.apache.logging.log4j.spi.LoggerContextFactory.shutdown(java.lang.String,java.lang.ClassLoader,boolean,boolean)"""
        super(_spi.LoggerContextFactory, self).shutdown(fqcn, loader, _boolean.valueOf(currentContext), _boolean.valueOf(allContexts))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.simple.SimpleLoggerContextFactory()"""
        val = _SimpleLoggerContextFactory()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.logging.log4j.simple.SimpleLoggerContextFactory 
 
 
# CLASS: org.apache.logging.log4j.simple.SimpleLoggerContext
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.logging.log4j.spi.LoggerContext as _LoggerContext
_LoggerContext = _LoggerContext
from builtins import type
import java.lang.Object as _object
import org.apache.logging.log4j.spi.ExtendedLogger as _ExtendedLogger
_ExtendedLogger = _ExtendedLogger
import org.apache.logging.log4j.simple.SimpleLoggerContext as _SimpleLoggerContext
_SimpleLoggerContext = _SimpleLoggerContext
try:
    from log4py import message
except ImportError:
    message = _import_once("log4py.message")

from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
try:
    from log4py import spi
except ImportError:
    spi = _import_once("log4py.spi")

import java.lang.Integer as _int
from builtins import bool
import org.apache.logging.log4j.spi.LoggerRegistry as _LoggerRegistry
_LoggerRegistry = _LoggerRegistry
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleLoggerContext():
    """org.apache.logging.log4j.simple.SimpleLoggerContext"""
 
    @staticmethod
    def _wrap(java_value: _SimpleLoggerContext) -> 'SimpleLoggerContext':
        return SimpleLoggerContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleLoggerContext):
        """
        Dynamic initializer for SimpleLoggerContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleLoggerContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleLoggerContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getLogger(self, cls: 'Class') -> 'spi.ExtendedLogger':
        """public default org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.spi.LoggerContext.getLogger(java.lang.Class<?>)"""
        return 'spi.ExtendedLogger'._wrap(super(_spi.LoggerContext, self).getLogger(cls))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.simple.SimpleLoggerContext()"""
        val = _SimpleLoggerContext()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def putObjectIfAbsent(self, key: str, value: object) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.putObjectIfAbsent(java.lang.String,java.lang.Object)"""
        return object._wrap(super(_spi.LoggerContext, self).putObjectIfAbsent(key, value))

    @override
    @overload
    def getExternalContext(self) -> object:
        """public java.lang.Object org.apache.logging.log4j.simple.SimpleLoggerContext.getExternalContext()"""
        return object._wrap(super(SimpleLoggerContext, self).getExternalContext())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.simple.SimpleLoggerContext()"""
        val = _SimpleLoggerContext()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getLoggerRegistry(self) -> 'spi.LoggerRegistry':
        """public org.apache.logging.log4j.spi.LoggerRegistry<org.apache.logging.log4j.spi.ExtendedLogger> org.apache.logging.log4j.simple.SimpleLoggerContext.getLoggerRegistry()"""
        return 'spi.LoggerRegistry'._wrap(super(SimpleLoggerContext, self).getLoggerRegistry())

    @overload
    def getLogger(self, name: str, messageFactory: 'MessageFactory') -> 'spi.ExtendedLogger':
        """public org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.simple.SimpleLoggerContext.getLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        return 'spi.ExtendedLogger'._wrap(super(_SimpleLoggerContext, self).getLogger(name, messageFactory))

    @overload
    def getLogger(self, name: str) -> 'spi.ExtendedLogger':
        """public org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.simple.SimpleLoggerContext.getLogger(java.lang.String)"""
        return 'spi.ExtendedLogger'._wrap(super(_SimpleLoggerContext, self).getLogger(name))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def removeObject(self, key: str, value: object) -> bool:
        """public default boolean org.apache.logging.log4j.spi.LoggerContext.removeObject(java.lang.String,java.lang.Object)"""
        return bool._wrap(super(_spi.LoggerContext, self).removeObject(key, value))

    @overload
    def hasLogger(self, name: str) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLoggerContext.hasLogger(java.lang.String)"""
        return bool._wrap(super(_SimpleLoggerContext, self).hasLogger(name))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def putObject(self, key: str, value: object) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.putObject(java.lang.String,java.lang.Object)"""
        return object._wrap(super(_spi.LoggerContext, self).putObject(key, value))

    @overload
    def getLogger(self, cls: 'Class', messageFactory: 'MessageFactory') -> 'spi.ExtendedLogger':
        """public default org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.spi.LoggerContext.getLogger(java.lang.Class<?>,org.apache.logging.log4j.message.MessageFactory)"""
        return 'spi.ExtendedLogger'._wrap(super(_spi.LoggerContext, self).getLogger(cls, messageFactory))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def removeObject(self, key: str) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.removeObject(java.lang.String)"""
        return object._wrap(super(_spi.LoggerContext, self).removeObject(key))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getObject(self, key: str) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.getObject(java.lang.String)"""
        return object._wrap(super(_spi.LoggerContext, self).getObject(key))

    @overload
    def hasLogger(self, name: str, messageFactory: 'MessageFactory') -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLoggerContext.hasLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        return bool._wrap(super(_SimpleLoggerContext, self).hasLogger(name, messageFactory))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def hasLogger(self, name: str, messageFactoryClass: 'Class') -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLoggerContext.hasLogger(java.lang.String,java.lang.Class<? extends org.apache.logging.log4j.message.MessageFactory>)"""
        return bool._wrap(super(_SimpleLoggerContext, self).hasLogger(name, messageFactoryClass))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.simple.SimpleLogger
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.logging.log4j.Level as _Level
_Level = _Level
import org.apache.logging.log4j.message.MessageFactory as _MessageFactory
_MessageFactory = _MessageFactory
import java.lang.String as _string
import java.lang.Boolean as _boolean
try:
    from log4py import spi
except ImportError:
    spi = _import_once("log4py.spi")

try:
    from log4py import util
except ImportError:
    util = _import_once("log4py.util")

try:
    import log4py
except ImportError:
    log4py = _import_once("log4py")

from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.logging.log4j.simple.SimpleLogger as _SimpleLogger
_SimpleLogger = _SimpleLogger
import org.apache.logging.log4j.spi.AbstractLogger as _AbstractLogger
_AbstractLogger = _AbstractLogger
try:
    from log4py import message
except ImportError:
    message = _import_once("log4py.message")

from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import org.apache.logging.log4j.message.FlowMessageFactory as _FlowMessageFactory
_FlowMessageFactory = _FlowMessageFactory
import java.lang.Long as _long
import org.apache.logging.log4j.LogBuilder as _LogBuilder
_LogBuilder = _LogBuilder
import org.apache.logging.log4j.message.EntryMessage as _EntryMessage
_EntryMessage = _EntryMessage
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleLogger():
    """org.apache.logging.log4j.simple.SimpleLogger"""
 
    @staticmethod
    def _wrap(java_value: _SimpleLogger) -> 'SimpleLogger':
        return SimpleLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleLogger):
        """
        Dynamic initializer for SimpleLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def info(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).info(message, params)

    @override
    @overload
    def getMessageFactory(self) -> 'message.MessageFactory':
        """public <MF extends org.apache.logging.log4j.message.MessageFactory> MF org.apache.logging.log4j.spi.AbstractLogger.getMessageFactory()"""
        return 'message.MessageFactory'._wrap(super(spi.AbstractLogger, self).getMessageFactory())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @overload
    def isTraceEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_spi.AbstractLogger, self).isTraceEnabled(marker))

    @override
    @overload
    def warn(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', msg: object, t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, msg, t))

    @override
    @overload
    def log(self, level: 'Level', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).log(level, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).info(message, paramSuppliers)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, message, p0, p1, p2, p3, p4, p5, p6))

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', msg: 'CharSequence', t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, msg, t))

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def info(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def fatal(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(message)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def warn(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(message, throwable)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def isWarnEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_spi.AbstractLogger, self).isWarnEnabled(marker))

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(marker, message, p0)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def traceExit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit()"""
        super(spi.AbstractLogger, self).traceExit()

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_spi.AbstractLogger, self).isEnabled(level, marker))

    @override
    @overload
    def info(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String)"""
        super(_spi.AbstractLogger, self).info(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def catching(self, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).catching(throwable)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(marker, messageSupplier, throwable)

    @overload
    def isEnabled(self, level: 'Level') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level)"""
        return bool._wrap(super(_spi.AbstractLogger, self).isEnabled(level))

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, p0)

    @override
    @overload
    def warn(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).warn(message)

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(message, p0, p1)

    @override
    @overload
    def warn(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String)"""
        super(_spi.AbstractLogger, self).warn(message)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def error(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, p0, p1)

    @override
    @overload
    def debug(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(message, p0)

    @overload
    def traceExit(self, format: str, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(java.lang.String,R)"""
        return object._wrap(super(_spi.AbstractLogger, self).traceExit(format, result))

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(message, p0, p1)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).error(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, paramSuppliers)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(marker, message, p0)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def fatal(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).fatal(message, paramSuppliers)

    @override
    @overload
    def error(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).error(message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def trace(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).trace(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String)"""
        super(_spi.AbstractLogger, self).log(level, message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).debug(marker, message, paramSuppliers)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @overload
    def traceExit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(R)"""
        return object._wrap(super(_spi.AbstractLogger, self).traceExit(result))

    @override
    @overload
    def error(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).error(message)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, message, p0, p1, p2))

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(message, p0)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @staticmethod
    @overload
    def getRecursionDepth() -> int:
        """public static int org.apache.logging.log4j.spi.AbstractLogger.getRecursionDepth()"""
        return int._wrap(_AbstractLogger.getRecursionDepth())

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(marker, message, p0, p1)

    @override
    @overload
    def fatal(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String)"""
        super(_spi.AbstractLogger, self).fatal(message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).debug(message, params)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, message, p0, p1, p2, p3))

    @override
    @overload
    def error(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(message, throwable)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', msg: str, *p1: object) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, msg, p1))

    @override
    @overload
    def fatal(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def info(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def trace(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def atWarn(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atWarn()"""
        return 'log4py.LogBuilder'._wrap(super(spi.AbstractLogger, self).atWarn())

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).info(message)

    @override
    @overload
    def traceEntry(self) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry()"""
        return 'message.EntryMessage'._wrap(super(spi.AbstractLogger, self).traceEntry())

    @override
    @overload
    def trace(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).trace(message, params)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, params)

    @override
    @overload
    def error(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled()"""
        return bool._wrap(super(spi.AbstractLogger, self).isDebugEnabled())

    @override
    @overload
    def trace(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).trace(message, paramSuppliers)

    @override
    @overload
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).logMessage(level, marker, fqcn, location, message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def fatal(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).fatal(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(marker, message, p0, p1)

    @override
    @overload
    def warn(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).warn(message)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).info(marker, message)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(message, p0, p1, p2, p3)

    @overload
    def isInfoEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_spi.AbstractLogger, self).isInfoEnabled(marker))

    @override
    @overload
    def entry(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry()"""
        super(spi.AbstractLogger, self).entry()

    @override
    @overload
    def atTrace(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atTrace()"""
        return 'log4py.LogBuilder'._wrap(super(spi.AbstractLogger, self).atTrace())

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(marker, message)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def atDebug(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atDebug()"""
        return 'log4py.LogBuilder'._wrap(super(spi.AbstractLogger, self).atDebug())

    @override
    @overload
    def error(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(message, p0)

    @overload
    def throwing(self, throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(T)"""
        return 'Throwable'._wrap(super(_spi.AbstractLogger, self).throwing(throwable))

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).error(marker, message, params)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, message, p0)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(message, p0, p1)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def warn(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(message, throwable)

    @overload
    def traceEntry(self, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'._wrap(super(_spi.AbstractLogger, self).traceEntry(paramSuppliers))

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(message, p0, p1, p2, p3)

    @override
    @overload
    def debug(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def atInfo(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atInfo()"""
        return 'log4py.LogBuilder'._wrap(super(spi.AbstractLogger, self).atInfo())

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', msg: str, t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, msg, t))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).info(marker, message, params)

    @override
    @overload
    def debug(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).debug(message, paramSuppliers)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', message: str, p0: object) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, message, p0))

    @overload
    def traceExit(self, message: 'Message', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.Message,R)"""
        return object._wrap(super(_spi.AbstractLogger, self).traceExit(message, result))

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6)

    @overload
    def __init__(self, name: str, defaultLevel: 'Level', showLogName: bool, showShortLogName: bool, showDateTime: bool, showContextMap: bool, dateTimeFormat: str, messageFactory: 'MessageFactory', props: 'PropertiesUtil', stream: 'PrintStream'):
        """public org.apache.logging.log4j.simple.SimpleLogger(java.lang.String,org.apache.logging.log4j.Level,boolean,boolean,boolean,boolean,java.lang.String,org.apache.logging.log4j.message.MessageFactory,org.apache.logging.log4j.util.PropertiesUtil,java.io.PrintStream)"""
        val = _SimpleLogger(name, defaultLevel, _boolean.valueOf(showLogName), _boolean.valueOf(showShortLogName), _boolean.valueOf(showDateTime), _boolean.valueOf(showContextMap), dateTimeFormat, messageFactory, props, stream)
        self.__wrapper = val

    @override
    @overload
    def error(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def traceEntry(self, format: str, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'._wrap(super(_spi.AbstractLogger, self).traceEntry(format, paramSuppliers))

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @override
    @overload
    def error(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(marker, message, p0, p1, p2)

    @override
    @overload
    def debug(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String)"""
        super(_spi.AbstractLogger, self).debug(message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def setLevel(self, level: 'Level'):
        """public void org.apache.logging.log4j.simple.SimpleLogger.setLevel(org.apache.logging.log4j.Level)"""
        super(_SimpleLogger, self).setLevel(level)

    @override
    @overload
    def log(self, level: 'Level', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).log(level, message, paramSuppliers)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(message, p0, p1, p2, p3)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def debug(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def trace(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def error(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).trace(marker, message, params)

    @override
    @overload
    def warn(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def logMessage(self, fqcn: str, mgsLevel: 'Level', marker: 'Marker', msg: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.simple.SimpleLogger.logMessage(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_SimpleLogger, self).logMessage(fqcn, mgsLevel, marker, msg, throwable)

    @override
    @overload
    def getLevel(self) -> 'log4py.Level':
        """public org.apache.logging.log4j.Level org.apache.logging.log4j.simple.SimpleLogger.getLevel()"""
        return 'log4py.Level'._wrap(super(SimpleLogger, self).getLevel())

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def debug(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled()"""
        return bool._wrap(super(spi.AbstractLogger, self).isInfoEnabled())

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(message, p0)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def printf(self, level: 'Level', marker: 'Marker', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).printf(level, marker, format, params)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, p0)

    @overload
    def setStream(self, stream: 'PrintStream'):
        """public void org.apache.logging.log4j.simple.SimpleLogger.setStream(java.io.PrintStream)"""
        super(_SimpleLogger, self).setStream(stream)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_spi.AbstractLogger, self).error(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(marker, message, p0, p1)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, message, p0, p1, p2, p3, p4))

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3)

    @overload
    def throwing(self, level: 'Level', throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(org.apache.logging.log4j.Level,T)"""
        return 'Throwable'._wrap(super(_spi.AbstractLogger, self).throwing(level, throwable))

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).fatal(marker, message)

    @overload
    def traceEntry(self, format: str, *params: object) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,java.lang.Object...)"""
        return 'message.EntryMessage'._wrap(super(_spi.AbstractLogger, self).traceEntry(format, params))

    @override
    @overload
    def info(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', msg: 'Message', t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, msg, t))

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).log(level, message, params)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).trace(marker, message, paramSuppliers)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, p0, p1)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def warn(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(message, throwable)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', msg: str) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, msg))

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_spi.AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def printf(self, level: 'Level', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).printf(level, format, params)

    @overload
    def isErrorEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_spi.AbstractLogger, self).isErrorEnabled(marker))

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).info(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def fatal(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).fatal(message, params)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).error(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled()"""
        return bool._wrap(super(spi.AbstractLogger, self).isWarnEnabled())

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, message, p0, p1)

    @override
    @overload
    def warn(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).warn(message, paramSuppliers)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4)

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
    def log(self, level: 'Level', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(message, p0, p1, p2)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(message, p0, p1, p2, p3)

    @override
    @overload
    def debug(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(marker, message, p0, p1, p2)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def trace(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(marker, message, p0, p1, p2)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, params)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).log(level, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, message, p0, p1, p2)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(marker, message, p0, p1)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def info(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(message, p0, p1)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_spi.AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def debug(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).warn(marker, message, params)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def fatal(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def traceExit(self, message: 'EntryMessage'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage)"""
        super(_spi.AbstractLogger, self).traceExit(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled()"""
        return bool._wrap(super(spi.AbstractLogger, self).isErrorEnabled())

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_spi.AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def warn(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(message)

    @override
    @overload
    def trace(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def debug(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).debug(message)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(marker, message, p0)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, paramSuppliers)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(marker, message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_spi.AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String)"""
        super(_spi.AbstractLogger, self).trace(message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_spi.AbstractLogger, self).info(marker, message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(marker, message, p0, p1)

    @override
    @overload
    def error(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).error(message, params)

    @overload
    def atLevel(self, level: 'Level') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atLevel(org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'._wrap(super(_spi.AbstractLogger, self).atLevel(level))

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def error(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String)"""
        super(_spi.AbstractLogger, self).error(message)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.AbstractLogger.getName()"""
        return str._wrap(super(spi.AbstractLogger, self).getName())

    @override
    @overload
    def exit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.exit()"""
        super(spi.AbstractLogger, self).exit()

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def entry(self, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry(java.lang.Object...)"""
        super(_spi.AbstractLogger, self).entry(params)

    @override
    @overload
    def info(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, paramSuppliers)

    @override
    @overload
    def info(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, params)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(marker, message, p0)

    @override
    @overload
    def getFlowMessageFactory(self) -> 'message.FlowMessageFactory':
        """public org.apache.logging.log4j.message.FlowMessageFactory org.apache.logging.log4j.spi.AbstractLogger.getFlowMessageFactory()"""
        return 'message.FlowMessageFactory'._wrap(super(spi.AbstractLogger, self).getFlowMessageFactory())

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def info(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def trace(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).trace(message)

    @overload
    def exit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.exit(R)"""
        return object._wrap(super(_spi.AbstractLogger, self).exit(result))

    @override
    @overload
    def isFatalEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled()"""
        return bool._wrap(super(spi.AbstractLogger, self).isFatalEnabled())

    @override
    @overload
    def atError(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atError()"""
        return 'log4py.LogBuilder'._wrap(super(spi.AbstractLogger, self).atError())

    @override
    @overload
    def warn(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).warn(message, params)

    @override
    @overload
    def fatal(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(message, p0)

    @overload
    def isDebugEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_spi.AbstractLogger, self).isDebugEnabled(marker))

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(message, p0, p1, p2)

    @override
    @overload
    def fatal(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).fatal(message)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(message, p0, p1)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def traceExit(self, message: 'EntryMessage', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage,R)"""
        return object._wrap(super(_spi.AbstractLogger, self).traceExit(message, result))

    @staticmethod
    @overload
    def checkMessageFactory(logger: 'ExtendedLogger', messageFactory: 'MessageFactory'):
        """public static void org.apache.logging.log4j.spi.AbstractLogger.checkMessageFactory(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.message.MessageFactory)"""
        _AbstractLogger.checkMessageFactory(logger, messageFactory)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).debug(message)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def atFatal(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atFatal()"""
        return 'log4py.LogBuilder'._wrap(super(spi.AbstractLogger, self).atFatal())

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).warn(marker, message, paramSuppliers)

    @overload
    def traceEntry(self, message: 'Message') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.message.Message)"""
        return 'message.EntryMessage'._wrap(super(_spi.AbstractLogger, self).traceEntry(message))

    @override
    @overload
    def always(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.always()"""
        return 'log4py.LogBuilder'._wrap(super(spi.AbstractLogger, self).always())

    @override
    @overload
    def catching(self, level: 'Level', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(org.apache.logging.log4j.Level,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).catching(level, throwable)

    @overload
    def isFatalEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_spi.AbstractLogger, self).isFatalEnabled(marker))

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_spi.AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(marker, message, p0, p1, p2)

    @override
    @overload
    def warn(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).warn(message, p0)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(message, p0, p1, p2)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).error(marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).trace(message, p0, p1, p2)

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled()"""
        return bool._wrap(super(spi.AbstractLogger, self).isTraceEnabled())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_spi.AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).error(marker, message, paramSuppliers)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', message: str, p0: object, p1: object) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, message, p0, p1))

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(message, p0, p1, p2)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).info(marker, message, paramSuppliers)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_spi.AbstractLogger, self).debug(marker, message, params)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_spi.AbstractLogger, self).error(message, paramSuppliers)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_spi.AbstractLogger, self).info(marker, message)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(message, p0, p1, p2)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(message, p0, p1)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @overload
    def isEnabled(self, testLevel: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> bool:
        """public boolean org.apache.logging.log4j.simple.SimpleLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_SimpleLogger, self).isEnabled(testLevel, marker, message, p0, p1, p2, p3, p4, p5))

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_spi.AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_spi.AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_spi.AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_spi.AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_spi.AbstractLogger, self).warn(messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_spi.AbstractLogger, self).error(marker, message, p0)