from __future__ import annotations
from overload import overload


 
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import org.apache.commons.lang3.exception.ContextedException as _ContextedException
_ContextedException = _ContextedException
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.util.Set as Set
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ContextedException():
    """org.apache.commons.lang3.exception.ContextedException"""
 
    @staticmethod
    def _wrap(java_value: _ContextedException) -> 'ContextedException':
        return ContextedException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ContextedException):
        """
        Dynamic initializer for ContextedException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ContextedException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ContextedException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getContextLabels(self) -> 'Set':
        """public java.util.Set<java.lang.String> org.apache.commons.lang3.exception.ContextedException.getContextLabels()"""
        return 'Set'._wrap(super(ContextedException, self).getContextLabels())

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
        """public org.apache.commons.lang3.exception.ContextedException()"""
        val = _ContextedException()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedException.getMessage()"""
        return str._wrap(super(ContextedException, self).getMessage())

    @overload
    def setContextValue(self, arg0: str, arg1: object) -> 'ContextedException':
        """public org.apache.commons.lang3.exception.ContextedException org.apache.commons.lang3.exception.ContextedException.setContextValue(java.lang.String,java.lang.Object)"""
        return 'ContextedException'._wrap(super(_ContextedException, self).setContextValue(arg0, arg1))

    @overload
    def getFormattedExceptionMessage(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedException.getFormattedExceptionMessage(java.lang.String)"""
        return str._wrap(super(_ContextedException, self).getFormattedExceptionMessage(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable', arg2: 'ExceptionContext'):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.String,java.lang.Throwable,org.apache.commons.lang3.exception.ExceptionContext)"""
        val = _ContextedException(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def getContextEntries(self) -> 'List':
        """public java.util.List<org.apache.commons.lang3.tuple.Pair<java.lang.String, java.lang.Object>> org.apache.commons.lang3.exception.ContextedException.getContextEntries()"""
        return 'List'._wrap(super(ContextedException, self).getContextEntries())

    @overload
    def getContextValues(self, arg0: str) -> 'List':
        """public java.util.List<java.lang.Object> org.apache.commons.lang3.exception.ContextedException.getContextValues(java.lang.String)"""
        return 'List'._wrap(super(_ContextedException, self).getContextValues(arg0))

    @overload
    def addContextValue(self, arg0: str, arg1: object) -> 'ContextedException':
        """public org.apache.commons.lang3.exception.ContextedException org.apache.commons.lang3.exception.ContextedException.addContextValue(java.lang.String,java.lang.Object)"""
        return 'ContextedException'._wrap(super(_ContextedException, self).addContextValue(arg0, arg1))

    @overload
    def getRawMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedException.getRawMessage()"""
        return str._wrap(super(ContextedException, self).getRawMessage())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getFirstContextValue(self, arg0: str) -> object:
        """public java.lang.Object org.apache.commons.lang3.exception.ContextedException.getFirstContextValue(java.lang.String)"""
        return object._wrap(super(_ContextedException, self).getFirstContextValue(arg0))

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.String,java.lang.Throwable)"""
        val = _ContextedException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.Throwable)"""
        val = _ContextedException(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.exception.ContextedException()"""
        val = _ContextedException()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.String)"""
        val = _ContextedException(arg0)
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.lang3.exception.ContextedException
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import org.apache.commons.lang3.exception.ContextedException as _ContextedException
_ContextedException = _ContextedException
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.util.Set as Set
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ContextedException():
    """org.apache.commons.lang3.exception.ContextedException"""
 
    @staticmethod
    def _wrap(java_value: _ContextedException) -> 'ContextedException':
        return ContextedException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ContextedException):
        """
        Dynamic initializer for ContextedException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ContextedException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ContextedException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getContextLabels(self) -> 'Set':
        """public java.util.Set<java.lang.String> org.apache.commons.lang3.exception.ContextedException.getContextLabels()"""
        return 'Set'._wrap(super(ContextedException, self).getContextLabels())

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
        """public org.apache.commons.lang3.exception.ContextedException()"""
        val = _ContextedException()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedException.getMessage()"""
        return str._wrap(super(ContextedException, self).getMessage())

    @overload
    def setContextValue(self, arg0: str, arg1: object) -> 'ContextedException':
        """public org.apache.commons.lang3.exception.ContextedException org.apache.commons.lang3.exception.ContextedException.setContextValue(java.lang.String,java.lang.Object)"""
        return 'ContextedException'._wrap(super(_ContextedException, self).setContextValue(arg0, arg1))

    @overload
    def getFormattedExceptionMessage(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedException.getFormattedExceptionMessage(java.lang.String)"""
        return str._wrap(super(_ContextedException, self).getFormattedExceptionMessage(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable', arg2: 'ExceptionContext'):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.String,java.lang.Throwable,org.apache.commons.lang3.exception.ExceptionContext)"""
        val = _ContextedException(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def getContextEntries(self) -> 'List':
        """public java.util.List<org.apache.commons.lang3.tuple.Pair<java.lang.String, java.lang.Object>> org.apache.commons.lang3.exception.ContextedException.getContextEntries()"""
        return 'List'._wrap(super(ContextedException, self).getContextEntries())

    @overload
    def getContextValues(self, arg0: str) -> 'List':
        """public java.util.List<java.lang.Object> org.apache.commons.lang3.exception.ContextedException.getContextValues(java.lang.String)"""
        return 'List'._wrap(super(_ContextedException, self).getContextValues(arg0))

    @overload
    def addContextValue(self, arg0: str, arg1: object) -> 'ContextedException':
        """public org.apache.commons.lang3.exception.ContextedException org.apache.commons.lang3.exception.ContextedException.addContextValue(java.lang.String,java.lang.Object)"""
        return 'ContextedException'._wrap(super(_ContextedException, self).addContextValue(arg0, arg1))

    @overload
    def getRawMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedException.getRawMessage()"""
        return str._wrap(super(ContextedException, self).getRawMessage())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getFirstContextValue(self, arg0: str) -> object:
        """public java.lang.Object org.apache.commons.lang3.exception.ContextedException.getFirstContextValue(java.lang.String)"""
        return object._wrap(super(_ContextedException, self).getFirstContextValue(arg0))

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.String,java.lang.Throwable)"""
        val = _ContextedException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.Throwable)"""
        val = _ContextedException(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.exception.ContextedException()"""
        val = _ContextedException()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.exception.ContextedException(java.lang.String)"""
        val = _ContextedException(arg0)
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.lang3.exception.ContextedException 
 
 
# CLASS: org.apache.commons.lang3.exception.ExceptionUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.exception.ExceptionUtils as _ExceptionUtils
_ExceptionUtils = _ExceptionUtils
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
import java.util.function.Consumer as Consumer
from typing import List
import java.lang.Integer as _int
import java.io.PrintStream as PrintStream
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.lang.Throwable as Throwable
import java.util.stream.Stream as Stream
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ExceptionUtils():
    """org.apache.commons.lang3.exception.ExceptionUtils"""
 
    @staticmethod
    def _wrap(java_value: _ExceptionUtils) -> 'ExceptionUtils':
        return ExceptionUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExceptionUtils):
        """
        Dynamic initializer for ExceptionUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExceptionUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExceptionUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public org.apache.commons.lang3.exception.ExceptionUtils()"""
        val = _ExceptionUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def getMessage(arg0: 'Throwable') -> str:
        """public static java.lang.String org.apache.commons.lang3.exception.ExceptionUtils.getMessage(java.lang.Throwable)"""
        return str._wrap(_ExceptionUtils.getMessage(arg0))

    @staticmethod
    @overload
    def getStackFrames(arg0: 'Throwable') -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.exception.ExceptionUtils.getStackFrames(java.lang.Throwable)"""
        return List[str]._wrap(_ExceptionUtils.getStackFrames(arg0))

    @staticmethod
    @overload
    def throwableOfType(arg0: 'Throwable', arg1: 'Class', arg2: int) -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfType(java.lang.Throwable,java.lang.Class<T>,int)"""
        return Throwable._wrap(_ExceptionUtils.throwableOfType(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def getCause(arg0: 'Throwable') -> 'Throwable':
        """public static java.lang.Throwable org.apache.commons.lang3.exception.ExceptionUtils.getCause(java.lang.Throwable)"""
        return Throwable._wrap(_ExceptionUtils.getCause(arg0))

    @staticmethod
    @overload
    def getRootCauseStackTrace(arg0: 'Throwable') -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.exception.ExceptionUtils.getRootCauseStackTrace(java.lang.Throwable)"""
        return List[str]._wrap(_ExceptionUtils.getRootCauseStackTrace(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def printRootCauseStackTrace(arg0: 'Throwable', arg1: 'PrintWriter'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.printRootCauseStackTrace(java.lang.Throwable,java.io.PrintWriter)"""
        _ExceptionUtils.printRootCauseStackTrace(arg0, arg1)

    @staticmethod
    @overload
    def getCause(arg0: 'Throwable', arg1: 'String') -> 'Throwable':
        """public static java.lang.Throwable org.apache.commons.lang3.exception.ExceptionUtils.getCause(java.lang.Throwable,java.lang.String[])"""
        return Throwable._wrap(_ExceptionUtils.getCause(arg0, arg1))

    @staticmethod
    @overload
    def isChecked(arg0: 'Throwable') -> bool:
        """public static boolean org.apache.commons.lang3.exception.ExceptionUtils.isChecked(java.lang.Throwable)"""
        return bool._wrap(_ExceptionUtils.isChecked(arg0))

    @staticmethod
    @overload
    def removeCommonFrames(arg0: 'List', arg1: 'List'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.removeCommonFrames(java.util.List<java.lang.String>,java.util.List<java.lang.String>)"""
        _ExceptionUtils.removeCommonFrames(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getThrowableCount(arg0: 'Throwable') -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.getThrowableCount(java.lang.Throwable)"""
        return int._wrap(_ExceptionUtils.getThrowableCount(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def stream(arg0: 'Throwable') -> 'Stream':
        """public static java.util.stream.Stream<java.lang.Throwable> org.apache.commons.lang3.exception.ExceptionUtils.stream(java.lang.Throwable)"""
        return Stream._wrap(_ExceptionUtils.stream(arg0))

    @staticmethod
    @overload
    def getThrowables(arg0: 'Throwable') -> List['Throwable']:
        """public static java.lang.Throwable[] org.apache.commons.lang3.exception.ExceptionUtils.getThrowables(java.lang.Throwable)"""
        return List[Throwable]._wrap(_ExceptionUtils.getThrowables(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.exception.ExceptionUtils()"""
        val = _ExceptionUtils()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def throwUnchecked(arg0: object) -> object:
        """public static <T> T org.apache.commons.lang3.exception.ExceptionUtils.throwUnchecked(T)"""
        return object._wrap(_ExceptionUtils.throwUnchecked(arg0))

    @staticmethod
    @overload
    def rethrow(arg0: 'Throwable') -> object:
        """public static <R> R org.apache.commons.lang3.exception.ExceptionUtils.rethrow(java.lang.Throwable)"""
        return object._wrap(_ExceptionUtils.rethrow(arg0))

    @staticmethod
    @overload
    def throwableOfThrowable(arg0: 'Throwable', arg1: 'Class') -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfThrowable(java.lang.Throwable,java.lang.Class<T>)"""
        return Throwable._wrap(_ExceptionUtils.throwableOfThrowable(arg0, arg1))

    @staticmethod
    @overload
    def getRootCauseMessage(arg0: 'Throwable') -> str:
        """public static java.lang.String org.apache.commons.lang3.exception.ExceptionUtils.getRootCauseMessage(java.lang.Throwable)"""
        return str._wrap(_ExceptionUtils.getRootCauseMessage(arg0))

    @staticmethod
    @overload
    def hasCause(arg0: 'Throwable', arg1: 'Class') -> bool:
        """public static boolean org.apache.commons.lang3.exception.ExceptionUtils.hasCause(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>)"""
        return bool._wrap(_ExceptionUtils.hasCause(arg0, arg1))

    @staticmethod
    @overload
    def getRootCause(arg0: 'Throwable') -> 'Throwable':
        """public static java.lang.Throwable org.apache.commons.lang3.exception.ExceptionUtils.getRootCause(java.lang.Throwable)"""
        return Throwable._wrap(_ExceptionUtils.getRootCause(arg0))

    @staticmethod
    @overload
    def getRootCauseStackTraceList(arg0: 'Throwable') -> 'List':
        """public static java.util.List<java.lang.String> org.apache.commons.lang3.exception.ExceptionUtils.getRootCauseStackTraceList(java.lang.Throwable)"""
        return List._wrap(_ExceptionUtils.getRootCauseStackTraceList(arg0))

    @staticmethod
    @overload
    def indexOfType(arg0: 'Throwable', arg1: 'Class', arg2: int) -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfType(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>,int)"""
        return int._wrap(_ExceptionUtils.indexOfType(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def indexOfType(arg0: 'Throwable', arg1: 'Class') -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfType(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>)"""
        return int._wrap(_ExceptionUtils.indexOfType(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def indexOfThrowable(arg0: 'Throwable', arg1: 'Class', arg2: int) -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfThrowable(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>,int)"""
        return int._wrap(_ExceptionUtils.indexOfThrowable(arg0, arg1, _int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def wrapAndThrow(arg0: 'Throwable') -> object:
        """public static <R> R org.apache.commons.lang3.exception.ExceptionUtils.wrapAndThrow(java.lang.Throwable)"""
        return object._wrap(_ExceptionUtils.wrapAndThrow(arg0))

    @staticmethod
    @overload
    def isUnchecked(arg0: 'Throwable') -> bool:
        """public static boolean org.apache.commons.lang3.exception.ExceptionUtils.isUnchecked(java.lang.Throwable)"""
        return bool._wrap(_ExceptionUtils.isUnchecked(arg0))

    @staticmethod
    @overload
    def printRootCauseStackTrace(arg0: 'Throwable'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.printRootCauseStackTrace(java.lang.Throwable)"""
        _ExceptionUtils.printRootCauseStackTrace(arg0)

    @staticmethod
    @overload
    def indexOfThrowable(arg0: 'Throwable', arg1: 'Class') -> int:
        """public static int org.apache.commons.lang3.exception.ExceptionUtils.indexOfThrowable(java.lang.Throwable,java.lang.Class<? extends java.lang.Throwable>)"""
        return int._wrap(_ExceptionUtils.indexOfThrowable(arg0, arg1))

    @staticmethod
    @overload
    def getThrowableList(arg0: 'Throwable') -> 'List':
        """public static java.util.List<java.lang.Throwable> org.apache.commons.lang3.exception.ExceptionUtils.getThrowableList(java.lang.Throwable)"""
        return List._wrap(_ExceptionUtils.getThrowableList(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getStackTrace(arg0: 'Throwable') -> str:
        """public static java.lang.String org.apache.commons.lang3.exception.ExceptionUtils.getStackTrace(java.lang.Throwable)"""
        return str._wrap(_ExceptionUtils.getStackTrace(arg0))

    @staticmethod
    @overload
    def throwableOfType(arg0: 'Throwable', arg1: 'Class') -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfType(java.lang.Throwable,java.lang.Class<T>)"""
        return Throwable._wrap(_ExceptionUtils.throwableOfType(arg0, arg1))

    @staticmethod
    @overload
    def forEach(arg0: 'Throwable', arg1: 'Consumer'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.forEach(java.lang.Throwable,java.util.function.Consumer<java.lang.Throwable>)"""
        _ExceptionUtils.forEach(arg0, arg1)

    @staticmethod
    @overload
    def printRootCauseStackTrace(arg0: 'Throwable', arg1: 'PrintStream'):
        """public static void org.apache.commons.lang3.exception.ExceptionUtils.printRootCauseStackTrace(java.lang.Throwable,java.io.PrintStream)"""
        _ExceptionUtils.printRootCauseStackTrace(arg0, arg1)

    @staticmethod
    @overload
    def getDefaultCauseMethodNames() -> List[str]:
        """public static java.lang.String[] org.apache.commons.lang3.exception.ExceptionUtils.getDefaultCauseMethodNames()"""
        return List[str]._wrap(_ExceptionUtils.getDefaultCauseMethodNames())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def throwableOfThrowable(arg0: 'Throwable', arg1: 'Class', arg2: int) -> 'Throwable':
        """public static <T extends java.lang.Throwable> T org.apache.commons.lang3.exception.ExceptionUtils.throwableOfThrowable(java.lang.Throwable,java.lang.Class<T>,int)"""
        return Throwable._wrap(_ExceptionUtils.throwableOfThrowable(arg0, arg1, _int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.exception.ContextedRuntimeException
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import org.apache.commons.lang3.exception.ContextedRuntimeException as _ContextedRuntimeException
_ContextedRuntimeException = _ContextedRuntimeException
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.util.Set as Set
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ContextedRuntimeException():
    """org.apache.commons.lang3.exception.ContextedRuntimeException"""
 
    @staticmethod
    def _wrap(java_value: _ContextedRuntimeException) -> 'ContextedRuntimeException':
        return ContextedRuntimeException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ContextedRuntimeException):
        """
        Dynamic initializer for ContextedRuntimeException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ContextedRuntimeException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ContextedRuntimeException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def getFirstContextValue(self, arg0: str) -> object:
        """public java.lang.Object org.apache.commons.lang3.exception.ContextedRuntimeException.getFirstContextValue(java.lang.String)"""
        return object._wrap(super(_ContextedRuntimeException, self).getFirstContextValue(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getContextEntries(self) -> 'List':
        """public java.util.List<org.apache.commons.lang3.tuple.Pair<java.lang.String, java.lang.Object>> org.apache.commons.lang3.exception.ContextedRuntimeException.getContextEntries()"""
        return 'List'._wrap(super(ContextedRuntimeException, self).getContextEntries())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException(java.lang.Throwable)"""
        val = _ContextedRuntimeException(arg0)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def addContextValue(self, arg0: str, arg1: object) -> 'ContextedRuntimeException':
        """public org.apache.commons.lang3.exception.ContextedRuntimeException org.apache.commons.lang3.exception.ContextedRuntimeException.addContextValue(java.lang.String,java.lang.Object)"""
        return 'ContextedRuntimeException'._wrap(super(_ContextedRuntimeException, self).addContextValue(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException(java.lang.String,java.lang.Throwable)"""
        val = _ContextedRuntimeException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getContextLabels(self) -> 'Set':
        """public java.util.Set<java.lang.String> org.apache.commons.lang3.exception.ContextedRuntimeException.getContextLabels()"""
        return 'Set'._wrap(super(ContextedRuntimeException, self).getContextLabels())

    @overload
    def getFormattedExceptionMessage(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedRuntimeException.getFormattedExceptionMessage(java.lang.String)"""
        return str._wrap(super(_ContextedRuntimeException, self).getFormattedExceptionMessage(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException()"""
        val = _ContextedRuntimeException()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable', arg2: 'ExceptionContext'):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException(java.lang.String,java.lang.Throwable,org.apache.commons.lang3.exception.ExceptionContext)"""
        val = _ContextedRuntimeException(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException()"""
        val = _ContextedRuntimeException()
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedRuntimeException.getMessage()"""
        return str._wrap(super(ContextedRuntimeException, self).getMessage())

    @overload
    def getContextValues(self, arg0: str) -> 'List':
        """public java.util.List<java.lang.Object> org.apache.commons.lang3.exception.ContextedRuntimeException.getContextValues(java.lang.String)"""
        return 'List'._wrap(super(_ContextedRuntimeException, self).getContextValues(arg0))

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.exception.ContextedRuntimeException(java.lang.String)"""
        val = _ContextedRuntimeException(arg0)
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @overload
    def setContextValue(self, arg0: str, arg1: object) -> 'ContextedRuntimeException':
        """public org.apache.commons.lang3.exception.ContextedRuntimeException org.apache.commons.lang3.exception.ContextedRuntimeException.setContextValue(java.lang.String,java.lang.Object)"""
        return 'ContextedRuntimeException'._wrap(super(_ContextedRuntimeException, self).setContextValue(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getRawMessage(self) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.ContextedRuntimeException.getRawMessage()"""
        return str._wrap(super(ContextedRuntimeException, self).getRawMessage())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.exception.UncheckedReflectiveOperationException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import org.apache.commons.lang3.exception.UncheckedReflectiveOperationException as _UncheckedReflectiveOperationException
_UncheckedReflectiveOperationException = _UncheckedReflectiveOperationException
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UncheckedReflectiveOperationException():
    """org.apache.commons.lang3.exception.UncheckedReflectiveOperationException"""
 
    @staticmethod
    def _wrap(java_value: _UncheckedReflectiveOperationException) -> 'UncheckedReflectiveOperationException':
        return UncheckedReflectiveOperationException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UncheckedReflectiveOperationException):
        """
        Dynamic initializer for UncheckedReflectiveOperationException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UncheckedReflectiveOperationException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UncheckedReflectiveOperationException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.UncheckedReflectiveOperationException(java.lang.Throwable)"""
        val = _UncheckedReflectiveOperationException(arg0)
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.exception.DefaultExceptionContext
from builtins import str
from pyquantum_helper import override
import org.apache.commons.lang3.exception.DefaultExceptionContext as _DefaultExceptionContext
_DefaultExceptionContext = _DefaultExceptionContext
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.util.Set as Set
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultExceptionContext():
    """org.apache.commons.lang3.exception.DefaultExceptionContext"""
 
    @staticmethod
    def _wrap(java_value: _DefaultExceptionContext) -> 'DefaultExceptionContext':
        return DefaultExceptionContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultExceptionContext):
        """
        Dynamic initializer for DefaultExceptionContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultExceptionContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultExceptionContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addContextValue(self, arg0: str, arg1: object) -> 'DefaultExceptionContext':
        """public org.apache.commons.lang3.exception.DefaultExceptionContext org.apache.commons.lang3.exception.DefaultExceptionContext.addContextValue(java.lang.String,java.lang.Object)"""
        return 'DefaultExceptionContext'._wrap(super(_DefaultExceptionContext, self).addContextValue(arg0, arg1))

    @override
    @overload
    def getContextEntries(self) -> 'List':
        """public java.util.List<org.apache.commons.lang3.tuple.Pair<java.lang.String, java.lang.Object>> org.apache.commons.lang3.exception.DefaultExceptionContext.getContextEntries()"""
        return 'List'._wrap(super(DefaultExceptionContext, self).getContextEntries())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getContextValues(self, arg0: str) -> 'List':
        """public java.util.List<java.lang.Object> org.apache.commons.lang3.exception.DefaultExceptionContext.getContextValues(java.lang.String)"""
        return 'List'._wrap(super(_DefaultExceptionContext, self).getContextValues(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getContextLabels(self) -> 'Set':
        """public java.util.Set<java.lang.String> org.apache.commons.lang3.exception.DefaultExceptionContext.getContextLabels()"""
        return 'Set'._wrap(super(DefaultExceptionContext, self).getContextLabels())

    @overload
    def getFirstContextValue(self, arg0: str) -> object:
        """public java.lang.Object org.apache.commons.lang3.exception.DefaultExceptionContext.getFirstContextValue(java.lang.String)"""
        return object._wrap(super(_DefaultExceptionContext, self).getFirstContextValue(arg0))

    @overload
    def getFormattedExceptionMessage(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.exception.DefaultExceptionContext.getFormattedExceptionMessage(java.lang.String)"""
        return str._wrap(super(_DefaultExceptionContext, self).getFormattedExceptionMessage(arg0))

    @overload
    def setContextValue(self, arg0: str, arg1: object) -> 'DefaultExceptionContext':
        """public org.apache.commons.lang3.exception.DefaultExceptionContext org.apache.commons.lang3.exception.DefaultExceptionContext.setContextValue(java.lang.String,java.lang.Object)"""
        return 'DefaultExceptionContext'._wrap(super(_DefaultExceptionContext, self).setContextValue(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.exception.DefaultExceptionContext()"""
        val = _DefaultExceptionContext()
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
    def __init__(self):
        """public org.apache.commons.lang3.exception.DefaultExceptionContext()"""
        val = _DefaultExceptionContext()
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
 
 
# CLASS: org.apache.commons.lang3.exception.UncheckedIllegalAccessException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.exception.UncheckedIllegalAccessException as _UncheckedIllegalAccessException
_UncheckedIllegalAccessException = _UncheckedIllegalAccessException
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UncheckedIllegalAccessException():
    """org.apache.commons.lang3.exception.UncheckedIllegalAccessException"""
 
    @staticmethod
    def _wrap(java_value: _UncheckedIllegalAccessException) -> 'UncheckedIllegalAccessException':
        return UncheckedIllegalAccessException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UncheckedIllegalAccessException):
        """
        Dynamic initializer for UncheckedIllegalAccessException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UncheckedIllegalAccessException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UncheckedIllegalAccessException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.UncheckedIllegalAccessException(java.lang.Throwable)"""
        val = _UncheckedIllegalAccessException(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.exception.UncheckedInterruptedException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import org.apache.commons.lang3.exception.UncheckedInterruptedException as _UncheckedInterruptedException
_UncheckedInterruptedException = _UncheckedInterruptedException
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UncheckedInterruptedException():
    """org.apache.commons.lang3.exception.UncheckedInterruptedException"""
 
    @staticmethod
    def _wrap(java_value: _UncheckedInterruptedException) -> 'UncheckedInterruptedException':
        return UncheckedInterruptedException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UncheckedInterruptedException):
        """
        Dynamic initializer for UncheckedInterruptedException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UncheckedInterruptedException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UncheckedInterruptedException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.UncheckedInterruptedException(java.lang.Throwable)"""
        val = _UncheckedInterruptedException(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.exception.UncheckedException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
import org.apache.commons.lang3.exception.UncheckedException as _UncheckedException
_UncheckedException = _UncheckedException
from typing import List
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UncheckedException():
    """org.apache.commons.lang3.exception.UncheckedException"""
 
    @staticmethod
    def _wrap(java_value: _UncheckedException) -> 'UncheckedException':
        return UncheckedException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UncheckedException):
        """
        Dynamic initializer for UncheckedException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UncheckedException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UncheckedException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.UncheckedException(java.lang.Throwable)"""
        val = _UncheckedException(arg0)
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.exception.CloneFailedException
import org.apache.commons.lang3.exception.CloneFailedException as _CloneFailedException
_CloneFailedException = _CloneFailedException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CloneFailedException():
    """org.apache.commons.lang3.exception.CloneFailedException"""
 
    @staticmethod
    def _wrap(java_value: _CloneFailedException) -> 'CloneFailedException':
        return CloneFailedException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CloneFailedException):
        """
        Dynamic initializer for CloneFailedException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CloneFailedException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CloneFailedException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.exception.CloneFailedException(java.lang.Throwable)"""
        val = _CloneFailedException(arg0)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.exception.CloneFailedException(java.lang.String,java.lang.Throwable)"""
        val = _CloneFailedException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.exception.CloneFailedException(java.lang.String)"""
        val = _CloneFailedException(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.exception.ExceptionContext
import org.apache.commons.lang3.exception.ExceptionContext as _ExceptionContext
_ExceptionContext = _ExceptionContext
from abc import abstractmethod, ABC
 
class ExceptionContext():
    """org.apache.commons.lang3.exception.ExceptionContext"""
 
    @staticmethod
    def _wrap(java_value: _ExceptionContext) -> 'ExceptionContext':
        return ExceptionContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExceptionContext):
        """
        Dynamic initializer for ExceptionContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExceptionContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExceptionContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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