from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.util.CollectionUtils as __CollectionUtils
__CollectionUtils = __CollectionUtils
import java.util.Collection as Collection
import java.lang.Comparable as Comparable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Comparable as __Comparable
__Comparable = __Comparable
from builtins import int
 
class CollectionUtils():
    """dev.ultreon.libs.commons.v0.util.CollectionUtils"""
 
    @staticmethod
    def __wrap(java_value: __CollectionUtils) -> 'CollectionUtils':
        return CollectionUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CollectionUtils):
        """
        Dynamic initializer for CollectionUtils.
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
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.CollectionUtils()"""
        val = __CollectionUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.CollectionUtils()"""
        val = __CollectionUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def max(arg0: 'Collection', arg1: 'Comparable') -> 'Comparable':
        """public static <T extends java.lang.Comparable<T>> T dev.ultreon.libs.commons.v0.util.CollectionUtils.max(java.util.Collection<T>,T)"""
        return Comparable.__wrap(__CollectionUtils.max(arg0, arg1))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.CollectionUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.util.CollectionUtils as __CollectionUtils
__CollectionUtils = __CollectionUtils
import java.util.Collection as Collection
import java.lang.Comparable as Comparable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Comparable as __Comparable
__Comparable = __Comparable
from builtins import int
 
class CollectionUtils():
    """dev.ultreon.libs.commons.v0.util.CollectionUtils"""
 
    @staticmethod
    def __wrap(java_value: __CollectionUtils) -> 'CollectionUtils':
        return CollectionUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CollectionUtils):
        """
        Dynamic initializer for CollectionUtils.
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
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.CollectionUtils()"""
        val = __CollectionUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.CollectionUtils()"""
        val = __CollectionUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def max(arg0: 'Collection', arg1: 'Comparable') -> 'Comparable':
        """public static <T extends java.lang.Comparable<T>> T dev.ultreon.libs.commons.v0.util.CollectionUtils.max(java.util.Collection<T>,T)"""
        return Comparable.__wrap(__CollectionUtils.max(arg0, arg1))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.CollectionUtils 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.IllegalCallerException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import dev.ultreon.libs.commons.v0.util.IllegalCallerException as __IllegalCallerException
__IllegalCallerException = __IllegalCallerException
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
 
