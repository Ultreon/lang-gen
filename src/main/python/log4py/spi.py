from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.logging.log4j.Level as _Level
_Level = _Level
import org.apache.logging.log4j.message.MessageFactory as _MessageFactory
_MessageFactory = _MessageFactory
import java.lang.String as _string
try:
    from log4py import util
except ImportError:
    util = _import_once("log4py.util")

import org.apache.logging.log4j.spi.ExtendedLoggerWrapper as _ExtendedLoggerWrapper
_ExtendedLoggerWrapper = _ExtendedLoggerWrapper
try:
    import log4py
except ImportError:
    log4py = _import_once("log4py")

from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _object
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
 
class ExtendedLoggerWrapper():
    """org.apache.logging.log4j.spi.ExtendedLoggerWrapper"""
 
    @staticmethod
    def _wrap(java_value: _ExtendedLoggerWrapper) -> 'ExtendedLoggerWrapper':
        return ExtendedLoggerWrapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExtendedLoggerWrapper):
        """
        Dynamic initializer for ExtendedLoggerWrapper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExtendedLoggerWrapper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExtendedLoggerWrapper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @overload
    def isTraceEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isTraceEnabled(marker))

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1)

    @override
    @overload
    def atDebug(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atDebug()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atDebug())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.AbstractLogger.getName()"""
        return str._wrap(super(AbstractLogger, self).getName())

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def info(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).info(message, params)

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isInfoEnabled())

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @overload
    def throwing(self, level: 'Level', throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(org.apache.logging.log4j.Level,T)"""
        return 'Throwable'._wrap(super(_AbstractLogger, self).throwing(level, throwable))

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).log(level, marker, message, params)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def trace(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def error(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2)

    @override
    @overload
    def trace(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def info(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).info(marker, message, paramSuppliers)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def printf(self, level: 'Level', marker: 'Marker', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).printf(level, marker, format, params)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def fatal(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).fatal(message, params)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).trace(message)

    @overload
    def isDebugEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isDebugEnabled(marker))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @overload
    def isFatalEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isFatalEnabled(marker))

    @override
    @overload
    def error(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(messageSupplier, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def __init__(self, logger: 'ExtendedLogger', name: str, messageFactory: 'MessageFactory'):
        """public org.apache.logging.log4j.spi.ExtendedLoggerWrapper(org.apache.logging.log4j.spi.ExtendedLogger,java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        val = _ExtendedLoggerWrapper(logger, name, messageFactory)
        self.__wrapper = val

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @staticmethod
    @overload
    def getRecursionDepth() -> int:
        """public static int org.apache.logging.log4j.spi.AbstractLogger.getRecursionDepth()"""
        return int._wrap(_AbstractLogger.getRecursionDepth())

    @override
    @overload
    def debug(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def warn(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).warn(message, params)

    @overload
    def traceExit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(result))

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).info(marker, message)

    @override
    @overload
    def fatal(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def fatal(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isErrorEnabled())

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, messageSupplier, throwable)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0)

    @override
    @overload
    def info(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).info(message, paramSuppliers)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2))

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1)

    @override
    @overload
    def logMessage(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public void org.apache.logging.log4j.spi.ExtendedLoggerWrapper.logMessage(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_ExtendedLoggerWrapper, self).logMessage(fqcn, level, marker, message, t)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def warn(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String)"""
        super(_AbstractLogger, self).warn(message)

    @override
    @overload
    def catching(self, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(java.lang.Throwable)"""
        super(_AbstractLogger, self).catching(throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def error(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def log(self, level: 'Level', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).log(level, message, params)

    @overload
    def isWarnEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isWarnEnabled(marker))

    @override
    @overload
    def trace(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def printf(self, level: 'Level', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).printf(level, format, params)

    @override
    @overload
    def info(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def debug(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence)"""
        super(_AbstractLogger, self).info(message)

    @overload
    def isInfoEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isInfoEnabled(marker))

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1)

    @override
    @overload
    def trace(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message)

    @overload
    def traceEntry(self, format: str, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(format, paramSuppliers))

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def debug(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def isFatalEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isFatalEnabled())

    @override
    @overload
    def trace(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).debug(message, params)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).log(level, message)

    @overload
    def traceEntry(self, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(paramSuppliers))

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1)

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def traceEntry(self) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry()"""
        return 'message.EntryMessage'._wrap(super(AbstractLogger, self).traceEntry())

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).info(marker, message, params)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def log(self, level: 'Level', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String)"""
        super(_AbstractLogger, self).log(level, message)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: object, t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def error(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).log(level, marker, message, paramSuppliers)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence)"""
        super(_AbstractLogger, self).log(level, message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).warn(marker, message, params)

    @override
    @overload
    def info(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String)"""
        super(_AbstractLogger, self).info(message)

    @override
    @overload
    def warn(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'CharSequence', t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).warn(marker, message, paramSuppliers)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def info(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).info(message)

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).log(level, messageSupplier)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3)

    @override
    @overload
    def fatal(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0)

    @override
    @overload
    def debug(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).debug(message, paramSuppliers)

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def entry(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry()"""
        super(AbstractLogger, self).entry()

    @override
    @overload
    def debug(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def error(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).error(message, params)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def warn(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).warn(message, paramSuppliers)

    @override
    @overload
    def warn(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence)"""
        super(_AbstractLogger, self).warn(message)

    @override
    @overload
    def atWarn(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atWarn()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atWarn())

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).fatal(marker, message, paramSuppliers)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def error(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).logMessage(level, marker, fqcn, location, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3))

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def atError(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atError()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atError())

    @overload
    def isEnabled(self, level: 'Level') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level)"""
        return bool._wrap(super(_AbstractLogger, self).isEnabled(level))

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, paramSuppliers)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).debug(marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def error(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).error(message, paramSuppliers)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6))

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).info(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def log(self, level: 'Level', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5))

    @override
    @overload
    def getLevel(self) -> 'log4py.Level':
        """public org.apache.logging.log4j.Level org.apache.logging.log4j.spi.ExtendedLoggerWrapper.getLevel()"""
        return 'log4py.Level'._wrap(super(ExtendedLoggerWrapper, self).getLevel())

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).error(marker, message, paramSuppliers)

    @override
    @overload
    def fatal(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isTraceEnabled())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).trace(marker, message, params)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object)"""
        super(_AbstractLogger, self).trace(message)

    @override
    @overload
    def trace(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String)"""
        super(_AbstractLogger, self).trace(message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def traceExit(self, message: 'EntryMessage', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage,R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(message, result))

    @override
    @overload
    def debug(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0)

    @override
    @overload
    def warn(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).warn(message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def error(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1))

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def warn(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).fatal(marker, message, params)

    @overload
    def atLevel(self, level: 'Level') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atLevel(org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'._wrap(super(_AbstractLogger, self).atLevel(level))

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def trace(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).trace(message, paramSuppliers)

    @override
    @overload
    def debug(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def getMessageFactory(self) -> 'message.MessageFactory':
        """public <MF extends org.apache.logging.log4j.message.MessageFactory> MF org.apache.logging.log4j.spi.AbstractLogger.getMessageFactory()"""
        return 'message.MessageFactory'._wrap(super(AbstractLogger, self).getMessageFactory())

    @override
    @overload
    def exit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.exit()"""
        super(AbstractLogger, self).exit()

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0)

    @override
    @overload
    def atInfo(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atInfo()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atInfo())

    @override
    @overload
    def atFatal(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atFatal()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atFatal())

    @overload
    def exit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.exit(R)"""
        return object._wrap(super(_AbstractLogger, self).exit(result))

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).error(marker, message, params)

    @overload
    def throwing(self, throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(T)"""
        return 'Throwable'._wrap(super(_AbstractLogger, self).throwing(throwable))

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0)

    @override
    @overload
    def log(self, level: 'Level', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).log(level, message, paramSuppliers)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def error(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def error(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def error(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message)

    @override
    @overload
    def atTrace(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atTrace()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atTrace())

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def info(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object)"""
        super(_AbstractLogger, self).info(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def traceEntry(self, message: 'Message') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.message.Message)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(message))

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def traceExit(self, message: 'Message', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.Message,R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(message, result))

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @overload
    def traceExit(self, format: str, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(java.lang.String,R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(format, result))

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).trace(marker, message, paramSuppliers)

    @overload
    def traceEntry(self, format: str, *params: object) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,java.lang.Object...)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(format, params))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4))

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message)

    @staticmethod
    @overload
    def checkMessageFactory(logger: 'ExtendedLogger', messageFactory: 'MessageFactory'):
        """public static void org.apache.logging.log4j.spi.AbstractLogger.checkMessageFactory(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.message.MessageFactory)"""
        _AbstractLogger.checkMessageFactory(logger, messageFactory)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def fatal(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0)

    @override
    @overload
    def entry(self, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry(java.lang.Object...)"""
        super(_AbstractLogger, self).entry(params)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).info(marker, message)

    @override
    @overload
    def log(self, level: 'Level', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def traceExit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit()"""
        super(AbstractLogger, self).traceExit()

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, level: 'Level', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).debug(marker, message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2)

    @override
    @overload
    def warn(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object)"""
        super(_AbstractLogger, self).warn(message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isEnabled(level, marker))

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, *params: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, params))

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def debug(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).trace(message, params)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def fatal(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def getFlowMessageFactory(self) -> 'message.FlowMessageFactory':
        """public org.apache.logging.log4j.message.FlowMessageFactory org.apache.logging.log4j.spi.AbstractLogger.getFlowMessageFactory()"""
        return 'message.FlowMessageFactory'._wrap(super(AbstractLogger, self).getFlowMessageFactory())

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1)

    @overload
    def isErrorEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isErrorEnabled(marker))

    @override
    @overload
    def always(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.always()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).always())

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isDebugEnabled())

    @override
    @overload
    def error(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def catching(self, level: 'Level', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(org.apache.logging.log4j.Level,java.lang.Throwable)"""
        super(_AbstractLogger, self).catching(level, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def fatal(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).fatal(message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isWarnEnabled())

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2)

    @override
    @overload
    def traceExit(self, message: 'EntryMessage'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage)"""
        super(_AbstractLogger, self).traceExit(message)

    @override
    @overload
    def trace(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence)"""
        super(_AbstractLogger, self).trace(message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1)

 
 
 
# CLASS: org.apache.logging.log4j.spi.ExtendedLoggerWrapper
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.logging.log4j.Level as _Level
_Level = _Level
import org.apache.logging.log4j.message.MessageFactory as _MessageFactory
_MessageFactory = _MessageFactory
import java.lang.String as _string
try:
    from log4py import util
except ImportError:
    util = _import_once("log4py.util")

import org.apache.logging.log4j.spi.ExtendedLoggerWrapper as _ExtendedLoggerWrapper
_ExtendedLoggerWrapper = _ExtendedLoggerWrapper
try:
    import log4py
except ImportError:
    log4py = _import_once("log4py")

from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _object
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
 
