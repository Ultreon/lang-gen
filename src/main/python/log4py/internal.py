from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.apache.logging.log4j.internal.LogManagerStatus as _LogManagerStatus
_LogManagerStatus = _LogManagerStatus
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LogManagerStatus():
    """org.apache.logging.log4j.internal.LogManagerStatus"""
 
    @staticmethod
    def _wrap(java_value: _LogManagerStatus) -> 'LogManagerStatus':
        return LogManagerStatus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LogManagerStatus):
        """
        Dynamic initializer for LogManagerStatus.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LogManagerStatus__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LogManagerStatus__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.internal.LogManagerStatus()"""
        val = _LogManagerStatus()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def setInitialized(managerStatus: bool):
        """public static void org.apache.logging.log4j.internal.LogManagerStatus.setInitialized(boolean)"""
        _LogManagerStatus.setInitialized(_boolean.valueOf(managerStatus))

    @staticmethod
    @overload
    def isInitialized() -> bool:
        """public static boolean org.apache.logging.log4j.internal.LogManagerStatus.isInitialized()"""
        return bool._wrap(_LogManagerStatus.isInitialized())

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

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.internal.LogManagerStatus()"""
        val = _LogManagerStatus()
        self.__wrapper = val

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

 
 
 
# CLASS: org.apache.logging.log4j.internal.LogManagerStatus
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.apache.logging.log4j.internal.LogManagerStatus as _LogManagerStatus
_LogManagerStatus = _LogManagerStatus
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LogManagerStatus():
    """org.apache.logging.log4j.internal.LogManagerStatus"""
 
    @staticmethod
    def _wrap(java_value: _LogManagerStatus) -> 'LogManagerStatus':
        return LogManagerStatus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LogManagerStatus):
        """
        Dynamic initializer for LogManagerStatus.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LogManagerStatus__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LogManagerStatus__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.internal.LogManagerStatus()"""
        val = _LogManagerStatus()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def setInitialized(managerStatus: bool):
        """public static void org.apache.logging.log4j.internal.LogManagerStatus.setInitialized(boolean)"""
        _LogManagerStatus.setInitialized(_boolean.valueOf(managerStatus))

    @staticmethod
    @overload
    def isInitialized() -> bool:
        """public static boolean org.apache.logging.log4j.internal.LogManagerStatus.isInitialized()"""
        return bool._wrap(_LogManagerStatus.isInitialized())

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

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.internal.LogManagerStatus()"""
        val = _LogManagerStatus()
        self.__wrapper = val

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

 
 
 
# CLASS: org.apache.logging.log4j.internal.LogManagerStatus 
 
 
# CLASS: org.apache.logging.log4j.internal.DefaultLogBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.internal.DefaultLogBuilder as _DefaultLogBuilder
_DefaultLogBuilder = _DefaultLogBuilder
try:
    from log4py import message
except ImportError:
    message = _import_once("log4py.message")

from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
import java.lang.String as _string
try:
    from log4py import spi
except ImportError:
    spi = _import_once("log4py.spi")

import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
try:
    from log4py import util
except ImportError:
    util = _import_once("log4py.util")

try:
    import log4py
except ImportError:
    log4py = _import_once("log4py")

import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
import org.apache.logging.log4j.LogBuilder as _LogBuilder
_LogBuilder = _LogBuilder
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultLogBuilder():
    """org.apache.logging.log4j.internal.DefaultLogBuilder"""
 
    @staticmethod
    def _wrap(java_value: _DefaultLogBuilder) -> 'DefaultLogBuilder':
        return DefaultLogBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultLogBuilder):
        """
        Dynamic initializer for DefaultLogBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultLogBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultLogBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def log(self, message: str):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String)"""
        super(_DefaultLogBuilder, self).log(message)

    @override
    @overload
    def log(self):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log()"""
        super(DefaultLogBuilder, self).log()

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def log(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_DefaultLogBuilder, self).log(message, p0, p1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def reset(self, logger: 'ExtendedLogger', level: 'Level') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.reset(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'._wrap(super(_DefaultLogBuilder, self).reset(logger, level))

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def withThrowable(self, throwable: 'Throwable') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withThrowable(java.lang.Throwable)"""
        return 'log4py.LogBuilder'._wrap(super(_DefaultLogBuilder, self).withThrowable(throwable))

    @override
    @overload
    def log(self, message: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.Object)"""
        super(_DefaultLogBuilder, self).log(message)

    @override
    @overload
    def log(self, message: 'Message'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(org.apache.logging.log4j.message.Message)"""
        super(_DefaultLogBuilder, self).log(message)

    @overload
    def withMarker(self, marker: 'Marker') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withMarker(org.apache.logging.log4j.Marker)"""
        return 'log4py.LogBuilder'._wrap(super(_DefaultLogBuilder, self).withMarker(marker))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, logger: 'ExtendedLogger', level: 'Level'):
        """public org.apache.logging.log4j.internal.DefaultLogBuilder(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.Level)"""
        val = _DefaultLogBuilder(logger, level)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4)

    @overload
    def logAndGet(self, messageSupplier: 'Supplier') -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.internal.DefaultLogBuilder.logAndGet(org.apache.logging.log4j.util.Supplier<org.apache.logging.log4j.message.Message>)"""
        return 'message.Message'._wrap(super(_DefaultLogBuilder, self).logAndGet(messageSupplier))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.internal.DefaultLogBuilder()"""
        val = _DefaultLogBuilder()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.internal.DefaultLogBuilder()"""
        val = _DefaultLogBuilder()
        self.__wrapper = val

    @override
    @overload
    def log(self, message: str, p0: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object)"""
        super(_DefaultLogBuilder, self).log(message, p0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_DefaultLogBuilder, self).log(message, p0, p1, p2)

    @override
    @overload
    def log(self, message: str, *params: 'util.Supplier'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_DefaultLogBuilder, self).log(message, params)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def log(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.CharSequence)"""
        super(_DefaultLogBuilder, self).log(message)

    @override
    @overload
    def setEntryPoint(self, fqcn: str):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.setEntryPoint(java.lang.String)"""
        super(_DefaultLogBuilder, self).setEntryPoint(fqcn)

    @overload
    def isInUse(self) -> bool:
        """public boolean org.apache.logging.log4j.internal.DefaultLogBuilder.isInUse()"""
        return bool._wrap(super(DefaultLogBuilder, self).isInUse())

    @override
    @overload
    def log(self, message: str, *params: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object...)"""
        super(_DefaultLogBuilder, self).log(message, params)

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def withLocation(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withLocation()"""
        return 'log4py.LogBuilder'._wrap(super(DefaultLogBuilder, self).withLocation())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_DefaultLogBuilder, self).log(message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(org.apache.logging.log4j.util.Supplier<org.apache.logging.log4j.message.Message>)"""
        super(_DefaultLogBuilder, self).log(messageSupplier)

    @overload
    def withLocation(self, location: 'StackTraceElement') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withLocation(java.lang.StackTraceElement)"""
        return 'log4py.LogBuilder'._wrap(super(_DefaultLogBuilder, self).withLocation(location))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())