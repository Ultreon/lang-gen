from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
try:
    from slf4py import event
except ImportError:
    event = __import_once__("slf4py.event")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import org.slf4j.helpers.NormalizedParameters as __NormalizedParameters
__NormalizedParameters = __NormalizedParameters
from builtins import bool
from builtins import int
 
class NormalizedParameters():
    """org.slf4j.helpers.NormalizedParameters"""
 
    @staticmethod
    def __wrap(java_value: __NormalizedParameters) -> 'NormalizedParameters':
        return NormalizedParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NormalizedParameters):
        """
        Dynamic initializer for NormalizedParameters.
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

    @overload
    def __init__(self, arg0: str, arg1: 'Object'):
        """public org.slf4j.helpers.NormalizedParameters(java.lang.String,java.lang.Object[])"""
        val = __NormalizedParameters(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def normalize(arg0: 'LoggingEvent') -> 'NormalizedParameters':
        """public static org.slf4j.helpers.NormalizedParameters org.slf4j.helpers.NormalizedParameters.normalize(org.slf4j.event.LoggingEvent)"""
        return NormalizedParameters.__wrap(__NormalizedParameters.normalize(arg0))

    @staticmethod
    @overload
    def normalize(arg0: str, arg1: 'Object', arg2: 'Throwable') -> 'NormalizedParameters':
        """public static org.slf4j.helpers.NormalizedParameters org.slf4j.helpers.NormalizedParameters.normalize(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        return NormalizedParameters.__wrap(__NormalizedParameters.normalize(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getArguments(self) -> List[object]:
        """public java.lang.Object[] org.slf4j.helpers.NormalizedParameters.getArguments()"""
        return List[object].__wrap(super(NormalizedParameters, self).getArguments())

    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.slf4j.helpers.NormalizedParameters.getThrowable()"""
        return 'Throwable'.__wrap(super(NormalizedParameters, self).getThrowable())

    @staticmethod
    @overload
    def getThrowableCandidate(arg0: 'Object') -> 'Throwable':
        """public static java.lang.Throwable org.slf4j.helpers.NormalizedParameters.getThrowableCandidate(java.lang.Object[])"""
        return Throwable.__wrap(__NormalizedParameters.getThrowableCandidate(arg0))

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

    @overload
    def __init__(self, arg0: str, arg1: 'Object', arg2: 'Throwable'):
        """public org.slf4j.helpers.NormalizedParameters(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        val = __NormalizedParameters(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.slf4j.helpers.NormalizedParameters.getMessage()"""
        return str.__wrap(super(NormalizedParameters, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def trimmedCopy(arg0: 'Object') -> List[object]:
        """public static java.lang.Object[] org.slf4j.helpers.NormalizedParameters.trimmedCopy(java.lang.Object[])"""
        return List[object].__wrap(__NormalizedParameters.trimmedCopy(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.slf4j.helpers.NormalizedParameters
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
try:
    from slf4py import event
except ImportError:
    event = __import_once__("slf4py.event")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import org.slf4j.helpers.NormalizedParameters as __NormalizedParameters
__NormalizedParameters = __NormalizedParameters
from builtins import bool
from builtins import int
 
class NormalizedParameters():
    """org.slf4j.helpers.NormalizedParameters"""
 
    @staticmethod
    def __wrap(java_value: __NormalizedParameters) -> 'NormalizedParameters':
        return NormalizedParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NormalizedParameters):
        """
        Dynamic initializer for NormalizedParameters.
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

    @overload
    def __init__(self, arg0: str, arg1: 'Object'):
        """public org.slf4j.helpers.NormalizedParameters(java.lang.String,java.lang.Object[])"""
        val = __NormalizedParameters(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def normalize(arg0: 'LoggingEvent') -> 'NormalizedParameters':
        """public static org.slf4j.helpers.NormalizedParameters org.slf4j.helpers.NormalizedParameters.normalize(org.slf4j.event.LoggingEvent)"""
        return NormalizedParameters.__wrap(__NormalizedParameters.normalize(arg0))

    @staticmethod
    @overload
    def normalize(arg0: str, arg1: 'Object', arg2: 'Throwable') -> 'NormalizedParameters':
        """public static org.slf4j.helpers.NormalizedParameters org.slf4j.helpers.NormalizedParameters.normalize(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        return NormalizedParameters.__wrap(__NormalizedParameters.normalize(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getArguments(self) -> List[object]:
        """public java.lang.Object[] org.slf4j.helpers.NormalizedParameters.getArguments()"""
        return List[object].__wrap(super(NormalizedParameters, self).getArguments())

    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.slf4j.helpers.NormalizedParameters.getThrowable()"""
        return 'Throwable'.__wrap(super(NormalizedParameters, self).getThrowable())

    @staticmethod
    @overload
    def getThrowableCandidate(arg0: 'Object') -> 'Throwable':
        """public static java.lang.Throwable org.slf4j.helpers.NormalizedParameters.getThrowableCandidate(java.lang.Object[])"""
        return Throwable.__wrap(__NormalizedParameters.getThrowableCandidate(arg0))

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

    @overload
    def __init__(self, arg0: str, arg1: 'Object', arg2: 'Throwable'):
        """public org.slf4j.helpers.NormalizedParameters(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        val = __NormalizedParameters(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.slf4j.helpers.NormalizedParameters.getMessage()"""
        return str.__wrap(super(NormalizedParameters, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def trimmedCopy(arg0: 'Object') -> List[object]:
        """public static java.lang.Object[] org.slf4j.helpers.NormalizedParameters.trimmedCopy(java.lang.Object[])"""
        return List[object].__wrap(__NormalizedParameters.trimmedCopy(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.slf4j.helpers.NormalizedParameters 
 
 
# CLASS: org.slf4j.helpers.SubstituteLoggerFactory
from pyquantum_helper import import_once as __import_once__
import java.util.concurrent.LinkedBlockingQueue as LinkedBlockingQueue
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.LinkedBlockingQueue as __LinkedBlockingQueue
__LinkedBlockingQueue = __LinkedBlockingQueue
import org.slf4j.Logger as __Logger
__Logger = __Logger
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
import org.slf4j.helpers.SubstituteLoggerFactory as __SubstituteLoggerFactory
__SubstituteLoggerFactory = __SubstituteLoggerFactory
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class SubstituteLoggerFactory():
    """org.slf4j.helpers.SubstituteLoggerFactory"""
 
    @staticmethod
    def __wrap(java_value: __SubstituteLoggerFactory) -> 'SubstituteLoggerFactory':
        return SubstituteLoggerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SubstituteLoggerFactory):
        """
        Dynamic initializer for SubstituteLoggerFactory.
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
    def getEventQueue(self) -> 'LinkedBlockingQueue':
        """public java.util.concurrent.LinkedBlockingQueue<org.slf4j.event.SubstituteLoggingEvent> org.slf4j.helpers.SubstituteLoggerFactory.getEventQueue()"""
        return 'LinkedBlockingQueue'.__wrap(super(SubstituteLoggerFactory, self).getEventQueue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getLogger(self, arg0: str) -> 'slf4py.Logger':
        """public synchronized org.slf4j.Logger org.slf4j.helpers.SubstituteLoggerFactory.getLogger(java.lang.String)"""
        return 'slf4py.Logger'.__wrap(super(__SubstituteLoggerFactory, self).getLogger(arg0))

    @overload
    def postInitialization(self):
        """public void org.slf4j.helpers.SubstituteLoggerFactory.postInitialization()"""
        super(SubstituteLoggerFactory, self).postInitialization()

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

    @overload
    def clear(self):
        """public void org.slf4j.helpers.SubstituteLoggerFactory.clear()"""
        super(SubstituteLoggerFactory, self).clear()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getLoggers(self) -> 'List':
        """public java.util.List<org.slf4j.helpers.SubstituteLogger> org.slf4j.helpers.SubstituteLoggerFactory.getLoggers()"""
        return 'List'.__wrap(super(SubstituteLoggerFactory, self).getLoggers())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getLoggerNames(self) -> 'List':
        """public java.util.List<java.lang.String> org.slf4j.helpers.SubstituteLoggerFactory.getLoggerNames()"""
        return 'List'.__wrap(super(SubstituteLoggerFactory, self).getLoggerNames())

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
    def __init__(self, ):
        """public org.slf4j.helpers.SubstituteLoggerFactory()"""
        val = __SubstituteLoggerFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.slf4j.helpers.SubstituteLoggerFactory()"""
        val = __SubstituteLoggerFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.slf4j.helpers.ThreadLocalMapOfStacks
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Deque as Deque
import java.util.Deque as __Deque
__Deque = __Deque
import org.slf4j.helpers.ThreadLocalMapOfStacks as __ThreadLocalMapOfStacks
__ThreadLocalMapOfStacks = __ThreadLocalMapOfStacks
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
 
class ThreadLocalMapOfStacks():
    """org.slf4j.helpers.ThreadLocalMapOfStacks"""
 
    @staticmethod
    def __wrap(java_value: __ThreadLocalMapOfStacks) -> 'ThreadLocalMapOfStacks':
        return ThreadLocalMapOfStacks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadLocalMapOfStacks):
        """
        Dynamic initializer for ThreadLocalMapOfStacks.
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

    @overload
    def clearDequeByKey(self, arg0: str):
        """public void org.slf4j.helpers.ThreadLocalMapOfStacks.clearDequeByKey(java.lang.String)"""
        super(__ThreadLocalMapOfStacks, self).clearDequeByKey(arg0)

    @overload
    def pushByKey(self, arg0: str, arg1: str):
        """public void org.slf4j.helpers.ThreadLocalMapOfStacks.pushByKey(java.lang.String,java.lang.String)"""
        super(__ThreadLocalMapOfStacks, self).pushByKey(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.ThreadLocalMapOfStacks()"""
        val = __ThreadLocalMapOfStacks()
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

    @overload
    def __init__(self):
        """public org.slf4j.helpers.ThreadLocalMapOfStacks()"""
        val = __ThreadLocalMapOfStacks()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def popByKey(self, arg0: str) -> str:
        """public java.lang.String org.slf4j.helpers.ThreadLocalMapOfStacks.popByKey(java.lang.String)"""
        return str.__wrap(super(__ThreadLocalMapOfStacks, self).popByKey(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getCopyOfDequeByKey(self, arg0: str) -> 'Deque':
        """public java.util.Deque<java.lang.String> org.slf4j.helpers.ThreadLocalMapOfStacks.getCopyOfDequeByKey(java.lang.String)"""
        return 'Deque'.__wrap(super(__ThreadLocalMapOfStacks, self).getCopyOfDequeByKey(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.slf4j.helpers.SubstituteLogger
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.slf4j.spi.LoggingEventBuilder as __LoggingEventBuilder
__LoggingEventBuilder = __LoggingEventBuilder
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from slf4py import spi
except ImportError:
    spi = __import_once__("slf4py.spi")

from builtins import object
import java.util.Queue as Queue
import org.slf4j.Logger as __Logger
__Logger = __Logger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
try:
    from slf4py import event
except ImportError:
    event = __import_once__("slf4py.event")

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
from builtins import int
 
class SubstituteLogger():
    """org.slf4j.helpers.SubstituteLogger"""
 
    @staticmethod
    def __wrap(java_value: __SubstituteLogger) -> 'SubstituteLogger':
        return SubstituteLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SubstituteLogger):
        """
        Dynamic initializer for SubstituteLogger.
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
    def debug(self, arg0: str):
        """public void org.slf4j.helpers.SubstituteLogger.debug(java.lang.String)"""
        super(__SubstituteLogger, self).debug(arg0)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__SubstituteLogger, self).error(arg0, arg1, arg2)

    @overload
    def delegate(self) -> 'slf4py.Logger':
        """public org.slf4j.Logger org.slf4j.helpers.SubstituteLogger.delegate()"""
        return 'slf4py.Logger'.__wrap(super(SubstituteLogger, self).delegate())

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isTraceEnabled()"""
        return bool.__wrap(super(SubstituteLogger, self).isTraceEnabled())

    @override
    @overload
    def trace(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(java.lang.String,java.lang.Object)"""
        super(__SubstituteLogger, self).trace(arg0, arg1)

    @override
    @overload
    def isWarnEnabled(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isWarnEnabled()"""
        return bool.__wrap(super(SubstituteLogger, self).isWarnEnabled())

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__SubstituteLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__SubstituteLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__SubstituteLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__SubstituteLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__SubstituteLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__SubstituteLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isDebugEnabled()"""
        return bool.__wrap(super(SubstituteLogger, self).isDebugEnabled())

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__SubstituteLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.SubstituteLogger.info(org.slf4j.Marker,java.lang.String)"""
        super(__SubstituteLogger, self).info(arg0, arg1)

    @overload
    def isDelegateEventAware(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isDelegateEventAware()"""
        return bool.__wrap(super(SubstituteLogger, self).isDelegateEventAware())

    @overload
    def isErrorEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isErrorEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__SubstituteLogger, self).isErrorEnabled(arg0))

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.SubstituteLogger.trace(org.slf4j.Marker,java.lang.String)"""
        super(__SubstituteLogger, self).trace(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(java.lang.String,java.lang.Object...)"""
        super(__SubstituteLogger, self).debug(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(java.lang.String,java.lang.Object...)"""
        super(__SubstituteLogger, self).trace(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.error(java.lang.String,java.lang.Throwable)"""
        super(__SubstituteLogger, self).error(arg0, arg1)

    @overload
    def log(self, arg0: 'LoggingEvent'):
        """public void org.slf4j.helpers.SubstituteLogger.log(org.slf4j.event.LoggingEvent)"""
        super(__SubstituteLogger, self).log(arg0)

    @override
    @overload
    def trace(self, arg0: str):
        """public void org.slf4j.helpers.SubstituteLogger.trace(java.lang.String)"""
        super(__SubstituteLogger, self).trace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setDelegate(self, arg0: 'Logger'):
        """public void org.slf4j.helpers.SubstituteLogger.setDelegate(org.slf4j.Logger)"""
        super(__SubstituteLogger, self).setDelegate(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.helpers.SubstituteLogger.getName()"""
        return str.__wrap(super(SubstituteLogger, self).getName())

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__SubstituteLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__SubstituteLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str):
        """public void org.slf4j.helpers.SubstituteLogger.warn(java.lang.String)"""
        super(__SubstituteLogger, self).warn(arg0)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__SubstituteLogger, self).info(arg0, arg1, arg2, arg3)

    @override
    @overload
    def warn(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(java.lang.String,java.lang.Object...)"""
        super(__SubstituteLogger, self).warn(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.info(java.lang.String,java.lang.Throwable)"""
        super(__SubstituteLogger, self).info(arg0, arg1)

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool.__wrap(super(__SubstituteLogger, self).isEnabledForLevel(arg0))

    @overload
    def isDelegateNull(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isDelegateNull()"""
        return bool.__wrap(super(SubstituteLogger, self).isDelegateNull())

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.SubstituteLogger.warn(org.slf4j.Marker,java.lang.String)"""
        super(__SubstituteLogger, self).warn(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__SubstituteLogger, self).debug(arg0, arg1, arg2, arg3)

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__SubstituteLogger, self).makeLoggingEventBuilder(arg0))

    @override
    @overload
    def info(self, arg0: str):
        """public void org.slf4j.helpers.SubstituteLogger.info(java.lang.String)"""
        super(__SubstituteLogger, self).info(arg0)

    @overload
    def isDebugEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isDebugEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__SubstituteLogger, self).isDebugEnabled(arg0))

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atTrace()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(SubstituteLogger, self).atTrace())

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__SubstituteLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def info(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(java.lang.String,java.lang.Object...)"""
        super(__SubstituteLogger, self).info(arg0, arg1)

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atError()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(SubstituteLogger, self).atError())

    @override
    @overload
    def error(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(java.lang.String,java.lang.Object...)"""
        super(__SubstituteLogger, self).error(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(java.lang.String,java.lang.Object)"""
        super(__SubstituteLogger, self).debug(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(java.lang.String,java.lang.Object)"""
        super(__SubstituteLogger, self).error(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__SubstituteLogger, self).error(arg0, arg1, arg2, arg3)

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(java.lang.String,java.lang.Object)"""
        super(__SubstituteLogger, self).info(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.slf4j.helpers.SubstituteLogger.hashCode()"""
        return int.__wrap(super(SubstituteLogger, self).hashCode())

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(java.lang.String,java.lang.Object)"""
        super(__SubstituteLogger, self).warn(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__SubstituteLogger, self).trace(arg0, arg1, arg2, arg3)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__SubstituteLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(__SubstituteLogger, self).trace(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str):
        """public void org.slf4j.helpers.SubstituteLogger.error(java.lang.String)"""
        super(__SubstituteLogger, self).error(arg0)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__SubstituteLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__SubstituteLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__SubstituteLogger, self).warn(arg0, arg1, arg2, arg3)

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isErrorEnabled()"""
        return bool.__wrap(super(SubstituteLogger, self).isErrorEnabled())

    @overload
    def isDelegateNOP(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isDelegateNOP()"""
        return bool.__wrap(super(SubstituteLogger, self).isDelegateNOP())

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.SubstituteLogger.error(org.slf4j.Marker,java.lang.String)"""
        super(__SubstituteLogger, self).error(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__SubstituteLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.SubstituteLogger.debug(org.slf4j.Marker,java.lang.String)"""
        super(__SubstituteLogger, self).debug(arg0, arg1)

    @overload
    def isWarnEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isWarnEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__SubstituteLogger, self).isWarnEnabled(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Queue', arg2: bool):
        """public org.slf4j.helpers.SubstituteLogger(java.lang.String,java.util.Queue<org.slf4j.event.SubstituteLoggingEvent>,boolean)"""
        val = __SubstituteLogger(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isInfoEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isInfoEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__SubstituteLogger, self).isInfoEnabled(arg0))

    @override
    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atWarn()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(SubstituteLogger, self).atWarn())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__SubstituteLogger, self).warn(arg0, arg1, arg2)

    @overload
    def isTraceEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isTraceEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__SubstituteLogger, self).isTraceEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(__SubstituteLogger, self).warn(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__SubstituteLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atDebug()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(SubstituteLogger, self).atDebug())

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__SubstituteLogger, self).atLevel(arg0))

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public org.slf4j.spi.LoggingEventBuilder org.slf4j.helpers.SubstituteLogger.atInfo()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(SubstituteLogger, self).atInfo())

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.isInfoEnabled()"""
        return bool.__wrap(super(SubstituteLogger, self).isInfoEnabled())

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__SubstituteLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__SubstituteLogger, self).error(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.slf4j.helpers.SubstituteLogger.equals(java.lang.Object)"""
        return bool.__wrap(super(__SubstituteLogger, self).equals(arg0))

    @override
    @overload
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.SubstituteLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__SubstituteLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.SubstituteLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(__SubstituteLogger, self).debug(arg0, arg1) 
 
 
# CLASS: org.slf4j.helpers.NOPMDCAdapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Deque as Deque
import java.util.Deque as __Deque
__Deque = __Deque
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.slf4j.helpers.NOPMDCAdapter as __NOPMDCAdapter
__NOPMDCAdapter = __NOPMDCAdapter
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class NOPMDCAdapter():
    """org.slf4j.helpers.NOPMDCAdapter"""
 
    @staticmethod
    def __wrap(java_value: __NOPMDCAdapter) -> 'NOPMDCAdapter':
        return NOPMDCAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NOPMDCAdapter):
        """
        Dynamic initializer for NOPMDCAdapter.
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

    @overload
    def __init__(self):
        """public org.slf4j.helpers.NOPMDCAdapter()"""
        val = __NOPMDCAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def put(self, arg0: str, arg1: str):
        """public void org.slf4j.helpers.NOPMDCAdapter.put(java.lang.String,java.lang.String)"""
        super(__NOPMDCAdapter, self).put(arg0, arg1)

    @overload
    def get(self, arg0: str) -> str:
        """public java.lang.String org.slf4j.helpers.NOPMDCAdapter.get(java.lang.String)"""
        return str.__wrap(super(__NOPMDCAdapter, self).get(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def popByKey(self, arg0: str) -> str:
        """public java.lang.String org.slf4j.helpers.NOPMDCAdapter.popByKey(java.lang.String)"""
        return str.__wrap(super(__NOPMDCAdapter, self).popByKey(arg0))

    @overload
    def getCopyOfDequeByKey(self, arg0: str) -> 'Deque':
        """public java.util.Deque<java.lang.String> org.slf4j.helpers.NOPMDCAdapter.getCopyOfDequeByKey(java.lang.String)"""
        return 'Deque'.__wrap(super(__NOPMDCAdapter, self).getCopyOfDequeByKey(arg0))

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
    def remove(self, arg0: str):
        """public void org.slf4j.helpers.NOPMDCAdapter.remove(java.lang.String)"""
        super(__NOPMDCAdapter, self).remove(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def clearDequeByKey(self, arg0: str):
        """public void org.slf4j.helpers.NOPMDCAdapter.clearDequeByKey(java.lang.String)"""
        super(__NOPMDCAdapter, self).clearDequeByKey(arg0)

    @override
    @overload
    def getCopyOfContextMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.slf4j.helpers.NOPMDCAdapter.getCopyOfContextMap()"""
        return 'Map'.__wrap(super(NOPMDCAdapter, self).getCopyOfContextMap())

    @override
    @overload
    def clear(self):
        """public void org.slf4j.helpers.NOPMDCAdapter.clear()"""
        super(NOPMDCAdapter, self).clear()

    @override
    @overload
    def setContextMap(self, arg0: 'Map'):
        """public void org.slf4j.helpers.NOPMDCAdapter.setContextMap(java.util.Map<java.lang.String, java.lang.String>)"""
        super(__NOPMDCAdapter, self).setContextMap(arg0)

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

    @override
    @overload
    def pushByKey(self, arg0: str, arg1: str):
        """public void org.slf4j.helpers.NOPMDCAdapter.pushByKey(java.lang.String,java.lang.String)"""
        super(__NOPMDCAdapter, self).pushByKey(arg0, arg1)

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.NOPMDCAdapter()"""
        val = __NOPMDCAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.slf4j.helpers.NOPLogger
from pyquantum_helper import import_once as __import_once__
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

from builtins import object
import org.slf4j.Logger as __Logger
__Logger = __Logger
import java.lang.Long as __long
import org.slf4j.helpers.NOPLogger as __NOPLogger
__NOPLogger = __NOPLogger
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
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
 
class NOPLogger():
    """org.slf4j.helpers.NOPLogger"""
 
    @staticmethod
    def __wrap(java_value: __NOPLogger) -> 'NOPLogger':
        return NOPLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NOPLogger):
        """
        Dynamic initializer for NOPLogger.
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
    def isWarnEnabled(self) -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isWarnEnabled()"""
        return bool.__wrap(super(NOPLogger, self).isWarnEnabled())

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__NOPLogger, self).warn(arg0, arg1, arg2, arg3)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__NOPLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, *arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(java.lang.String,java.lang.Object...)"""
        super(__NOPLogger, self).warn(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(java.lang.String,java.lang.Object)"""
        super(__NOPLogger, self).debug(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isInfoEnabled(self) -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isInfoEnabled()"""
        return bool.__wrap(super(NOPLogger, self).isInfoEnabled())

    @overload
    def isInfoEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.NOPLogger.isInfoEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__NOPLogger, self).isInfoEnabled(arg0))

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.info(java.lang.String,java.lang.Throwable)"""
        super(__NOPLogger, self).info(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str):
        """public final void org.slf4j.helpers.NOPLogger.info(java.lang.String)"""
        super(__NOPLogger, self).info(arg0)

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).atLevel(arg0))

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__NOPLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def error(self, arg0: str):
        """public final void org.slf4j.helpers.NOPLogger.error(java.lang.String)"""
        super(__NOPLogger, self).error(arg0)

    @override
    @overload
    def trace(self, arg0: str, *arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(java.lang.String,java.lang.Object...)"""
        super(__NOPLogger, self).trace(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__NOPLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.helpers.NOPLogger.getName()"""
        return str.__wrap(super(NOPLogger, self).getName())

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool.__wrap(super(__slf4py.Logger, self).isEnabledForLevel(arg0))

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__NOPLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, *arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(java.lang.String,java.lang.Object...)"""
        super(__NOPLogger, self).debug(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def isErrorEnabled(self, arg0: 'Marker') -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isErrorEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__NOPLogger, self).isErrorEnabled(arg0))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public final void org.slf4j.helpers.NOPLogger.debug(org.slf4j.Marker,java.lang.String)"""
        super(__NOPLogger, self).debug(arg0, arg1)

    @override
    @overload
    def isDebugEnabled(self) -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isDebugEnabled()"""
        return bool.__wrap(super(NOPLogger, self).isDebugEnabled())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.info(java.lang.String,java.lang.Object)"""
        super(__NOPLogger, self).info(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__NOPLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__NOPLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__NOPLogger, self).warn(arg0, arg1, arg2)

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).makeLoggingEventBuilder(arg0))

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__NOPLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public final void org.slf4j.helpers.NOPLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__NOPLogger, self).error(arg0, arg1, arg2, arg3)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__NOPLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__NOPLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__NOPLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str):
        """public final void org.slf4j.helpers.NOPLogger.error(org.slf4j.Marker,java.lang.String)"""
        super(__NOPLogger, self).error(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__NOPLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__NOPLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str):
        """public final void org.slf4j.helpers.NOPLogger.debug(java.lang.String)"""
        super(__NOPLogger, self).debug(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def warn(self, arg0: str):
        """public final void org.slf4j.helpers.NOPLogger.warn(java.lang.String)"""
        super(__NOPLogger, self).warn(arg0)

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__NOPLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.warn(java.lang.String,java.lang.Object)"""
        super(__NOPLogger, self).warn(arg0, arg1)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public final void org.slf4j.helpers.NOPLogger.info(org.slf4j.Marker,java.lang.String)"""
        super(__NOPLogger, self).info(arg0, arg1)

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atTrace())

    @override
    @overload
    def info(self, arg0: str, arg1: object, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__NOPLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__NOPLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atDebug())

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__NOPLogger, self).trace(arg0, arg1, arg2, arg3)

    @override
    @overload
    def isTraceEnabled(self) -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isTraceEnabled()"""
        return bool.__wrap(super(NOPLogger, self).isTraceEnabled())

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

    @overload
    def isDebugEnabled(self, arg0: 'Marker') -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isDebugEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__NOPLogger, self).isDebugEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(__NOPLogger, self).warn(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(__NOPLogger, self).trace(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str, arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.trace(java.lang.String,java.lang.Object)"""
        super(__NOPLogger, self).trace(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.error(java.lang.String,java.lang.Throwable)"""
        super(__NOPLogger, self).error(arg0, arg1)

    @overload
    def isWarnEnabled(self, arg0: 'Marker') -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isWarnEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__NOPLogger, self).isWarnEnabled(arg0))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__NOPLogger, self).debug(arg0, arg1, arg2, arg3)

    @override
    @overload
    def info(self, arg0: str, *arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.info(java.lang.String,java.lang.Object...)"""
        super(__NOPLogger, self).info(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(__NOPLogger, self).debug(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__NOPLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public final void org.slf4j.helpers.NOPLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__NOPLogger, self).info(arg0, arg1, arg2, arg3)

    @override
    @overload
    def isErrorEnabled(self) -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isErrorEnabled()"""
        return bool.__wrap(super(NOPLogger, self).isErrorEnabled())

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atError())

    @override
    @overload
    def trace(self, arg0: str):
        """public final void org.slf4j.helpers.NOPLogger.trace(java.lang.String)"""
        super(__NOPLogger, self).trace(arg0)

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atInfo())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public final void org.slf4j.helpers.NOPLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__NOPLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def error(self, arg0: str, *arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.error(java.lang.String,java.lang.Object...)"""
        super(__NOPLogger, self).error(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public final void org.slf4j.helpers.NOPLogger.error(java.lang.String,java.lang.Object)"""
        super(__NOPLogger, self).error(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public final void org.slf4j.helpers.NOPLogger.warn(org.slf4j.Marker,java.lang.String)"""
        super(__NOPLogger, self).warn(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__NOPLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public final void org.slf4j.helpers.NOPLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__NOPLogger, self).error(arg0, arg1, arg2)

    @overload
    def isTraceEnabled(self, arg0: 'Marker') -> bool:
        """public final boolean org.slf4j.helpers.NOPLogger.isTraceEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__NOPLogger, self).isTraceEnabled(arg0))

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public final void org.slf4j.helpers.NOPLogger.trace(org.slf4j.Marker,java.lang.String)"""
        super(__NOPLogger, self).trace(arg0, arg1) 
 
 
# CLASS: org.slf4j.helpers.BasicMarkerFactory
from pyquantum_helper import import_once as __import_once__
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
import org.slf4j.helpers.BasicMarkerFactory as __BasicMarkerFactory
__BasicMarkerFactory = __BasicMarkerFactory
import java.lang.Object as __Object
__Object = __Object
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BasicMarkerFactory():
    """org.slf4j.helpers.BasicMarkerFactory"""
 
    @staticmethod
    def __wrap(java_value: __BasicMarkerFactory) -> 'BasicMarkerFactory':
        return BasicMarkerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BasicMarkerFactory):
        """
        Dynamic initializer for BasicMarkerFactory.
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
        """public org.slf4j.helpers.BasicMarkerFactory()"""
        val = __BasicMarkerFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def detachMarker(self, arg0: str) -> bool:
        """public boolean org.slf4j.helpers.BasicMarkerFactory.detachMarker(java.lang.String)"""
        return bool.__wrap(super(__BasicMarkerFactory, self).detachMarker(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getDetachedMarker(self, arg0: str) -> 'slf4py.Marker':
        """public org.slf4j.Marker org.slf4j.helpers.BasicMarkerFactory.getDetachedMarker(java.lang.String)"""
        return 'slf4py.Marker'.__wrap(super(__BasicMarkerFactory, self).getDetachedMarker(arg0))

    @overload
    def exists(self, arg0: str) -> bool:
        """public boolean org.slf4j.helpers.BasicMarkerFactory.exists(java.lang.String)"""
        return bool.__wrap(super(__BasicMarkerFactory, self).exists(arg0))

    @overload
    def getMarker(self, arg0: str) -> 'slf4py.Marker':
        """public org.slf4j.Marker org.slf4j.helpers.BasicMarkerFactory.getMarker(java.lang.String)"""
        return 'slf4py.Marker'.__wrap(super(__BasicMarkerFactory, self).getMarker(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.BasicMarkerFactory()"""
        val = __BasicMarkerFactory()
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.slf4j.helpers.FormattingTuple
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
from typing import List
import org.slf4j.helpers.FormattingTuple as __FormattingTuple
__FormattingTuple = __FormattingTuple
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FormattingTuple():
    """org.slf4j.helpers.FormattingTuple"""
 
    @staticmethod
    def __wrap(java_value: __FormattingTuple) -> 'FormattingTuple':
        return FormattingTuple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FormattingTuple):
        """
        Dynamic initializer for FormattingTuple.
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
    def __init__(self, arg0: str):
        """public org.slf4j.helpers.FormattingTuple(java.lang.String)"""
        val = __FormattingTuple(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getArgArray(self) -> List[object]:
        """public java.lang.Object[] org.slf4j.helpers.FormattingTuple.getArgArray()"""
        return List[object].__wrap(super(FormattingTuple, self).getArgArray())

    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.slf4j.helpers.FormattingTuple.getThrowable()"""
        return 'Throwable'.__wrap(super(FormattingTuple, self).getThrowable())

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

    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.slf4j.helpers.FormattingTuple.getMessage()"""
        return str.__wrap(super(FormattingTuple, self).getMessage())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: 'Object', arg2: 'Throwable'):
        """public org.slf4j.helpers.FormattingTuple(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        val = __FormattingTuple(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: org.slf4j.helpers.AbstractLogger
from pyquantum_helper import import_once as __import_once__
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

from builtins import object
from abc import abstractmethod, ABC
import org.slf4j.helpers.AbstractLogger as __AbstractLogger
__AbstractLogger = __AbstractLogger
import org.slf4j.Logger as __Logger
__Logger = __Logger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
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
 
class AbstractLogger(ABC):
    """org.slf4j.helpers.AbstractLogger"""
 
    @staticmethod
    def __wrap(java_value: __AbstractLogger) -> 'AbstractLogger':
        return AbstractLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractLogger):
        """
        Dynamic initializer for AbstractLogger.
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
    def isTraceEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isTraceEnabled(org.slf4j.Marker)"""
        pass

    @override
    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(arg0, arg1, arg2)

    @abstractmethod
    def isInfoEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isInfoEnabled(org.slf4j.Marker)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).info(arg0, arg1)

    @abstractmethod
    def isDebugEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled(org.slf4j.Marker)"""
        pass

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).atLevel(arg0))

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def isDebugEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled()"""
        pass

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).warn(arg0, arg1)

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool.__wrap(super(__slf4py.Logger, self).isEnabledForLevel(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(arg0, arg1, arg2, arg3)

    @override
    @overload
    def debug(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String)"""
        super(__AbstractLogger, self).debug(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).trace(arg0, arg1, arg2)

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).makeLoggingEventBuilder(arg0))

    @override
    @overload
    def info(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String)"""
        super(__AbstractLogger, self).info(arg0)

    @override
    @overload
    def trace(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(arg0, arg1, arg2)

    @overload
    def __init__(self):
        """public org.slf4j.helpers.AbstractLogger()"""
        val = __AbstractLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).info(arg0, arg1)

    @abstractmethod
    def isInfoEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isInfoEnabled()"""
        pass

    @abstractmethod
    def isWarnEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled(org.slf4j.Marker)"""
        pass

    @override
    @overload
    def warn(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String)"""
        super(__AbstractLogger, self).warn(arg0)

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.AbstractLogger()"""
        val = __AbstractLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def debug(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).debug(arg0, arg1)

    @abstractmethod
    def isErrorEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isErrorEnabled()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).debug(arg0, arg1, arg2)

    @abstractmethod
    def isErrorEnabled(self, arg0: 'Marker'):
        """public abstract boolean org.slf4j.Logger.isErrorEnabled(org.slf4j.Marker)"""
        pass

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atTrace())

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(arg0, arg1, arg2)

    @abstractmethod
    def isTraceEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isTraceEnabled()"""
        pass

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atDebug())

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).error(arg0, arg1)

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
    def error(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.helpers.AbstractLogger.getName()"""
        return str.__wrap(super(AbstractLogger, self).getName())

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(arg0, arg1, arg2, arg3)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(arg0, arg1, arg2, arg3)

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String)"""
        super(__AbstractLogger, self).error(arg0)

    @override
    @overload
    def trace(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String)"""
        super(__AbstractLogger, self).trace(arg0)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(arg0, arg1, arg2, arg3)

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atError())

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atInfo())

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).debug(arg0, arg1)

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
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(arg0, arg1, arg2, arg3)

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled()"""
        pass 
 
 
# CLASS: org.slf4j.helpers.NOP_FallbackServiceProvider
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.slf4j.spi.MDCAdapter as __MDCAdapter
__MDCAdapter = __MDCAdapter
try:
    from slf4py import spi
except ImportError:
    spi = __import_once__("slf4py.spi")

import org.slf4j.ILoggerFactory as __ILoggerFactory
__ILoggerFactory = __ILoggerFactory
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.slf4j.helpers.NOP_FallbackServiceProvider as __NOP_FallbackServiceProvider
__NOP_FallbackServiceProvider = __NOP_FallbackServiceProvider
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import org.slf4j.IMarkerFactory as __IMarkerFactory
__IMarkerFactory = __IMarkerFactory
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NOP_FallbackServiceProvider():
    """org.slf4j.helpers.NOP_FallbackServiceProvider"""
 
    @staticmethod
    def __wrap(java_value: __NOP_FallbackServiceProvider) -> 'NOP_FallbackServiceProvider':
        return NOP_FallbackServiceProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NOP_FallbackServiceProvider):
        """
        Dynamic initializer for NOP_FallbackServiceProvider.
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
    def getMDCAdapter(self) -> 'spi.MDCAdapter':
        """public org.slf4j.spi.MDCAdapter org.slf4j.helpers.NOP_FallbackServiceProvider.getMDCAdapter()"""
        return 'spi.MDCAdapter'.__wrap(super(NOP_FallbackServiceProvider, self).getMDCAdapter())

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getLoggerFactory(self) -> 'slf4py.ILoggerFactory':
        """public org.slf4j.ILoggerFactory org.slf4j.helpers.NOP_FallbackServiceProvider.getLoggerFactory()"""
        return 'slf4py.ILoggerFactory'.__wrap(super(NOP_FallbackServiceProvider, self).getLoggerFactory())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.NOP_FallbackServiceProvider()"""
        val = __NOP_FallbackServiceProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def initialize(self):
        """public void org.slf4j.helpers.NOP_FallbackServiceProvider.initialize()"""
        super(NOP_FallbackServiceProvider, self).initialize()

    @override
    @overload
    def getRequestedApiVersion(self) -> str:
        """public java.lang.String org.slf4j.helpers.NOP_FallbackServiceProvider.getRequestedApiVersion()"""
        return str.__wrap(super(NOP_FallbackServiceProvider, self).getRequestedApiVersion())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getMarkerFactory(self) -> 'slf4py.IMarkerFactory':
        """public org.slf4j.IMarkerFactory org.slf4j.helpers.NOP_FallbackServiceProvider.getMarkerFactory()"""
        return 'slf4py.IMarkerFactory'.__wrap(super(NOP_FallbackServiceProvider, self).getMarkerFactory())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.slf4j.helpers.NOP_FallbackServiceProvider()"""
        val = __NOP_FallbackServiceProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.slf4j.helpers.BasicMarker
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.slf4j.helpers.BasicMarker as __BasicMarker
__BasicMarker = __BasicMarker
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Iterator as Iterator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BasicMarker():
    """org.slf4j.helpers.BasicMarker"""
 
    @staticmethod
    def __wrap(java_value: __BasicMarker) -> 'BasicMarker':
        return BasicMarker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BasicMarker):
        """
        Dynamic initializer for BasicMarker.
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
    def hashCode(self) -> int:
        """public int org.slf4j.helpers.BasicMarker.hashCode()"""
        return int.__wrap(super(BasicMarker, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.equals(java.lang.Object)"""
        return bool.__wrap(super(__BasicMarker, self).equals(arg0))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.contains(java.lang.String)"""
        return bool.__wrap(super(__BasicMarker, self).contains(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.slf4j.helpers.BasicMarker.toString()"""
        return str.__wrap(super(BasicMarker, self).toString())

    @overload
    def contains(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.contains(org.slf4j.Marker)"""
        return bool.__wrap(super(__BasicMarker, self).contains(arg0))

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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<org.slf4j.Marker> org.slf4j.helpers.BasicMarker.iterator()"""
        return 'Iterator'.__wrap(super(BasicMarker, self).iterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def add(self, arg0: 'Marker'):
        """public void org.slf4j.helpers.BasicMarker.add(org.slf4j.Marker)"""
        super(__BasicMarker, self).add(arg0)

    @override
    @overload
    def hasReferences(self) -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.hasReferences()"""
        return bool.__wrap(super(BasicMarker, self).hasReferences())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.helpers.BasicMarker.getName()"""
        return str.__wrap(super(BasicMarker, self).getName())

    @override
    @overload
    def hasChildren(self) -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.hasChildren()"""
        return bool.__wrap(super(BasicMarker, self).hasChildren())

    @overload
    def remove(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.BasicMarker.remove(org.slf4j.Marker)"""
        return bool.__wrap(super(__BasicMarker, self).remove(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.slf4j.helpers.MarkerIgnoringBase
from pyquantum_helper import import_once as __import_once__
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

from builtins import object
from abc import abstractmethod, ABC
import org.slf4j.Logger as __Logger
__Logger = __Logger
import org.slf4j.helpers.MarkerIgnoringBase as __MarkerIgnoringBase
__MarkerIgnoringBase = __MarkerIgnoringBase
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
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
 
class MarkerIgnoringBase(ABC):
    """org.slf4j.helpers.MarkerIgnoringBase"""
 
    @staticmethod
    def __wrap(java_value: __MarkerIgnoringBase) -> 'MarkerIgnoringBase':
        return MarkerIgnoringBase(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MarkerIgnoringBase):
        """
        Dynamic initializer for MarkerIgnoringBase.
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
 
    @overload
    def isErrorEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.MarkerIgnoringBase.isErrorEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__MarkerIgnoringBase, self).isErrorEnabled(arg0))

    @abstractmethod
    def debug(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.debug(java.lang.String,java.lang.Object)"""
        pass

    @overload
    def isWarnEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.MarkerIgnoringBase.isWarnEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__MarkerIgnoringBase, self).isWarnEnabled(arg0))

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__MarkerIgnoringBase, self).info(arg0, arg1, arg2, arg3)

    @abstractmethod
    def warn(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Object...)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.MarkerIgnoringBase.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__MarkerIgnoringBase, self).error(arg0, arg1, arg2)

    @abstractmethod
    def trace(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Object...)"""
        pass

    @overload
    def __init__(self):
        """public org.slf4j.helpers.MarkerIgnoringBase()"""
        val = __MarkerIgnoringBase()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).atLevel(arg0))

    @overload
    def isInfoEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.MarkerIgnoringBase.isInfoEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__MarkerIgnoringBase, self).isInfoEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__MarkerIgnoringBase, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__MarkerIgnoringBase, self).error(arg0, arg1, arg2, arg3)

    @abstractmethod
    def isDebugEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled()"""
        pass

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__MarkerIgnoringBase, self).debug(arg0, arg1, arg2, arg3)

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool.__wrap(super(__slf4py.Logger, self).isEnabledForLevel(arg0))

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__MarkerIgnoringBase, self).trace(arg0, arg1, arg2, arg3)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.MarkerIgnoringBase.trace(org.slf4j.Marker,java.lang.String)"""
        super(__MarkerIgnoringBase, self).trace(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @abstractmethod
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.MarkerIgnoringBase.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__MarkerIgnoringBase, self).info(arg0, arg1, arg2)

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

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__MarkerIgnoringBase, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.MarkerIgnoringBase.error(org.slf4j.Marker,java.lang.String)"""
        super(__MarkerIgnoringBase, self).error(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.MarkerIgnoringBase.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__MarkerIgnoringBase, self).warn(arg0, arg1, arg2)

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).makeLoggingEventBuilder(arg0))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.MarkerIgnoringBase.debug(org.slf4j.Marker,java.lang.String)"""
        super(__MarkerIgnoringBase, self).debug(arg0, arg1)

    @abstractmethod
    def info(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Object)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.slf4j.helpers.MarkerIgnoringBase.toString()"""
        return str.__wrap(super(MarkerIgnoringBase, self).toString())

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.MarkerIgnoringBase.warn(org.slf4j.Marker,java.lang.String)"""
        super(__MarkerIgnoringBase, self).warn(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__MarkerIgnoringBase, self).warn(arg0, arg1, arg2)

    @abstractmethod
    def error(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def isInfoEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isInfoEnabled()"""
        pass

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__MarkerIgnoringBase, self).info(arg0, arg1, arg2)

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
    def isErrorEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isErrorEnabled()"""
        pass

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.MarkerIgnoringBase.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__MarkerIgnoringBase, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__MarkerIgnoringBase, self).warn(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isDebugEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.MarkerIgnoringBase.isDebugEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__MarkerIgnoringBase, self).isDebugEnabled(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__MarkerIgnoringBase, self).debug(arg0, arg1, arg2)

    @abstractmethod
    def info(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.info(java.lang.String,java.lang.Object...)"""
        pass

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.MarkerIgnoringBase.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__MarkerIgnoringBase, self).trace(arg0, arg1, arg2)

    @abstractmethod
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__MarkerIgnoringBase, self).trace(arg0, arg1, arg2)

    @abstractmethod
    def info(self, arg0: str):
        """public abstract void org.slf4j.Logger.info(java.lang.String)"""
        pass

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__MarkerIgnoringBase, self).debug(arg0, arg1, arg2)

    @abstractmethod
    def warn(self, arg0: str, arg1: object):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Object)"""
        pass

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atTrace())

    @abstractmethod
    def isTraceEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isTraceEnabled()"""
        pass

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.MarkerIgnoringBase()"""
        val = __MarkerIgnoringBase()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.warn(java.lang.String,java.lang.Throwable)"""
        pass

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atDebug())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def error(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.error(java.lang.String,java.lang.Throwable)"""
        pass

    @override
    @overload
    def atWarn(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atWarn()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atWarn())

    @abstractmethod
    def debug(self, arg0: str):
        """public abstract void org.slf4j.Logger.debug(java.lang.String)"""
        pass

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__MarkerIgnoringBase, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.MarkerIgnoringBase.info(org.slf4j.Marker,java.lang.String)"""
        super(__MarkerIgnoringBase, self).info(arg0, arg1)

    @abstractmethod
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public abstract void org.slf4j.Logger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__MarkerIgnoringBase, self).error(arg0, arg1, arg2)

    @abstractmethod
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public abstract void org.slf4j.Logger.debug(java.lang.String,java.lang.Throwable)"""
        pass

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atError())

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atInfo())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @abstractmethod
    def warn(self, arg0: str):
        """public abstract void org.slf4j.Logger.warn(java.lang.String)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @abstractmethod
    def error(self, arg0: str, *arg1: object):
        """public abstract void org.slf4j.Logger.error(java.lang.String,java.lang.Object...)"""
        pass

    @overload
    def isTraceEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.MarkerIgnoringBase.isTraceEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__MarkerIgnoringBase, self).isTraceEnabled(arg0))

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.MarkerIgnoringBase.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__MarkerIgnoringBase, self).trace(arg0, arg1, arg2)

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled()"""
        pass 
 
 
# CLASS: org.slf4j.helpers.Util
from builtins import str
from pyquantum_helper import override
import org.slf4j.helpers.Util as __Util
__Util = __Util
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
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Util():
    """org.slf4j.helpers.Util"""
 
    @staticmethod
    def __wrap(java_value: __Util) -> 'Util':
        return Util(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Util):
        """
        Dynamic initializer for Util.
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
 
    @staticmethod
    @overload
    def safeGetBooleanSystemProperty(arg0: str) -> bool:
        """public static boolean org.slf4j.helpers.Util.safeGetBooleanSystemProperty(java.lang.String)"""
        return bool.__wrap(__Util.safeGetBooleanSystemProperty(arg0))

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

    @staticmethod
    @overload
    def getCallingClass() -> 'type.Class':
        """public static java.lang.Class<?> org.slf4j.helpers.Util.getCallingClass()"""
        return type.Class.__wrap(__Util.getCallingClass())

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
    def report(arg0: str, arg1: 'Throwable'):
        """public static final void org.slf4j.helpers.Util.report(java.lang.String,java.lang.Throwable)"""
        __Util.report(arg0, arg1)

    @staticmethod
    @overload
    def safeGetSystemProperty(arg0: str) -> str:
        """public static java.lang.String org.slf4j.helpers.Util.safeGetSystemProperty(java.lang.String)"""
        return str.__wrap(__Util.safeGetSystemProperty(arg0))

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

    @staticmethod
    @overload
    def report(arg0: str):
        """public static final void org.slf4j.helpers.Util.report(java.lang.String)"""
        __Util.report(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.slf4j.helpers.SubstituteServiceProvider
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.slf4j.spi.MDCAdapter as __MDCAdapter
__MDCAdapter = __MDCAdapter
try:
    from slf4py import spi
except ImportError:
    spi = __import_once__("slf4py.spi")

import org.slf4j.ILoggerFactory as __ILoggerFactory
__ILoggerFactory = __ILoggerFactory
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.slf4j.helpers.SubstituteLoggerFactory as __SubstituteLoggerFactory
__SubstituteLoggerFactory = __SubstituteLoggerFactory
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import org.slf4j.IMarkerFactory as __IMarkerFactory
__IMarkerFactory = __IMarkerFactory
import java.lang.Integer as __int
from builtins import bool
import org.slf4j.helpers.SubstituteServiceProvider as __SubstituteServiceProvider
__SubstituteServiceProvider = __SubstituteServiceProvider
from builtins import int
 
class SubstituteServiceProvider():
    """org.slf4j.helpers.SubstituteServiceProvider"""
 
    @staticmethod
    def __wrap(java_value: __SubstituteServiceProvider) -> 'SubstituteServiceProvider':
        return SubstituteServiceProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SubstituteServiceProvider):
        """
        Dynamic initializer for SubstituteServiceProvider.
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
 
    @overload
    def getSubstituteLoggerFactory(self) -> 'SubstituteLoggerFactory':
        """public org.slf4j.helpers.SubstituteLoggerFactory org.slf4j.helpers.SubstituteServiceProvider.getSubstituteLoggerFactory()"""
        return 'SubstituteLoggerFactory'.__wrap(super(SubstituteServiceProvider, self).getSubstituteLoggerFactory())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getRequestedApiVersion(self) -> str:
        """public java.lang.String org.slf4j.helpers.SubstituteServiceProvider.getRequestedApiVersion()"""
        return str.__wrap(super(SubstituteServiceProvider, self).getRequestedApiVersion())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMarkerFactory(self) -> 'slf4py.IMarkerFactory':
        """public org.slf4j.IMarkerFactory org.slf4j.helpers.SubstituteServiceProvider.getMarkerFactory()"""
        return 'slf4py.IMarkerFactory'.__wrap(super(SubstituteServiceProvider, self).getMarkerFactory())

    @override
    @overload
    def getMDCAdapter(self) -> 'spi.MDCAdapter':
        """public org.slf4j.spi.MDCAdapter org.slf4j.helpers.SubstituteServiceProvider.getMDCAdapter()"""
        return 'spi.MDCAdapter'.__wrap(super(SubstituteServiceProvider, self).getMDCAdapter())

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.SubstituteServiceProvider()"""
        val = __SubstituteServiceProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.slf4j.helpers.SubstituteServiceProvider()"""
        val = __SubstituteServiceProvider()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def initialize(self):
        """public void org.slf4j.helpers.SubstituteServiceProvider.initialize()"""
        super(SubstituteServiceProvider, self).initialize()

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
    def getLoggerFactory(self) -> 'slf4py.ILoggerFactory':
        """public org.slf4j.ILoggerFactory org.slf4j.helpers.SubstituteServiceProvider.getLoggerFactory()"""
        return 'slf4py.ILoggerFactory'.__wrap(super(SubstituteServiceProvider, self).getLoggerFactory())

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
 
 
# CLASS: org.slf4j.helpers.MessageFormatter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import org.slf4j.helpers.MessageFormatter as __MessageFormatter
__MessageFormatter = __MessageFormatter
from builtins import object
from typing import List
import org.slf4j.helpers.FormattingTuple as __FormattingTuple
__FormattingTuple = __FormattingTuple
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MessageFormatter():
    """org.slf4j.helpers.MessageFormatter"""
 
    @staticmethod
    def __wrap(java_value: __MessageFormatter) -> 'MessageFormatter':
        return MessageFormatter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageFormatter):
        """
        Dynamic initializer for MessageFormatter.
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
    def arrayFormat(arg0: str, arg1: 'Object') -> 'FormattingTuple':
        """public static final org.slf4j.helpers.FormattingTuple org.slf4j.helpers.MessageFormatter.arrayFormat(java.lang.String,java.lang.Object[])"""
        return FormattingTuple.__wrap(__MessageFormatter.arrayFormat(arg0, arg1))

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

    @staticmethod
    @overload
    def basicArrayFormat(arg0: 'NormalizedParameters') -> str:
        """public static java.lang.String org.slf4j.helpers.MessageFormatter.basicArrayFormat(org.slf4j.helpers.NormalizedParameters)"""
        return str.__wrap(__MessageFormatter.basicArrayFormat(arg0))

    @staticmethod
    @overload
    def arrayFormat(arg0: str, arg1: 'Object', arg2: 'Throwable') -> 'FormattingTuple':
        """public static final org.slf4j.helpers.FormattingTuple org.slf4j.helpers.MessageFormatter.arrayFormat(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        return FormattingTuple.__wrap(__MessageFormatter.arrayFormat(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.MessageFormatter()"""
        val = __MessageFormatter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.slf4j.helpers.MessageFormatter()"""
        val = __MessageFormatter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getThrowableCandidate(arg0: 'Object') -> 'Throwable':
        """public static java.lang.Throwable org.slf4j.helpers.MessageFormatter.getThrowableCandidate(java.lang.Object[])"""
        return Throwable.__wrap(__MessageFormatter.getThrowableCandidate(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def format(arg0: str, arg1: object, arg2: object) -> 'FormattingTuple':
        """public static final org.slf4j.helpers.FormattingTuple org.slf4j.helpers.MessageFormatter.format(java.lang.String,java.lang.Object,java.lang.Object)"""
        return FormattingTuple.__wrap(__MessageFormatter.format(arg0, arg1, arg2))

    @staticmethod
    @overload
    def trimmedCopy(arg0: 'Object') -> List[object]:
        """public static java.lang.Object[] org.slf4j.helpers.MessageFormatter.trimmedCopy(java.lang.Object[])"""
        return List[object].__wrap(__MessageFormatter.trimmedCopy(arg0))

    @staticmethod
    @overload
    def basicArrayFormat(arg0: str, arg1: 'Object') -> str:
        """public static final java.lang.String org.slf4j.helpers.MessageFormatter.basicArrayFormat(java.lang.String,java.lang.Object[])"""
        return str.__wrap(__MessageFormatter.basicArrayFormat(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def format(arg0: str, arg1: object) -> 'FormattingTuple':
        """public static final org.slf4j.helpers.FormattingTuple org.slf4j.helpers.MessageFormatter.format(java.lang.String,java.lang.Object)"""
        return FormattingTuple.__wrap(__MessageFormatter.format(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.slf4j.helpers.BasicMDCAdapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Map as __Map
__Map = __Map
import java.util.Deque as Deque
import java.util.Deque as __Deque
__Deque = __Deque
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.slf4j.helpers.BasicMDCAdapter as __BasicMDCAdapter
__BasicMDCAdapter = __BasicMDCAdapter
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class BasicMDCAdapter():
    """org.slf4j.helpers.BasicMDCAdapter"""
 
    @staticmethod
    def __wrap(java_value: __BasicMDCAdapter) -> 'BasicMDCAdapter':
        return BasicMDCAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BasicMDCAdapter):
        """
        Dynamic initializer for BasicMDCAdapter.
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
    def put(self, arg0: str, arg1: str):
        """public void org.slf4j.helpers.BasicMDCAdapter.put(java.lang.String,java.lang.String)"""
        super(__BasicMDCAdapter, self).put(arg0, arg1)

    @override
    @overload
    def pushByKey(self, arg0: str, arg1: str):
        """public void org.slf4j.helpers.BasicMDCAdapter.pushByKey(java.lang.String,java.lang.String)"""
        super(__BasicMDCAdapter, self).pushByKey(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getCopyOfDequeByKey(self, arg0: str) -> 'Deque':
        """public java.util.Deque<java.lang.String> org.slf4j.helpers.BasicMDCAdapter.getCopyOfDequeByKey(java.lang.String)"""
        return 'Deque'.__wrap(super(__BasicMDCAdapter, self).getCopyOfDequeByKey(arg0))

    @override
    @overload
    def clearDequeByKey(self, arg0: str):
        """public void org.slf4j.helpers.BasicMDCAdapter.clearDequeByKey(java.lang.String)"""
        super(__BasicMDCAdapter, self).clearDequeByKey(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCopyOfContextMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.slf4j.helpers.BasicMDCAdapter.getCopyOfContextMap()"""
        return 'Map'.__wrap(super(BasicMDCAdapter, self).getCopyOfContextMap())

    @override
    @overload
    def setContextMap(self, arg0: 'Map'):
        """public void org.slf4j.helpers.BasicMDCAdapter.setContextMap(java.util.Map<java.lang.String, java.lang.String>)"""
        super(__BasicMDCAdapter, self).setContextMap(arg0)

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
    def remove(self, arg0: str):
        """public void org.slf4j.helpers.BasicMDCAdapter.remove(java.lang.String)"""
        super(__BasicMDCAdapter, self).remove(arg0)

    @overload
    def get(self, arg0: str) -> str:
        """public java.lang.String org.slf4j.helpers.BasicMDCAdapter.get(java.lang.String)"""
        return str.__wrap(super(__BasicMDCAdapter, self).get(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public org.slf4j.helpers.BasicMDCAdapter()"""
        val = __BasicMDCAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def clear(self):
        """public void org.slf4j.helpers.BasicMDCAdapter.clear()"""
        super(BasicMDCAdapter, self).clear()

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.BasicMDCAdapter()"""
        val = __BasicMDCAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def popByKey(self, arg0: str) -> str:
        """public java.lang.String org.slf4j.helpers.BasicMDCAdapter.popByKey(java.lang.String)"""
        return str.__wrap(super(__BasicMDCAdapter, self).popByKey(arg0))

    @overload
    def getKeys(self) -> 'Set':
        """public java.util.Set<java.lang.String> org.slf4j.helpers.BasicMDCAdapter.getKeys()"""
        return 'Set'.__wrap(super(BasicMDCAdapter, self).getKeys())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.slf4j.helpers.CheckReturnValue
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import org.slf4j.helpers.CheckReturnValue as __CheckReturnValue
__CheckReturnValue = __CheckReturnValue
from abc import abstractmethod, ABC
 
class CheckReturnValue(ABC):
    """org.slf4j.helpers.CheckReturnValue"""
 
    @staticmethod
    def __wrap(java_value: __CheckReturnValue) -> 'CheckReturnValue':
        return CheckReturnValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CheckReturnValue):
        """
        Dynamic initializer for CheckReturnValue.
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
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.slf4j.helpers.NOPLoggerFactory
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.slf4j.Logger as __Logger
__Logger = __Logger
import java.lang.Long as __long
import org.slf4j.helpers.NOPLoggerFactory as __NOPLoggerFactory
__NOPLoggerFactory = __NOPLoggerFactory
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    import slf4py
except ImportError:
    slf4py = __import_once__("slf4py")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NOPLoggerFactory():
    """org.slf4j.helpers.NOPLoggerFactory"""
 
    @staticmethod
    def __wrap(java_value: __NOPLoggerFactory) -> 'NOPLoggerFactory':
        return NOPLoggerFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NOPLoggerFactory):
        """
        Dynamic initializer for NOPLoggerFactory.
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

    @overload
    def getLogger(self, arg0: str) -> 'slf4py.Logger':
        """public org.slf4j.Logger org.slf4j.helpers.NOPLoggerFactory.getLogger(java.lang.String)"""
        return 'slf4py.Logger'.__wrap(super(__NOPLoggerFactory, self).getLogger(arg0))

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

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.NOPLoggerFactory()"""
        val = __NOPLoggerFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.slf4j.helpers.NOPLoggerFactory()"""
        val = __NOPLoggerFactory()
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
 
 
# CLASS: org.slf4j.helpers.LegacyAbstractLogger
from pyquantum_helper import import_once as __import_once__
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

from builtins import object
from abc import abstractmethod, ABC
import org.slf4j.helpers.AbstractLogger as __AbstractLogger
__AbstractLogger = __AbstractLogger
import org.slf4j.Logger as __Logger
__Logger = __Logger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
try:
    from slf4py import event
except ImportError:
    event = __import_once__("slf4py.event")

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
 
class LegacyAbstractLogger(ABC):
    """org.slf4j.helpers.LegacyAbstractLogger"""
 
    @staticmethod
    def __wrap(java_value: __LegacyAbstractLogger) -> 'LegacyAbstractLogger':
        return LegacyAbstractLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LegacyAbstractLogger):
        """
        Dynamic initializer for LegacyAbstractLogger.
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
    def error(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def info(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).info(arg0, arg1)

    @overload
    def atLevel(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atLevel(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).atLevel(arg0))

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def isDebugEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isDebugEnabled()"""
        pass

    @overload
    def isTraceEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isTraceEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__LegacyAbstractLogger, self).isTraceEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).warn(arg0, arg1)

    @overload
    def isEnabledForLevel(self, arg0: 'Level') -> bool:
        """public default boolean org.slf4j.Logger.isEnabledForLevel(org.slf4j.event.Level)"""
        return bool.__wrap(super(__slf4py.Logger, self).isEnabledForLevel(arg0))

    @overload
    def isInfoEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isInfoEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__LegacyAbstractLogger, self).isInfoEnabled(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(arg0, arg1, arg2, arg3)

    @override
    @overload
    def debug(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String)"""
        super(__AbstractLogger, self).debug(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).trace(arg0, arg1, arg2)

    @overload
    def __init__(self, ):
        """public org.slf4j.helpers.LegacyAbstractLogger()"""
        val = __LegacyAbstractLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def makeLoggingEventBuilder(self, arg0: 'Level') -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.makeLoggingEventBuilder(org.slf4j.event.Level)"""
        return 'spi.LoggingEventBuilder'.__wrap(super(__slf4py.Logger, self).makeLoggingEventBuilder(arg0))

    @override
    @overload
    def info(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String)"""
        super(__AbstractLogger, self).info(arg0)

    @override
    @overload
    def trace(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def warn(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def info(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).info(arg0, arg1)

    @abstractmethod
    def isInfoEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isInfoEnabled()"""
        pass

    @override
    @overload
    def warn(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String)"""
        super(__AbstractLogger, self).warn(arg0)

    @override
    @overload
    def debug(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).debug(arg0, arg1)

    @abstractmethod
    def isErrorEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isErrorEnabled()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isErrorEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isErrorEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__LegacyAbstractLogger, self).isErrorEnabled(arg0))

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, *arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def atTrace(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atTrace()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atTrace())

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(arg0, arg1, arg2)

    @abstractmethod
    def isTraceEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isTraceEnabled()"""
        pass

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def atDebug(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atDebug()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atDebug())

    @override
    @overload
    def debug(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).debug(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).error(arg0, arg1)

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
    def error(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).error(arg0, arg1)

    @overload
    def isDebugEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isDebugEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__LegacyAbstractLogger, self).isDebugEnabled(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.slf4j.helpers.AbstractLogger.getName()"""
        return str.__wrap(super(AbstractLogger, self).getName())

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).debug(arg0, arg1, arg2, arg3)

    @override
    @overload
    def error(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.error(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(arg0, arg1, arg2, arg3)

    @override
    @overload
    def warn(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).trace(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String)"""
        super(__AbstractLogger, self).error(arg0)

    @override
    @overload
    def trace(self, arg0: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String)"""
        super(__AbstractLogger, self).trace(arg0)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def trace(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).info(arg0, arg1)

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).trace(arg0, arg1, arg2, arg3)

    @override
    @overload
    def atError(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atError()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atError())

    @override
    @overload
    def atInfo(self) -> 'spi.LoggingEventBuilder':
        """public default org.slf4j.spi.LoggingEventBuilder org.slf4j.Logger.atInfo()"""
        return 'spi.LoggingEventBuilder'.__wrap(super(slf4py.Logger, self).atInfo())

    @override
    @overload
    def trace(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.trace(org.slf4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).trace(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: 'Marker', arg1: str):
        """public void org.slf4j.helpers.AbstractLogger.debug(org.slf4j.Marker,java.lang.String)"""
        super(__AbstractLogger, self).debug(arg0, arg1)

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
    def info(self, arg0: str, arg1: object, arg2: object):
        """public void org.slf4j.helpers.AbstractLogger.info(java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.debug(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).debug(arg0, arg1)

    @overload
    def isWarnEnabled(self, arg0: 'Marker') -> bool:
        """public boolean org.slf4j.helpers.LegacyAbstractLogger.isWarnEnabled(org.slf4j.Marker)"""
        return bool.__wrap(super(__LegacyAbstractLogger, self).isWarnEnabled(arg0))

    @override
    @overload
    def warn(self, arg0: str, *arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Object...)"""
        super(__AbstractLogger, self).warn(arg0, arg1)

    @overload
    def __init__(self):
        """public org.slf4j.helpers.LegacyAbstractLogger()"""
        val = __LegacyAbstractLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def error(self, arg0: str, arg1: object):
        """public void org.slf4j.helpers.AbstractLogger.error(java.lang.String,java.lang.Object)"""
        super(__AbstractLogger, self).error(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public void org.slf4j.helpers.AbstractLogger.warn(java.lang.String,java.lang.Throwable)"""
        super(__AbstractLogger, self).warn(arg0, arg1)

    @override
    @overload
    def warn(self, arg0: 'Marker', arg1: str, arg2: object, arg3: object):
        """public void org.slf4j.helpers.AbstractLogger.warn(org.slf4j.Marker,java.lang.String,java.lang.Object,java.lang.Object)"""
        super(__AbstractLogger, self).warn(arg0, arg1, arg2, arg3)

    @abstractmethod
    def isWarnEnabled(self, ):
        """public abstract boolean org.slf4j.Logger.isWarnEnabled()"""
        pass