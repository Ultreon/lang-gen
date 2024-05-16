from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import dev.ultreon.quantum.crash.CrashLog as _CrashLog
_CrashLog = _CrashLog
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import dev.ultreon.quantum.util.Result as _Result
_Result = _Result
import java.io.OutputStream as OutputStream
import dev.ultreon.quantum.crash.ApplicationCrash as _ApplicationCrash
_ApplicationCrash = _ApplicationCrash
import java.lang.Integer as _int
import dev.ultreon.quantum.crash.CrashCategory as _CrashCategory
_CrashCategory = _CrashCategory
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrashLog():
    """dev.ultreon.quantum.crash.CrashLog"""
 
    @staticmethod
    def _wrap(java_value: _CrashLog) -> 'CrashLog':
        return CrashLog(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CrashLog):
        """
        Dynamic initializer for CrashLog.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CrashLog__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CrashLog__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getFileNameWithoutExt() -> str:
        """public static java.lang.String dev.ultreon.quantum.crash.CrashLog.getFileNameWithoutExt()"""
        return str._wrap(_CrashLog.getFileNameWithoutExt())

    @overload
    def addLog(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.crash.CrashLog.addLog(dev.ultreon.quantum.crash.CrashLog)"""
        super(_CrashLog, self).addLog(arg0)

    @overload
    def writeToStream(self, arg0: 'OutputStream'):
        """public void dev.ultreon.quantum.crash.CrashLog.writeToStream(java.io.OutputStream) throws java.io.IOException"""
        super(_CrashLog, self).writeToStream(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def writeToFile(self, arg0: 'File') -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.crash.CrashLog.writeToFile(java.io.File)"""
        return 'util.Result'._wrap(super(_CrashLog, self).writeToFile(arg0))

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
    def getDetails(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashCategory.getDetails()"""
        return str._wrap(super(CrashCategory, self).getDetails())

    @overload
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.crash.CrashCategory> dev.ultreon.quantum.crash.CrashLog.getCategories()"""
        return 'List'._wrap(super(CrashLog, self).getCategories())

    @overload
    def defaultSave(self) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.crash.CrashLog.defaultSave()"""
        return 'util.Result'._wrap(super(CrashLog, self).defaultSave())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def createCrash(self) -> 'ApplicationCrash':
        """public dev.ultreon.quantum.crash.ApplicationCrash dev.ultreon.quantum.crash.CrashLog.createCrash()"""
        return 'ApplicationCrash'._wrap(super(CrashLog, self).createCrash())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,java.lang.Throwable)"""
        val = _CrashLog(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashLog.toString()"""
        return str._wrap(super(CrashLog, self).toString())

    @override
    @overload
    def add(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.crash.CrashCategory.add(java.lang.String,java.lang.Object)"""
        super(_CrashCategory, self).add(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.crash.CrashLog.getThrowable()"""
        return 'Throwable'._wrap(super(CrashLog, self).getThrowable())

    @overload
    def __init__(self, arg0: str, arg1: 'CrashLog', arg2: 'Throwable'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,dev.ultreon.quantum.crash.CrashLog,java.lang.Throwable)"""
        val = _CrashLog(arg0, arg1, arg2)
        self.__wrapper = val

    @staticmethod
    @overload
    def getFileName() -> str:
        """public static java.lang.String dev.ultreon.quantum.crash.CrashLog.getFileName()"""
        return str._wrap(_CrashLog.getFileName())

    @overload
    def writeToLog(self):
        """public void dev.ultreon.quantum.crash.CrashLog.writeToLog()"""
        super(CrashLog, self).writeToLog()

    @overload
    def addCategory(self, arg0: 'CrashCategory'):
        """public void dev.ultreon.quantum.crash.CrashLog.addCategory(dev.ultreon.quantum.crash.CrashCategory)"""
        super(_CrashLog, self).addCategory(arg0)

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
    def __init__(self, arg0: str, arg1: 'CrashLog'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,dev.ultreon.quantum.crash.CrashLog)"""
        val = _CrashLog(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.crash.CrashLog
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import dev.ultreon.quantum.crash.CrashLog as _CrashLog
_CrashLog = _CrashLog
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import dev.ultreon.quantum.util.Result as _Result
_Result = _Result
import java.io.OutputStream as OutputStream
import dev.ultreon.quantum.crash.ApplicationCrash as _ApplicationCrash
_ApplicationCrash = _ApplicationCrash
import java.lang.Integer as _int
import dev.ultreon.quantum.crash.CrashCategory as _CrashCategory
_CrashCategory = _CrashCategory
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrashLog():
    """dev.ultreon.quantum.crash.CrashLog"""
 
    @staticmethod
    def _wrap(java_value: _CrashLog) -> 'CrashLog':
        return CrashLog(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CrashLog):
        """
        Dynamic initializer for CrashLog.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CrashLog__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CrashLog__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getFileNameWithoutExt() -> str:
        """public static java.lang.String dev.ultreon.quantum.crash.CrashLog.getFileNameWithoutExt()"""
        return str._wrap(_CrashLog.getFileNameWithoutExt())

    @overload
    def addLog(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.crash.CrashLog.addLog(dev.ultreon.quantum.crash.CrashLog)"""
        super(_CrashLog, self).addLog(arg0)

    @overload
    def writeToStream(self, arg0: 'OutputStream'):
        """public void dev.ultreon.quantum.crash.CrashLog.writeToStream(java.io.OutputStream) throws java.io.IOException"""
        super(_CrashLog, self).writeToStream(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def writeToFile(self, arg0: 'File') -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.crash.CrashLog.writeToFile(java.io.File)"""
        return 'util.Result'._wrap(super(_CrashLog, self).writeToFile(arg0))

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
    def getDetails(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashCategory.getDetails()"""
        return str._wrap(super(CrashCategory, self).getDetails())

    @overload
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.crash.CrashCategory> dev.ultreon.quantum.crash.CrashLog.getCategories()"""
        return 'List'._wrap(super(CrashLog, self).getCategories())

    @overload
    def defaultSave(self) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.crash.CrashLog.defaultSave()"""
        return 'util.Result'._wrap(super(CrashLog, self).defaultSave())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def createCrash(self) -> 'ApplicationCrash':
        """public dev.ultreon.quantum.crash.ApplicationCrash dev.ultreon.quantum.crash.CrashLog.createCrash()"""
        return 'ApplicationCrash'._wrap(super(CrashLog, self).createCrash())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,java.lang.Throwable)"""
        val = _CrashLog(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashLog.toString()"""
        return str._wrap(super(CrashLog, self).toString())

    @override
    @overload
    def add(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.crash.CrashCategory.add(java.lang.String,java.lang.Object)"""
        super(_CrashCategory, self).add(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.crash.CrashLog.getThrowable()"""
        return 'Throwable'._wrap(super(CrashLog, self).getThrowable())

    @overload
    def __init__(self, arg0: str, arg1: 'CrashLog', arg2: 'Throwable'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,dev.ultreon.quantum.crash.CrashLog,java.lang.Throwable)"""
        val = _CrashLog(arg0, arg1, arg2)
        self.__wrapper = val

    @staticmethod
    @overload
    def getFileName() -> str:
        """public static java.lang.String dev.ultreon.quantum.crash.CrashLog.getFileName()"""
        return str._wrap(_CrashLog.getFileName())

    @overload
    def writeToLog(self):
        """public void dev.ultreon.quantum.crash.CrashLog.writeToLog()"""
        super(CrashLog, self).writeToLog()

    @overload
    def addCategory(self, arg0: 'CrashCategory'):
        """public void dev.ultreon.quantum.crash.CrashLog.addCategory(dev.ultreon.quantum.crash.CrashCategory)"""
        super(_CrashLog, self).addCategory(arg0)

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
    def __init__(self, arg0: str, arg1: 'CrashLog'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,dev.ultreon.quantum.crash.CrashLog)"""
        val = _CrashLog(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.crash.CrashLog 
 
 
# CLASS: dev.ultreon.quantum.crash.ApplicationCrash
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import java.io.PrintWriter as PrintWriter
import dev.ultreon.quantum.crash.CrashLog as _CrashLog
_CrashLog = _CrashLog
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import dev.ultreon.quantum.crash.ApplicationCrash as _ApplicationCrash
_ApplicationCrash = _ApplicationCrash
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
 
class ApplicationCrash():
    """dev.ultreon.quantum.crash.ApplicationCrash"""
 
    @staticmethod
    def _wrap(java_value: _ApplicationCrash) -> 'ApplicationCrash':
        return ApplicationCrash(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ApplicationCrash):
        """
        Dynamic initializer for ApplicationCrash.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ApplicationCrash__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ApplicationCrash__wrapper":
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
    def __init__(self, arg0: 'CrashLog'):
        """public dev.ultreon.quantum.crash.ApplicationCrash(dev.ultreon.quantum.crash.CrashLog)"""
        val = _ApplicationCrash(arg0)
        self.__wrapper = val

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
    def printCrash(self):
        """public void dev.ultreon.quantum.crash.ApplicationCrash.printCrash()"""
        super(ApplicationCrash, self).printCrash()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def handleCrash(self):
        """public void dev.ultreon.quantum.crash.ApplicationCrash.handleCrash()"""
        super(ApplicationCrash, self).handleCrash()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.ApplicationCrash.toString()"""
        return str._wrap(super(ApplicationCrash, self).toString())

    @overload
    def getCrashLog(self) -> 'CrashLog':
        """public dev.ultreon.quantum.crash.CrashLog dev.ultreon.quantum.crash.ApplicationCrash.getCrashLog()"""
        return 'CrashLog'._wrap(super(ApplicationCrash, self).getCrashLog())

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

    @staticmethod
    @overload
    def onCrash(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.crash.ApplicationCrash.onCrash(java.lang.Runnable)"""
        _ApplicationCrash.onCrash(arg0)

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.crash.CrashException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.crash.CrashException as _CrashException
_CrashException = _CrashException
import java.io.PrintWriter as PrintWriter
import dev.ultreon.quantum.crash.CrashLog as _CrashLog
_CrashLog = _CrashLog
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
 
class CrashException():
    """dev.ultreon.quantum.crash.CrashException"""
 
    @staticmethod
    def _wrap(java_value: _CrashException) -> 'CrashException':
        return CrashException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CrashException):
        """
        Dynamic initializer for CrashException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CrashException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CrashException__wrapper":
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

    @overload
    def __init__(self, arg0: 'CrashLog'):
        """public dev.ultreon.quantum.crash.CrashException(dev.ultreon.quantum.crash.CrashLog)"""
        val = _CrashException(arg0)
        self.__wrapper = val

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
    def __init__(self, arg0: 'CrashLog', arg1: str):
        """public dev.ultreon.quantum.crash.CrashException(dev.ultreon.quantum.crash.CrashLog,java.lang.String)"""
        val = _CrashException(arg0, arg1)
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

    @overload
    def getCrashLog(self) -> 'CrashLog':
        """public dev.ultreon.quantum.crash.CrashLog dev.ultreon.quantum.crash.CrashException.getCrashLog()"""
        return 'CrashLog'._wrap(super(CrashException, self).getCrashLog())

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
 
 
# CLASS: dev.ultreon.quantum.crash.CrashCategory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.crash.CrashCategory as _CrashCategory
_CrashCategory = _CrashCategory
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrashCategory():
    """dev.ultreon.quantum.crash.CrashCategory"""
 
    @staticmethod
    def _wrap(java_value: _CrashCategory) -> 'CrashCategory':
        return CrashCategory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CrashCategory):
        """
        Dynamic initializer for CrashCategory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CrashCategory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CrashCategory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashCategory.toString()"""
        return str._wrap(super(CrashCategory, self).toString())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.crash.CrashCategory(java.lang.String)"""
        val = _CrashCategory(arg0)
        self.__wrapper = val

    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.crash.CrashCategory.getThrowable()"""
        return 'Throwable'._wrap(super(CrashCategory, self).getThrowable())

    @overload
    def getDetails(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashCategory.getDetails()"""
        return str._wrap(super(CrashCategory, self).getDetails())

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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.crash.CrashCategory(java.lang.String,java.lang.Throwable)"""
        val = _CrashCategory(arg0, arg1)
        self.__wrapper = val

    @overload
    def add(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.crash.CrashCategory.add(java.lang.String,java.lang.Object)"""
        super(_CrashCategory, self).add(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())