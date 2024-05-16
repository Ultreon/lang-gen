from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.lwjgl.Version as __Version
__Version = __Version
from builtins import bool
from builtins import int
 
class Version():
    """org.lwjgl.Version"""
 
    @staticmethod
    def __wrap(java_value: __Version) -> 'Version':
        return Version(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Version):
        """
        Dynamic initializer for Version.
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
    def main(arg0: 'String'):
        """public static void org.lwjgl.Version.main(java.lang.String[])"""
        __Version.main(arg0)

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

    @staticmethod
    @overload
    def getVersion() -> str:
        """public static java.lang.String org.lwjgl.Version.getVersion()"""
        return str.__wrap(__Version.getVersion())

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

 
 
 
# CLASS: org.lwjgl.Version
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.lwjgl.Version as __Version
__Version = __Version
from builtins import bool
from builtins import int
 
class Version():
    """org.lwjgl.Version"""
 
    @staticmethod
    def __wrap(java_value: __Version) -> 'Version':
        return Version(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Version):
        """
        Dynamic initializer for Version.
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
    def main(arg0: 'String'):
        """public static void org.lwjgl.Version.main(java.lang.String[])"""
        __Version.main(arg0)

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

    @staticmethod
    @overload
    def getVersion() -> str:
        """public static java.lang.String org.lwjgl.Version.getVersion()"""
        return str.__wrap(__Version.getVersion())

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

 
 
 
# CLASS: org.lwjgl.Version 
 
 
# CLASS: org.lwjgl.PointerBuffer
from pyquantum_helper import import_once as __import_once__
import java.nio.IntBuffer as IntBuffer
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import bool
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
import java.lang.Long as __long
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.nio.DoubleBuffer as __DoubleBuffer
__DoubleBuffer = __DoubleBuffer
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class PointerBuffer():
    """org.lwjgl.PointerBuffer"""
 
    @staticmethod
    def __wrap(java_value: __PointerBuffer) -> 'PointerBuffer':
        return PointerBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PointerBuffer):
        """
        Dynamic initializer for PointerBuffer.
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
 
    @overload
    def getStringUTF8(self) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF8()"""
        return str.__wrap(super(PointerBuffer, self).getStringUTF8())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'long', arg1: int, arg2: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(long[],int,int)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: 'ByteBuffer') -> 'PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.create(java.nio.ByteBuffer)"""
        return PointerBuffer.__wrap(__PointerBuffer.create(arg0))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def put(self, arg0: int, arg1: 'LongBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.LongBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'IntBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.IntBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def get(self, arg0: 'long', arg1: int, arg2: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.get(long[],int,int)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).get(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def put(self, arg0: 'LongBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.LongBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(arg0))

    @overload
    def put(self, arg0: 'long') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(long[])"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(arg0))

    @overload
    def put(self, arg0: int, arg1: 'Pointer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,org.lwjgl.system.Pointer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def put(arg0: 'ByteBuffer', arg1: int, arg2: int):
        """public static void org.lwjgl.PointerBuffer.put(java.nio.ByteBuffer,int,long)"""
        __PointerBuffer.put(arg0, __int.valueOf(arg1), __long.valueOf(arg2))

    @overload
    def getPointerBuffer(self, arg0: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.getPointerBuffer(int)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).getPointerBuffer(__int.valueOf(arg0)))

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def getByteBuffer(self, arg0: int, arg1: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.PointerBuffer.getByteBuffer(int,int)"""
        return 'ByteBuffer'.__wrap(super(__PointerBuffer, self).getByteBuffer(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def put(self, arg0: int, arg1: 'ByteBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.ByteBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: 'ByteBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.ByteBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(arg0))

    @overload
    def put(self, arg0: 'FloatBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.FloatBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(arg0))

    @overload
    def put(self, arg0: int, arg1: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,long)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def get(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static long org.lwjgl.PointerBuffer.get(java.nio.ByteBuffer,int)"""
        return int.__wrap(__PointerBuffer.get(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.create(long,int)"""
        return PointerBuffer.__wrap(__PointerBuffer.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def putAddressOf(self, arg0: int, arg1: 'CustomBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.putAddressOf(int,org.lwjgl.system.CustomBuffer<?>)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).putAddressOf(__int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: 'Pointer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(org.lwjgl.system.Pointer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def getFloatBuffer(self, arg0: int) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.PointerBuffer.getFloatBuffer(int)"""
        return 'FloatBuffer'.__wrap(super(__PointerBuffer, self).getFloatBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def put(arg0: 'ByteBuffer', arg1: int):
        """public static void org.lwjgl.PointerBuffer.put(java.nio.ByteBuffer,long)"""
        __PointerBuffer.put(arg0, __long.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compareTo(self, arg0: 'PointerBuffer') -> int:
        """public int org.lwjgl.PointerBuffer.compareTo(org.lwjgl.PointerBuffer)"""
        return int.__wrap(super(__PointerBuffer, self).compareTo(arg0))

    @overload
    def getDoubleBuffer(self, arg0: int) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.PointerBuffer.getDoubleBuffer(int)"""
        return 'DoubleBuffer'.__wrap(super(__PointerBuffer, self).getDoubleBuffer(__int.valueOf(arg0)))

    @overload
    def getByteBuffer(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.PointerBuffer.getByteBuffer(int)"""
        return 'ByteBuffer'.__wrap(super(__PointerBuffer, self).getByteBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getStringASCII(self) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringASCII()"""
        return str.__wrap(super(PointerBuffer, self).getStringASCII())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def getStringUTF8(self, arg0: int) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF8(int)"""
        return str.__wrap(super(__PointerBuffer, self).getStringUTF8(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: int, arg1: 'FloatBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.FloatBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(long)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(__long.valueOf(arg0)))

    @overload
    def put(self, arg0: 'IntBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.IntBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(arg0))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def get(self, arg0: 'long') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.get(long[])"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).get(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.PointerBuffer.sizeof()"""
        return int.__wrap(super(PointerBuffer, self).sizeof())

    @overload
    def getShortBuffer(self, arg0: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.PointerBuffer.getShortBuffer(int)"""
        return 'ShortBuffer'.__wrap(super(__PointerBuffer, self).getShortBuffer(__int.valueOf(arg0)))

    @overload
    def getIntBuffer(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.PointerBuffer.getIntBuffer(int)"""
        return 'IntBuffer'.__wrap(super(__PointerBuffer, self).getIntBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def getLongBuffer(self, arg0: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.PointerBuffer.getLongBuffer(int)"""
        return 'LongBuffer'.__wrap(super(__PointerBuffer, self).getLongBuffer(__int.valueOf(arg0)))

    @overload
    def getIntBuffer(self, arg0: int, arg1: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.PointerBuffer.getIntBuffer(int,int)"""
        return 'IntBuffer'.__wrap(super(__PointerBuffer, self).getIntBuffer(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def getStringASCII(self, arg0: int) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringASCII(int)"""
        return str.__wrap(super(__PointerBuffer, self).getStringASCII(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.PointerBuffer.hashCode()"""
        return int.__wrap(super(PointerBuffer, self).hashCode())

    @overload
    def getPointerBuffer(self, arg0: int, arg1: int) -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.getPointerBuffer(int,int)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).getPointerBuffer(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def put(self, arg0: int, arg1: 'ShortBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.ShortBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def getShortBuffer(self, arg0: int, arg1: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.PointerBuffer.getShortBuffer(int,int)"""
        return 'ShortBuffer'.__wrap(super(__PointerBuffer, self).getShortBuffer(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def get(self, arg0: int) -> int:
        """public long org.lwjgl.PointerBuffer.get(int)"""
        return int.__wrap(super(__PointerBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def getDoubleBuffer(self, arg0: int, arg1: int) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.PointerBuffer.getDoubleBuffer(int,int)"""
        return 'DoubleBuffer'.__wrap(super(__PointerBuffer, self).getDoubleBuffer(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getStringUTF16(self, arg0: int) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF16(int)"""
        return str.__wrap(super(__PointerBuffer, self).getStringUTF16(__int.valueOf(arg0)))

    @overload
    def getLongBuffer(self, arg0: int, arg1: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.PointerBuffer.getLongBuffer(int,int)"""
        return 'LongBuffer'.__wrap(super(__PointerBuffer, self).getLongBuffer(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def putAddressOf(self, arg0: 'CustomBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.putAddressOf(org.lwjgl.system.CustomBuffer<?>)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).putAddressOf(arg0))

    @staticmethod
    @overload
    def get(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.PointerBuffer.get(java.nio.ByteBuffer)"""
        return int.__wrap(__PointerBuffer.get(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def put(self, arg0: 'ShortBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.ShortBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(arg0))

    @overload
    def put(self, arg0: int, arg1: 'DoubleBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(int,java.nio.DoubleBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.PointerBuffer.equals(java.lang.Object)"""
        return bool.__wrap(super(__PointerBuffer, self).equals(arg0))

    @overload
    def get(self) -> int:
        """public long org.lwjgl.PointerBuffer.get()"""
        return int.__wrap(super(PointerBuffer, self).get())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def getFloatBuffer(self, arg0: int, arg1: int) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.PointerBuffer.getFloatBuffer(int,int)"""
        return 'FloatBuffer'.__wrap(super(__PointerBuffer, self).getFloatBuffer(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getStringUTF16(self) -> str:
        """public java.lang.String org.lwjgl.PointerBuffer.getStringUTF16()"""
        return str.__wrap(super(PointerBuffer, self).getStringUTF16())

    @staticmethod
    @overload
    def allocateDirect(arg0: int) -> 'PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.allocateDirect(int)"""
        return PointerBuffer.__wrap(__PointerBuffer.allocateDirect(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'DoubleBuffer') -> 'PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.PointerBuffer.put(java.nio.DoubleBuffer)"""
        return 'PointerBuffer'.__wrap(super(__PointerBuffer, self).put(arg0))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.CLongBuffer
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.lwjgl.CLongBuffer as __CLongBuffer
__CLongBuffer = __CLongBuffer
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class CLongBuffer():
    """org.lwjgl.CLongBuffer"""
 
    @staticmethod
    def __wrap(java_value: __CLongBuffer) -> 'CLongBuffer':
        return CLongBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CLongBuffer):
        """
        Dynamic initializer for CLongBuffer.
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
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: 'long', arg1: int, arg2: int) -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.get(long[],int,int)"""
        return 'CLongBuffer'.__wrap(super(__CLongBuffer, self).get(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.create(long,int)"""
        return CLongBuffer.__wrap(__CLongBuffer.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @staticmethod
    @overload
    def allocateDirect(arg0: int) -> 'CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.allocateDirect(int)"""
        return CLongBuffer.__wrap(__CLongBuffer.allocateDirect(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def put(self, arg0: int) -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.put(long)"""
        return 'CLongBuffer'.__wrap(super(__CLongBuffer, self).put(__long.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.CLongBuffer.equals(java.lang.Object)"""
        return bool.__wrap(super(__CLongBuffer, self).equals(arg0))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.CLongBuffer.hashCode()"""
        return int.__wrap(super(CLongBuffer, self).hashCode())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @staticmethod
    @overload
    def get(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static long org.lwjgl.CLongBuffer.get(java.nio.ByteBuffer,int)"""
        return int.__wrap(__CLongBuffer.get(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'long') -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.put(long[])"""
        return 'CLongBuffer'.__wrap(super(__CLongBuffer, self).put(arg0))

    @overload
    def get(self, arg0: 'long') -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.get(long[])"""
        return 'CLongBuffer'.__wrap(super(__CLongBuffer, self).get(arg0))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.CLongBuffer.sizeof()"""
        return int.__wrap(super(CLongBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def put(arg0: 'ByteBuffer', arg1: int, arg2: int):
        """public static void org.lwjgl.CLongBuffer.put(java.nio.ByteBuffer,int,long)"""
        __CLongBuffer.put(arg0, __int.valueOf(arg1), __long.valueOf(arg2))

    @overload
    def put(self, arg0: int, arg1: int) -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.put(int,long)"""
        return 'CLongBuffer'.__wrap(super(__CLongBuffer, self).put(__int.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'CLongBuffer') -> int:
        """public int org.lwjgl.CLongBuffer.compareTo(org.lwjgl.CLongBuffer)"""
        return int.__wrap(super(__CLongBuffer, self).compareTo(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @staticmethod
    @overload
    def put(arg0: 'ByteBuffer', arg1: int):
        """public static void org.lwjgl.CLongBuffer.put(java.nio.ByteBuffer,long)"""
        __CLongBuffer.put(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'ByteBuffer') -> 'CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.create(java.nio.ByteBuffer)"""
        return CLongBuffer.__wrap(__CLongBuffer.create(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def get(self) -> int:
        """public long org.lwjgl.CLongBuffer.get()"""
        return int.__wrap(super(CLongBuffer, self).get())

    @staticmethod
    @overload
    def get(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.CLongBuffer.get(java.nio.ByteBuffer)"""
        return int.__wrap(__CLongBuffer.get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def put(self, arg0: 'long', arg1: int, arg2: int) -> 'CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.CLongBuffer.put(long[],int,int)"""
        return 'CLongBuffer'.__wrap(super(__CLongBuffer, self).put(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def get(self, arg0: int) -> int:
        """public long org.lwjgl.CLongBuffer.get(int)"""
        return int.__wrap(super(__CLongBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.Version$BuildType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import org.lwjgl.Version as __Version_BuildType
__BuildType = __Version_BuildType.BuildType
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class BuildType():
    """org.lwjgl.Version.BuildType"""
 
    @staticmethod
    def __wrap(java_value: __BuildType) -> 'BuildType':
        return BuildType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BuildType):
        """
        Dynamic initializer for BuildType.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def values() -> List['BuildType']:
        """public static org.lwjgl.Version$BuildType[] org.lwjgl.Version$BuildType.values()"""
        return List[BuildType].__wrap(__BuildType.values())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BuildType':
        """public static org.lwjgl.Version$BuildType org.lwjgl.Version$BuildType.valueOf(java.lang.String)"""
        return BuildType.__wrap(__BuildType.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: org.lwjgl.BufferUtils
from pyquantum_helper import import_once as __import_once__
import java.nio.IntBuffer as IntBuffer
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import org.lwjgl.BufferUtils as __BufferUtils
__BufferUtils = __BufferUtils
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.CLongBuffer as __CLongBuffer
__CLongBuffer = __CLongBuffer
import java.nio.CharBuffer as CharBuffer
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import bool
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
import java.nio.LongBuffer as LongBuffer
import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.nio.DoubleBuffer as __DoubleBuffer
__DoubleBuffer = __DoubleBuffer
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
import java.nio.CharBuffer as __CharBuffer
__CharBuffer = __CharBuffer
from builtins import int
 
class BufferUtils():
    """org.lwjgl.BufferUtils"""
 
    @staticmethod
    def __wrap(java_value: __BufferUtils) -> 'BufferUtils':
        return BufferUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BufferUtils):
        """
        Dynamic initializer for BufferUtils.
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
    def zeroBuffer(arg0: 'FloatBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.FloatBuffer)"""
        __BufferUtils.zeroBuffer(arg0)

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'CharBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.CharBuffer)"""
        __BufferUtils.zeroBuffer(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createShortBuffer(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.BufferUtils.createShortBuffer(int)"""
        return ShortBuffer.__wrap(__BufferUtils.createShortBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createCLongBuffer(arg0: int) -> 'CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.BufferUtils.createCLongBuffer(int)"""
        return CLongBuffer.__wrap(__BufferUtils.createCLongBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'CustomBuffer'):
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> void org.lwjgl.BufferUtils.zeroBuffer(T)"""
        __BufferUtils.zeroBuffer(arg0)

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'IntBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.IntBuffer)"""
        __BufferUtils.zeroBuffer(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'ShortBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.ShortBuffer)"""
        __BufferUtils.zeroBuffer(arg0)

    @staticmethod
    @overload
    def createLongBuffer(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.BufferUtils.createLongBuffer(int)"""
        return LongBuffer.__wrap(__BufferUtils.createLongBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createCharBuffer(arg0: int) -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.BufferUtils.createCharBuffer(int)"""
        return CharBuffer.__wrap(__BufferUtils.createCharBuffer(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def createDoubleBuffer(arg0: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.BufferUtils.createDoubleBuffer(int)"""
        return DoubleBuffer.__wrap(__BufferUtils.createDoubleBuffer(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.ByteBuffer)"""
        __BufferUtils.zeroBuffer(arg0)

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'LongBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.LongBuffer)"""
        __BufferUtils.zeroBuffer(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def createPointerBuffer(arg0: int) -> 'PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.BufferUtils.createPointerBuffer(int)"""
        return PointerBuffer.__wrap(__BufferUtils.createPointerBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createFloatBuffer(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.BufferUtils.createFloatBuffer(int)"""
        return FloatBuffer.__wrap(__BufferUtils.createFloatBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def zeroBuffer(arg0: 'DoubleBuffer'):
        """public static void org.lwjgl.BufferUtils.zeroBuffer(java.nio.DoubleBuffer)"""
        __BufferUtils.zeroBuffer(arg0)

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createByteBuffer(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.BufferUtils.createByteBuffer(int)"""
        return ByteBuffer.__wrap(__BufferUtils.createByteBuffer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createIntBuffer(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.BufferUtils.createIntBuffer(int)"""
        return IntBuffer.__wrap(__BufferUtils.createIntBuffer(__int.valueOf(arg0)))