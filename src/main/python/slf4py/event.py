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
import org.slf4j.event.KeyValuePair as _KeyValuePair
_KeyValuePair = _KeyValuePair
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KeyValuePair():
    """org.slf4j.event.KeyValuePair"""
 
    @staticmethod
    def _wrap(java_value: _KeyValuePair) -> 'KeyValuePair':
        return KeyValuePair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeyValuePair):
        """
        Dynamic initializer for KeyValuePair.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeyValuePair__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeyValuePair__wrapper":
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.slf4j.event.KeyValuePair.equals(java.lang.Object)"""
        return bool._wrap(super(_KeyValuePair, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.slf4j.event.KeyValuePair.hashCode()"""
        return int._wrap(super(KeyValuePair, self).hashCode())

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
    def __init__(self, arg0: str, arg1: object):
        """public org.slf4j.event.KeyValuePair(java.lang.String,java.lang.Object)"""
        val = _KeyValuePair(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.slf4j.event.KeyValuePair.toString()"""
        return str._wrap(super(KeyValuePair, self).toString())

 
 
 
# CLASS: org.slf4j.event.KeyValuePair
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.slf4j.event.KeyValuePair as _KeyValuePair
_KeyValuePair = _KeyValuePair
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KeyValuePair():
    """org.slf4j.event.KeyValuePair"""
 
    @staticmethod
    def _wrap(java_value: _KeyValuePair) -> 'KeyValuePair':
        return KeyValuePair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeyValuePair):
        """
        Dynamic initializer for KeyValuePair.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeyValuePair__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeyValuePair__wrapper":
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.slf4j.event.KeyValuePair.equals(java.lang.Object)"""
        return bool._wrap(super(_KeyValuePair, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.slf4j.event.KeyValuePair.hashCode()"""
        return int._wrap(super(KeyValuePair, self).hashCode())

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
    def __init__(self, arg0: str, arg1: object):
        """public org.slf4j.event.KeyValuePair(java.lang.String,java.lang.Object)"""
        val = _KeyValuePair(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.slf4j.event.KeyValuePair.toString()"""
        return str._wrap(super(KeyValuePair, self).toString())

 
 
 
# CLASS: org.slf4j.event.KeyValuePair 
 
 
# CLASS: org.slf4j.event.EventRecordingLogger
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.slf4j.helpers.AbstractLogger as _AbstractLogger
_AbstractLogger = _AbstractLogger
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from slf4py import spi
except ImportError:
    spi = _import_once("slf4py.spi")

try:
    from slf4py import helpers
except ImportError:
    helpers = _import_once("slf4py.helpers")

import java.lang.String as _String
_String = _String
import org.slf4j.helpers.LegacyAbstractLogger as _LegacyAbstractLogger
_LegacyAbstractLogger = _LegacyAbstractLogger
from builtins import object
import org.slf4j.Logger as _Logger
_Logger = _Logger
import java.util.Queue as Queue
import org.slf4j.event.EventRecordingLogger as _EventRecordingLogger
_EventRecordingLogger = _EventRecordingLogger
import java.lang.String as _string
import org.slf4j.spi.LoggingEventBuilder as _LoggingEventBuilder
_LoggingEventBuilder = _LoggingEventBuilder
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EventRecordingLogger():
    """org.slf4j.event.EventRecordingLogger"""
 
    @staticmethod
    def _wrap(java_value: _EventRecordingLogger) -> 'EventRecordingLogger':
        return EventRecordingLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventRecordingLogger):
        """
        Dynamic initializer for EventRecordingLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventRecordingLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventRecordingLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).info(arg0, arg1, arg2, arg3)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_helpers.AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(_helpers.AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String)"""
        super(_helpers.AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String)"""
        super(_helpers.AbstractLogger, self).debug(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public boolean org.slf4j.event.EventRecordingLogger.isInfoEnabled()"""
        return bool._wrap(super(EventRecordingLogger, self).isInfoEnabled())

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String)"""
        super(_helpers.AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String)"""
        super(_helpers.AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(_helpers.AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).trace(arg0, arg1, arg2, arg3)

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atError())

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public boolean org.slf4j.event.EventRecordingLogger.isTraceEnabled()"""
        return bool._wrap(super(EventRecordingLogger, self).isTraceEnabled())

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_helpers.AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_helpers.AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(_helpers.AbstractLogger, self).error(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isWarnEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isWarnEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_helpers.LegacyAbstractLogger, self).isWarnEnabled(arg0))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).debug(arg0, arg1, arg2, arg3)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_helpers.AbstractLogger, self).debug(arg0, arg1, arg2)

    @overload
    def isTraceEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isTraceEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_helpers.LegacyAbstractLogger, self).isTraceEnabled(arg0))

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(_helpers.AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atTrace())

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_helpers.AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atWarn()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atWarn())

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_helpers.AbstractLogger, self).warn(arg0, arg1, arg2)

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool._wrap(super(_slf4py.Logger, self).isEnabledForLevel(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public boolean org.slf4j.event.EventRecordingLogger.isErrorEnabled()"""
        return bool._wrap(super(EventRecordingLogger, self).isErrorEnabled())

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(_helpers.AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'SubstituteLogger', arg1: 'Queue'):
        """public org.slf4j.event.EventRecordingLogger(org.slf4j.helpers.SubstituteLogger,java.util.Queue<org.slf4j.event.SubstituteLoggingEvent>)"""
        val = _EventRecordingLogger(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean org.slf4j.event.EventRecordingLogger.isDebugEnabled()"""
        return bool._wrap(super(EventRecordingLogger, self).isDebugEnabled())

    @overload
    def isDebugEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isDebugEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_helpers.LegacyAbstractLogger, self).isDebugEnabled(arg0))

    @override
    @overload
    def error(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String)"""
        super(_helpers.AbstractLogger, self).error(arg0)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.event.EventRecordingLogger.getName()"""
        return str._wrap(super(EventRecordingLogger, self).getName())

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String)"""
        super(_helpers.AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(_helpers.AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_helpers.AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).warn(arg0, arg1, arg2, arg3)

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_slf4py.Logger, self).atLevel(arg0))

    @override
    @overload
    def trace(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_helpers.AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(_helpers.AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(_helpers.AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(_helpers.AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String)"""
        super(_helpers.AbstractLogger, self).info(arg0)

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public boolean org.slf4j.event.EventRecordingLogger.isWarnEnabled()"""
        return bool._wrap(super(EventRecordingLogger, self).isWarnEnabled())

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(_helpers.AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String)"""
        super(_helpers.AbstractLogger, self).trace(arg0)

    @overload
    def isErrorEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isErrorEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_helpers.LegacyAbstractLogger, self).isErrorEnabled(arg0))

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).error(arg0, arg1, arg2, arg3)

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'._wrap(super(_slf4py.Logger, self).makeLoggingEventBuilder(arg0))

    @overload
    def isInfoEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isInfoEnabled(org.slf4j.Marker)"""
        return bool._wrap(super(_helpers.LegacyAbstractLogger, self).isInfoEnabled(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(_helpers.AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atInfo())

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(_helpers.AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'._wrap(super(slf4py.Logger, self).atDebug())

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def warn(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String)"""
        super(_helpers.AbstractLogger, self).warn(arg0)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String)"""
        super(_helpers.AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(_helpers.AbstractLogger, self).info(arg0, arg1) 
 
 
# CLASS: org.slf4j.event.EventConstants
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.slf4j.event.EventConstants as _EventConstants
_EventConstants = _EventConstants
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EventConstants():
    """org.slf4j.event.EventConstants"""
 
    @staticmethod
    def _wrap(java_value: _EventConstants) -> 'EventConstants':
        return EventConstants(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventConstants):
        """
        Dynamic initializer for EventConstants.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventConstants__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventConstants__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.slf4j.event.EventConstants()"""
        val = _EventConstants()
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

    @overload
    def __init__(self, ):
        """public org.slf4j.event.EventConstants()"""
        val = _EventConstants()
        self.__wrapper = val

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
 
 
# CLASS: org.slf4j.event.SubstituteLoggingEvent
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.slf4j.event.SubstituteLoggingEvent as _SubstituteLoggingEvent
_SubstituteLoggingEvent = _SubstituteLoggingEvent
try:
    from slf4py import helpers
except ImportError:
    helpers = _import_once("slf4py.helpers")

import org.slf4j.event.LoggingEvent as _LoggingEvent
_LoggingEvent = _LoggingEvent
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
from typing import List
import org.slf4j.helpers.SubstituteLogger as _SubstituteLogger
_SubstituteLogger = _SubstituteLogger
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

import org.slf4j.event.Level as _Level
_Level = _Level
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SubstituteLoggingEvent():
    """org.slf4j.event.SubstituteLoggingEvent"""
 
    @staticmethod
    def _wrap(java_value: _SubstituteLoggingEvent) -> 'SubstituteLoggingEvent':
        return SubstituteLoggingEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SubstituteLoggingEvent):
        """
        Dynamic initializer for SubstituteLoggingEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SubstituteLoggingEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SubstituteLoggingEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLevel(self) -> 'Level':
        """public org.slf4j.event.Level org.slf4j.event.SubstituteLoggingEvent.getLevel()"""
        return 'Level'._wrap(super(SubstituteLoggingEvent, self).getLevel())

    @overload
    def __init__(self):
        """public org.slf4j.event.SubstituteLoggingEvent()"""
        val = _SubstituteLoggingEvent()
        self.__wrapper = val

    @override
    @overload
    def getArguments(self) -> 'List':
        """public java.util.List<java.lang.Object> org.slf4j.event.SubstituteLoggingEvent.getArguments()"""
        return 'List'._wrap(super(SubstituteLoggingEvent, self).getArguments())

    @overload
    def setThrowable(self, arg0: 'Throwable'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setThrowable(java.lang.Throwable)"""
        super(_SubstituteLoggingEvent, self).setThrowable(arg0)

    @override
    @overload
    def getTimeStamp(self) -> int:
        """public long org.slf4j.event.SubstituteLoggingEvent.getTimeStamp()"""
        return int._wrap(super(SubstituteLoggingEvent, self).getTimeStamp())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setArgumentArray(self, arg0: 'Object'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setArgumentArray(java.lang.Object[])"""
        super(_SubstituteLoggingEvent, self).setArgumentArray(arg0)

    @overload
    def __init__(self, ):
        """public org.slf4j.event.SubstituteLoggingEvent()"""
        val = _SubstituteLoggingEvent()
        self.__wrapper = val

    @overload
    def setLoggerName(self, arg0: str):
        """public void org.slf4j.event.SubstituteLoggingEvent.setLoggerName(java.lang.String)"""
        super(_SubstituteLoggingEvent, self).setLoggerName(arg0)

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
    def getThreadName(self) -> str:
        """public java.lang.String org.slf4j.event.SubstituteLoggingEvent.getThreadName()"""
        return str._wrap(super(SubstituteLoggingEvent, self).getThreadName())

    @overload
    def setThreadName(self, arg0: str):
        """public void org.slf4j.event.SubstituteLoggingEvent.setThreadName(java.lang.String)"""
        super(_SubstituteLoggingEvent, self).setThreadName(arg0)

    @overload
    def setMessage(self, arg0: str):
        """public void org.slf4j.event.SubstituteLoggingEvent.setMessage(java.lang.String)"""
        super(_SubstituteLoggingEvent, self).setMessage(arg0)

    @override
    @overload
    def getArgumentArray(self) -> List[object]:
        """public java.lang.Object[] org.slf4j.event.SubstituteLoggingEvent.getArgumentArray()"""
        return List[object]._wrap(super(SubstituteLoggingEvent, self).getArgumentArray())

    @overload
    def setTimeStamp(self, arg0: int):
        """public void org.slf4j.event.SubstituteLoggingEvent.setTimeStamp(long)"""
        super(_SubstituteLoggingEvent, self).setTimeStamp(_long.valueOf(arg0))

    @overload
    def addMarker(self, arg0: 'Marker'):
        """public void org.slf4j.event.SubstituteLoggingEvent.addMarker(org.slf4j.Marker)"""
        super(_SubstituteLoggingEvent, self).addMarker(arg0)

    @overload
    def getLogger(self) -> 'helpers.SubstituteLogger':
        """public org.slf4j.helpers.SubstituteLogger org.slf4j.event.SubstituteLoggingEvent.getLogger()"""
        return 'helpers.SubstituteLogger'._wrap(super(SubstituteLoggingEvent, self).getLogger())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.slf4j.event.SubstituteLoggingEvent.getMessage()"""
        return str._wrap(super(SubstituteLoggingEvent, self).getMessage())

    @overload
    def setLogger(self, arg0: 'SubstituteLogger'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setLogger(org.slf4j.helpers.SubstituteLogger)"""
        super(_SubstituteLoggingEvent, self).setLogger(arg0)

    @override
    @overload
    def getKeyValuePairs(self) -> 'List':
        """public java.util.List<org.slf4j.event.KeyValuePair> org.slf4j.event.SubstituteLoggingEvent.getKeyValuePairs()"""
        return 'List'._wrap(super(SubstituteLoggingEvent, self).getKeyValuePairs())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.slf4j.event.SubstituteLoggingEvent.getThrowable()"""
        return 'Throwable'._wrap(super(SubstituteLoggingEvent, self).getThrowable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setLevel(self, arg0: 'Level'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setLevel(org.slf4j.event.Level)"""
        super(_SubstituteLoggingEvent, self).setLevel(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getMarkers(self) -> 'List':
        """public java.util.List<org.slf4j.Marker> org.slf4j.event.SubstituteLoggingEvent.getMarkers()"""
        return 'List'._wrap(super(SubstituteLoggingEvent, self).getMarkers())

    @override
    @overload
    def getLoggerName(self) -> str:
        """public java.lang.String org.slf4j.event.SubstituteLoggingEvent.getLoggerName()"""
        return str._wrap(super(SubstituteLoggingEvent, self).getLoggerName())

    @override
    @overload
    def getCallerBoundary(self) -> str:
        """public default java.lang.String org.slf4j.event.LoggingEvent.getCallerBoundary()"""
        return str._wrap(super(LoggingEvent, self).getCallerBoundary())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.slf4j.event.Level
from builtins import str
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
import org.slf4j.event.Level as _Level
_Level = _Level
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Level():
    """org.slf4j.event.Level"""
 
    @staticmethod
    def _wrap(java_value: _Level) -> 'Level':
        return Level(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Level):
        """
        Dynamic initializer for Level.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Level__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Level__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def valueOf(arg0: str) -> 'Level':
        """public static org.slf4j.event.Level org.slf4j.event.Level.valueOf(java.lang.String)"""
        return Level._wrap(_Level.valueOf(arg0))

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

    @staticmethod
    @overload
    def intToLevel(arg0: int) -> 'Level':
        """public static org.slf4j.event.Level org.slf4j.event.Level.intToLevel(int)"""
        return Level._wrap(_Level.intToLevel(_int.valueOf(arg0)))

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

    @staticmethod
    @overload
    def values() -> List['Level']:
        """public static org.slf4j.event.Level[] org.slf4j.event.Level.values()"""
        return List[Level]._wrap(_Level.values())

    @overload
    def toInt(self) -> int:
        """public int org.slf4j.event.Level.toInt()"""
        return int._wrap(super(Level, self).toInt())

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

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.slf4j.event.Level.toString()"""
        return str._wrap(super(Level, self).toString()) 
 
 
# CLASS: org.slf4j.event.LoggingEvent
from builtins import str
import org.slf4j.event.LoggingEvent as _LoggingEvent
_LoggingEvent = _LoggingEvent
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
 
class LoggingEvent():
    """org.slf4j.event.LoggingEvent"""
 
    @staticmethod
    def _wrap(java_value: _LoggingEvent) -> 'LoggingEvent':
        return LoggingEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoggingEvent):
        """
        Dynamic initializer for LoggingEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoggingEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoggingEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getLevel(self, ):
        """public abstract org.slf4j.event.Level org.slf4j.event.LoggingEvent.getLevel()"""
        pass

    @abstractmethod
    def getThreadName(self, ):
        """public abstract java.lang.String org.slf4j.event.LoggingEvent.getThreadName()"""
        pass

    @abstractmethod
    def getMessage(self, ):
        """public abstract java.lang.String org.slf4j.event.LoggingEvent.getMessage()"""
        pass

    @abstractmethod
    def getArguments(self, ):
        """public abstract java.util.List<java.lang.Object> org.slf4j.event.LoggingEvent.getArguments()"""
        pass

    @abstractmethod
    def getKeyValuePairs(self, ):
        """public abstract java.util.List<org.slf4j.event.KeyValuePair> org.slf4j.event.LoggingEvent.getKeyValuePairs()"""
        pass

    @abstractmethod
    def getLoggerName(self, ):
        """public abstract java.lang.String org.slf4j.event.LoggingEvent.getLoggerName()"""
        pass

    @abstractmethod
    def getThrowable(self, ):
        """public abstract java.lang.Throwable org.slf4j.event.LoggingEvent.getThrowable()"""
        pass

    @abstractmethod
    def getMarkers(self, ):
        """public abstract java.util.List<org.slf4j.Marker> org.slf4j.event.LoggingEvent.getMarkers()"""
        pass

    @overload
    def getCallerBoundary(self) -> str:
        """public default java.lang.String org.slf4j.event.LoggingEvent.getCallerBoundary()"""
        return str._wrap(super(LoggingEvent, self).getCallerBoundary())

    @abstractmethod
    def getArgumentArray(self, ):
        """public abstract java.lang.Object[] org.slf4j.event.LoggingEvent.getArgumentArray()"""
        pass

    @abstractmethod
    def getTimeStamp(self, ):
        """public abstract long org.slf4j.event.LoggingEvent.getTimeStamp()"""
        pass 
 
 
# CLASS: org.slf4j.event.DefaultLoggingEvent
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.slf4j.event.DefaultLoggingEvent as _DefaultLoggingEvent
_DefaultLoggingEvent = _DefaultLoggingEvent
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = _import_once("slf4py")

import org.slf4j.event.Level as _Level
_Level = _Level
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultLoggingEvent():
    """org.slf4j.event.DefaultLoggingEvent"""
 
    @staticmethod
    def _wrap(java_value: _DefaultLoggingEvent) -> 'DefaultLoggingEvent':
        return DefaultLoggingEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultLoggingEvent):
        """
        Dynamic initializer for DefaultLoggingEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultLoggingEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultLoggingEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addKeyValue(self, arg0: str, arg1: object):
        """public void org.slf4j.event.DefaultLoggingEvent.addKeyValue(java.lang.String,java.lang.Object)"""
        super(_DefaultLoggingEvent, self).addKeyValue(arg0, arg1)

    @overload
    def addArguments(self, *arg0: object):
        """public void org.slf4j.event.DefaultLoggingEvent.addArguments(java.lang.Object...)"""
        super(_DefaultLoggingEvent, self).addArguments(arg0)

    @overload
    def setThrowable(self, arg0: 'Throwable'):
        """public void org.slf4j.event.DefaultLoggingEvent.setThrowable(java.lang.Throwable)"""
        super(_DefaultLoggingEvent, self).setThrowable(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getArguments(self) -> 'List':
        """public java.util.List<java.lang.Object> org.slf4j.event.DefaultLoggingEvent.getArguments()"""
        return 'List'._wrap(super(DefaultLoggingEvent, self).getArguments())

    @override
    @overload
    def getThreadName(self) -> str:
        """public java.lang.String org.slf4j.event.DefaultLoggingEvent.getThreadName()"""
        return str._wrap(super(DefaultLoggingEvent, self).getThreadName())

    @override
    @overload
    def getCallerBoundary(self) -> str:
        """public java.lang.String org.slf4j.event.DefaultLoggingEvent.getCallerBoundary()"""
        return str._wrap(super(DefaultLoggingEvent, self).getCallerBoundary())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def addMarker(self, arg0: 'Marker'):
        """public void org.slf4j.event.DefaultLoggingEvent.addMarker(org.slf4j.Marker)"""
        super(_DefaultLoggingEvent, self).addMarker(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Level', arg1: 'Logger'):
        """public org.slf4j.event.DefaultLoggingEvent(org.slf4j.event.Level,org.slf4j.Logger)"""
        val = _DefaultLoggingEvent(arg0, arg1)
        self.__wrapper = val

    @overload
    def setCallerBoundary(self, arg0: str):
        """public void org.slf4j.event.DefaultLoggingEvent.setCallerBoundary(java.lang.String)"""
        super(_DefaultLoggingEvent, self).setCallerBoundary(arg0)

    @override
    @overload
    def getMarkers(self) -> 'List':
        """public java.util.List<org.slf4j.Marker> org.slf4j.event.DefaultLoggingEvent.getMarkers()"""
        return 'List'._wrap(super(DefaultLoggingEvent, self).getMarkers())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.slf4j.event.DefaultLoggingEvent.getThrowable()"""
        return 'Throwable'._wrap(super(DefaultLoggingEvent, self).getThrowable())

    @overload
    def setTimeStamp(self, arg0: int):
        """public void org.slf4j.event.DefaultLoggingEvent.setTimeStamp(long)"""
        super(_DefaultLoggingEvent, self).setTimeStamp(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getLevel(self) -> 'Level':
        """public org.slf4j.event.Level org.slf4j.event.DefaultLoggingEvent.getLevel()"""
        return 'Level'._wrap(super(DefaultLoggingEvent, self).getLevel())

    @overload
    def addArgument(self, arg0: object):
        """public void org.slf4j.event.DefaultLoggingEvent.addArgument(java.lang.Object)"""
        super(_DefaultLoggingEvent, self).addArgument(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setMessage(self, arg0: str):
        """public void org.slf4j.event.DefaultLoggingEvent.setMessage(java.lang.String)"""
        super(_DefaultLoggingEvent, self).setMessage(arg0)

    @override
    @overload
    def getArgumentArray(self) -> List[object]:
        """public java.lang.Object[] org.slf4j.event.DefaultLoggingEvent.getArgumentArray()"""
        return List[object]._wrap(super(DefaultLoggingEvent, self).getArgumentArray())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getLoggerName(self) -> str:
        """public java.lang.String org.slf4j.event.DefaultLoggingEvent.getLoggerName()"""
        return str._wrap(super(DefaultLoggingEvent, self).getLoggerName())

    @override
    @overload
    def getTimeStamp(self) -> int:
        """public long org.slf4j.event.DefaultLoggingEvent.getTimeStamp()"""
        return int._wrap(super(DefaultLoggingEvent, self).getTimeStamp())

    @override
    @overload
    def getKeyValuePairs(self) -> 'List':
        """public java.util.List<org.slf4j.event.KeyValuePair> org.slf4j.event.DefaultLoggingEvent.getKeyValuePairs()"""
        return 'List'._wrap(super(DefaultLoggingEvent, self).getKeyValuePairs())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.slf4j.event.DefaultLoggingEvent.getMessage()"""
        return str._wrap(super(DefaultLoggingEvent, self).getMessage())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())