class ExtendedLoggerWrapper():
    """org.apache.logging.log4j.spi.ExtendedLoggerWrapper"""
 
    @staticmethod
    def _wrap(java_value: _ExtendedLoggerWrapper) -> 'ExtendedLoggerWrapper':
        return ExtendedLoggerWrapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExtendedLoggerWrapper):
        """
        Dynamic initializer for ExtendedLoggerWrapper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExtendedLoggerWrapper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExtendedLoggerWrapper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @overload
    def isTraceEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isTraceEnabled(marker))

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1)

    @override
    @overload
    def atDebug(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atDebug()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atDebug())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.AbstractLogger.getName()"""
        return str._wrap(super(AbstractLogger, self).getName())

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def info(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).info(message, params)

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isInfoEnabled())

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @overload
    def throwing(self, level: 'Level', throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(org.apache.logging.log4j.Level,T)"""
        return 'Throwable'._wrap(super(_AbstractLogger, self).throwing(level, throwable))

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).log(level, marker, message, params)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def trace(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def error(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2)

    @override
    @overload
    def trace(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def info(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).info(marker, message, paramSuppliers)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def printf(self, level: 'Level', marker: 'Marker', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).printf(level, marker, format, params)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def fatal(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).fatal(message, params)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).trace(message)

    @overload
    def isDebugEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isDebugEnabled(marker))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @overload
    def isFatalEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isFatalEnabled(marker))

    @override
    @overload
    def error(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(messageSupplier, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def __init__(self, logger: 'ExtendedLogger', name: str, messageFactory: 'MessageFactory'):
        """public org.apache.logging.log4j.spi.ExtendedLoggerWrapper(org.apache.logging.log4j.spi.ExtendedLogger,java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        val = _ExtendedLoggerWrapper(logger, name, messageFactory)
        self.__wrapper = val

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @staticmethod
    @overload
    def getRecursionDepth() -> int:
        """public static int org.apache.logging.log4j.spi.AbstractLogger.getRecursionDepth()"""
        return int._wrap(_AbstractLogger.getRecursionDepth())

    @override
    @overload
    def debug(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def warn(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).warn(message, params)

    @overload
    def traceExit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(result))

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).info(marker, message)

    @override
    @overload
    def fatal(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def fatal(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isErrorEnabled())

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, messageSupplier, throwable)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0)

    @override
    @overload
    def info(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).info(message, paramSuppliers)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2))

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1)

    @override
    @overload
    def logMessage(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public void org.apache.logging.log4j.spi.ExtendedLoggerWrapper.logMessage(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_ExtendedLoggerWrapper, self).logMessage(fqcn, level, marker, message, t)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def warn(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String)"""
        super(_AbstractLogger, self).warn(message)

    @override
    @overload
    def catching(self, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(java.lang.Throwable)"""
        super(_AbstractLogger, self).catching(throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def error(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def log(self, level: 'Level', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).log(level, message, params)

    @overload
    def isWarnEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isWarnEnabled(marker))

    @override
    @overload
    def trace(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def printf(self, level: 'Level', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).printf(level, format, params)

    @override
    @overload
    def info(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def debug(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence)"""
        super(_AbstractLogger, self).info(message)

    @overload
    def isInfoEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isInfoEnabled(marker))

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1)

    @override
    @overload
    def trace(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message)

    @overload
    def traceEntry(self, format: str, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(format, paramSuppliers))

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def debug(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def isFatalEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isFatalEnabled())

    @override
    @overload
    def trace(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).debug(message, params)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).log(level, message)

    @overload
    def traceEntry(self, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(paramSuppliers))

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1)

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def traceEntry(self) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry()"""
        return 'message.EntryMessage'._wrap(super(AbstractLogger, self).traceEntry())

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).info(marker, message, params)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def log(self, level: 'Level', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String)"""
        super(_AbstractLogger, self).log(level, message)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: object, t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def error(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).log(level, marker, message, paramSuppliers)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence)"""
        super(_AbstractLogger, self).log(level, message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).warn(marker, message, params)

    @override
    @overload
    def info(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String)"""
        super(_AbstractLogger, self).info(message)

    @override
    @overload
    def warn(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'CharSequence', t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).warn(marker, message, paramSuppliers)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def info(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).info(message)

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).log(level, messageSupplier)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3)

    @override
    @overload
    def fatal(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0)

    @override
    @overload
    def debug(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).debug(message, paramSuppliers)

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def entry(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry()"""
        super(AbstractLogger, self).entry()

    @override
    @overload
    def debug(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def error(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).error(message, params)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def warn(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).warn(message, paramSuppliers)

    @override
    @overload
    def warn(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence)"""
        super(_AbstractLogger, self).warn(message)

    @override
    @overload
    def atWarn(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atWarn()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atWarn())

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).fatal(marker, message, paramSuppliers)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def error(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).logMessage(level, marker, fqcn, location, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3))

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def atError(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atError()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atError())

    @overload
    def isEnabled(self, level: 'Level') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level)"""
        return bool._wrap(super(_AbstractLogger, self).isEnabled(level))

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, paramSuppliers)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).debug(marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def error(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).error(message, paramSuppliers)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6))

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).info(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def log(self, level: 'Level', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5))

    @override
    @overload
    def getLevel(self) -> 'log4py.Level':
        """public org.apache.logging.log4j.Level org.apache.logging.log4j.spi.ExtendedLoggerWrapper.getLevel()"""
        return 'log4py.Level'._wrap(super(ExtendedLoggerWrapper, self).getLevel())

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).error(marker, message, paramSuppliers)

    @override
    @overload
    def fatal(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isTraceEnabled())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).trace(marker, message, params)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object)"""
        super(_AbstractLogger, self).trace(message)

    @override
    @overload
    def trace(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String)"""
        super(_AbstractLogger, self).trace(message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def traceExit(self, message: 'EntryMessage', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage,R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(message, result))

    @override
    @overload
    def debug(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0)

    @override
    @overload
    def warn(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).warn(message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def error(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1))

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def warn(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).fatal(marker, message, params)

    @overload
    def atLevel(self, level: 'Level') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atLevel(org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'._wrap(super(_AbstractLogger, self).atLevel(level))

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def trace(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).trace(message, paramSuppliers)

    @override
    @overload
    def debug(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def getMessageFactory(self) -> 'message.MessageFactory':
        """public <MF extends org.apache.logging.log4j.message.MessageFactory> MF org.apache.logging.log4j.spi.AbstractLogger.getMessageFactory()"""
        return 'message.MessageFactory'._wrap(super(AbstractLogger, self).getMessageFactory())

    @override
    @overload
    def exit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.exit()"""
        super(AbstractLogger, self).exit()

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0)

    @override
    @overload
    def atInfo(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atInfo()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atInfo())

    @override
    @overload
    def atFatal(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atFatal()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atFatal())

    @overload
    def exit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.exit(R)"""
        return object._wrap(super(_AbstractLogger, self).exit(result))

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).error(marker, message, params)

    @overload
    def throwing(self, throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(T)"""
        return 'Throwable'._wrap(super(_AbstractLogger, self).throwing(throwable))

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0)

    @override
    @overload
    def log(self, level: 'Level', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).log(level, message, paramSuppliers)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def error(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def error(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def error(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message)

    @override
    @overload
    def atTrace(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atTrace()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atTrace())

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def info(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object)"""
        super(_AbstractLogger, self).info(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def traceEntry(self, message: 'Message') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.message.Message)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(message))

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def traceExit(self, message: 'Message', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.Message,R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(message, result))

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @overload
    def traceExit(self, format: str, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(java.lang.String,R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(format, result))

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).trace(marker, message, paramSuppliers)

    @overload
    def traceEntry(self, format: str, *params: object) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,java.lang.Object...)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(format, params))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, p0, p1, p2, p3, p4))

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message)

    @staticmethod
    @overload
    def checkMessageFactory(logger: 'ExtendedLogger', messageFactory: 'MessageFactory'):
        """public static void org.apache.logging.log4j.spi.AbstractLogger.checkMessageFactory(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.message.MessageFactory)"""
        _AbstractLogger.checkMessageFactory(logger, messageFactory)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def fatal(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0)

    @override
    @overload
    def entry(self, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry(java.lang.Object...)"""
        super(_AbstractLogger, self).entry(params)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).info(marker, message)

    @override
    @overload
    def log(self, level: 'Level', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def traceExit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit()"""
        super(AbstractLogger, self).traceExit()

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, t: 'Throwable') -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, t))

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, level: 'Level', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).debug(marker, message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2)

    @override
    @overload
    def warn(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object)"""
        super(_AbstractLogger, self).warn(message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isEnabled(level, marker))

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, *params: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.ExtendedLoggerWrapper.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        return bool._wrap(super(_ExtendedLoggerWrapper, self).isEnabled(level, marker, message, params))

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def debug(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).trace(message, params)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def fatal(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def getFlowMessageFactory(self) -> 'message.FlowMessageFactory':
        """public org.apache.logging.log4j.message.FlowMessageFactory org.apache.logging.log4j.spi.AbstractLogger.getFlowMessageFactory()"""
        return 'message.FlowMessageFactory'._wrap(super(AbstractLogger, self).getFlowMessageFactory())

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1)

    @overload
    def isErrorEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isErrorEnabled(marker))

    @override
    @overload
    def always(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.always()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).always())

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isDebugEnabled())

    @override
    @overload
    def error(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def catching(self, level: 'Level', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(org.apache.logging.log4j.Level,java.lang.Throwable)"""
        super(_AbstractLogger, self).catching(level, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def fatal(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).fatal(message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isWarnEnabled())

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2)

    @override
    @overload
    def traceExit(self, message: 'EntryMessage'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage)"""
        super(_AbstractLogger, self).traceExit(message)

    @override
    @overload
    def trace(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence)"""
        super(_AbstractLogger, self).trace(message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1)

 
 
 
# CLASS: org.apache.logging.log4j.spi.ExtendedLoggerWrapper 
 
 
# CLASS: org.apache.logging.log4j.spi.LocationAwareLogger
from pyquantum_helper import import_once as _import_once
try:
    import log4py
except ImportError:
    log4py = _import_once("log4py")

import java.lang.Throwable as Throwable
try:
    from log4py import message
except ImportError:
    message = _import_once("log4py.message")

from abc import abstractmethod, ABC
import java.lang.StackTraceElement as StackTraceElement
import org.apache.logging.log4j.spi.LocationAwareLogger as _LocationAwareLogger
_LocationAwareLogger = _LocationAwareLogger
 
