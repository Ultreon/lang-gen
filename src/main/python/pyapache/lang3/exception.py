from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.io.PrintWriter as PrintWriter
from builtins import object
import java.util.function.Consumer as Consumer
from typing import List
import org.apache.commons.lang3.exception.ExceptionUtils as __ExceptionUtils
__ExceptionUtils = __ExceptionUtils
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class ExceptionUtils():
    """org.apache.commons.lang3.exception.ExceptionUtils"""
 
    @staticmethod
    def __wrap(java_value: __ExceptionUtils) -> 'ExceptionUtils':
        return ExceptionUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExceptionUtils):
        """
        Dynamic initializer for ExceptionUtils.
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
    def getStackFrames(arg0: 'Throwable') -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.exception.ExceptionUtils.getStackFrames(java.lang.Throwable)"""
        return List[str].__wrap(__ExceptionUtils.getStackFrames(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def indexOfType(arg0: 'Throwable', arg1: 'Class') -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfType(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>)"""
        return int.__wrap(__ExceptionUtils.indexOfType(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.exception.ExceptionUtils()"""
        val = __ExceptionUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.exception.ExceptionUtils()"""
        val = __ExceptionUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getRootCauseStackTraceList(arg0: 'Throwable') -> 'List':
        """public static java.util.List<java.lang.String> org.apache.commons.lang3.exception.ExceptionUtils.getRootCauseStackTraceList(java.lang.Throwable)"""
        return List.__wrap(__ExceptionUtils.getRootCauseStackTraceList(arg0))

    @staticmethod
    @overload
    def isUnchecked(arg0: 'Throwable') -> bool:
        """public static boolean org.apache.commons.lang3.exception.ExceptionUtils.isUnchecked(java.lang.Throwable)"""
        return bool.__wrap(__ExceptionUtils.isUnchecked(arg0))

    @staticmethod
    @overload
    def printRootCauseStackTrace(arg0: 'Throwable', arg1: 'PrintStream'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.printRootCauseStackTrace(java.lang.Throwable,java.io.PrintStream)"""
        __ExceptionUtils.printRootCauseStackTrace(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def removeCommonFrames(arg0: 'List', arg1: 'List'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.removeCommonFrames(java.util.List<java.lang.String>,java.util.List<java.lang.String>)"""
        __ExceptionUtils.removeCommonFrames(arg0, arg1)

    @staticmethod
    @overload
    def rethrow(arg0: 'Throwable') -> object:
        """public static <R> R org.apache.commons.lang3.exception.ExceptionUtils.rethrow(java.lang.Throwable)"""
        return object.__wrap(__ExceptionUtils.rethrow(arg0))

    @staticmethod
    @overload
    def getRootCauseStackTrace(arg0: 'Throwable') -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.exception.ExceptionUtils.getRootCauseStackTrace(java.lang.Throwable)"""
        return List[str].__wrap(__ExceptionUtils.getRootCauseStackTrace(arg0))

    @staticmethod
    @overload
    def throwableOfThrowable(arg0: 'Throwable', arg1: 'Class', arg2: int) -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfThrowable(java.lang.Throwable,java.lang.Class<T>,int)"""
        return Throwable.__wrap(__ExceptionUtils.throwableOfThrowable(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def getRootCauseMessage(arg0: 'Throwable') -> str:
        """public static java.lang.String org.apache.commons.lang3.exception.ExceptionUtils.getRootCauseMessage(java.lang.Throwable)"""
        return str.__wrap(__ExceptionUtils.getRootCauseMessage(arg0))

    @staticmethod
    @overload
    def getThrowables(arg0: 'Throwable') -> List['Throwable']:
        """public static java.lang.Throwable[] org.apache.commons.lang3.exception.ExceptionUtils.getThrowables(java.lang.Throwable)"""
        return List[Throwable].__wrap(__ExceptionUtils.getThrowables(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getThrowableCount(arg0: 'Throwable') -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.getThrowableCount(java.lang.Throwable)"""
        return int.__wrap(__ExceptionUtils.getThrowableCount(arg0))

    @staticmethod
    @overload
    def getMessage(arg0: 'Throwable') -> str:
        """public static java.lang.String org.apache.commons.lang3.exception.ExceptionUtils.getMessage(java.lang.Throwable)"""
        return str.__wrap(__ExceptionUtils.getMessage(arg0))

    @staticmethod
    @overload
    def printRootCauseStackTrace(arg0: 'Throwable', arg1: 'PrintWriter'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.printRootCauseStackTrace(java.lang.Throwable,java.io.PrintWriter)"""
        __ExceptionUtils.printRootCauseStackTrace(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def throwableOfThrowable(arg0: 'Throwable', arg1: 'Class') -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfThrowable(java.lang.Throwable,java.lang.Class<T>)"""
        return Throwable.__wrap(__ExceptionUtils.throwableOfThrowable(arg0, arg1))

    @staticmethod
    @overload
    def getDefaultCauseMethodNames() -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.exception.ExceptionUtils.getDefaultCauseMethodNames()"""
        return List[str].__wrap(__ExceptionUtils.getDefaultCauseMethodNames())

    @staticmethod
    @overload
    def printRootCauseStackTrace(arg0: 'Throwable'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.printRootCauseStackTrace(java.lang.Throwable)"""
        __ExceptionUtils.printRootCauseStackTrace(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def isChecked(arg0: 'Throwable') -> bool:
        """public static boolean org.apache.commons.lang3.exception.ExceptionUtils.isChecked(java.lang.Throwable)"""
        return bool.__wrap(__ExceptionUtils.isChecked(arg0))

    @staticmethod
    @overload
    def indexOfType(arg0: 'Throwable', arg1: 'Class', arg2: int) -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfType(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>,int)"""
        return int.__wrap(__ExceptionUtils.indexOfType(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def getThrowableList(arg0: 'Throwable') -> 'List':
        """public static java.util.List<java.lang.Throwable> org.apache.commons.lang3.exception.ExceptionUtils.getThrowableList(java.lang.Throwable)"""
        return List.__wrap(__ExceptionUtils.getThrowableList(arg0))

    @staticmethod
    @overload
    def throwUnchecked(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.exception.ExceptionUtils.throwUnchecked(T)"""
        return object.__wrap(__ExceptionUtils.throwUnchecked(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getCause(arg0: 'Throwable', arg1: 'String') -> 'Throwable':
        """public static java.lang.Throwable org.apache.commons.lang3.exception.ExceptionUtils.getCause(java.lang.Throwable,java.lang.String[])"""
        return Throwable.__wrap(__ExceptionUtils.getCause(arg0, arg1))

    @staticmethod
    @overload
    def getCause(arg0: 'Throwable') -> 'Throwable':
        """public static java.lang.Throwable org.apache.commons.lang3.exception.ExceptionUtils.getCause(java.lang.Throwable)"""
        return Throwable.__wrap(__ExceptionUtils.getCause(arg0))

    @staticmethod
    @overload
    def stream(arg0: 'Throwable') -> 'Stream':
        """public static java.util.stream.Stream<java.lang.Throwable> org.apache.commons.lang3.exception.ExceptionUtils.stream(java.lang.Throwable)"""
        return Stream.__wrap(__ExceptionUtils.stream(arg0))

    @staticmethod
    @overload
    def wrapAndThrow(arg0: 'Throwable') -> object:
        """public static <R> R org.apache.commons.lang3.exception.ExceptionUtils.wrapAndThrow(java.lang.Throwable)"""
        return object.__wrap(__ExceptionUtils.wrapAndThrow(arg0))

    @staticmethod
    @overload
    def indexOfThrowable(arg0: 'Throwable', arg1: 'Class') -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfThrowable(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>)"""
        return int.__wrap(__ExceptionUtils.indexOfThrowable(arg0, arg1))

    @staticmethod
    @overload
    def forEach(arg0: 'Throwable', arg1: 'Consumer'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.forEach(java.lang.Throwable,java.util.function.Consumer<java.lang.Throwable>)"""
        __ExceptionUtils.forEach(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def throwableOfType(arg0: 'Throwable', arg1: 'Class', arg2: int) -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfType(java.lang.Throwable,java.lang.Class<T>,int)"""
        return Throwable.__wrap(__ExceptionUtils.throwableOfType(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def getStackTrace(arg0: 'Throwable') -> str:
        """public static java.lang.String org.apache.commons.lang3.exception.ExceptionUtils.getStackTrace(java.lang.Throwable)"""
        return str.__wrap(__ExceptionUtils.getStackTrace(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getRootCause(arg0: 'Throwable') -> 'Throwable':
        """public static java.lang.Throwable org.apache.commons.lang3.exception.ExceptionUtils.getRootCause(java.lang.Throwable)"""
        return Throwable.__wrap(__ExceptionUtils.getRootCause(arg0))

    @staticmethod
    @overload
    def throwableOfType(arg0: 'Throwable', arg1: 'Class') -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfType(java.lang.Throwable,java.lang.Class<T>)"""
        return Throwable.__wrap(__ExceptionUtils.throwableOfType(arg0, arg1))

    @staticmethod
    @overload
    def indexOfThrowable(arg0: 'Throwable', arg1: 'Class', arg2: int) -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfThrowable(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>,int)"""
        return int.__wrap(__ExceptionUtils.indexOfThrowable(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def hasCause(arg0: 'Throwable', arg1: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.exception.ExceptionUtils.hasCause(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>)"""
        return bool.__wrap(__ExceptionUtils.hasCause(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: org.apache.commons.lang3.exception.ExceptionUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.io.PrintWriter as PrintWriter
from builtins import object
import java.util.function.Consumer as Consumer
from typing import List
import org.apache.commons.lang3.exception.ExceptionUtils as __ExceptionUtils
__ExceptionUtils = __ExceptionUtils
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class ExceptionUtils():
    """org.apache.commons.lang3.exception.ExceptionUtils"""
 
    @staticmethod
    def __wrap(java_value: __ExceptionUtils) -> 'ExceptionUtils':
        return ExceptionUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExceptionUtils):
        """
        Dynamic initializer for ExceptionUtils.
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
    def getStackFrames(arg0: 'Throwable') -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.exception.ExceptionUtils.getStackFrames(java.lang.Throwable)"""
        return List[str].__wrap(__ExceptionUtils.getStackFrames(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def indexOfType(arg0: 'Throwable', arg1: 'Class') -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfType(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>)"""
        return int.__wrap(__ExceptionUtils.indexOfType(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.exception.ExceptionUtils()"""
        val = __ExceptionUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.exception.ExceptionUtils()"""
        val = __ExceptionUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getRootCauseStackTraceList(arg0: 'Throwable') -> 'List':
        """public static java.util.List<java.lang.String> org.apache.commons.lang3.exception.ExceptionUtils.getRootCauseStackTraceList(java.lang.Throwable)"""
        return List.__wrap(__ExceptionUtils.getRootCauseStackTraceList(arg0))

    @staticmethod
    @overload
    def isUnchecked(arg0: 'Throwable') -> bool:
        """public static boolean org.apache.commons.lang3.exception.ExceptionUtils.isUnchecked(java.lang.Throwable)"""
        return bool.__wrap(__ExceptionUtils.isUnchecked(arg0))

    @staticmethod
    @overload
    def printRootCauseStackTrace(arg0: 'Throwable', arg1: 'PrintStream'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.printRootCauseStackTrace(java.lang.Throwable,java.io.PrintStream)"""
        __ExceptionUtils.printRootCauseStackTrace(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def removeCommonFrames(arg0: 'List', arg1: 'List'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.removeCommonFrames(java.util.List<java.lang.String>,java.util.List<java.lang.String>)"""
        __ExceptionUtils.removeCommonFrames(arg0, arg1)

    @staticmethod
    @overload
    def rethrow(arg0: 'Throwable') -> object:
        """public static <R> R org.apache.commons.lang3.exception.ExceptionUtils.rethrow(java.lang.Throwable)"""
        return object.__wrap(__ExceptionUtils.rethrow(arg0))

    @staticmethod
    @overload
    def getRootCauseStackTrace(arg0: 'Throwable') -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.exception.ExceptionUtils.getRootCauseStackTrace(java.lang.Throwable)"""
        return List[str].__wrap(__ExceptionUtils.getRootCauseStackTrace(arg0))

    @staticmethod
    @overload
    def throwableOfThrowable(arg0: 'Throwable', arg1: 'Class', arg2: int) -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfThrowable(java.lang.Throwable,java.lang.Class<T>,int)"""
        return Throwable.__wrap(__ExceptionUtils.throwableOfThrowable(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def getRootCauseMessage(arg0: 'Throwable') -> str:
        """public static java.lang.String org.apache.commons.lang3.exception.ExceptionUtils.getRootCauseMessage(java.lang.Throwable)"""
        return str.__wrap(__ExceptionUtils.getRootCauseMessage(arg0))

    @staticmethod
    @overload
    def getThrowables(arg0: 'Throwable') -> List['Throwable']:
        """public static java.lang.Throwable[] org.apache.commons.lang3.exception.ExceptionUtils.getThrowables(java.lang.Throwable)"""
        return List[Throwable].__wrap(__ExceptionUtils.getThrowables(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getThrowableCount(arg0: 'Throwable') -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.getThrowableCount(java.lang.Throwable)"""
        return int.__wrap(__ExceptionUtils.getThrowableCount(arg0))

    @staticmethod
    @overload
    def getMessage(arg0: 'Throwable') -> str:
        """public static java.lang.String org.apache.commons.lang3.exception.ExceptionUtils.getMessage(java.lang.Throwable)"""
        return str.__wrap(__ExceptionUtils.getMessage(arg0))

    @staticmethod
    @overload
    def printRootCauseStackTrace(arg0: 'Throwable', arg1: 'PrintWriter'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.printRootCauseStackTrace(java.lang.Throwable,java.io.PrintWriter)"""
        __ExceptionUtils.printRootCauseStackTrace(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def throwableOfThrowable(arg0: 'Throwable', arg1: 'Class') -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfThrowable(java.lang.Throwable,java.lang.Class<T>)"""
        return Throwable.__wrap(__ExceptionUtils.throwableOfThrowable(arg0, arg1))

    @staticmethod
    @overload
    def getDefaultCauseMethodNames() -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.exception.ExceptionUtils.getDefaultCauseMethodNames()"""
        return List[str].__wrap(__ExceptionUtils.getDefaultCauseMethodNames())

    @staticmethod
    @overload
    def printRootCauseStackTrace(arg0: 'Throwable'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.printRootCauseStackTrace(java.lang.Throwable)"""
        __ExceptionUtils.printRootCauseStackTrace(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def isChecked(arg0: 'Throwable') -> bool:
        """public static boolean org.apache.commons.lang3.exception.ExceptionUtils.isChecked(java.lang.Throwable)"""
        return bool.__wrap(__ExceptionUtils.isChecked(arg0))

    @staticmethod
    @overload
    def indexOfType(arg0: 'Throwable', arg1: 'Class', arg2: int) -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfType(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>,int)"""
        return int.__wrap(__ExceptionUtils.indexOfType(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def getThrowableList(arg0: 'Throwable') -> 'List':
        """public static java.util.List<java.lang.Throwable> org.apache.commons.lang3.exception.ExceptionUtils.getThrowableList(java.lang.Throwable)"""
        return List.__wrap(__ExceptionUtils.getThrowableList(arg0))

    @staticmethod
    @overload
    def throwUnchecked(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.exception.ExceptionUtils.throwUnchecked(T)"""
        return object.__wrap(__ExceptionUtils.throwUnchecked(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getCause(arg0: 'Throwable', arg1: 'String') -> 'Throwable':
        """public static java.lang.Throwable org.apache.commons.lang3.exception.ExceptionUtils.getCause(java.lang.Throwable,java.lang.String[])"""
        return Throwable.__wrap(__ExceptionUtils.getCause(arg0, arg1))

    @staticmethod
    @overload
    def getCause(arg0: 'Throwable') -> 'Throwable':
        """public static java.lang.Throwable org.apache.commons.lang3.exception.ExceptionUtils.getCause(java.lang.Throwable)"""
        return Throwable.__wrap(__ExceptionUtils.getCause(arg0))

    @staticmethod
    @overload
    def stream(arg0: 'Throwable') -> 'Stream':
        """public static java.util.stream.Stream<java.lang.Throwable> org.apache.commons.lang3.exception.ExceptionUtils.stream(java.lang.Throwable)"""
        return Stream.__wrap(__ExceptionUtils.stream(arg0))

    @staticmethod
    @overload
    def wrapAndThrow(arg0: 'Throwable') -> object:
        """public static <R> R org.apache.commons.lang3.exception.ExceptionUtils.wrapAndThrow(java.lang.Throwable)"""
        return object.__wrap(__ExceptionUtils.wrapAndThrow(arg0))

    @staticmethod
    @overload
    def indexOfThrowable(arg0: 'Throwable', arg1: 'Class') -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfThrowable(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>)"""
        return int.__wrap(__ExceptionUtils.indexOfThrowable(arg0, arg1))

    @staticmethod
    @overload
    def forEach(arg0: 'Throwable', arg1: 'Consumer'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.forEach(java.lang.Throwable,java.util.function.Consumer<java.lang.Throwable>)"""
        __ExceptionUtils.forEach(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def throwableOfType(arg0: 'Throwable', arg1: 'Class', arg2: int) -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfType(java.lang.Throwable,java.lang.Class<T>,int)"""
        return Throwable.__wrap(__ExceptionUtils.throwableOfType(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def getStackTrace(arg0: 'Throwable') -> str:
        """public static java.lang.String org.apache.commons.lang3.exception.ExceptionUtils.getStackTrace(java.lang.Throwable)"""
        return str.__wrap(__ExceptionUtils.getStackTrace(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getRootCause(arg0: 'Throwable') -> 'Throwable':
        """public static java.lang.Throwable org.apache.commons.lang3.exception.ExceptionUtils.getRootCause(java.lang.Throwable)"""
        return Throwable.__wrap(__ExceptionUtils.getRootCause(arg0))

    @staticmethod
    @overload
    def throwableOfType(arg0: 'Throwable', arg1: 'Class') -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfType(java.lang.Throwable,java.lang.Class<T>)"""
        return Throwable.__wrap(__ExceptionUtils.throwableOfType(arg0, arg1))

    @staticmethod
    @overload
    def indexOfThrowable(arg0: 'Throwable', arg1: 'Class', arg2: int) -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfThrowable(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>,int)"""
        return int.__wrap(__ExceptionUtils.indexOfThrowable(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def hasCause(arg0: 'Throwable', arg1: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.exception.ExceptionUtils.hasCause(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>)"""
        return bool.__wrap(__ExceptionUtils.hasCause(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: org.apache.commons.lang3.exception.ExceptionUtils 
 
 
# CLASS: org.apache.commons.lang3.exception.CloneFailedException
import org.apache.commons.lang3.exception.CloneFailedException as __CloneFailedException
__CloneFailedException = __CloneFailedException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CloneFailedException(__RuntimeException, RuntimeException):
    """org.apache.commons.lang3.exception.CloneFailedException"""
 
    @staticmethod
    def __wrap(java_value: __CloneFailedException) -> 'CloneFailedException':
        return CloneFailedException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CloneFailedException):
        """
        Dynamic initializer for CloneFailedException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.exception.CloneFailedException(java.lang.String,java.lang.Throwable)"""
        val = __CloneFailedException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.exception.CloneFailedException(java.lang.String)"""
        val = __CloneFailedException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.CloneFailedException(java.lang.Throwable)"""
        val = __CloneFailedException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.commons.lang3.exception.UncheckedException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.exception.UncheckedException as __UncheckedException
__UncheckedException = __UncheckedException
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UncheckedException(__RuntimeException, RuntimeException):
    """org.apache.commons.lang3.exception.UncheckedException"""
 
    @staticmethod
    def __wrap(java_value: __UncheckedException) -> 'UncheckedException':
        return UncheckedException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UncheckedException):
        """
        Dynamic initializer for UncheckedException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.UncheckedException(java.lang.Throwable)"""
        val = __UncheckedException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.commons.lang3.exception.UncheckedInterruptedException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
import org.apache.commons.lang3.exception.UncheckedInterruptedException as __UncheckedInterruptedException
__UncheckedInterruptedException = __UncheckedInterruptedException
from builtins import int
 
class UncheckedInterruptedException(__UncheckedException, UncheckedException):
    """org.apache.commons.lang3.exception.UncheckedInterruptedException"""
 
    @staticmethod
    def __wrap(java_value: __UncheckedInterruptedException) -> 'UncheckedInterruptedException':
        return UncheckedInterruptedException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UncheckedInterruptedException):
        """
        Dynamic initializer for UncheckedInterruptedException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.UncheckedInterruptedException(java.lang.Throwable)"""
        val = __UncheckedInterruptedException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.exception.UncheckedIllegalAccessException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import org.apache.commons.lang3.exception.UncheckedIllegalAccessException as __UncheckedIllegalAccessException
__UncheckedIllegalAccessException = __UncheckedIllegalAccessException
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UncheckedIllegalAccessException(__UncheckedReflectiveOperationException, UncheckedReflectiveOperationException):
    """org.apache.commons.lang3.exception.UncheckedIllegalAccessException"""
 
    @staticmethod
    def __wrap(java_value: __UncheckedIllegalAccessException) -> 'UncheckedIllegalAccessException':
        return UncheckedIllegalAccessException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UncheckedIllegalAccessException):
        """
        Dynamic initializer for UncheckedIllegalAccessException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.UncheckedIllegalAccessException(java.lang.Throwable)"""
        val = __UncheckedIllegalAccessException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.exception.ExceptionContext
from abc import abstractmethod, ABC
import org.apache.commons.lang3.exception.ExceptionContext as __ExceptionContext
__ExceptionContext = __ExceptionContext
 
class ExceptionContext(ABC):
    """org.apache.commons.lang3.exception.ExceptionContext"""
 
    @staticmethod
    def __wrap(java_value: __ExceptionContext) -> 'ExceptionContext':
        return ExceptionContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExceptionContext):
        """
        Dynamic initializer for ExceptionContext.
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
    def addContextValue(self, arg0: str, arg1: object):
        """public abstract org.apache.commons.lang3.exception.ExceptionContext org.apache.commons.lang3.exception.ExceptionContext.addContextValue(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def getFirstContextValue(self, arg0: str):
        """public abstract java.lang.Object org.apache.commons.lang3.exception.ExceptionContext.getFirstContextValue(java.lang.String)"""
        pass

    @abstractmethod
    def getContextLabels(self, ):
        """public abstract java.util.Set<java.lang.String> org.apache.commons.lang3.exception.ExceptionContext.getContextLabels()"""
        pass

    @abstractmethod
    def getContextValues(self, arg0: str):
        """public abstract java.util.List<java.lang.Object> org.apache.commons.lang3.exception.ExceptionContext.getContextValues(java.lang.String)"""
        pass

    @abstractmethod
    def setContextValue(self, arg0: str, arg1: object):
        """public abstract org.apache.commons.lang3.exception.ExceptionContext org.apache.commons.lang3.exception.ExceptionContext.setContextValue(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def getFormattedExceptionMessage(self, arg0: str):
        """public abstract java.lang.String org.apache.commons.lang3.exception.ExceptionContext.getFormattedExceptionMessage(java.lang.String)"""
        pass

    @abstractmethod
    def getContextEntries(self, ):
        """public abstract java.util.List<org.apache.commons.lang3.tuple.Pair<java.lang.String, java.lang.Object>> org.apache.commons.lang3.exception.ExceptionContext.getContextEntries()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.exception.DefaultExceptionContext
from builtins import str
import org.apache.commons.lang3.exception.DefaultExceptionContext as __DefaultExceptionContext
__DefaultExceptionContext = __DefaultExceptionContext
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.List as __List
__List = __List
import java.util.Set as Set
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
import java.util.List as List
from builtins import int
 
class DefaultExceptionContext(__ExceptionContext, ExceptionContext, __Serializable, Serializable):
    """org.apache.commons.lang3.exception.DefaultExceptionContext"""
 
    @staticmethod
    def __wrap(java_value: __DefaultExceptionContext) -> 'DefaultExceptionContext':
        return DefaultExceptionContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultExceptionContext):
        """
        Dynamic initializer for DefaultExceptionContext.
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
    def __init__(self, ):
        """public org.apache.commons.lang3.exception.DefaultExceptionContext()"""
        val = __DefaultExceptionContext()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setContextValue(self, arg0: str, arg1: object) -> 'DefaultExceptionContext':
        """public org.apache.commons.lang3.exception.DefaultExceptionContext org.apache.commons.lang3.exception.DefaultExceptionContext.setContextValue(java.lang.String,java.lang.Object)"""
        return 'DefaultExceptionContext'.__wrap(super(__DefaultExceptionContext, self).setContextValue(arg0, arg1))

    @overload
    def getContextValues(self, arg0: str) -> 'List':
        """public java.util.List<java.lang.Object> org.apache.commons.lang3.exception.DefaultExceptionContext.getContextValues(java.lang.String)"""
        return 'List'.__wrap(super(__DefaultExceptionContext, self).getContextValues(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getFirstContextValue(self, arg0: str) -> object:
        """public java.lang.Object org.apache.commons.lang3.exception.DefaultExceptionContext.getFirstContextValue(java.lang.String)"""
        return object.__wrap(super(__DefaultExceptionContext, self).getFirstContextValue(arg0))

    @override
    @overload
    def getContextEntries(self) -> 'List':
        """public java.util.List<org.apache.commons.lang3.tuple.Pair<java.lang.String, java.lang.Object>> org.apache.commons.lang3.exception.DefaultExceptionContext.getContextEntries()"""
        return 'List'.__wrap(super(DefaultExceptionContext, self).getContextEntries())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getContextLabels(self) -> 'Set':
        """public java.util.Set<java.lang.String> org.apache.commons.lang3.exception.DefaultExceptionContext.getContextLabels()"""
        return 'Set'.__wrap(super(DefaultExceptionContext, self).getContextLabels())

    @overload
    def getFormattedExceptionMessage(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.DefaultExceptionContext.getFormattedExceptionMessage(java.lang.String)"""
        return str.__wrap(super(__DefaultExceptionContext, self).getFormattedExceptionMessage(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def addContextValue(self, arg0: str, arg1: object) -> 'DefaultExceptionContext':
        """public org.apache.commons.lang3.exception.DefaultExceptionContext org.apache.commons.lang3.exception.DefaultExceptionContext.addContextValue(java.lang.String,java.lang.Object)"""
        return 'DefaultExceptionContext'.__wrap(super(__DefaultExceptionContext, self).addContextValue(arg0, arg1))

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
    def __init__(self):
        """public org.apache.commons.lang3.exception.DefaultExceptionContext()"""
        val = __DefaultExceptionContext()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.exception.ContextedRuntimeException
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.lang3.exception.ContextedRuntimeException as __ContextedRuntimeException
__ContextedRuntimeException = __ContextedRuntimeException
import java.util.Set as __Set
__Set = __Set
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class ContextedRuntimeException(__RuntimeException, RuntimeException, __ExceptionContext, ExceptionContext):
    """org.apache.commons.lang3.exception.ContextedRuntimeException"""
 
    @staticmethod
    def __wrap(java_value: __ContextedRuntimeException) -> 'ContextedRuntimeException':
        return ContextedRuntimeException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContextedRuntimeException):
        """
        Dynamic initializer for ContextedRuntimeException.
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
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def addContextValue(self, arg0: str, arg1: object) -> 'ContextedRuntimeException':
        """public org.apache.commons.lang3.exception.ContextedRuntimeException org.apache.commons.lang3.exception.ContextedRuntimeException.addContextValue(java.lang.String,java.lang.Object)"""
        return 'ContextedRuntimeException'.__wrap(super(__ContextedRuntimeException, self).addContextValue(arg0, arg1))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException(java.lang.String,java.lang.Throwable)"""
        val = __ContextedRuntimeException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getFirstContextValue(self, arg0: str) -> object:
        """public java.lang.Object org.apache.commons.lang3.exception.ContextedRuntimeException.getFirstContextValue(java.lang.String)"""
        return object.__wrap(super(__ContextedRuntimeException, self).getFirstContextValue(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def getContextValues(self, arg0: str) -> 'List':
        """public java.util.List<java.lang.Object> org.apache.commons.lang3.exception.ContextedRuntimeException.getContextValues(java.lang.String)"""
        return 'List'.__wrap(super(__ContextedRuntimeException, self).getContextValues(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable', arg2: 'ExceptionContext'):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException(java.lang.String,java.lang.Throwable,org.apache.commons.lang3.exception.ExceptionContext)"""
        val = __ContextedRuntimeException(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getContextLabels(self) -> 'Set':
        """public java.util.Set<java.lang.String> org.apache.commons.lang3.exception.ContextedRuntimeException.getContextLabels()"""
        return 'Set'.__wrap(super(ContextedRuntimeException, self).getContextLabels())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getFormattedExceptionMessage(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedRuntimeException.getFormattedExceptionMessage(java.lang.String)"""
        return str.__wrap(super(__ContextedRuntimeException, self).getFormattedExceptionMessage(arg0))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException(java.lang.String)"""
        val = __ContextedRuntimeException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getContextEntries(self) -> 'List':
        """public java.util.List<org.apache.commons.lang3.tuple.Pair<java.lang.String, java.lang.Object>> org.apache.commons.lang3.exception.ContextedRuntimeException.getContextEntries()"""
        return 'List'.__wrap(super(ContextedRuntimeException, self).getContextEntries())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException()"""
        val = __ContextedRuntimeException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedRuntimeException.getMessage()"""
        return str.__wrap(super(ContextedRuntimeException, self).getMessage())

    @overload
    def getRawMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedRuntimeException.getRawMessage()"""
        return str.__wrap(super(ContextedRuntimeException, self).getRawMessage())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException(java.lang.Throwable)"""
        val = __ContextedRuntimeException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setContextValue(self, arg0: str, arg1: object) -> 'ContextedRuntimeException':
        """public org.apache.commons.lang3.exception.ContextedRuntimeException org.apache.commons.lang3.exception.ContextedRuntimeException.setContextValue(java.lang.String,java.lang.Object)"""
        return 'ContextedRuntimeException'.__wrap(super(__ContextedRuntimeException, self).setContextValue(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException()"""
        val = __ContextedRuntimeException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.commons.lang3.exception.ContextedException
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import org.apache.commons.lang3.exception.ContextedException as __ContextedException
__ContextedException = __ContextedException
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class ContextedException(__Exception, Exception, __ExceptionContext, ExceptionContext):
    """org.apache.commons.lang3.exception.ContextedException"""
 
    @staticmethod
    def __wrap(java_value: __ContextedException) -> 'ContextedException':
        return ContextedException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContextedException):
        """
        Dynamic initializer for ContextedException.
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
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def getRawMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedException.getRawMessage()"""
        return str.__wrap(super(ContextedException, self).getRawMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.exception.ContextedException()"""
        val = __ContextedException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def getContextLabels(self) -> 'Set':
        """public java.util.Set<java.lang.String> org.apache.commons.lang3.exception.ContextedException.getContextLabels()"""
        return 'Set'.__wrap(super(ContextedException, self).getContextLabels())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedException.getMessage()"""
        return str.__wrap(super(ContextedException, self).getMessage())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getFormattedExceptionMessage(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedException.getFormattedExceptionMessage(java.lang.String)"""
        return str.__wrap(super(__ContextedException, self).getFormattedExceptionMessage(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable', arg2: 'ExceptionContext'):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.String,java.lang.Throwable,org.apache.commons.lang3.exception.ExceptionContext)"""
        val = __ContextedException(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.String,java.lang.Throwable)"""
        val = __ContextedException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setContextValue(self, arg0: str, arg1: object) -> 'ContextedException':
        """public org.apache.commons.lang3.exception.ContextedException org.apache.commons.lang3.exception.ContextedException.setContextValue(java.lang.String,java.lang.Object)"""
        return 'ContextedException'.__wrap(super(__ContextedException, self).setContextValue(arg0, arg1))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getContextEntries(self) -> 'List':
        """public java.util.List<org.apache.commons.lang3.tuple.Pair<java.lang.String, java.lang.Object>> org.apache.commons.lang3.exception.ContextedException.getContextEntries()"""
        return 'List'.__wrap(super(ContextedException, self).getContextEntries())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.exception.ContextedException()"""
        val = __ContextedException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getContextValues(self, arg0: str) -> 'List':
        """public java.util.List<java.lang.Object> org.apache.commons.lang3.exception.ContextedException.getContextValues(java.lang.String)"""
        return 'List'.__wrap(super(__ContextedException, self).getContextValues(arg0))

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @overload
    def addContextValue(self, arg0: str, arg1: object) -> 'ContextedException':
        """public org.apache.commons.lang3.exception.ContextedException org.apache.commons.lang3.exception.ContextedException.addContextValue(java.lang.String,java.lang.Object)"""
        return 'ContextedException'.__wrap(super(__ContextedException, self).addContextValue(arg0, arg1))

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.String)"""
        val = __ContextedException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def getFirstContextValue(self, arg0: str) -> object:
        """public java.lang.Object org.apache.commons.lang3.exception.ContextedException.getFirstContextValue(java.lang.String)"""
        return object.__wrap(super(__ContextedException, self).getFirstContextValue(arg0))

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.Throwable)"""
        val = __ContextedException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.commons.lang3.exception.UncheckedReflectiveOperationException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import org.apache.commons.lang3.exception.UncheckedReflectiveOperationException as __UncheckedReflectiveOperationException
__UncheckedReflectiveOperationException = __UncheckedReflectiveOperationException
from builtins import bool
from builtins import int
 
class UncheckedReflectiveOperationException(__UncheckedException, UncheckedException):
    """org.apache.commons.lang3.exception.UncheckedReflectiveOperationException"""
 
    @staticmethod
    def __wrap(java_value: __UncheckedReflectiveOperationException) -> 'UncheckedReflectiveOperationException':
        return UncheckedReflectiveOperationException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UncheckedReflectiveOperationException):
        """
        Dynamic initializer for UncheckedReflectiveOperationException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.UncheckedReflectiveOperationException(java.lang.Throwable)"""
        val = __UncheckedReflectiveOperationException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())