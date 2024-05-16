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
import org.apache.commons.lang3.concurrent.ConcurrentException as _ConcurrentException
_ConcurrentException = _ConcurrentException
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
 
class ConcurrentException():
    """org.apache.commons.lang3.concurrent.ConcurrentException"""
 
    @staticmethod
    def _wrap(java_value: _ConcurrentException) -> 'ConcurrentException':
        return ConcurrentException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConcurrentException):
        """
        Dynamic initializer for ConcurrentException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConcurrentException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConcurrentException__wrapper":
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

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.ConcurrentException(java.lang.Throwable)"""
        val = _ConcurrentException(arg0)
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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.ConcurrentException(java.lang.String,java.lang.Throwable)"""
        val = _ConcurrentException(arg0, arg1)
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

 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConcurrentException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import org.apache.commons.lang3.concurrent.ConcurrentException as _ConcurrentException
_ConcurrentException = _ConcurrentException
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
 
class ConcurrentException():
    """org.apache.commons.lang3.concurrent.ConcurrentException"""
 
    @staticmethod
    def _wrap(java_value: _ConcurrentException) -> 'ConcurrentException':
        return ConcurrentException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConcurrentException):
        """
        Dynamic initializer for ConcurrentException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConcurrentException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConcurrentException__wrapper":
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

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.ConcurrentException(java.lang.Throwable)"""
        val = _ConcurrentException(arg0)
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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.ConcurrentException(java.lang.String,java.lang.Throwable)"""
        val = _ConcurrentException(arg0, arg1)
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

 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConcurrentException 
 
 
