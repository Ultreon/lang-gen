from __future__ import annotations
from overload import overload


 
from builtins import str
import dev.ultreon.libs.crash.v0.CrashLog as __CrashLog
__CrashLog = __CrashLog
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
import dev.ultreon.libs.crash.v0.CrashException as __CrashException
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
    """dev.ultreon.libs.crash.v0.CrashException"""
 
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
    def __init__(self, arg0: 'CrashLog', arg1: str):
        """public dev.ultreon.libs.crash.v0.CrashException(dev.ultreon.libs.crash.v0.CrashLog,java.lang.String)"""
        val = __CrashException(arg0, arg1)
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

    @overload
    def getCrashLog(self) -> 'CrashLog':
        """public dev.ultreon.libs.crash.v0.CrashLog dev.ultreon.libs.crash.v0.CrashException.getCrashLog()"""
        return 'CrashLog'.__wrap(super(CrashException, self).getCrashLog())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'CrashLog'):
        """public dev.ultreon.libs.crash.v0.CrashException(dev.ultreon.libs.crash.v0.CrashLog)"""
        val = __CrashException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

 
 
 
# CLASS: dev.ultreon.libs.crash.v0.CrashException
from builtins import str
import dev.ultreon.libs.crash.v0.CrashLog as __CrashLog
__CrashLog = __CrashLog
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
import dev.ultreon.libs.crash.v0.CrashException as __CrashException
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
    """dev.ultreon.libs.crash.v0.CrashException"""
 
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
    def __init__(self, arg0: 'CrashLog', arg1: str):
        """public dev.ultreon.libs.crash.v0.CrashException(dev.ultreon.libs.crash.v0.CrashLog,java.lang.String)"""
        val = __CrashException(arg0, arg1)
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

    @overload
    def getCrashLog(self) -> 'CrashLog':
        """public dev.ultreon.libs.crash.v0.CrashLog dev.ultreon.libs.crash.v0.CrashException.getCrashLog()"""
        return 'CrashLog'.__wrap(super(CrashException, self).getCrashLog())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'CrashLog'):
        """public dev.ultreon.libs.crash.v0.CrashException(dev.ultreon.libs.crash.v0.CrashLog)"""
        val = __CrashException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

 
 
 
