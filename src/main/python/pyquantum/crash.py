from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.util.Result as __Result
__Result = __Result
from builtins import type
import java.io.File as File
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import dev.ultreon.quantum.crash.CrashLog as __CrashLog
__CrashLog = __CrashLog
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.crash.CrashCategory as __CrashCategory
__CrashCategory = __CrashCategory
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.crash.ApplicationCrash as __ApplicationCrash
__ApplicationCrash = __ApplicationCrash
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class CrashLog(__CrashCategory, CrashCategory):
    """dev.ultreon.quantum.crash.CrashLog"""
 
    @staticmethod
    def __wrap(java_value: __CrashLog) -> 'CrashLog':
        return CrashLog(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CrashLog):
        """
        Dynamic initializer for CrashLog.
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
    def getFileName() -> str:
        """public static java.lang.String dev.ultreon.quantum.crash.CrashLog.getFileName()"""
        return str.__wrap(__CrashLog.getFileName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, arg1: 'CrashLog'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,dev.ultreon.quantum.crash.CrashLog)"""
        val = __CrashLog(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addLog(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.crash.CrashLog.addLog(dev.ultreon.quantum.crash.CrashLog)"""
        super(__CrashLog, self).addLog(arg0)

    @overload
    def writeToStream(self, arg0: 'OutputStream'):
        """public void dev.ultreon.quantum.crash.CrashLog.writeToStream(java.io.OutputStream) throws java.io.IOException"""
        super(__CrashLog, self).writeToStream(arg0)

    @override
    @overload
    def add(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.crash.CrashCategory.add(java.lang.String,java.lang.Object)"""
        super(__CrashCategory, self).add(arg0, arg1)

    @override
    @overload
    def getDetails(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashCategory.getDetails()"""
        return str.__wrap(super(CrashCategory, self).getDetails())

    @overload
    def addCategory(self, arg0: 'CrashCategory'):
        """public void dev.ultreon.quantum.crash.CrashLog.addCategory(dev.ultreon.quantum.crash.CrashCategory)"""
        super(__CrashLog, self).addCategory(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.crash.CrashLog.getThrowable()"""
        return 'Throwable'.__wrap(super(CrashLog, self).getThrowable())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashLog.toString()"""
        return str.__wrap(super(CrashLog, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.crash.CrashCategory> dev.ultreon.quantum.crash.CrashLog.getCategories()"""
        return 'List'.__wrap(super(CrashLog, self).getCategories())

    @overload
    def createCrash(self) -> 'ApplicationCrash':
        """public dev.ultreon.quantum.crash.ApplicationCrash dev.ultreon.quantum.crash.CrashLog.createCrash()"""
        return 'ApplicationCrash'.__wrap(super(CrashLog, self).createCrash())

    @overload
    def __init__(self, arg0: str, arg1: 'CrashLog', arg2: 'Throwable'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,dev.ultreon.quantum.crash.CrashLog,java.lang.Throwable)"""
        val = __CrashLog(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getFileNameWithoutExt() -> str:
        """public static java.lang.String dev.ultreon.quantum.crash.CrashLog.getFileNameWithoutExt()"""
        return str.__wrap(__CrashLog.getFileNameWithoutExt())

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
    def writeToLog(self):
        """public void dev.ultreon.quantum.crash.CrashLog.writeToLog()"""
        super(CrashLog, self).writeToLog()

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,java.lang.Throwable)"""
        val = __CrashLog(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def writeToFile(self, arg0: 'File') -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.crash.CrashLog.writeToFile(java.io.File)"""
        return 'util.Result'.__wrap(super(__CrashLog, self).writeToFile(arg0))

    @overload
    def defaultSave(self) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.crash.CrashLog.defaultSave()"""
        return 'util.Result'.__wrap(super(CrashLog, self).defaultSave())

 
 
 
# CLASS: dev.ultreon.quantum.crash.CrashLog
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.util.Result as __Result
__Result = __Result
from builtins import type
import java.io.File as File
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import dev.ultreon.quantum.crash.CrashLog as __CrashLog
__CrashLog = __CrashLog
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.crash.CrashCategory as __CrashCategory
__CrashCategory = __CrashCategory
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.crash.ApplicationCrash as __ApplicationCrash
__ApplicationCrash = __ApplicationCrash
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class CrashLog(__CrashCategory, CrashCategory):
    """dev.ultreon.quantum.crash.CrashLog"""
 
    @staticmethod
    def __wrap(java_value: __CrashLog) -> 'CrashLog':
        return CrashLog(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CrashLog):
        """
        Dynamic initializer for CrashLog.
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
    def getFileName() -> str:
        """public static java.lang.String dev.ultreon.quantum.crash.CrashLog.getFileName()"""
        return str.__wrap(__CrashLog.getFileName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, arg1: 'CrashLog'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,dev.ultreon.quantum.crash.CrashLog)"""
        val = __CrashLog(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addLog(self, arg0: 'CrashLog'):
        """public void dev.ultreon.quantum.crash.CrashLog.addLog(dev.ultreon.quantum.crash.CrashLog)"""
        super(__CrashLog, self).addLog(arg0)

    @overload
    def writeToStream(self, arg0: 'OutputStream'):
        """public void dev.ultreon.quantum.crash.CrashLog.writeToStream(java.io.OutputStream) throws java.io.IOException"""
        super(__CrashLog, self).writeToStream(arg0)

    @override
    @overload
    def add(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.crash.CrashCategory.add(java.lang.String,java.lang.Object)"""
        super(__CrashCategory, self).add(arg0, arg1)

    @override
    @overload
    def getDetails(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashCategory.getDetails()"""
        return str.__wrap(super(CrashCategory, self).getDetails())

    @overload
    def addCategory(self, arg0: 'CrashCategory'):
        """public void dev.ultreon.quantum.crash.CrashLog.addCategory(dev.ultreon.quantum.crash.CrashCategory)"""
        super(__CrashLog, self).addCategory(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.crash.CrashLog.getThrowable()"""
        return 'Throwable'.__wrap(super(CrashLog, self).getThrowable())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashLog.toString()"""
        return str.__wrap(super(CrashLog, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.crash.CrashCategory> dev.ultreon.quantum.crash.CrashLog.getCategories()"""
        return 'List'.__wrap(super(CrashLog, self).getCategories())

    @overload
    def createCrash(self) -> 'ApplicationCrash':
        """public dev.ultreon.quantum.crash.ApplicationCrash dev.ultreon.quantum.crash.CrashLog.createCrash()"""
        return 'ApplicationCrash'.__wrap(super(CrashLog, self).createCrash())

    @overload
    def __init__(self, arg0: str, arg1: 'CrashLog', arg2: 'Throwable'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,dev.ultreon.quantum.crash.CrashLog,java.lang.Throwable)"""
        val = __CrashLog(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getFileNameWithoutExt() -> str:
        """public static java.lang.String dev.ultreon.quantum.crash.CrashLog.getFileNameWithoutExt()"""
        return str.__wrap(__CrashLog.getFileNameWithoutExt())

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
    def writeToLog(self):
        """public void dev.ultreon.quantum.crash.CrashLog.writeToLog()"""
        super(CrashLog, self).writeToLog()

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.crash.CrashLog(java.lang.String,java.lang.Throwable)"""
        val = __CrashLog(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def writeToFile(self, arg0: 'File') -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.crash.CrashLog.writeToFile(java.io.File)"""
        return 'util.Result'.__wrap(super(__CrashLog, self).writeToFile(arg0))

    @overload
    def defaultSave(self) -> 'util.Result':
        """public dev.ultreon.quantum.util.Result<java.lang.Void> dev.ultreon.quantum.crash.CrashLog.defaultSave()"""
        return 'util.Result'.__wrap(super(CrashLog, self).defaultSave())

 
 
 
# CLASS: dev.ultreon.quantum.crash.CrashLog 
 
 
# CLASS: dev.ultreon.quantum.crash.ApplicationCrash
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import dev.ultreon.quantum.crash.CrashLog as __CrashLog
__CrashLog = __CrashLog
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.crash.ApplicationCrash as __ApplicationCrash
__ApplicationCrash = __ApplicationCrash
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ApplicationCrash(__Error, Error):
    """dev.ultreon.quantum.crash.ApplicationCrash"""
 
    @staticmethod
    def __wrap(java_value: __ApplicationCrash) -> 'ApplicationCrash':
        return ApplicationCrash(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ApplicationCrash):
        """
        Dynamic initializer for ApplicationCrash.
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.ApplicationCrash.toString()"""
        return str.__wrap(super(ApplicationCrash, self).toString())

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
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

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
    def getCrashLog(self) -> 'CrashLog':
        """public dev.ultreon.quantum.crash.CrashLog dev.ultreon.quantum.crash.ApplicationCrash.getCrashLog()"""
        return 'CrashLog'.__wrap(super(ApplicationCrash, self).getCrashLog())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def handleCrash(self):
        """public void dev.ultreon.quantum.crash.ApplicationCrash.handleCrash()"""
        super(ApplicationCrash, self).handleCrash()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @overload
    def __init__(self, arg0: 'CrashLog'):
        """public dev.ultreon.quantum.crash.ApplicationCrash(dev.ultreon.quantum.crash.CrashLog)"""
        val = __ApplicationCrash(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def onCrash(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.crash.ApplicationCrash.onCrash(java.lang.Runnable)"""
        __ApplicationCrash.onCrash(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.crash.CrashException
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
import dev.ultreon.quantum.crash.CrashLog as __CrashLog
__CrashLog = __CrashLog
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import dev.ultreon.quantum.crash.CrashException as __CrashException
__CrashException = __CrashException
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CrashException(__RuntimeException, RuntimeException):
    """dev.ultreon.quantum.crash.CrashException"""
 
    @staticmethod
    def __wrap(java_value: __CrashException) -> 'CrashException':
        return CrashException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CrashException):
        """
        Dynamic initializer for CrashException.
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
    def getCrashLog(self) -> 'CrashLog':
        """public dev.ultreon.quantum.crash.CrashLog dev.ultreon.quantum.crash.CrashException.getCrashLog()"""
        return 'CrashLog'.__wrap(super(CrashException, self).getCrashLog())

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

    @overload
    def __init__(self, arg0: 'CrashLog'):
        """public dev.ultreon.quantum.crash.CrashException(dev.ultreon.quantum.crash.CrashLog)"""
        val = __CrashException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'CrashLog', arg1: str):
        """public dev.ultreon.quantum.crash.CrashException(dev.ultreon.quantum.crash.CrashLog,java.lang.String)"""
        val = __CrashException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.crash.CrashCategory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.crash.CrashCategory as __CrashCategory
__CrashCategory = __CrashCategory
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CrashCategory():
    """dev.ultreon.quantum.crash.CrashCategory"""
 
    @staticmethod
    def __wrap(java_value: __CrashCategory) -> 'CrashCategory':
        return CrashCategory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CrashCategory):
        """
        Dynamic initializer for CrashCategory.
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashCategory.toString()"""
        return str.__wrap(super(CrashCategory, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.quantum.crash.CrashCategory.getThrowable()"""
        return 'Throwable'.__wrap(super(CrashCategory, self).getThrowable())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.crash.CrashCategory(java.lang.String,java.lang.Throwable)"""
        val = __CrashCategory(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.crash.CrashCategory(java.lang.String)"""
        val = __CrashCategory(arg0)
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

    @overload
    def add(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.crash.CrashCategory.add(java.lang.String,java.lang.Object)"""
        super(__CrashCategory, self).add(arg0, arg1)

    @overload
    def getDetails(self) -> str:
        """public java.lang.String dev.ultreon.quantum.crash.CrashCategory.getDetails()"""
        return str.__wrap(super(CrashCategory, self).getDetails())

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