class LocationAwareLogger():
    """org.apache.logging.log4j.spi.LocationAwareLogger"""
 
    @staticmethod
    def _wrap(java_value: _LocationAwareLogger) -> 'LocationAwareLogger':
        return LocationAwareLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LocationAwareLogger):
        """
        Dynamic initializer for LocationAwareLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LocationAwareLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LocationAwareLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.LocationAwareLogger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.StandardLevel
from builtins import str
import org.apache.logging.log4j.spi.StandardLevel as _StandardLevel
_StandardLevel = _StandardLevel
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StandardLevel():
    """org.apache.logging.log4j.spi.StandardLevel"""
 
    @staticmethod
    def _wrap(java_value: _StandardLevel) -> 'StandardLevel':
        return StandardLevel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StandardLevel):
        """
        Dynamic initializer for StandardLevel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StandardLevel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StandardLevel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def valueOf(name: str) -> 'StandardLevel':
        """public static org.apache.logging.log4j.spi.StandardLevel org.apache.logging.log4j.spi.StandardLevel.valueOf(java.lang.String)"""
        return StandardLevel._wrap(_StandardLevel.valueOf(name))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def getStandardLevel(intLevel: int) -> 'StandardLevel':
        """public static org.apache.logging.log4j.spi.StandardLevel org.apache.logging.log4j.spi.StandardLevel.getStandardLevel(int)"""
        return StandardLevel._wrap(_StandardLevel.getStandardLevel(_int.valueOf(intLevel)))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @overload
    def intLevel(self) -> int:
        """public int org.apache.logging.log4j.spi.StandardLevel.intLevel()"""
        return int._wrap(super(StandardLevel, self).intLevel())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['StandardLevel']:
        """public static org.apache.logging.log4j.spi.StandardLevel[] org.apache.logging.log4j.spi.StandardLevel.values()"""
        return List[StandardLevel]._wrap(_StandardLevel.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.logging.log4j.spi.LoggerRegistry as _LoggerRegistry_ConcurrentMapFactory
_ConcurrentMapFactory = _LoggerRegistry_ConcurrentMapFactory.ConcurrentMapFactory
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConcurrentMapFactory():
    """org.apache.logging.log4j.spi.LoggerRegistry.ConcurrentMapFactory"""
 
    @staticmethod
    def _wrap(java_value: _ConcurrentMapFactory) -> 'ConcurrentMapFactory':
        return ConcurrentMapFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConcurrentMapFactory):
        """
        Dynamic initializer for ConcurrentMapFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConcurrentMapFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConcurrentMapFactory__wrapper":
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
    def createOuterMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.util.Map<java.lang.String, T>> org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory.createOuterMap()"""
        return 'Map'._wrap(super(ConcurrentMapFactory, self).createOuterMap())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def createInnerMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, T> org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory.createInnerMap()"""
        return 'Map'._wrap(super(ConcurrentMapFactory, self).createInnerMap())

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory()"""
        val = _ConcurrentMapFactory()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory()"""
        val = _ConcurrentMapFactory()
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

    @override
    @overload
    def putIfAbsent(self, innerMap: 'Map', name: str, logger: 'ExtendedLogger'):
        """public void org.apache.logging.log4j.spi.LoggerRegistry$ConcurrentMapFactory.putIfAbsent(java.util.Map<java.lang.String, T>,java.lang.String,T)"""
        super(_ConcurrentMapFactory, self).putIfAbsent(innerMap, name, logger)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.spi.AbstractLogger
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.logging.log4j.message.MessageFactory as _MessageFactory
_MessageFactory = _MessageFactory
from abc import abstractmethod, ABC
import java.lang.String as _string
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
import org.apache.logging.log4j.spi.ExtendedLogger as _ExtendedLogger
_ExtendedLogger = _ExtendedLogger
import org.apache.logging.log4j.spi.AbstractLogger as _AbstractLogger
_AbstractLogger = _AbstractLogger
import java.lang.String as _String
_String = _String
from builtins import object
try:
    from log4py import message
except ImportError:
    message = _import_once("log4py.message")

import java.lang.StackTraceElement as StackTraceElement
import java.lang.Integer as _int
import org.apache.logging.log4j.Logger as _Logger
_Logger = _Logger
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
 
class AbstractLogger():
    """org.apache.logging.log4j.spi.AbstractLogger"""
 
    @staticmethod
    def _wrap(java_value: _AbstractLogger) -> 'AbstractLogger':
        return AbstractLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractLogger):
        """
        Dynamic initializer for AbstractLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @overload
    def isTraceEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isTraceEnabled(marker))

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1)

    @override
    @overload
    def atDebug(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atDebug()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atDebug())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.AbstractLogger.getName()"""
        return str._wrap(super(AbstractLogger, self).getName())

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def info(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).info(message, params)

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isInfoEnabled())

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @overload
    def throwing(self, level: 'Level', throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(org.apache.logging.log4j.Level,T)"""
        return 'Throwable'._wrap(super(_AbstractLogger, self).throwing(level, throwable))

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).log(level, marker, message, params)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def trace(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def error(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def info(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2)

    @override
    @overload
    def trace(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def info(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).info(marker, message, paramSuppliers)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def printf(self, level: 'Level', marker: 'Marker', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).printf(level, marker, format, params)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def fatal(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).fatal(message, params)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).trace(message)

    @overload
    def isDebugEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isDebugEnabled(marker))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @abstractmethod
    def logMessage(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logMessage(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @overload
    def isFatalEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isFatalEnabled(marker))

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def error(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(messageSupplier, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @staticmethod
    @overload
    def getRecursionDepth() -> int:
        """public static int org.apache.logging.log4j.spi.AbstractLogger.getRecursionDepth()"""
        return int._wrap(_AbstractLogger.getRecursionDepth())

    @override
    @overload
    def debug(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def warn(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).warn(message, params)

    @overload
    def traceExit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(result))

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def info(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).info(marker, message)

    @override
    @overload
    def fatal(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def fatal(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isErrorEnabled())

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0)

    @override
    @overload
    def info(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).info(message, paramSuppliers)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def log(self, level: 'Level', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def warn(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String)"""
        super(_AbstractLogger, self).warn(message)

    @override
    @overload
    def catching(self, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(java.lang.Throwable)"""
        super(_AbstractLogger, self).catching(throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def error(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def log(self, level: 'Level', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).log(level, message, params)

    @overload
    def isWarnEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isWarnEnabled(marker))

    @override
    @overload
    def trace(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).fatal(messageSupplier)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @override
    @overload
    def info(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def printf(self, level: 'Level', format: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.printf(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).printf(level, format, params)

    @override
    @overload
    def info(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, message, throwable)

    @override
    @overload
    def debug(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.Object)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def info(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.CharSequence)"""
        super(_AbstractLogger, self).info(message)

    @overload
    def isInfoEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isInfoEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isInfoEnabled(marker))

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1)

    @override
    @overload
    def trace(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message)

    @overload
    def traceEntry(self, format: str, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(format, paramSuppliers))

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def debug(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def isFatalEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isFatalEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isFatalEnabled())

    @override
    @overload
    def trace(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).debug(message, params)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).log(level, message)

    @overload
    def traceEntry(self, *paramSuppliers: 'util.Supplier') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.util.Supplier<?>...)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(paramSuppliers))

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1)

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).fatal(messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, messageSupplier, throwable)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def traceEntry(self) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry()"""
        return 'message.EntryMessage'._wrap(super(AbstractLogger, self).traceEntry())

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).info(marker, message, params)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def log(self, level: 'Level', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String)"""
        super(_AbstractLogger, self).log(level, message)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2)

    @override
    @overload
    def error(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).log(level, marker, message, paramSuppliers)

    @override
    @overload
    def trace(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence)"""
        super(_AbstractLogger, self).log(level, message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).warn(marker, message, params)

    @override
    @overload
    def info(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String)"""
        super(_AbstractLogger, self).info(message)

    @override
    @overload
    def warn(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).warn(marker, message, paramSuppliers)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def warn(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def info(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).info(message)

    @override
    @overload
    def fatal(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @override
    @overload
    def log(self, level: 'Level', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).log(level, messageSupplier)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3)

    @override
    @overload
    def fatal(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0)

    @override
    @overload
    def debug(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).debug(message, paramSuppliers)

    @override
    @overload
    def info(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).info(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: object, t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def warn(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def entry(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry()"""
        super(AbstractLogger, self).entry()

    @override
    @overload
    def debug(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def error(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).error(message, params)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def warn(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).warn(message, paramSuppliers)

    @override
    @overload
    def warn(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.CharSequence)"""
        super(_AbstractLogger, self).warn(message)

    @override
    @overload
    def atWarn(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atWarn()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atWarn())

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).fatal(marker, message, paramSuppliers)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def error(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).logMessage(level, marker, fqcn, location, message, throwable)

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.AbstractLogger()"""
        val = _AbstractLogger()
        self.__wrapper = val

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def trace(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def info(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(messageSupplier, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, message, throwable)

    @overload
    def __init__(self, name: str, messageFactory: 'MessageFactory'):
        """public org.apache.logging.log4j.spi.AbstractLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        val = _AbstractLogger(name, messageFactory)
        self.__wrapper = val

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def atError(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atError()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atError())

    @overload
    def isEnabled(self, level: 'Level') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level)"""
        return bool._wrap(super(_AbstractLogger, self).isEnabled(level))

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def info(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def trace(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).trace(messageSupplier)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def warn(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier, throwable)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, paramSuppliers)

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).trace(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).log(level, marker, messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).debug(marker, message, params)

    @override
    @overload
    def log(self, level: 'Level', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def error(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def error(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).error(message, paramSuppliers)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).info(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def log(self, level: 'Level', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(message, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).error(marker, message, paramSuppliers)

    @override
    @overload
    def fatal(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(message, throwable)

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isTraceEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isTraceEnabled())

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).trace(marker, message, params)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1)

    @override
    @overload
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, messageSupplier, throwable)

    @override
    @overload
    def trace(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.Object)"""
        super(_AbstractLogger, self).trace(message)

    @override
    @overload
    def trace(self, message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String)"""
        super(_AbstractLogger, self).trace(message)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def traceExit(self, message: 'EntryMessage', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage,R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(message, result))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.AbstractLogger()"""
        val = _AbstractLogger()
        self.__wrapper = val

    @override
    @overload
    def debug(self, message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def info(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0)

    @override
    @overload
    def warn(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).warn(message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1)

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(messageSupplier, throwable)

    @override
    @overload
    def error(self, message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def warn(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).info(marker, messageSupplier)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).fatal(marker, message, params)

    @overload
    def atLevel(self, level: 'Level') -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atLevel(org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'._wrap(super(_AbstractLogger, self).atLevel(level))

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def fatal(self, message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def trace(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).trace(message, paramSuppliers)

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @override
    @overload
    def debug(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(marker, message, throwable)

    @override
    @overload
    def getMessageFactory(self) -> 'message.MessageFactory':
        """public <MF extends org.apache.logging.log4j.message.MessageFactory> MF org.apache.logging.log4j.spi.AbstractLogger.getMessageFactory()"""
        return 'message.MessageFactory'._wrap(super(AbstractLogger, self).getMessageFactory())

    @override
    @overload
    def exit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.exit()"""
        super(AbstractLogger, self).exit()

    @override
    @overload
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, messageSupplier, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0)

    @override
    @overload
    def atInfo(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atInfo()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atInfo())

    @override
    @overload
    def atFatal(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atFatal()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atFatal())

    @overload
    def exit(self, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.exit(R)"""
        return object._wrap(super(_AbstractLogger, self).exit(result))

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).warn(messageSupplier)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).error(marker, message, params)

    @overload
    def throwing(self, throwable: 'Throwable') -> 'Throwable':
        """public <T extends java.lang.Throwable> T org.apache.logging.log4j.spi.AbstractLogger.throwing(T)"""
        return 'Throwable'._wrap(super(_AbstractLogger, self).throwing(throwable))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0)

    @override
    @overload
    def log(self, level: 'Level', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).log(level, message, paramSuppliers)

    @override
    @overload
    def debug(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def error(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.CharSequence)"""
        super(_AbstractLogger, self).error(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def error(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(messageSupplier, throwable)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier)

    @override
    @overload
    def error(self, messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).error(messageSupplier)

    @override
    @overload
    def trace(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(message, p0, p1, p2)

    @override
    @overload
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).info(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message)

    @override
    @overload
    def atTrace(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.atTrace()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).atTrace())

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1)

    @override
    @overload
    def debug(self, messageSupplier: 'MessageSupplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.util.MessageSupplier)"""
        super(_AbstractLogger, self).debug(messageSupplier)

    @override
    @overload
    def info(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.Object)"""
        super(_AbstractLogger, self).info(message)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).log(level, marker, message)

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, marker, message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def traceEntry(self, message: 'Message') -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(org.apache.logging.log4j.message.Message)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(message))

    @override
    @overload
    def error(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @overload
    def traceExit(self, message: 'Message', result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.Message,R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(message, result))

    @override
    @overload
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, messageSupplier, throwable)

    @overload
    def traceExit(self, format: str, result: object) -> object:
        """public <R> R org.apache.logging.log4j.spi.AbstractLogger.traceExit(java.lang.String,R)"""
        return object._wrap(super(_AbstractLogger, self).traceExit(format, result))

    @override
    @overload
    def error(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).error(marker, messageSupplier)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).trace(marker, message, paramSuppliers)

    @overload
    def traceEntry(self, format: str, *params: object) -> 'message.EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.spi.AbstractLogger.traceEntry(java.lang.String,java.lang.Object...)"""
        return 'message.EntryMessage'._wrap(super(_AbstractLogger, self).traceEntry(format, params))

    @override
    @overload
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).warn(marker, message)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def fatal(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        super(_AbstractLogger, self).fatal(messageSupplier, throwable)

    @override
    @overload
    def warn(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message)

    @staticmethod
    @overload
    def checkMessageFactory(logger: 'ExtendedLogger', messageFactory: 'MessageFactory'):
        """public static void org.apache.logging.log4j.spi.AbstractLogger.checkMessageFactory(org.apache.logging.log4j.spi.ExtendedLogger,org.apache.logging.log4j.message.MessageFactory)"""
        _AbstractLogger.checkMessageFactory(logger, messageFactory)

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def fatal(self, message: str, p0: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0)

    @override
    @overload
    def entry(self, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.entry(java.lang.Object...)"""
        super(_AbstractLogger, self).entry(params)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(marker, messageSupplier, throwable)

    @override
    @overload
    def debug(self, message: 'CharSequence', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def info(self, marker: 'Marker', message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        super(_AbstractLogger, self).info(marker, message)

    @override
    @overload
    def log(self, level: 'Level', message: object, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object,java.lang.Throwable)"""
        super(_AbstractLogger, self).log(level, message, throwable)

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def debug(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).debug(message, throwable)

    @override
    @overload
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2)

    @override
    @overload
    def warn(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(marker, message, throwable)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3, p4, p5)

    @override
    @overload
    def traceExit(self):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit()"""
        super(AbstractLogger, self).traceExit()

    @override
    @overload
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).warn(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @overload
    def __init__(self, name: str):
        """public org.apache.logging.log4j.spi.AbstractLogger(java.lang.String)"""
        val = _AbstractLogger(name)
        self.__wrapper = val

    @override
    @overload
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(message, p0, p1, p2, p3, p4)

    @override
    @overload
    def log(self, level: 'Level', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.log(org.apache.logging.log4j.Level,java.lang.Object)"""
        super(_AbstractLogger, self).log(level, message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).debug(marker, message, paramSuppliers)

    @abstractmethod
    def getLevel(self, ):
        """public abstract org.apache.logging.log4j.Level org.apache.logging.log4j.Logger.getLevel()"""
        pass

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2)

    @override
    @overload
    def warn(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(java.lang.Object)"""
        super(_AbstractLogger, self).warn(message)

    @overload
    def isEnabled(self, level: 'Level', marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isEnabled(level, marker))

    @override
    @overload
    def trace(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).trace(marker, message, throwable)

    @override
    @overload
    def debug(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(java.lang.CharSequence)"""
        super(_AbstractLogger, self).debug(message)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def error(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(marker, message, throwable)

    @override
    @overload
    def trace(self, message: str, *params: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(_AbstractLogger, self).trace(message, params)

    @override
    @overload
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        super(_AbstractLogger, self).warn(marker, messageSupplier)

    @override
    @overload
    def error(self, marker: 'Marker', message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message)

    @override
    @overload
    def fatal(self, message: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message)

    @override
    @overload
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).debug(marker, message, p0, p1, p2, p3, p4, p5, p6, p7)

    @override
    @overload
    def getFlowMessageFactory(self) -> 'message.FlowMessageFactory':
        """public org.apache.logging.log4j.message.FlowMessageFactory org.apache.logging.log4j.spi.AbstractLogger.getFlowMessageFactory()"""
        return 'message.FlowMessageFactory'._wrap(super(AbstractLogger, self).getFlowMessageFactory())

    @override
    @overload
    def debug(self, marker: 'Marker', message: 'Message'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        super(_AbstractLogger, self).debug(marker, message)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1)

    @overload
    def isErrorEnabled(self, marker: 'Marker') -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isErrorEnabled(org.apache.logging.log4j.Marker)"""
        return bool._wrap(super(_AbstractLogger, self).isErrorEnabled(marker))

    @override
    @overload
    def always(self) -> 'log4py.LogBuilder':
        """public org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.spi.AbstractLogger.always()"""
        return 'log4py.LogBuilder'._wrap(super(AbstractLogger, self).always())

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isDebugEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isDebugEnabled())

    @override
    @overload
    def error(self, message: str, throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_AbstractLogger, self).error(message, throwable)

    @override
    @overload
    def catching(self, level: 'Level', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.catching(org.apache.logging.log4j.Level,java.lang.Throwable)"""
        super(_AbstractLogger, self).catching(level, throwable)

    @override
    @overload
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def fatal(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        super(_AbstractLogger, self).fatal(message, paramSuppliers)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.AbstractLogger.isWarnEnabled()"""
        return bool._wrap(super(AbstractLogger, self).isWarnEnabled())

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'CharSequence', t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1, p2, p3, p4)

    @override
    @overload
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).info(message, p0, p1, p2, p3)

    @override
    @overload
    def fatal(self, message: str, p0: object, p1: object, p2: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).fatal(message, p0, p1, p2)

    @override
    @overload
    def traceExit(self, message: 'EntryMessage'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.traceExit(org.apache.logging.log4j.message.EntryMessage)"""
        super(_AbstractLogger, self).traceExit(message)

    @override
    @overload
    def trace(self, message: 'CharSequence'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(java.lang.CharSequence)"""
        super(_AbstractLogger, self).trace(message)

    @override
    @overload
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).trace(marker, message, p0, p1, p2, p3, p4, p5, p6)

    @override
    @overload
    def warn(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public void org.apache.logging.log4j.spi.AbstractLogger.warn(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        super(_AbstractLogger, self).warn(messageSupplier, throwable)

    @override
    @overload
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).error(marker, message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    @override
    @overload
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public void org.apache.logging.log4j.spi.AbstractLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_AbstractLogger, self).logIfEnabled(fqcn, level, marker, message, p0, p1) 
 
 
# CLASS: org.apache.logging.log4j.spi.CleanableThreadContextMap
import org.apache.logging.log4j.spi.ThreadContextMap as _ThreadContextMap
_ThreadContextMap = _ThreadContextMap
import org.apache.logging.log4j.spi.CleanableThreadContextMap as _CleanableThreadContextMap
_CleanableThreadContextMap = _CleanableThreadContextMap
import java.lang.Iterable as Iterable
import org.apache.logging.log4j.spi.ThreadContextMap2 as _ThreadContextMap2
_ThreadContextMap2 = _ThreadContextMap2
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class CleanableThreadContextMap():
    """org.apache.logging.log4j.spi.CleanableThreadContextMap"""
 
    @staticmethod
    def _wrap(java_value: _CleanableThreadContextMap) -> 'CleanableThreadContextMap':
        return CleanableThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CleanableThreadContextMap):
        """
        Dynamic initializer for CleanableThreadContextMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CleanableThreadContextMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CleanableThreadContextMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.isEmpty()"""
        pass

    @abstractmethod
    def getReadOnlyContextData(self, ):
        """public abstract org.apache.logging.log4j.util.StringMap org.apache.logging.log4j.spi.ThreadContextMap2.getReadOnlyContextData()"""
        pass

    @abstractmethod
    def getCopy(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getCopy()"""
        pass

    @abstractmethod
    def getImmutableMapOrNull(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getImmutableMapOrNull()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.clear()"""
        pass

    @abstractmethod
    def putAll(self, map: 'Map'):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap2.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        pass

    @abstractmethod
    def get(self, key: str):
        """public abstract java.lang.String org.apache.logging.log4j.spi.ThreadContextMap.get(java.lang.String)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def removeAll(self, keys: 'Iterable'):
        """public abstract void org.apache.logging.log4j.spi.CleanableThreadContextMap.removeAll(java.lang.Iterable<java.lang.String>)"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def put(self, key: str, value: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.put(java.lang.String,java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerContext
from pyquantum_helper import import_once as _import_once
import java.lang.String as _string
import org.apache.logging.log4j.spi.LoggerContext as _LoggerContext
_LoggerContext = _LoggerContext
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import org.apache.logging.log4j.spi.ExtendedLogger as _ExtendedLogger
_ExtendedLogger = _ExtendedLogger
try:
    from log4py import message
except ImportError:
    message = _import_once("log4py.message")

from abc import abstractmethod, ABC
from builtins import object
from builtins import bool
import org.apache.logging.log4j.spi.LoggerRegistry as _LoggerRegistry
_LoggerRegistry = _LoggerRegistry
 
class LoggerContext():
    """org.apache.logging.log4j.spi.LoggerContext"""
 
    @staticmethod
    def _wrap(java_value: _LoggerContext) -> 'LoggerContext':
        return LoggerContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoggerContext):
        """
        Dynamic initializer for LoggerContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoggerContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoggerContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def removeObject(self, key: str) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.removeObject(java.lang.String)"""
        return object._wrap(super(_LoggerContext, self).removeObject(key))

    @abstractmethod
    def getLogger(self, name: str):
        """public abstract org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.spi.LoggerContext.getLogger(java.lang.String)"""
        pass

    @abstractmethod
    def hasLogger(self, name: str):
        """public abstract boolean org.apache.logging.log4j.spi.LoggerContext.hasLogger(java.lang.String)"""
        pass

    @overload
    def putObjectIfAbsent(self, key: str, value: object) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.putObjectIfAbsent(java.lang.String,java.lang.Object)"""
        return object._wrap(super(_LoggerContext, self).putObjectIfAbsent(key, value))

    @overload
    def getObject(self, key: str) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.getObject(java.lang.String)"""
        return object._wrap(super(_LoggerContext, self).getObject(key))

    @abstractmethod
    def hasLogger(self, name: str, messageFactoryClass: 'Class'):
        """public abstract boolean org.apache.logging.log4j.spi.LoggerContext.hasLogger(java.lang.String,java.lang.Class<? extends org.apache.logging.log4j.message.MessageFactory>)"""
        pass

    @abstractmethod
    def hasLogger(self, name: str, messageFactory: 'MessageFactory'):
        """public abstract boolean org.apache.logging.log4j.spi.LoggerContext.hasLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        pass

    @overload
    def removeObject(self, key: str, value: object) -> bool:
        """public default boolean org.apache.logging.log4j.spi.LoggerContext.removeObject(java.lang.String,java.lang.Object)"""
        return bool._wrap(super(_LoggerContext, self).removeObject(key, value))

    @overload
    def getLogger(self, cls: 'Class') -> 'ExtendedLogger':
        """public default org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.spi.LoggerContext.getLogger(java.lang.Class<?>)"""
        return 'ExtendedLogger'._wrap(super(_LoggerContext, self).getLogger(cls))

    @overload
    def getLoggerRegistry(self) -> 'LoggerRegistry':
        """public default org.apache.logging.log4j.spi.LoggerRegistry<? extends org.apache.logging.log4j.Logger> org.apache.logging.log4j.spi.LoggerContext.getLoggerRegistry()"""
        return 'LoggerRegistry'._wrap(super(LoggerContext, self).getLoggerRegistry())

    @overload
    def getLogger(self, cls: 'Class', messageFactory: 'MessageFactory') -> 'ExtendedLogger':
        """public default org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.spi.LoggerContext.getLogger(java.lang.Class<?>,org.apache.logging.log4j.message.MessageFactory)"""
        return 'ExtendedLogger'._wrap(super(_LoggerContext, self).getLogger(cls, messageFactory))

    @abstractmethod
    def getLogger(self, name: str, messageFactory: 'MessageFactory'):
        """public abstract org.apache.logging.log4j.spi.ExtendedLogger org.apache.logging.log4j.spi.LoggerContext.getLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        pass

    @abstractmethod
    def getExternalContext(self, ):
        """public abstract java.lang.Object org.apache.logging.log4j.spi.LoggerContext.getExternalContext()"""
        pass

    @overload
    def putObject(self, key: str, value: object) -> object:
        """public default java.lang.Object org.apache.logging.log4j.spi.LoggerContext.putObject(java.lang.String,java.lang.Object)"""
        return object._wrap(super(_LoggerContext, self).putObject(key, value)) 
 
 
# CLASS: org.apache.logging.log4j.spi.AbstractLoggerAdapter
from builtins import str
import java.util.concurrent.ConcurrentMap as _ConcurrentMap
_ConcurrentMap = _ConcurrentMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.ConcurrentMap as ConcurrentMap
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.util.Set as Set
import java.lang.Integer as _int
import org.apache.logging.log4j.spi.AbstractLoggerAdapter as _AbstractLoggerAdapter
_AbstractLoggerAdapter = _AbstractLoggerAdapter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractLoggerAdapter():
    """org.apache.logging.log4j.spi.AbstractLoggerAdapter"""
 
    @staticmethod
    def _wrap(java_value: _AbstractLoggerAdapter) -> 'AbstractLoggerAdapter':
        return AbstractLoggerAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractLoggerAdapter):
        """
        Dynamic initializer for AbstractLoggerAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractLoggerAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractLoggerAdapter__wrapper":
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

    @overload
    def getLogger(self, name: str) -> object:
        """public L org.apache.logging.log4j.spi.AbstractLoggerAdapter.getLogger(java.lang.String)"""
        return object._wrap(super(_AbstractLoggerAdapter, self).getLogger(name))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.AbstractLoggerAdapter()"""
        val = _AbstractLoggerAdapter()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def close(self):
        """public void org.apache.logging.log4j.spi.AbstractLoggerAdapter.close()"""
        super(AbstractLoggerAdapter, self).close()

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
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.AbstractLoggerAdapter()"""
        val = _AbstractLoggerAdapter()
        self.__wrapper = val

    @override
    @overload
    def contextShutdown(self, loggerContext: 'LoggerContext'):
        """public void org.apache.logging.log4j.spi.AbstractLoggerAdapter.contextShutdown(org.apache.logging.log4j.spi.LoggerContext)"""
        super(_AbstractLoggerAdapter, self).contextShutdown(loggerContext)

    @overload
    def getLoggerContexts(self) -> 'Set':
        """public java.util.Set<org.apache.logging.log4j.spi.LoggerContext> org.apache.logging.log4j.spi.AbstractLoggerAdapter.getLoggerContexts()"""
        return 'Set'._wrap(super(AbstractLoggerAdapter, self).getLoggerContexts())

    @overload
    def getLoggersInContext(self, context: 'LoggerContext') -> 'ConcurrentMap':
        """public java.util.concurrent.ConcurrentMap<java.lang.String, L> org.apache.logging.log4j.spi.AbstractLoggerAdapter.getLoggersInContext(org.apache.logging.log4j.spi.LoggerContext)"""
        return 'ConcurrentMap'._wrap(super(_AbstractLoggerAdapter, self).getLoggersInContext(context))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerContextKey
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
try:
    from log4py import message
except ImportError:
    message = _import_once("log4py.message")

import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import org.apache.logging.log4j.spi.LoggerContextKey as _LoggerContextKey
_LoggerContextKey = _LoggerContextKey
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoggerContextKey():
    """org.apache.logging.log4j.spi.LoggerContextKey"""
 
    @staticmethod
    def _wrap(java_value: _LoggerContextKey) -> 'LoggerContextKey':
        return LoggerContextKey(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoggerContextKey):
        """
        Dynamic initializer for LoggerContextKey.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoggerContextKey__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoggerContextKey__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(name: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.spi.LoggerContextKey.create(java.lang.String)"""
        return str._wrap(_LoggerContextKey.create(name))

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

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.LoggerContextKey()"""
        val = _LoggerContextKey()
        self.__wrapper = val

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.LoggerContextKey()"""
        val = _LoggerContextKey()
        self.__wrapper = val

    @staticmethod
    @overload
    def create(name: str, messageFactoryClass: 'Class') -> str:
        """public static java.lang.String org.apache.logging.log4j.spi.LoggerContextKey.create(java.lang.String,java.lang.Class<? extends org.apache.logging.log4j.message.MessageFactory>)"""
        return str._wrap(_LoggerContextKey.create(name, messageFactoryClass))

    @staticmethod
    @overload
    def create(name: str, messageFactory: 'MessageFactory') -> str:
        """public static java.lang.String org.apache.logging.log4j.spi.LoggerContextKey.create(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        return str._wrap(_LoggerContextKey.create(name, messageFactory))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.spi.Terminable
import org.apache.logging.log4j.spi.Terminable as _Terminable
_Terminable = _Terminable
from abc import abstractmethod, ABC
 
class Terminable():
    """org.apache.logging.log4j.spi.Terminable"""
 
    @staticmethod
    def _wrap(java_value: _Terminable) -> 'Terminable':
        return Terminable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Terminable):
        """
        Dynamic initializer for Terminable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Terminable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Terminable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def terminate(self, ):
        """public abstract void org.apache.logging.log4j.spi.Terminable.terminate()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.CopyOnWrite
import org.apache.logging.log4j.spi.CopyOnWrite as _CopyOnWrite
_CopyOnWrite = _CopyOnWrite
 
class CopyOnWrite():
    """org.apache.logging.log4j.spi.CopyOnWrite"""
 
    @staticmethod
    def _wrap(java_value: _CopyOnWrite) -> 'CopyOnWrite':
        return CopyOnWrite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CopyOnWrite):
        """
        Dynamic initializer for CopyOnWrite.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CopyOnWrite__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CopyOnWrite__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__)) 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerContextShutdownEnabled
import org.apache.logging.log4j.spi.LoggerContextShutdownEnabled as _LoggerContextShutdownEnabled
_LoggerContextShutdownEnabled = _LoggerContextShutdownEnabled
from abc import abstractmethod, ABC
 
class LoggerContextShutdownEnabled():
    """org.apache.logging.log4j.spi.LoggerContextShutdownEnabled"""
 
    @staticmethod
    def _wrap(java_value: _LoggerContextShutdownEnabled) -> 'LoggerContextShutdownEnabled':
        return LoggerContextShutdownEnabled(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoggerContextShutdownEnabled):
        """
        Dynamic initializer for LoggerContextShutdownEnabled.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoggerContextShutdownEnabled__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoggerContextShutdownEnabled__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getListeners(self, ):
        """public abstract java.util.List<org.apache.logging.log4j.spi.LoggerContextShutdownAware> org.apache.logging.log4j.spi.LoggerContextShutdownEnabled.getListeners()"""
        pass

    @abstractmethod
    def addShutdownListener(self, listener: 'LoggerContextShutdownAware'):
        """public abstract void org.apache.logging.log4j.spi.LoggerContextShutdownEnabled.addShutdownListener(org.apache.logging.log4j.spi.LoggerContextShutdownAware)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.MutableThreadContextStack
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
import org.apache.logging.log4j.spi.MutableThreadContextStack as _MutableThreadContextStack
_MutableThreadContextStack = _MutableThreadContextStack
from builtins import type
import org.apache.logging.log4j.ThreadContext as _ThreadContext_ContextStack
_ContextStack = _ThreadContext_ContextStack.ContextStack
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.util.Spliterator as Spliterator
try:
    import log4py
except ImportError:
    log4py = _import_once("log4py")

import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.logging.log4j.spi.ThreadContextStack as _ThreadContextStack
_ThreadContextStack = _ThreadContextStack
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.StringBuilder as StringBuilder
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class MutableThreadContextStack():
    """org.apache.logging.log4j.spi.MutableThreadContextStack"""
 
    @staticmethod
    def _wrap(java_value: _MutableThreadContextStack) -> 'MutableThreadContextStack':
        return MutableThreadContextStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableThreadContextStack):
        """
        Dynamic initializer for MutableThreadContextStack.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableThreadContextStack__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableThreadContextStack__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.spi.MutableThreadContextStack.clear()"""
        super(MutableThreadContextStack, self).clear()

    @override
    @overload
    def asList(self) -> 'List':
        """public java.util.List<java.lang.String> org.apache.logging.log4j.spi.MutableThreadContextStack.asList()"""
        return 'List'._wrap(super(MutableThreadContextStack, self).asList())

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.MutableThreadContextStack()"""
        val = _MutableThreadContextStack()
        self.__wrapper = val

    @overload
    def __init__(self, list: 'List'):
        """public org.apache.logging.log4j.spi.MutableThreadContextStack(java.util.List<java.lang.String>)"""
        val = _MutableThreadContextStack(list)
        self.__wrapper = val

    @overload
    def isFrozen(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.isFrozen()"""
        return bool._wrap(super(MutableThreadContextStack, self).isFrozen())

    @override
    @overload
    def push(self, message: str):
        """public void org.apache.logging.log4j.spi.MutableThreadContextStack.push(java.lang.String)"""
        super(_MutableThreadContextStack, self).push(message)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def retainAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_MutableThreadContextStack, self).retainAll(objects))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def contains(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.contains(java.lang.Object)"""
        return bool._wrap(super(_MutableThreadContextStack, self).contains(o))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def pop(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.MutableThreadContextStack.pop()"""
        return str._wrap(super(MutableThreadContextStack, self).pop())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.isEmpty()"""
        return bool._wrap(super(MutableThreadContextStack, self).isEmpty())

    @override
    @overload
    def trim(self, depth: int):
        """public void org.apache.logging.log4j.spi.MutableThreadContextStack.trim(int)"""
        super(_MutableThreadContextStack, self).trim(_int.valueOf(depth))

    @override
    @overload
    def getImmutableStackOrNull(self) -> 'log4py.ThreadContext$ContextStack':
        """public org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.spi.MutableThreadContextStack.getImmutableStackOrNull()"""
        return 'log4py.ThreadContext$ContextStack'._wrap(super(MutableThreadContextStack, self).getImmutableStackOrNull())

    @overload
    def add(self, s: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.add(java.lang.String)"""
        return bool._wrap(super(_MutableThreadContextStack, self).add(s))

    @override
    @overload
    def copy(self) -> 'ThreadContextStack':
        """public org.apache.logging.log4j.spi.ThreadContextStack org.apache.logging.log4j.spi.MutableThreadContextStack.copy()"""
        return 'ThreadContextStack'._wrap(super(MutableThreadContextStack, self).copy())

    @overload
    def freeze(self):
        """public void org.apache.logging.log4j.spi.MutableThreadContextStack.freeze()"""
        super(MutableThreadContextStack, self).freeze()

    @override
    @overload
    def getDepth(self) -> int:
        """public int org.apache.logging.log4j.spi.MutableThreadContextStack.getDepth()"""
        return int._wrap(super(MutableThreadContextStack, self).getDepth())

    @overload
    def containsAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_MutableThreadContextStack, self).containsAll(objects))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.spi.MutableThreadContextStack.toArray()"""
        return List[object]._wrap(super(MutableThreadContextStack, self).toArray())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.spi.MutableThreadContextStack.formatTo(java.lang.StringBuilder)"""
        super(_MutableThreadContextStack, self).formatTo(buffer)

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.equals(java.lang.Object)"""
        return bool._wrap(super(_MutableThreadContextStack, self).equals(obj))

    @overload
    def addAll(self, strings: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.addAll(java.util.Collection<? extends java.lang.String>)"""
        return bool._wrap(super(_MutableThreadContextStack, self).addAll(strings))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.MutableThreadContextStack()"""
        val = _MutableThreadContextStack()
        self.__wrapper = val

    @overload
    def remove(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.remove(java.lang.Object)"""
        return bool._wrap(super(_MutableThreadContextStack, self).remove(o))

    @overload
    def removeAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.MutableThreadContextStack.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_MutableThreadContextStack, self).removeAll(objects))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.spi.MutableThreadContextStack.hashCode()"""
        return int._wrap(super(MutableThreadContextStack, self).hashCode())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def peek(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.MutableThreadContextStack.peek()"""
        return str._wrap(super(MutableThreadContextStack, self).peek())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.lang.String> org.apache.logging.log4j.spi.MutableThreadContextStack.iterator()"""
        return 'Iterator'._wrap(super(MutableThreadContextStack, self).iterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.MutableThreadContextStack.toString()"""
        return str._wrap(super(MutableThreadContextStack, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.logging.log4j.spi.MutableThreadContextStack.size()"""
        return int._wrap(super(MutableThreadContextStack, self).size())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def toArray(self, ts: 'Object') -> List[object]:
        """public <T> T[] org.apache.logging.log4j.spi.MutableThreadContextStack.toArray(T[])"""
        return List[object]._wrap(super(_MutableThreadContextStack, self).toArray(ts)) 
 
 
# CLASS: org.apache.logging.log4j.spi.ReadOnlyThreadContextMap
import org.apache.logging.log4j.spi.ReadOnlyThreadContextMap as _ReadOnlyThreadContextMap
_ReadOnlyThreadContextMap = _ReadOnlyThreadContextMap
from abc import abstractmethod, ABC
 
class ReadOnlyThreadContextMap():
    """org.apache.logging.log4j.spi.ReadOnlyThreadContextMap"""
 
    @staticmethod
    def _wrap(java_value: _ReadOnlyThreadContextMap) -> 'ReadOnlyThreadContextMap':
        return ReadOnlyThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReadOnlyThreadContextMap):
        """
        Dynamic initializer for ReadOnlyThreadContextMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReadOnlyThreadContextMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReadOnlyThreadContextMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.isEmpty()"""
        pass

    @abstractmethod
    def getCopy(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.getCopy()"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def getReadOnlyContextData(self, ):
        """public abstract org.apache.logging.log4j.util.StringMap org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.getReadOnlyContextData()"""
        pass

    @abstractmethod
    def get(self, key: str):
        """public abstract java.lang.String org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.get(java.lang.String)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.clear()"""
        pass

    @abstractmethod
    def getImmutableMapOrNull(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ReadOnlyThreadContextMap.getImmutableMapOrNull()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.DefaultThreadContextMap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.String as _string
import org.apache.logging.log4j.spi.DefaultThreadContextMap as _DefaultThreadContextMap
_DefaultThreadContextMap = _DefaultThreadContextMap
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from log4py import util
except ImportError:
    util = _import_once("log4py.util")

from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultThreadContextMap():
    """org.apache.logging.log4j.spi.DefaultThreadContextMap"""
 
    @staticmethod
    def _wrap(java_value: _DefaultThreadContextMap) -> 'DefaultThreadContextMap':
        return DefaultThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultThreadContextMap):
        """
        Dynamic initializer for DefaultThreadContextMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultThreadContextMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultThreadContextMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, obj: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextMap.equals(java.lang.Object)"""
        return bool._wrap(super(_DefaultThreadContextMap, self).equals(obj))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.DefaultThreadContextMap()"""
        val = _DefaultThreadContextMap()
        self.__wrapper = val

    @override
    @overload
    def toMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.DefaultThreadContextMap.toMap()"""
        return 'Map'._wrap(super(DefaultThreadContextMap, self).toMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def removeAll(self, keys: 'Iterable'):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextMap.removeAll(java.lang.Iterable<java.lang.String>)"""
        super(_DefaultThreadContextMap, self).removeAll(keys)

    @override
    @overload
    def forEach(self, action: 'TriConsumer', state: object):
        """public <V,S> void org.apache.logging.log4j.spi.DefaultThreadContextMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, S>,S)"""
        super(_DefaultThreadContextMap, self).forEach(action, state)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.DefaultThreadContextMap.toString()"""
        return str._wrap(super(DefaultThreadContextMap, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public <V> void org.apache.logging.log4j.spi.DefaultThreadContextMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        super(_DefaultThreadContextMap, self).forEach(action)

    @overload
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextMap.containsKey(java.lang.String)"""
        return bool._wrap(super(_DefaultThreadContextMap, self).containsKey(key))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.DefaultThreadContextMap()"""
        val = _DefaultThreadContextMap()
        self.__wrapper = val

    @override
    @overload
    def getImmutableMapOrNull(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.DefaultThreadContextMap.getImmutableMapOrNull()"""
        return 'Map'._wrap(super(DefaultThreadContextMap, self).getImmutableMapOrNull())

    @overload
    def get(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.DefaultThreadContextMap.get(java.lang.String)"""
        return str._wrap(super(_DefaultThreadContextMap, self).get(key))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextMap.isEmpty()"""
        return bool._wrap(super(DefaultThreadContextMap, self).isEmpty())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def remove(self, key: str):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextMap.remove(java.lang.String)"""
        super(_DefaultThreadContextMap, self).remove(key)

    @overload
    def getValue(self, key: str) -> object:
        """public <V> V org.apache.logging.log4j.spi.DefaultThreadContextMap.getValue(java.lang.String)"""
        return object._wrap(super(_DefaultThreadContextMap, self).getValue(key))

    @override
    @overload
    def put(self, key: str, value: str):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextMap.put(java.lang.String,java.lang.String)"""
        super(_DefaultThreadContextMap, self).put(key, value)

    @overload
    def __init__(self, useMap: bool):
        """public org.apache.logging.log4j.spi.DefaultThreadContextMap(boolean)"""
        val = _DefaultThreadContextMap(_boolean.valueOf(useMap))
        self.__wrapper = val

    @overload
    def putAll(self, m: 'Map'):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextMap.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        super(_DefaultThreadContextMap, self).putAll(m)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.logging.log4j.spi.DefaultThreadContextMap.size()"""
        return int._wrap(super(DefaultThreadContextMap, self).size())

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextMap.clear()"""
        super(DefaultThreadContextMap, self).clear()

    @override
    @overload
    def getCopy(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.DefaultThreadContextMap.getCopy()"""
        return 'Map'._wrap(super(DefaultThreadContextMap, self).getCopy())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.spi.DefaultThreadContextMap.hashCode()"""
        return int._wrap(super(DefaultThreadContextMap, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.logging.log4j.spi.LoggerRegistry as _LoggerRegistry_WeakMapFactory
_WeakMapFactory = _LoggerRegistry_WeakMapFactory.WeakMapFactory
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WeakMapFactory():
    """org.apache.logging.log4j.spi.LoggerRegistry.WeakMapFactory"""
 
    @staticmethod
    def _wrap(java_value: _WeakMapFactory) -> 'WeakMapFactory':
        return WeakMapFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WeakMapFactory):
        """
        Dynamic initializer for WeakMapFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WeakMapFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WeakMapFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory()"""
        val = _WeakMapFactory()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory()"""
        val = _WeakMapFactory()
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

    @override
    @overload
    def putIfAbsent(self, innerMap: 'Map', name: str, logger: 'ExtendedLogger'):
        """public void org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory.putIfAbsent(java.util.Map<java.lang.String, T>,java.lang.String,T)"""
        super(_WeakMapFactory, self).putIfAbsent(innerMap, name, logger)

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
    def createInnerMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, T> org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory.createInnerMap()"""
        return 'Map'._wrap(super(WeakMapFactory, self).createInnerMap())

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

    @override
    @overload
    def createOuterMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.util.Map<java.lang.String, T>> org.apache.logging.log4j.spi.LoggerRegistry$WeakMapFactory.createOuterMap()"""
        return 'Map'._wrap(super(WeakMapFactory, self).createOuterMap())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerContextFactory
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.net.URI as URI
import java.lang.ClassLoader as ClassLoader
import org.apache.logging.log4j.spi.LoggerContextFactory as _LoggerContextFactory
_LoggerContextFactory = _LoggerContextFactory
from abc import abstractmethod, ABC
from builtins import bool
 
class LoggerContextFactory():
    """org.apache.logging.log4j.spi.LoggerContextFactory"""
 
    @staticmethod
    def _wrap(java_value: _LoggerContextFactory) -> 'LoggerContextFactory':
        return LoggerContextFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoggerContextFactory):
        """
        Dynamic initializer for LoggerContextFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoggerContextFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoggerContextFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getContext(self, fqcn: str, loader: 'ClassLoader', externalContext: object, currentContext: bool, configLocation: 'URI', name: str):
        """public abstract org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.spi.LoggerContextFactory.getContext(java.lang.String,java.lang.ClassLoader,java.lang.Object,boolean,java.net.URI,java.lang.String)"""
        pass

    @overload
    def hasContext(self, fqcn: str, loader: 'ClassLoader', currentContext: bool) -> bool:
        """public default boolean org.apache.logging.log4j.spi.LoggerContextFactory.hasContext(java.lang.String,java.lang.ClassLoader,boolean)"""
        return bool._wrap(super(_LoggerContextFactory, self).hasContext(fqcn, loader, _boolean.valueOf(currentContext)))

    @abstractmethod
    def removeContext(self, context: 'LoggerContext'):
        """public abstract void org.apache.logging.log4j.spi.LoggerContextFactory.removeContext(org.apache.logging.log4j.spi.LoggerContext)"""
        pass

    @abstractmethod
    def getContext(self, fqcn: str, loader: 'ClassLoader', externalContext: object, currentContext: bool):
        """public abstract org.apache.logging.log4j.spi.LoggerContext org.apache.logging.log4j.spi.LoggerContextFactory.getContext(java.lang.String,java.lang.ClassLoader,java.lang.Object,boolean)"""
        pass

    @overload
    def isClassLoaderDependent(self) -> bool:
        """public default boolean org.apache.logging.log4j.spi.LoggerContextFactory.isClassLoaderDependent()"""
        return bool._wrap(super(LoggerContextFactory, self).isClassLoaderDependent())

    @overload
    def shutdown(self, fqcn: str, loader: 'ClassLoader', currentContext: bool, allContexts: bool):
        """public default void org.apache.logging.log4j.spi.LoggerContextFactory.shutdown(java.lang.String,java.lang.ClassLoader,boolean,boolean)"""
        super(_LoggerContextFactory, self).shutdown(fqcn, loader, _boolean.valueOf(currentContext), _boolean.valueOf(allContexts)) 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerRegistry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import org.apache.logging.log4j.spi.ExtendedLogger as _ExtendedLogger
_ExtendedLogger = _ExtendedLogger
import java.util.Collection as Collection
try:
    from log4py import message
except ImportError:
    message = _import_once("log4py.message")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
from builtins import bool
import org.apache.logging.log4j.spi.LoggerRegistry as _LoggerRegistry
_LoggerRegistry = _LoggerRegistry
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoggerRegistry():
    """org.apache.logging.log4j.spi.LoggerRegistry"""
 
    @staticmethod
    def _wrap(java_value: _LoggerRegistry) -> 'LoggerRegistry':
        return LoggerRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoggerRegistry):
        """
        Dynamic initializer for LoggerRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoggerRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoggerRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def hasLogger(self, name: str, messageFactory: 'MessageFactory') -> bool:
        """public boolean org.apache.logging.log4j.spi.LoggerRegistry.hasLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        return bool._wrap(super(_LoggerRegistry, self).hasLogger(name, messageFactory))

    @overload
    def putIfAbsent(self, name: str, messageFactory: 'MessageFactory', logger: 'ExtendedLogger'):
        """public void org.apache.logging.log4j.spi.LoggerRegistry.putIfAbsent(java.lang.String,org.apache.logging.log4j.message.MessageFactory,T)"""
        super(_LoggerRegistry, self).putIfAbsent(name, messageFactory, logger)

    @overload
    def hasLogger(self, name: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.LoggerRegistry.hasLogger(java.lang.String)"""
        return bool._wrap(super(_LoggerRegistry, self).hasLogger(name))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.spi.LoggerRegistry()"""
        val = _LoggerRegistry()
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

    @overload
    def hasLogger(self, name: str, messageFactoryClass: 'Class') -> bool:
        """public boolean org.apache.logging.log4j.spi.LoggerRegistry.hasLogger(java.lang.String,java.lang.Class<? extends org.apache.logging.log4j.message.MessageFactory>)"""
        return bool._wrap(super(_LoggerRegistry, self).hasLogger(name, messageFactoryClass))

    @overload
    def getLoggers(self, destination: 'Collection') -> 'Collection':
        """public java.util.Collection<T> org.apache.logging.log4j.spi.LoggerRegistry.getLoggers(java.util.Collection<T>)"""
        return 'Collection'._wrap(super(_LoggerRegistry, self).getLoggers(destination))

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
    def getLoggers(self) -> 'Collection':
        """public java.util.Collection<T> org.apache.logging.log4j.spi.LoggerRegistry.getLoggers()"""
        return 'Collection'._wrap(super(LoggerRegistry, self).getLoggers())

    @overload
    def __init__(self, factory: 'MapFactory'):
        """public org.apache.logging.log4j.spi.LoggerRegistry(org.apache.logging.log4j.spi.LoggerRegistry$MapFactory<T>)"""
        val = _LoggerRegistry(factory)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getLogger(self, name: str) -> 'ExtendedLogger':
        """public T org.apache.logging.log4j.spi.LoggerRegistry.getLogger(java.lang.String)"""
        return 'ExtendedLogger'._wrap(super(_LoggerRegistry, self).getLogger(name))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getLogger(self, name: str, messageFactory: 'MessageFactory') -> 'ExtendedLogger':
        """public T org.apache.logging.log4j.spi.LoggerRegistry.getLogger(java.lang.String,org.apache.logging.log4j.message.MessageFactory)"""
        return 'ExtendedLogger'._wrap(super(_LoggerRegistry, self).getLogger(name, messageFactory))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.LoggerRegistry()"""
        val = _LoggerRegistry()
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
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerRegistry$MapFactory
from abc import abstractmethod, ABC
import java.util.Map as Map
import org.apache.logging.log4j.spi.LoggerRegistry as _LoggerRegistry_MapFactory
_MapFactory = _LoggerRegistry_MapFactory.MapFactory
 
class MapFactory():
    """org.apache.logging.log4j.spi.LoggerRegistry.MapFactory"""
 
    @staticmethod
    def _wrap(java_value: _MapFactory) -> 'MapFactory':
        return MapFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapFactory):
        """
        Dynamic initializer for MapFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def createOuterMap(self, ):
        """public abstract java.util.Map<java.lang.String, java.util.Map<java.lang.String, T>> org.apache.logging.log4j.spi.LoggerRegistry$MapFactory.createOuterMap()"""
        pass

    @abstractmethod
    def createInnerMap(self, ):
        """public abstract java.util.Map<java.lang.String, T> org.apache.logging.log4j.spi.LoggerRegistry$MapFactory.createInnerMap()"""
        pass

    @abstractmethod
    def putIfAbsent(self, innerMap: 'Map', name: str, logger: 'ExtendedLogger'):
        """public abstract void org.apache.logging.log4j.spi.LoggerRegistry$MapFactory.putIfAbsent(java.util.Map<java.lang.String, T>,java.lang.String,T)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.ObjectThreadContextMap
import org.apache.logging.log4j.spi.ThreadContextMap as _ThreadContextMap
_ThreadContextMap = _ThreadContextMap
import org.apache.logging.log4j.spi.ObjectThreadContextMap as _ObjectThreadContextMap
_ObjectThreadContextMap = _ObjectThreadContextMap
import java.lang.Iterable as Iterable
import org.apache.logging.log4j.spi.CleanableThreadContextMap as _CleanableThreadContextMap
_CleanableThreadContextMap = _CleanableThreadContextMap
import org.apache.logging.log4j.spi.ThreadContextMap2 as _ThreadContextMap2
_ThreadContextMap2 = _ThreadContextMap2
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class ObjectThreadContextMap():
    """org.apache.logging.log4j.spi.ObjectThreadContextMap"""
 
    @staticmethod
    def _wrap(java_value: _ObjectThreadContextMap) -> 'ObjectThreadContextMap':
        return ObjectThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectThreadContextMap):
        """
        Dynamic initializer for ObjectThreadContextMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectThreadContextMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectThreadContextMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def putValue(self, key: str, value: object):
        """public abstract <V> void org.apache.logging.log4j.spi.ObjectThreadContextMap.putValue(java.lang.String,V)"""
        pass

    @abstractmethod
    def getCopy(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getCopy()"""
        pass

    @abstractmethod
    def putAll(self, map: 'Map'):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap2.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def putAllValues(self, values: 'Map'):
        """public abstract <V> void org.apache.logging.log4j.spi.ObjectThreadContextMap.putAllValues(java.util.Map<java.lang.String, V>)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.isEmpty()"""
        pass

    @abstractmethod
    def getReadOnlyContextData(self, ):
        """public abstract org.apache.logging.log4j.util.StringMap org.apache.logging.log4j.spi.ThreadContextMap2.getReadOnlyContextData()"""
        pass

    @abstractmethod
    def getImmutableMapOrNull(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getImmutableMapOrNull()"""
        pass

    @abstractmethod
    def getValue(self, key: str):
        """public abstract <V> V org.apache.logging.log4j.spi.ObjectThreadContextMap.getValue(java.lang.String)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.clear()"""
        pass

    @abstractmethod
    def get(self, key: str):
        """public abstract java.lang.String org.apache.logging.log4j.spi.ThreadContextMap.get(java.lang.String)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def removeAll(self, keys: 'Iterable'):
        """public abstract void org.apache.logging.log4j.spi.CleanableThreadContextMap.removeAll(java.lang.Iterable<java.lang.String>)"""
        pass

    @abstractmethod
    def put(self, key: str, value: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.put(java.lang.String,java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.ThreadContextMap
import org.apache.logging.log4j.spi.ThreadContextMap as _ThreadContextMap
_ThreadContextMap = _ThreadContextMap
from abc import abstractmethod, ABC
 
class ThreadContextMap():
    """org.apache.logging.log4j.spi.ThreadContextMap"""
 
    @staticmethod
    def _wrap(java_value: _ThreadContextMap) -> 'ThreadContextMap':
        return ThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadContextMap):
        """
        Dynamic initializer for ThreadContextMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadContextMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadContextMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.isEmpty()"""
        pass

    @abstractmethod
    def getCopy(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getCopy()"""
        pass

    @abstractmethod
    def getImmutableMapOrNull(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getImmutableMapOrNull()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.clear()"""
        pass

    @abstractmethod
    def get(self, key: str):
        """public abstract java.lang.String org.apache.logging.log4j.spi.ThreadContextMap.get(java.lang.String)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def put(self, key: str, value: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.put(java.lang.String,java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerAdapter
import org.apache.logging.log4j.spi.LoggerAdapter as _LoggerAdapter
_LoggerAdapter = _LoggerAdapter
from abc import abstractmethod, ABC
import java.io.Closeable as _Closeable
_Closeable = _Closeable
 
class LoggerAdapter():
    """org.apache.logging.log4j.spi.LoggerAdapter"""
 
    @staticmethod
    def _wrap(java_value: _LoggerAdapter) -> 'LoggerAdapter':
        return LoggerAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoggerAdapter):
        """
        Dynamic initializer for LoggerAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoggerAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoggerAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def close(self, ):
        """public abstract void java.io.Closeable.close() throws java.io.IOException"""
        pass

    @abstractmethod
    def getLogger(self, name: str):
        """public abstract L org.apache.logging.log4j.spi.LoggerAdapter.getLogger(java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.MessageFactory2Adapter
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.message.MessageFactory as _MessageFactory
_MessageFactory = _MessageFactory
try:
    from log4py import message
except ImportError:
    message = _import_once("log4py.message")

from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import org.apache.logging.log4j.spi.MessageFactory2Adapter as _MessageFactory2Adapter
_MessageFactory2Adapter = _MessageFactory2Adapter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MessageFactory2Adapter():
    """org.apache.logging.log4j.spi.MessageFactory2Adapter"""
 
    @staticmethod
    def _wrap(java_value: _MessageFactory2Adapter) -> 'MessageFactory2Adapter':
        return MessageFactory2Adapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageFactory2Adapter):
        """
        Dynamic initializer for MessageFactory2Adapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageFactory2Adapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageFactory2Adapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message, p0, p1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.Object)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message))

    @overload
    def newMessage(self, message: str, *params: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object...)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message, params))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4))

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
    def getOriginal(self) -> 'message.MessageFactory':
        """public org.apache.logging.log4j.message.MessageFactory org.apache.logging.log4j.spi.MessageFactory2Adapter.getOriginal()"""
        return 'message.MessageFactory'._wrap(super(MessageFactory2Adapter, self).getOriginal())

    @overload
    def __init__(self, wrapped: 'MessageFactory'):
        """public org.apache.logging.log4j.spi.MessageFactory2Adapter(org.apache.logging.log4j.message.MessageFactory)"""
        val = _MessageFactory2Adapter(wrapped)
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message, p0, p1, p2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: str, p0: object) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String,java.lang.Object)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message, p0))

    @overload
    def newMessage(self, charSequence: 'CharSequence') -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.CharSequence)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(charSequence))

    @overload
    def newMessage(self, message: str) -> 'message.Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.spi.MessageFactory2Adapter.newMessage(java.lang.String)"""
        return 'message.Message'._wrap(super(_MessageFactory2Adapter, self).newMessage(message))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.spi.ExtendedLogger
from pyquantum_helper import import_once as _import_once
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import org.apache.logging.log4j.spi.ExtendedLogger as _ExtendedLogger
_ExtendedLogger = _ExtendedLogger
from abc import abstractmethod, ABC
try:
    from log4py import message
except ImportError:
    message = _import_once("log4py.message")

from builtins import object
import java.lang.StackTraceElement as StackTraceElement
import java.lang.String as _string
import org.apache.logging.log4j.Logger as _Logger
_Logger = _Logger
try:
    from log4py import util
except ImportError:
    util = _import_once("log4py.util")

try:
    import log4py
except ImportError:
    log4py = _import_once("log4py")

import java.lang.Throwable as Throwable
import org.apache.logging.log4j.LogBuilder as _LogBuilder
_LogBuilder = _LogBuilder
 
class ExtendedLogger():
    """org.apache.logging.log4j.spi.ExtendedLogger"""
 
    @staticmethod
    def _wrap(java_value: _ExtendedLogger) -> 'ExtendedLogger':
        return ExtendedLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExtendedLogger):
        """
        Dynamic initializer for ExtendedLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExtendedLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExtendedLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def error(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def exit(self, ):
        """public abstract void org.apache.logging.log4j.Logger.exit()"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isDebugEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isDebugEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def isInfoEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isInfoEnabled()"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def traceExit(self, message: 'EntryMessage'):
        """public abstract void org.apache.logging.log4j.Logger.traceExit(org.apache.logging.log4j.message.EntryMessage)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def traceEntry(self, format: str, *paramSuppliers: 'util.Supplier'):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def traceEntry(self, message: 'Message'):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def warn(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @overload
    def atLevel(self, level: 'Level') -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atLevel(org.apache.logging.log4j.Level)"""
        return 'log4py.LogBuilder'._wrap(super(_log4py.Logger, self).atLevel(level))

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: object, t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def trace(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @override
    @overload
    def logMessage(self, level: 'Level', marker: 'Marker', fqcn: str, location: 'StackTraceElement', message: 'Message', throwable: 'Throwable'):
        """public default void org.apache.logging.log4j.Logger.logMessage(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.StackTraceElement,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        super(_log4py.Logger, self).logMessage(level, marker, fqcn, location, message, throwable)

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def logMessage(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logMessage(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def debug(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def traceExit(self, message: 'Message', result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(org.apache.logging.log4j.message.Message,R)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String)"""
        pass

    @abstractmethod
    def fatal(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def getMessageFactory(self, ):
        """public abstract <MF extends org.apache.logging.log4j.message.MessageFactory> MF org.apache.logging.log4j.Logger.getMessageFactory()"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def info(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def isTraceEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isTraceEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def trace(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def catching(self, level: 'Level', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.catching(org.apache.logging.log4j.Level,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def printf(self, level: 'Level', marker: 'Marker', format: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.printf(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'CharSequence', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @override
    @overload
    def atFatal(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atFatal()"""
        return 'log4py.LogBuilder'._wrap(super(log4py.Logger, self).atFatal())

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level'):
        """public abstract boolean org.apache.logging.log4j.Logger.isEnabled(org.apache.logging.log4j.Level)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def throwing(self, level: 'Level', throwable: 'Throwable'):
        """public abstract <T extends java.lang.Throwable> T org.apache.logging.log4j.Logger.throwing(org.apache.logging.log4j.Level,T)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: 'Message', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def error(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @override
    @overload
    def always(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.always()"""
        return 'log4py.LogBuilder'._wrap(super(log4py.Logger, self).always())

    @abstractmethod
    def error(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isErrorEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isErrorEnabled()"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isErrorEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isErrorEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def debug(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isWarnEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isWarnEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isWarnEnabled()"""
        pass

    @abstractmethod
    def traceEntry(self, *paramSuppliers: 'util.Supplier'):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def trace(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def trace(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: object, t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def traceEntry(self, format: str, *params: object):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def isDebugEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isDebugEnabled()"""
        pass

    @abstractmethod
    def trace(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def atError(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atError()"""
        return 'log4py.LogBuilder'._wrap(super(log4py.Logger, self).atError())

    @override
    @overload
    def atWarn(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atWarn()"""
        return 'log4py.LogBuilder'._wrap(super(log4py.Logger, self).atWarn())

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def printf(self, level: 'Level', format: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.printf(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String)"""
        pass

    @abstractmethod
    def debug(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.Logger.getName()"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def throwing(self, throwable: 'Throwable'):
        """public abstract <T extends java.lang.Throwable> T org.apache.logging.log4j.Logger.throwing(T)"""
        pass

    @abstractmethod
    def debug(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def catching(self, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.catching(java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def fatal(self, message: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def entry(self, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.entry(java.lang.Object...)"""
        pass

    @abstractmethod
    def traceExit(self, result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(R)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isInfoEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isInfoEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String)"""
        pass

    @abstractmethod
    def info(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def traceExit(self, message: 'EntryMessage', result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(org.apache.logging.log4j.message.EntryMessage,R)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def getFlowMessageFactory(self, ):
        """public abstract org.apache.logging.log4j.message.FlowMessageFactory org.apache.logging.log4j.Logger.getFlowMessageFactory()"""
        pass

    @override
    @overload
    def atInfo(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atInfo()"""
        return 'log4py.LogBuilder'._wrap(super(log4py.Logger, self).atInfo())

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def atDebug(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atDebug()"""
        return 'log4py.LogBuilder'._wrap(super(log4py.Logger, self).atDebug())

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', msgSupplier: 'MessageSupplier', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: str, t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isTraceEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isTraceEnabled()"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isFatalEnabled(self, ):
        """public abstract boolean org.apache.logging.log4j.Logger.isFatalEnabled()"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def debug(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def fatal(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def traceEntry(self, ):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.Logger.traceEntry()"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def traceExit(self, ):
        """public abstract void org.apache.logging.log4j.Logger.traceExit()"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isFatalEnabled(self, marker: 'Marker'):
        """public abstract boolean org.apache.logging.log4j.Logger.isFatalEnabled(org.apache.logging.log4j.Marker)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: str):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def warn(self, message: 'Message', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.message.Message,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def atTrace(self) -> 'log4py.LogBuilder':
        """public default org.apache.logging.log4j.LogBuilder org.apache.logging.log4j.Logger.atTrace()"""
        return 'log4py.LogBuilder'._wrap(super(log4py.Logger, self).atTrace())

    @abstractmethod
    def exit(self, result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.exit(R)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def info(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def trace(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def info(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'MessageSupplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.MessageSupplier,java.lang.Throwable)"""
        pass

    @abstractmethod
    def debug(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def traceExit(self, format: str, result: object):
        """public abstract <R> R org.apache.logging.log4j.Logger.traceExit(java.lang.String,R)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def entry(self, ):
        """public abstract void org.apache.logging.log4j.Logger.entry()"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def info(self, message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.debug(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def warn(self, messageSupplier: 'Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.util.Supplier<?>)"""
        pass

    @abstractmethod
    def fatal(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def getLevel(self, ):
        """public abstract org.apache.logging.log4j.Level org.apache.logging.log4j.Logger.getLevel()"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'Supplier', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', msgSupplier: 'Supplier', t: 'Throwable'):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,org.apache.logging.log4j.util.Supplier<?>,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, marker: 'Marker', message: str, *paramSuppliers: 'util.Supplier'):
        """public abstract void org.apache.logging.log4j.Logger.info(org.apache.logging.log4j.Marker,java.lang.String,org.apache.logging.log4j.util.Supplier<?>...)"""
        pass

    @abstractmethod
    def warn(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.warn(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def fatal(self, message: object, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.Object,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def trace(self, message: str, *params: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def fatal(self, message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.fatal(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: str, p0: object, p1: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def fatal(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.fatal(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def info(self, message: 'CharSequence'):
        """public abstract void org.apache.logging.log4j.Logger.info(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def warn(self, marker: 'Marker', message: str):
        """public abstract void org.apache.logging.log4j.Logger.warn(org.apache.logging.log4j.Marker,java.lang.String)"""
        pass

    @abstractmethod
    def logIfEnabled(self, fqcn: str, level: 'Level', marker: 'Marker', message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract void org.apache.logging.log4j.spi.ExtendedLogger.logIfEnabled(java.lang.String,org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, marker: 'Marker', message: str, p0: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def isEnabled(self, level: 'Level', marker: 'Marker', message: 'CharSequence', t: 'Throwable'):
        """public abstract boolean org.apache.logging.log4j.spi.ExtendedLogger.isEnabled(org.apache.logging.log4j.Level,org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass

    @abstractmethod
    def error(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def error(self, message: str, throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.error(java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', messageSupplier: 'MessageSupplier'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.util.MessageSupplier)"""
        pass

    @abstractmethod
    def log(self, level: 'Level', message: 'Message'):
        """public abstract void org.apache.logging.log4j.Logger.log(org.apache.logging.log4j.Level,org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def error(self, marker: 'Marker', message: object):
        """public abstract void org.apache.logging.log4j.Logger.error(org.apache.logging.log4j.Marker,java.lang.Object)"""
        pass

    @abstractmethod
    def trace(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract void org.apache.logging.log4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def debug(self, marker: 'Marker', message: 'CharSequence', throwable: 'Throwable'):
        """public abstract void org.apache.logging.log4j.Logger.debug(org.apache.logging.log4j.Marker,java.lang.CharSequence,java.lang.Throwable)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.ThreadContextStack
import java.util.function.Predicate as Predicate
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _Object
_Object = _Object
import org.apache.logging.log4j.ThreadContext as _ThreadContext_ContextStack
_ContextStack = _ThreadContext_ContextStack.ContextStack
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
import org.apache.logging.log4j.spi.ThreadContextStack as _ThreadContextStack
_ThreadContextStack = _ThreadContextStack
from typing import List
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
from builtins import bool
 
class ThreadContextStack():
    """org.apache.logging.log4j.spi.ThreadContextStack"""
 
    @staticmethod
    def _wrap(java_value: _ThreadContextStack) -> 'ThreadContextStack':
        return ThreadContextStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadContextStack):
        """
        Dynamic initializer for ThreadContextStack.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadContextStack__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadContextStack__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Collection.size()"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Collection.isEmpty()"""
        pass

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @abstractmethod
    def retainAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.retainAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Collection.hashCode()"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @abstractmethod
    def toArray(self, arg0: 'Object'):
        """public abstract <T> T[] java.util.Collection.toArray(T[])"""
        pass

    @abstractmethod
    def copy(self, ):
        """public abstract org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.ThreadContext$ContextStack.copy()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Collection.clear()"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract boolean java.util.Collection.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def removeAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.removeAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def containsAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.containsAll(java.util.Collection<?>)"""
        pass

    @abstractmethod
    def pop(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.ThreadContext$ContextStack.pop()"""
        pass

    @abstractmethod
    def peek(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.ThreadContext$ContextStack.peek()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Collection.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def asList(self, ):
        """public abstract java.util.List<java.lang.String> org.apache.logging.log4j.ThreadContext$ContextStack.asList()"""
        pass

    @abstractmethod
    def trim(self, depth: int):
        """public abstract void org.apache.logging.log4j.ThreadContext$ContextStack.trim(int)"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<E> java.util.Collection.iterator()"""
        pass

    @abstractmethod
    def push(self, message: str):
        """public abstract void org.apache.logging.log4j.ThreadContext$ContextStack.push(java.lang.String)"""
        pass

    @abstractmethod
    def contains(self, arg0: object):
        """public abstract boolean java.util.Collection.contains(java.lang.Object)"""
        pass

    @abstractmethod
    def addAll(self, arg0: 'Collection'):
        """public abstract boolean java.util.Collection.addAll(java.util.Collection<? extends E>)"""
        pass

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @abstractmethod
    def add(self, arg0: object):
        """public abstract boolean java.util.Collection.add(E)"""
        pass

    @abstractmethod
    def toArray(self, ):
        """public abstract java.lang.Object[] java.util.Collection.toArray()"""
        pass

    @abstractmethod
    def getDepth(self, ):
        """public abstract int org.apache.logging.log4j.ThreadContext$ContextStack.getDepth()"""
        pass

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @abstractmethod
    def getImmutableStackOrNull(self, ):
        """public abstract org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.ThreadContext$ContextStack.getImmutableStackOrNull()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: org.apache.logging.log4j.spi.DefaultThreadContextStack
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.logging.log4j.ThreadContext as _ThreadContext_ContextStack
_ContextStack = _ThreadContext_ContextStack.ContextStack
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import org.apache.logging.log4j.spi.DefaultThreadContextStack as _DefaultThreadContextStack
_DefaultThreadContextStack = _DefaultThreadContextStack
import java.lang.String as _string
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
try:
    import log4py
except ImportError:
    log4py = _import_once("log4py")

import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.logging.log4j.spi.ThreadContextStack as _ThreadContextStack
_ThreadContextStack = _ThreadContextStack
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
from typing import List
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.StringBuilder as StringBuilder
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class DefaultThreadContextStack():
    """org.apache.logging.log4j.spi.DefaultThreadContextStack"""
 
    @staticmethod
    def _wrap(java_value: _DefaultThreadContextStack) -> 'DefaultThreadContextStack':
        return DefaultThreadContextStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultThreadContextStack):
        """
        Dynamic initializer for DefaultThreadContextStack.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultThreadContextStack__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultThreadContextStack__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def pop(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.DefaultThreadContextStack.pop()"""
        return str._wrap(super(DefaultThreadContextStack, self).pop())

    @override
    @overload
    def copy(self) -> 'ThreadContextStack':
        """public org.apache.logging.log4j.spi.ThreadContextStack org.apache.logging.log4j.spi.DefaultThreadContextStack.copy()"""
        return 'ThreadContextStack'._wrap(super(DefaultThreadContextStack, self).copy())

    @overload
    def containsAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_DefaultThreadContextStack, self).containsAll(objects))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def remove(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.remove(java.lang.Object)"""
        return bool._wrap(super(_DefaultThreadContextStack, self).remove(o))

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextStack.formatTo(java.lang.StringBuilder)"""
        super(_DefaultThreadContextStack, self).formatTo(buffer)

    @override
    @overload
    def asList(self) -> 'List':
        """public java.util.List<java.lang.String> org.apache.logging.log4j.spi.DefaultThreadContextStack.asList()"""
        return 'List'._wrap(super(DefaultThreadContextStack, self).asList())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Collection.spliterator()"""
        return 'Spliterator'._wrap(super(Collection, self).spliterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<java.lang.String> org.apache.logging.log4j.spi.DefaultThreadContextStack.iterator()"""
        return 'Iterator'._wrap(super(DefaultThreadContextStack, self).iterator())

    @override
    @overload
    def trim(self, depth: int):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextStack.trim(int)"""
        super(_DefaultThreadContextStack, self).trim(_int.valueOf(depth))

    @override
    @overload
    def getImmutableStackOrNull(self) -> 'log4py.ThreadContext$ContextStack':
        """public org.apache.logging.log4j.ThreadContext$ContextStack org.apache.logging.log4j.spi.DefaultThreadContextStack.getImmutableStackOrNull()"""
        return 'log4py.ThreadContext$ContextStack'._wrap(super(DefaultThreadContextStack, self).getImmutableStackOrNull())

    @overload
    def __init__(self, useStack: bool):
        """public org.apache.logging.log4j.spi.DefaultThreadContextStack(boolean)"""
        val = _DefaultThreadContextStack(_boolean.valueOf(useStack))
        self.__wrapper = val

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.equals(java.lang.Object)"""
        return bool._wrap(super(_DefaultThreadContextStack, self).equals(obj))

    @override
    @overload
    def getDepth(self) -> int:
        """public int org.apache.logging.log4j.spi.DefaultThreadContextStack.getDepth()"""
        return int._wrap(super(DefaultThreadContextStack, self).getDepth())

    @overload
    def contains(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.contains(java.lang.Object)"""
        return bool._wrap(super(_DefaultThreadContextStack, self).contains(o))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextStack.clear()"""
        super(DefaultThreadContextStack, self).clear()

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @override
    @overload
    def push(self, message: str):
        """public void org.apache.logging.log4j.spi.DefaultThreadContextStack.push(java.lang.String)"""
        super(_DefaultThreadContextStack, self).push(message)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.spi.DefaultThreadContextStack.hashCode()"""
        return int._wrap(super(DefaultThreadContextStack, self).hashCode())

    @overload
    def retainAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_DefaultThreadContextStack, self).retainAll(objects))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.DefaultThreadContextStack.toString()"""
        return str._wrap(super(DefaultThreadContextStack, self).toString())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.isEmpty()"""
        return bool._wrap(super(DefaultThreadContextStack, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def peek(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.DefaultThreadContextStack.peek()"""
        return str._wrap(super(DefaultThreadContextStack, self).peek())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.spi.DefaultThreadContextStack.toArray()"""
        return List[object]._wrap(super(DefaultThreadContextStack, self).toArray())

    @overload
    def toArray(self, ts: 'Object') -> List[object]:
        """public <T> T[] org.apache.logging.log4j.spi.DefaultThreadContextStack.toArray(T[])"""
        return List[object]._wrap(super(_DefaultThreadContextStack, self).toArray(ts))

    @overload
    def addAll(self, strings: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.addAll(java.util.Collection<? extends java.lang.String>)"""
        return bool._wrap(super(_DefaultThreadContextStack, self).addAll(strings))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeAll(self, objects: 'Collection') -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_DefaultThreadContextStack, self).removeAll(objects))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.logging.log4j.spi.DefaultThreadContextStack.size()"""
        return int._wrap(super(DefaultThreadContextStack, self).size())

    @overload
    def add(self, s: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.DefaultThreadContextStack.add(java.lang.String)"""
        return bool._wrap(super(_DefaultThreadContextStack, self).add(s)) 
 
 
# CLASS: org.apache.logging.log4j.spi.ThreadContextMap2
import org.apache.logging.log4j.spi.ThreadContextMap as _ThreadContextMap
_ThreadContextMap = _ThreadContextMap
import org.apache.logging.log4j.spi.ThreadContextMap2 as _ThreadContextMap2
_ThreadContextMap2 = _ThreadContextMap2
from abc import abstractmethod, ABC
import java.util.Map as Map
 
class ThreadContextMap2():
    """org.apache.logging.log4j.spi.ThreadContextMap2"""
 
    @staticmethod
    def _wrap(java_value: _ThreadContextMap2) -> 'ThreadContextMap2':
        return ThreadContextMap2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadContextMap2):
        """
        Dynamic initializer for ThreadContextMap2.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadContextMap2__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadContextMap2__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.isEmpty()"""
        pass

    @abstractmethod
    def getReadOnlyContextData(self, ):
        """public abstract org.apache.logging.log4j.util.StringMap org.apache.logging.log4j.spi.ThreadContextMap2.getReadOnlyContextData()"""
        pass

    @abstractmethod
    def getCopy(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getCopy()"""
        pass

    @abstractmethod
    def getImmutableMapOrNull(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.ThreadContextMap.getImmutableMapOrNull()"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.clear()"""
        pass

    @abstractmethod
    def putAll(self, map: 'Map'):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap2.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        pass

    @abstractmethod
    def get(self, key: str):
        """public abstract java.lang.String org.apache.logging.log4j.spi.ThreadContextMap.get(java.lang.String)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.spi.ThreadContextMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def put(self, key: str, value: str):
        """public abstract void org.apache.logging.log4j.spi.ThreadContextMap.put(java.lang.String,java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.Provider
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.net.URL as URL
import java.lang.String as _string
import org.apache.logging.log4j.spi.Provider as _Provider
_Provider = _Provider
import java.net.URL as _URL
_URL = _URL
import java.lang.Integer as _int
import java.lang.Integer as Integer
import java.lang.ClassLoader as ClassLoader
import java.util.Properties as Properties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Provider():
    """org.apache.logging.log4j.spi.Provider"""
 
    @staticmethod
    def _wrap(java_value: _Provider) -> 'Provider':
        return Provider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Provider):
        """
        Dynamic initializer for Provider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Provider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Provider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getVersions(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.Provider.getVersions()"""
        return str._wrap(super(Provider, self).getVersions())

    @overload
    def getUrl(self) -> 'URL':
        """public java.net.URL org.apache.logging.log4j.spi.Provider.getUrl()"""
        return 'URL'._wrap(super(Provider, self).getUrl())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getThreadContextMap(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.Provider.getThreadContextMap()"""
        return str._wrap(super(Provider, self).getThreadContextMap())

    @overload
    def loadThreadContextMap(self) -> 'type.Class':
        """public java.lang.Class<? extends org.apache.logging.log4j.spi.ThreadContextMap> org.apache.logging.log4j.spi.Provider.loadThreadContextMap()"""
        return 'type.Class'._wrap(super(Provider, self).loadThreadContextMap())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.spi.Provider.hashCode()"""
        return int._wrap(super(Provider, self).hashCode())

    @overload
    def getPriority(self) -> 'Integer':
        """public java.lang.Integer org.apache.logging.log4j.spi.Provider.getPriority()"""
        return _transform(super(Provider, self).getPriority()).'Integer'Value()

    @overload
    def __init__(self, props: 'Properties', url: 'URL', classLoader: 'ClassLoader'):
        """public org.apache.logging.log4j.spi.Provider(java.util.Properties,java.net.URL,java.lang.ClassLoader)"""
        val = _Provider(props, url, classLoader)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.Provider.toString()"""
        return str._wrap(super(Provider, self).toString())

    @overload
    def __init__(self, priority: 'Integer', versions: str, loggerContextFactoryClass: 'Class'):
        """public org.apache.logging.log4j.spi.Provider(java.lang.Integer,java.lang.String,java.lang.Class<? extends org.apache.logging.log4j.spi.LoggerContextFactory>)"""
        val = _Provider(priority, versions, loggerContextFactoryClass)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getClassName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.Provider.getClassName()"""
        return str._wrap(super(Provider, self).getClassName())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, priority: 'Integer', versions: str, loggerContextFactoryClass: 'Class', threadContextMapClass: 'Class'):
        """public org.apache.logging.log4j.spi.Provider(java.lang.Integer,java.lang.String,java.lang.Class<? extends org.apache.logging.log4j.spi.LoggerContextFactory>,java.lang.Class<? extends org.apache.logging.log4j.spi.ThreadContextMap>)"""
        val = _Provider(priority, versions, loggerContextFactoryClass, threadContextMapClass)
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
    def loadLoggerContextFactory(self) -> 'type.Class':
        """public java.lang.Class<? extends org.apache.logging.log4j.spi.LoggerContextFactory> org.apache.logging.log4j.spi.Provider.loadLoggerContextFactory()"""
        return 'type.Class'._wrap(super(Provider, self).loadLoggerContextFactory())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.spi.Provider.equals(java.lang.Object)"""
        return bool._wrap(super(_Provider, self).equals(o)) 
 
 
# CLASS: org.apache.logging.log4j.spi.LoggerContextShutdownAware
import org.apache.logging.log4j.spi.LoggerContextShutdownAware as _LoggerContextShutdownAware
_LoggerContextShutdownAware = _LoggerContextShutdownAware
from abc import abstractmethod, ABC
 
class LoggerContextShutdownAware():
    """org.apache.logging.log4j.spi.LoggerContextShutdownAware"""
 
    @staticmethod
    def _wrap(java_value: _LoggerContextShutdownAware) -> 'LoggerContextShutdownAware':
        return LoggerContextShutdownAware(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoggerContextShutdownAware):
        """
        Dynamic initializer for LoggerContextShutdownAware.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoggerContextShutdownAware__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoggerContextShutdownAware__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def contextShutdown(self, loggerContext: 'LoggerContext'):
        """public abstract void org.apache.logging.log4j.spi.LoggerContextShutdownAware.contextShutdown(org.apache.logging.log4j.spi.LoggerContext)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.spi.NoOpThreadContextMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.spi.NoOpThreadContextMap as _NoOpThreadContextMap
_NoOpThreadContextMap = _NoOpThreadContextMap
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NoOpThreadContextMap():
    """org.apache.logging.log4j.spi.NoOpThreadContextMap"""
 
    @staticmethod
    def _wrap(java_value: _NoOpThreadContextMap) -> 'NoOpThreadContextMap':
        return NoOpThreadContextMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NoOpThreadContextMap):
        """
        Dynamic initializer for NoOpThreadContextMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NoOpThreadContextMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NoOpThreadContextMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getImmutableMapOrNull(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.NoOpThreadContextMap.getImmutableMapOrNull()"""
        return 'Map'._wrap(super(NoOpThreadContextMap, self).getImmutableMapOrNull())

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.spi.NoOpThreadContextMap()"""
        val = _NoOpThreadContextMap()
        self.__wrapper = val

    @override
    @overload
    def getCopy(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.spi.NoOpThreadContextMap.getCopy()"""
        return 'Map'._wrap(super(NoOpThreadContextMap, self).getCopy())

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

    @overload
    def get(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.spi.NoOpThreadContextMap.get(java.lang.String)"""
        return str._wrap(super(_NoOpThreadContextMap, self).get(key))

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
        """public org.apache.logging.log4j.spi.NoOpThreadContextMap()"""
        val = _NoOpThreadContextMap()
        self.__wrapper = val

    @override
    @overload
    def put(self, key: str, value: str):
        """public void org.apache.logging.log4j.spi.NoOpThreadContextMap.put(java.lang.String,java.lang.String)"""
        super(_NoOpThreadContextMap, self).put(key, value)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.spi.NoOpThreadContextMap.clear()"""
        super(NoOpThreadContextMap, self).clear()

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.logging.log4j.spi.NoOpThreadContextMap.isEmpty()"""
        return bool._wrap(super(NoOpThreadContextMap, self).isEmpty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.spi.NoOpThreadContextMap.containsKey(java.lang.String)"""
        return bool._wrap(super(_NoOpThreadContextMap, self).containsKey(key))

    @override
    @overload
    def remove(self, key: str):
        """public void org.apache.logging.log4j.spi.NoOpThreadContextMap.remove(java.lang.String)"""
        super(_NoOpThreadContextMap, self).remove(key)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.spi.ThreadContextMapFactory
from builtins import str
from pyquantum_helper import override
import org.apache.logging.log4j.spi.ThreadContextMap as _ThreadContextMap
_ThreadContextMap = _ThreadContextMap
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.logging.log4j.spi.ThreadContextMapFactory as _ThreadContextMapFactory
_ThreadContextMapFactory = _ThreadContextMapFactory
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ThreadContextMapFactory():
    """org.apache.logging.log4j.spi.ThreadContextMapFactory"""
 
    @staticmethod
    def _wrap(java_value: _ThreadContextMapFactory) -> 'ThreadContextMapFactory':
        return ThreadContextMapFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadContextMapFactory):
        """
        Dynamic initializer for ThreadContextMapFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadContextMapFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadContextMapFactory__wrapper":
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

    @staticmethod
    @overload
    def createThreadContextMap() -> 'ThreadContextMap':
        """public static org.apache.logging.log4j.spi.ThreadContextMap org.apache.logging.log4j.spi.ThreadContextMapFactory.createThreadContextMap()"""
        return ThreadContextMap._wrap(_ThreadContextMapFactory.createThreadContextMap())

        @staticmethod
        @overload
        def init():
            """public static void org.apache.logging.log4j.spi.ThreadContextMapFactory.init()"""
            _ThreadContextMapFactory.init()

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())