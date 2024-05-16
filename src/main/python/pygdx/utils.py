from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.io.Closeable as Closeable
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.SharedLibraryLoader as _SharedLibraryLoader
_SharedLibraryLoader = _SharedLibraryLoader
import java.lang.String as _string
import java.io.File as _File
_File = _File
import java.lang.Integer as _int
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SharedLibraryLoader():
    """com.badlogic.gdx.utils.SharedLibraryLoader"""
 
    @staticmethod
    def _wrap(java_value: _SharedLibraryLoader) -> 'SharedLibraryLoader':
        return SharedLibraryLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SharedLibraryLoader):
        """
        Dynamic initializer for SharedLibraryLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SharedLibraryLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SharedLibraryLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def mapLibraryName(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.SharedLibraryLoader.mapLibraryName(java.lang.String)"""
        return str._wrap(super(_SharedLibraryLoader, self).mapLibraryName(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.SharedLibraryLoader()"""
        val = _SharedLibraryLoader()
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
    def extractFile(self, arg0: str, arg1: str) -> 'File':
        """public java.io.File com.badlogic.gdx.utils.SharedLibraryLoader.extractFile(java.lang.String,java.lang.String) throws java.io.IOException"""
        return 'File'._wrap(super(_SharedLibraryLoader, self).extractFile(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def load(self, arg0: str):
        """public void com.badlogic.gdx.utils.SharedLibraryLoader.load(java.lang.String)"""
        super(_SharedLibraryLoader, self).load(arg0)

    @staticmethod
    @overload
    def closeQuietly(arg0: 'Closeable'):
        """public static void com.badlogic.gdx.utils.SharedLibraryLoader.closeQuietly(java.io.Closeable)"""
        _SharedLibraryLoader.closeQuietly(arg0)

    @staticmethod
    @overload
    def setLoaded(arg0: str):
        """public static synchronized void com.badlogic.gdx.utils.SharedLibraryLoader.setLoaded(java.lang.String)"""
        _SharedLibraryLoader.setLoaded(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.SharedLibraryLoader()"""
        val = _SharedLibraryLoader()
        self.__wrapper = val

    @overload
    def crc(self, arg0: 'InputStream') -> str:
        """public java.lang.String com.badlogic.gdx.utils.SharedLibraryLoader.crc(java.io.InputStream)"""
        return str._wrap(super(_SharedLibraryLoader, self).crc(arg0))

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
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.utils.SharedLibraryLoader(java.lang.String)"""
        val = _SharedLibraryLoader(arg0)
        self.__wrapper = val

    @overload
    def extractFileTo(self, arg0: str, arg1: 'File'):
        """public void com.badlogic.gdx.utils.SharedLibraryLoader.extractFileTo(java.lang.String,java.io.File) throws java.io.IOException"""
        super(_SharedLibraryLoader, self).extractFileTo(arg0, arg1)

    @staticmethod
    @overload
    def isLoaded(arg0: str) -> bool:
        """public static synchronized boolean com.badlogic.gdx.utils.SharedLibraryLoader.isLoaded(java.lang.String)"""
        return bool._wrap(_SharedLibraryLoader.isLoaded(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.utils.SharedLibraryLoader
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.io.Closeable as Closeable
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.SharedLibraryLoader as _SharedLibraryLoader
_SharedLibraryLoader = _SharedLibraryLoader
import java.lang.String as _string
import java.io.File as _File
_File = _File
import java.lang.Integer as _int
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SharedLibraryLoader():
    """com.badlogic.gdx.utils.SharedLibraryLoader"""
 
    @staticmethod
    def _wrap(java_value: _SharedLibraryLoader) -> 'SharedLibraryLoader':
        return SharedLibraryLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SharedLibraryLoader):
        """
        Dynamic initializer for SharedLibraryLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SharedLibraryLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SharedLibraryLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def mapLibraryName(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.utils.SharedLibraryLoader.mapLibraryName(java.lang.String)"""
        return str._wrap(super(_SharedLibraryLoader, self).mapLibraryName(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.SharedLibraryLoader()"""
        val = _SharedLibraryLoader()
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
    def extractFile(self, arg0: str, arg1: str) -> 'File':
        """public java.io.File com.badlogic.gdx.utils.SharedLibraryLoader.extractFile(java.lang.String,java.lang.String) throws java.io.IOException"""
        return 'File'._wrap(super(_SharedLibraryLoader, self).extractFile(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def load(self, arg0: str):
        """public void com.badlogic.gdx.utils.SharedLibraryLoader.load(java.lang.String)"""
        super(_SharedLibraryLoader, self).load(arg0)

    @staticmethod
    @overload
    def closeQuietly(arg0: 'Closeable'):
        """public static void com.badlogic.gdx.utils.SharedLibraryLoader.closeQuietly(java.io.Closeable)"""
        _SharedLibraryLoader.closeQuietly(arg0)

    @staticmethod
    @overload
    def setLoaded(arg0: str):
        """public static synchronized void com.badlogic.gdx.utils.SharedLibraryLoader.setLoaded(java.lang.String)"""
        _SharedLibraryLoader.setLoaded(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.SharedLibraryLoader()"""
        val = _SharedLibraryLoader()
        self.__wrapper = val

    @overload
    def crc(self, arg0: 'InputStream') -> str:
        """public java.lang.String com.badlogic.gdx.utils.SharedLibraryLoader.crc(java.io.InputStream)"""
        return str._wrap(super(_SharedLibraryLoader, self).crc(arg0))

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
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.utils.SharedLibraryLoader(java.lang.String)"""
        val = _SharedLibraryLoader(arg0)
        self.__wrapper = val

    @overload
    def extractFileTo(self, arg0: str, arg1: 'File'):
        """public void com.badlogic.gdx.utils.SharedLibraryLoader.extractFileTo(java.lang.String,java.io.File) throws java.io.IOException"""
        super(_SharedLibraryLoader, self).extractFileTo(arg0, arg1)

    @staticmethod
    @overload
    def isLoaded(arg0: str) -> bool:
        """public static synchronized boolean com.badlogic.gdx.utils.SharedLibraryLoader.isLoaded(java.lang.String)"""
        return bool._wrap(_SharedLibraryLoader.isLoaded(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.utils.SharedLibraryLoader 
 
 
# CLASS: com.badlogic.gdx.utils.SharedLibraryLoadRuntimeException
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
import com.badlogic.gdx.utils.SharedLibraryLoadRuntimeException as _SharedLibraryLoadRuntimeException
_SharedLibraryLoadRuntimeException = _SharedLibraryLoadRuntimeException
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
 
class SharedLibraryLoadRuntimeException():
    """com.badlogic.gdx.utils.SharedLibraryLoadRuntimeException"""
 
    @staticmethod
    def _wrap(java_value: _SharedLibraryLoadRuntimeException) -> 'SharedLibraryLoadRuntimeException':
        return SharedLibraryLoadRuntimeException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SharedLibraryLoadRuntimeException):
        """
        Dynamic initializer for SharedLibraryLoadRuntimeException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SharedLibraryLoadRuntimeException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SharedLibraryLoadRuntimeException__wrapper":
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

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.utils.SharedLibraryLoadRuntimeException(java.lang.String)"""
        val = _SharedLibraryLoadRuntimeException(arg0)
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

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.badlogic.gdx.utils.SharedLibraryLoadRuntimeException(java.lang.String,java.lang.Throwable)"""
        val = _SharedLibraryLoadRuntimeException(arg0, arg1)
        self.__wrapper = val

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
        """public com.badlogic.gdx.utils.SharedLibraryLoadRuntimeException(java.lang.Throwable)"""
        val = _SharedLibraryLoadRuntimeException(arg0)
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