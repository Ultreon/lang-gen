from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import org.slf4j.event.SubstituteLoggingEvent as __SubstituteLoggingEvent
__SubstituteLoggingEvent = __SubstituteLoggingEvent
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
try:
    from slf4py import helpers
except ImportError:
    helpers = __import_once__("slf4py.helpers")

from builtins import object
from typing import List
import org.slf4j.event.Level as __Level
__Level = __Level
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.slf4j.event.LoggingEvent as __LoggingEvent
__LoggingEvent = __LoggingEvent
import java.lang.Object as __Object
__Object = __Object
import org.slf4j.helpers.SubstituteLogger as __SubstituteLogger
__SubstituteLogger = __SubstituteLogger
import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class SubstituteLoggingEvent():
    """org.slf4j.event.SubstituteLoggingEvent"""
 
    @staticmethod
    def __wrap(java_value: __SubstituteLoggingEvent) -> 'SubstituteLoggingEvent':
        return SubstituteLoggingEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SubstituteLoggingEvent):
        """
        Dynamic initializer for SubstituteLoggingEvent.
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
    def setLoggerName(self, arg0: str):
        """public void org.slf4j.event.SubstituteLoggingEvent.setLoggerName(java.lang.String)"""
        super(__SubstituteLoggingEvent, self).setLoggerName(arg0)

    @overload
    def getLogger(self) -> 'helpers.SubstituteLogger':
        """public org.slf4j.helpers.SubstituteLogger org.slf4j.event.SubstituteLoggingEvent.getLogger()"""
        return 'helpers.SubstituteLogger'.__wrap(super(SubstituteLoggingEvent, self).getLogger())

    @overload
    def setThreadName(self, arg0: str):
        """public void org.slf4j.event.SubstituteLoggingEvent.setThreadName(java.lang.String)"""
        super(__SubstituteLoggingEvent, self).setThreadName(arg0)

    @overload
    def __init__(self):
        """public org.slf4j.event.SubstituteLoggingEvent()"""
        val = __SubstituteLoggingEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setThrowable(self, arg0: 'Throwable'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setThrowable(java.lang.Throwable)"""
        super(__SubstituteLoggingEvent, self).setThrowable(arg0)

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.slf4j.event.SubstituteLoggingEvent.getMessage()"""
        return str.__wrap(super(SubstituteLoggingEvent, self).getMessage())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setLogger(self, arg0: 'SubstituteLogger'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setLogger(org.slf4j.helpers.SubstituteLogger)"""
        super(__SubstituteLoggingEvent, self).setLogger(arg0)

    @overload
    def addMarker(self, arg0: 'Marker'):
        """public void org.slf4j.event.SubstituteLoggingEvent.addMarker(org.slf4j.Marker)"""
        super(__SubstituteLoggingEvent, self).addMarker(arg0)

    @override
    @overload
    def getThreadName(self) -> str:
        """public java.lang.String org.slf4j.event.SubstituteLoggingEvent.getThreadName()"""
        return str.__wrap(super(SubstituteLoggingEvent, self).getThreadName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setMessage(self, arg0: str):
        """public void org.slf4j.event.SubstituteLoggingEvent.setMessage(java.lang.String)"""
        super(__SubstituteLoggingEvent, self).setMessage(arg0)

    @overload
    def setTimeStamp(self, arg0: int):
        """public void org.slf4j.event.SubstituteLoggingEvent.setTimeStamp(long)"""
        super(__SubstituteLoggingEvent, self).setTimeStamp(__long.valueOf(arg0))

    @override
    @overload
    def getArgumentArray(self) -> List[object]:
        """public java.lang.Object[] org.slf4j.event.SubstituteLoggingEvent.getArgumentArray()"""
        return List[object].__wrap(super(SubstituteLoggingEvent, self).getArgumentArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getArguments(self) -> 'List':
        """public java.util.List<java.lang.Object> org.slf4j.event.SubstituteLoggingEvent.getArguments()"""
        return 'List'.__wrap(super(SubstituteLoggingEvent, self).getArguments())

    @overload
    def setLevel(self, arg0: 'Level'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setLevel(org.slf4j.event.Level)"""
        super(__SubstituteLoggingEvent, self).setLevel(arg0)

    @overload
    def __init__(self, ):
        """public org.slf4j.event.SubstituteLoggingEvent()"""
        val = __SubstituteLoggingEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTimeStamp(self) -> int:
        """public long org.slf4j.event.SubstituteLoggingEvent.getTimeStamp()"""
        return int.__wrap(super(SubstituteLoggingEvent, self).getTimeStamp())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getKeyValuePairs(self) -> 'List':
        """public java.util.List<org.slf4j.event.KeyValuePair> org.slf4j.event.SubstituteLoggingEvent.getKeyValuePairs()"""
        return 'List'.__wrap(super(SubstituteLoggingEvent, self).getKeyValuePairs())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.slf4j.event.SubstituteLoggingEvent.getThrowable()"""
        return 'Throwable'.__wrap(super(SubstituteLoggingEvent, self).getThrowable())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCallerBoundary(self) -> str:
        """public default java.lang.String org.slf4j.event.LoggingEvent.getCallerBoundary()"""
        return str.__wrap(super(LoggingEvent, self).getCallerBoundary())

    @override
    @overload
    def getMarkers(self) -> 'List':
        """public java.util.List<org.slf4j.Marker> org.slf4j.event.SubstituteLoggingEvent.getMarkers()"""
        return 'List'.__wrap(super(SubstituteLoggingEvent, self).getMarkers())

    @override
    @overload
    def getLevel(self) -> 'Level':
        """public org.slf4j.event.Level org.slf4j.event.SubstituteLoggingEvent.getLevel()"""
        return 'Level'.__wrap(super(SubstituteLoggingEvent, self).getLevel())

    @overload
    def setArgumentArray(self, arg0: 'Object'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setArgumentArray(java.lang.Object[])"""
        super(__SubstituteLoggingEvent, self).setArgumentArray(arg0)

    @override
    @overload
    def getLoggerName(self) -> str:
        """public java.lang.String org.slf4j.event.SubstituteLoggingEvent.getLoggerName()"""
        return str.__wrap(super(SubstituteLoggingEvent, self).getLoggerName())

 
 
 
# CLASS: org.slf4j.event.SubstituteLoggingEvent
from pyquantum_helper import import_once as __import_once__
import org.slf4j.event.SubstituteLoggingEvent as __SubstituteLoggingEvent
__SubstituteLoggingEvent = __SubstituteLoggingEvent
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
try:
    from slf4py import helpers
except ImportError:
    helpers = __import_once__("slf4py.helpers")

from builtins import object
from typing import List
import org.slf4j.event.Level as __Level
__Level = __Level
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.slf4j.event.LoggingEvent as __LoggingEvent
__LoggingEvent = __LoggingEvent
import java.lang.Object as __Object
__Object = __Object
import org.slf4j.helpers.SubstituteLogger as __SubstituteLogger
__SubstituteLogger = __SubstituteLogger
import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class SubstituteLoggingEvent():
    """org.slf4j.event.SubstituteLoggingEvent"""
 
    @staticmethod
    def __wrap(java_value: __SubstituteLoggingEvent) -> 'SubstituteLoggingEvent':
        return SubstituteLoggingEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SubstituteLoggingEvent):
        """
        Dynamic initializer for SubstituteLoggingEvent.
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
    def setLoggerName(self, arg0: str):
        """public void org.slf4j.event.SubstituteLoggingEvent.setLoggerName(java.lang.String)"""
        super(__SubstituteLoggingEvent, self).setLoggerName(arg0)

    @overload
    def getLogger(self) -> 'helpers.SubstituteLogger':
        """public org.slf4j.helpers.SubstituteLogger org.slf4j.event.SubstituteLoggingEvent.getLogger()"""
        return 'helpers.SubstituteLogger'.__wrap(super(SubstituteLoggingEvent, self).getLogger())

    @overload
    def setThreadName(self, arg0: str):
        """public void org.slf4j.event.SubstituteLoggingEvent.setThreadName(java.lang.String)"""
        super(__SubstituteLoggingEvent, self).setThreadName(arg0)

    @overload
    def __init__(self):
        """public org.slf4j.event.SubstituteLoggingEvent()"""
        val = __SubstituteLoggingEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setThrowable(self, arg0: 'Throwable'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setThrowable(java.lang.Throwable)"""
        super(__SubstituteLoggingEvent, self).setThrowable(arg0)

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.slf4j.event.SubstituteLoggingEvent.getMessage()"""
        return str.__wrap(super(SubstituteLoggingEvent, self).getMessage())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setLogger(self, arg0: 'SubstituteLogger'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setLogger(org.slf4j.helpers.SubstituteLogger)"""
        super(__SubstituteLoggingEvent, self).setLogger(arg0)

    @overload
    def addMarker(self, arg0: 'Marker'):
        """public void org.slf4j.event.SubstituteLoggingEvent.addMarker(org.slf4j.Marker)"""
        super(__SubstituteLoggingEvent, self).addMarker(arg0)

    @override
    @overload
    def getThreadName(self) -> str:
        """public java.lang.String org.slf4j.event.SubstituteLoggingEvent.getThreadName()"""
        return str.__wrap(super(SubstituteLoggingEvent, self).getThreadName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setMessage(self, arg0: str):
        """public void org.slf4j.event.SubstituteLoggingEvent.setMessage(java.lang.String)"""
        super(__SubstituteLoggingEvent, self).setMessage(arg0)

    @overload
    def setTimeStamp(self, arg0: int):
        """public void org.slf4j.event.SubstituteLoggingEvent.setTimeStamp(long)"""
        super(__SubstituteLoggingEvent, self).setTimeStamp(__long.valueOf(arg0))

    @override
    @overload
    def getArgumentArray(self) -> List[object]:
        """public java.lang.Object[] org.slf4j.event.SubstituteLoggingEvent.getArgumentArray()"""
        return List[object].__wrap(super(SubstituteLoggingEvent, self).getArgumentArray())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getArguments(self) -> 'List':
        """public java.util.List<java.lang.Object> org.slf4j.event.SubstituteLoggingEvent.getArguments()"""
        return 'List'.__wrap(super(SubstituteLoggingEvent, self).getArguments())

    @overload
    def setLevel(self, arg0: 'Level'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setLevel(org.slf4j.event.Level)"""
        super(__SubstituteLoggingEvent, self).setLevel(arg0)

    @overload
    def __init__(self, ):
        """public org.slf4j.event.SubstituteLoggingEvent()"""
        val = __SubstituteLoggingEvent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTimeStamp(self) -> int:
        """public long org.slf4j.event.SubstituteLoggingEvent.getTimeStamp()"""
        return int.__wrap(super(SubstituteLoggingEvent, self).getTimeStamp())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getKeyValuePairs(self) -> 'List':
        """public java.util.List<org.slf4j.event.KeyValuePair> org.slf4j.event.SubstituteLoggingEvent.getKeyValuePairs()"""
        return 'List'.__wrap(super(SubstituteLoggingEvent, self).getKeyValuePairs())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.slf4j.event.SubstituteLoggingEvent.getThrowable()"""
        return 'Throwable'.__wrap(super(SubstituteLoggingEvent, self).getThrowable())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCallerBoundary(self) -> str:
        """public default java.lang.String org.slf4j.event.LoggingEvent.getCallerBoundary()"""
        return str.__wrap(super(LoggingEvent, self).getCallerBoundary())

    @override
    @overload
    def getMarkers(self) -> 'List':
        """public java.util.List<org.slf4j.Marker> org.slf4j.event.SubstituteLoggingEvent.getMarkers()"""
        return 'List'.__wrap(super(SubstituteLoggingEvent, self).getMarkers())

    @override
    @overload
    def getLevel(self) -> 'Level':
        """public org.slf4j.event.Level org.slf4j.event.SubstituteLoggingEvent.getLevel()"""
        return 'Level'.__wrap(super(SubstituteLoggingEvent, self).getLevel())

    @overload
    def setArgumentArray(self, arg0: 'Object'):
        """public void org.slf4j.event.SubstituteLoggingEvent.setArgumentArray(java.lang.Object[])"""
        super(__SubstituteLoggingEvent, self).setArgumentArray(arg0)

    @override
    @overload
    def getLoggerName(self) -> str:
        """public java.lang.String org.slf4j.event.SubstituteLoggingEvent.getLoggerName()"""
        return str.__wrap(super(SubstituteLoggingEvent, self).getLoggerName())

 
 
 
# CLASS: org.slf4j.event.SubstituteLoggingEvent 
 
 
# CLASS: org.slf4j.event.EventRecordingLogger
from pyquantum_helper import import_once as __import_once__
import org.slf4j.event.EventRecordingLogger as __EventRecordingLogger
__EventRecordingLogger = __EventRecordingLogger
from builtins import str
import org.slf4j.spi.LoggingEventBuilder as __LoggingEventBuilder
__LoggingEventBuilder = __LoggingEventBuilder
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from slf4py import spi
except ImportError:
    spi = __import_once__("slf4py.spi")

try:
    from slf4py import helpers
except ImportError:
    helpers = __import_once__("slf4py.helpers")

from builtins import object
import org.slf4j.helpers.AbstractLogger as __AbstractLogger
__AbstractLogger = __AbstractLogger
import java.util.Queue as Queue
import org.slf4j.Logger as __Logger
__Logger = __Logger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import org.slf4j.helpers.LegacyAbstractLogger as __LegacyAbstractLogger
__LegacyAbstractLogger = __LegacyAbstractLogger
import java.lang.Throwable as Throwable
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EventRecordingLogger():
    """org.slf4j.event.EventRecordingLogger"""
 
    @staticmethod
    def __wrap(java_value: __EventRecordingLogger) -> 'EventRecordingLogger':
        return EventRecordingLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventRecordingLogger):
        """
        Dynamic initializer for EventRecordingLogger.
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
    def error(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String)"""
        super(__helpers.AbstractLogger, self).error(arg0, arg1)

    @overload
    def isWarnEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isWarnEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__helpers.LegacyAbstractLogger, self).isWarnEnabled(arg0))

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public boolean org.slf4j.event.EventRecordingLogger.isTraceEnabled()"""
        return bool.__wrap(super(EventRecordingLogger, self).isTraceEnabled())

    @override
    @overload
    def error(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(__helpers.AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public boolean org.slf4j.event.EventRecordingLogger.isInfoEnabled()"""
        return bool.__wrap(super(EventRecordingLogger, self).isInfoEnabled())

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public boolean org.slf4j.event.EventRecordingLogger.isErrorEnabled()"""
        return bool.__wrap(super(EventRecordingLogger, self).isErrorEnabled())

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).error(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(__helpers.AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String)"""
        super(__helpers.AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.event.EventRecordingLogger.getName()"""
        return str.__wrap(super(EventRecordingLogger, self).getName())

    @override
    @overload
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(__helpers.AbstractLogger, self).trace(arg0, arg1)

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).atLevel(arg0))

    @overload
    def isTraceEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isTraceEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__helpers.LegacyAbstractLogger, self).isTraceEnabled(arg0))

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__helpers.AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def debug(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(__helpers.AbstractLogger, self).debug(arg0, arg1)

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool.__wrap(super(__slf4py.Logger, self).isEnabledForLevel(arg0))

    @override
    @overload
    def error(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String)"""
        super(__helpers.AbstractLogger, self).error(arg0)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public boolean org.slf4j.event.EventRecordingLogger.isWarnEnabled()"""
        return bool.__wrap(super(EventRecordingLogger, self).isWarnEnabled())

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).trace(arg0, arg1, arg2, arg3)

    @override
    @overload
    def debug(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String)"""
        super(__helpers.AbstractLogger, self).debug(arg0)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__helpers.AbstractLogger, self).warn(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def info(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String)"""
        super(__helpers.AbstractLogger, self).info(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).makeLoggingEventBuilder(arg0))

    @overload
    def isInfoEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isInfoEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__helpers.LegacyAbstractLogger, self).isInfoEnabled(arg0))

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).debug(arg0, arg1, arg2, arg3)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__helpers.AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String)"""
        super(__helpers.AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(__helpers.AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(__helpers.AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atTrace())

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__helpers.AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atDebug())

    @override
    @overload
    def trace(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String)"""
        super(__helpers.AbstractLogger, self).trace(arg0)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__helpers.AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(__helpers.AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atWarn()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atWarn())

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean org.slf4j.event.EventRecordingLogger.isDebugEnabled()"""
        return bool.__wrap(super(EventRecordingLogger, self).isDebugEnabled())

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__helpers.AbstractLogger, self).info(arg0, arg1, arg2)

    @overload
    def __init__(self, arg0: 'SubstituteLogger', arg1: 'Queue'):
        """public org.slf4j.event.EventRecordingLogger(org.slf4j.helpers.SubstituteLogger,java.util.Queue<org.slf4j.event.SubstituteLoggingEvent>)"""
        val = __EventRecordingLogger(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__helpers.AbstractLogger, self).debug(arg0, arg1, arg2)

    @overload
    def isDebugEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isDebugEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__helpers.LegacyAbstractLogger, self).isDebugEnabled(arg0))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String)"""
        super(__helpers.AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).info(arg0, arg1, arg2, arg3)

    @override
    @overload
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atError())

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__helpers.AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atInfo())

    @overload
    def isErrorEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isErrorEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__helpers.LegacyAbstractLogger, self).isErrorEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(__helpers.AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String)"""
        super(__helpers.AbstractLogger, self).warn(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__helpers.AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__helpers.AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(__helpers.AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).warn(arg0, arg1, arg2, arg3)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String)"""
        super(__helpers.AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__helpers.AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(__helpers.AbstractLogger, self).info(arg0, arg1) 
 
 
# CLASS: org.slf4j.event.DefaultLoggingEvent
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.slf4j.event.DefaultLoggingEvent as __DefaultLoggingEvent
__DefaultLoggingEvent = __DefaultLoggingEvent
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
from typing import List
import org.slf4j.event.Level as __Level
__Level = __Level
import java.util.List as __List
__List = __List
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
import java.util.List as List
from builtins import int
 
class DefaultLoggingEvent():
    """org.slf4j.event.DefaultLoggingEvent"""
 
    @staticmethod
    def __wrap(java_value: __DefaultLoggingEvent) -> 'DefaultLoggingEvent':
        return DefaultLoggingEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultLoggingEvent):
        """
        Dynamic initializer for DefaultLoggingEvent.
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
    def getLevel(self) -> 'Level':
        """public org.slf4j.event.Level org.slf4j.event.DefaultLoggingEvent.getLevel()"""
        return 'Level'.__wrap(super(DefaultLoggingEvent, self).getLevel())

    @overload
    def addKeyValue(self, arg0: str, arg1: object):
        """public void org.slf4j.event.DefaultLoggingEvent.addKeyValue(java.lang.String,java.lang.Object)"""
        super(__DefaultLoggingEvent, self).addKeyValue(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def addArguments(self, *arg0: object):
        """public void org.slf4j.event.DefaultLoggingEvent.addArguments(java.lang.Object...)"""
        super(__DefaultLoggingEvent, self).addArguments(arg0)

    @overload
    def setThrowable(self, arg0: 'Throwable'):
        """public void org.slf4j.event.DefaultLoggingEvent.setThrowable(java.lang.Throwable)"""
        super(__DefaultLoggingEvent, self).setThrowable(arg0)

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.slf4j.event.DefaultLoggingEvent.getThrowable()"""
        return 'Throwable'.__wrap(super(DefaultLoggingEvent, self).getThrowable())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getArgumentArray(self) -> List[object]:
        """public java.lang.Object[] org.slf4j.event.DefaultLoggingEvent.getArgumentArray()"""
        return List[object].__wrap(super(DefaultLoggingEvent, self).getArgumentArray())

    @override
    @overload
    def getArguments(self) -> 'List':
        """public java.util.List<java.lang.Object> org.slf4j.event.DefaultLoggingEvent.getArguments()"""
        return 'List'.__wrap(super(DefaultLoggingEvent, self).getArguments())

    @override
    @overload
    def getLoggerName(self) -> str:
        """public java.lang.String org.slf4j.event.DefaultLoggingEvent.getLoggerName()"""
        return str.__wrap(super(DefaultLoggingEvent, self).getLoggerName())

    @overload
    def setTimeStamp(self, arg0: int):
        """public void org.slf4j.event.DefaultLoggingEvent.setTimeStamp(long)"""
        super(__DefaultLoggingEvent, self).setTimeStamp(__long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTimeStamp(self) -> int:
        """public long org.slf4j.event.DefaultLoggingEvent.getTimeStamp()"""
        return int.__wrap(super(DefaultLoggingEvent, self).getTimeStamp())

    @override
    @overload
    def getCallerBoundary(self) -> str:
        """public java.lang.String org.slf4j.event.DefaultLoggingEvent.getCallerBoundary()"""
        return str.__wrap(super(DefaultLoggingEvent, self).getCallerBoundary())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def addMarker(self, arg0: 'Marker'):
        """public void org.slf4j.event.DefaultLoggingEvent.addMarker(org.slf4j.Marker)"""
        super(__DefaultLoggingEvent, self).addMarker(arg0)

    @overload
    def __init__(self, arg0: 'Level', arg1: 'Logger'):
        """public org.slf4j.event.DefaultLoggingEvent(org.slf4j.event.Level,org.slf4j.Logger)"""
        val = __DefaultLoggingEvent(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setCallerBoundary(self, arg0: str):
        """public void org.slf4j.event.DefaultLoggingEvent.setCallerBoundary(java.lang.String)"""
        super(__DefaultLoggingEvent, self).setCallerBoundary(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getKeyValuePairs(self) -> 'List':
        """public java.util.List<org.slf4j.event.KeyValuePair> org.slf4j.event.DefaultLoggingEvent.getKeyValuePairs()"""
        return 'List'.__wrap(super(DefaultLoggingEvent, self).getKeyValuePairs())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMarkers(self) -> 'List':
        """public java.util.List<org.slf4j.Marker> org.slf4j.event.DefaultLoggingEvent.getMarkers()"""
        return 'List'.__wrap(super(DefaultLoggingEvent, self).getMarkers())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.slf4j.event.DefaultLoggingEvent.getMessage()"""
        return str.__wrap(super(DefaultLoggingEvent, self).getMessage())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setMessage(self, arg0: str):
        """public void org.slf4j.event.DefaultLoggingEvent.setMessage(java.lang.String)"""
        super(__DefaultLoggingEvent, self).setMessage(arg0)

    @overload
    def addArgument(self, arg0: object):
        """public void org.slf4j.event.DefaultLoggingEvent.addArgument(java.lang.Object)"""
        super(__DefaultLoggingEvent, self).addArgument(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getThreadName(self) -> str:
        """public java.lang.String org.slf4j.event.DefaultLoggingEvent.getThreadName()"""
        return str.__wrap(super(DefaultLoggingEvent, self).getThreadName()) 
 
 
# CLASS: org.slf4j.event.LoggingEvent
from builtins import str
import org.slf4j.event.LoggingEvent as __LoggingEvent
__LoggingEvent = __LoggingEvent
import java.lang.String as __String
__String = __String
from abc import abstractmethod, ABC
 
class LoggingEvent(ABC):
    """org.slf4j.event.LoggingEvent"""
 
    @staticmethod
    def __wrap(java_value: __LoggingEvent) -> 'LoggingEvent':
        return LoggingEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggingEvent):
        """
        Dynamic initializer for LoggingEvent.
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

    @abstractmethod
    def getArgumentArray(self, ):
        """public abstract java.lang.Object[] org.slf4j.event.LoggingEvent.getArgumentArray()"""
        pass

    @abstractmethod
    def getTimeStamp(self, ):
        """public abstract long org.slf4j.event.LoggingEvent.getTimeStamp()"""
        pass

    @overload
    def getCallerBoundary(self) -> str:
        """public default java.lang.String org.slf4j.event.LoggingEvent.getCallerBoundary()"""
        return str.__wrap(super(LoggingEvent, self).getCallerBoundary()) 
 
 
# CLASS: org.slf4j.event.EventConstants
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import org.slf4j.event.EventConstants as __EventConstants
__EventConstants = __EventConstants
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EventConstants():
    """org.slf4j.event.EventConstants"""
 
    @staticmethod
    def __wrap(java_value: __EventConstants) -> 'EventConstants':
        return EventConstants(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventConstants):
        """
        Dynamic initializer for EventConstants.
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
    def __init__(self, ):
        """public org.slf4j.event.EventConstants()"""
        val = __EventConstants()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.slf4j.event.EventConstants()"""
        val = __EventConstants()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.slf4j.event.Level
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import org.slf4j.event.Level as __Level
__Level = __Level
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Level():
    """org.slf4j.event.Level"""
 
    @staticmethod
    def __wrap(java_value: __Level) -> 'Level':
        return Level(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Level):
        """
        Dynamic initializer for Level.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['Level']:
        """public static org.slf4j.event.Level[] org.slf4j.event.Level.values()"""
        return List[Level].__wrap(__Level.values())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toInt(self) -> int:
        """public int org.slf4j.event.Level.toInt()"""
        return int.__wrap(super(Level, self).toInt())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Level':
        """public static org.slf4j.event.Level org.slf4j.event.Level.valueOf(java.lang.String)"""
        return Level.__wrap(__Level.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def intToLevel(arg0: int) -> 'Level':
        """public static org.slf4j.event.Level org.slf4j.event.Level.intToLevel(int)"""
        return Level.__wrap(__Level.intToLevel(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.slf4j.event.Level.toString()"""
        return str.__wrap(super(Level, self).toString()) 
 
 
# CLASS: org.slf4j.event.KeyValuePair
from builtins import str
from pyquantum_helper import override
import org.slf4j.event.KeyValuePair as __KeyValuePair
__KeyValuePair = __KeyValuePair
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class KeyValuePair():
    """org.slf4j.event.KeyValuePair"""
 
    @staticmethod
    def __wrap(java_value: __KeyValuePair) -> 'KeyValuePair':
        return KeyValuePair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeyValuePair):
        """
        Dynamic initializer for KeyValuePair.
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
    def hashCode(self) -> int:
        """public int org.slf4j.event.KeyValuePair.hashCode()"""
        return int.__wrap(super(KeyValuePair, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.slf4j.event.KeyValuePair.toString()"""
        return str.__wrap(super(KeyValuePair, self).toString())

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
        """public boolean org.slf4j.event.KeyValuePair.equals(java.lang.Object)"""
        return bool.__wrap(super(__KeyValuePair, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: object):
        """public org.slf4j.event.KeyValuePair(java.lang.String,java.lang.Object)"""
        val = __KeyValuePair(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val