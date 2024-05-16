from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.nio.DoubleBuffer as _DoubleBuffer
_DoubleBuffer = _DoubleBuffer
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PointerBuffer():
    """org.lwjgl.PointerBuffer"""
 
    @staticmethod
    def _wrap(java_value: _PointerBuffer) -> 'PointerBuffer':
        return PointerBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PointerBuffer):
        """
        Dynamic initializer for PointerBuffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PointerBuffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PointerBuffer__wrapper":
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
    def put(self, arg0: 'ShortBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.ShortBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

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

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.create(long,int)"""
        return PointerBuffer._wrap(_PointerBuffer.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getStringASCII(self, arg0: int) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringASCII(int)"""
        return str._wrap(super(_PointerBuffer, self).getStringASCII(_int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def put(self, arg0: int, arg1: 'DoubleBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.DoubleBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'IntBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.IntBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

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
    def putAddressOf(self, arg0: int, arg1: 'CustomBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.putAddressOf(int,org.lwjgl.system.CustomBuffer<?>)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).putAddressOf(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def get(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.PointerBuffer.get(java.nio.ByteBuffer)"""
        return int._wrap(_PointerBuffer.get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getStringUTF16(self, arg0: int) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF16(int)"""
        return str._wrap(super(_PointerBuffer, self).getStringUTF16(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @overload
    def put(self, arg0: int, arg1: 'ByteBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.ByteBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

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
    def get(self, arg0: 'long') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.get(long[])"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).get(arg0))

    @overload
    def put(self, arg0: int, arg1: 'FloatBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.FloatBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

    @overload
    def getDoubleBuffer(self, arg0: int) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.PointerBuffer.getDoubleBuffer(int)"""
        return 'DoubleBuffer'._wrap(super(_PointerBuffer, self).getDoubleBuffer(_int.valueOf(arg0)))

    @overload
    def get(self, arg0: 'long', arg1: int, arg2: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.get(long[],int,int)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).get(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getPointerBuffer(self, arg0: int, arg1: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.getPointerBuffer(int,int)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).getPointerBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def put(self, arg0: 'FloatBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.FloatBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.PointerBuffer.hashCode()"""
        return int._wrap(super(PointerBuffer, self).hashCode())

    @overload
    def getByteBuffer(self, arg0: int, arg1: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.PointerBuffer.getByteBuffer(int,int)"""
        return 'ByteBuffer'._wrap(super(_PointerBuffer, self).getByteBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'ByteBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.ByteBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

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

    @overload
    def putAddressOf(self, arg0: 'CustomBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.putAddressOf(org.lwjgl.system.CustomBuffer<?>)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).putAddressOf(arg0))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def getStringASCII(self) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringASCII()"""
        return str._wrap(super(PointerBuffer, self).getStringASCII())

    @staticmethod
    @overload
    def create(arg0: 'ByteBuffer') -> 'PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.create(java.nio.ByteBuffer)"""
        return PointerBuffer._wrap(_PointerBuffer.create(arg0))

    @overload
    def put(self, arg0: int, arg1: 'LongBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.LongBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

    @overload
    def getDoubleBuffer(self, arg0: int, arg1: int) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.PointerBuffer.getDoubleBuffer(int,int)"""
        return 'DoubleBuffer'._wrap(super(_PointerBuffer, self).getDoubleBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getIntBuffer(self, arg0: int, arg1: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.PointerBuffer.getIntBuffer(int,int)"""
        return 'IntBuffer'._wrap(super(_PointerBuffer, self).getIntBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getStringUTF8(self) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF8()"""
        return str._wrap(super(PointerBuffer, self).getStringUTF8())

    @overload
    def getLongBuffer(self, arg0: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.PointerBuffer.getLongBuffer(int)"""
        return 'LongBuffer'._wrap(super(_PointerBuffer, self).getLongBuffer(_int.valueOf(arg0)))

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
    def put(self, arg0: int, arg1: 'ShortBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.ShortBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def put(arg0: 'ByteBuffer', arg1: int, arg2: int):
        """public static void org.lwjgl.PointerBuffer.put(java.nio.ByteBuffer,int,long)"""
        _PointerBuffer.put(arg0, _int.valueOf(arg1), _long.valueOf(arg2))

    @overload
    def put(self, arg0: 'long') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(long[])"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @overload
    def put(self, arg0: 'long', arg1: int, arg2: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(long[],int,int)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getPointerBuffer(self, arg0: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.getPointerBuffer(int)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).getPointerBuffer(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'Pointer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(org.lwjgl.system.Pointer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @overload
    def getByteBuffer(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.PointerBuffer.getByteBuffer(int)"""
        return 'ByteBuffer'._wrap(super(_PointerBuffer, self).getByteBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.PointerBuffer.sizeof()"""
        return int._wrap(super(PointerBuffer, self).sizeof())

    @overload
    def put(self, arg0: 'DoubleBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.DoubleBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @overload
    def getFloatBuffer(self, arg0: int) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.PointerBuffer.getFloatBuffer(int)"""
        return 'FloatBuffer'._wrap(super(_PointerBuffer, self).getFloatBuffer(_int.valueOf(arg0)))

    @overload
    def get(self) -> int:
        """public long org.lwjgl.PointerBuffer.get()"""
        return int._wrap(super(PointerBuffer, self).get())

    @overload
    def put(self, arg0: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(long)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_long.valueOf(arg0)))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def put(arg0: 'ByteBuffer', arg1: int):
        """public static void org.lwjgl.PointerBuffer.put(java.nio.ByteBuffer,long)"""
        _PointerBuffer.put(arg0, _long.valueOf(arg1))

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
    def getLongBuffer(self, arg0: int, arg1: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.PointerBuffer.getLongBuffer(int,int)"""
        return 'LongBuffer'._wrap(super(_PointerBuffer, self).getLongBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def getStringUTF16(self) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF16()"""
        return str._wrap(super(PointerBuffer, self).getStringUTF16())

    @overload
    def put(self, arg0: 'LongBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.LongBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @overload
    def put(self, arg0: int, arg1: 'Pointer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,org.lwjgl.system.Pointer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

    @overload
    def getShortBuffer(self, arg0: int, arg1: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.PointerBuffer.getShortBuffer(int,int)"""
        return 'ShortBuffer'._wrap(super(_PointerBuffer, self).getShortBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def compareTo(self, arg0: 'PointerBuffer') -> int:
        """public int org.lwjgl.PointerBuffer.compareTo(org.lwjgl.PointerBuffer)"""
        return int._wrap(super(_PointerBuffer, self).compareTo(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getShortBuffer(self, arg0: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.PointerBuffer.getShortBuffer(int)"""
        return 'ShortBuffer'._wrap(super(_PointerBuffer, self).getShortBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def get(self, arg0: int) -> int:
        """public long org.lwjgl.PointerBuffer.get(int)"""
        return int._wrap(super(_PointerBuffer, self).get(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: int, arg1: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,long)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.PointerBuffer.equals(java.lang.Object)"""
        return bool._wrap(super(_PointerBuffer, self).equals(arg0))

    @overload
    def getStringUTF8(self, arg0: int) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF8(int)"""
        return str._wrap(super(_PointerBuffer, self).getStringUTF8(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def get(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static long org.lwjgl.PointerBuffer.get(java.nio.ByteBuffer,int)"""
        return int._wrap(_PointerBuffer.get(arg0, _int.valueOf(arg1)))

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
    def put(self, arg0: 'IntBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.IntBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @staticmethod
    @overload
    def allocateDirect(arg0: int) -> 'PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.allocateDirect(int)"""
        return PointerBuffer._wrap(_PointerBuffer.allocateDirect(_int.valueOf(arg0)))

    @overload
    def getFloatBuffer(self, arg0: int, arg1: int) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.PointerBuffer.getFloatBuffer(int,int)"""
        return 'FloatBuffer'._wrap(super(_PointerBuffer, self).getFloatBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getIntBuffer(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.PointerBuffer.getIntBuffer(int)"""
        return 'IntBuffer'._wrap(super(_PointerBuffer, self).getIntBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

 
 
 
# CLASS: org.lwjgl.PointerBuffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.nio.DoubleBuffer as _DoubleBuffer
_DoubleBuffer = _DoubleBuffer
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PointerBuffer():
    """org.lwjgl.PointerBuffer"""
 
    @staticmethod
    def _wrap(java_value: _PointerBuffer) -> 'PointerBuffer':
        return PointerBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PointerBuffer):
        """
        Dynamic initializer for PointerBuffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PointerBuffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PointerBuffer__wrapper":
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
    def put(self, arg0: 'ShortBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.ShortBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

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

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.create(long,int)"""
        return PointerBuffer._wrap(_PointerBuffer.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getStringASCII(self, arg0: int) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringASCII(int)"""
        return str._wrap(super(_PointerBuffer, self).getStringASCII(_int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def put(self, arg0: int, arg1: 'DoubleBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.DoubleBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'IntBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.IntBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

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
    def putAddressOf(self, arg0: int, arg1: 'CustomBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.putAddressOf(int,org.lwjgl.system.CustomBuffer<?>)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).putAddressOf(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def get(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.PointerBuffer.get(java.nio.ByteBuffer)"""
        return int._wrap(_PointerBuffer.get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getStringUTF16(self, arg0: int) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF16(int)"""
        return str._wrap(super(_PointerBuffer, self).getStringUTF16(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @overload
    def put(self, arg0: int, arg1: 'ByteBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.ByteBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

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
    def get(self, arg0: 'long') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.get(long[])"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).get(arg0))

    @overload
    def put(self, arg0: int, arg1: 'FloatBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.FloatBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

    @overload
    def getDoubleBuffer(self, arg0: int) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.PointerBuffer.getDoubleBuffer(int)"""
        return 'DoubleBuffer'._wrap(super(_PointerBuffer, self).getDoubleBuffer(_int.valueOf(arg0)))

    @overload
    def get(self, arg0: 'long', arg1: int, arg2: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.get(long[],int,int)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).get(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getPointerBuffer(self, arg0: int, arg1: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.getPointerBuffer(int,int)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).getPointerBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def put(self, arg0: 'FloatBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.FloatBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.PointerBuffer.hashCode()"""
        return int._wrap(super(PointerBuffer, self).hashCode())

    @overload
    def getByteBuffer(self, arg0: int, arg1: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.PointerBuffer.getByteBuffer(int,int)"""
        return 'ByteBuffer'._wrap(super(_PointerBuffer, self).getByteBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'ByteBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.ByteBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

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

    @overload
    def putAddressOf(self, arg0: 'CustomBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.putAddressOf(org.lwjgl.system.CustomBuffer<?>)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).putAddressOf(arg0))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def getStringASCII(self) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringASCII()"""
        return str._wrap(super(PointerBuffer, self).getStringASCII())

    @staticmethod
    @overload
    def create(arg0: 'ByteBuffer') -> 'PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.create(java.nio.ByteBuffer)"""
        return PointerBuffer._wrap(_PointerBuffer.create(arg0))

    @overload
    def put(self, arg0: int, arg1: 'LongBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.LongBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

    @overload
    def getDoubleBuffer(self, arg0: int, arg1: int) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.PointerBuffer.getDoubleBuffer(int,int)"""
        return 'DoubleBuffer'._wrap(super(_PointerBuffer, self).getDoubleBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getIntBuffer(self, arg0: int, arg1: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.PointerBuffer.getIntBuffer(int,int)"""
        return 'IntBuffer'._wrap(super(_PointerBuffer, self).getIntBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getStringUTF8(self) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF8()"""
        return str._wrap(super(PointerBuffer, self).getStringUTF8())

    @overload
    def getLongBuffer(self, arg0: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.PointerBuffer.getLongBuffer(int)"""
        return 'LongBuffer'._wrap(super(_PointerBuffer, self).getLongBuffer(_int.valueOf(arg0)))

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
    def put(self, arg0: int, arg1: 'ShortBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.ShortBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def put(arg0: 'ByteBuffer', arg1: int, arg2: int):
        """public static void org.lwjgl.PointerBuffer.put(java.nio.ByteBuffer,int,long)"""
        _PointerBuffer.put(arg0, _int.valueOf(arg1), _long.valueOf(arg2))

    @overload
    def put(self, arg0: 'long') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(long[])"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @overload
    def put(self, arg0: 'long', arg1: int, arg2: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(long[],int,int)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getPointerBuffer(self, arg0: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.getPointerBuffer(int)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).getPointerBuffer(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'Pointer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(org.lwjgl.system.Pointer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @overload
    def getByteBuffer(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.PointerBuffer.getByteBuffer(int)"""
        return 'ByteBuffer'._wrap(super(_PointerBuffer, self).getByteBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.PointerBuffer.sizeof()"""
        return int._wrap(super(PointerBuffer, self).sizeof())

    @overload
    def put(self, arg0: 'DoubleBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.DoubleBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @overload
    def getFloatBuffer(self, arg0: int) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.PointerBuffer.getFloatBuffer(int)"""
        return 'FloatBuffer'._wrap(super(_PointerBuffer, self).getFloatBuffer(_int.valueOf(arg0)))

    @overload
    def get(self) -> int:
        """public long org.lwjgl.PointerBuffer.get()"""
        return int._wrap(super(PointerBuffer, self).get())

    @overload
    def put(self, arg0: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(long)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_long.valueOf(arg0)))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def put(arg0: 'ByteBuffer', arg1: int):
        """public static void org.lwjgl.PointerBuffer.put(java.nio.ByteBuffer,long)"""
        _PointerBuffer.put(arg0, _long.valueOf(arg1))

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
    def getLongBuffer(self, arg0: int, arg1: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.PointerBuffer.getLongBuffer(int,int)"""
        return 'LongBuffer'._wrap(super(_PointerBuffer, self).getLongBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def getStringUTF16(self) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF16()"""
        return str._wrap(super(PointerBuffer, self).getStringUTF16())

    @overload
    def put(self, arg0: 'LongBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.LongBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @overload
    def put(self, arg0: int, arg1: 'Pointer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,org.lwjgl.system.Pointer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), arg1))

    @overload
    def getShortBuffer(self, arg0: int, arg1: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.PointerBuffer.getShortBuffer(int,int)"""
        return 'ShortBuffer'._wrap(super(_PointerBuffer, self).getShortBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def compareTo(self, arg0: 'PointerBuffer') -> int:
        """public int org.lwjgl.PointerBuffer.compareTo(org.lwjgl.PointerBuffer)"""
        return int._wrap(super(_PointerBuffer, self).compareTo(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getShortBuffer(self, arg0: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.PointerBuffer.getShortBuffer(int)"""
        return 'ShortBuffer'._wrap(super(_PointerBuffer, self).getShortBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def get(self, arg0: int) -> int:
        """public long org.lwjgl.PointerBuffer.get(int)"""
        return int._wrap(super(_PointerBuffer, self).get(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: int, arg1: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,long)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(_int.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.PointerBuffer.equals(java.lang.Object)"""
        return bool._wrap(super(_PointerBuffer, self).equals(arg0))

    @overload
    def getStringUTF8(self, arg0: int) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF8(int)"""
        return str._wrap(super(_PointerBuffer, self).getStringUTF8(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def get(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static long org.lwjgl.PointerBuffer.get(java.nio.ByteBuffer,int)"""
        return int._wrap(_PointerBuffer.get(arg0, _int.valueOf(arg1)))

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
    def put(self, arg0: 'IntBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.IntBuffer)"""
        return 'PointerBuffer'._wrap(super(_PointerBuffer, self).put(arg0))

    @staticmethod
    @overload
    def allocateDirect(arg0: int) -> 'PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.allocateDirect(int)"""
        return PointerBuffer._wrap(_PointerBuffer.allocateDirect(_int.valueOf(arg0)))

    @overload
    def getFloatBuffer(self, arg0: int, arg1: int) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.PointerBuffer.getFloatBuffer(int,int)"""
        return 'FloatBuffer'._wrap(super(_PointerBuffer, self).getFloatBuffer(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def getIntBuffer(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.PointerBuffer.getIntBuffer(int)"""
        return 'IntBuffer'._wrap(super(_PointerBuffer, self).getIntBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

 
 
 
# CLASS: org.lwjgl.PointerBuffer 
 
 
# CLASS: org.lwjgl.BufferUtils
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.nio.FloatBuffer as FloatBuffer
import org.lwjgl.CLongBuffer as _CLongBuffer
_CLongBuffer = _CLongBuffer
import java.nio.DoubleBuffer as _DoubleBuffer
_DoubleBuffer = _DoubleBuffer
import java.nio.CharBuffer as _CharBuffer
_CharBuffer = _CharBuffer
import java.nio.CharBuffer as CharBuffer
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.BufferUtils as _BufferUtils
_BufferUtils = _BufferUtils
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BufferUtils():
    """org.lwjgl.BufferUtils"""
 
    @staticmethod
    def _wrap(java_value: _BufferUtils) -> 'BufferUtils':
        return BufferUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BufferUtils):
        """
        Dynamic initializer for BufferUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BufferUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BufferUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def createLongBuffer(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.BufferUtils.createLongBuffer(int)"""
        return LongBuffer._wrap(_BufferUtils.createLongBuffer(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'IntBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.IntBuffer)"""
        _BufferUtils.zeroBuffer(arg0)

    @staticmethod
    @overload
    def createCharBuffer(arg0: int) -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.BufferUtils.createCharBuffer(int)"""
        return CharBuffer._wrap(_BufferUtils.createCharBuffer(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'ShortBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.ShortBuffer)"""
        _BufferUtils.zeroBuffer(arg0)

    @staticmethod
    @overload
    def createCLongBuffer(arg0: int) -> 'CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.BufferUtils.createCLongBuffer(int)"""
        return CLongBuffer._wrap(_BufferUtils.createCLongBuffer(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'DoubleBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.DoubleBuffer)"""
        _BufferUtils.zeroBuffer(arg0)

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.ByteBuffer)"""
        _BufferUtils.zeroBuffer(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'FloatBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.FloatBuffer)"""
        _BufferUtils.zeroBuffer(arg0)

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
    def zeroBuffer(arg0: 'CharBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.CharBuffer)"""
        _BufferUtils.zeroBuffer(arg0)

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'LongBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.LongBuffer)"""
        _BufferUtils.zeroBuffer(arg0)

    @staticmethod
    @overload
    def createByteBuffer(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.BufferUtils.createByteBuffer(int)"""
        return ByteBuffer._wrap(_BufferUtils.createByteBuffer(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def createPointerBuffer(arg0: int) -> 'PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.BufferUtils.createPointerBuffer(int)"""
        return PointerBuffer._wrap(_BufferUtils.createPointerBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def createDoubleBuffer(arg0: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.BufferUtils.createDoubleBuffer(int)"""
        return DoubleBuffer._wrap(_BufferUtils.createDoubleBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def createShortBuffer(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.BufferUtils.createShortBuffer(int)"""
        return ShortBuffer._wrap(_BufferUtils.createShortBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createIntBuffer(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.BufferUtils.createIntBuffer(int)"""
        return IntBuffer._wrap(_BufferUtils.createIntBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'CustomBuffer'):
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> void org.lwjgl.BufferUtils.zeroBuffer(T)"""
        _BufferUtils.zeroBuffer(arg0)

    @staticmethod
    @overload
    def createFloatBuffer(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.BufferUtils.createFloatBuffer(int)"""
        return FloatBuffer._wrap(_BufferUtils.createFloatBuffer(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.Version$BuildType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.Version as _Version_BuildType
_BuildType = _Version_BuildType.BuildType
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BuildType():
    """org.lwjgl.Version.BuildType"""
 
    @staticmethod
    def _wrap(java_value: _BuildType) -> 'BuildType':
        return BuildType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BuildType):
        """
        Dynamic initializer for BuildType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BuildType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BuildType__wrapper":
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

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['BuildType']:
        """public static org.lwjgl.Version$BuildType[] org.lwjgl.Version$BuildType.values()"""
        return List[BuildType]._wrap(_BuildType.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BuildType':
        """public static org.lwjgl.Version$BuildType org.lwjgl.Version$BuildType.valueOf(java.lang.String)"""
        return BuildType._wrap(_BuildType.valueOf(arg0)) 
 
 
# CLASS: org.lwjgl.Version
from builtins import str
import org.lwjgl.Version as _Version
_Version = _Version
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
 
class Version():
    """org.lwjgl.Version"""
 
    @staticmethod
    def _wrap(java_value: _Version) -> 'Version':
        return Version(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Version):
        """
        Dynamic initializer for Version.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Version__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Version__wrapper":
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

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void org.lwjgl.Version.main(java.lang.String[])"""
        _Version.main(arg0)

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
    def getVersion() -> str:
        """public static java.lang.String org.lwjgl.Version.getVersion()"""
        return str._wrap(_Version.getVersion())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.CLongBuffer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.CLongBuffer as _CLongBuffer
_CLongBuffer = _CLongBuffer
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CLongBuffer():
    """org.lwjgl.CLongBuffer"""
 
    @staticmethod
    def _wrap(java_value: _CLongBuffer) -> 'CLongBuffer':
        return CLongBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CLongBuffer):
        """
        Dynamic initializer for CLongBuffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CLongBuffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CLongBuffer__wrapper":
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
    def put(self, arg0: int) -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.put(long)"""
        return 'CLongBuffer'._wrap(super(_CLongBuffer, self).put(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def put(arg0: 'ByteBuffer', arg1: int):
        """public static void org.lwjgl.CLongBuffer.put(java.nio.ByteBuffer,long)"""
        _CLongBuffer.put(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'ByteBuffer') -> 'CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.create(java.nio.ByteBuffer)"""
        return CLongBuffer._wrap(_CLongBuffer.create(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.CLongBuffer.equals(java.lang.Object)"""
        return bool._wrap(super(_CLongBuffer, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, arg0: int) -> int:
        """public long org.lwjgl.CLongBuffer.get(int)"""
        return int._wrap(super(_CLongBuffer, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.create(long,int)"""
        return CLongBuffer._wrap(_CLongBuffer.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @staticmethod
    @overload
    def get(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static long org.lwjgl.CLongBuffer.get(java.nio.ByteBuffer,int)"""
        return int._wrap(_CLongBuffer.get(arg0, _int.valueOf(arg1)))

    @overload
    def put(self, arg0: 'long') -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.put(long[])"""
        return 'CLongBuffer'._wrap(super(_CLongBuffer, self).put(arg0))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.CLongBuffer.sizeof()"""
        return int._wrap(super(CLongBuffer, self).sizeof())

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

    @staticmethod
    @overload
    def get(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.CLongBuffer.get(java.nio.ByteBuffer)"""
        return int._wrap(_CLongBuffer.get(arg0))

    @staticmethod
    @overload
    def allocateDirect(arg0: int) -> 'CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.allocateDirect(int)"""
        return CLongBuffer._wrap(_CLongBuffer.allocateDirect(_int.valueOf(arg0)))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.CLongBuffer.hashCode()"""
        return int._wrap(super(CLongBuffer, self).hashCode())

    @overload
    def put(self, arg0: 'long', arg1: int, arg2: int) -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.put(long[],int,int)"""
        return 'CLongBuffer'._wrap(super(_CLongBuffer, self).put(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def put(self, arg0: int, arg1: int) -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.put(int,long)"""
        return 'CLongBuffer'._wrap(super(_CLongBuffer, self).put(_int.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def get(self, arg0: 'long', arg1: int, arg2: int) -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.get(long[],int,int)"""
        return 'CLongBuffer'._wrap(super(_CLongBuffer, self).get(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self) -> int:
        """public long org.lwjgl.CLongBuffer.get()"""
        return int._wrap(super(CLongBuffer, self).get())

    @staticmethod
    @overload
    def put(arg0: 'ByteBuffer', arg1: int, arg2: int):
        """public static void org.lwjgl.CLongBuffer.put(java.nio.ByteBuffer,int,long)"""
        _CLongBuffer.put(arg0, _int.valueOf(arg1), _long.valueOf(arg2))

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
    def compareTo(self, arg0: 'CLongBuffer') -> int:
        """public int org.lwjgl.CLongBuffer.compareTo(org.lwjgl.CLongBuffer)"""
        return int._wrap(super(_CLongBuffer, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: 'long') -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.get(long[])"""
        return 'CLongBuffer'._wrap(super(_CLongBuffer, self).get(arg0))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))