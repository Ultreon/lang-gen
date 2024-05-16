from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
import java.lang.Short as _short
import java.util.function.Consumer as Consumer
import org.lwjgl.system.libffi.FFIType as _FFIType_Buffer
_Buffer = _FFIType_Buffer.Buffer
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
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
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
    """org.lwjgl.system.libffi.FFIType.Buffer"""
 
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

    @overload
    def alignment(self) -> int:
        """public short org.lwjgl.system.libffi.FFIType$Buffer.alignment()"""
        return int._wrap(super(Buffer, self).alignment())

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

    @overload
    def size(self) -> int:
        """public long org.lwjgl.system.libffi.FFIType$Buffer.size()"""
        return int._wrap(super(Buffer, self).size())

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
    def alignment(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.alignment(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).alignment(_short.valueOf(arg0)))

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

    @overload
    def elements(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFIType$Buffer.elements(int)"""
        return 'pygl.PointerBuffer'._wrap(super(_Buffer, self).elements(_int.valueOf(arg0)))

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

    @overload
    def elements(self, arg0: 'PointerBuffer') -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.elements(org.lwjgl.PointerBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).elements(arg0))

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFIType$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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

    @overload
    def type(self) -> int:
        """public short org.lwjgl.system.libffi.FFIType$Buffer.type()"""
        return int._wrap(super(Buffer, self).type())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def type(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.type(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).type(_short.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.libffi.FFIType$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def size(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.size(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).size(_long.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0))

 
 
 
# CLASS: org.lwjgl.system.libffi.FFIType$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
import java.lang.Short as _short
import java.util.function.Consumer as Consumer
import org.lwjgl.system.libffi.FFIType as _FFIType_Buffer
_Buffer = _FFIType_Buffer.Buffer
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
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
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
    """org.lwjgl.system.libffi.FFIType.Buffer"""
 
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

    @overload
    def alignment(self) -> int:
        """public short org.lwjgl.system.libffi.FFIType$Buffer.alignment()"""
        return int._wrap(super(Buffer, self).alignment())

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

    @overload
    def size(self) -> int:
        """public long org.lwjgl.system.libffi.FFIType$Buffer.size()"""
        return int._wrap(super(Buffer, self).size())

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
    def alignment(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.alignment(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).alignment(_short.valueOf(arg0)))

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

    @overload
    def elements(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFIType$Buffer.elements(int)"""
        return 'pygl.PointerBuffer'._wrap(super(_Buffer, self).elements(_int.valueOf(arg0)))

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

    @overload
    def elements(self, arg0: 'PointerBuffer') -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.elements(org.lwjgl.PointerBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).elements(arg0))

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFIType$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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

    @overload
    def type(self) -> int:
        """public short org.lwjgl.system.libffi.FFIType$Buffer.type()"""
        return int._wrap(super(Buffer, self).type())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def type(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.type(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).type(_short.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.libffi.FFIType$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def size(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.size(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).size(_long.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0))

 
 
 
# CLASS: org.lwjgl.system.libffi.FFIType$Buffer 
 
 
# CLASS: org.lwjgl.system.libffi.FFIClosure
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.system.libffi.FFIClosure as _FFIClosure
_FFIClosure = _FFIClosure
from pyquantum_helper import override
import org.lwjgl.system.libffi.FFIClosure as _FFIClosure_Buffer
_Buffer = _FFIClosure_Buffer.Buffer
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FFIClosure():
    """org.lwjgl.system.libffi.FFIClosure"""
 
    @staticmethod
    def _wrap(java_value: _FFIClosure) -> 'FFIClosure':
        return FFIClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FFIClosure):
        """
        Dynamic initializer for FFIClosure.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FFIClosure__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FFIClosure__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def cif(self) -> 'FFICIF':
        """public org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFIClosure.cif()"""
        return 'FFICIF'._wrap(super(FFIClosure, self).cif())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.calloc(int)"""
        return Buffer._wrap(_FFIClosure.calloc(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFIClosure(java.nio.ByteBuffer)"""
        val = _FFIClosure(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def nfun(arg0: int) -> int:
        """public static long org.lwjgl.system.libffi.FFIClosure.nfun(long)"""
        return int._wrap(_FFIClosure.nfun(_long.valueOf(arg0)))

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
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.create(int)"""
        return Buffer._wrap(_FFIClosure.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncif(arg0: int) -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFIClosure.ncif(long)"""
        return FFICIF._wrap(_FFIClosure.ncif(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.create()"""
        return FFIClosure._wrap(_FFIClosure.create())

    @staticmethod
    @overload
    def calloc() -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.calloc()"""
        return FFIClosure._wrap(_FFIClosure.calloc())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.create(long,int)"""
        return Buffer._wrap(_FFIClosure.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.malloc(org.lwjgl.system.MemoryStack)"""
        return FFIClosure._wrap(_FFIClosure.malloc(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.libffi.FFIClosure.sizeof()"""
        return int._wrap(super(FFIClosure, self).sizeof())

    @staticmethod
    @overload
    def nuser_data(arg0: int) -> int:
        """public static long org.lwjgl.system.libffi.FFIClosure.nuser_data(long)"""
        return int._wrap(_FFIClosure.nuser_data(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.createSafe(long)"""
        return FFIClosure._wrap(_FFIClosure.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

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
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_FFIClosure.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.malloc(int)"""
        return Buffer._wrap(_FFIClosure.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.malloc()"""
        return FFIClosure._wrap(_FFIClosure.malloc())

    @staticmethod
    @overload
    def create(arg0: int) -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.create(long)"""
        return FFIClosure._wrap(_FFIClosure.create(_long.valueOf(arg0)))

    @overload
    def fun(self) -> int:
        """public long org.lwjgl.system.libffi.FFIClosure.fun()"""
        return int._wrap(super(FFIClosure, self).fun())

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
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.createSafe(long,int)"""
        return Buffer._wrap(_FFIClosure.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

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

    @overload
    def user_data(self) -> int:
        """public long org.lwjgl.system.libffi.FFIClosure.user_data()"""
        return int._wrap(super(FFIClosure, self).user_data())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_FFIClosure.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.calloc(org.lwjgl.system.MemoryStack)"""
        return FFIClosure._wrap(_FFIClosure.calloc(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address()) 
 
 
# CLASS: org.lwjgl.system.libffi.LibFFI
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.system.libffi.FFIClosure as _FFIClosure
_FFIClosure = _FFIClosure
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.libffi.LibFFI as _LibFFI
_LibFFI = _LibFFI
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibFFI():
    """org.lwjgl.system.libffi.LibFFI"""
 
    @staticmethod
    def _wrap(java_value: _LibFFI) -> 'LibFFI':
        return LibFFI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibFFI):
        """
        Dynamic initializer for LibFFI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibFFI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibFFI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ffi_prep_cif_var(arg0: 'FFICIF', arg1: int, arg2: int, arg3: 'FFIType', arg4: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_prep_cif_var(org.lwjgl.system.libffi.FFICIF,int,int,org.lwjgl.system.libffi.FFIType,org.lwjgl.PointerBuffer)"""
        return int._wrap(_LibFFI.ffi_prep_cif_var(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4))

    @staticmethod
    @overload
    def nffi_prep_cif_var(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_prep_cif_var(long,int,int,int,long,long)"""
        return int._wrap(_LibFFI.nffi_prep_cif_var(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def nffi_closure_free(arg0: int):
        """public static native void org.lwjgl.system.libffi.LibFFI.nffi_closure_free(long)"""
        _LibFFI.nffi_closure_free(_long.valueOf(arg0))

    @staticmethod
    @overload
    def ffi_closure_alloc(arg0: int, arg1: 'PointerBuffer') -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.LibFFI.ffi_closure_alloc(long,org.lwjgl.PointerBuffer)"""
        return FFIClosure._wrap(_LibFFI.ffi_closure_alloc(_long.valueOf(arg0), arg1))

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
    def ffi_get_struct_offsets(arg0: int, arg1: 'FFIType', arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_get_struct_offsets(int,org.lwjgl.system.libffi.FFIType,org.lwjgl.PointerBuffer)"""
        return int._wrap(_LibFFI.ffi_get_struct_offsets(_int.valueOf(arg0), arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nffi_get_struct_offsets(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_get_struct_offsets(int,long,long)"""
        return int._wrap(_LibFFI.nffi_get_struct_offsets(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nffi_prep_closure_loc(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_prep_closure_loc(long,long,long,long,long)"""
        return int._wrap(_LibFFI.nffi_prep_closure_loc(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def ffi_prep_closure_loc(arg0: 'FFIClosure', arg1: 'FFICIF', arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_prep_closure_loc(org.lwjgl.system.libffi.FFIClosure,org.lwjgl.system.libffi.FFICIF,long,long,long)"""
        return int._wrap(_LibFFI.ffi_prep_closure_loc(arg0, arg1, _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nffi_call(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.libffi.LibFFI.nffi_call(long,long,long,long)"""
        _LibFFI.nffi_call(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nffi_closure_alloc(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.libffi.LibFFI.nffi_closure_alloc(long,long)"""
        return int._wrap(_LibFFI.nffi_closure_alloc(_long.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def ffi_call(arg0: 'FFICIF', arg1: int, arg2: 'ByteBuffer', arg3: 'PointerBuffer'):
        """public static void org.lwjgl.system.libffi.LibFFI.ffi_call(org.lwjgl.system.libffi.FFICIF,long,java.nio.ByteBuffer,org.lwjgl.PointerBuffer)"""
        _LibFFI.ffi_call(arg0, _long.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def ffi_prep_cif(arg0: 'FFICIF', arg1: int, arg2: 'FFIType', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_prep_cif(org.lwjgl.system.libffi.FFICIF,int,org.lwjgl.system.libffi.FFIType,org.lwjgl.PointerBuffer)"""
        return int._wrap(_LibFFI.ffi_prep_cif(arg0, _int.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ffi_closure_free(arg0: 'FFIClosure'):
        """public static void org.lwjgl.system.libffi.LibFFI.ffi_closure_free(org.lwjgl.system.libffi.FFIClosure)"""
        _LibFFI.ffi_closure_free(arg0)

    @staticmethod
    @overload
    def nffi_prep_cif(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_prep_cif(long,int,int,long,long)"""
        return int._wrap(_LibFFI.nffi_prep_cif(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.libffi.FFIType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.system.libffi.FFIType as _FFIType
_FFIType = _FFIType
import java.lang.Short as _short
import org.lwjgl.system.libffi.FFIType as _FFIType_Buffer
_Buffer = _FFIType_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FFIType():
    """org.lwjgl.system.libffi.FFIType"""
 
    @staticmethod
    def _wrap(java_value: _FFIType) -> 'FFIType':
        return FFIType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FFIType):
        """
        Dynamic initializer for FFIType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FFIType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FFIType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_FFIType.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.malloc(int)"""
        return Buffer._wrap(_FFIType.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.create(long)"""
        return FFIType._wrap(_FFIType.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.malloc()"""
        return FFIType._wrap(_FFIType.malloc())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def alignment(self, arg0: int) -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.alignment(short)"""
        return 'FFIType'._wrap(super(_FFIType, self).alignment(_short.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: 'FFIType') -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.set(org.lwjgl.system.libffi.FFIType)"""
        return 'FFIType'._wrap(super(_FFIType, self).set(arg0))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.malloc(org.lwjgl.system.MemoryStack)"""
        return FFIType._wrap(_FFIType.malloc(arg0))

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
    def nsize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.libffi.FFIType.nsize(long,long)"""
        _FFIType.nsize(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def ntype(arg0: int, arg1: int):
        """public static void org.lwjgl.system.libffi.FFIType.ntype(long,short)"""
        _FFIType.ntype(_long.valueOf(arg0), _short.valueOf(arg1))

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

    @overload
    def type(self) -> int:
        """public short org.lwjgl.system.libffi.FFIType.type()"""
        return int._wrap(super(FFIType, self).type())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFIType(java.nio.ByteBuffer)"""
        val = _FFIType(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def ntype(arg0: int) -> int:
        """public static short org.lwjgl.system.libffi.FFIType.ntype(long)"""
        return int._wrap(_FFIType.ntype(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.create(int)"""
        return Buffer._wrap(_FFIType.create(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def calloc() -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.calloc()"""
        return FFIType._wrap(_FFIType.calloc())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.calloc(org.lwjgl.system.MemoryStack)"""
        return FFIType._wrap(_FFIType.calloc(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.libffi.FFIType.sizeof()"""
        return int._wrap(super(FFIType, self).sizeof())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.calloc(int)"""
        return Buffer._wrap(_FFIType.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nelements(arg0: int, arg1: 'PointerBuffer'):
        """public static void org.lwjgl.system.libffi.FFIType.nelements(long,org.lwjgl.PointerBuffer)"""
        _FFIType.nelements(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nsize(arg0: int) -> int:
        """public static long org.lwjgl.system.libffi.FFIType.nsize(long)"""
        return int._wrap(_FFIType.nsize(_long.valueOf(arg0)))

    @overload
    def type(self, arg0: int) -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.type(short)"""
        return 'FFIType'._wrap(super(_FFIType, self).type(_short.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'PointerBuffer') -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.set(long,short,short,org.lwjgl.PointerBuffer)"""
        return 'FFIType'._wrap(super(_FFIType, self).set(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), arg3))

    @overload
    def size(self, arg0: int) -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.size(long)"""
        return 'FFIType'._wrap(super(_FFIType, self).size(_long.valueOf(arg0)))

    @overload
    def alignment(self) -> int:
        """public short org.lwjgl.system.libffi.FFIType.alignment()"""
        return int._wrap(super(FFIType, self).alignment())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.createSafe(long)"""
        return FFIType._wrap(_FFIType.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_FFIType.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.create(long,int)"""
        return Buffer._wrap(_FFIType.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create() -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.create()"""
        return FFIType._wrap(_FFIType.create())

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

    @staticmethod
    @overload
    def nalignment(arg0: int) -> int:
        """public static short org.lwjgl.system.libffi.FFIType.nalignment(long)"""
        return int._wrap(_FFIType.nalignment(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nalignment(arg0: int, arg1: int):
        """public static void org.lwjgl.system.libffi.FFIType.nalignment(long,short)"""
        _FFIType.nalignment(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.createSafe(long,int)"""
        return Buffer._wrap(_FFIType.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def size(self) -> int:
        """public long org.lwjgl.system.libffi.FFIType.size()"""
        return int._wrap(super(FFIType, self).size())

    @overload
    def elements(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFIType.elements(int)"""
        return 'pygl.PointerBuffer'._wrap(super(_FFIType, self).elements(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nelements(arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFIType.nelements(long,int)"""
        return pygl.PointerBuffer._wrap(_FFIType.nelements(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def elements(self, arg0: 'PointerBuffer') -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.elements(org.lwjgl.PointerBuffer)"""
        return 'FFIType'._wrap(super(_FFIType, self).elements(arg0)) 
 
 
# CLASS: org.lwjgl.system.libffi.FFICIF$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
import org.lwjgl.system.libffi.FFIType as _FFIType
_FFIType = _FFIType
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
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import org.lwjgl.system.libffi.FFICIF as _FFICIF_Buffer
_Buffer = _FFICIF_Buffer.Buffer
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
    """org.lwjgl.system.libffi.FFICIF.Buffer"""
 
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
    def bytes(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF$Buffer.bytes()"""
        return int._wrap(super(Buffer, self).bytes())

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

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.libffi.FFICIF$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF$Buffer.flags()"""
        return int._wrap(super(Buffer, self).flags())

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

    @overload
    def rtype(self) -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFICIF$Buffer.rtype()"""
        return 'FFIType'._wrap(super(Buffer, self).rtype())

    @overload
    def arg_types(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFICIF$Buffer.arg_types(int)"""
        return 'pygl.PointerBuffer'._wrap(super(_Buffer, self).arg_types(_int.valueOf(arg0)))

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

    @overload
    def nargs(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF$Buffer.nargs()"""
        return int._wrap(super(Buffer, self).nargs())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFICIF$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def abi(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF$Buffer.abi()"""
        return int._wrap(super(Buffer, self).abi())

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
 
 
# CLASS: org.lwjgl.system.libffi.FFIClosure$Buffer
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
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import org.lwjgl.system.libffi.FFIClosure as _FFIClosure_Buffer
_Buffer = _FFIClosure_Buffer.Buffer
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
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
    """org.lwjgl.system.libffi.FFIClosure.Buffer"""
 
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

    @overload
    def cif(self) -> 'FFICIF':
        """public org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFIClosure$Buffer.cif()"""
        return 'FFICIF'._wrap(super(Buffer, self).cif())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.libffi.FFIClosure$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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

    @overload
    def fun(self) -> int:
        """public long org.lwjgl.system.libffi.FFIClosure$Buffer.fun()"""
        return int._wrap(super(Buffer, self).fun())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFIClosure$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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

    @overload
    def user_data(self) -> int:
        """public long org.lwjgl.system.libffi.FFIClosure$Buffer.user_data()"""
        return int._wrap(super(Buffer, self).user_data())

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

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.libffi.FFICIF
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.system.libffi.FFIType as _FFIType
_FFIType = _FFIType
import org.lwjgl.system.libffi.FFICIF as _FFICIF_Buffer
_Buffer = _FFICIF_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FFICIF():
    """org.lwjgl.system.libffi.FFICIF"""
 
    @staticmethod
    def _wrap(java_value: _FFICIF) -> 'FFICIF':
        return FFICIF(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FFICIF):
        """
        Dynamic initializer for FFICIF.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FFICIF__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FFICIF__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nrtype(arg0: int) -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFICIF.nrtype(long)"""
        return FFIType._wrap(_FFICIF.nrtype(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.calloc(int)"""
        return Buffer._wrap(_FFICIF.calloc(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFICIF(java.nio.ByteBuffer)"""
        val = _FFICIF(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def nbytes(arg0: int) -> int:
        """public static int org.lwjgl.system.libffi.FFICIF.nbytes(long)"""
        return int._wrap(_FFICIF.nbytes(_long.valueOf(arg0)))

    @overload
    def rtype(self) -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFICIF.rtype()"""
        return 'FFIType'._wrap(super(FFICIF, self).rtype())

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
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.create(long,int)"""
        return Buffer._wrap(_FFICIF.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.calloc(org.lwjgl.system.MemoryStack)"""
        return FFICIF._wrap(_FFICIF.calloc(arg0))

    @staticmethod
    @overload
    def calloc() -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.calloc()"""
        return FFICIF._wrap(_FFICIF.calloc())

    @staticmethod
    @overload
    def narg_types(arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFICIF.narg_types(long,int)"""
        return pygl.PointerBuffer._wrap(_FFICIF.narg_types(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_FFICIF.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.libffi.FFICIF.nflags(long)"""
        return int._wrap(_FFICIF.nflags(_long.valueOf(arg0)))

    @overload
    def nargs(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF.nargs()"""
        return int._wrap(super(FFICIF, self).nargs())

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
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.createSafe(long,int)"""
        return Buffer._wrap(_FFICIF.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def bytes(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF.bytes()"""
        return int._wrap(super(FFICIF, self).bytes())

    @staticmethod
    @overload
    def create(arg0: int) -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.create(long)"""
        return FFICIF._wrap(_FFICIF.create(_long.valueOf(arg0)))

    @overload
    def abi(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF.abi()"""
        return int._wrap(super(FFICIF, self).abi())

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF.flags()"""
        return int._wrap(super(FFICIF, self).flags())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.malloc(int)"""
        return Buffer._wrap(_FFICIF.malloc(_int.valueOf(arg0)))

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
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.createSafe(long)"""
        return FFICIF._wrap(_FFICIF.createSafe(_long.valueOf(arg0)))

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

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF.sizeof()"""
        return int._wrap(super(FFICIF, self).sizeof())

    @staticmethod
    @overload
    def nnargs(arg0: int) -> int:
        """public static int org.lwjgl.system.libffi.FFICIF.nnargs(long)"""
        return int._wrap(_FFICIF.nnargs(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.create(int)"""
        return Buffer._wrap(_FFICIF.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.create()"""
        return FFICIF._wrap(_FFICIF.create())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.malloc(org.lwjgl.system.MemoryStack)"""
        return FFICIF._wrap(_FFICIF.malloc(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def arg_types(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFICIF.arg_types(int)"""
        return 'pygl.PointerBuffer'._wrap(super(_FFICIF, self).arg_types(_int.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_FFICIF.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc() -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.malloc()"""
        return FFICIF._wrap(_FFICIF.malloc())

    @staticmethod
    @overload
    def nabi(arg0: int) -> int:
        """public static int org.lwjgl.system.libffi.FFICIF.nabi(long)"""
        return int._wrap(_FFICIF.nabi(_long.valueOf(arg0)))

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