from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.logging.log4j.LogBuilder as __LogBuilder
__LogBuilder = __LogBuilder
from builtins import type
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

from builtins import object
import java.lang.StackTraceElement as StackTraceElement
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from log4py import spi
except ImportError:
    spi = __import_once__("log4py.spi")

import org.apache.logging.log4j.internal.DefaultLogBuilder as __DefaultLogBuilder
__DefaultLogBuilder = __DefaultLogBuilder
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

import java.lang.Object as __Object
__Object = __Object
try:
    import log4py
except ImportError:
    log4py = __import_once__("log4py")

import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DefaultLogBuilder():
    """org.apache.logging.log4j.internal.DefaultLogBuilder"""
 
    @staticmethod
    def __wrap(java_value: __DefaultLogBuilder) -> 'DefaultLogBuilder':
        return DefaultLogBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultLogBuilder):
        """
        Dynamic initializer for DefaultLogBuilder.
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
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def withLocation(self, location: 'StackTraceElement') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withLocation(java.lang.StackTraceElement)"""
        return 'log4py.LogBuilder'.__wrap(super(__DefaultLogBuilder, self).withLocation(location))

    @override
    @overload
    def log(self):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log()"""
        super(DefaultLogBuilder, self).log()

    @override
    @overload
    def setEntryPoint(self, fqcn: str):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.setEntryPoint(java.lang.String)"""
        super(__DefaultLogBuilder, self).setEntryPoint(fqcn)

    @override
    @overload
    def log(self, message: str, *params: 'util.Supplier'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__DefaultLogBuilder, self).log(message, params)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def log(self, message: str, p0: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0)

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5)

    @overload
    def reset(self, logger: 'ExtendedLogger', level: 'Level') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.reset(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'.__wrap(super(__DefaultLogBuilder, self).reset(logger, level))

    @override
    @overload
    def log(self, message: str, *params: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object...)"""
        super(__DefaultLogBuilder, self).log(message, params)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def log(self, message: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def log(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.CharSequence)"""
        super(__DefaultLogBuilder, self).log(message)

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.internal.DefaultLogBuilder()"""
        val = __DefaultLogBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def withMarker(self, marker: 'Marker') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withMarker(org.apache.logging.log4j.Marker)"""
        return 'log4py.LogBuilder'.__wrap(super(__DefaultLogBuilder, self).withMarker(marker))

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, logger: 'ExtendedLogger', level: 'Level'):
        """public org.apache.logging.log4j.internal.DefaultLogBuilder(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.Level)"""
        val = __DefaultLogBuilder(logger, level)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def withThrowable(self, throwable: 'Throwable') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withThrowable(java.lang.Throwable)"""
        return 'log4py.LogBuilder'.__wrap(super(__DefaultLogBuilder, self).withThrowable(throwable))

    @overload
    def isInUse(self) -> bool:
        """public boolean org.apache.logging.log4j.internal.DefaultLogBuilder.isInUse()"""
        return bool.__wrap(super(DefaultLogBuilder, self).isInUse())

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, message: str):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String)"""
        super(__DefaultLogBuilder, self).log(message)

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.internal.DefaultLogBuilder()"""
        val = __DefaultLogBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def log(self, message: 'Message'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(org.apache.logging.log4j.message.Message)"""
        super(__DefaultLogBuilder, self).log(message)

    @override
    @overload
    def log(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1)

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

    @override
    @overload
    def log(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(org.apache.logging.log4j.util.Supplier<org.apache.logging.log4j.message.Message>)"""
        super(__DefaultLogBuilder, self).log(messageSupplier)

    @overload
    def logAndGet(self, messageSupplier: 'Supplier') -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.internal.DefaultLogBuilder.logAndGet(org.apache.logging.log4j.util.Supplier<org.apache.logging.log4j.message.Message>)"""
        return 'message.Message'.__wrap(super(__DefaultLogBuilder, self).logAndGet(messageSupplier))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def withLocation(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withLocation()"""
        return 'log4py.LogBuilder'.__wrap(super(DefaultLogBuilder, self).withLocation())

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2)

 
 
 
# CLASS: org.apache.logging.log4j.internal.DefaultLogBuilder
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.logging.log4j.LogBuilder as __LogBuilder
__LogBuilder = __LogBuilder
from builtins import type
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

from builtins import object
import java.lang.StackTraceElement as StackTraceElement
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from log4py import spi
except ImportError:
    spi = __import_once__("log4py.spi")

import org.apache.logging.log4j.internal.DefaultLogBuilder as __DefaultLogBuilder
__DefaultLogBuilder = __DefaultLogBuilder
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

import java.lang.Object as __Object
__Object = __Object
try:
    import log4py
except ImportError:
    log4py = __import_once__("log4py")

import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DefaultLogBuilder():
    """org.apache.logging.log4j.internal.DefaultLogBuilder"""
 
    @staticmethod
    def __wrap(java_value: __DefaultLogBuilder) -> 'DefaultLogBuilder':
        return DefaultLogBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultLogBuilder):
        """
        Dynamic initializer for DefaultLogBuilder.
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
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def withLocation(self, location: 'StackTraceElement') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withLocation(java.lang.StackTraceElement)"""
        return 'log4py.LogBuilder'.__wrap(super(__DefaultLogBuilder, self).withLocation(location))

    @override
    @overload
    def log(self):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log()"""
        super(DefaultLogBuilder, self).log()

    @override
    @overload
    def setEntryPoint(self, fqcn: str):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.setEntryPoint(java.lang.String)"""
        super(__DefaultLogBuilder, self).setEntryPoint(fqcn)

    @override
    @overload
    def log(self, message: str, *params: 'util.Supplier'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(__DefaultLogBuilder, self).log(message, params)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def log(self, message: str, p0: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0)

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5)

    @overload
    def reset(self, logger: 'ExtendedLogger', level: 'Level') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.reset(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'.__wrap(super(__DefaultLogBuilder, self).reset(logger, level))

    @override
    @overload
    def log(self, message: str, *params: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object...)"""
        super(__DefaultLogBuilder, self).log(message, params)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def log(self, message: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def log(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.CharSequence)"""
        super(__DefaultLogBuilder, self).log(message)

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.internal.DefaultLogBuilder()"""
        val = __DefaultLogBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def withMarker(self, marker: 'Marker') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withMarker(org.apache.logging.log4j.Marker)"""
        return 'log4py.LogBuilder'.__wrap(super(__DefaultLogBuilder, self).withMarker(marker))

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, logger: 'ExtendedLogger', level: 'Level'):
        """public org.apache.logging.log4j.internal.DefaultLogBuilder(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.Level)"""
        val = __DefaultLogBuilder(logger, level)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def withThrowable(self, throwable: 'Throwable') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withThrowable(java.lang.Throwable)"""
        return 'log4py.LogBuilder'.__wrap(super(__DefaultLogBuilder, self).withThrowable(throwable))

    @overload
    def isInUse(self) -> bool:
        """public boolean org.apache.logging.log4j.internal.DefaultLogBuilder.isInUse()"""
        return bool.__wrap(super(DefaultLogBuilder, self).isInUse())

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, message: str):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String)"""
        super(__DefaultLogBuilder, self).log(message)

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.internal.DefaultLogBuilder()"""
        val = __DefaultLogBuilder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def log(self, message: 'Message'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(org.apache.logging.log4j.message.Message)"""
        super(__DefaultLogBuilder, self).log(message)

    @override
    @overload
    def log(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1)

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

    @override
    @overload
    def log(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(org.apache.logging.log4j.util.Supplier<org.apache.logging.log4j.message.Message>)"""
        super(__DefaultLogBuilder, self).log(messageSupplier)

    @overload
    def logAndGet(self, messageSupplier: 'Supplier') -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.internal.DefaultLogBuilder.logAndGet(org.apache.logging.log4j.util.Supplier<org.apache.logging.log4j.message.Message>)"""
        return 'message.Message'.__wrap(super(__DefaultLogBuilder, self).logAndGet(messageSupplier))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def withLocation(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.internal.DefaultLogBuilder.withLocation()"""
        return 'log4py.LogBuilder'.__wrap(super(DefaultLogBuilder, self).withLocation())

    @override
    @overload
    def log(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.internal.DefaultLogBuilder.log(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(__DefaultLogBuilder, self).log(message, p0, p1, p2)

 
 
 
# CLASS: org.apache.logging.log4j.internal.DefaultLogBuilder 
 
 
# CLASS: org.apache.logging.log4j.internal.LogManagerStatus
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
import java.lang.Integer as __int
from builtins import bool
import org.apache.logging.log4j.internal.LogManagerStatus as __LogManagerStatus
__LogManagerStatus = __LogManagerStatus
from builtins import int
 
class LogManagerStatus():
    """org.apache.logging.log4j.internal.LogManagerStatus"""
 
    @staticmethod
    def __wrap(java_value: __LogManagerStatus) -> 'LogManagerStatus':
        return LogManagerStatus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LogManagerStatus):
        """
        Dynamic initializer for LogManagerStatus.
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

    @staticmethod
    @overload
    def isInitialized() -> bool:
        """public static boolean org.apache.logging.log4j.internal.LogManagerStatus.isInitialized()"""
        return bool.__wrap(__LogManagerStatus.isInitialized())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.internal.LogManagerStatus()"""
        val = __LogManagerStatus()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.internal.LogManagerStatus()"""
        val = __LogManagerStatus()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def setInitialized(managerStatus: bool):
        """public static void org.apache.logging.log4j.internal.LogManagerStatus.setInitialized(boolean)"""
        __LogManagerStatus.setInitialized(__boolean.valueOf(managerStatus))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))