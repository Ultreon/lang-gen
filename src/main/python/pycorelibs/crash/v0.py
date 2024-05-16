from __future__ import annotations
from overload import overload


 
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
import dev.ultreon.libs.crash.v0.CrashException as _CrashException
_CrashException = _CrashException
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import dev.ultreon.libs.crash.v0.CrashLog as _CrashLog
_CrashLog = _CrashLog
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrashException():
    """dev.ultreon.libs.crash.v0.CrashException"""
 
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

    @overload
    def __init__(self, arg0: 'CrashLog'):
        """public dev.ultreon.libs.crash.v0.CrashException(dev.ultreon.libs.crash.v0.CrashLog)"""
        val = _CrashException(arg0)
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

    @overload
    def getCrashLog(self) -> 'CrashLog':
        """public dev.ultreon.libs.crash.v0.CrashLog dev.ultreon.libs.crash.v0.CrashException.getCrashLog()"""
        return 'CrashLog'._wrap(super(CrashException, self).getCrashLog())

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
        """public dev.ultreon.libs.crash.v0.CrashException(dev.ultreon.libs.crash.v0.CrashLog,java.lang.String)"""
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

 
 
 
# CLASS: dev.ultreon.libs.crash.v0.CrashException
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
import dev.ultreon.libs.crash.v0.CrashException as _CrashException
_CrashException = _CrashException
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import dev.ultreon.libs.crash.v0.CrashLog as _CrashLog
_CrashLog = _CrashLog
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrashException():
    """dev.ultreon.libs.crash.v0.CrashException"""
 
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

    @overload
    def __init__(self, arg0: 'CrashLog'):
        """public dev.ultreon.libs.crash.v0.CrashException(dev.ultreon.libs.crash.v0.CrashLog)"""
        val = _CrashException(arg0)
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

    @overload
    def getCrashLog(self) -> 'CrashLog':
        """public dev.ultreon.libs.crash.v0.CrashLog dev.ultreon.libs.crash.v0.CrashException.getCrashLog()"""
        return 'CrashLog'._wrap(super(CrashException, self).getCrashLog())

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
        """public dev.ultreon.libs.crash.v0.CrashException(dev.ultreon.libs.crash.v0.CrashLog,java.lang.String)"""
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

 
 
 
# CLASS: dev.ultreon.libs.crash.v0.CrashException 
 
 
# CLASS: dev.ultreon.libs.crash.v0.CrashCategory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.crash.v0.CrashCategory as _CrashCategory
_CrashCategory = _CrashCategory
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CrashCategory():
    """dev.ultreon.libs.crash.v0.CrashCategory"""
 
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
        """public java.lang.String dev.ultreon.libs.crash.v0.CrashCategory.toString()"""
        return str._wrap(super(CrashCategory, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.crash.v0.CrashCategory.getThrowable()"""
        return 'Throwable'._wrap(super(CrashCategory, self).getThrowable())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: str, arg1: object):
        """public void dev.ultreon.libs.crash.v0.CrashCategory.add(java.lang.String,java.lang.Object)"""
        super(_CrashCategory, self).add(arg0, arg1)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.libs.crash.v0.CrashCategory(java.lang.String)"""
        val = _CrashCategory(arg0)
        self.__wrapper = val

    @overload
    def getDetails(self) -> str:
        """public java.lang.String dev.ultreon.libs.crash.v0.CrashCategory.getDetails()"""
        return str._wrap(super(CrashCategory, self).getDetails())

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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.libs.crash.v0.CrashCategory(java.lang.String,java.lang.Throwable)"""
        val = _CrashCategory(arg0, arg1)
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
 
 
# CLASS: dev.ultreon.libs.crash.v0.ApplicationCrash
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.libs.crash.v0.ApplicationCrash as _ApplicationCrash
_ApplicationCrash = _ApplicationCrash
import dev.ultreon.libs.crash.v0.CrashLog as _CrashLog
_CrashLog = _CrashLog
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ApplicationCrash():
    """dev.ultreon.libs.crash.v0.ApplicationCrash"""
 
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
 
    @overload
    def printCrash(self):
        """public void dev.ultreon.libs.crash.v0.ApplicationCrash.printCrash()"""
        super(ApplicationCrash, self).printCrash()

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

    @staticmethod
    @overload
    def onCrash(arg0: 'Runnable'):
        """public static void dev.ultreon.libs.crash.v0.ApplicationCrash.onCrash(java.lang.Runnable)"""
        _ApplicationCrash.onCrash(arg0)

    @overload
    def getCrashLog(self) -> 'CrashLog':
        """public dev.ultreon.libs.crash.v0.CrashLog dev.ultreon.libs.crash.v0.ApplicationCrash.getCrashLog()"""
        return 'CrashLog'._wrap(super(ApplicationCrash, self).getCrashLog())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.crash.v0.CrashLog
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import dev.ultreon.libs.crash.v0.CrashCategory as _CrashCategory
_CrashCategory = _CrashCategory
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.libs.crash.v0.CrashLog as _CrashLog
_CrashLog = _CrashLog
import dev.ultreon.libs.crash.v0.ApplicationCrash as _ApplicationCrash
_ApplicationCrash = _ApplicationCrash
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
    """dev.ultreon.libs.crash.v0.CrashLog"""
 
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
 
    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.libs.crash.v0.CrashLog(java.lang.String,java.lang.Throwable)"""
        val = _CrashLog(arg0, arg1)
        self.__wrapper = val

    @overload
    def addCategory(self, arg0: 'CrashCategory'):
        """public void dev.ultreon.libs.crash.v0.CrashLog.addCategory(dev.ultreon.libs.crash.v0.CrashCategory)"""
        super(_CrashLog, self).addCategory(arg0)

    @overload
    def getDefaultFileName(self) -> str:
        """public java.lang.String dev.ultreon.libs.crash.v0.CrashLog.getDefaultFileName()"""
        return str._wrap(super(CrashLog, self).getDefaultFileName())

    @override
    @overload
    def add(self, arg0: str, arg1: object):
        """public void dev.ultreon.libs.crash.v0.CrashCategory.add(java.lang.String,java.lang.Object)"""
        super(_CrashCategory, self).add(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getDetails(self) -> str:
        """public java.lang.String dev.ultreon.libs.crash.v0.CrashCategory.getDetails()"""
        return str._wrap(super(CrashCategory, self).getDetails())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def createCrash(self) -> 'ApplicationCrash':
        """public dev.ultreon.libs.crash.v0.ApplicationCrash dev.ultreon.libs.crash.v0.CrashLog.createCrash()"""
        return 'ApplicationCrash'._wrap(super(CrashLog, self).createCrash())

    @overload
    def __init__(self, arg0: str, arg1: 'CrashLog', arg2: 'Throwable'):
        """public dev.ultreon.libs.crash.v0.CrashLog(java.lang.String,dev.ultreon.libs.crash.v0.CrashLog,java.lang.Throwable)"""
        val = _CrashLog(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'CrashLog'):
        """public dev.ultreon.libs.crash.v0.CrashLog(java.lang.String,dev.ultreon.libs.crash.v0.CrashLog)"""
        val = _CrashLog(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.crash.v0.CrashLog.getThrowable()"""
        return 'Throwable'._wrap(super(CrashLog, self).getThrowable())

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
    def getCategories(self) -> 'List':
        """public java.util.List<dev.ultreon.libs.crash.v0.CrashCategory> dev.ultreon.libs.crash.v0.CrashLog.getCategories()"""
        return 'List'._wrap(super(CrashLog, self).getCategories())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def writeToFile(self, arg0: 'File'):
        """public void dev.ultreon.libs.crash.v0.CrashLog.writeToFile(java.io.File)"""
        super(_CrashLog, self).writeToFile(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.crash.v0.CrashLog.toString()"""
        return str._wrap(super(CrashLog, self).toString())

    @overload
    def defaultSave(self):
        """public void dev.ultreon.libs.crash.v0.CrashLog.defaultSave()"""
        super(CrashLog, self).defaultSave()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())