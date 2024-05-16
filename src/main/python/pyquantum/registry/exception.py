from __future__ import annotations
from overload import overload


 
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
import dev.ultreon.quantum.registry.exception.RegistryException as __RegistryException
__RegistryException = __RegistryException
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
 
class RegistryException(__IllegalStateException, IllegalStateException):
    """dev.ultreon.quantum.registry.exception.RegistryException"""
 
    @staticmethod
    def __wrap(java_value: __RegistryException) -> 'RegistryException':
        return RegistryException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegistryException):
        """
        Dynamic initializer for RegistryException.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.registry.exception.RegistryException(java.lang.String,java.lang.Throwable)"""
        val = __RegistryException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.registry.exception.RegistryException(java.lang.Throwable)"""
        val = __RegistryException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.registry.exception.RegistryException()"""
        val = __RegistryException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.registry.exception.RegistryException(java.lang.String)"""
        val = __RegistryException(arg0)
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.registry.exception.RegistryException()"""
        val = __RegistryException()
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

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

 
 
 
# CLASS: dev.ultreon.quantum.registry.exception.RegistryException
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
import dev.ultreon.quantum.registry.exception.RegistryException as __RegistryException
__RegistryException = __RegistryException
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
 
class RegistryException(__IllegalStateException, IllegalStateException):
    """dev.ultreon.quantum.registry.exception.RegistryException"""
 
    @staticmethod
    def __wrap(java_value: __RegistryException) -> 'RegistryException':
        return RegistryException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegistryException):
        """
        Dynamic initializer for RegistryException.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.registry.exception.RegistryException(java.lang.String,java.lang.Throwable)"""
        val = __RegistryException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.registry.exception.RegistryException(java.lang.Throwable)"""
        val = __RegistryException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.registry.exception.RegistryException()"""
        val = __RegistryException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.registry.exception.RegistryException(java.lang.String)"""
        val = __RegistryException(arg0)
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.registry.exception.RegistryException()"""
        val = __RegistryException()
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

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

 
 
 
# CLASS: dev.ultreon.quantum.registry.exception.RegistryException