# CLASS: dev.ultreon.libs.crash.v0.CrashException 
 
 
# CLASS: dev.ultreon.libs.crash.v0.ApplicationCrash
from builtins import str
import dev.ultreon.libs.crash.v0.CrashLog as __CrashLog
__CrashLog = __CrashLog
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.crash.v0.ApplicationCrash as __ApplicationCrash
__ApplicationCrash = __ApplicationCrash
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ApplicationCrash():
    """dev.ultreon.libs.crash.v0.ApplicationCrash"""
 
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def printCrash(self):
        """public void dev.ultreon.libs.crash.v0.ApplicationCrash.printCrash()"""
        super(ApplicationCrash, self).printCrash()

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
    def getCrashLog(self) -> 'CrashLog':
        """public dev.ultreon.libs.crash.v0.CrashLog dev.ultreon.libs.crash.v0.ApplicationCrash.getCrashLog()"""
        return 'CrashLog'.__wrap(super(ApplicationCrash, self).getCrashLog())

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

    @staticmethod
    @overload
    def onCrash(arg0: 'Runnable'):
        """public static void dev.ultreon.libs.crash.v0.ApplicationCrash.onCrash(java.lang.Runnable)"""
        __ApplicationCrash.onCrash(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.libs.crash.v0.CrashLog
from builtins import str
import dev.ultreon.libs.crash.v0.CrashLog as __CrashLog
__CrashLog = __CrashLog
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import dev.ultreon.libs.crash.v0.CrashCategory as __CrashCategory
__CrashCategory = __CrashCategory
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.crash.v0.ApplicationCrash as __ApplicationCrash
__ApplicationCrash = __ApplicationCrash
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class CrashLog(__CrashCategory, CrashCategory):
    """dev.ultreon.libs.crash.v0.CrashLog"""
 
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.libs.crash.v0.CrashCategory> dev.ultreon.libs.crash.v0.CrashLog.getCategories()"""
        return 'List'.__wrap(super(CrashLog, self).getCategories())

    @override
    @overload
    def getDetails(self) -> str:
        """public java.lang.String dev.ultreon.libs.crash.v0.CrashCategory.getDetails()"""
        return str.__wrap(super(CrashCategory, self).getDetails())

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.libs.crash.v0.CrashLog(java.lang.String,java.lang.Throwable)"""
        val = __CrashLog(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def createCrash(self) -> 'ApplicationCrash':
        """public dev.ultreon.libs.crash.v0.ApplicationCrash dev.ultreon.libs.crash.v0.CrashLog.createCrash()"""
        return 'ApplicationCrash'.__wrap(super(CrashLog, self).createCrash())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.crash.v0.CrashLog.getThrowable()"""
        return 'Throwable'.__wrap(super(CrashLog, self).getThrowable())

    @overload
    def addCategory(self, arg0: 'CrashCategory'):
        """public void dev.ultreon.libs.crash.v0.CrashLog.addCategory(dev.ultreon.libs.crash.v0.CrashCategory)"""
        super(__CrashLog, self).addCategory(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.crash.v0.CrashLog.toString()"""
        return str.__wrap(super(CrashLog, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def writeToFile(self, arg0: 'File'):
        """public void dev.ultreon.libs.crash.v0.CrashLog.writeToFile(java.io.File)"""
        super(__CrashLog, self).writeToFile(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def add(self, arg0: str, arg1: object):
        """public void dev.ultreon.libs.crash.v0.CrashCategory.add(java.lang.String,java.lang.Object)"""
        super(__CrashCategory, self).add(arg0, arg1)

    @overload
    def getDefaultFileName(self) -> str:
        """public java.lang.String dev.ultreon.libs.crash.v0.CrashLog.getDefaultFileName()"""
        return str.__wrap(super(CrashLog, self).getDefaultFileName())

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
    def defaultSave(self):
        """public void dev.ultreon.libs.crash.v0.CrashLog.defaultSave()"""
        super(CrashLog, self).defaultSave()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'CrashLog'):
        """public dev.ultreon.libs.crash.v0.CrashLog(java.lang.String,dev.ultreon.libs.crash.v0.CrashLog)"""
        val = __CrashLog(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'CrashLog', arg2: 'Throwable'):
        """public dev.ultreon.libs.crash.v0.CrashLog(java.lang.String,dev.ultreon.libs.crash.v0.CrashLog,java.lang.Throwable)"""
        val = __CrashLog(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.libs.crash.v0.CrashCategory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.crash.v0.CrashCategory as __CrashCategory
__CrashCategory = __CrashCategory
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
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
 
class CrashCategory():
    """dev.ultreon.libs.crash.v0.CrashCategory"""
 
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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.libs.crash.v0.CrashCategory(java.lang.String,java.lang.Throwable)"""
        val = __CrashCategory(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: str):
        """public dev.ultreon.libs.crash.v0.CrashCategory(java.lang.String)"""
        val = __CrashCategory(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDetails(self) -> str:
        """public java.lang.String dev.ultreon.libs.crash.v0.CrashCategory.getDetails()"""
        return str.__wrap(super(CrashCategory, self).getDetails())

    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.crash.v0.CrashCategory.getThrowable()"""
        return 'Throwable'.__wrap(super(CrashCategory, self).getThrowable())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.crash.v0.CrashCategory.toString()"""
        return str.__wrap(super(CrashCategory, self).toString())

    @overload
    def add(self, arg0: str, arg1: object):
        """public void dev.ultreon.libs.crash.v0.CrashCategory.add(java.lang.String,java.lang.Object)"""
        super(__CrashCategory, self).add(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))