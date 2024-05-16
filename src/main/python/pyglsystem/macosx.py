from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.macosx.LibC as _LibC
_LibC = _LibC
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibC():
    """org.lwjgl.system.macosx.LibC"""
 
    @staticmethod
    def _wrap(java_value: _LibC) -> 'LibC':
        return LibC(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibC):
        """
        Dynamic initializer for LibC.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibC__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibC__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getpid() -> int:
        """public static long org.lwjgl.system.macosx.LibC.getpid()"""
        return int._wrap(_LibC.getpid())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.lwjgl.system.macosx.LibC
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.macosx.LibC as _LibC
_LibC = _LibC
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibC():
    """org.lwjgl.system.macosx.LibC"""
 
    @staticmethod
    def _wrap(java_value: _LibC) -> 'LibC':
        return LibC(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibC):
        """
        Dynamic initializer for LibC.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibC__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibC__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getpid() -> int:
        """public static long org.lwjgl.system.macosx.LibC.getpid()"""
        return int._wrap(_LibC.getpid())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.lwjgl.system.macosx.LibC 
 
 
# CLASS: org.lwjgl.system.macosx.DynamicLinkLoader
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.lwjgl.system.macosx.DynamicLinkLoader as _DynamicLinkLoader
_DynamicLinkLoader = _DynamicLinkLoader
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DynamicLinkLoader():
    """org.lwjgl.system.macosx.DynamicLinkLoader"""
 
    @staticmethod
    def _wrap(java_value: _DynamicLinkLoader) -> 'DynamicLinkLoader':
        return DynamicLinkLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DynamicLinkLoader):
        """
        Dynamic initializer for DynamicLinkLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DynamicLinkLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DynamicLinkLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def dlerror() -> str:
        """public static java.lang.String org.lwjgl.system.macosx.DynamicLinkLoader.dlerror()"""
        return str._wrap(_DynamicLinkLoader.dlerror())

    @staticmethod
    @overload
    def dlsym(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.DynamicLinkLoader.dlsym(long,java.lang.CharSequence)"""
        return int._wrap(_DynamicLinkLoader.dlsym(_long.valueOf(arg0), arg1))

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

    @staticmethod
    @overload
    def ndlsym(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.macosx.DynamicLinkLoader.ndlsym(long,long)"""
        return int._wrap(_DynamicLinkLoader.ndlsym(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def ndlopen(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.macosx.DynamicLinkLoader.ndlopen(long,int)"""
        return int._wrap(_DynamicLinkLoader.ndlopen(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def ndlerror() -> int:
        """public static native long org.lwjgl.system.macosx.DynamicLinkLoader.ndlerror()"""
        return int._wrap(_DynamicLinkLoader.ndlerror())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def dlsym(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.DynamicLinkLoader.dlsym(long,java.nio.ByteBuffer)"""
        return int._wrap(_DynamicLinkLoader.dlsym(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def dlclose(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.DynamicLinkLoader.dlclose(long)"""
        return int._wrap(_DynamicLinkLoader.dlclose(_long.valueOf(arg0)))

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

    @staticmethod
    @overload
    def dlopen(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.DynamicLinkLoader.dlopen(java.nio.ByteBuffer,int)"""
        return int._wrap(_DynamicLinkLoader.dlopen(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def dlopen(arg0: 'CharSequence', arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.DynamicLinkLoader.dlopen(java.lang.CharSequence,int)"""
        return int._wrap(_DynamicLinkLoader.dlopen(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def ndlclose(arg0: int) -> int:
        """public static native int org.lwjgl.system.macosx.DynamicLinkLoader.ndlclose(long)"""
        return int._wrap(_DynamicLinkLoader.ndlclose(_long.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.system.macosx.MacOSXLibrary
import org.lwjgl.system.SharedLibrary as _SharedLibrary_Default
_Default = _SharedLibrary_Default.Default
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.lwjgl.system.FunctionProvider as _FunctionProvider
_FunctionProvider = _FunctionProvider
import org.lwjgl.system.macosx.MacOSXLibrary as _MacOSXLibrary
_MacOSXLibrary = _MacOSXLibrary
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.String as _string
import java.lang.Integer as _int
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MacOSXLibrary():
    """org.lwjgl.system.macosx.MacOSXLibrary"""
 
    @staticmethod
    def _wrap(java_value: _MacOSXLibrary) -> 'MacOSXLibrary':
        return MacOSXLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MacOSXLibrary):
        """
        Dynamic initializer for MacOSXLibrary.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MacOSXLibrary__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MacOSXLibrary__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Default.getName()"""
        return str._wrap(super(pyglsystem.SharedLibrary$Default, self).getName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def getWithIdentifier(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.getWithIdentifier(java.lang.String)"""
        return MacOSXLibrary._wrap(_MacOSXLibrary.getWithIdentifier(arg0))

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
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int._wrap(super(_pyglsystem.FunctionProvider, self).getFunctionAddress(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.create(java.lang.String)"""
        return MacOSXLibrary._wrap(_MacOSXLibrary.create(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @abstractmethod
    def getPath(self, ):
        """public abstract java.lang.String org.lwjgl.system.SharedLibrary.getPath()"""
        pass

    @abstractmethod
    def free(self, ):
        """public abstract void org.lwjgl.system.NativeResource.free()"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass 
 
 
# CLASS: org.lwjgl.system.macosx.CoreGraphics
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.nio.IntBuffer as IntBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.nio.ShortBuffer as ShortBuffer
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Boolean as _boolean
import org.lwjgl.system.macosx.CGPoint as _CGPoint
_CGPoint = _CGPoint
import java.lang.Integer as _int
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
import org.lwjgl.system.macosx.CoreGraphics as _CoreGraphics
_CoreGraphics = _CoreGraphics
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CoreGraphics():
    """org.lwjgl.system.macosx.CoreGraphics"""
 
    @staticmethod
    def _wrap(java_value: _CoreGraphics) -> 'CoreGraphics':
        return CoreGraphics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CoreGraphics):
        """
        Dynamic initializer for CoreGraphics.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CoreGraphics__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CoreGraphics__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def CGEventCreateMouseEvent(arg0: int, arg1: int, arg2: 'CGPoint', arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateMouseEvent(long,int,org.lwjgl.system.macosx.CGPoint,int)"""
        return int._wrap(_CoreGraphics.CGEventCreateMouseEvent(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def CGEventKeyboardSetUnicodeString(arg0: int, arg1: 'ShortBuffer'):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventKeyboardSetUnicodeString(long,java.nio.ShortBuffer)"""
        _CoreGraphics.CGEventKeyboardSetUnicodeString(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nCGEventKeyboardGetUnicodeString(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.nCGEventKeyboardGetUnicodeString(long,long,long,long)"""
        _CoreGraphics.nCGEventKeyboardGetUnicodeString(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nCGEventCreateMouseEvent(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.nCGEventCreateMouseEvent(long,int,long,int)"""
        return int._wrap(_CoreGraphics.nCGEventCreateMouseEvent(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def CGEventSetType(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetType(long,int)"""
        _CoreGraphics.CGEventSetType(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nCGEventSetLocation(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.nCGEventSetLocation(long,long)"""
        _CoreGraphics.nCGEventSetLocation(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def CGEventSetTimestamp(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetTimestamp(long,long)"""
        _CoreGraphics.CGEventSetTimestamp(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def CGEventGetUnflippedLocation(arg0: int, arg1: 'CGPoint') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CoreGraphics.CGEventGetUnflippedLocation(long,org.lwjgl.system.macosx.CGPoint)"""
        return CGPoint._wrap(_CoreGraphics.CGEventGetUnflippedLocation(_long.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nCGGetEventTapList(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.macosx.CoreGraphics.nCGGetEventTapList(int,long,long)"""
        return int._wrap(_CoreGraphics.nCGGetEventTapList(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def CGEventTapCreateForPid(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'CGEventTapCallBackI', arg5: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventTapCreateForPid(long,int,int,long,org.lwjgl.system.macosx.CGEventTapCallBackI,long)"""
        return int._wrap(_CoreGraphics.CGEventTapCreateForPid(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def CGEventCreateData(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateData(long,long)"""
        return int._wrap(_CoreGraphics.CGEventCreateData(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def CGEventSetSource(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetSource(long,long)"""
        _CoreGraphics.CGEventSetSource(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def CGEventGetLocation(arg0: int, arg1: 'CGPoint') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CoreGraphics.CGEventGetLocation(long,org.lwjgl.system.macosx.CGPoint)"""
        return CGPoint._wrap(_CoreGraphics.CGEventGetLocation(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def CGEventPostToPid(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventPostToPid(long,long)"""
        _CoreGraphics.CGEventPostToPid(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def CGEventKeyboardSetUnicodeString(arg0: int, arg1: 'short'):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventKeyboardSetUnicodeString(long,short[])"""
        _CoreGraphics.CGEventKeyboardSetUnicodeString(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def CGEventSetIntegerValueField(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetIntegerValueField(long,int,long)"""
        _CoreGraphics.CGEventSetIntegerValueField(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def CGEventGetDoubleValueField(arg0: int, arg1: int) -> float:
        """public static double org.lwjgl.system.macosx.CoreGraphics.CGEventGetDoubleValueField(long,int)"""
        return float._wrap(_CoreGraphics.CGEventGetDoubleValueField(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def CGEventCreateCopy(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateCopy(long)"""
        return int._wrap(_CoreGraphics.CGEventCreateCopy(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def CGEventCreateFromData(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateFromData(long,long)"""
        return int._wrap(_CoreGraphics.CGEventCreateFromData(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def CGEventCreateScrollWheelEvent2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateScrollWheelEvent2(long,int,int,int,int,int)"""
        return int._wrap(_CoreGraphics.CGEventCreateScrollWheelEvent2(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @staticmethod
    @overload
    def CGEventGetTimestamp(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventGetTimestamp(long)"""
        return int._wrap(_CoreGraphics.CGEventGetTimestamp(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def CGEventPost(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventPost(int,long)"""
        _CoreGraphics.CGEventPost(_int.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def CGEventGetTypeID() -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventGetTypeID()"""
        return int._wrap(_CoreGraphics.CGEventGetTypeID())

    @staticmethod
    @overload
    def CGEventSetDoubleValueField(arg0: int, arg1: int, arg2: float):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetDoubleValueField(long,int,double)"""
        _CoreGraphics.CGEventSetDoubleValueField(_long.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2))

    @staticmethod
    @overload
    def nCGEventGetUnflippedLocation(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.macosx.CoreGraphics.nCGEventGetUnflippedLocation(long,long,long)"""
        _CoreGraphics.nCGEventGetUnflippedLocation(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def CGEventTapPostEvent(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventTapPostEvent(long,long)"""
        _CoreGraphics.CGEventTapPostEvent(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def CGEventCreateKeyboardEvent(arg0: int, arg1: int, arg2: bool) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateKeyboardEvent(long,short,boolean)"""
        return int._wrap(_CoreGraphics.CGEventCreateKeyboardEvent(_long.valueOf(arg0), _short.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def CGEventCreateScrollWheelEvent(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateScrollWheelEvent(long,int,int)"""
        return int._wrap(_CoreGraphics.CGEventCreateScrollWheelEvent(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def CGEventKeyboardGetUnicodeString(arg0: int, arg1: 'CLongBuffer', arg2: 'short'):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventKeyboardGetUnicodeString(long,org.lwjgl.CLongBuffer,short[])"""
        _CoreGraphics.CGEventKeyboardGetUnicodeString(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def nCGEventKeyboardSetUnicodeString(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.nCGEventKeyboardSetUnicodeString(long,long,long)"""
        _CoreGraphics.nCGEventKeyboardSetUnicodeString(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def nCGEventGetUnflippedLocation(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.nCGEventGetUnflippedLocation(long,long)"""
        _CoreGraphics.nCGEventGetUnflippedLocation(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nCGEventTapCreate(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.nCGEventTapCreate(int,int,int,long,long,long)"""
        return int._wrap(_CoreGraphics.nCGEventTapCreate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def nCGEventGetLocation(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.nCGEventGetLocation(long,long)"""
        _CoreGraphics.nCGEventGetLocation(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def CGEventSetFlags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetFlags(long,long)"""
        _CoreGraphics.CGEventSetFlags(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nCGEventTapCreateForPid(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.nCGEventTapCreateForPid(long,int,int,long,long,long)"""
        return int._wrap(_CoreGraphics.nCGEventTapCreateForPid(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def CGEventTapIsEnabled(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.CoreGraphics.CGEventTapIsEnabled(long)"""
        return bool._wrap(_CoreGraphics.CGEventTapIsEnabled(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def CGEventTapEnable(arg0: int, arg1: bool):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventTapEnable(long,boolean)"""
        _CoreGraphics.CGEventTapEnable(_long.valueOf(arg0), _boolean.valueOf(arg1))

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.macosx.CoreGraphics.getLibrary()"""
        return pyglsystem.SharedLibrary._wrap(_CoreGraphics.getLibrary())

    @staticmethod
    @overload
    def CGEventSetLocation(arg0: int, arg1: 'CGPoint'):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetLocation(long,org.lwjgl.system.macosx.CGPoint)"""
        _CoreGraphics.CGEventSetLocation(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def CGGetEventTapList(arg0: 'Buffer', arg1: 'IntBuffer') -> int:
        """public static int org.lwjgl.system.macosx.CoreGraphics.CGGetEventTapList(org.lwjgl.system.macosx.CGEventTapInformation$Buffer,java.nio.IntBuffer)"""
        return int._wrap(_CoreGraphics.CGGetEventTapList(arg0, arg1))

    @staticmethod
    @overload
    def CGEventKeyboardGetUnicodeString(arg0: int, arg1: 'CLongBuffer', arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventKeyboardGetUnicodeString(long,org.lwjgl.CLongBuffer,java.nio.ShortBuffer)"""
        _CoreGraphics.CGEventKeyboardGetUnicodeString(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def CGEventCreate(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreate(long)"""
        return int._wrap(_CoreGraphics.CGEventCreate(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def CGEventCreateScrollWheelEvent(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateScrollWheelEvent(long,int,int,int)"""
        return int._wrap(_CoreGraphics.CGEventCreateScrollWheelEvent(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def CGEventCreateSourceFromEvent(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateSourceFromEvent(long)"""
        return int._wrap(_CoreGraphics.CGEventCreateSourceFromEvent(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def CGEventGetFlags(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventGetFlags(long)"""
        return int._wrap(_CoreGraphics.CGEventGetFlags(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nCGEventCreateMouseEvent(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreGraphics.nCGEventCreateMouseEvent(long,int,long,int,long)"""
        return int._wrap(_CoreGraphics.nCGEventCreateMouseEvent(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def CGEventGetType(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.CoreGraphics.CGEventGetType(long)"""
        return int._wrap(_CoreGraphics.CGEventGetType(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def CGEventTapCreate(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'CGEventTapCallBackI', arg5: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventTapCreate(int,int,int,long,org.lwjgl.system.macosx.CGEventTapCallBackI,long)"""
        return int._wrap(_CoreGraphics.CGEventTapCreate(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def CGEventGetIntegerValueField(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventGetIntegerValueField(long,int)"""
        return int._wrap(_CoreGraphics.CGEventGetIntegerValueField(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nCGEventGetLocation(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.macosx.CoreGraphics.nCGEventGetLocation(long,long,long)"""
        _CoreGraphics.nCGEventGetLocation(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def CGGetEventTapList(arg0: 'Buffer', arg1: 'int') -> int:
        """public static int org.lwjgl.system.macosx.CoreGraphics.CGGetEventTapList(org.lwjgl.system.macosx.CGEventTapInformation$Buffer,int[])"""
        return int._wrap(_CoreGraphics.CGGetEventTapList(arg0, arg1))

    @staticmethod
    @overload
    def nCGEventSetLocation(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.macosx.CoreGraphics.nCGEventSetLocation(long,long,long)"""
        _CoreGraphics.nCGEventSetLocation(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass()) 
 
 
# CLASS: org.lwjgl.system.macosx.ObjCPropertyAttribute
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.system.macosx.ObjCPropertyAttribute as _ObjCPropertyAttribute
_ObjCPropertyAttribute = _ObjCPropertyAttribute
import java.lang.Integer as _int
import org.lwjgl.system.macosx.ObjCPropertyAttribute as _ObjCPropertyAttribute_Buffer
_Buffer = _ObjCPropertyAttribute_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjCPropertyAttribute():
    """org.lwjgl.system.macosx.ObjCPropertyAttribute"""
 
    @staticmethod
    def _wrap(java_value: _ObjCPropertyAttribute) -> 'ObjCPropertyAttribute':
        return ObjCPropertyAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjCPropertyAttribute):
        """
        Dynamic initializer for ObjCPropertyAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjCPropertyAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjCPropertyAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.malloc(int)"""
        return Buffer._wrap(_ObjCPropertyAttribute.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nnameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute.nnameString(long)"""
        return str._wrap(_ObjCPropertyAttribute.nnameString(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.createSafe(long,int)"""
        return Buffer._wrap(_ObjCPropertyAttribute.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def set(self, arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> 'ObjCPropertyAttribute':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.set(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return 'ObjCPropertyAttribute'._wrap(super(_ObjCPropertyAttribute, self).set(arg0, arg1))

    @overload
    def nameString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute.nameString()"""
        return str._wrap(super(ObjCPropertyAttribute, self).nameString())

    @overload
    def name(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute.name()"""
        return 'ByteBuffer'._wrap(super(ObjCPropertyAttribute, self).name())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.callocStack(org.lwjgl.system.MemoryStack)"""
        return ObjCPropertyAttribute._wrap(_ObjCPropertyAttribute.callocStack(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nvalue(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute.nvalue(long)"""
        return ByteBuffer._wrap(_ObjCPropertyAttribute.nvalue(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.create(long,int)"""
        return Buffer._wrap(_ObjCPropertyAttribute.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def name(self, arg0: 'ByteBuffer') -> 'ObjCPropertyAttribute':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.name(java.nio.ByteBuffer)"""
        return 'ObjCPropertyAttribute'._wrap(super(_ObjCPropertyAttribute, self).name(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def nname(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute.nname(long)"""
        return ByteBuffer._wrap(_ObjCPropertyAttribute.nname(_long.valueOf(arg0)))

    @overload
    def valueString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute.valueString()"""
        return str._wrap(super(ObjCPropertyAttribute, self).valueString())

    @staticmethod
    @overload
    def nvalue(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCPropertyAttribute.nvalue(long,java.nio.ByteBuffer)"""
        _ObjCPropertyAttribute.nvalue(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.calloc(int)"""
        return Buffer._wrap(_ObjCPropertyAttribute.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.createSafe(long)"""
        return ObjCPropertyAttribute._wrap(_ObjCPropertyAttribute.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.macosx.ObjCPropertyAttribute.sizeof()"""
        return int._wrap(super(ObjCPropertyAttribute, self).sizeof())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def mallocStack() -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.mallocStack()"""
        return ObjCPropertyAttribute._wrap(_ObjCPropertyAttribute.mallocStack())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.create(int)"""
        return Buffer._wrap(_ObjCPropertyAttribute.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.calloc()"""
        return ObjCPropertyAttribute._wrap(_ObjCPropertyAttribute.calloc())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.mallocStack(org.lwjgl.system.MemoryStack)"""
        return ObjCPropertyAttribute._wrap(_ObjCPropertyAttribute.mallocStack(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.callocStack(int)"""
        return Buffer._wrap(_ObjCPropertyAttribute.callocStack(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.malloc(org.lwjgl.system.MemoryStack)"""
        return ObjCPropertyAttribute._wrap(_ObjCPropertyAttribute.malloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.calloc(org.lwjgl.system.MemoryStack)"""
        return ObjCPropertyAttribute._wrap(_ObjCPropertyAttribute.calloc(arg0))

    @staticmethod
    @overload
    def nvalueString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute.nvalueString(long)"""
        return str._wrap(_ObjCPropertyAttribute.nvalueString(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_ObjCPropertyAttribute.calloc(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def create() -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.create()"""
        return ObjCPropertyAttribute._wrap(_ObjCPropertyAttribute.create())

    @overload
    def value(self, arg0: 'ByteBuffer') -> 'ObjCPropertyAttribute':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.value(java.nio.ByteBuffer)"""
        return 'ObjCPropertyAttribute'._wrap(super(_ObjCPropertyAttribute, self).value(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.mallocStack(int)"""
        return Buffer._wrap(_ObjCPropertyAttribute.mallocStack(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'ObjCPropertyAttribute') -> 'ObjCPropertyAttribute':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.set(org.lwjgl.system.macosx.ObjCPropertyAttribute)"""
        return 'ObjCPropertyAttribute'._wrap(super(_ObjCPropertyAttribute, self).set(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_ObjCPropertyAttribute.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nname(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCPropertyAttribute.nname(long,java.nio.ByteBuffer)"""
        _ObjCPropertyAttribute.nname(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def create(arg0: int) -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.create(long)"""
        return ObjCPropertyAttribute._wrap(_ObjCPropertyAttribute.create(_long.valueOf(arg0)))

    @overload
    def value(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute.value()"""
        return 'ByteBuffer'._wrap(super(ObjCPropertyAttribute, self).value())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute(java.nio.ByteBuffer)"""
        val = _ObjCPropertyAttribute(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def malloc() -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.malloc()"""
        return ObjCPropertyAttribute._wrap(_ObjCPropertyAttribute.malloc())

    @staticmethod
    @overload
    def callocStack() -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.callocStack()"""
        return ObjCPropertyAttribute._wrap(_ObjCPropertyAttribute.callocStack())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCPropertyAttribute.validate(long)"""
        _ObjCPropertyAttribute.validate(_long.valueOf(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_ObjCPropertyAttribute.mallocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_ObjCPropertyAttribute.malloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.macosx.MacOSXLibraryBundle
import org.lwjgl.system.SharedLibrary as _SharedLibrary_Default
_Default = _SharedLibrary_Default.Default
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.lwjgl.system.FunctionProvider as _FunctionProvider
_FunctionProvider = _FunctionProvider
import org.lwjgl.system.macosx.MacOSXLibrary as _MacOSXLibrary
_MacOSXLibrary = _MacOSXLibrary
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
import org.lwjgl.system.macosx.MacOSXLibraryBundle as _MacOSXLibraryBundle
_MacOSXLibraryBundle = _MacOSXLibraryBundle
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MacOSXLibraryBundle():
    """org.lwjgl.system.macosx.MacOSXLibraryBundle"""
 
    @staticmethod
    def _wrap(java_value: _MacOSXLibraryBundle) -> 'MacOSXLibraryBundle':
        return MacOSXLibraryBundle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MacOSXLibraryBundle):
        """
        Dynamic initializer for MacOSXLibraryBundle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MacOSXLibraryBundle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MacOSXLibraryBundle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPath(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.MacOSXLibraryBundle.getPath()"""
        return str._wrap(super(MacOSXLibraryBundle, self).getPath())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Default.getName()"""
        return str._wrap(super(pyglsystem.SharedLibrary$Default, self).getName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.macosx.MacOSXLibraryBundle.free()"""
        super(MacOSXLibraryBundle, self).free()

    @overload
    def getFunctionAddress(self, arg0: 'ByteBuffer') -> int:
        """public long org.lwjgl.system.macosx.MacOSXLibraryBundle.getFunctionAddress(java.nio.ByteBuffer)"""
        return int._wrap(super(_MacOSXLibraryBundle, self).getFunctionAddress(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: str) -> 'MacOSXLibraryBundle':
        """public static org.lwjgl.system.macosx.MacOSXLibraryBundle org.lwjgl.system.macosx.MacOSXLibraryBundle.create(java.lang.String)"""
        return MacOSXLibraryBundle._wrap(_MacOSXLibraryBundle.create(arg0))

    @staticmethod
    @overload
    def getWithIdentifier(arg0: str) -> 'MacOSXLibraryBundle':
        """public static org.lwjgl.system.macosx.MacOSXLibraryBundle org.lwjgl.system.macosx.MacOSXLibraryBundle.getWithIdentifier(java.lang.String)"""
        return MacOSXLibraryBundle._wrap(_MacOSXLibraryBundle.getWithIdentifier(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def getWithIdentifier(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.getWithIdentifier(java.lang.String)"""
        return MacOSXLibrary._wrap(_MacOSXLibrary.getWithIdentifier(arg0))

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
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int._wrap(super(_pyglsystem.FunctionProvider, self).getFunctionAddress(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.create(java.lang.String)"""
        return MacOSXLibrary._wrap(_MacOSXLibrary.create(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public org.lwjgl.system.macosx.MacOSXLibraryBundle(java.lang.String,long)"""
        val = _MacOSXLibraryBundle(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address()) 
 
 
# CLASS: org.lwjgl.system.macosx.CGEventTapCallBackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.system.macosx.CGEventTapCallBackI as _CGEventTapCallBackI
_CGEventTapCallBackI = _CGEventTapCallBackI
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class CGEventTapCallBackI():
    """org.lwjgl.system.macosx.CGEventTapCallBackI"""
 
    @staticmethod
    def _wrap(java_value: _CGEventTapCallBackI) -> 'CGEventTapCallBackI':
        return CGEventTapCallBackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CGEventTapCallBackI):
        """
        Dynamic initializer for CGEventTapCallBackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CGEventTapCallBackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CGEventTapCallBackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.macosx.CGEventTapCallBackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(CGEventTapCallBackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract long org.lwjgl.system.macosx.CGEventTapCallBackI.invoke(long,int,long,long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.macosx.CGEventTapCallBackI.callback(long,long)"""
        super(_CGEventTapCallBackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.system.macosx.ObjCRuntime$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.macosx.ObjCRuntime as _ObjCRuntime_Functions
_Functions = _ObjCRuntime_Functions.Functions
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.system.macosx.ObjCRuntime.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
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
 
 
# CLASS: org.lwjgl.system.macosx.EnumerationMutationHandler
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.lwjgl.system.macosx.EnumerationMutationHandlerI as _EnumerationMutationHandlerI
_EnumerationMutationHandlerI = _EnumerationMutationHandlerI
import org.lwjgl.system.macosx.EnumerationMutationHandler as _EnumerationMutationHandler
_EnumerationMutationHandler = _EnumerationMutationHandler
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EnumerationMutationHandler():
    """org.lwjgl.system.macosx.EnumerationMutationHandler"""
 
    @staticmethod
    def _wrap(java_value: _EnumerationMutationHandler) -> 'EnumerationMutationHandler':
        return EnumerationMutationHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EnumerationMutationHandler):
        """
        Dynamic initializer for EnumerationMutationHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EnumerationMutationHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EnumerationMutationHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'EnumerationMutationHandler':
        """public static org.lwjgl.system.macosx.EnumerationMutationHandler org.lwjgl.system.macosx.EnumerationMutationHandler.create(long)"""
        return EnumerationMutationHandler._wrap(_EnumerationMutationHandler.create(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'EnumerationMutationHandlerI') -> 'EnumerationMutationHandler':
        """public static org.lwjgl.system.macosx.EnumerationMutationHandler org.lwjgl.system.macosx.EnumerationMutationHandler.create(org.lwjgl.system.macosx.EnumerationMutationHandlerI)"""
        return EnumerationMutationHandler._wrap(_EnumerationMutationHandler.create(arg0))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(pyglsystem.Callback, self).free()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.macosx.EnumerationMutationHandlerI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(EnumerationMutationHandlerI, self).getCallInterface())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'EnumerationMutationHandler':
        """public static org.lwjgl.system.macosx.EnumerationMutationHandler org.lwjgl.system.macosx.EnumerationMutationHandler.createSafe(long)"""
        return EnumerationMutationHandler._wrap(_EnumerationMutationHandler.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.macosx.EnumerationMutationHandlerI.callback(long,long)"""
        super(_EnumerationMutationHandlerI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.system.macosx.EnumerationMutationHandlerI.invoke(long)"""
        pass 
 
 
# CLASS: org.lwjgl.system.macosx.CoreGraphics$Functions
import org.lwjgl.system.macosx.CoreGraphics as _CoreGraphics_Functions
_Functions = _CoreGraphics_Functions.Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.system.macosx.CoreGraphics.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
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
 
 
# CLASS: org.lwjgl.system.macosx.CoreFoundation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.lwjgl.system.macosx.CoreFoundation as _CoreFoundation
_CoreFoundation = _CoreFoundation
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CoreFoundation():
    """org.lwjgl.system.macosx.CoreFoundation"""
 
    @staticmethod
    def _wrap(java_value: _CoreFoundation) -> 'CoreFoundation':
        return CoreFoundation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CoreFoundation):
        """
        Dynamic initializer for CoreFoundation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CoreFoundation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CoreFoundation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def CFBundleGetBundleWithIdentifier(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFBundleGetBundleWithIdentifier(long)"""
        return int._wrap(_CoreFoundation.CFBundleGetBundleWithIdentifier(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nCFBundleGetBundleWithIdentifier(arg0: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFBundleGetBundleWithIdentifier(long)"""
        return int._wrap(_CoreFoundation.nCFBundleGetBundleWithIdentifier(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nCFRetain(arg0: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFRetain(long)"""
        return int._wrap(_CoreFoundation.nCFRetain(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def CFRetain(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFRetain(long)"""
        return int._wrap(_CoreFoundation.CFRetain(_long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nCFStringCreateWithCStringNoCopy(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFStringCreateWithCStringNoCopy(long,long,int,long)"""
        return int._wrap(_CoreFoundation.nCFStringCreateWithCStringNoCopy(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def nCFURLCreateWithFileSystemPath(arg0: int, arg1: int, arg2: int, arg3: bool) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFURLCreateWithFileSystemPath(long,long,long,boolean)"""
        return int._wrap(_CoreFoundation.nCFURLCreateWithFileSystemPath(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def CFBundleGetFunctionPointerForName(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFBundleGetFunctionPointerForName(long,long)"""
        return int._wrap(_CoreFoundation.CFBundleGetFunctionPointerForName(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def CFRelease(arg0: int):
        """public static void org.lwjgl.system.macosx.CoreFoundation.CFRelease(long)"""
        _CoreFoundation.CFRelease(_long.valueOf(arg0))

    @staticmethod
    @overload
    def CFStringCreateWithCString(arg0: int, arg1: 'ByteBuffer', arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFStringCreateWithCString(long,java.nio.ByteBuffer,int)"""
        return int._wrap(_CoreFoundation.CFStringCreateWithCString(_long.valueOf(arg0), arg1, _int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def CFStringCreateWithCStringNoCopy(arg0: int, arg1: 'ByteBuffer', arg2: int, arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFStringCreateWithCStringNoCopy(long,java.nio.ByteBuffer,int,long)"""
        return int._wrap(_CoreFoundation.CFStringCreateWithCStringNoCopy(_long.valueOf(arg0), arg1, _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def CFBundleCreate(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFBundleCreate(long,long)"""
        return int._wrap(_CoreFoundation.CFBundleCreate(_long.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nCFRelease(arg0: int):
        """public static native void org.lwjgl.system.macosx.CoreFoundation.nCFRelease(long)"""
        _CoreFoundation.nCFRelease(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nCFBundleCreate(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFBundleCreate(long,long)"""
        return int._wrap(_CoreFoundation.nCFBundleCreate(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nCFStringCreateWithCString(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFStringCreateWithCString(long,long,int)"""
        return int._wrap(_CoreFoundation.nCFStringCreateWithCString(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

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
    def CFURLCreateWithFileSystemPath(arg0: int, arg1: int, arg2: int, arg3: bool) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFURLCreateWithFileSystemPath(long,long,long,boolean)"""
        return int._wrap(_CoreFoundation.CFURLCreateWithFileSystemPath(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def nCFBundleGetFunctionPointerForName(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFBundleGetFunctionPointerForName(long,long)"""
        return int._wrap(_CoreFoundation.nCFBundleGetFunctionPointerForName(_long.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.macosx.CGEventTapInformation$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import org.lwjgl.system.macosx.CGEventTapInformation as _CGEventTapInformation_Buffer
_Buffer = _CGEventTapInformation_Buffer.Buffer
from builtins import float
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.macosx.CGEventTapInformation.Buffer"""
 
    @staticmethod
    def _wrap(java_value: _Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Buffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Buffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def minUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation$Buffer.minUsecLatency()"""
        return float._wrap(super(Buffer, self).minUsecLatency())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).limit(_int.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.CGEventTapInformation$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def processBeingTapped(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation$Buffer.processBeingTapped()"""
        return int._wrap(super(Buffer, self).processBeingTapped())

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def options(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation$Buffer.options()"""
        return int._wrap(super(Buffer, self).options())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @overload
    def avgUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation$Buffer.avgUsecLatency()"""
        return float._wrap(super(Buffer, self).avgUsecLatency())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).stream())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @overload
    def tappingProcess(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation$Buffer.tappingProcess()"""
        return int._wrap(super(Buffer, self).tappingProcess())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def eventTapID(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation$Buffer.eventTapID()"""
        return int._wrap(super(Buffer, self).eventTapID())

    @overload
    def maxUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation$Buffer.maxUsecLatency()"""
        return float._wrap(super(Buffer, self).maxUsecLatency())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def eventsOfInterest(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation$Buffer.eventsOfInterest()"""
        return int._wrap(super(Buffer, self).eventsOfInterest())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def tapPoint(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation$Buffer.tapPoint()"""
        return int._wrap(super(Buffer, self).tapPoint())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).clear())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def enabled(self) -> bool:
        """public boolean org.lwjgl.system.macosx.CGEventTapInformation$Buffer.enabled()"""
        return bool._wrap(super(Buffer, self).enabled())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int._wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.macosx.CGEventTapInformation$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.macosx.ObjCMethodDescription
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.macosx.ObjCMethodDescription as _ObjCMethodDescription
_ObjCMethodDescription = _ObjCMethodDescription
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.macosx.ObjCMethodDescription as _ObjCMethodDescription_Buffer
_Buffer = _ObjCMethodDescription_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjCMethodDescription():
    """org.lwjgl.system.macosx.ObjCMethodDescription"""
 
    @staticmethod
    def _wrap(java_value: _ObjCMethodDescription) -> 'ObjCMethodDescription':
        return ObjCMethodDescription(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjCMethodDescription):
        """
        Dynamic initializer for ObjCMethodDescription.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjCMethodDescription__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjCMethodDescription__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.create(long,int)"""
        return Buffer._wrap(_ObjCMethodDescription.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.createSafe(long,int)"""
        return Buffer._wrap(_ObjCMethodDescription.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.callocStack(int)"""
        return Buffer._wrap(_ObjCMethodDescription.callocStack(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def callocStack() -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.callocStack()"""
        return ObjCMethodDescription._wrap(_ObjCMethodDescription.callocStack())

    @staticmethod
    @overload
    def create(arg0: int) -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.create(long)"""
        return ObjCMethodDescription._wrap(_ObjCMethodDescription.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntypesString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCMethodDescription.ntypesString(long)"""
        return str._wrap(_ObjCMethodDescription.ntypesString(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.createSafe(long)"""
        return ObjCMethodDescription._wrap(_ObjCMethodDescription.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.create(int)"""
        return Buffer._wrap(_ObjCMethodDescription.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.mallocStack(org.lwjgl.system.MemoryStack)"""
        return ObjCMethodDescription._wrap(_ObjCMethodDescription.mallocStack(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.calloc(org.lwjgl.system.MemoryStack)"""
        return ObjCMethodDescription._wrap(_ObjCMethodDescription.calloc(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_ObjCMethodDescription.malloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.macosx.ObjCMethodDescription.sizeof()"""
        return int._wrap(super(ObjCMethodDescription, self).sizeof())

    @overload
    def types(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCMethodDescription.types()"""
        return 'ByteBuffer'._wrap(super(ObjCMethodDescription, self).types())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.calloc(int)"""
        return Buffer._wrap(_ObjCMethodDescription.calloc(_int.valueOf(arg0)))

    @overload
    def name(self) -> int:
        """public long org.lwjgl.system.macosx.ObjCMethodDescription.name()"""
        return int._wrap(super(ObjCMethodDescription, self).name())

    @staticmethod
    @overload
    def create() -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.create()"""
        return ObjCMethodDescription._wrap(_ObjCMethodDescription.create())

    @staticmethod
    @overload
    def ntypes(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCMethodDescription.ntypes(long)"""
        return ByteBuffer._wrap(_ObjCMethodDescription.ntypes(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.malloc(int)"""
        return Buffer._wrap(_ObjCMethodDescription.malloc(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack() -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.mallocStack()"""
        return ObjCMethodDescription._wrap(_ObjCMethodDescription.mallocStack())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_ObjCMethodDescription.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_ObjCMethodDescription.callocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def calloc() -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.calloc()"""
        return ObjCMethodDescription._wrap(_ObjCMethodDescription.calloc())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.mallocStack(int)"""
        return Buffer._wrap(_ObjCMethodDescription.mallocStack(_int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.callocStack(org.lwjgl.system.MemoryStack)"""
        return ObjCMethodDescription._wrap(_ObjCMethodDescription.callocStack(arg0))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_ObjCMethodDescription.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.malloc(org.lwjgl.system.MemoryStack)"""
        return ObjCMethodDescription._wrap(_ObjCMethodDescription.malloc(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.ObjCMethodDescription(java.nio.ByteBuffer)"""
        val = _ObjCMethodDescription(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def nname(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCMethodDescription.nname(long)"""
        return int._wrap(_ObjCMethodDescription.nname(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.malloc()"""
        return ObjCMethodDescription._wrap(_ObjCMethodDescription.malloc())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def typesString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCMethodDescription.typesString()"""
        return str._wrap(super(ObjCMethodDescription, self).typesString())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address()) 
 
 
# CLASS: org.lwjgl.system.macosx.MacOSXLibraryDL
import org.lwjgl.system.SharedLibrary as _SharedLibrary_Default
_Default = _SharedLibrary_Default.Default
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.lwjgl.system.FunctionProvider as _FunctionProvider
_FunctionProvider = _FunctionProvider
import org.lwjgl.system.macosx.MacOSXLibrary as _MacOSXLibrary
_MacOSXLibrary = _MacOSXLibrary
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.lang.String as _String
_String = _String
import org.lwjgl.system.macosx.MacOSXLibraryDL as _MacOSXLibraryDL
_MacOSXLibraryDL = _MacOSXLibraryDL
import java.lang.String as _string
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MacOSXLibraryDL():
    """org.lwjgl.system.macosx.MacOSXLibraryDL"""
 
    @staticmethod
    def _wrap(java_value: _MacOSXLibraryDL) -> 'MacOSXLibraryDL':
        return MacOSXLibraryDL(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MacOSXLibraryDL):
        """
        Dynamic initializer for MacOSXLibraryDL.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MacOSXLibraryDL__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MacOSXLibraryDL__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getFunctionAddress(self, arg0: 'ByteBuffer') -> int:
        """public long org.lwjgl.system.macosx.MacOSXLibraryDL.getFunctionAddress(java.nio.ByteBuffer)"""
        return int._wrap(super(_MacOSXLibraryDL, self).getFunctionAddress(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Default.getName()"""
        return str._wrap(super(pyglsystem.SharedLibrary$Default, self).getName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def getWithIdentifier(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.getWithIdentifier(java.lang.String)"""
        return MacOSXLibrary._wrap(_MacOSXLibrary.getWithIdentifier(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.macosx.MacOSXLibraryDL.free()"""
        super(MacOSXLibraryDL, self).free()

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
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int._wrap(super(_pyglsystem.FunctionProvider, self).getFunctionAddress(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public org.lwjgl.system.macosx.MacOSXLibraryDL(java.lang.String,long)"""
        val = _MacOSXLibraryDL(arg0, _long.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.create(java.lang.String)"""
        return MacOSXLibrary._wrap(_MacOSXLibrary.create(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public org.lwjgl.system.macosx.MacOSXLibraryDL(java.lang.String)"""
        val = _MacOSXLibraryDL(arg0)
        self.__wrapper = val

    @override
    @overload
    def getPath(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.MacOSXLibraryDL.getPath()"""
        return str._wrap(super(MacOSXLibraryDL, self).getPath())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address()) 
 
 
# CLASS: org.lwjgl.system.macosx.LibC$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.macosx.LibC as _LibC_Functions
_Functions = _LibC_Functions.Functions
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.system.macosx.LibC.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
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
 
 
# CLASS: org.lwjgl.system.macosx.ObjCMethodDescription$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import org.lwjgl.system.macosx.ObjCMethodDescription as _ObjCMethodDescription_Buffer
_Buffer = _ObjCMethodDescription_Buffer.Buffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.macosx.ObjCMethodDescription.Buffer"""
 
    @staticmethod
    def _wrap(java_value: _Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Buffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Buffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def typesString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCMethodDescription$Buffer.typesString()"""
        return str._wrap(super(Buffer, self).typesString())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.macosx.ObjCMethodDescription$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).limit(_int.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).stream())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.ObjCMethodDescription$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def name(self) -> int:
        """public long org.lwjgl.system.macosx.ObjCMethodDescription$Buffer.name()"""
        return int._wrap(super(Buffer, self).name())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).clear())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int._wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def types(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCMethodDescription$Buffer.types()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).types())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.macosx.LibSystem
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.macosx.LibSystem as _LibSystem
_LibSystem = _LibSystem
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibSystem():
    """org.lwjgl.system.macosx.LibSystem"""
 
    @staticmethod
    def _wrap(java_value: _LibSystem) -> 'LibSystem':
        return LibSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibSystem):
        """
        Dynamic initializer for LibSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibSystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibSystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.macosx.LibSystem.getLibrary()"""
        return pyglsystem.SharedLibrary._wrap(_LibSystem.getLibrary())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.macosx.CGEventTapCallBack
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.system.macosx.CGEventTapCallBackI as _CGEventTapCallBackI
_CGEventTapCallBackI = _CGEventTapCallBackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.macosx.CGEventTapCallBack as _CGEventTapCallBack
_CGEventTapCallBack = _CGEventTapCallBack
import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CGEventTapCallBack():
    """org.lwjgl.system.macosx.CGEventTapCallBack"""
 
    @staticmethod
    def _wrap(java_value: _CGEventTapCallBack) -> 'CGEventTapCallBack':
        return CGEventTapCallBack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CGEventTapCallBack):
        """
        Dynamic initializer for CGEventTapCallBack.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CGEventTapCallBack__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CGEventTapCallBack__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.macosx.CGEventTapCallBackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(CGEventTapCallBackI, self).getCallInterface())

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract long org.lwjgl.system.macosx.CGEventTapCallBackI.invoke(long,int,long,long)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.macosx.CGEventTapCallBackI.callback(long,long)"""
        super(_CGEventTapCallBackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'CGEventTapCallBack':
        """public static org.lwjgl.system.macosx.CGEventTapCallBack org.lwjgl.system.macosx.CGEventTapCallBack.create(long)"""
        return CGEventTapCallBack._wrap(_CGEventTapCallBack.create(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(pyglsystem.Callback, self).free()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'CGEventTapCallBack':
        """public static org.lwjgl.system.macosx.CGEventTapCallBack org.lwjgl.system.macosx.CGEventTapCallBack.createSafe(long)"""
        return CGEventTapCallBack._wrap(_CGEventTapCallBack.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(arg0: 'CGEventTapCallBackI') -> 'CGEventTapCallBack':
        """public static org.lwjgl.system.macosx.CGEventTapCallBack org.lwjgl.system.macosx.CGEventTapCallBack.create(org.lwjgl.system.macosx.CGEventTapCallBackI)"""
        return CGEventTapCallBack._wrap(_CGEventTapCallBack.create(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.system.macosx.EnumerationMutationHandlerI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.macosx.EnumerationMutationHandlerI as _EnumerationMutationHandlerI
_EnumerationMutationHandlerI = _EnumerationMutationHandlerI
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class EnumerationMutationHandlerI():
    """org.lwjgl.system.macosx.EnumerationMutationHandlerI"""
 
    @staticmethod
    def _wrap(java_value: _EnumerationMutationHandlerI) -> 'EnumerationMutationHandlerI':
        return EnumerationMutationHandlerI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EnumerationMutationHandlerI):
        """
        Dynamic initializer for EnumerationMutationHandlerI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EnumerationMutationHandlerI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EnumerationMutationHandlerI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.macosx.EnumerationMutationHandlerI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(EnumerationMutationHandlerI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.macosx.EnumerationMutationHandlerI.callback(long,long)"""
        super(_EnumerationMutationHandlerI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.system.macosx.EnumerationMutationHandlerI.invoke(long)"""
        pass 
 
 
# CLASS: org.lwjgl.system.macosx.ObjCRuntime
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import org.lwjgl.system.macosx.ObjCRuntime as _ObjCRuntime
_ObjCRuntime = _ObjCRuntime
import java.lang.Object as _Object
_Object = _Object
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.lang.Object as _object
from builtins import type
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
import org.lwjgl.system.macosx.ObjCMethodDescription as _ObjCMethodDescription
_ObjCMethodDescription = _ObjCMethodDescription
import org.lwjgl.system.macosx.ObjCPropertyAttribute as _ObjCPropertyAttribute_Buffer
_Buffer = _ObjCPropertyAttribute_Buffer.Buffer
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.macosx.ObjCMethodDescription as _ObjCMethodDescription_Buffer
_Buffer = _ObjCMethodDescription_Buffer.Buffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjCRuntime():
    """org.lwjgl.system.macosx.ObjCRuntime"""
 
    @staticmethod
    def _wrap(java_value: _ObjCRuntime) -> 'ObjCRuntime':
        return ObjCRuntime(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjCRuntime):
        """
        Dynamic initializer for ObjCRuntime.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjCRuntime__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjCRuntime__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nobjc_loadWeak(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_loadWeak(long)"""
        return int._wrap(_ObjCRuntime.nobjc_loadWeak(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getInstanceVariable(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getInstanceVariable(long,java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.class_getInstanceVariable(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def objc_storeWeak(arg0: 'PointerBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_storeWeak(org.lwjgl.PointerBuffer,long)"""
        return int._wrap(_ObjCRuntime.objc_storeWeak(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def objc_getMetaClass(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getMetaClass(java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.objc_getMetaClass(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nmethod_copyReturnType(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nmethod_copyReturnType(long)"""
        return int._wrap(_ObjCRuntime.nmethod_copyReturnType(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getProperty(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getProperty(long,java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.class_getProperty(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def class_addProperty(arg0: int, arg1: 'CharSequence', arg2: 'Buffer') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addProperty(long,java.lang.CharSequence,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer)"""
        return bool._wrap(_ObjCRuntime.class_addProperty(_long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def protocol_copyMethodDescriptionList(arg0: int, arg1: bool, arg2: bool) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCRuntime.protocol_copyMethodDescriptionList(long,boolean,boolean)"""
        return Buffer._wrap(_ObjCRuntime.protocol_copyMethodDescriptionList(_long.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def nobjc_lookUpClass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_lookUpClass(long)"""
        return int._wrap(_ObjCRuntime.nobjc_lookUpClass(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobjc_copyClassNamesForImage(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_copyClassNamesForImage(long,long)"""
        return int._wrap(_ObjCRuntime.nobjc_copyClassNamesForImage(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_conformsToProtocol(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_conformsToProtocol(long,long)"""
        return bool._wrap(_ObjCRuntime.class_conformsToProtocol(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nclass_copyProtocolList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_copyProtocolList(long,long)"""
        return int._wrap(_ObjCRuntime.nclass_copyProtocolList(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nclass_addIvar(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.nclass_addIvar(long,long,long,byte,long)"""
        return bool._wrap(_ObjCRuntime.nclass_addIvar(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _byte.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def class_getWeakIvarLayout(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.class_getWeakIvarLayout(long)"""
        return str._wrap(_ObjCRuntime.class_getWeakIvarLayout(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsel_getUid(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nsel_getUid(long)"""
        return int._wrap(_ObjCRuntime.nsel_getUid(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def object_setInstanceVariable(arg0: int, arg1: 'CharSequence', arg2: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_setInstanceVariable(long,java.lang.CharSequence,java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.object_setInstanceVariable(_long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def property_copyAttributeList(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCRuntime.property_copyAttributeList(long)"""
        return Buffer._wrap(_ObjCRuntime.property_copyAttributeList(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_enumerationMutation(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_enumerationMutation(long)"""
        _ObjCRuntime.objc_enumerationMutation(_long.valueOf(arg0))

    @staticmethod
    @overload
    def class_getClassMethod(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getClassMethod(long,long)"""
        return int._wrap(_ObjCRuntime.class_getClassMethod(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nclass_copyPropertyList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_copyPropertyList(long,long)"""
        return int._wrap(_ObjCRuntime.nclass_copyPropertyList(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def method_exchangeImplementations(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.method_exchangeImplementations(long,long)"""
        _ObjCRuntime.method_exchangeImplementations(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nclass_replaceProperty(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nclass_replaceProperty(long,long,long,int)"""
        _ObjCRuntime.nclass_replaceProperty(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def protocol_addProtocol(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.protocol_addProtocol(long,long)"""
        _ObjCRuntime.protocol_addProtocol(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def objc_loadWeak(arg0: 'PointerBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_loadWeak(org.lwjgl.PointerBuffer)"""
        return int._wrap(_ObjCRuntime.objc_loadWeak(arg0))

    @staticmethod
    @overload
    def class_setIvarLayout(arg0: int, arg1: 'CharSequence'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_setIvarLayout(long,java.lang.CharSequence)"""
        _ObjCRuntime.class_setIvarLayout(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def objc_constructInstance(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_constructInstance(long,java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.objc_constructInstance(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def sel_getUid(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.sel_getUid(java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.sel_getUid(arg0))

    @staticmethod
    @overload
    def ivar_getName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.ivar_getName(long)"""
        return str._wrap(_ObjCRuntime.ivar_getName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_registerClassPair(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_registerClassPair(long)"""
        _ObjCRuntime.objc_registerClassPair(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def objc_allocateProtocol(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_allocateProtocol(java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.objc_allocateProtocol(arg0))

    @staticmethod
    @overload
    def object_setIvar(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.object_setIvar(long,long,long)"""
        _ObjCRuntime.object_setIvar(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def nobjc_allocateProtocol(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_allocateProtocol(long)"""
        return int._wrap(_ObjCRuntime.nobjc_allocateProtocol(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getProperty(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getProperty(long,java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.class_getProperty(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def class_getInstanceMethod(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getInstanceMethod(long,long)"""
        return int._wrap(_ObjCRuntime.class_getInstanceMethod(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_addProtocol(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addProtocol(long,long)"""
        return bool._wrap(_ObjCRuntime.class_addProtocol(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def objc_copyProtocolList() -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.objc_copyProtocolList()"""
        return pygl.PointerBuffer._wrap(_ObjCRuntime.objc_copyProtocolList())

    @staticmethod
    @overload
    def class_setIvarLayout(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_setIvarLayout(long,java.nio.ByteBuffer)"""
        _ObjCRuntime.class_setIvarLayout(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def sel_getUid(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.sel_getUid(java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.sel_getUid(arg0))

    @staticmethod
    @overload
    def class_getIvarLayout(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.class_getIvarLayout(long)"""
        return str._wrap(_ObjCRuntime.class_getIvarLayout(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_replaceProperty(arg0: int, arg1: 'CharSequence', arg2: 'Buffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_replaceProperty(long,java.lang.CharSequence,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer)"""
        _ObjCRuntime.class_replaceProperty(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def protocol_copyPropertyList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.protocol_copyPropertyList(long)"""
        return pygl.PointerBuffer._wrap(_ObjCRuntime.protocol_copyPropertyList(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_replaceMethod(arg0: int, arg1: int, arg2: int, arg3: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_replaceMethod(long,long,long,java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.class_replaceMethod(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def nprotocol_copyPropertyList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nprotocol_copyPropertyList(long,long)"""
        return int._wrap(_ObjCRuntime.nprotocol_copyPropertyList(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nobjc_constructInstance(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_constructInstance(long,long)"""
        return int._wrap(_ObjCRuntime.nobjc_constructInstance(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_getInstanceVariable(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getInstanceVariable(long,java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.class_getInstanceVariable(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def class_setWeakIvarLayout(arg0: int, arg1: 'CharSequence'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_setWeakIvarLayout(long,java.lang.CharSequence)"""
        _ObjCRuntime.class_setWeakIvarLayout(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nclass_copyMethodList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_copyMethodList(long,long)"""
        return int._wrap(_ObjCRuntime.nclass_copyMethodList(_long.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def property_getName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.property_getName(long)"""
        return str._wrap(_ObjCRuntime.property_getName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_getClass(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getClass(java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.objc_getClass(arg0))

    @staticmethod
    @overload
    def class_copyProtocolList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.class_copyProtocolList(long)"""
        return pygl.PointerBuffer._wrap(_ObjCRuntime.class_copyProtocolList(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def method_copyArgumentType(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.method_copyArgumentType(long,int)"""
        return str._wrap(_ObjCRuntime.method_copyArgumentType(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def ivar_getTypeEncoding(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.ivar_getTypeEncoding(long)"""
        return str._wrap(_ObjCRuntime.ivar_getTypeEncoding(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getSuperclass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getSuperclass(long)"""
        return int._wrap(_ObjCRuntime.class_getSuperclass(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nivar_getTypeEncoding(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nivar_getTypeEncoding(long)"""
        return int._wrap(_ObjCRuntime.nivar_getTypeEncoding(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def protocol_addMethodDescription(arg0: int, arg1: int, arg2: 'ByteBuffer', arg3: bool, arg4: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.protocol_addMethodDescription(long,long,java.nio.ByteBuffer,boolean,boolean)"""
        _ObjCRuntime.protocol_addMethodDescription(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _boolean.valueOf(arg3), _boolean.valueOf(arg4))

    @staticmethod
    @overload
    def protocol_conformsToProtocol(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.protocol_conformsToProtocol(long,long)"""
        return bool._wrap(_ObjCRuntime.protocol_conformsToProtocol(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_copyIvarList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.class_copyIvarList(long)"""
        return pygl.PointerBuffer._wrap(_ObjCRuntime.class_copyIvarList(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_allocateClassPair(arg0: int, arg1: 'CharSequence', arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_allocateClassPair(long,java.lang.CharSequence,long)"""
        return int._wrap(_ObjCRuntime.objc_allocateClassPair(_long.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def property_copyAttributeValue(arg0: int, arg1: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.property_copyAttributeValue(long,java.nio.ByteBuffer)"""
        return str._wrap(_ObjCRuntime.property_copyAttributeValue(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def class_addProperty(arg0: int, arg1: 'ByteBuffer', arg2: 'Buffer') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addProperty(long,java.nio.ByteBuffer,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer)"""
        return bool._wrap(_ObjCRuntime.class_addProperty(_long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def objc_allocateClassPair(arg0: int, arg1: 'ByteBuffer', arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_allocateClassPair(long,java.nio.ByteBuffer,long)"""
        return int._wrap(_ObjCRuntime.objc_allocateClassPair(_long.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nobject_getInstanceVariable(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobject_getInstanceVariable(long,long,long)"""
        return int._wrap(_ObjCRuntime.nobject_getInstanceVariable(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmethod_copyArgumentType(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nmethod_copyArgumentType(long,int)"""
        return int._wrap(_ObjCRuntime.nmethod_copyArgumentType(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def object_getClass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_getClass(long)"""
        return int._wrap(_ObjCRuntime.object_getClass(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_getProtocol(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getProtocol(java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.objc_getProtocol(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def objc_removeAssociatedObjects(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_removeAssociatedObjects(long)"""
        _ObjCRuntime.objc_removeAssociatedObjects(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def method_getArgumentType(arg0: int, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.method_getArgumentType(long,int,java.nio.ByteBuffer)"""
        _ObjCRuntime.method_getArgumentType(_long.valueOf(arg0), _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def class_getClassVariable(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getClassVariable(long,java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.class_getClassVariable(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nclass_getInstanceVariable(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getInstanceVariable(long,long)"""
        return int._wrap(_ObjCRuntime.nclass_getInstanceVariable(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_getClassVariable(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getClassVariable(long,java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.class_getClassVariable(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def protocol_getMethodDescription(arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: 'ObjCMethodDescription') -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCRuntime.protocol_getMethodDescription(long,long,boolean,boolean,org.lwjgl.system.macosx.ObjCMethodDescription)"""
        return ObjCMethodDescription._wrap(_ObjCRuntime.protocol_getMethodDescription(_long.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def class_getMethodImplementation(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getMethodImplementation(long,long)"""
        return int._wrap(_ObjCRuntime.class_getMethodImplementation(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nclass_getClassVariable(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getClassVariable(long,long)"""
        return int._wrap(_ObjCRuntime.nclass_getClassVariable(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_isMetaClass(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_isMetaClass(long)"""
        return bool._wrap(_ObjCRuntime.class_isMetaClass(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nprotocol_getProperty(arg0: int, arg1: int, arg2: bool, arg3: bool) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nprotocol_getProperty(long,long,boolean,boolean)"""
        return int._wrap(_ObjCRuntime.nprotocol_getProperty(_long.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def method_getNumberOfArguments(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.ObjCRuntime.method_getNumberOfArguments(long)"""
        return int._wrap(_ObjCRuntime.method_getNumberOfArguments(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def property_getAttributes(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.property_getAttributes(long)"""
        return str._wrap(_ObjCRuntime.property_getAttributes(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobjc_getClassList(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.macosx.ObjCRuntime.nobjc_getClassList(long,int)"""
        return int._wrap(_ObjCRuntime.nobjc_getClassList(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nproperty_copyAttributeValue(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nproperty_copyAttributeValue(long,long)"""
        return int._wrap(_ObjCRuntime.nproperty_copyAttributeValue(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def objc_lookUpClass(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_lookUpClass(java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.objc_lookUpClass(arg0))

    @staticmethod
    @overload
    def objc_copyClassNamesForImage(arg0: 'CharSequence') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.objc_copyClassNamesForImage(java.lang.CharSequence)"""
        return pygl.PointerBuffer._wrap(_ObjCRuntime.objc_copyClassNamesForImage(arg0))

    @staticmethod
    @overload
    def nprotocol_copyMethodDescriptionList(arg0: int, arg1: bool, arg2: bool, arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nprotocol_copyMethodDescriptionList(long,boolean,boolean,long)"""
        return int._wrap(_ObjCRuntime.nprotocol_copyMethodDescriptionList(_long.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def method_getTypeEncoding(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.method_getTypeEncoding(long)"""
        return str._wrap(_ObjCRuntime.method_getTypeEncoding(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def sel_registerName(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.sel_registerName(java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.sel_registerName(arg0))

    @staticmethod
    @overload
    def objc_getClassList(arg0: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.macosx.ObjCRuntime.objc_getClassList(org.lwjgl.PointerBuffer)"""
        return int._wrap(_ObjCRuntime.objc_getClassList(arg0))

    @staticmethod
    @overload
    def nobjc_getMetaClass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_getMetaClass(long)"""
        return int._wrap(_ObjCRuntime.nobjc_getMetaClass(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def method_copyReturnType(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.method_copyReturnType(long)"""
        return str._wrap(_ObjCRuntime.method_copyReturnType(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def method_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.method_getName(long)"""
        return int._wrap(_ObjCRuntime.method_getName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_allocateProtocol(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_allocateProtocol(java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.objc_allocateProtocol(arg0))

    @staticmethod
    @overload
    def objc_setEnumerationMutationHandler(arg0: 'EnumerationMutationHandlerI'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_setEnumerationMutationHandler(org.lwjgl.system.macosx.EnumerationMutationHandlerI)"""
        _ObjCRuntime.objc_setEnumerationMutationHandler(arg0)

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.macosx.ObjCRuntime.getLibrary()"""
        return pyglsystem.SharedLibrary._wrap(_ObjCRuntime.getLibrary())

    @staticmethod
    @overload
    def class_getInstanceSize(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getInstanceSize(long)"""
        return int._wrap(_ObjCRuntime.class_getInstanceSize(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_lookUpClass(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_lookUpClass(java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.objc_lookUpClass(arg0))

    @staticmethod
    @overload
    def nclass_copyIvarList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_copyIvarList(long,long)"""
        return int._wrap(_ObjCRuntime.nclass_copyIvarList(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def method_getArgumentType(arg0: int, arg1: int, arg2: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.method_getArgumentType(long,int,long)"""
        return str._wrap(_ObjCRuntime.method_getArgumentType(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def object_getInstanceVariable(arg0: int, arg1: 'CharSequence', arg2: 'PointerBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_getInstanceVariable(long,java.lang.CharSequence,org.lwjgl.PointerBuffer)"""
        return int._wrap(_ObjCRuntime.object_getInstanceVariable(_long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def objc_getRequiredClass(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getRequiredClass(java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.objc_getRequiredClass(arg0))

    @staticmethod
    @overload
    def method_getReturnType(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.method_getReturnType(long,java.nio.ByteBuffer)"""
        _ObjCRuntime.method_getReturnType(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nproperty_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nproperty_getName(long)"""
        return int._wrap(_ObjCRuntime.nproperty_getName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_addMethod(arg0: int, arg1: int, arg2: int, arg3: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addMethod(long,long,long,java.lang.CharSequence)"""
        return bool._wrap(_ObjCRuntime.class_addMethod(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def protocol_getName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.protocol_getName(long)"""
        return str._wrap(_ObjCRuntime.protocol_getName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getVersion(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.ObjCRuntime.class_getVersion(long)"""
        return int._wrap(_ObjCRuntime.class_getVersion(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobjc_copyClassList(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_copyClassList(long)"""
        return int._wrap(_ObjCRuntime.nobjc_copyClassList(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nprotocol_copyProtocolList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nprotocol_copyProtocolList(long,long)"""
        return int._wrap(_ObjCRuntime.nprotocol_copyProtocolList(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_copyMethodList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.class_copyMethodList(long)"""
        return pygl.PointerBuffer._wrap(_ObjCRuntime.class_copyMethodList(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def object_getClassName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.object_getClassName(long)"""
        return str._wrap(_ObjCRuntime.object_getClassName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_createInstance(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_createInstance(long,long)"""
        return int._wrap(_ObjCRuntime.class_createInstance(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def protocol_copyProtocolList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.protocol_copyProtocolList(long)"""
        return pygl.PointerBuffer._wrap(_ObjCRuntime.protocol_copyProtocolList(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_destructInstance(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_destructInstance(long)"""
        return int._wrap(_ObjCRuntime.objc_destructInstance(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getImageName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.class_getImageName(long)"""
        return str._wrap(_ObjCRuntime.class_getImageName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def object_getInstanceVariable(arg0: int, arg1: 'ByteBuffer', arg2: 'PointerBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_getInstanceVariable(long,java.nio.ByteBuffer,org.lwjgl.PointerBuffer)"""
        return int._wrap(_ObjCRuntime.object_getInstanceVariable(_long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def nmethod_getArgumentType(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nmethod_getArgumentType(long,int,long,long)"""
        _ObjCRuntime.nmethod_getArgumentType(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nivar_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nivar_getName(long)"""
        return int._wrap(_ObjCRuntime.nivar_getName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_registerProtocol(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_registerProtocol(long)"""
        _ObjCRuntime.objc_registerProtocol(_long.valueOf(arg0))

    @staticmethod
    @overload
    def class_addIvar(arg0: int, arg1: 'CharSequence', arg2: int, arg3: int, arg4: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addIvar(long,java.lang.CharSequence,long,byte,java.lang.CharSequence)"""
        return bool._wrap(_ObjCRuntime.class_addIvar(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _byte.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def objc_getProtocol(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getProtocol(java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.objc_getProtocol(arg0))

    @staticmethod
    @overload
    def objc_disposeClassPair(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_disposeClassPair(long)"""
        _ObjCRuntime.objc_disposeClassPair(_long.valueOf(arg0))

    @staticmethod
    @overload
    def imp_removeBlock(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.imp_removeBlock(long)"""
        return bool._wrap(_ObjCRuntime.imp_removeBlock(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def object_setInstanceVariable(arg0: int, arg1: 'ByteBuffer', arg2: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_setInstanceVariable(long,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.object_setInstanceVariable(_long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def nobjc_storeWeak(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_storeWeak(long,long)"""
        return int._wrap(_ObjCRuntime.nobjc_storeWeak(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_replaceMethod(arg0: int, arg1: int, arg2: int, arg3: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_replaceMethod(long,long,long,java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.class_replaceMethod(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def nobjc_copyImageNames(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_copyImageNames(long)"""
        return int._wrap(_ObjCRuntime.nobjc_copyImageNames(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nclass_getImageName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getImageName(long)"""
        return int._wrap(_ObjCRuntime.nclass_getImageName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_setAssociatedObject(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_setAssociatedObject(long,long,long,long)"""
        _ObjCRuntime.objc_setAssociatedObject(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def class_setWeakIvarLayout(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_setWeakIvarLayout(long,java.nio.ByteBuffer)"""
        _ObjCRuntime.class_setWeakIvarLayout(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def method_setImplementation(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.method_setImplementation(long,long)"""
        return int._wrap(_ObjCRuntime.method_setImplementation(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nclass_getWeakIvarLayout(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getWeakIvarLayout(long)"""
        return int._wrap(_ObjCRuntime.nclass_getWeakIvarLayout(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def protocol_addMethodDescription(arg0: int, arg1: int, arg2: 'CharSequence', arg3: bool, arg4: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.protocol_addMethodDescription(long,long,java.lang.CharSequence,boolean,boolean)"""
        _ObjCRuntime.protocol_addMethodDescription(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _boolean.valueOf(arg3), _boolean.valueOf(arg4))

    @staticmethod
    @overload
    def nobjc_getProtocol(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_getProtocol(long)"""
        return int._wrap(_ObjCRuntime.nobjc_getProtocol(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobject_setInstanceVariable(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobject_setInstanceVariable(long,long,long)"""
        return int._wrap(_ObjCRuntime.nobject_setInstanceVariable(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def ivar_getOffset(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.ivar_getOffset(long)"""
        return int._wrap(_ObjCRuntime.ivar_getOffset(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nobjc_setEnumerationMutationHandler(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nobjc_setEnumerationMutationHandler(long)"""
        _ObjCRuntime.nobjc_setEnumerationMutationHandler(_long.valueOf(arg0))

    @staticmethod
    @overload
    def class_copyPropertyList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.class_copyPropertyList(long)"""
        return pygl.PointerBuffer._wrap(_ObjCRuntime.class_copyPropertyList(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def protocol_getProperty(arg0: int, arg1: 'CharSequence', arg2: bool, arg3: bool) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.protocol_getProperty(long,java.lang.CharSequence,boolean,boolean)"""
        return int._wrap(_ObjCRuntime.protocol_getProperty(_long.valueOf(arg0), arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def nclass_addMethod(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.nclass_addMethod(long,long,long,long)"""
        return bool._wrap(_ObjCRuntime.nclass_addMethod(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def imp_getBlock(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.imp_getBlock(long)"""
        return int._wrap(_ObjCRuntime.imp_getBlock(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nprotocol_addMethodDescription(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nprotocol_addMethodDescription(long,long,long,boolean,boolean)"""
        _ObjCRuntime.nprotocol_addMethodDescription(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4))

    @staticmethod
    @overload
    def nclass_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getName(long)"""
        return int._wrap(_ObjCRuntime.nclass_getName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nprotocol_addProperty(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nprotocol_addProperty(long,long,long,int,boolean,boolean)"""
        _ObjCRuntime.nprotocol_addProperty(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4), _boolean.valueOf(arg5))

    @staticmethod
    @overload
    def class_addMethod(arg0: int, arg1: int, arg2: int, arg3: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addMethod(long,long,long,java.nio.ByteBuffer)"""
        return bool._wrap(_ObjCRuntime.class_addMethod(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def object_copy(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_copy(long,long)"""
        return int._wrap(_ObjCRuntime.object_copy(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def method_getReturnType(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.method_getReturnType(long,long)"""
        return str._wrap(_ObjCRuntime.method_getReturnType(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def object_getIvar(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_getIvar(long,long)"""
        return int._wrap(_ObjCRuntime.object_getIvar(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def objc_copyImageNames() -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.objc_copyImageNames()"""
        return pygl.PointerBuffer._wrap(_ObjCRuntime.objc_copyImageNames())

    @staticmethod
    @overload
    def object_getIndexedIvars(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_getIndexedIvars(long)"""
        return int._wrap(_ObjCRuntime.object_getIndexedIvars(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def sel_registerName(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.sel_registerName(java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.sel_registerName(arg0))

    @staticmethod
    @overload
    def nclass_setIvarLayout(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nclass_setIvarLayout(long,long)"""
        _ObjCRuntime.nclass_setIvarLayout(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nclass_getProperty(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getProperty(long,long)"""
        return int._wrap(_ObjCRuntime.nclass_getProperty(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nclass_getIvarLayout(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getIvarLayout(long)"""
        return int._wrap(_ObjCRuntime.nclass_getIvarLayout(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def object_dispose(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_dispose(long)"""
        return int._wrap(_ObjCRuntime.object_dispose(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_getMetaClass(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getMetaClass(java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.objc_getMetaClass(arg0))

    @staticmethod
    @overload
    def class_setVersion(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_setVersion(long,int)"""
        _ObjCRuntime.class_setVersion(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nobjc_getRequiredClass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_getRequiredClass(long)"""
        return int._wrap(_ObjCRuntime.nobjc_getRequiredClass(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmethod_getTypeEncoding(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nmethod_getTypeEncoding(long)"""
        return int._wrap(_ObjCRuntime.nmethod_getTypeEncoding(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobjc_copyProtocolList(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_copyProtocolList(long)"""
        return int._wrap(_ObjCRuntime.nobjc_copyProtocolList(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nprotocol_getMethodDescription(arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nprotocol_getMethodDescription(long,long,boolean,boolean,long)"""
        _ObjCRuntime.nprotocol_getMethodDescription(_long.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def nobject_getClassName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobject_getClassName(long)"""
        return int._wrap(_ObjCRuntime.nobject_getClassName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.class_getName(long)"""
        return str._wrap(_ObjCRuntime.class_getName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_replaceProperty(arg0: int, arg1: 'ByteBuffer', arg2: 'Buffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_replaceProperty(long,java.nio.ByteBuffer,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer)"""
        _ObjCRuntime.class_replaceProperty(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def nsel_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nsel_getName(long)"""
        return int._wrap(_ObjCRuntime.nsel_getName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def protocol_addProperty(arg0: int, arg1: 'CharSequence', arg2: 'Buffer', arg3: bool, arg4: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.protocol_addProperty(long,java.lang.CharSequence,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer,boolean,boolean)"""
        _ObjCRuntime.protocol_addProperty(_long.valueOf(arg0), arg1, arg2, _boolean.valueOf(arg3), _boolean.valueOf(arg4))

    @staticmethod
    @overload
    def sel_isEqual(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.sel_isEqual(long,long)"""
        return bool._wrap(_ObjCRuntime.sel_isEqual(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_respondsToSelector(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_respondsToSelector(long,long)"""
        return bool._wrap(_ObjCRuntime.class_respondsToSelector(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def protocol_isEqual(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.protocol_isEqual(long,long)"""
        return bool._wrap(_ObjCRuntime.protocol_isEqual(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nproperty_copyAttributeList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nproperty_copyAttributeList(long,long)"""
        return int._wrap(_ObjCRuntime.nproperty_copyAttributeList(_long.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def nobjc_allocateClassPair(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_allocateClassPair(long,long,long)"""
        return int._wrap(_ObjCRuntime.nobjc_allocateClassPair(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nprotocol_getMethodDescription(arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.macosx.ObjCRuntime.nprotocol_getMethodDescription(long,long,boolean,boolean,long,long)"""
        _ObjCRuntime.nprotocol_getMethodDescription(_long.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def objc_getAssociatedObject(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getAssociatedObject(long,long)"""
        return int._wrap(_ObjCRuntime.objc_getAssociatedObject(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nmethod_getReturnType(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nmethod_getReturnType(long,long,long)"""
        _ObjCRuntime.nmethod_getReturnType(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def objc_getClass(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getClass(java.lang.CharSequence)"""
        return int._wrap(_ObjCRuntime.objc_getClass(arg0))

    @staticmethod
    @overload
    def protocol_addProperty(arg0: int, arg1: 'ByteBuffer', arg2: 'Buffer', arg3: bool, arg4: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.protocol_addProperty(long,java.nio.ByteBuffer,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer,boolean,boolean)"""
        _ObjCRuntime.protocol_addProperty(_long.valueOf(arg0), arg1, arg2, _boolean.valueOf(arg3), _boolean.valueOf(arg4))

    @staticmethod
    @overload
    def nsel_registerName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nsel_registerName(long)"""
        return int._wrap(_ObjCRuntime.nsel_registerName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nclass_setWeakIvarLayout(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nclass_setWeakIvarLayout(long,long)"""
        _ObjCRuntime.nclass_setWeakIvarLayout(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def object_setClass(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_setClass(long,long)"""
        return int._wrap(_ObjCRuntime.object_setClass(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def objc_copyClassNamesForImage(arg0: 'ByteBuffer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.objc_copyClassNamesForImage(java.nio.ByteBuffer)"""
        return pygl.PointerBuffer._wrap(_ObjCRuntime.objc_copyClassNamesForImage(arg0))

    @staticmethod
    @overload
    def nproperty_getAttributes(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nproperty_getAttributes(long)"""
        return int._wrap(_ObjCRuntime.nproperty_getAttributes(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def sel_getName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.sel_getName(long)"""
        return str._wrap(_ObjCRuntime.sel_getName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_addIvar(arg0: int, arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addIvar(long,java.nio.ByteBuffer,long,byte,java.nio.ByteBuffer)"""
        return bool._wrap(_ObjCRuntime.class_addIvar(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _byte.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def nprotocol_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nprotocol_getName(long)"""
        return int._wrap(_ObjCRuntime.nprotocol_getName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def property_copyAttributeValue(arg0: int, arg1: 'CharSequence') -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.property_copyAttributeValue(long,java.lang.CharSequence)"""
        return str._wrap(_ObjCRuntime.property_copyAttributeValue(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def protocol_getProperty(arg0: int, arg1: 'ByteBuffer', arg2: bool, arg3: bool) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.protocol_getProperty(long,java.nio.ByteBuffer,boolean,boolean)"""
        return int._wrap(_ObjCRuntime.protocol_getProperty(_long.valueOf(arg0), arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def objc_getRequiredClass(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getRequiredClass(java.nio.ByteBuffer)"""
        return int._wrap(_ObjCRuntime.objc_getRequiredClass(arg0))

    @staticmethod
    @overload
    def nclass_replaceMethod(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_replaceMethod(long,long,long,long)"""
        return int._wrap(_ObjCRuntime.nclass_replaceMethod(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def method_getImplementation(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.method_getImplementation(long)"""
        return int._wrap(_ObjCRuntime.method_getImplementation(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nclass_addProperty(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.nclass_addProperty(long,long,long,int)"""
        return bool._wrap(_ObjCRuntime.nclass_addProperty(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def imp_implementationWithBlock(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.imp_implementationWithBlock(long)"""
        return int._wrap(_ObjCRuntime.imp_implementationWithBlock(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobjc_getClass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_getClass(long)"""
        return int._wrap(_ObjCRuntime.nobjc_getClass(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_copyClassList() -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.objc_copyClassList()"""
        return pygl.PointerBuffer._wrap(_ObjCRuntime.objc_copyClassList()) 
 
 
# CLASS: org.lwjgl.system.macosx.CGEventTapInformation
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.system.macosx.CGEventTapInformation as _CGEventTapInformation_Buffer
_Buffer = _CGEventTapInformation_Buffer.Buffer
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.system.macosx.CGEventTapInformation as _CGEventTapInformation
_CGEventTapInformation = _CGEventTapInformation
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CGEventTapInformation():
    """org.lwjgl.system.macosx.CGEventTapInformation"""
 
    @staticmethod
    def _wrap(java_value: _CGEventTapInformation) -> 'CGEventTapInformation':
        return CGEventTapInformation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CGEventTapInformation):
        """
        Dynamic initializer for CGEventTapInformation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CGEventTapInformation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CGEventTapInformation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.malloc(int)"""
        return Buffer._wrap(_CGEventTapInformation.malloc(_int.valueOf(arg0)))

    @overload
    def minUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation.minUsecLatency()"""
        return float._wrap(super(CGEventTapInformation, self).minUsecLatency())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.CGEventTapInformation(java.nio.ByteBuffer)"""
        val = _CGEventTapInformation(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def mallocStack() -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.mallocStack()"""
        return CGEventTapInformation._wrap(_CGEventTapInformation.mallocStack())

    @overload
    def maxUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation.maxUsecLatency()"""
        return float._wrap(super(CGEventTapInformation, self).maxUsecLatency())

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

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.calloc(int)"""
        return Buffer._wrap(_CGEventTapInformation.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.create(int)"""
        return Buffer._wrap(_CGEventTapInformation.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.create()"""
        return CGEventTapInformation._wrap(_CGEventTapInformation.create())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def options(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation.options()"""
        return int._wrap(super(CGEventTapInformation, self).options())

    @staticmethod
    @overload
    def ntappingProcess(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CGEventTapInformation.ntappingProcess(long)"""
        return int._wrap(_CGEventTapInformation.ntappingProcess(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntapPoint(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.CGEventTapInformation.ntapPoint(long)"""
        return int._wrap(_CGEventTapInformation.ntapPoint(_long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation.sizeof()"""
        return int._wrap(super(CGEventTapInformation, self).sizeof())

    @staticmethod
    @overload
    def callocStack() -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.callocStack()"""
        return CGEventTapInformation._wrap(_CGEventTapInformation.callocStack())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.callocStack(org.lwjgl.system.MemoryStack)"""
        return CGEventTapInformation._wrap(_CGEventTapInformation.callocStack(arg0))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def tappingProcess(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation.tappingProcess()"""
        return int._wrap(super(CGEventTapInformation, self).tappingProcess())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def nminUsecLatency(arg0: int) -> float:
        """public static float org.lwjgl.system.macosx.CGEventTapInformation.nminUsecLatency(long)"""
        return float._wrap(_CGEventTapInformation.nminUsecLatency(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.calloc()"""
        return CGEventTapInformation._wrap(_CGEventTapInformation.calloc())

    @staticmethod
    @overload
    def create(arg0: int) -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.create(long)"""
        return CGEventTapInformation._wrap(_CGEventTapInformation.create(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_CGEventTapInformation.mallocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def navgUsecLatency(arg0: int) -> float:
        """public static float org.lwjgl.system.macosx.CGEventTapInformation.navgUsecLatency(long)"""
        return float._wrap(_CGEventTapInformation.navgUsecLatency(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_CGEventTapInformation.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_CGEventTapInformation.callocStack(_int.valueOf(arg0), arg1))

    @overload
    def processBeingTapped(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation.processBeingTapped()"""
        return int._wrap(super(CGEventTapInformation, self).processBeingTapped())

    @overload
    def avgUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation.avgUsecLatency()"""
        return float._wrap(super(CGEventTapInformation, self).avgUsecLatency())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def eventsOfInterest(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation.eventsOfInterest()"""
        return int._wrap(super(CGEventTapInformation, self).eventsOfInterest())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.malloc(org.lwjgl.system.MemoryStack)"""
        return CGEventTapInformation._wrap(_CGEventTapInformation.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.create(long,int)"""
        return Buffer._wrap(_CGEventTapInformation.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def neventsOfInterest(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CGEventTapInformation.neventsOfInterest(long)"""
        return int._wrap(_CGEventTapInformation.neventsOfInterest(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def noptions(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.CGEventTapInformation.noptions(long)"""
        return int._wrap(_CGEventTapInformation.noptions(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.createSafe(long)"""
        return CGEventTapInformation._wrap(_CGEventTapInformation.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmaxUsecLatency(arg0: int) -> float:
        """public static float org.lwjgl.system.macosx.CGEventTapInformation.nmaxUsecLatency(long)"""
        return float._wrap(_CGEventTapInformation.nmaxUsecLatency(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.malloc()"""
        return CGEventTapInformation._wrap(_CGEventTapInformation.malloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.createSafe(long,int)"""
        return Buffer._wrap(_CGEventTapInformation.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def tapPoint(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation.tapPoint()"""
        return int._wrap(super(CGEventTapInformation, self).tapPoint())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def neventTapID(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.CGEventTapInformation.neventTapID(long)"""
        return int._wrap(_CGEventTapInformation.neventTapID(_long.valueOf(arg0)))

    @overload
    def enabled(self) -> bool:
        """public boolean org.lwjgl.system.macosx.CGEventTapInformation.enabled()"""
        return bool._wrap(super(CGEventTapInformation, self).enabled())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.mallocStack(org.lwjgl.system.MemoryStack)"""
        return CGEventTapInformation._wrap(_CGEventTapInformation.mallocStack(arg0))

    @overload
    def eventTapID(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation.eventTapID()"""
        return int._wrap(super(CGEventTapInformation, self).eventTapID())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.callocStack(int)"""
        return Buffer._wrap(_CGEventTapInformation.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_CGEventTapInformation.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nenabled(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.CGEventTapInformation.nenabled(long)"""
        return bool._wrap(_CGEventTapInformation.nenabled(_long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.mallocStack(int)"""
        return Buffer._wrap(_CGEventTapInformation.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.calloc(org.lwjgl.system.MemoryStack)"""
        return CGEventTapInformation._wrap(_CGEventTapInformation.calloc(arg0))

    @staticmethod
    @overload
    def nprocessBeingTapped(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CGEventTapInformation.nprocessBeingTapped(long)"""
        return int._wrap(_CGEventTapInformation.nprocessBeingTapped(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import org.lwjgl.system.macosx.ObjCPropertyAttribute as _ObjCPropertyAttribute_Buffer
_Buffer = _ObjCPropertyAttribute_Buffer.Buffer
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.macosx.ObjCPropertyAttribute.Buffer"""
 
    @staticmethod
    def _wrap(java_value: _Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Buffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Buffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).limit(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def value(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.value(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).value(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).stream())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def name(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.name()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).name())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def name(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.name(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).name(arg0))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def nameString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.nameString()"""
        return str._wrap(super(Buffer, self).nameString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def value(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.value()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).value())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).clear())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def valueString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.valueString()"""
        return str._wrap(super(Buffer, self).valueString())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int._wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.macosx.CGPoint$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import org.lwjgl.system.macosx.CGPoint as _CGPoint_Buffer
_Buffer = _CGPoint_Buffer.Buffer
from builtins import float
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.macosx.CGPoint.Buffer"""
 
    @staticmethod
    def _wrap(java_value: _Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Buffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Buffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.CGPoint$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).limit(_int.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def x(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint$Buffer.x(double)"""
        return 'Buffer'._wrap(super(_Buffer, self).x(_double.valueOf(arg0)))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).stream())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @overload
    def y(self) -> float:
        """public double org.lwjgl.system.macosx.CGPoint$Buffer.y()"""
        return float._wrap(super(Buffer, self).y())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.macosx.CGPoint$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def x(self) -> float:
        """public double org.lwjgl.system.macosx.CGPoint$Buffer.x()"""
        return float._wrap(super(Buffer, self).x())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).clear())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int._wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def y(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint$Buffer.y(double)"""
        return 'Buffer'._wrap(super(_Buffer, self).y(_double.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.macosx.CGPoint
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.macosx.CGPoint as _CGPoint_Buffer
_Buffer = _CGPoint_Buffer.Buffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.system.macosx.CGPoint as _CGPoint
_CGPoint = _CGPoint
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CGPoint():
    """org.lwjgl.system.macosx.CGPoint"""
 
    @staticmethod
    def _wrap(java_value: _CGPoint) -> 'CGPoint':
        return CGPoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CGPoint):
        """
        Dynamic initializer for CGPoint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CGPoint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CGPoint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def calloc() -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.calloc()"""
        return CGPoint._wrap(_CGPoint.calloc())

    @staticmethod
    @overload
    def nx(arg0: int, arg1: float):
        """public static void org.lwjgl.system.macosx.CGPoint.nx(long,double)"""
        _CGPoint.nx(_long.valueOf(arg0), _double.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def x(self) -> float:
        """public double org.lwjgl.system.macosx.CGPoint.x()"""
        return float._wrap(super(CGPoint, self).x())

    @overload
    def y(self, arg0: float) -> 'CGPoint':
        """public org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.y(double)"""
        return 'CGPoint'._wrap(super(_CGPoint, self).y(_double.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def ny(arg0: int, arg1: float):
        """public static void org.lwjgl.system.macosx.CGPoint.ny(long,double)"""
        _CGPoint.ny(_long.valueOf(arg0), _double.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nx(arg0: int) -> float:
        """public static double org.lwjgl.system.macosx.CGPoint.nx(long)"""
        return float._wrap(_CGPoint.nx(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def x(self, arg0: float) -> 'CGPoint':
        """public org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.x(double)"""
        return 'CGPoint'._wrap(super(_CGPoint, self).x(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_CGPoint.malloc(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: float, arg1: float) -> 'CGPoint':
        """public org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.set(double,double)"""
        return 'CGPoint'._wrap(super(_CGPoint, self).set(_double.valueOf(arg0), _double.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_CGPoint.mallocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def malloc() -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.malloc()"""
        return CGPoint._wrap(_CGPoint.malloc())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_CGPoint.callocStack(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: 'CGPoint') -> 'CGPoint':
        """public org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.set(org.lwjgl.system.macosx.CGPoint)"""
        return 'CGPoint'._wrap(super(_CGPoint, self).set(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.callocStack(int)"""
        return Buffer._wrap(_CGPoint.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.create()"""
        return CGPoint._wrap(_CGPoint.create())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.malloc(org.lwjgl.system.MemoryStack)"""
        return CGPoint._wrap(_CGPoint.malloc(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def mallocStack() -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.mallocStack()"""
        return CGPoint._wrap(_CGPoint.mallocStack())

    @staticmethod
    @overload
    def ny(arg0: int) -> float:
        """public static double org.lwjgl.system.macosx.CGPoint.ny(long)"""
        return float._wrap(_CGPoint.ny(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.create(long,int)"""
        return Buffer._wrap(_CGPoint.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.mallocStack(org.lwjgl.system.MemoryStack)"""
        return CGPoint._wrap(_CGPoint.mallocStack(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.createSafe(long)"""
        return CGPoint._wrap(_CGPoint.createSafe(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.create(int)"""
        return Buffer._wrap(_CGPoint.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.calloc(org.lwjgl.system.MemoryStack)"""
        return CGPoint._wrap(_CGPoint.calloc(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.createSafe(long,int)"""
        return Buffer._wrap(_CGPoint.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def y(self) -> float:
        """public double org.lwjgl.system.macosx.CGPoint.y()"""
        return float._wrap(super(CGPoint, self).y())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.mallocStack(int)"""
        return Buffer._wrap(_CGPoint.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.callocStack()"""
        return CGPoint._wrap(_CGPoint.callocStack())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.calloc(int)"""
        return Buffer._wrap(_CGPoint.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.malloc(int)"""
        return Buffer._wrap(_CGPoint.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.create(long)"""
        return CGPoint._wrap(_CGPoint.create(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.CGPoint(java.nio.ByteBuffer)"""
        val = _CGPoint(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.macosx.CGPoint.sizeof()"""
        return int._wrap(super(CGPoint, self).sizeof())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_CGPoint.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.callocStack(org.lwjgl.system.MemoryStack)"""
        return CGPoint._wrap(_CGPoint.callocStack(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())