# CLASS: org.apache.commons.lang3.concurrent.CallableBackgroundInitializer
from builtins import str
import org.apache.commons.lang3.concurrent.BackgroundInitializer as _BackgroundInitializer
_BackgroundInitializer = _BackgroundInitializer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.ExecutorService as ExecutorService
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.concurrent.CallableBackgroundInitializer as _CallableBackgroundInitializer
_CallableBackgroundInitializer = _CallableBackgroundInitializer
import java.lang.Integer as _int
import java.util.concurrent.ExecutorService as _ExecutorService
_ExecutorService = _ExecutorService
import java.util.concurrent.Future as Future
import java.util.concurrent.Callable as Callable
from builtins import bool
import java.lang.Long as _long
import java.util.concurrent.Future as _Future
_Future = _Future
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CallableBackgroundInitializer():
    """org.apache.commons.lang3.concurrent.CallableBackgroundInitializer"""
 
    @staticmethod
    def _wrap(java_value: _CallableBackgroundInitializer) -> 'CallableBackgroundInitializer':
        return CallableBackgroundInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CallableBackgroundInitializer):
        """
        Dynamic initializer for CallableBackgroundInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CallableBackgroundInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CallableBackgroundInitializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getExternalExecutor(self) -> 'ExecutorService':
        """public final synchronized java.util.concurrent.ExecutorService org.apache.commons.lang3.concurrent.BackgroundInitializer.getExternalExecutor()"""
        return 'ExecutorService'._wrap(super(BackgroundInitializer, self).getExternalExecutor())

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

    @override
    @overload
    def getFuture(self) -> 'Future':
        """public synchronized java.util.concurrent.Future<T> org.apache.commons.lang3.concurrent.BackgroundInitializer.getFuture()"""
        return 'Future'._wrap(super(BackgroundInitializer, self).getFuture())

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
    def setExternalExecutor(self, arg0: 'ExecutorService'):
        """public final synchronized void org.apache.commons.lang3.concurrent.BackgroundInitializer.setExternalExecutor(java.util.concurrent.ExecutorService)"""
        super(_BackgroundInitializer, self).setExternalExecutor(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Callable', arg1: 'ExecutorService'):
        """public org.apache.commons.lang3.concurrent.CallableBackgroundInitializer(java.util.concurrent.Callable<T>,java.util.concurrent.ExecutorService)"""
        val = _CallableBackgroundInitializer(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.BackgroundInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object._wrap(super(BackgroundInitializer, self).get())

    @override
    @overload
    def start(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.start()"""
        return bool._wrap(super(BackgroundInitializer, self).start())

    @overload
    def __init__(self, arg0: 'Callable'):
        """public org.apache.commons.lang3.concurrent.CallableBackgroundInitializer(java.util.concurrent.Callable<T>)"""
        val = _CallableBackgroundInitializer(arg0)
        self.__wrapper = val

    @override
    @overload
    def isStarted(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.isStarted()"""
        return bool._wrap(super(BackgroundInitializer, self).isStarted())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.MultiBackgroundInitializer
from builtins import str
import org.apache.commons.lang3.concurrent.BackgroundInitializer as _BackgroundInitializer
_BackgroundInitializer = _BackgroundInitializer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.ExecutorService as ExecutorService
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.concurrent.MultiBackgroundInitializer as _MultiBackgroundInitializer
_MultiBackgroundInitializer = _MultiBackgroundInitializer
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.concurrent.ExecutorService as _ExecutorService
_ExecutorService = _ExecutorService
import java.util.concurrent.Future as Future
from builtins import bool
import java.lang.Long as _long
import java.util.concurrent.Future as _Future
_Future = _Future
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultiBackgroundInitializer():
    """org.apache.commons.lang3.concurrent.MultiBackgroundInitializer"""
 
    @staticmethod
    def _wrap(java_value: _MultiBackgroundInitializer) -> 'MultiBackgroundInitializer':
        return MultiBackgroundInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiBackgroundInitializer):
        """
        Dynamic initializer for MultiBackgroundInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiBackgroundInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiBackgroundInitializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getExternalExecutor(self) -> 'ExecutorService':
        """public final synchronized java.util.concurrent.ExecutorService org.apache.commons.lang3.concurrent.BackgroundInitializer.getExternalExecutor()"""
        return 'ExecutorService'._wrap(super(BackgroundInitializer, self).getExternalExecutor())

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
    def __init__(self, arg0: 'ExecutorService'):
        """public org.apache.commons.lang3.concurrent.MultiBackgroundInitializer(java.util.concurrent.ExecutorService)"""
        val = _MultiBackgroundInitializer(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def addInitializer(self, arg0: str, arg1: 'BackgroundInitializer'):
        """public void org.apache.commons.lang3.concurrent.MultiBackgroundInitializer.addInitializer(java.lang.String,org.apache.commons.lang3.concurrent.BackgroundInitializer<?>)"""
        super(_MultiBackgroundInitializer, self).addInitializer(arg0, arg1)

    @override
    @overload
    def getFuture(self) -> 'Future':
        """public synchronized java.util.concurrent.Future<T> org.apache.commons.lang3.concurrent.BackgroundInitializer.getFuture()"""
        return 'Future'._wrap(super(BackgroundInitializer, self).getFuture())

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
    def setExternalExecutor(self, arg0: 'ExecutorService'):
        """public final synchronized void org.apache.commons.lang3.concurrent.BackgroundInitializer.setExternalExecutor(java.util.concurrent.ExecutorService)"""
        super(_BackgroundInitializer, self).setExternalExecutor(arg0)

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
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.BackgroundInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object._wrap(super(BackgroundInitializer, self).get())

    @override
    @overload
    def start(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.start()"""
        return bool._wrap(super(BackgroundInitializer, self).start())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.MultiBackgroundInitializer()"""
        val = _MultiBackgroundInitializer()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.MultiBackgroundInitializer()"""
        val = _MultiBackgroundInitializer()
        self.__wrapper = val

    @override
    @overload
    def isStarted(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.isStarted()"""
        return bool._wrap(super(BackgroundInitializer, self).isStarted())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker
from builtins import str
from pyquantum_helper import override
import java.lang.Long as Long
import java.beans.PropertyChangeListener as PropertyChangeListener
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.concurrent.AbstractCircuitBreaker as _AbstractCircuitBreaker
_AbstractCircuitBreaker = _AbstractCircuitBreaker
import org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker as _ThresholdCircuitBreaker
_ThresholdCircuitBreaker = _ThresholdCircuitBreaker
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ThresholdCircuitBreaker():
    """org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker"""
 
    @staticmethod
    def _wrap(java_value: _ThresholdCircuitBreaker) -> 'ThresholdCircuitBreaker':
        return ThresholdCircuitBreaker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThresholdCircuitBreaker):
        """
        Dynamic initializer for ThresholdCircuitBreaker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThresholdCircuitBreaker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThresholdCircuitBreaker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def checkState(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker.checkState()"""
        return bool._wrap(super(ThresholdCircuitBreaker, self).checkState())

    @override
    @overload
    def close(self):
        """public void org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker.close()"""
        super(ThresholdCircuitBreaker, self).close()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def incrementAndCheckState(self, arg0: 'Long') -> bool:
        """public boolean org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker.incrementAndCheckState(java.lang.Long)"""
        return bool._wrap(super(_ThresholdCircuitBreaker, self).incrementAndCheckState(arg0))

    @override
    @overload
    def addChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.addChangeListener(java.beans.PropertyChangeListener)"""
        super(_AbstractCircuitBreaker, self).addChangeListener(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getThreshold(self) -> int:
        """public long org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker.getThreshold()"""
        return int._wrap(super(ThresholdCircuitBreaker, self).getThreshold())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isOpen(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isOpen()"""
        return bool._wrap(super(AbstractCircuitBreaker, self).isOpen())

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
    def __init__(self, arg0: int):
        """public org.apache.commons.lang3.concurrent.ThresholdCircuitBreaker(long)"""
        val = _ThresholdCircuitBreaker(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def isClosed(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isClosed()"""
        return bool._wrap(super(AbstractCircuitBreaker, self).isClosed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def open(self):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.open()"""
        super(AbstractCircuitBreaker, self).open()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def removeChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.removeChangeListener(java.beans.PropertyChangeListener)"""
        super(_AbstractCircuitBreaker, self).removeChangeListener(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults
from builtins import str
import org.apache.commons.lang3.concurrent.BackgroundInitializer as _BackgroundInitializer
_BackgroundInitializer = _BackgroundInitializer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.concurrent.ConcurrentException as _ConcurrentException
_ConcurrentException = _ConcurrentException
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.util.Set as Set
import java.lang.Integer as _int
import org.apache.commons.lang3.concurrent.MultiBackgroundInitializer as _MultiBackgroundInitializer_MultiBackgroundInitializerResults
_MultiBackgroundInitializerResults = _MultiBackgroundInitializer_MultiBackgroundInitializerResults.MultiBackgroundInitializerResults
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultiBackgroundInitializerResults():
    """org.apache.commons.lang3.concurrent.MultiBackgroundInitializer.MultiBackgroundInitializerResults"""
 
    @staticmethod
    def _wrap(java_value: _MultiBackgroundInitializerResults) -> 'MultiBackgroundInitializerResults':
        return MultiBackgroundInitializerResults(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiBackgroundInitializerResults):
        """
        Dynamic initializer for MultiBackgroundInitializerResults.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiBackgroundInitializerResults__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiBackgroundInitializerResults__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getException(self, arg0: str) -> 'ConcurrentException':
        """public org.apache.commons.lang3.concurrent.ConcurrentException org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.getException(java.lang.String)"""
        return 'ConcurrentException'._wrap(super(_MultiBackgroundInitializerResults, self).getException(arg0))

    @overload
    def isSuccessful(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.isSuccessful()"""
        return bool._wrap(super(MultiBackgroundInitializerResults, self).isSuccessful())

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
    def initializerNames(self) -> 'Set':
        """public java.util.Set<java.lang.String> org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.initializerNames()"""
        return 'Set'._wrap(super(MultiBackgroundInitializerResults, self).initializerNames())

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

    @overload
    def getInitializer(self, arg0: str) -> 'BackgroundInitializer':
        """public org.apache.commons.lang3.concurrent.BackgroundInitializer<?> org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.getInitializer(java.lang.String)"""
        return 'BackgroundInitializer'._wrap(super(_MultiBackgroundInitializerResults, self).getInitializer(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getResultObject(self, arg0: str) -> object:
        """public java.lang.Object org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.getResultObject(java.lang.String)"""
        return object._wrap(super(_MultiBackgroundInitializerResults, self).getResultObject(arg0))

    @overload
    def isException(self, arg0: str) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.MultiBackgroundInitializer$MultiBackgroundInitializerResults.isException(java.lang.String)"""
        return bool._wrap(super(_MultiBackgroundInitializerResults, self).isException(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.Memoizer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.function.Function as Function
import org.apache.commons.lang3.concurrent.Memoizer as _Memoizer
_Memoizer = _Memoizer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Memoizer():
    """org.apache.commons.lang3.concurrent.Memoizer"""
 
    @staticmethod
    def _wrap(java_value: _Memoizer) -> 'Memoizer':
        return Memoizer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Memoizer):
        """
        Dynamic initializer for Memoizer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Memoizer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Memoizer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'Function', arg1: bool):
        """public org.apache.commons.lang3.concurrent.Memoizer(java.util.function.Function<I, O>,boolean)"""
        val = _Memoizer(arg0, _boolean.valueOf(arg1))
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
    def __init__(self, arg0: 'Computable', arg1: bool):
        """public org.apache.commons.lang3.concurrent.Memoizer(org.apache.commons.lang3.concurrent.Computable<I, O>,boolean)"""
        val = _Memoizer(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Computable'):
        """public org.apache.commons.lang3.concurrent.Memoizer(org.apache.commons.lang3.concurrent.Computable<I, O>)"""
        val = _Memoizer(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Function'):
        """public org.apache.commons.lang3.concurrent.Memoizer(java.util.function.Function<I, O>)"""
        val = _Memoizer(arg0)
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
    def compute(self, arg0: object) -> object:
        """public O org.apache.commons.lang3.concurrent.Memoizer.compute(I) throws java.lang.InterruptedException"""
        return object._wrap(super(_Memoizer, self).compute(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.concurrent.BasicThreadFactory as _BasicThreadFactory_Builder
_Builder = _BasicThreadFactory_Builder.Builder
import java.lang.Thread.UncaughtExceptionHandler as UncaughtExceptionHandler
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.apache.commons.lang3.concurrent.BasicThreadFactory as _BasicThreadFactory
_BasicThreadFactory = _BasicThreadFactory
from builtins import bool
import java.util.concurrent.ThreadFactory as ThreadFactory
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """org.apache.commons.lang3.concurrent.BasicThreadFactory.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def reset(self):
        """public void org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.reset()"""
        super(Builder, self).reset()

    @overload
    def daemon(self, arg0: bool) -> 'Builder':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.daemon(boolean)"""
        return 'Builder'._wrap(super(_Builder, self).daemon(_boolean.valueOf(arg0)))

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
    def wrappedFactory(self, arg0: 'ThreadFactory') -> 'Builder':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.wrappedFactory(java.util.concurrent.ThreadFactory)"""
        return 'Builder'._wrap(super(_Builder, self).wrappedFactory(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def namingPattern(self, arg0: str) -> 'Builder':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.namingPattern(java.lang.String)"""
        return 'Builder'._wrap(super(_Builder, self).namingPattern(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder()"""
        val = _Builder()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder()"""
        val = _Builder()
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
    def build(self) -> 'BasicThreadFactory':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.build()"""
        return 'BasicThreadFactory'._wrap(super(Builder, self).build())

    @overload
    def priority(self, arg0: int) -> 'Builder':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.priority(int)"""
        return 'Builder'._wrap(super(_Builder, self).priority(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def uncaughtExceptionHandler(self, arg0: 'UncaughtExceptionHandler') -> 'Builder':
        """public org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder org.apache.commons.lang3.concurrent.BasicThreadFactory$Builder.uncaughtExceptionHandler(java.lang.Thread$UncaughtExceptionHandler)"""
        return 'Builder'._wrap(super(_Builder, self).uncaughtExceptionHandler(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConcurrentInitializer
import org.apache.commons.lang3.concurrent.ConcurrentInitializer as _ConcurrentInitializer
_ConcurrentInitializer = _ConcurrentInitializer
from abc import abstractmethod, ABC
 
class ConcurrentInitializer():
    """org.apache.commons.lang3.concurrent.ConcurrentInitializer"""
 
    @staticmethod
    def _wrap(java_value: _ConcurrentInitializer) -> 'ConcurrentInitializer':
        return ConcurrentInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConcurrentInitializer):
        """
        Dynamic initializer for ConcurrentInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConcurrentInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConcurrentInitializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, ):
        """public abstract T org.apache.commons.lang3.concurrent.ConcurrentInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConstantInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.apache.commons.lang3.concurrent.ConstantInitializer as _ConstantInitializer
_ConstantInitializer = _ConstantInitializer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConstantInitializer():
    """org.apache.commons.lang3.concurrent.ConstantInitializer"""
 
    @staticmethod
    def _wrap(java_value: _ConstantInitializer) -> 'ConstantInitializer':
        return ConstantInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstantInitializer):
        """
        Dynamic initializer for ConstantInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstantInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstantInitializer__wrapper":
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
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.ConstantInitializer.equals(java.lang.Object)"""
        return bool._wrap(super(_ConstantInitializer, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.lang3.concurrent.ConstantInitializer(T)"""
        val = _ConstantInitializer(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.concurrent.ConstantInitializer.toString()"""
        return str._wrap(super(ConstantInitializer, self).toString())

    @override
    @overload
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.ConstantInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object._wrap(super(ConstantInitializer, self).get())

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
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.concurrent.ConstantInitializer.hashCode()"""
        return int._wrap(super(ConstantInitializer, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getObject(self) -> object:
        """public final T org.apache.commons.lang3.concurrent.ConstantInitializer.getObject()"""
        return object._wrap(super(ConstantInitializer, self).getObject()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.LazyInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.apache.commons.lang3.concurrent.LazyInitializer as _LazyInitializer
_LazyInitializer = _LazyInitializer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LazyInitializer():
    """org.apache.commons.lang3.concurrent.LazyInitializer"""
 
    @staticmethod
    def _wrap(java_value: _LazyInitializer) -> 'LazyInitializer':
        return LazyInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LazyInitializer):
        """
        Dynamic initializer for LazyInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LazyInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LazyInitializer__wrapper":
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
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.LazyInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object._wrap(super(LazyInitializer, self).get())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.LazyInitializer()"""
        val = _LazyInitializer()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.LazyInitializer()"""
        val = _LazyInitializer()
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
 
 
# CLASS: org.apache.commons.lang3.concurrent.TimedSemaphore
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import org.apache.commons.lang3.concurrent.TimedSemaphore as _TimedSemaphore
_TimedSemaphore = _TimedSemaphore
import java.util.concurrent.TimeUnit as _TimeUnit
_TimeUnit = _TimeUnit
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.ScheduledExecutorService as ScheduledExecutorService
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TimedSemaphore():
    """org.apache.commons.lang3.concurrent.TimedSemaphore"""
 
    @staticmethod
    def _wrap(java_value: _TimedSemaphore) -> 'TimedSemaphore':
        return TimedSemaphore(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TimedSemaphore):
        """
        Dynamic initializer for TimedSemaphore.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TimedSemaphore__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TimedSemaphore__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def acquire(self):
        """public synchronized void org.apache.commons.lang3.concurrent.TimedSemaphore.acquire() throws java.lang.InterruptedException"""
        super(TimedSemaphore, self).acquire()

    @overload
    def tryAcquire(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.TimedSemaphore.tryAcquire()"""
        return bool._wrap(super(TimedSemaphore, self).tryAcquire())

    @overload
    def setLimit(self, arg0: int):
        """public final synchronized void org.apache.commons.lang3.concurrent.TimedSemaphore.setLimit(int)"""
        super(_TimedSemaphore, self).setLimit(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ScheduledExecutorService', arg1: int, arg2: 'TimeUnit', arg3: int):
        """public org.apache.commons.lang3.concurrent.TimedSemaphore(java.util.concurrent.ScheduledExecutorService,long,java.util.concurrent.TimeUnit,int)"""
        val = _TimedSemaphore(arg0, _long.valueOf(arg1), arg2, _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getUnit(self) -> 'TimeUnit':
        """public java.util.concurrent.TimeUnit org.apache.commons.lang3.concurrent.TimedSemaphore.getUnit()"""
        return 'TimeUnit'._wrap(super(TimedSemaphore, self).getUnit())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAverageCallsPerPeriod(self) -> float:
        """public synchronized double org.apache.commons.lang3.concurrent.TimedSemaphore.getAverageCallsPerPeriod()"""
        return float._wrap(super(TimedSemaphore, self).getAverageCallsPerPeriod())

    @overload
    def __init__(self, arg0: int, arg1: 'TimeUnit', arg2: int):
        """public org.apache.commons.lang3.concurrent.TimedSemaphore(long,java.util.concurrent.TimeUnit,int)"""
        val = _TimedSemaphore(_long.valueOf(arg0), arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isShutdown(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.TimedSemaphore.isShutdown()"""
        return bool._wrap(super(TimedSemaphore, self).isShutdown())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getLastAcquiresPerPeriod(self) -> int:
        """public synchronized int org.apache.commons.lang3.concurrent.TimedSemaphore.getLastAcquiresPerPeriod()"""
        return int._wrap(super(TimedSemaphore, self).getLastAcquiresPerPeriod())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getAcquireCount(self) -> int:
        """public synchronized int org.apache.commons.lang3.concurrent.TimedSemaphore.getAcquireCount()"""
        return int._wrap(super(TimedSemaphore, self).getAcquireCount())

    @overload
    def getAvailablePermits(self) -> int:
        """public synchronized int org.apache.commons.lang3.concurrent.TimedSemaphore.getAvailablePermits()"""
        return int._wrap(super(TimedSemaphore, self).getAvailablePermits())

    @overload
    def getPeriod(self) -> int:
        """public long org.apache.commons.lang3.concurrent.TimedSemaphore.getPeriod()"""
        return int._wrap(super(TimedSemaphore, self).getPeriod())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getLimit(self) -> int:
        """public final synchronized int org.apache.commons.lang3.concurrent.TimedSemaphore.getLimit()"""
        return int._wrap(super(TimedSemaphore, self).getLimit())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def shutdown(self):
        """public synchronized void org.apache.commons.lang3.concurrent.TimedSemaphore.shutdown()"""
        super(TimedSemaphore, self).shutdown()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.AtomicSafeInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.concurrent.AtomicSafeInitializer as _AtomicSafeInitializer
_AtomicSafeInitializer = _AtomicSafeInitializer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AtomicSafeInitializer():
    """org.apache.commons.lang3.concurrent.AtomicSafeInitializer"""
 
    @staticmethod
    def _wrap(java_value: _AtomicSafeInitializer) -> 'AtomicSafeInitializer':
        return AtomicSafeInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AtomicSafeInitializer):
        """
        Dynamic initializer for AtomicSafeInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AtomicSafeInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AtomicSafeInitializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.AtomicSafeInitializer()"""
        val = _AtomicSafeInitializer()
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
    def get(self) -> object:
        """public final T org.apache.commons.lang3.concurrent.AtomicSafeInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object._wrap(super(AtomicSafeInitializer, self).get())

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
        """public org.apache.commons.lang3.concurrent.AtomicSafeInitializer()"""
        val = _AtomicSafeInitializer()
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
 
 
# CLASS: org.apache.commons.lang3.concurrent.CircuitBreakingException
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
import org.apache.commons.lang3.concurrent.CircuitBreakingException as _CircuitBreakingException
_CircuitBreakingException = _CircuitBreakingException
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CircuitBreakingException():
    """org.apache.commons.lang3.concurrent.CircuitBreakingException"""
 
    @staticmethod
    def _wrap(java_value: _CircuitBreakingException) -> 'CircuitBreakingException':
        return CircuitBreakingException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CircuitBreakingException):
        """
        Dynamic initializer for CircuitBreakingException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CircuitBreakingException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CircuitBreakingException__wrapper":
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
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.CircuitBreakingException()"""
        val = _CircuitBreakingException()
        self.__wrapper = val

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str):
        """public org.apache.commons.lang3.concurrent.CircuitBreakingException(java.lang.String)"""
        val = _CircuitBreakingException(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.CircuitBreakingException()"""
        val = _CircuitBreakingException()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.CircuitBreakingException(java.lang.String,java.lang.Throwable)"""
        val = _CircuitBreakingException(arg0, arg1)
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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.CircuitBreakingException(java.lang.Throwable)"""
        val = _CircuitBreakingException(arg0)
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
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConcurrentUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.ConcurrentMap as ConcurrentMap
import org.apache.commons.lang3.concurrent.ConcurrentException as _ConcurrentException
_ConcurrentException = _ConcurrentException
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.ExecutionException as ExecutionException
import java.util.concurrent.Future as Future
import org.apache.commons.lang3.concurrent.ConcurrentUtils as _ConcurrentUtils
_ConcurrentUtils = _ConcurrentUtils
import org.apache.commons.lang3.concurrent.ConcurrentRuntimeException as _ConcurrentRuntimeException
_ConcurrentRuntimeException = _ConcurrentRuntimeException
from builtins import bool
import java.lang.Long as _long
import java.util.concurrent.Future as _Future
_Future = _Future
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConcurrentUtils():
    """org.apache.commons.lang3.concurrent.ConcurrentUtils"""
 
    @staticmethod
    def _wrap(java_value: _ConcurrentUtils) -> 'ConcurrentUtils':
        return ConcurrentUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConcurrentUtils):
        """
        Dynamic initializer for ConcurrentUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConcurrentUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConcurrentUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def handleCause(arg0: 'ExecutionException'):
        """public static void org.apache.commons.lang3.concurrent.ConcurrentUtils.handleCause(java.util.concurrent.ExecutionException) throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        _ConcurrentUtils.handleCause(arg0)

    @staticmethod
    @overload
    def createIfAbsentUnchecked(arg0: 'ConcurrentMap', arg1: object, arg2: 'ConcurrentInitializer') -> object:
        """public static <K,V> V org.apache.commons.lang3.concurrent.ConcurrentUtils.createIfAbsentUnchecked(java.util.concurrent.ConcurrentMap<K, V>,K,org.apache.commons.lang3.concurrent.ConcurrentInitializer<V>)"""
        return object._wrap(_ConcurrentUtils.createIfAbsentUnchecked(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def putIfAbsent(arg0: 'ConcurrentMap', arg1: object, arg2: object) -> object:
        """public static <K,V> V org.apache.commons.lang3.concurrent.ConcurrentUtils.putIfAbsent(java.util.concurrent.ConcurrentMap<K, V>,K,V)"""
        return object._wrap(_ConcurrentUtils.putIfAbsent(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def initializeUnchecked(arg0: 'ConcurrentInitializer') -> object:
        """public static <T> T org.apache.commons.lang3.concurrent.ConcurrentUtils.initializeUnchecked(org.apache.commons.lang3.concurrent.ConcurrentInitializer<T>)"""
        return object._wrap(_ConcurrentUtils.initializeUnchecked(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def initialize(arg0: 'ConcurrentInitializer') -> object:
        """public static <T> T org.apache.commons.lang3.concurrent.ConcurrentUtils.initialize(org.apache.commons.lang3.concurrent.ConcurrentInitializer<T>) throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object._wrap(_ConcurrentUtils.initialize(arg0))

    @staticmethod
    @overload
    def extractCause(arg0: 'ExecutionException') -> 'ConcurrentException':
        """public static org.apache.commons.lang3.concurrent.ConcurrentException org.apache.commons.lang3.concurrent.ConcurrentUtils.extractCause(java.util.concurrent.ExecutionException)"""
        return ConcurrentException._wrap(_ConcurrentUtils.extractCause(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def handleCauseUnchecked(arg0: 'ExecutionException'):
        """public static void org.apache.commons.lang3.concurrent.ConcurrentUtils.handleCauseUnchecked(java.util.concurrent.ExecutionException)"""
        _ConcurrentUtils.handleCauseUnchecked(arg0)

    @staticmethod
    @overload
    def extractCauseUnchecked(arg0: 'ExecutionException') -> 'ConcurrentRuntimeException':
        """public static org.apache.commons.lang3.concurrent.ConcurrentRuntimeException org.apache.commons.lang3.concurrent.ConcurrentUtils.extractCauseUnchecked(java.util.concurrent.ExecutionException)"""
        return ConcurrentRuntimeException._wrap(_ConcurrentUtils.extractCauseUnchecked(arg0))

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

    @staticmethod
    @overload
    def constantFuture(arg0: object) -> 'Future':
        """public static <T> java.util.concurrent.Future<T> org.apache.commons.lang3.concurrent.ConcurrentUtils.constantFuture(T)"""
        return Future._wrap(_ConcurrentUtils.constantFuture(arg0))

    @staticmethod
    @overload
    def createIfAbsent(arg0: 'ConcurrentMap', arg1: object, arg2: 'ConcurrentInitializer') -> object:
        """public static <K,V> V org.apache.commons.lang3.concurrent.ConcurrentUtils.createIfAbsent(java.util.concurrent.ConcurrentMap<K, V>,K,org.apache.commons.lang3.concurrent.ConcurrentInitializer<V>) throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object._wrap(_ConcurrentUtils.createIfAbsent(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.FutureTasks
from builtins import str
import java.util.concurrent.FutureTask as _FutureTask
_FutureTask = _FutureTask
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.FutureTask as FutureTask
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.Callable as Callable
import org.apache.commons.lang3.concurrent.FutureTasks as _FutureTasks
_FutureTasks = _FutureTasks
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FutureTasks():
    """org.apache.commons.lang3.concurrent.FutureTasks"""
 
    @staticmethod
    def _wrap(java_value: _FutureTasks) -> 'FutureTasks':
        return FutureTasks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FutureTasks):
        """
        Dynamic initializer for FutureTasks.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FutureTasks__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FutureTasks__wrapper":
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

    @staticmethod
    @overload
    def run(arg0: 'Callable') -> 'FutureTask':
        """public static <V> java.util.concurrent.FutureTask<V> org.apache.commons.lang3.concurrent.FutureTasks.run(java.util.concurrent.Callable<V>)"""
        return FutureTask._wrap(_FutureTasks.run(arg0))

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
 
 
# CLASS: org.apache.commons.lang3.concurrent.EventCountCircuitBreaker
from builtins import str
from pyquantum_helper import override
import java.beans.PropertyChangeListener as PropertyChangeListener
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.concurrent.EventCountCircuitBreaker as _EventCountCircuitBreaker
_EventCountCircuitBreaker = _EventCountCircuitBreaker
import org.apache.commons.lang3.concurrent.AbstractCircuitBreaker as _AbstractCircuitBreaker
_AbstractCircuitBreaker = _AbstractCircuitBreaker
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.lang.Integer as Integer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EventCountCircuitBreaker():
    """org.apache.commons.lang3.concurrent.EventCountCircuitBreaker"""
 
    @staticmethod
    def _wrap(java_value: _EventCountCircuitBreaker) -> 'EventCountCircuitBreaker':
        return EventCountCircuitBreaker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventCountCircuitBreaker):
        """
        Dynamic initializer for EventCountCircuitBreaker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventCountCircuitBreaker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventCountCircuitBreaker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public void org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.close()"""
        super(EventCountCircuitBreaker, self).close()

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
    def isClosed(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isClosed()"""
        return bool._wrap(super(AbstractCircuitBreaker, self).isClosed())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'TimeUnit'):
        """public org.apache.commons.lang3.concurrent.EventCountCircuitBreaker(int,long,java.util.concurrent.TimeUnit)"""
        val = _EventCountCircuitBreaker(_int.valueOf(arg0), _long.valueOf(arg1), arg2)
        self.__wrapper = val

    @overload
    def incrementAndCheckState(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.incrementAndCheckState()"""
        return bool._wrap(super(EventCountCircuitBreaker, self).incrementAndCheckState())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def open(self):
        """public void org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.open()"""
        super(EventCountCircuitBreaker, self).open()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def addChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.addChangeListener(java.beans.PropertyChangeListener)"""
        super(_AbstractCircuitBreaker, self).addChangeListener(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getOpeningInterval(self) -> int:
        """public long org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.getOpeningInterval()"""
        return int._wrap(super(EventCountCircuitBreaker, self).getOpeningInterval())

    @overload
    def getClosingThreshold(self) -> int:
        """public int org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.getClosingThreshold()"""
        return int._wrap(super(EventCountCircuitBreaker, self).getClosingThreshold())

    @override
    @overload
    def isOpen(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isOpen()"""
        return bool._wrap(super(AbstractCircuitBreaker, self).isOpen())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def checkState(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.checkState()"""
        return bool._wrap(super(EventCountCircuitBreaker, self).checkState())

    @overload
    def incrementAndCheckState(self, arg0: 'Integer') -> bool:
        """public boolean org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.incrementAndCheckState(java.lang.Integer)"""
        return bool._wrap(super(_EventCountCircuitBreaker, self).incrementAndCheckState(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def removeChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.removeChangeListener(java.beans.PropertyChangeListener)"""
        super(_AbstractCircuitBreaker, self).removeChangeListener(arg0)

    @overload
    def getClosingInterval(self) -> int:
        """public long org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.getClosingInterval()"""
        return int._wrap(super(EventCountCircuitBreaker, self).getClosingInterval())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'TimeUnit', arg3: int):
        """public org.apache.commons.lang3.concurrent.EventCountCircuitBreaker(int,long,java.util.concurrent.TimeUnit,int)"""
        val = _EventCountCircuitBreaker(_int.valueOf(arg0), _long.valueOf(arg1), arg2, _int.valueOf(arg3))
        self.__wrapper = val

    @overload
    def getOpeningThreshold(self) -> int:
        """public int org.apache.commons.lang3.concurrent.EventCountCircuitBreaker.getOpeningThreshold()"""
        return int._wrap(super(EventCountCircuitBreaker, self).getOpeningThreshold())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'TimeUnit', arg3: int, arg4: int, arg5: 'TimeUnit'):
        """public org.apache.commons.lang3.concurrent.EventCountCircuitBreaker(int,long,java.util.concurrent.TimeUnit,int,long,java.util.concurrent.TimeUnit)"""
        val = _EventCountCircuitBreaker(_int.valueOf(arg0), _long.valueOf(arg1), arg2, _int.valueOf(arg3), _long.valueOf(arg4), arg5)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.AtomicInitializer
from builtins import str
from pyquantum_helper import override
import org.apache.commons.lang3.concurrent.AtomicInitializer as _AtomicInitializer
_AtomicInitializer = _AtomicInitializer
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AtomicInitializer():
    """org.apache.commons.lang3.concurrent.AtomicInitializer"""
 
    @staticmethod
    def _wrap(java_value: _AtomicInitializer) -> 'AtomicInitializer':
        return AtomicInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AtomicInitializer):
        """
        Dynamic initializer for AtomicInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AtomicInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AtomicInitializer__wrapper":
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
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.AtomicInitializer()"""
        val = _AtomicInitializer()
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

    @override
    @overload
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.AtomicInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object._wrap(super(AtomicInitializer, self).get())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.AtomicInitializer()"""
        val = _AtomicInitializer()
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
 
 
# CLASS: org.apache.commons.lang3.concurrent.Computable
import org.apache.commons.lang3.concurrent.Computable as _Computable
_Computable = _Computable
from abc import abstractmethod, ABC
 
class Computable():
    """org.apache.commons.lang3.concurrent.Computable"""
 
    @staticmethod
    def _wrap(java_value: _Computable) -> 'Computable':
        return Computable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Computable):
        """
        Dynamic initializer for Computable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Computable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Computable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def compute(self, arg0: object):
        """public abstract O org.apache.commons.lang3.concurrent.Computable.compute(I) throws java.lang.InterruptedException"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import org.apache.commons.lang3.concurrent.AbstractCircuitBreaker as _AbstractCircuitBreaker_State
_State = _AbstractCircuitBreaker_State.State
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class State():
    """org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.State"""
 
    @staticmethod
    def _wrap(java_value: _State) -> 'State':
        return State(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _State):
        """
        Dynamic initializer for State.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_State__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_State__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'State':
        """public static org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State.valueOf(java.lang.String)"""
        return State._wrap(_State.valueOf(arg0))

    @abstractmethod
    def oppositeState(self, ):
        """public abstract org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State.oppositeState()"""
        pass

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
    def values() -> List['State']:
        """public static org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State[] org.apache.commons.lang3.concurrent.AbstractCircuitBreaker$State.values()"""
        return List[State]._wrap(_State.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.commons.lang3.concurrent.UncheckedExecutionException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import org.apache.commons.lang3.concurrent.UncheckedExecutionException as _UncheckedExecutionException
_UncheckedExecutionException = _UncheckedExecutionException
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
 
class UncheckedExecutionException():
    """org.apache.commons.lang3.concurrent.UncheckedExecutionException"""
 
    @staticmethod
    def _wrap(java_value: _UncheckedExecutionException) -> 'UncheckedExecutionException':
        return UncheckedExecutionException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UncheckedExecutionException):
        """
        Dynamic initializer for UncheckedExecutionException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UncheckedExecutionException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UncheckedExecutionException__wrapper":
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
        """public org.apache.commons.lang3.concurrent.UncheckedExecutionException(java.lang.Throwable)"""
        val = _UncheckedExecutionException(arg0)
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
 
 
# CLASS: org.apache.commons.lang3.concurrent.ConcurrentRuntimeException
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
import org.apache.commons.lang3.concurrent.ConcurrentRuntimeException as _ConcurrentRuntimeException
_ConcurrentRuntimeException = _ConcurrentRuntimeException
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConcurrentRuntimeException():
    """org.apache.commons.lang3.concurrent.ConcurrentRuntimeException"""
 
    @staticmethod
    def _wrap(java_value: _ConcurrentRuntimeException) -> 'ConcurrentRuntimeException':
        return ConcurrentRuntimeException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConcurrentRuntimeException):
        """
        Dynamic initializer for ConcurrentRuntimeException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConcurrentRuntimeException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConcurrentRuntimeException__wrapper":
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
        """public org.apache.commons.lang3.concurrent.ConcurrentRuntimeException(java.lang.Throwable)"""
        val = _ConcurrentRuntimeException(arg0)
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

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public org.apache.commons.lang3.concurrent.ConcurrentRuntimeException(java.lang.String,java.lang.Throwable)"""
        val = _ConcurrentRuntimeException(arg0, arg1)
        self.__wrapper = val

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
 
 
# CLASS: org.apache.commons.lang3.concurrent.UncheckedFuture
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.util.concurrent.Future.State as State
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import object
import org.apache.commons.lang3.concurrent.UncheckedFuture as _UncheckedFuture
_UncheckedFuture = _UncheckedFuture
import java.util.Collection as _Collection
_Collection = _Collection
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Future as Future
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.util.stream.Stream as Stream
import java.lang.Throwable as Throwable
import java.util.concurrent.Future as _Future
_Future = _Future
 
class UncheckedFuture():
    """org.apache.commons.lang3.concurrent.UncheckedFuture"""
 
    @staticmethod
    def _wrap(java_value: _UncheckedFuture) -> 'UncheckedFuture':
        return UncheckedFuture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UncheckedFuture):
        """
        Dynamic initializer for UncheckedFuture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UncheckedFuture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UncheckedFuture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, ):
        """public abstract V org.apache.commons.lang3.concurrent.UncheckedFuture.get()"""
        pass

    @abstractmethod
    def cancel(self, arg0: bool):
        """public abstract boolean java.util.concurrent.Future.cancel(boolean)"""
        pass

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'._wrap(super(Future, self).state())

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'._wrap(super(Future, self).exceptionNow())

    @abstractmethod
    def get(self, arg0: int, arg1: 'TimeUnit'):
        """public abstract V org.apache.commons.lang3.concurrent.UncheckedFuture.get(long,java.util.concurrent.TimeUnit)"""
        pass

    @abstractmethod
    def isCancelled(self, ):
        """public abstract boolean java.util.concurrent.Future.isCancelled()"""
        pass

    @staticmethod
    @overload
    def map(arg0: 'Collection') -> 'Stream':
        """public static <T> java.util.stream.Stream<org.apache.commons.lang3.concurrent.UncheckedFuture<T>> org.apache.commons.lang3.concurrent.UncheckedFuture.map(java.util.Collection<java.util.concurrent.Future<T>>)"""
        return Stream._wrap(_UncheckedFuture.map(arg0))

    @override
    @overload
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object._wrap(super(Future, self).resultNow())

    @staticmethod
    @overload
    def on(arg0: 'Collection') -> 'Collection':
        """public static <T> java.util.Collection<org.apache.commons.lang3.concurrent.UncheckedFuture<T>> org.apache.commons.lang3.concurrent.UncheckedFuture.on(java.util.Collection<java.util.concurrent.Future<T>>)"""
        return Collection._wrap(_UncheckedFuture.on(arg0))

    @staticmethod
    @overload
    def on(arg0: 'Future') -> 'UncheckedFuture':
        """public static <T> org.apache.commons.lang3.concurrent.UncheckedFuture<T> org.apache.commons.lang3.concurrent.UncheckedFuture.on(java.util.concurrent.Future<T>)"""
        return UncheckedFuture._wrap(_UncheckedFuture.on(arg0))

    @abstractmethod
    def isDone(self, ):
        """public abstract boolean java.util.concurrent.Future.isDone()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.concurrent.BackgroundInitializer
from builtins import str
import org.apache.commons.lang3.concurrent.BackgroundInitializer as _BackgroundInitializer
_BackgroundInitializer = _BackgroundInitializer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.ExecutorService as ExecutorService
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.util.concurrent.ExecutorService as _ExecutorService
_ExecutorService = _ExecutorService
import java.util.concurrent.Future as Future
from builtins import bool
import java.lang.Long as _long
import java.util.concurrent.Future as _Future
_Future = _Future
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BackgroundInitializer():
    """org.apache.commons.lang3.concurrent.BackgroundInitializer"""
 
    @staticmethod
    def _wrap(java_value: _BackgroundInitializer) -> 'BackgroundInitializer':
        return BackgroundInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BackgroundInitializer):
        """
        Dynamic initializer for BackgroundInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BackgroundInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BackgroundInitializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setExternalExecutor(self, arg0: 'ExecutorService'):
        """public final synchronized void org.apache.commons.lang3.concurrent.BackgroundInitializer.setExternalExecutor(java.util.concurrent.ExecutorService)"""
        super(_BackgroundInitializer, self).setExternalExecutor(arg0)

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getExternalExecutor(self) -> 'ExecutorService':
        """public final synchronized java.util.concurrent.ExecutorService org.apache.commons.lang3.concurrent.BackgroundInitializer.getExternalExecutor()"""
        return 'ExecutorService'._wrap(super(BackgroundInitializer, self).getExternalExecutor())

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
    def start(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.start()"""
        return bool._wrap(super(BackgroundInitializer, self).start())

    @overload
    def isStarted(self) -> bool:
        """public synchronized boolean org.apache.commons.lang3.concurrent.BackgroundInitializer.isStarted()"""
        return bool._wrap(super(BackgroundInitializer, self).isStarted())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def get(self) -> object:
        """public T org.apache.commons.lang3.concurrent.BackgroundInitializer.get() throws org.apache.commons.lang3.concurrent.ConcurrentException"""
        return object._wrap(super(BackgroundInitializer, self).get())

    @overload
    def getFuture(self) -> 'Future':
        """public synchronized java.util.concurrent.Future<T> org.apache.commons.lang3.concurrent.BackgroundInitializer.getFuture()"""
        return 'Future'._wrap(super(BackgroundInitializer, self).getFuture())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.AbstractFutureProxy
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Future.State as State
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.util.concurrent.TimeUnit as TimeUnit
import java.util.concurrent.Future as Future
import java.util.concurrent.Future as _Future_State
_State = _Future_State.State
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import org.apache.commons.lang3.concurrent.AbstractFutureProxy as _AbstractFutureProxy
_AbstractFutureProxy = _AbstractFutureProxy
from builtins import bool
import java.lang.Long as _long
import java.util.concurrent.Future as _Future
_Future = _Future
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractFutureProxy():
    """org.apache.commons.lang3.concurrent.AbstractFutureProxy"""
 
    @staticmethod
    def _wrap(java_value: _AbstractFutureProxy) -> 'AbstractFutureProxy':
        return AbstractFutureProxy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractFutureProxy):
        """
        Dynamic initializer for AbstractFutureProxy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractFutureProxy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractFutureProxy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def cancel(self, arg0: bool) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractFutureProxy.cancel(boolean)"""
        return bool._wrap(super(_AbstractFutureProxy, self).cancel(_boolean.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Future'):
        """public org.apache.commons.lang3.concurrent.AbstractFutureProxy(java.util.concurrent.Future<V>)"""
        val = _AbstractFutureProxy(arg0)
        self.__wrapper = val

    @override
    @overload
    def isCancelled(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractFutureProxy.isCancelled()"""
        return bool._wrap(super(AbstractFutureProxy, self).isCancelled())

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
    def resultNow(self) -> object:
        """public default V java.util.concurrent.Future.resultNow()"""
        return object._wrap(super(Future, self).resultNow())

    @overload
    def get(self, arg0: int, arg1: 'TimeUnit') -> object:
        """public V org.apache.commons.lang3.concurrent.AbstractFutureProxy.get(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_AbstractFutureProxy, self).get(_long.valueOf(arg0), arg1))

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
    def isDone(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractFutureProxy.isDone()"""
        return bool._wrap(super(AbstractFutureProxy, self).isDone())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def state(self) -> 'State.Future$State':
        """public default java.util.concurrent.Future$State java.util.concurrent.Future.state()"""
        return 'State.Future$State'._wrap(super(Future, self).state())

    @overload
    def getFuture(self) -> 'Future':
        """public java.util.concurrent.Future<V> org.apache.commons.lang3.concurrent.AbstractFutureProxy.getFuture()"""
        return 'Future'._wrap(super(AbstractFutureProxy, self).getFuture())

    @override
    @overload
    def exceptionNow(self) -> 'Throwable':
        """public default java.lang.Throwable java.util.concurrent.Future.exceptionNow()"""
        return 'Throwable'._wrap(super(Future, self).exceptionNow())

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
    def get(self) -> object:
        """public V org.apache.commons.lang3.concurrent.AbstractFutureProxy.get() throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(AbstractFutureProxy, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.UncheckedTimeoutException
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
import org.apache.commons.lang3.concurrent.UncheckedTimeoutException as _UncheckedTimeoutException
_UncheckedTimeoutException = _UncheckedTimeoutException
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UncheckedTimeoutException():
    """org.apache.commons.lang3.concurrent.UncheckedTimeoutException"""
 
    @staticmethod
    def _wrap(java_value: _UncheckedTimeoutException) -> 'UncheckedTimeoutException':
        return UncheckedTimeoutException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UncheckedTimeoutException):
        """
        Dynamic initializer for UncheckedTimeoutException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UncheckedTimeoutException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UncheckedTimeoutException__wrapper":
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
        """public org.apache.commons.lang3.concurrent.UncheckedTimeoutException(java.lang.Throwable)"""
        val = _UncheckedTimeoutException(arg0)
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
 
 
# CLASS: org.apache.commons.lang3.concurrent.BasicThreadFactory
import java.lang.Thread as Thread
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Thread as _Thread
_Thread = _Thread
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.Thread.UncaughtExceptionHandler as UncaughtExceptionHandler
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
import java.lang.Integer as _int
import java.lang.Thread as _Thread_UncaughtExceptionHandler
_UncaughtExceptionHandler = _Thread_UncaughtExceptionHandler.UncaughtExceptionHandler
import java.lang.Integer as Integer
import java.util.concurrent.ThreadFactory as _ThreadFactory
_ThreadFactory = _ThreadFactory
import org.apache.commons.lang3.concurrent.BasicThreadFactory as _BasicThreadFactory
_BasicThreadFactory = _BasicThreadFactory
from builtins import bool
import java.util.concurrent.ThreadFactory as ThreadFactory
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BasicThreadFactory():
    """org.apache.commons.lang3.concurrent.BasicThreadFactory"""
 
    @staticmethod
    def _wrap(java_value: _BasicThreadFactory) -> 'BasicThreadFactory':
        return BasicThreadFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BasicThreadFactory):
        """
        Dynamic initializer for BasicThreadFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BasicThreadFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BasicThreadFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getWrappedFactory(self) -> 'ThreadFactory':
        """public final java.util.concurrent.ThreadFactory org.apache.commons.lang3.concurrent.BasicThreadFactory.getWrappedFactory()"""
        return 'ThreadFactory'._wrap(super(BasicThreadFactory, self).getWrappedFactory())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getNamingPattern(self) -> str:
        """public final java.lang.String org.apache.commons.lang3.concurrent.BasicThreadFactory.getNamingPattern()"""
        return str._wrap(super(BasicThreadFactory, self).getNamingPattern())

    @overload
    def getThreadCount(self) -> int:
        """public long org.apache.commons.lang3.concurrent.BasicThreadFactory.getThreadCount()"""
        return int._wrap(super(BasicThreadFactory, self).getThreadCount())

    @overload
    def getDaemonFlag(self) -> 'Boolean':
        """public final java.lang.Boolean org.apache.commons.lang3.concurrent.BasicThreadFactory.getDaemonFlag()"""
        return 'Boolean'._wrap(super(BasicThreadFactory, self).getDaemonFlag())

    @overload
    def newThread(self, arg0: 'Runnable') -> 'Thread':
        """public java.lang.Thread org.apache.commons.lang3.concurrent.BasicThreadFactory.newThread(java.lang.Runnable)"""
        return 'Thread'._wrap(super(_BasicThreadFactory, self).newThread(arg0))

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

    @overload
    def getPriority(self) -> 'Integer':
        """public final java.lang.Integer org.apache.commons.lang3.concurrent.BasicThreadFactory.getPriority()"""
        return _transform(super(BasicThreadFactory, self).getPriority()).'Integer'Value()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getUncaughtExceptionHandler(self) -> 'UncaughtExceptionHandler.Thread$UncaughtExceptionHandler':
        """public final java.lang.Thread$UncaughtExceptionHandler org.apache.commons.lang3.concurrent.BasicThreadFactory.getUncaughtExceptionHandler()"""
        return 'UncaughtExceptionHandler.Thread$UncaughtExceptionHandler'._wrap(super(BasicThreadFactory, self).getUncaughtExceptionHandler())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.concurrent.CircuitBreaker
import org.apache.commons.lang3.concurrent.CircuitBreaker as _CircuitBreaker
_CircuitBreaker = _CircuitBreaker
from abc import abstractmethod, ABC
 
class CircuitBreaker():
    """org.apache.commons.lang3.concurrent.CircuitBreaker"""
 
    @staticmethod
    def _wrap(java_value: _CircuitBreaker) -> 'CircuitBreaker':
        return CircuitBreaker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CircuitBreaker):
        """
        Dynamic initializer for CircuitBreaker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CircuitBreaker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CircuitBreaker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def incrementAndCheckState(self, arg0: object):
        """public abstract boolean org.apache.commons.lang3.concurrent.CircuitBreaker.incrementAndCheckState(T)"""
        pass

    @abstractmethod
    def isOpen(self, ):
        """public abstract boolean org.apache.commons.lang3.concurrent.CircuitBreaker.isOpen()"""
        pass

    @abstractmethod
    def checkState(self, ):
        """public abstract boolean org.apache.commons.lang3.concurrent.CircuitBreaker.checkState()"""
        pass

    @abstractmethod
    def close(self, ):
        """public abstract void org.apache.commons.lang3.concurrent.CircuitBreaker.close()"""
        pass

    @abstractmethod
    def isClosed(self, ):
        """public abstract boolean org.apache.commons.lang3.concurrent.CircuitBreaker.isClosed()"""
        pass

    @abstractmethod
    def open(self, ):
        """public abstract void org.apache.commons.lang3.concurrent.CircuitBreaker.open()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.concurrent.AbstractCircuitBreaker
from builtins import str
from pyquantum_helper import override
import java.beans.PropertyChangeListener as PropertyChangeListener
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import org.apache.commons.lang3.concurrent.AbstractCircuitBreaker as _AbstractCircuitBreaker
_AbstractCircuitBreaker = _AbstractCircuitBreaker
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractCircuitBreaker():
    """org.apache.commons.lang3.concurrent.AbstractCircuitBreaker"""
 
    @staticmethod
    def _wrap(java_value: _AbstractCircuitBreaker) -> 'AbstractCircuitBreaker':
        return AbstractCircuitBreaker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractCircuitBreaker):
        """
        Dynamic initializer for AbstractCircuitBreaker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractCircuitBreaker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractCircuitBreaker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def close(self):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.close()"""
        super(AbstractCircuitBreaker, self).close()

    @overload
    def addChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.addChangeListener(java.beans.PropertyChangeListener)"""
        super(_AbstractCircuitBreaker, self).addChangeListener(arg0)

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.concurrent.AbstractCircuitBreaker()"""
        val = _AbstractCircuitBreaker()
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
    def removeChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.removeChangeListener(java.beans.PropertyChangeListener)"""
        super(_AbstractCircuitBreaker, self).removeChangeListener(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isOpen(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isOpen()"""
        return bool._wrap(super(AbstractCircuitBreaker, self).isOpen())

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
    def __init__(self):
        """public org.apache.commons.lang3.concurrent.AbstractCircuitBreaker()"""
        val = _AbstractCircuitBreaker()
        self.__wrapper = val

    @override
    @overload
    def isClosed(self) -> bool:
        """public boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.isClosed()"""
        return bool._wrap(super(AbstractCircuitBreaker, self).isClosed())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def open(self):
        """public void org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.open()"""
        super(AbstractCircuitBreaker, self).open()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def incrementAndCheckState(self, arg0: object):
        """public abstract boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.incrementAndCheckState(T)"""
        pass

    @abstractmethod
    def checkState(self, ):
        """public abstract boolean org.apache.commons.lang3.concurrent.AbstractCircuitBreaker.checkState()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())