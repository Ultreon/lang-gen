from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import org.lwjgl.system.libc.LibCString as _LibCString
_LibCString = _LibCString
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibCString():
    """org.lwjgl.system.libc.LibCString"""
 
    @staticmethod
    def _wrap(java_value: _LibCString) -> 'LibCString':
        return LibCString(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibCString):
        """
        Dynamic initializer for LibCString.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibCString__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibCString__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def memcpy(arg0: 'LongBuffer', arg1: 'LongBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.LongBuffer,java.nio.LongBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def nmemset(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(long,int,long)"""
        return int._wrap(_LibCString.nmemset(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memset(arg0: 'int', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(int[],int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nmemset(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(int[],int,long)"""
        return int._wrap(_LibCString.nmemset(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemset(arg0: 'long', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(long[],int,long)"""
        return int._wrap(_LibCString.nmemset(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nmemmove(arg0: 'short', arg1: 'short', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(short[],short[],long)"""
        return int._wrap(_LibCString.nmemmove(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memmove(arg0: 'DoubleBuffer', arg1: 'DoubleBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.DoubleBuffer,java.nio.DoubleBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nmemset(arg0: 'float', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(float[],int,long)"""
        return int._wrap(_LibCString.nmemset(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memcpy(arg0: 'long', arg1: 'long') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(long[],long[])"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def nstrlen(arg0: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nstrlen(long)"""
        return int._wrap(_LibCString.nstrlen(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmemcpy(arg0: 'short', arg1: 'short', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(short[],short[],long)"""
        return int._wrap(_LibCString.nmemcpy(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemmove(arg0: 'int', arg1: 'int', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(int[],int[],long)"""
        return int._wrap(_LibCString.nmemmove(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memset(arg0: 'DoubleBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.DoubleBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memmove(arg0: bytes, arg1: bytes) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(byte[],byte[])"""
        return int._wrap(_LibCString.memmove(bytes, bytes))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def memset(arg0: bytes, arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(byte[],int)"""
        return int._wrap(_LibCString.memset(bytes, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memset(arg0: 'float', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(float[],int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memcpy(arg0: 'IntBuffer', arg1: 'IntBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.IntBuffer,java.nio.IntBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def nmemcpy(arg0: 'int', arg1: 'int', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(int[],int[],long)"""
        return int._wrap(_LibCString.nmemcpy(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemset(arg0: 'double', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(double[],int,long)"""
        return int._wrap(_LibCString.nmemset(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def memcpy(arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'ShortBuffer', arg1: 'ShortBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.ShortBuffer,java.nio.ShortBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def memset(arg0: 'CustomBuffer', arg1: int) -> int:
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> long org.lwjgl.system.libc.LibCString.memset(T,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memmove(arg0: 'IntBuffer', arg1: 'IntBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.IntBuffer,java.nio.IntBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def nmemmove(arg0: 'double', arg1: 'double', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(double[],double[],long)"""
        return int._wrap(_LibCString.nmemmove(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memcpy(arg0: 'float', arg1: 'float') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(float[],float[])"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memcpy(arg0: 'double', arg1: 'double') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(double[],double[])"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'int', arg1: 'int') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(int[],int[])"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def memset(arg0: 'FloatBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.FloatBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def memcpy(arg0: 'CustomBuffer', arg1: 'CustomBuffer') -> int:
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> long org.lwjgl.system.libc.LibCString.memcpy(T,T)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memset(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.ByteBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memmove(arg0: 'short', arg1: 'short') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(short[],short[])"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nmemcpy(arg0: 'double', arg1: 'double', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(double[],double[],long)"""
        return int._wrap(_LibCString.nmemcpy(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemmove(arg0: 'long', arg1: 'long', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(long[],long[],long)"""
        return int._wrap(_LibCString.nmemmove(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memcpy(arg0: bytes, arg1: bytes) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(byte[],byte[])"""
        return int._wrap(_LibCString.memcpy(bytes, bytes))

    @staticmethod
    @overload
    def nmemcpy(arg0: 'long', arg1: 'long', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(long[],long[],long)"""
        return int._wrap(_LibCString.nmemcpy(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memset(arg0: 'long', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(long[],int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memmove(arg0: 'FloatBuffer', arg1: 'FloatBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'long', arg1: 'long') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(long[],long[])"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'LongBuffer', arg1: 'LongBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.LongBuffer,java.nio.LongBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'double', arg1: 'double') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(double[],double[])"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def nmemset(arg0: bytes, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(byte[],int,long)"""
        return int._wrap(_LibCString.nmemset(bytes, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemcpy(arg0: bytes, arg1: bytes, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(byte[],byte[],long)"""
        return int._wrap(_LibCString.nmemcpy(bytes, bytes, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memmove(arg0: 'CustomBuffer', arg1: 'CustomBuffer') -> int:
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> long org.lwjgl.system.libc.LibCString.memmove(T,T)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def nmemcpy(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(long,long,long)"""
        return int._wrap(_LibCString.nmemcpy(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemmove(arg0: 'float', arg1: 'float', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(float[],float[],long)"""
        return int._wrap(_LibCString.nmemmove(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memset(arg0: 'IntBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.IntBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memset(arg0: 'LongBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.LongBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nmemset(arg0: 'short', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(short[],int,long)"""
        return int._wrap(_LibCString.nmemset(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memcpy(arg0: 'FloatBuffer', arg1: 'FloatBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def nmemmove(arg0: bytes, arg1: bytes, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(byte[],byte[],long)"""
        return int._wrap(_LibCString.nmemmove(bytes, bytes, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstrerror(arg0: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nstrerror(int)"""
        return int._wrap(_LibCString.nstrerror(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def strerror(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.libc.LibCString.strerror(int)"""
        return str._wrap(_LibCString.strerror(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memset(arg0: 'short', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(short[],int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memcpy(arg0: 'ShortBuffer', arg1: 'ShortBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.ShortBuffer,java.nio.ShortBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def memset(arg0: 'ShortBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.ShortBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nmemmove(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(long,long,long)"""
        return int._wrap(_LibCString.nmemmove(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemcpy(arg0: 'float', arg1: 'float', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(float[],float[],long)"""
        return int._wrap(_LibCString.nmemcpy(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memcpy(arg0: 'short', arg1: 'short') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(short[],short[])"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memcpy(arg0: 'int', arg1: 'int') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(int[],int[])"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def strlen(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.strlen(java.nio.ByteBuffer)"""
        return int._wrap(_LibCString.strlen(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def memset(arg0: 'double', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(double[],int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memcpy(arg0: 'DoubleBuffer', arg1: 'DoubleBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.DoubleBuffer,java.nio.DoubleBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'float', arg1: 'float') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(float[],float[])"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

 
 
 
# CLASS: org.lwjgl.system.libc.LibCString
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import org.lwjgl.system.libc.LibCString as _LibCString
_LibCString = _LibCString
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibCString():
    """org.lwjgl.system.libc.LibCString"""
 
    @staticmethod
    def _wrap(java_value: _LibCString) -> 'LibCString':
        return LibCString(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibCString):
        """
        Dynamic initializer for LibCString.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibCString__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibCString__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def memcpy(arg0: 'LongBuffer', arg1: 'LongBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.LongBuffer,java.nio.LongBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def nmemset(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(long,int,long)"""
        return int._wrap(_LibCString.nmemset(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memset(arg0: 'int', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(int[],int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nmemset(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(int[],int,long)"""
        return int._wrap(_LibCString.nmemset(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemset(arg0: 'long', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(long[],int,long)"""
        return int._wrap(_LibCString.nmemset(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nmemmove(arg0: 'short', arg1: 'short', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(short[],short[],long)"""
        return int._wrap(_LibCString.nmemmove(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memmove(arg0: 'DoubleBuffer', arg1: 'DoubleBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.DoubleBuffer,java.nio.DoubleBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nmemset(arg0: 'float', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(float[],int,long)"""
        return int._wrap(_LibCString.nmemset(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memcpy(arg0: 'long', arg1: 'long') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(long[],long[])"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def nstrlen(arg0: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nstrlen(long)"""
        return int._wrap(_LibCString.nstrlen(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmemcpy(arg0: 'short', arg1: 'short', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(short[],short[],long)"""
        return int._wrap(_LibCString.nmemcpy(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemmove(arg0: 'int', arg1: 'int', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(int[],int[],long)"""
        return int._wrap(_LibCString.nmemmove(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memset(arg0: 'DoubleBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.DoubleBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memmove(arg0: bytes, arg1: bytes) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(byte[],byte[])"""
        return int._wrap(_LibCString.memmove(bytes, bytes))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def memset(arg0: bytes, arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(byte[],int)"""
        return int._wrap(_LibCString.memset(bytes, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memset(arg0: 'float', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(float[],int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memcpy(arg0: 'IntBuffer', arg1: 'IntBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.IntBuffer,java.nio.IntBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def nmemcpy(arg0: 'int', arg1: 'int', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(int[],int[],long)"""
        return int._wrap(_LibCString.nmemcpy(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemset(arg0: 'double', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(double[],int,long)"""
        return int._wrap(_LibCString.nmemset(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def memcpy(arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'ShortBuffer', arg1: 'ShortBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.ShortBuffer,java.nio.ShortBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def memset(arg0: 'CustomBuffer', arg1: int) -> int:
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> long org.lwjgl.system.libc.LibCString.memset(T,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memmove(arg0: 'IntBuffer', arg1: 'IntBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.IntBuffer,java.nio.IntBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def nmemmove(arg0: 'double', arg1: 'double', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(double[],double[],long)"""
        return int._wrap(_LibCString.nmemmove(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memcpy(arg0: 'float', arg1: 'float') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(float[],float[])"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memcpy(arg0: 'double', arg1: 'double') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(double[],double[])"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'int', arg1: 'int') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(int[],int[])"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def memset(arg0: 'FloatBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.FloatBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def memcpy(arg0: 'CustomBuffer', arg1: 'CustomBuffer') -> int:
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> long org.lwjgl.system.libc.LibCString.memcpy(T,T)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memset(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.ByteBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memmove(arg0: 'short', arg1: 'short') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(short[],short[])"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nmemcpy(arg0: 'double', arg1: 'double', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(double[],double[],long)"""
        return int._wrap(_LibCString.nmemcpy(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemmove(arg0: 'long', arg1: 'long', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(long[],long[],long)"""
        return int._wrap(_LibCString.nmemmove(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memcpy(arg0: bytes, arg1: bytes) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(byte[],byte[])"""
        return int._wrap(_LibCString.memcpy(bytes, bytes))

    @staticmethod
    @overload
    def nmemcpy(arg0: 'long', arg1: 'long', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(long[],long[],long)"""
        return int._wrap(_LibCString.nmemcpy(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memset(arg0: 'long', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(long[],int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memmove(arg0: 'FloatBuffer', arg1: 'FloatBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'long', arg1: 'long') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(long[],long[])"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'LongBuffer', arg1: 'LongBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.LongBuffer,java.nio.LongBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'double', arg1: 'double') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(double[],double[])"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def nmemset(arg0: bytes, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(byte[],int,long)"""
        return int._wrap(_LibCString.nmemset(bytes, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemcpy(arg0: bytes, arg1: bytes, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(byte[],byte[],long)"""
        return int._wrap(_LibCString.nmemcpy(bytes, bytes, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memmove(arg0: 'CustomBuffer', arg1: 'CustomBuffer') -> int:
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> long org.lwjgl.system.libc.LibCString.memmove(T,T)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @staticmethod
    @overload
    def nmemcpy(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(long,long,long)"""
        return int._wrap(_LibCString.nmemcpy(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemmove(arg0: 'float', arg1: 'float', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(float[],float[],long)"""
        return int._wrap(_LibCString.nmemmove(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memset(arg0: 'IntBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.IntBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memset(arg0: 'LongBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.LongBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nmemset(arg0: 'short', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemset(short[],int,long)"""
        return int._wrap(_LibCString.nmemset(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memcpy(arg0: 'FloatBuffer', arg1: 'FloatBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def nmemmove(arg0: bytes, arg1: bytes, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(byte[],byte[],long)"""
        return int._wrap(_LibCString.nmemmove(bytes, bytes, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstrerror(arg0: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nstrerror(int)"""
        return int._wrap(_LibCString.nstrerror(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def strerror(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.libc.LibCString.strerror(int)"""
        return str._wrap(_LibCString.strerror(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memset(arg0: 'short', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(short[],int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memcpy(arg0: 'ShortBuffer', arg1: 'ShortBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.ShortBuffer,java.nio.ShortBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def memset(arg0: 'ShortBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(java.nio.ShortBuffer,int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nmemmove(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemmove(long,long,long)"""
        return int._wrap(_LibCString.nmemmove(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemcpy(arg0: 'float', arg1: 'float', arg2: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCString.nmemcpy(float[],float[],long)"""
        return int._wrap(_LibCString.nmemcpy(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def memcpy(arg0: 'short', arg1: 'short') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(short[],short[])"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memcpy(arg0: 'int', arg1: 'int') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(int[],int[])"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def strlen(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.strlen(java.nio.ByteBuffer)"""
        return int._wrap(_LibCString.strlen(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def memset(arg0: 'double', arg1: int) -> int:
        """public static long org.lwjgl.system.libc.LibCString.memset(double[],int)"""
        return int._wrap(_LibCString.memset(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memcpy(arg0: 'DoubleBuffer', arg1: 'DoubleBuffer') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memcpy(java.nio.DoubleBuffer,java.nio.DoubleBuffer)"""
        return int._wrap(_LibCString.memcpy(arg0, arg1))

    @staticmethod
    @overload
    def memmove(arg0: 'float', arg1: 'float') -> int:
        """public static long org.lwjgl.system.libc.LibCString.memmove(float[],float[])"""
        return int._wrap(_LibCString.memmove(arg0, arg1))

 
 
 
# CLASS: org.lwjgl.system.libc.LibCString 
 
 
# CLASS: org.lwjgl.system.libc.LibCStdlib
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.lang.Object as _object
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.nio.LongBuffer as LongBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Integer as _int
import org.lwjgl.system.libc.LibCStdlib as _LibCStdlib
_LibCStdlib = _LibCStdlib
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibCStdlib():
    """org.lwjgl.system.libc.LibCStdlib"""
 
    @staticmethod
    def _wrap(java_value: _LibCStdlib) -> 'LibCStdlib':
        return LibCStdlib(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibCStdlib):
        """
        Dynamic initializer for LibCStdlib.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibCStdlib__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibCStdlib__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def aligned_free(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.aligned_free(java.nio.ByteBuffer)"""
        _LibCStdlib.aligned_free(arg0)

    @staticmethod
    @overload
    def aligned_free(arg0: 'FloatBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.aligned_free(java.nio.FloatBuffer)"""
        _LibCStdlib.aligned_free(arg0)

    @staticmethod
    @overload
    def aligned_free(arg0: 'PointerBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.aligned_free(org.lwjgl.PointerBuffer)"""
        _LibCStdlib.aligned_free(arg0)

    @staticmethod
    @overload
    def aligned_free(arg0: 'LongBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.aligned_free(java.nio.LongBuffer)"""
        _LibCStdlib.aligned_free(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nmalloc(arg0: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCStdlib.nmalloc(long)"""
        return int._wrap(_LibCStdlib.nmalloc(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def aligned_free(arg0: 'ShortBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.aligned_free(java.nio.ShortBuffer)"""
        _LibCStdlib.aligned_free(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def naligned_alloc(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCStdlib.naligned_alloc(long,long)"""
        return int._wrap(_LibCStdlib.naligned_alloc(_long.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def free(arg0: 'ShortBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.free(java.nio.ShortBuffer)"""
        _LibCStdlib.free(arg0)

    @staticmethod
    @overload
    def realloc(arg0: 'ByteBuffer', arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.libc.LibCStdlib.realloc(java.nio.ByteBuffer,long)"""
        return ByteBuffer._wrap(_LibCStdlib.realloc(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def free(arg0: 'LongBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.free(java.nio.LongBuffer)"""
        _LibCStdlib.free(arg0)

    @staticmethod
    @overload
    def free(arg0: 'PointerBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.free(org.lwjgl.PointerBuffer)"""
        _LibCStdlib.free(arg0)

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.libc.LibCStdlib.calloc(long,long)"""
        return ByteBuffer._wrap(_LibCStdlib.calloc(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nrealloc(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCStdlib.nrealloc(long,long)"""
        return int._wrap(_LibCStdlib.nrealloc(_long.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def aligned_alloc(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.libc.LibCStdlib.aligned_alloc(long,long)"""
        return ByteBuffer._wrap(_LibCStdlib.aligned_alloc(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def free(arg0: 'DoubleBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.free(java.nio.DoubleBuffer)"""
        _LibCStdlib.free(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def aligned_free(arg0: 'DoubleBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.aligned_free(java.nio.DoubleBuffer)"""
        _LibCStdlib.aligned_free(arg0)

    @staticmethod
    @overload
    def aligned_free(arg0: 'IntBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.aligned_free(java.nio.IntBuffer)"""
        _LibCStdlib.aligned_free(arg0)

    @staticmethod
    @overload
    def nfree(arg0: int):
        """public static native void org.lwjgl.system.libc.LibCStdlib.nfree(long)"""
        _LibCStdlib.nfree(_long.valueOf(arg0))

    @staticmethod
    @overload
    def free(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.free(java.nio.ByteBuffer)"""
        _LibCStdlib.free(arg0)

    @staticmethod
    @overload
    def free(arg0: 'FloatBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.free(java.nio.FloatBuffer)"""
        _LibCStdlib.free(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def free(arg0: 'IntBuffer'):
        """public static void org.lwjgl.system.libc.LibCStdlib.free(java.nio.IntBuffer)"""
        _LibCStdlib.free(arg0)

    @staticmethod
    @overload
    def ncalloc(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCStdlib.ncalloc(long,long)"""
        return int._wrap(_LibCStdlib.ncalloc(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def naligned_free(arg0: int):
        """public static native void org.lwjgl.system.libc.LibCStdlib.naligned_free(long)"""
        _LibCStdlib.naligned_free(_long.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.libc.LibCStdlib.malloc(long)"""
        return ByteBuffer._wrap(_LibCStdlib.malloc(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.libc.LibCErrno
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import org.lwjgl.system.libc.LibCErrno as _LibCErrno
_LibCErrno = _LibCErrno
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibCErrno():
    """org.lwjgl.system.libc.LibCErrno"""
 
    @staticmethod
    def _wrap(java_value: _LibCErrno) -> 'LibCErrno':
        return LibCErrno(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibCErrno):
        """
        Dynamic initializer for LibCErrno.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibCErrno__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibCErrno__wrapper":
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
    def errno() -> int:
        """public static native int org.lwjgl.system.libc.LibCErrno.errno()"""
        return int._wrap(_LibCErrno.errno())

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

    @staticmethod
    @overload
    def getErrno() -> int:
        """public static native int org.lwjgl.system.libc.LibCErrno.getErrno()"""
        return int._wrap(_LibCErrno.getErrno())

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
 
 
# CLASS: org.lwjgl.system.libc.LibCLocale
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.libc.LibCLocale as _LibCLocale
_LibCLocale = _LibCLocale
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibCLocale():
    """org.lwjgl.system.libc.LibCLocale"""
 
    @staticmethod
    def _wrap(java_value: _LibCLocale) -> 'LibCLocale':
        return LibCLocale(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibCLocale):
        """
        Dynamic initializer for LibCLocale.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibCLocale__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibCLocale__wrapper":
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
    def setlocale(arg0: int, arg1: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.libc.LibCLocale.setlocale(int,java.nio.ByteBuffer)"""
        return str._wrap(_LibCLocale.setlocale(_int.valueOf(arg0), arg1))

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
    def nsetlocale(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.libc.LibCLocale.nsetlocale(int,long)"""
        return int._wrap(_LibCLocale.nsetlocale(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def setlocale(arg0: int, arg1: 'CharSequence') -> str:
        """public static java.lang.String org.lwjgl.system.libc.LibCLocale.setlocale(int,java.lang.CharSequence)"""
        return str._wrap(_LibCLocale.setlocale(_int.valueOf(arg0), arg1))

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
 
 
# CLASS: org.lwjgl.system.libc.LibCStdio
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.libc.LibCStdio as _LibCStdio
_LibCStdio = _LibCStdio
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibCStdio():
    """org.lwjgl.system.libc.LibCStdio"""
 
    @staticmethod
    def _wrap(java_value: _LibCStdio) -> 'LibCStdio':
        return LibCStdio(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibCStdio):
        """
        Dynamic initializer for LibCStdio.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibCStdio__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibCStdio__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nvsscanf(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.libc.LibCStdio.nvsscanf(long,long,long)"""
        return int._wrap(_LibCStdio.nvsscanf(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def vsnprintf(arg0: 'ByteBuffer', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.lwjgl.system.libc.LibCStdio.vsnprintf(java.nio.ByteBuffer,java.lang.CharSequence,long)"""
        return int._wrap(_LibCStdio.vsnprintf(arg0, arg1, _long.valueOf(arg2)))

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

    @staticmethod
    @overload
    def vsscanf(arg0: 'CharSequence', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.lwjgl.system.libc.LibCStdio.vsscanf(java.lang.CharSequence,java.lang.CharSequence,long)"""
        return int._wrap(_LibCStdio.vsscanf(arg0, arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def vsnprintf(arg0: 'ByteBuffer', arg1: 'ByteBuffer', arg2: int) -> int:
        """public static int org.lwjgl.system.libc.LibCStdio.vsnprintf(java.nio.ByteBuffer,java.nio.ByteBuffer,long)"""
        return int._wrap(_LibCStdio.vsnprintf(arg0, arg1, _long.valueOf(arg2)))

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
    def nvsnprintf(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.libc.LibCStdio.nvsnprintf(long,long,long,long)"""
        return int._wrap(_LibCStdio.nvsnprintf(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def vsscanf(arg0: 'ByteBuffer', arg1: 'ByteBuffer', arg2: int) -> int:
        """public static int org.lwjgl.system.libc.LibCStdio.vsscanf(java.nio.ByteBuffer,java.nio.ByteBuffer,long)"""
        return int._wrap(_LibCStdio.vsscanf(arg0, arg1, _long.valueOf(arg2)))

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