class IllegalCallerException(__RuntimeException, RuntimeException):
    """dev.ultreon.libs.commons.v0.util.IllegalCallerException"""
 
    @staticmethod
    def __wrap(java_value: __IllegalCallerException) -> 'IllegalCallerException':
        return IllegalCallerException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IllegalCallerException):
        """
        Dynamic initializer for IllegalCallerException.
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
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.libs.commons.v0.util.IllegalCallerException(java.lang.String,java.lang.Throwable)"""
        val = __IllegalCallerException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.IllegalCallerException()"""
        val = __IllegalCallerException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.libs.commons.v0.util.IllegalCallerException(java.lang.Throwable)"""
        val = __IllegalCallerException(arg0)
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
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

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
        """public dev.ultreon.libs.commons.v0.util.IllegalCallerException()"""
        val = __IllegalCallerException()
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
    def __init__(self, arg0: str):
        """public dev.ultreon.libs.commons.v0.util.IllegalCallerException(java.lang.String)"""
        val = __IllegalCallerException(arg0)
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
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.FileUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import java.io.PrintWriter as PrintWriter
import dev.ultreon.libs.commons.v0.util.FileUtils as __FileUtils
__FileUtils = __FileUtils
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintWriter as __PrintWriter
__PrintWriter = __PrintWriter
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FileUtils(commons.__UtilityClass, v0.UtilityClass):
    """dev.ultreon.libs.commons.v0.util.FileUtils"""
 
    @staticmethod
    def __wrap(java_value: __FileUtils) -> 'FileUtils':
        return FileUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileUtils):
        """
        Dynamic initializer for FileUtils.
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

    @staticmethod
    @overload
    def setCwd(arg0: 'File') -> bool:
        """public static boolean dev.ultreon.libs.commons.v0.util.FileUtils.setCwd(java.io.File)"""
        return bool.__wrap(__FileUtils.setCwd(arg0))

    @staticmethod
    @overload
    def openOutputFile(arg0: str) -> 'PrintWriter':
        """public static java.io.PrintWriter dev.ultreon.libs.commons.v0.util.FileUtils.openOutputFile(java.lang.String)"""
        return PrintWriter.__wrap(__FileUtils.openOutputFile(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.FileUtils()"""
        val = __FileUtils()
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
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.FileUtils()"""
        val = __FileUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getExtension(arg0: 'File') -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.FileUtils.getExtension(java.io.File)"""
        return str.__wrap(__FileUtils.getExtension(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.ColorUtils
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.util.ColorUtils as __ColorUtils
__ColorUtils = __ColorUtils
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.commons.v0.Color as __Color
__Color = __Color
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ColorUtils(commons.__UtilityClass, v0.UtilityClass):
    """dev.ultreon.libs.commons.v0.util.ColorUtils"""
 
    @staticmethod
    def __wrap(java_value: __ColorUtils) -> 'ColorUtils':
        return ColorUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ColorUtils):
        """
        Dynamic initializer for ColorUtils.
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
        """public dev.ultreon.libs.commons.v0.util.ColorUtils()"""
        val = __ColorUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.ColorUtils()"""
        val = __ColorUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def parseHexList(arg0: str) -> List['v0.Color']:
        """public static dev.ultreon.libs.commons.v0.Color[] dev.ultreon.libs.commons.v0.util.ColorUtils.parseHexList(java.lang.String)"""
        return List[v0.Color].__wrap(__ColorUtils.parseHexList(arg0))

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
    def extractMultiHex(*arg0: str) -> List['v0.Color']:
        """public static dev.ultreon.libs.commons.v0.Color[] dev.ultreon.libs.commons.v0.util.ColorUtils.extractMultiHex(java.lang.String...)"""
        return List[v0.Color].__wrap(__ColorUtils.extractMultiHex(arg0))

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.StringUtils
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.awt.Font as Font
import java.text.AttributedString as __AttributedString
__AttributedString = __AttributedString
import java.text.AttributedString as AttributedString
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.awt.FontMetrics as FontMetrics
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.libs.commons.v0.util.StringUtils as __StringUtils
__StringUtils = __StringUtils
import java.util.List as List
from builtins import int
 
class StringUtils(commons.__UtilityClass, v0.UtilityClass):
    """dev.ultreon.libs.commons.v0.util.StringUtils"""
 
    @staticmethod
    def __wrap(java_value: __StringUtils) -> 'StringUtils':
        return StringUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringUtils):
        """
        Dynamic initializer for StringUtils.
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

    @staticmethod
    @overload
    def join(arg0: 'List', arg1: str) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.StringUtils.join(java.util.List<java.lang.String>,java.lang.String)"""
        return str.__wrap(__StringUtils.join(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.StringUtils()"""
        val = __StringUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def wrapLineInto(arg0: str, arg1: 'List', arg2: 'FontMetrics', arg3: int):
        """public static void dev.ultreon.libs.commons.v0.util.StringUtils.wrapLineInto(java.lang.String,java.util.List<java.lang.String>,java.awt.FontMetrics,int)"""
        __StringUtils.wrapLineInto(arg0, arg1, arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def splitIntoLines(arg0: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.libs.commons.v0.util.StringUtils.splitIntoLines(java.lang.String)"""
        return List.__wrap(__StringUtils.splitIntoLines(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def wrap(arg0: str, arg1: 'FontMetrics', arg2: int) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.libs.commons.v0.util.StringUtils.wrap(java.lang.String,java.awt.FontMetrics,int)"""
        return List.__wrap(__StringUtils.wrap(arg0, arg1, __int.valueOf(arg2)))

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
    def findBreakBefore(arg0: str, arg1: int) -> int:
        """public static int dev.ultreon.libs.commons.v0.util.StringUtils.findBreakBefore(java.lang.String,int)"""
        return int.__wrap(__StringUtils.findBreakBefore(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def count(arg0: str, arg1: str) -> int:
        """public static int dev.ultreon.libs.commons.v0.util.StringUtils.count(java.lang.String,char)"""
        return int.__wrap(__StringUtils.count(arg0, __char.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createFallbackString(arg0: str, arg1: 'Font', arg2: 'Font') -> 'AttributedString':
        """public static java.text.AttributedString dev.ultreon.libs.commons.v0.util.StringUtils.createFallbackString(java.lang.String,java.awt.Font,java.awt.Font)"""
        return AttributedString.__wrap(__StringUtils.createFallbackString(arg0, arg1, arg2))

    @staticmethod
    @overload
    def findBreakAfter(arg0: str, arg1: int) -> int:
        """public static int dev.ultreon.libs.commons.v0.util.StringUtils.findBreakAfter(java.lang.String,int)"""
        return int.__wrap(__StringUtils.findBreakAfter(arg0, __int.valueOf(arg1)))

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.StringUtils()"""
        val = __StringUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.ExceptionUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.RuntimeException as __RuntimeException
__RuntimeException = __RuntimeException
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.libs.commons.v0.util.ExceptionUtils as __ExceptionUtils
__ExceptionUtils = __ExceptionUtils
import java.lang.RuntimeException as RuntimeException
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ExceptionUtils(commons.__UtilityClass, v0.UtilityClass):
    """dev.ultreon.libs.commons.v0.util.ExceptionUtils"""
 
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getStackTrace(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.ExceptionUtils.getStackTrace(java.lang.String)"""
        return str.__wrap(__ExceptionUtils.getStackTrace(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getStackTrace(arg0: 'Throwable') -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.ExceptionUtils.getStackTrace(java.lang.Throwable)"""
        return str.__wrap(__ExceptionUtils.getStackTrace(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getStackTrace() -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.ExceptionUtils.getStackTrace()"""
        return str.__wrap(__ExceptionUtils.getStackTrace())

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
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.ExceptionUtils()"""
        val = __ExceptionUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def utilityClass() -> 'RuntimeException':
        """public static java.lang.RuntimeException dev.ultreon.libs.commons.v0.util.ExceptionUtils.utilityClass()"""
        return RuntimeException.__wrap(__ExceptionUtils.utilityClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.ExceptionUtils()"""
        val = __ExceptionUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.ClassUtils
from builtins import str
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.libs.commons.v0.util.ClassUtils as __ClassUtils
__ClassUtils = __ClassUtils
from builtins import int
 
class ClassUtils(commons.__UtilityClass, v0.UtilityClass):
    """dev.ultreon.libs.commons.v0.util.ClassUtils"""
 
    @staticmethod
    def __wrap(java_value: __ClassUtils) -> 'ClassUtils':
        return ClassUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClassUtils):
        """
        Dynamic initializer for ClassUtils.
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
    def getCallerClassName() -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.ClassUtils.getCallerClassName()"""
        return str.__wrap(__ClassUtils.getCallerClassName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def checkCallerClassExtends(arg0: 'Class'):
        """public static void dev.ultreon.libs.commons.v0.util.ClassUtils.checkCallerClassExtends(java.lang.Class<?>)"""
        __ClassUtils.checkCallerClassExtends(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.ClassUtils()"""
        val = __ClassUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getCallerClass() -> 'type.Class':
        """public static java.lang.Class<?> dev.ultreon.libs.commons.v0.util.ClassUtils.getCallerClass()"""
        return type.Class.__wrap(__ClassUtils.getCallerClass())

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

    @staticmethod
    @overload
    def checkCallerClassEquals(arg0: 'Class'):
        """public static void dev.ultreon.libs.commons.v0.util.ClassUtils.checkCallerClassEquals(java.lang.Class<?>)"""
        __ClassUtils.checkCallerClassEquals(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.ClassUtils()"""
        val = __ClassUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.IOUtils
from builtins import str
from pyquantum_helper import override
import dev.ultreon.libs.commons.v0.util.IOUtils as __IOUtils
__IOUtils = __IOUtils
import java.lang.Object as __object
from builtins import type
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IOUtils():
    """dev.ultreon.libs.commons.v0.util.IOUtils"""
 
    @staticmethod
    def __wrap(java_value: __IOUtils) -> 'IOUtils':
        return IOUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOUtils):
        """
        Dynamic initializer for IOUtils.
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
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.IOUtils()"""
        val = __IOUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.IOUtils()"""
        val = __IOUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def readAllBytes(arg0: 'InputStream') -> List[int]:
        """public static byte[] dev.ultreon.libs.commons.v0.util.IOUtils.readAllBytes(java.io.InputStream) throws java.io.IOException"""
        return List[int].__wrap(__IOUtils.readAllBytes(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.TimeUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.commons.v0.util.TimeUtils as __TimeUtils
__TimeUtils = __TimeUtils
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class TimeUtils(commons.__UtilityClass, v0.UtilityClass):
    """dev.ultreon.libs.commons.v0.util.TimeUtils"""
 
    @staticmethod
    def __wrap(java_value: __TimeUtils) -> 'TimeUtils':
        return TimeUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TimeUtils):
        """
        Dynamic initializer for TimeUtils.
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
    def formatDuration(arg0: int) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.TimeUtils.formatDuration(long)"""
        return str.__wrap(__TimeUtils.formatDuration(__long.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.util.TimeUtils()"""
        val = __TimeUtils()
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

    @staticmethod
    @overload
    def formatDuration(arg0: int, arg1: int, arg2: float) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.util.TimeUtils.formatDuration(int,int,double)"""
        return str.__wrap(__TimeUtils.formatDuration(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.util.TimeUtils()"""
        val = __TimeUtils()
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
 
 
# CLASS: dev.ultreon.libs.commons.v0.util.EnumUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.commons.v0.util.EnumUtils as __EnumUtils
__EnumUtils = __EnumUtils
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import int
 
class EnumUtils():
    """dev.ultreon.libs.commons.v0.util.EnumUtils"""
 
    @staticmethod
    def __wrap(java_value: __EnumUtils) -> 'EnumUtils':
        return EnumUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EnumUtils):
        """
        Dynamic initializer for EnumUtils.
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
    def validate(arg0: object, arg1: 'Class') -> bool:
        """public static <E extends java.lang.Enum<E>> boolean dev.ultreon.libs.commons.v0.util.EnumUtils.validate(java.lang.Object,java.lang.Class<E>)"""
        return bool.__wrap(__EnumUtils.validate(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def byIndex(arg0: int, arg1: 'Enum', arg2: 'Function') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E dev.ultreon.libs.commons.v0.util.EnumUtils.byIndex(int,E,java.util.function.Function<E, java.lang.Integer>)"""
        return Enum.__wrap(__EnumUtils.byIndex(__int.valueOf(arg0), arg1, arg2))

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
    def byOrdinal(arg0: int, arg1: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E dev.ultreon.libs.commons.v0.util.EnumUtils.byOrdinal(int,E)"""
        return Enum.__wrap(__EnumUtils.byOrdinal(__int.valueOf(arg0), arg1))

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
    def byName(arg0: str, arg1: 'Enum') -> 'Enum':
        """public static <E extends java.lang.Enum<E>> E dev.ultreon.libs.commons.v0.util.EnumUtils.byName(java.lang.String,E)"""
        return Enum.__wrap(__EnumUtils.byName(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))