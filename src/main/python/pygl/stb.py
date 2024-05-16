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
import org.lwjgl.stb.STBTTPackContext as _STBTTPackContext_Buffer
_Buffer = _STBTTPackContext_Buffer.Buffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.stb.STBRPContext as _STBRPContext
_STBRPContext = _STBRPContext
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
import org.lwjgl.stb.STBRPNode as _STBRPNode_Buffer
_Buffer = _STBRPNode_Buffer.Buffer
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
    """org.lwjgl.stb.STBTTPackContext.Buffer"""
 
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
    def skip_missing(self) -> bool:
        """public boolean org.lwjgl.stb.STBTTPackContext$Buffer.skip_missing()"""
        return bool._wrap(super(Buffer, self).skip_missing())

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
    def height(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.height()"""
        return int._wrap(super(Buffer, self).height())

    @overload
    def pack_info(self) -> 'STBRPContext':
        """public org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBTTPackContext$Buffer.pack_info()"""
        return 'STBRPContext'._wrap(super(Buffer, self).pack_info())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackContext$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def width(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.width()"""
        return int._wrap(super(Buffer, self).width())

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
    def padding(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.padding()"""
        return int._wrap(super(Buffer, self).padding())

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
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBTTPackContext$Buffer.pixels(int)"""
        return 'ByteBuffer'._wrap(super(_Buffer, self).pixels(_int.valueOf(arg0)))

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
    def stride_in_bytes(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.stride_in_bytes()"""
        return int._wrap(super(Buffer, self).stride_in_bytes())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def user_allocator_context(self) -> int:
        """public long org.lwjgl.stb.STBTTPackContext$Buffer.user_allocator_context()"""
        return int._wrap(super(Buffer, self).user_allocator_context())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTPackContext$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
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
    def h_oversample(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.h_oversample()"""
        return int._wrap(super(Buffer, self).h_oversample())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def v_oversample(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.v_oversample()"""
        return int._wrap(super(Buffer, self).v_oversample())

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
    def nodes(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBTTPackContext$Buffer.nodes(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).nodes(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0))

 
 
 
# CLASS: org.lwjgl.stb.STBTTPackContext$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.stb.STBTTPackContext as _STBTTPackContext_Buffer
_Buffer = _STBTTPackContext_Buffer.Buffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.stb.STBRPContext as _STBRPContext
_STBRPContext = _STBRPContext
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
import org.lwjgl.stb.STBRPNode as _STBRPNode_Buffer
_Buffer = _STBRPNode_Buffer.Buffer
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
    """org.lwjgl.stb.STBTTPackContext.Buffer"""
 
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
    def skip_missing(self) -> bool:
        """public boolean org.lwjgl.stb.STBTTPackContext$Buffer.skip_missing()"""
        return bool._wrap(super(Buffer, self).skip_missing())

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
    def height(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.height()"""
        return int._wrap(super(Buffer, self).height())

    @overload
    def pack_info(self) -> 'STBRPContext':
        """public org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBTTPackContext$Buffer.pack_info()"""
        return 'STBRPContext'._wrap(super(Buffer, self).pack_info())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackContext$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def width(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.width()"""
        return int._wrap(super(Buffer, self).width())

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
    def padding(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.padding()"""
        return int._wrap(super(Buffer, self).padding())

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
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBTTPackContext$Buffer.pixels(int)"""
        return 'ByteBuffer'._wrap(super(_Buffer, self).pixels(_int.valueOf(arg0)))

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
    def stride_in_bytes(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.stride_in_bytes()"""
        return int._wrap(super(Buffer, self).stride_in_bytes())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def user_allocator_context(self) -> int:
        """public long org.lwjgl.stb.STBTTPackContext$Buffer.user_allocator_context()"""
        return int._wrap(super(Buffer, self).user_allocator_context())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTPackContext$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
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
    def h_oversample(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.h_oversample()"""
        return int._wrap(super(Buffer, self).h_oversample())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def v_oversample(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.v_oversample()"""
        return int._wrap(super(Buffer, self).v_oversample())

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
    def nodes(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBTTPackContext$Buffer.nodes(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).nodes(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0))

 
 
 
# CLASS: org.lwjgl.stb.STBTTPackContext$Buffer 
 
 
# CLASS: org.lwjgl.stb.STBVorbisInfo$Buffer
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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import org.lwjgl.stb.STBVorbisInfo as _STBVorbisInfo_Buffer
_Buffer = _STBVorbisInfo_Buffer.Buffer
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
    """org.lwjgl.stb.STBVorbisInfo.Buffer"""
 
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
    def sample_rate(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.sample_rate()"""
        return int._wrap(super(Buffer, self).sample_rate())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBVorbisInfo$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).limit(_int.valueOf(arg0)))

    @overload
    def temp_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.temp_memory_required()"""
        return int._wrap(super(Buffer, self).temp_memory_required())

    @overload
    def channels(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.channels()"""
        return int._wrap(super(Buffer, self).channels())

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

    @overload
    def setup_temp_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.setup_temp_memory_required()"""
        return int._wrap(super(Buffer, self).setup_temp_memory_required())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisInfo$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def setup_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.setup_memory_required()"""
        return int._wrap(super(Buffer, self).setup_memory_required())

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
    def max_frame_size(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.max_frame_size()"""
        return int._wrap(super(Buffer, self).max_frame_size())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBISkipCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.stb.STBISkipCallbackI as _STBISkipCallbackI
_STBISkipCallbackI = _STBISkipCallbackI
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

import org.lwjgl.stb.STBISkipCallback as _STBISkipCallback
_STBISkipCallback = _STBISkipCallback
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
 
class STBISkipCallback():
    """org.lwjgl.stb.STBISkipCallback"""
 
    @staticmethod
    def _wrap(java_value: _STBISkipCallback) -> 'STBISkipCallback':
        return STBISkipCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBISkipCallback):
        """
        Dynamic initializer for STBISkipCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBISkipCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBISkipCallback__wrapper":
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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBISkipCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(STBISkipCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBISkipCallback':
        """public static org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBISkipCallback.createSafe(long)"""
        return STBISkipCallback._wrap(_STBISkipCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def create(arg0: 'STBISkipCallbackI') -> 'STBISkipCallback':
        """public static org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBISkipCallback.create(org.lwjgl.stb.STBISkipCallbackI)"""
        return STBISkipCallback._wrap(_STBISkipCallback.create(arg0))

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.stb.STBISkipCallbackI.invoke(long,int)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBISkipCallbackI.callback(long,long)"""
        super(_STBISkipCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBISkipCallback':
        """public static org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBISkipCallback.create(long)"""
        return STBISkipCallback._wrap(_STBISkipCallback.create(_long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.stb.STBTTBakedChar$Buffer
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
import org.lwjgl.stb.STBTTBakedChar as _STBTTBakedChar_Buffer
_Buffer = _STBTTBakedChar_Buffer.Buffer
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
    """org.lwjgl.stb.STBTTBakedChar.Buffer"""
 
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
    def y1(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar$Buffer.y1()"""
        return int._wrap(super(Buffer, self).y1())

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
    def xadvance(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar$Buffer.xadvance()"""
        return float._wrap(super(Buffer, self).xadvance())

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

    @overload
    def xoff(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar$Buffer.xoff()"""
        return float._wrap(super(Buffer, self).xoff())

    @overload
    def y0(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar$Buffer.y0()"""
        return int._wrap(super(Buffer, self).y0())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTBakedChar$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTBakedChar$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def x0(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar$Buffer.x0()"""
        return int._wrap(super(Buffer, self).x0())

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
    def yoff(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar$Buffer.yoff()"""
        return float._wrap(super(Buffer, self).yoff())

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

    @overload
    def x1(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar$Buffer.x1()"""
        return int._wrap(super(Buffer, self).x1())

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
 
 
# CLASS: org.lwjgl.stb.STBIReadCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.stb.STBIReadCallbackI as _STBIReadCallbackI
_STBIReadCallbackI = _STBIReadCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class STBIReadCallbackI():
    """org.lwjgl.stb.STBIReadCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _STBIReadCallbackI) -> 'STBIReadCallbackI':
        return STBIReadCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBIReadCallbackI):
        """
        Dynamic initializer for STBIReadCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBIReadCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBIReadCallbackI__wrapper":
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
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIReadCallbackI.callback(long,long)"""
        super(_STBIReadCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIReadCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(STBIReadCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract int org.lwjgl.stb.STBIReadCallbackI.invoke(long,long,int)"""
        pass 
 
 
# CLASS: org.lwjgl.stb.STBRPNode$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.stb.STBRPNode as _STBRPNode
_STBRPNode = _STBRPNode
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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBRPNode as _STBRPNode_Buffer
_Buffer = _STBRPNode_Buffer.Buffer
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
    """org.lwjgl.stb.STBRPNode.Buffer"""
 
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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPNode$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def x(self) -> int:
        """public int org.lwjgl.stb.STBRPNode$Buffer.x()"""
        return int._wrap(super(Buffer, self).x())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBRPNode$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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

    @overload
    def next(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode$Buffer.next()"""
        return 'STBRPNode'._wrap(super(Buffer, self).next())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def y(self) -> int:
        """public int org.lwjgl.stb.STBRPNode$Buffer.y()"""
        return int._wrap(super(Buffer, self).y())

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

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBVorbis
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.CharSequence as CharSequence
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
import org.lwjgl.stb.STBVorbisComment as _STBVorbisComment
_STBVorbisComment = _STBVorbisComment
from builtins import float
import org.lwjgl.stb.STBVorbis as _STBVorbis
_STBVorbis = _STBVorbis
import java.nio.ShortBuffer as ShortBuffer
import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBVorbisInfo as _STBVorbisInfo
_STBVorbisInfo = _STBVorbisInfo
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBVorbis():
    """org.lwjgl.stb.STBVorbis"""
 
    @staticmethod
    def _wrap(java_value: _STBVorbis) -> 'STBVorbis':
        return STBVorbis(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBVorbis):
        """
        Dynamic initializer for STBVorbis.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBVorbis__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBVorbis__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def stb_vorbis_decode_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_decode_memory(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstb_vorbis_open_filename(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_filename(long,int[],long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_open_filename(_long.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstb_vorbis_seek_frame(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_seek_frame(long,int)"""
        return int._wrap(_STBVorbis.nstb_vorbis_seek_frame(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'CharSequence', arg1: 'int', arg2: 'int', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.lang.CharSequence,int[],int[],org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_float(arg0: int, arg1: 'PointerBuffer', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_float(long,org.lwjgl.PointerBuffer,int)"""
        return int._wrap(_STBVorbis.stb_vorbis_get_samples_float(_long.valueOf(arg0), arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstb_vorbis_decode_frame_pushdata(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_frame_pushdata(long,long,int,long,long,long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_decode_frame_pushdata(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def nstb_vorbis_decode_frame_pushdata(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: 'int') -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_frame_pushdata(long,long,int,int[],long,int[])"""
        return int._wrap(_STBVorbis.nstb_vorbis_decode_frame_pushdata(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def nstb_vorbis_flush_pushdata(arg0: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_flush_pushdata(long)"""
        _STBVorbis.nstb_vorbis_flush_pushdata(_long.valueOf(arg0))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.nio.ByteBuffer,int[],int[],org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nstb_vorbis_get_comment(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_get_comment(long,long)"""
        _STBVorbis.nstb_vorbis_get_comment(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.nio.ByteBuffer,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int._wrap(_STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_float_interleaved(long,int,long,int)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_samples_float_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def stb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: 'FloatBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_float_interleaved(long,int,java.nio.FloatBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_get_samples_float_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nstb_vorbis_stream_length_in_seconds(arg0: int) -> float:
        """public static native float org.lwjgl.stb.STBVorbis.nstb_vorbis_stream_length_in_seconds(long)"""
        return float._wrap(_STBVorbis.nstb_vorbis_stream_length_in_seconds(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.lang.CharSequence,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int._wrap(_STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: 'float', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_float_interleaved(long,int,float[],int)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_samples_float_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: 'short') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_short_interleaved(long,int,short[])"""
        return int._wrap(_STBVorbis.stb_vorbis_get_samples_short_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def stb_vorbis_get_file_offset(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_file_offset(long)"""
        return int._wrap(_STBVorbis.stb_vorbis_get_file_offset(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_flush_pushdata(arg0: int):
        """public static void org.lwjgl.stb.STBVorbis.stb_vorbis_flush_pushdata(long)"""
        _STBVorbis.stb_vorbis_flush_pushdata(_long.valueOf(arg0))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_short(arg0: int, arg1: 'PointerBuffer', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_short(long,org.lwjgl.PointerBuffer,int)"""
        return int._wrap(_STBVorbis.stb_vorbis_get_samples_short(_long.valueOf(arg0), arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstb_vorbis_decode_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_memory(long,int,long,long,long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_decode_memory(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def stb_vorbis_seek_frame(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBVorbis.stb_vorbis_seek_frame(long,int)"""
        return bool._wrap(_STBVorbis.stb_vorbis_seek_frame(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def stb_vorbis_stream_length_in_seconds(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBVorbis.stb_vorbis_stream_length_in_seconds(long)"""
        return float._wrap(_STBVorbis.stb_vorbis_stream_length_in_seconds(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_short_interleaved(long,int,long,int)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_frame_short_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_open_pushdata(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_pushdata(long,int,long,long,long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_open_pushdata(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_float(arg0: int, arg1: 'int', arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_float(long,int[],org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_get_frame_float(_long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'ByteBuffer', arg1: 'int', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.nio.ByteBuffer,int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int._wrap(_STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_short(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_short(long,int,long,int)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_samples_short(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def stb_vorbis_decode_frame_pushdata(arg0: int, arg1: 'ByteBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer', arg4: 'IntBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_frame_pushdata(long,java.nio.ByteBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer,java.nio.IntBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_decode_frame_pushdata(_long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def nstb_vorbis_open_memory(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_memory(long,int,int[],long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_open_memory(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nstb_vorbis_open_pushdata(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_pushdata(long,int,int[],int[],long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_open_pushdata(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_float(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_float(long,int,long,int)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_samples_float(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ShortBuffer._wrap(_STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_open_memory(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_memory(long,int,long,long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_open_memory(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: 'short') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_short_interleaved(long,int,short[])"""
        return int._wrap(_STBVorbis.stb_vorbis_get_frame_short_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nstb_vorbis_get_error(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_error(long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_error(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_get_file_offset(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_file_offset(long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_file_offset(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_seek(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_seek(long,int)"""
        return int._wrap(_STBVorbis.nstb_vorbis_seek(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def stb_vorbis_close(arg0: int):
        """public static void org.lwjgl.stb.STBVorbis.stb_vorbis_close(long)"""
        _STBVorbis.stb_vorbis_close(_long.valueOf(arg0))

    @staticmethod
    @overload
    def stb_vorbis_get_info(arg0: int, arg1: 'STBVorbisInfo') -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbis.stb_vorbis_get_info(long,org.lwjgl.stb.STBVorbisInfo)"""
        return STBVorbisInfo._wrap(_STBVorbis.stb_vorbis_get_info(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def stb_vorbis_decode_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBVorbis.stb_vorbis_decode_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ShortBuffer._wrap(_STBVorbis.stb_vorbis_decode_memory(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: 'float') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_float_interleaved(long,int,float[])"""
        return int._wrap(_STBVorbis.stb_vorbis_get_samples_float_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_short(arg0: int, arg1: 'PointerBuffer', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_short(long,org.lwjgl.PointerBuffer,int)"""
        return int._wrap(_STBVorbis.stb_vorbis_get_frame_short(_long.valueOf(arg0), arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def stb_vorbis_stream_length_in_samples(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_stream_length_in_samples(long)"""
        return int._wrap(_STBVorbis.stb_vorbis_stream_length_in_samples(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: 'short', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_short_interleaved(long,int,short[],int)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_samples_short_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: 'ShortBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_short_interleaved(long,int,java.nio.ShortBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_get_frame_short_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stb_vorbis_seek_start(arg0: int) -> bool:
        """public static boolean org.lwjgl.stb.STBVorbis.stb_vorbis_seek_start(long)"""
        return bool._wrap(_STBVorbis.stb_vorbis_seek_start(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_open_pushdata(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_pushdata(java.nio.ByteBuffer,int[],int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int._wrap(_STBVorbis.stb_vorbis_open_pushdata(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_open_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_memory(java.nio.ByteBuffer,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int._wrap(_STBVorbis.stb_vorbis_open_memory(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_stream_length_in_samples(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_stream_length_in_samples(long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_stream_length_in_samples(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_float(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_float(long,int[],long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_frame_float(_long.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstb_vorbis_decode_memory(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_memory(long,int,int[],int[],long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_decode_memory(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstb_vorbis_close(arg0: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_close(long)"""
        _STBVorbis.nstb_vorbis_close(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nstb_vorbis_open_filename(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_filename(long,long,long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_open_filename(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: 'ShortBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_short_interleaved(long,int,java.nio.ShortBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_get_samples_short_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stb_vorbis_get_comment(arg0: int, arg1: 'STBVorbisComment') -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbis.stb_vorbis_get_comment(long,org.lwjgl.stb.STBVorbisComment)"""
        return STBVorbisComment._wrap(_STBVorbis.stb_vorbis_get_comment(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_float(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_float(long,long,long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_frame_float(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_float(arg0: int, arg1: 'IntBuffer', arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_float(long,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_get_frame_float(_long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_short(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_short(long,int,long,int)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_frame_short(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_decode_filename(arg0: int, arg1: 'int', arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_filename(long,int[],int[],long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_decode_filename(_long.valueOf(arg0), arg1, arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_get_info(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_get_info(long,long)"""
        _STBVorbis.nstb_vorbis_get_info(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: 'short', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_short_interleaved(long,int,short[],int)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_frame_short_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_seek_start(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_seek_start(long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_seek_start(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_get_error(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_error(long)"""
        return int._wrap(_STBVorbis.stb_vorbis_get_error(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_get_sample_offset(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_sample_offset(long)"""
        return int._wrap(_STBVorbis.stb_vorbis_get_sample_offset(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_open_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_memory(java.nio.ByteBuffer,int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int._wrap(_STBVorbis.stb_vorbis_open_memory(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_get_sample_offset(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_sample_offset(long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_sample_offset(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_short_interleaved(long,int,long,int)"""
        return int._wrap(_STBVorbis.nstb_vorbis_get_samples_short_interleaved(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'CharSequence', arg1: 'int', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.lang.CharSequence,int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int._wrap(_STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_open_pushdata(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_pushdata(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int._wrap(_STBVorbis.stb_vorbis_open_pushdata(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_decode_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_memory(java.nio.ByteBuffer,int[],int[],org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBVorbis.stb_vorbis_decode_memory(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_decode_frame_pushdata(arg0: int, arg1: 'ByteBuffer', arg2: 'int', arg3: 'PointerBuffer', arg4: 'int') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_frame_pushdata(long,java.nio.ByteBuffer,int[],org.lwjgl.PointerBuffer,int[])"""
        return int._wrap(_STBVorbis.stb_vorbis_decode_frame_pushdata(_long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def nstb_vorbis_decode_filename(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_filename(long,long,long,long)"""
        return int._wrap(_STBVorbis.nstb_vorbis_decode_filename(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_seek(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBVorbis.stb_vorbis_seek(long,int)"""
        return bool._wrap(_STBVorbis.stb_vorbis_seek(_long.valueOf(arg0), _int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBTTKerningentry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.stb.STBTTKerningentry as _STBTTKerningentry_Buffer
_Buffer = _STBTTKerningentry_Buffer.Buffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.stb.STBTTKerningentry as _STBTTKerningentry
_STBTTKerningentry = _STBTTKerningentry
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBTTKerningentry():
    """org.lwjgl.stb.STBTTKerningentry"""
 
    @staticmethod
    def _wrap(java_value: _STBTTKerningentry) -> 'STBTTKerningentry':
        return STBTTKerningentry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBTTKerningentry):
        """
        Dynamic initializer for STBTTKerningentry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBTTKerningentry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBTTKerningentry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nglyph1(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTKerningentry.nglyph1(long)"""
        return int._wrap(_STBTTKerningentry.nglyph1(_long.valueOf(arg0)))

    @overload
    def advance(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry.advance()"""
        return int._wrap(super(STBTTKerningentry, self).advance())

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
    def create() -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.create()"""
        return STBTTKerningentry._wrap(_STBTTKerningentry.create())

    @staticmethod
    @overload
    def nglyph2(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTKerningentry.nglyph2(long)"""
        return int._wrap(_STBTTKerningentry.nglyph2(_long.valueOf(arg0)))

    @overload
    def glyph2(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry.glyph2()"""
        return int._wrap(super(STBTTKerningentry, self).glyph2())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nadvance(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTKerningentry.nadvance(long)"""
        return int._wrap(_STBTTKerningentry.nadvance(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.malloc(int)"""
        return Buffer._wrap(_STBTTKerningentry.malloc(_int.valueOf(arg0)))

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTKerningentry(java.nio.ByteBuffer)"""
        val = _STBTTKerningentry(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc() -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.calloc()"""
        return STBTTKerningentry._wrap(_STBTTKerningentry.calloc())

    @staticmethod
    @overload
    def malloc() -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.malloc()"""
        return STBTTKerningentry._wrap(_STBTTKerningentry.malloc())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTKerningentry._wrap(_STBTTKerningentry.malloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.calloc(int)"""
        return Buffer._wrap(_STBTTKerningentry.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTKerningentry.malloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry.sizeof()"""
        return int._wrap(super(STBTTKerningentry, self).sizeof())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTKerningentry.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.createSafe(long,int)"""
        return Buffer._wrap(_STBTTKerningentry.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.create(long,int)"""
        return Buffer._wrap(_STBTTKerningentry.create(_long.valueOf(arg0), _int.valueOf(arg1)))

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

    @overload
    def glyph1(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry.glyph1()"""
        return int._wrap(super(STBTTKerningentry, self).glyph1())

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
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.create(int)"""
        return Buffer._wrap(_STBTTKerningentry.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.create(long)"""
        return STBTTKerningentry._wrap(_STBTTKerningentry.create(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTKerningentry._wrap(_STBTTKerningentry.calloc(arg0))

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
    def createSafe(arg0: int) -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.createSafe(long)"""
        return STBTTKerningentry._wrap(_STBTTKerningentry.createSafe(_long.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.stb.STBTTPackedchar
from pyquantum_helper import import_once as _import_once
import org.lwjgl.stb.STBTTPackedchar as _STBTTPackedchar_Buffer
_Buffer = _STBTTPackedchar_Buffer.Buffer
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
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Float as _float
import org.lwjgl.stb.STBTTPackedchar as _STBTTPackedchar
_STBTTPackedchar = _STBTTPackedchar
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBTTPackedchar():
    """org.lwjgl.stb.STBTTPackedchar"""
 
    @staticmethod
    def _wrap(java_value: _STBTTPackedchar) -> 'STBTTPackedchar':
        return STBTTPackedchar(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBTTPackedchar):
        """
        Dynamic initializer for STBTTPackedchar.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBTTPackedchar__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBTTPackedchar__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackedchar.malloc(_int.valueOf(arg0), arg1))

    @overload
    def yoff(self, arg0: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.yoff(float)"""
        return 'STBTTPackedchar'._wrap(super(_STBTTPackedchar, self).yoff(_float.valueOf(arg0)))

    @overload
    def y0(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar.y0()"""
        return int._wrap(super(STBTTPackedchar, self).y0())

    @staticmethod
    @overload
    def calloc() -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.calloc()"""
        return STBTTPackedchar._wrap(_STBTTPackedchar.calloc())

    @overload
    def xoff2(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar.xoff2()"""
        return float._wrap(super(STBTTPackedchar, self).xoff2())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackedchar(java.nio.ByteBuffer)"""
        val = _STBTTPackedchar(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def nx0(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTPackedchar.nx0(long)"""
        return int._wrap(_STBTTPackedchar.nx0(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nyoff2(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackedchar.nyoff2(long)"""
        return float._wrap(_STBTTPackedchar.nyoff2(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.calloc(int)"""
        return Buffer._wrap(_STBTTPackedchar.calloc(_int.valueOf(arg0)))

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
    def nyoff(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackedchar.nyoff(long)"""
        return float._wrap(_STBTTPackedchar.nyoff(_long.valueOf(arg0)))

    @overload
    def y1(self, arg0: int) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.y1(short)"""
        return 'STBTTPackedchar'._wrap(super(_STBTTPackedchar, self).y1(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackedchar._wrap(_STBTTPackedchar.calloc(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.callocStack(int)"""
        return Buffer._wrap(_STBTTPackedchar.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.callocStack()"""
        return STBTTPackedchar._wrap(_STBTTPackedchar.callocStack())

    @staticmethod
    @overload
    def nx1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTPackedchar.nx1(long)"""
        return int._wrap(_STBTTPackedchar.nx1(_long.valueOf(arg0)))

    @overload
    def xadvance(self, arg0: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.xadvance(float)"""
        return 'STBTTPackedchar'._wrap(super(_STBTTPackedchar, self).xadvance(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.create(long,int)"""
        return Buffer._wrap(_STBTTPackedchar.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def ny1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTPackedchar.ny1(long)"""
        return int._wrap(_STBTTPackedchar.ny1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nyoff(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackedchar.nyoff(long,float)"""
        _STBTTPackedchar.nyoff(_long.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def yoff2(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar.yoff2()"""
        return float._wrap(super(STBTTPackedchar, self).yoff2())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackedchar.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nyoff2(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackedchar.nyoff2(long,float)"""
        _STBTTPackedchar.nyoff2(_long.valueOf(arg0), _float.valueOf(arg1))

    @staticmethod
    @overload
    def create() -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.create()"""
        return STBTTPackedchar._wrap(_STBTTPackedchar.create())

    @overload
    def xoff(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar.xoff()"""
        return float._wrap(super(STBTTPackedchar, self).xoff())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.createSafe(long,int)"""
        return Buffer._wrap(_STBTTPackedchar.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

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

    @overload
    def set(self, arg0: 'STBTTPackedchar') -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.set(org.lwjgl.stb.STBTTPackedchar)"""
        return 'STBTTPackedchar'._wrap(super(_STBTTPackedchar, self).set(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackedchar.calloc(_int.valueOf(arg0), arg1))

    @overload
    def x1(self, arg0: int) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.x1(short)"""
        return 'STBTTPackedchar'._wrap(super(_STBTTPackedchar, self).x1(_short.valueOf(arg0)))

    @overload
    def xoff(self, arg0: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.xoff(float)"""
        return 'STBTTPackedchar'._wrap(super(_STBTTPackedchar, self).xoff(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def ny0(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTPackedchar.ny0(long)"""
        return int._wrap(_STBTTPackedchar.ny0(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nxadvance(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackedchar.nxadvance(long)"""
        return float._wrap(_STBTTPackedchar.nxadvance(_long.valueOf(arg0)))

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

    @overload
    def x0(self, arg0: int) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.x0(short)"""
        return 'STBTTPackedchar'._wrap(super(_STBTTPackedchar, self).x0(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.malloc()"""
        return STBTTPackedchar._wrap(_STBTTPackedchar.malloc())

    @overload
    def x1(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar.x1()"""
        return int._wrap(super(STBTTPackedchar, self).x1())

    @staticmethod
    @overload
    def nxoff(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackedchar.nxoff(long,float)"""
        _STBTTPackedchar.nxoff(_long.valueOf(arg0), _float.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackedchar.mallocStack(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nxoff2(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackedchar.nxoff2(long)"""
        return float._wrap(_STBTTPackedchar.nxoff2(_long.valueOf(arg0)))

    @overload
    def y0(self, arg0: int) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.y0(short)"""
        return 'STBTTPackedchar'._wrap(super(_STBTTPackedchar, self).y0(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def ny1(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackedchar.ny1(long,short)"""
        _STBTTPackedchar.ny1(_long.valueOf(arg0), _short.valueOf(arg1))

    @overload
    def yoff2(self, arg0: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.yoff2(float)"""
        return 'STBTTPackedchar'._wrap(super(_STBTTPackedchar, self).yoff2(_float.valueOf(arg0)))

    @overload
    def yoff(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar.yoff()"""
        return float._wrap(super(STBTTPackedchar, self).yoff())

    @staticmethod
    @overload
    def nxoff2(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackedchar.nxoff2(long,float)"""
        _STBTTPackedchar.nxoff2(_long.valueOf(arg0), _float.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.create(long)"""
        return STBTTPackedchar._wrap(_STBTTPackedchar.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nx1(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackedchar.nx1(long,short)"""
        _STBTTPackedchar.nx1(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.create(int)"""
        return Buffer._wrap(_STBTTPackedchar.create(_int.valueOf(arg0)))

    @overload
    def y1(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar.y1()"""
        return int._wrap(super(STBTTPackedchar, self).y1())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackedchar._wrap(_STBTTPackedchar.callocStack(arg0))

    @overload
    def x0(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar.x0()"""
        return int._wrap(super(STBTTPackedchar, self).x0())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.createSafe(long)"""
        return STBTTPackedchar._wrap(_STBTTPackedchar.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.mallocStack()"""
        return STBTTPackedchar._wrap(_STBTTPackedchar.mallocStack())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def ny0(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackedchar.ny0(long,short)"""
        _STBTTPackedchar.ny0(_long.valueOf(arg0), _short.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def xadvance(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar.xadvance()"""
        return float._wrap(super(STBTTPackedchar, self).xadvance())

    @staticmethod
    @overload
    def nxadvance(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackedchar.nxadvance(long,float)"""
        _STBTTPackedchar.nxadvance(_long.valueOf(arg0), _float.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackedchar._wrap(_STBTTPackedchar.malloc(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTPackedchar.sizeof()"""
        return int._wrap(super(STBTTPackedchar, self).sizeof())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nx0(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackedchar.nx0(long,short)"""
        _STBTTPackedchar.nx0(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackedchar._wrap(_STBTTPackedchar.mallocStack(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nxoff(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackedchar.nxoff(long)"""
        return float._wrap(_STBTTPackedchar.nxoff(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.malloc(int)"""
        return Buffer._wrap(_STBTTPackedchar.malloc(_int.valueOf(arg0)))

    @overload
    def xoff2(self, arg0: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.xoff2(float)"""
        return 'STBTTPackedchar'._wrap(super(_STBTTPackedchar, self).xoff2(_float.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.set(short,short,short,short,float,float,float,float,float)"""
        return 'STBTTPackedchar'._wrap(super(_STBTTPackedchar, self).set(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.mallocStack(int)"""
        return Buffer._wrap(_STBTTPackedchar.mallocStack(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBIZlibCompressI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.stb.STBIZlibCompressI as _STBIZlibCompressI
_STBIZlibCompressI = _STBIZlibCompressI
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
 
class STBIZlibCompressI():
    """org.lwjgl.stb.STBIZlibCompressI"""
 
    @staticmethod
    def _wrap(java_value: _STBIZlibCompressI) -> 'STBIZlibCompressI':
        return STBIZlibCompressI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBIZlibCompressI):
        """
        Dynamic initializer for STBIZlibCompressI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBIZlibCompressI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBIZlibCompressI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract long org.lwjgl.stb.STBIZlibCompressI.invoke(long,int,long,int)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIZlibCompressI.callback(long,long)"""
        super(_STBIZlibCompressI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIZlibCompressI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(STBIZlibCompressI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.stb.STBPerlin
from builtins import str
import org.lwjgl.stb.STBPerlin as _STBPerlin
_STBPerlin = _STBPerlin
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBPerlin():
    """org.lwjgl.stb.STBPerlin"""
 
    @staticmethod
    def _wrap(java_value: _STBPerlin) -> 'STBPerlin':
        return STBPerlin(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBPerlin):
        """
        Dynamic initializer for STBPerlin.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBPerlin__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBPerlin__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def stb_perlin_turbulence_noise3(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_turbulence_noise3(float,float,float,float,float,int)"""
        return float._wrap(_STBPerlin.stb_perlin_turbulence_noise3(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def stb_perlin_noise3(arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_noise3(float,float,float,int,int,int)"""
        return float._wrap(_STBPerlin.stb_perlin_noise3(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

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
    def stb_perlin_noise3_seed(arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_noise3_seed(float,float,float,int,int,int,int)"""
        return float._wrap(_STBPerlin.stb_perlin_noise3_seed(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

    @staticmethod
    @overload
    def stb_perlin_noise3_wrap_nonpow2(arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_noise3_wrap_nonpow2(float,float,float,int,int,int,byte)"""
        return float._wrap(_STBPerlin.stb_perlin_noise3_wrap_nonpow2(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _byte.valueOf(arg6)))

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
    def stb_perlin_fbm_noise3(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_fbm_noise3(float,float,float,float,float,int)"""
        return float._wrap(_STBPerlin.stb_perlin_fbm_noise3(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5)))

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
    def stb_perlin_ridge_noise3(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_ridge_noise3(float,float,float,float,float,float,int)"""
        return float._wrap(_STBPerlin.stb_perlin_ridge_noise3(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _int.valueOf(arg6)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.stb.STBIIOCallbacks$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.stb.STBIReadCallback as _STBIReadCallback
_STBIReadCallback = _STBIReadCallback
import org.lwjgl.stb.STBISkipCallback as _STBISkipCallback
_STBISkipCallback = _STBISkipCallback
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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import org.lwjgl.stb.STBIEOFCallback as _STBIEOFCallback
_STBIEOFCallback = _STBIEOFCallback
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.stb.STBIIOCallbacks as _STBIIOCallbacks_Buffer
_Buffer = _STBIIOCallbacks_Buffer.Buffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.stb.STBIIOCallbacks.Buffer"""
 
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

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def read(self) -> 'STBIReadCallback':
        """public org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIIOCallbacks$Buffer.read()"""
        return 'STBIReadCallback'._wrap(super(Buffer, self).read())

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
    def read(self, arg0: 'STBIReadCallbackI') -> 'Buffer':
        """public org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks$Buffer.read(org.lwjgl.stb.STBIReadCallbackI)"""
        return 'Buffer'._wrap(super(_Buffer, self).read(arg0))

    @overload
    def skip(self) -> 'STBISkipCallback':
        """public org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBIIOCallbacks$Buffer.skip()"""
        return 'STBISkipCallback'._wrap(super(Buffer, self).skip())

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

    @overload
    def eof(self) -> 'STBIEOFCallback':
        """public org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIIOCallbacks$Buffer.eof()"""
        return 'STBIEOFCallback'._wrap(super(Buffer, self).eof())

    @overload
    def eof(self, arg0: 'STBIEOFCallbackI') -> 'Buffer':
        """public org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks$Buffer.eof(org.lwjgl.stb.STBIEOFCallbackI)"""
        return 'Buffer'._wrap(super(_Buffer, self).eof(arg0))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBIIOCallbacks$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBIIOCallbacks$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def skip(self, arg0: 'STBISkipCallbackI') -> 'Buffer':
        """public org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks$Buffer.skip(org.lwjgl.stb.STBISkipCallbackI)"""
        return 'Buffer'._wrap(super(_Buffer, self).skip(arg0))

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
 
 
# CLASS: org.lwjgl.stb.STBISkipCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.stb.STBISkipCallbackI as _STBISkipCallbackI
_STBISkipCallbackI = _STBISkipCallbackI
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class STBISkipCallbackI():
    """org.lwjgl.stb.STBISkipCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _STBISkipCallbackI) -> 'STBISkipCallbackI':
        return STBISkipCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBISkipCallbackI):
        """
        Dynamic initializer for STBISkipCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBISkipCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBISkipCallbackI__wrapper":
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
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBISkipCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(STBISkipCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.stb.STBISkipCallbackI.invoke(long,int)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBISkipCallbackI.callback(long,long)"""
        super(_STBISkipCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.stb.STBTTBitmap$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.util.function.Consumer as Consumer
import org.lwjgl.stb.STBTTBitmap as _STBTTBitmap_Buffer
_Buffer = _STBTTBitmap_Buffer.Buffer
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
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.stb.STBTTBitmap.Buffer"""
 
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
    def w(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap$Buffer.w()"""
        return int._wrap(super(Buffer, self).w())

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
    def stride(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap$Buffer.stride(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).stride(_int.valueOf(arg0)))

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
    def pixels(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap$Buffer.pixels(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).pixels(arg0))

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
    def h(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap$Buffer.h(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).h(_int.valueOf(arg0)))

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
    def w(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap$Buffer.w(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).w(_int.valueOf(arg0)))

    @overload
    def stride(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap$Buffer.stride()"""
        return int._wrap(super(Buffer, self).stride())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBTTBitmap$Buffer.pixels(int)"""
        return 'ByteBuffer'._wrap(super(_Buffer, self).pixels(_int.valueOf(arg0)))

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
    def h(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap$Buffer.h()"""
        return int._wrap(super(Buffer, self).h())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTBitmap$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
        """public org.lwjgl.stb.STBTTBitmap$Buffer(long,int)"""
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
 
 
# CLASS: org.lwjgl.stb.STBDXT
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBDXT as _STBDXT
_STBDXT = _STBDXT
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBDXT():
    """org.lwjgl.stb.STBDXT"""
 
    @staticmethod
    def _wrap(java_value: _STBDXT) -> 'STBDXT':
        return STBDXT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBDXT):
        """
        Dynamic initializer for STBDXT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBDXT__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBDXT__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def stb_compress_dxt_block(arg0: 'ByteBuffer', arg1: 'ByteBuffer', arg2: bool, arg3: int):
        """public static void org.lwjgl.stb.STBDXT.stb_compress_dxt_block(java.nio.ByteBuffer,java.nio.ByteBuffer,boolean,int)"""
        _STBDXT.stb_compress_dxt_block(arg0, arg1, _boolean.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nstb_compress_bc4_block(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBDXT.nstb_compress_bc4_block(long,long)"""
        _STBDXT.nstb_compress_bc4_block(_long.valueOf(arg0), _long.valueOf(arg1))

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
    def stb_compress_bc5_block(arg0: 'ByteBuffer', arg1: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBDXT.stb_compress_bc5_block(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        _STBDXT.stb_compress_bc5_block(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nstb_compress_bc5_block(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBDXT.nstb_compress_bc5_block(long,long)"""
        _STBDXT.nstb_compress_bc5_block(_long.valueOf(arg0), _long.valueOf(arg1))

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
    def stb_compress_bc4_block(arg0: 'ByteBuffer', arg1: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBDXT.stb_compress_bc4_block(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        _STBDXT.stb_compress_bc4_block(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nstb_compress_dxt_block(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.stb.STBDXT.nstb_compress_dxt_block(long,long,int,int)"""
        _STBDXT.nstb_compress_dxt_block(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.stb.STBTTBitmap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.lwjgl.stb.STBTTBitmap as _STBTTBitmap
_STBTTBitmap = _STBTTBitmap
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
import org.lwjgl.stb.STBTTBitmap as _STBTTBitmap_Buffer
_Buffer = _STBTTBitmap_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBTTBitmap():
    """org.lwjgl.stb.STBTTBitmap"""
 
    @staticmethod
    def _wrap(java_value: _STBTTBitmap) -> 'STBTTBitmap':
        return STBTTBitmap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBTTBitmap):
        """
        Dynamic initializer for STBTTBitmap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBTTBitmap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBTTBitmap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def stride(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap.stride()"""
        return int._wrap(super(STBTTBitmap, self).stride())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.calloc(int)"""
        return Buffer._wrap(_STBTTBitmap.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nw(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTBitmap.nw(long)"""
        return int._wrap(_STBTTBitmap.nw(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.mallocStack()"""
        return STBTTBitmap._wrap(_STBTTBitmap.mallocStack())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTBitmap.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nw(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTBitmap.nw(long,int)"""
        _STBTTBitmap.nw(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTBitmap.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTBitmap._wrap(_STBTTBitmap.callocStack(arg0))

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
    def callocStack() -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.callocStack()"""
        return STBTTBitmap._wrap(_STBTTBitmap.callocStack())

    @staticmethod
    @overload
    def nstride(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTBitmap.nstride(long)"""
        return int._wrap(_STBTTBitmap.nstride(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.mallocStack(int)"""
        return Buffer._wrap(_STBTTBitmap.mallocStack(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTBitmap(java.nio.ByteBuffer)"""
        val = _STBTTBitmap(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def npixels(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTTBitmap.npixels(long,int)"""
        return ByteBuffer._wrap(_STBTTBitmap.npixels(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTBitmap.mallocStack(_int.valueOf(arg0), arg1))

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

    @overload
    def h(self, arg0: int) -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.h(int)"""
        return 'STBTTBitmap'._wrap(super(_STBTTBitmap, self).h(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTBitmap._wrap(_STBTTBitmap.calloc(arg0))

    @staticmethod
    @overload
    def create() -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.create()"""
        return STBTTBitmap._wrap(_STBTTBitmap.create())

    @staticmethod
    @overload
    def nh(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTBitmap.nh(long,int)"""
        _STBTTBitmap.nh(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTBitmap._wrap(_STBTTBitmap.mallocStack(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.create(int)"""
        return Buffer._wrap(_STBTTBitmap.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.createSafe(long)"""
        return STBTTBitmap._wrap(_STBTTBitmap.createSafe(_long.valueOf(arg0)))

    @overload
    def w(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap.w()"""
        return int._wrap(super(STBTTBitmap, self).w())

    @staticmethod
    @overload
    def malloc() -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.malloc()"""
        return STBTTBitmap._wrap(_STBTTBitmap.malloc())

    @overload
    def set(self, arg0: 'STBTTBitmap') -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.set(org.lwjgl.stb.STBTTBitmap)"""
        return 'STBTTBitmap'._wrap(super(_STBTTBitmap, self).set(arg0))

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
    def nh(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTBitmap.nh(long)"""
        return int._wrap(_STBTTBitmap.nh(_long.valueOf(arg0)))

    @overload
    def stride(self, arg0: int) -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.stride(int)"""
        return 'STBTTBitmap'._wrap(super(_STBTTBitmap, self).stride(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTBitmap.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nstride(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTBitmap.nstride(long,int)"""
        _STBTTBitmap.nstride(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.malloc(int)"""
        return Buffer._wrap(_STBTTBitmap.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTBitmap._wrap(_STBTTBitmap.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.create(long)"""
        return STBTTBitmap._wrap(_STBTTBitmap.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.stb.STBTTBitmap.validate(long)"""
        _STBTTBitmap.validate(_long.valueOf(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.createSafe(long,int)"""
        return Buffer._wrap(_STBTTBitmap.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.callocStack(int)"""
        return Buffer._wrap(_STBTTBitmap.callocStack(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'ByteBuffer') -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.set(int,int,int,java.nio.ByteBuffer)"""
        return 'STBTTBitmap'._wrap(super(_STBTTBitmap, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @overload
    def w(self, arg0: int) -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.w(int)"""
        return 'STBTTBitmap'._wrap(super(_STBTTBitmap, self).w(_int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap.sizeof()"""
        return int._wrap(super(STBTTBitmap, self).sizeof())

    @overload
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBTTBitmap.pixels(int)"""
        return 'ByteBuffer'._wrap(super(_STBTTBitmap, self).pixels(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.calloc()"""
        return STBTTBitmap._wrap(_STBTTBitmap.calloc())

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

    @overload
    def pixels(self, arg0: 'ByteBuffer') -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.pixels(java.nio.ByteBuffer)"""
        return 'STBTTBitmap'._wrap(super(_STBTTBitmap, self).pixels(arg0))

    @staticmethod
    @overload
    def npixels(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBTTBitmap.npixels(long,java.nio.ByteBuffer)"""
        _STBTTBitmap.npixels(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.create(long,int)"""
        return Buffer._wrap(_STBTTBitmap.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def h(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap.h()"""
        return int._wrap(super(STBTTBitmap, self).h())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBVorbisComment$Buffer
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
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.stb.STBVorbisComment as _STBVorbisComment_Buffer
_Buffer = _STBVorbisComment_Buffer.Buffer
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
    """org.lwjgl.stb.STBVorbisComment.Buffer"""
 
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
    def comment_list(self) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.stb.STBVorbisComment$Buffer.comment_list()"""
        return 'pygl.PointerBuffer'._wrap(super(Buffer, self).comment_list())

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
    def comment_list_length(self) -> int:
        """public int org.lwjgl.stb.STBVorbisComment$Buffer.comment_list_length()"""
        return int._wrap(super(Buffer, self).comment_list_length())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisComment$Buffer(java.nio.ByteBuffer)"""
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
    def vendor(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBVorbisComment$Buffer.vendor()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).vendor())

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

    @overload
    def vendorString(self) -> str:
        """public java.lang.String org.lwjgl.stb.STBVorbisComment$Buffer.vendorString()"""
        return str._wrap(super(Buffer, self).vendorString())

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
        """public org.lwjgl.stb.STBVorbisComment$Buffer(long,int)"""
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
 
 
# CLASS: org.lwjgl.stb.STBIWriteCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import org.lwjgl.stb.STBIWriteCallbackI as _STBIWriteCallbackI
_STBIWriteCallbackI = _STBIWriteCallbackI
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class STBIWriteCallbackI():
    """org.lwjgl.stb.STBIWriteCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _STBIWriteCallbackI) -> 'STBIWriteCallbackI':
        return STBIWriteCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBIWriteCallbackI):
        """
        Dynamic initializer for STBIWriteCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBIWriteCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBIWriteCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIWriteCallbackI.callback(long,long)"""
        super(_STBIWriteCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIWriteCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(STBIWriteCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.stb.STBIWriteCallbackI.invoke(long,long,int)"""
        pass 
 
 
# CLASS: org.lwjgl.stb.STBTTAlignedQuad$Buffer
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
import org.lwjgl.stb.STBTTAlignedQuad as _STBTTAlignedQuad_Buffer
_Buffer = _STBTTAlignedQuad_Buffer.Buffer
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
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
    """org.lwjgl.stb.STBTTAlignedQuad.Buffer"""
 
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
    def x0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.x0()"""
        return float._wrap(super(Buffer, self).x0())

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
    def y0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.y0()"""
        return float._wrap(super(Buffer, self).y0())

    @overload
    def s0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.s0()"""
        return float._wrap(super(Buffer, self).s0())

    @overload
    def s1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.s1()"""
        return float._wrap(super(Buffer, self).s1())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def y1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.y1()"""
        return float._wrap(super(Buffer, self).y1())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTAlignedQuad$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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

    @overload
    def x1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.x1()"""
        return float._wrap(super(Buffer, self).x1())

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
    def t0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.t0()"""
        return float._wrap(super(Buffer, self).t0())

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
    def t1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.t1()"""
        return float._wrap(super(Buffer, self).t1())

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTAlignedQuad$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
 
 
# CLASS: org.lwjgl.stb.STBVorbisComment
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
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.stb.STBVorbisComment as _STBVorbisComment
_STBVorbisComment = _STBVorbisComment
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.stb.STBVorbisComment as _STBVorbisComment_Buffer
_Buffer = _STBVorbisComment_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBVorbisComment():
    """org.lwjgl.stb.STBVorbisComment"""
 
    @staticmethod
    def _wrap(java_value: _STBVorbisComment) -> 'STBVorbisComment':
        return STBVorbisComment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBVorbisComment):
        """
        Dynamic initializer for STBVorbisComment.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBVorbisComment__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBVorbisComment__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBVorbisComment.sizeof()"""
        return int._wrap(super(STBVorbisComment, self).sizeof())

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
    def calloc() -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.calloc()"""
        return STBVorbisComment._wrap(_STBVorbisComment.calloc())

    @staticmethod
    @overload
    def ncomment_list_length(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisComment.ncomment_list_length(long)"""
        return int._wrap(_STBVorbisComment.ncomment_list_length(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.create(int)"""
        return Buffer._wrap(_STBVorbisComment.create(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def vendorString(self) -> str:
        """public java.lang.String org.lwjgl.stb.STBVorbisComment.vendorString()"""
        return str._wrap(super(STBVorbisComment, self).vendorString())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.malloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisComment._wrap(_STBVorbisComment.malloc(arg0))

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
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.createSafe(long,int)"""
        return Buffer._wrap(_STBVorbisComment.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def vendor(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBVorbisComment.vendor()"""
        return 'ByteBuffer'._wrap(super(STBVorbisComment, self).vendor())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBVorbisComment.malloc(_int.valueOf(arg0), arg1))

    @overload
    def comment_list(self) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.stb.STBVorbisComment.comment_list()"""
        return 'pygl.PointerBuffer'._wrap(super(STBVorbisComment, self).comment_list())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.createSafe(long)"""
        return STBVorbisComment._wrap(_STBVorbisComment.createSafe(_long.valueOf(arg0)))

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
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nvendorString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.stb.STBVorbisComment.nvendorString(long)"""
        return str._wrap(_STBVorbisComment.nvendorString(_long.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.calloc(int)"""
        return Buffer._wrap(_STBVorbisComment.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.create(long,int)"""
        return Buffer._wrap(_STBVorbisComment.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nvendor(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBVorbisComment.nvendor(long)"""
        return ByteBuffer._wrap(_STBVorbisComment.nvendor(_long.valueOf(arg0)))

    @overload
    def comment_list_length(self) -> int:
        """public int org.lwjgl.stb.STBVorbisComment.comment_list_length()"""
        return int._wrap(super(STBVorbisComment, self).comment_list_length())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.calloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisComment._wrap(_STBVorbisComment.calloc(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create() -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.create()"""
        return STBVorbisComment._wrap(_STBVorbisComment.create())

    @staticmethod
    @overload
    def malloc() -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.malloc()"""
        return STBVorbisComment._wrap(_STBVorbisComment.malloc())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisComment(java.nio.ByteBuffer)"""
        val = _STBVorbisComment(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def ncomment_list(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.stb.STBVorbisComment.ncomment_list(long)"""
        return pygl.PointerBuffer._wrap(_STBVorbisComment.ncomment_list(_long.valueOf(arg0)))

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
    def create(arg0: int) -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.create(long)"""
        return STBVorbisComment._wrap(_STBVorbisComment.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBVorbisComment.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.malloc(int)"""
        return Buffer._wrap(_STBVorbisComment.malloc(_int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address()) 
 
 
# CLASS: org.lwjgl.stb.STBVorbisInfo
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
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBVorbisInfo as _STBVorbisInfo
_STBVorbisInfo = _STBVorbisInfo
import org.lwjgl.stb.STBVorbisInfo as _STBVorbisInfo_Buffer
_Buffer = _STBVorbisInfo_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBVorbisInfo():
    """org.lwjgl.stb.STBVorbisInfo"""
 
    @staticmethod
    def _wrap(java_value: _STBVorbisInfo) -> 'STBVorbisInfo':
        return STBVorbisInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBVorbisInfo):
        """
        Dynamic initializer for STBVorbisInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBVorbisInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBVorbisInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBVorbisInfo.callocStack(_int.valueOf(arg0), arg1))

    @overload
    def setup_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.setup_memory_required()"""
        return int._wrap(super(STBVorbisInfo, self).setup_memory_required())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBVorbisInfo.mallocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def temp_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.temp_memory_required()"""
        return int._wrap(super(STBVorbisInfo, self).temp_memory_required())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.calloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisInfo._wrap(_STBVorbisInfo.calloc(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nsample_rate(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.nsample_rate(long)"""
        return int._wrap(_STBVorbisInfo.nsample_rate(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nchannels(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.nchannels(long)"""
        return int._wrap(_STBVorbisInfo.nchannels(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBVorbisInfo._wrap(_STBVorbisInfo.mallocStack(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.create(long)"""
        return STBVorbisInfo._wrap(_STBVorbisInfo.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBVorbisInfo.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.mallocStack(int)"""
        return Buffer._wrap(_STBVorbisInfo.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.mallocStack()"""
        return STBVorbisInfo._wrap(_STBVorbisInfo.mallocStack())

    @staticmethod
    @overload
    def create() -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.create()"""
        return STBVorbisInfo._wrap(_STBVorbisInfo.create())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.calloc(int)"""
        return Buffer._wrap(_STBVorbisInfo.calloc(_int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def sample_rate(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.sample_rate()"""
        return int._wrap(super(STBVorbisInfo, self).sample_rate())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.callocStack(int)"""
        return Buffer._wrap(_STBVorbisInfo.callocStack(_int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def malloc() -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.malloc()"""
        return STBVorbisInfo._wrap(_STBVorbisInfo.malloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.createSafe(long,int)"""
        return Buffer._wrap(_STBVorbisInfo.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.malloc(int)"""
        return Buffer._wrap(_STBVorbisInfo.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.createSafe(long)"""
        return STBVorbisInfo._wrap(_STBVorbisInfo.createSafe(_long.valueOf(arg0)))

    @overload
    def channels(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.channels()"""
        return int._wrap(super(STBVorbisInfo, self).channels())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.sizeof()"""
        return int._wrap(super(STBVorbisInfo, self).sizeof())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nsetup_temp_memory_required(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.nsetup_temp_memory_required(long)"""
        return int._wrap(_STBVorbisInfo.nsetup_temp_memory_required(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.malloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisInfo._wrap(_STBVorbisInfo.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.create(int)"""
        return Buffer._wrap(_STBVorbisInfo.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nmax_frame_size(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.nmax_frame_size(long)"""
        return int._wrap(_STBVorbisInfo.nmax_frame_size(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBVorbisInfo.malloc(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBVorbisInfo._wrap(_STBVorbisInfo.callocStack(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisInfo(java.nio.ByteBuffer)"""
        val = _STBVorbisInfo(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def nsetup_memory_required(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.nsetup_memory_required(long)"""
        return int._wrap(_STBVorbisInfo.nsetup_memory_required(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntemp_memory_required(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.ntemp_memory_required(long)"""
        return int._wrap(_STBVorbisInfo.ntemp_memory_required(_long.valueOf(arg0)))

    @overload
    def max_frame_size(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.max_frame_size()"""
        return int._wrap(super(STBVorbisInfo, self).max_frame_size())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.create(long,int)"""
        return Buffer._wrap(_STBVorbisInfo.create(_long.valueOf(arg0), _int.valueOf(arg1)))

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

    @overload
    def setup_temp_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.setup_temp_memory_required()"""
        return int._wrap(super(STBVorbisInfo, self).setup_temp_memory_required())

    @staticmethod
    @overload
    def callocStack() -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.callocStack()"""
        return STBVorbisInfo._wrap(_STBVorbisInfo.callocStack())

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
    def calloc() -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.calloc()"""
        return STBVorbisInfo._wrap(_STBVorbisInfo.calloc())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBRPContext
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.stb.STBRPNode as _STBRPNode
_STBRPNode = _STBRPNode
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.stb.STBRPContext as _STBRPContext_Buffer
_Buffer = _STBRPContext_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBRPNode as _STBRPNode_Buffer
_Buffer = _STBRPNode_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.stb.STBRPContext as _STBRPContext
_STBRPContext = _STBRPContext
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBRPContext():
    """org.lwjgl.stb.STBRPContext"""
 
    @staticmethod
    def _wrap(java_value: _STBRPContext) -> 'STBRPContext':
        return STBRPContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBRPContext):
        """
        Dynamic initializer for STBRPContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBRPContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBRPContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPContext._wrap(_STBRPContext.mallocStack(arg0))

    @staticmethod
    @overload
    def nalign(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.nalign(long)"""
        return int._wrap(_STBRPContext.nalign(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.callocStack()"""
        return STBRPContext._wrap(_STBRPContext.callocStack())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def height(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.height()"""
        return int._wrap(super(STBRPContext, self).height())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def align(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.align()"""
        return int._wrap(super(STBRPContext, self).align())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.sizeof()"""
        return int._wrap(super(STBRPContext, self).sizeof())

    @staticmethod
    @overload
    def ninit_mode(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.ninit_mode(long)"""
        return int._wrap(_STBRPContext.ninit_mode(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nnum_nodes(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.nnum_nodes(long)"""
        return int._wrap(_STBRPContext.nnum_nodes(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nheuristic(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.nheuristic(long)"""
        return int._wrap(_STBRPContext.nheuristic(_long.valueOf(arg0)))

    @overload
    def extra(self) -> 'Buffer':
        """public org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPContext.extra()"""
        return 'Buffer'._wrap(super(STBRPContext, self).extra())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPContext.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc() -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.malloc()"""
        return STBRPContext._wrap(_STBRPContext.malloc())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPContext(java.nio.ByteBuffer)"""
        val = _STBRPContext(arg0)
        self.__wrapper = val

    @overload
    def active_head(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.active_head()"""
        return 'STBRPNode'._wrap(super(STBRPContext, self).active_head())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPContext.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.create(int)"""
        return Buffer._wrap(_STBRPContext.create(_int.valueOf(arg0)))

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
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPContext.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.malloc(org.lwjgl.system.MemoryStack)"""
        return STBRPContext._wrap(_STBRPContext.malloc(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.mallocStack(int)"""
        return Buffer._wrap(_STBRPContext.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.malloc(int)"""
        return Buffer._wrap(_STBRPContext.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.calloc(int)"""
        return Buffer._wrap(_STBRPContext.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nfree_head(arg0: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.nfree_head(long)"""
        return STBRPNode._wrap(_STBRPContext.nfree_head(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.calloc()"""
        return STBRPContext._wrap(_STBRPContext.calloc())

    @staticmethod
    @overload
    def mallocStack() -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.mallocStack()"""
        return STBRPContext._wrap(_STBRPContext.mallocStack())

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
    def calloc(arg0: 'MemoryStack') -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.calloc(org.lwjgl.system.MemoryStack)"""
        return STBRPContext._wrap(_STBRPContext.calloc(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPContext._wrap(_STBRPContext.callocStack(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nactive_head(arg0: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.nactive_head(long)"""
        return STBRPNode._wrap(_STBRPContext.nactive_head(_long.valueOf(arg0)))

    @overload
    def heuristic(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.heuristic()"""
        return int._wrap(super(STBRPContext, self).heuristic())

    @overload
    def extra(self, arg0: int) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.extra(int)"""
        return 'STBRPNode'._wrap(super(_STBRPContext, self).extra(_int.valueOf(arg0)))

    @overload
    def width(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.width()"""
        return int._wrap(super(STBRPContext, self).width())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.callocStack(int)"""
        return Buffer._wrap(_STBRPContext.callocStack(_int.valueOf(arg0)))

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
    def nextra(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPContext.nextra(long)"""
        return Buffer._wrap(_STBRPContext.nextra(_long.valueOf(arg0)))

    @overload
    def init_mode(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.init_mode()"""
        return int._wrap(super(STBRPContext, self).init_mode())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.createSafe(long)"""
        return STBRPContext._wrap(_STBRPContext.createSafe(_long.valueOf(arg0)))

    @overload
    def free_head(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.free_head()"""
        return 'STBRPNode'._wrap(super(STBRPContext, self).free_head())

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.create(long)"""
        return STBRPContext._wrap(_STBRPContext.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.createSafe(long,int)"""
        return Buffer._wrap(_STBRPContext.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @overload
    def num_nodes(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.num_nodes()"""
        return int._wrap(super(STBRPContext, self).num_nodes())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.create(long,int)"""
        return Buffer._wrap(_STBRPContext.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create() -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.create()"""
        return STBRPContext._wrap(_STBRPContext.create())

    @staticmethod
    @overload
    def nheight(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.nheight(long)"""
        return int._wrap(_STBRPContext.nheight(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nextra(arg0: int, arg1: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.nextra(long,int)"""
        return STBRPNode._wrap(_STBRPContext.nextra(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPContext.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nwidth(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.nwidth(long)"""
        return int._wrap(_STBRPContext.nwidth(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBImage
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.CharSequence as CharSequence
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
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.lwjgl.stb.STBImage as _STBImage
_STBImage = _STBImage
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBImage():
    """org.lwjgl.stb.STBImage"""
 
    @staticmethod
    def _wrap(java_value: _STBImage) -> 'STBImage':
        return STBImage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBImage):
        """
        Dynamic initializer for STBImage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBImage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBImage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def stbi_load(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ByteBuffer._wrap(_STBImage.stbi_load(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_load_16(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16(long,long,long,long,int)"""
        return int._wrap(_STBImage.nstbi_load_16(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_load_16(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16(long,int[],int[],int[],int)"""
        return int._wrap(_STBImage.nstbi_load_16(_long.valueOf(arg0), arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_info(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool._wrap(_STBImage.stbi_info(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbi_zlib_decode_noheader_buffer(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_zlib_decode_noheader_buffer(long,int,long,int)"""
        return int._wrap(_STBImage.nstbi_zlib_decode_noheader_buffer(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nstbi_load(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load(long,long,long,long,int)"""
        return int._wrap(_STBImage.nstbi_load(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_set_unpremultiply_on_load_thread(arg0: bool):
        """public static void org.lwjgl.stb.STBImage.stbi_set_unpremultiply_on_load_thread(boolean)"""
        _STBImage.stbi_set_unpremultiply_on_load_thread(_boolean.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_ldr_to_hdr_scale(arg0: float):
        """public static native void org.lwjgl.stb.STBImage.stbi_ldr_to_hdr_scale(float)"""
        _STBImage.stbi_ldr_to_hdr_scale(_float.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_image_free(arg0: 'ShortBuffer'):
        """public static void org.lwjgl.stb.STBImage.stbi_image_free(java.nio.ShortBuffer)"""
        _STBImage.stbi_image_free(arg0)

    @staticmethod
    @overload
    def nstbi_loadf_from_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf_from_memory(long,int,long,long,long,int)"""
        return int._wrap(_STBImage.nstbi_loadf_from_memory(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_info_from_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info_from_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool._wrap(_STBImage.stbi_info_from_memory(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stbi_zlib_decode_noheader_malloc(arg0: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_zlib_decode_noheader_malloc(java.nio.ByteBuffer)"""
        return ByteBuffer._wrap(_STBImage.stbi_zlib_decode_noheader_malloc(arg0))

    @staticmethod
    @overload
    def nstbi_load_from_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_from_memory(long,int,long,long,long,int)"""
        return int._wrap(_STBImage.nstbi_load_from_memory(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_failure_reason() -> str:
        """public static java.lang.String org.lwjgl.stb.STBImage.stbi_failure_reason()"""
        return str._wrap(_STBImage.stbi_failure_reason())

    @staticmethod
    @overload
    def stbi_loadf_from_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf_from_memory(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return FloatBuffer._wrap(_STBImage.stbi_loadf_from_memory(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_load_16_from_memory(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16_from_memory(long,int,int[],int[],int[],int)"""
        return int._wrap(_STBImage.nstbi_load_16_from_memory(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_info(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int') -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info(long,int[],int[],int[])"""
        return int._wrap(_STBImage.nstbi_info(_long.valueOf(arg0), arg1, arg2, arg3))

    @staticmethod
    @overload
    def stbi_load_16(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return ShortBuffer._wrap(_STBImage.stbi_load_16(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nstbi_load_16_from_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16_from_memory(long,int,long,long,long,int)"""
        return int._wrap(_STBImage.nstbi_load_16_from_memory(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_info(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool._wrap(_STBImage.stbi_info(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stbi_set_flip_vertically_on_load_thread(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.stbi_set_flip_vertically_on_load_thread(int)"""
        _STBImage.stbi_set_flip_vertically_on_load_thread(_int.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_loadf_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return FloatBuffer._wrap(_STBImage.stbi_loadf_from_callbacks(arg0, _long.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_is_hdr_from_memory(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_hdr_from_memory(long,int)"""
        return int._wrap(_STBImage.nstbi_is_hdr_from_memory(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def stbi_load(arg0: 'CharSequence', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load(java.lang.CharSequence,int[],int[],int[],int)"""
        return ByteBuffer._wrap(_STBImage.stbi_load(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_loadf(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return FloatBuffer._wrap(_STBImage.stbi_loadf(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def stbi_load(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return ByteBuffer._wrap(_STBImage.stbi_load(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_loadf_from_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf_from_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return FloatBuffer._wrap(_STBImage.stbi_loadf_from_memory(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_set_unpremultiply_on_load_thread(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_set_unpremultiply_on_load_thread(int)"""
        _STBImage.nstbi_set_unpremultiply_on_load_thread(_int.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_zlib_decode_malloc_guesssize_headerflag(arg0: 'ByteBuffer', arg1: int, arg2: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_zlib_decode_malloc_guesssize_headerflag(java.nio.ByteBuffer,int,boolean)"""
        return ByteBuffer._wrap(_STBImage.stbi_zlib_decode_malloc_guesssize_headerflag(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbi_failure_reason() -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_failure_reason()"""
        return int._wrap(_STBImage.nstbi_failure_reason())

    @staticmethod
    @overload
    def stbi_load_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ByteBuffer._wrap(_STBImage.stbi_load_from_callbacks(arg0, _long.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_set_unpremultiply_on_load(arg0: bool):
        """public static void org.lwjgl.stb.STBImage.stbi_set_unpremultiply_on_load(boolean)"""
        _STBImage.stbi_set_unpremultiply_on_load(_boolean.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_loadf_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,int[],int[],int[],int)"""
        return FloatBuffer._wrap(_STBImage.stbi_loadf_from_callbacks(arg0, _long.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_zlib_decode_malloc_guesssize(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_zlib_decode_malloc_guesssize(long,int,int,long)"""
        return int._wrap(_STBImage.nstbi_zlib_decode_malloc_guesssize(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def nstbi_load_gif_from_memory(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: 'int', arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_gif_from_memory(long,int,long,int[],int[],int[],int[],int)"""
        return int._wrap(_STBImage.nstbi_load_gif_from_memory(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, arg4, arg5, arg6, _int.valueOf(arg7)))

    @staticmethod
    @overload
    def stbi_load_16(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ShortBuffer._wrap(_STBImage.stbi_load_16(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_load_16(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ShortBuffer._wrap(_STBImage.stbi_load_16(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_loadf(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return FloatBuffer._wrap(_STBImage.stbi_loadf(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_set_unpremultiply_on_load(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_set_unpremultiply_on_load(int)"""
        _STBImage.nstbi_set_unpremultiply_on_load(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nstbi_image_free(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_image_free(long)"""
        _STBImage.nstbi_image_free(_long.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_convert_iphone_png_to_rgb(arg0: bool):
        """public static void org.lwjgl.stb.STBImage.stbi_convert_iphone_png_to_rgb(boolean)"""
        _STBImage.stbi_convert_iphone_png_to_rgb(_boolean.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_set_flip_vertically_on_load(arg0: bool):
        """public static void org.lwjgl.stb.STBImage.stbi_set_flip_vertically_on_load(boolean)"""
        _STBImage.stbi_set_flip_vertically_on_load(_boolean.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_hdr_to_ldr_scale(arg0: float):
        """public static native void org.lwjgl.stb.STBImage.stbi_hdr_to_ldr_scale(float)"""
        _STBImage.stbi_hdr_to_ldr_scale(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def stbi_is_hdr_from_memory(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_hdr_from_memory(java.nio.ByteBuffer)"""
        return bool._wrap(_STBImage.stbi_is_hdr_from_memory(arg0))

    @staticmethod
    @overload
    def stbi_info(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info(java.nio.ByteBuffer,int[],int[],int[])"""
        return bool._wrap(_STBImage.stbi_info(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbi_info_from_memory(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int') -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info_from_memory(long,int,int[],int[],int[])"""
        return int._wrap(_STBImage.nstbi_info_from_memory(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def nstbi_load_16_from_callbacks(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16_from_callbacks(long,long,long,long,long,int)"""
        return int._wrap(_STBImage.nstbi_load_16_from_callbacks(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_set_flip_vertically_on_load(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_set_flip_vertically_on_load(int)"""
        _STBImage.nstbi_set_flip_vertically_on_load(_int.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_load_from_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_from_memory(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return ByteBuffer._wrap(_STBImage.stbi_load_from_memory(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_zlib_decode_malloc(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_zlib_decode_malloc(long,int,long)"""
        return int._wrap(_STBImage.nstbi_zlib_decode_malloc(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbi_loadf(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf(long,int[],int[],int[],int)"""
        return int._wrap(_STBImage.nstbi_loadf(_long.valueOf(arg0), arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_zlib_decode_buffer(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_zlib_decode_buffer(long,int,long,int)"""
        return int._wrap(_STBImage.nstbi_zlib_decode_buffer(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstbi_info_from_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info_from_memory(long,int,long,long,long)"""
        return int._wrap(_STBImage.nstbi_info_from_memory(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_info_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,int[],int[],int[])"""
        return bool._wrap(_STBImage.stbi_info_from_callbacks(arg0, _long.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def nstbi_load_from_memory(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_from_memory(long,int,int[],int[],int[],int)"""
        return int._wrap(_STBImage.nstbi_load_from_memory(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nstbi_convert_iphone_png_to_rgb_thread(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_convert_iphone_png_to_rgb_thread(int)"""
        _STBImage.nstbi_convert_iphone_png_to_rgb_thread(_int.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_load_16_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ShortBuffer._wrap(_STBImage.stbi_load_16_from_callbacks(arg0, _long.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_is_16_bit(arg0: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_16_bit(java.lang.CharSequence)"""
        return bool._wrap(_STBImage.stbi_is_16_bit(arg0))

    @staticmethod
    @overload
    def stbi_image_free(arg0: 'FloatBuffer'):
        """public static void org.lwjgl.stb.STBImage.stbi_image_free(java.nio.FloatBuffer)"""
        _STBImage.stbi_image_free(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def stbi_load(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ByteBuffer._wrap(_STBImage.stbi_load(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_load_gif_from_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_gif_from_memory(long,int,long,long,long,long,long,int)"""
        return int._wrap(_STBImage.nstbi_load_gif_from_memory(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7)))

    @staticmethod
    @overload
    def nstbi_is_16_bit_from_callbacks(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_16_bit_from_callbacks(long,long)"""
        return int._wrap(_STBImage.nstbi_is_16_bit_from_callbacks(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def stbi_image_free(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBImage.stbi_image_free(java.nio.ByteBuffer)"""
        _STBImage.stbi_image_free(arg0)

    @staticmethod
    @overload
    def stbi_ldr_to_hdr_gamma(arg0: float):
        """public static native void org.lwjgl.stb.STBImage.stbi_ldr_to_hdr_gamma(float)"""
        _STBImage.stbi_ldr_to_hdr_gamma(_float.valueOf(arg0))

    @staticmethod
    @overload
    def nstbi_loadf_from_callbacks(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf_from_callbacks(long,long,long,long,long,int)"""
        return int._wrap(_STBImage.nstbi_loadf_from_callbacks(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_info_from_callbacks(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info_from_callbacks(long,long,long,long,long)"""
        return int._wrap(_STBImage.nstbi_info_from_callbacks(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_load_gif_from_memory(arg0: 'ByteBuffer', arg1: 'PointerBuffer', arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int', arg6: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_gif_from_memory(java.nio.ByteBuffer,org.lwjgl.PointerBuffer,int[],int[],int[],int[],int)"""
        return ByteBuffer._wrap(_STBImage.stbi_load_gif_from_memory(arg0, arg1, arg2, arg3, arg4, arg5, _int.valueOf(arg6)))

    @staticmethod
    @overload
    def stbi_is_hdr(arg0: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_hdr(java.lang.CharSequence)"""
        return bool._wrap(_STBImage.stbi_is_hdr(arg0))

    @staticmethod
    @overload
    def stbi_loadf(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return FloatBuffer._wrap(_STBImage.stbi_loadf(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_info_from_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info_from_memory(java.nio.ByteBuffer,int[],int[],int[])"""
        return bool._wrap(_STBImage.stbi_info_from_memory(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbi_zlib_decode_malloc_guesssize_headerflag(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_zlib_decode_malloc_guesssize_headerflag(long,int,int,long,int)"""
        return int._wrap(_STBImage.nstbi_zlib_decode_malloc_guesssize_headerflag(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_hdr_to_ldr_gamma(arg0: float):
        """public static native void org.lwjgl.stb.STBImage.stbi_hdr_to_ldr_gamma(float)"""
        _STBImage.stbi_hdr_to_ldr_gamma(_float.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_zlib_decode_noheader_buffer(arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBImage.stbi_zlib_decode_noheader_buffer(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int._wrap(_STBImage.stbi_zlib_decode_noheader_buffer(arg0, arg1))

    @staticmethod
    @overload
    def stbi_is_hdr_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_hdr_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long)"""
        return bool._wrap(_STBImage.stbi_is_hdr_from_callbacks(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def stbi_load_16(arg0: 'CharSequence', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16(java.lang.CharSequence,int[],int[],int[],int)"""
        return ShortBuffer._wrap(_STBImage.stbi_load_16(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_is_16_bit(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_16_bit(java.nio.ByteBuffer)"""
        return bool._wrap(_STBImage.stbi_is_16_bit(arg0))

    @staticmethod
    @overload
    def stbi_info(arg0: 'CharSequence', arg1: 'int', arg2: 'int', arg3: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info(java.lang.CharSequence,int[],int[],int[])"""
        return bool._wrap(_STBImage.stbi_info(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stbi_load_16_from_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16_from_memory(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return ShortBuffer._wrap(_STBImage.stbi_load_16_from_memory(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_info_from_callbacks(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int') -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info_from_callbacks(long,long,int[],int[],int[])"""
        return int._wrap(_STBImage.nstbi_info_from_callbacks(_long.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def stbi_load_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,int[],int[],int[],int)"""
        return ByteBuffer._wrap(_STBImage.stbi_load_from_callbacks(arg0, _long.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_convert_iphone_png_to_rgb(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_convert_iphone_png_to_rgb(int)"""
        _STBImage.nstbi_convert_iphone_png_to_rgb(_int.valueOf(arg0))

    @staticmethod
    @overload
    def nstbi_loadf(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf(long,long,long,long,int)"""
        return int._wrap(_STBImage.nstbi_loadf(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_is_16_bit(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_16_bit(long)"""
        return int._wrap(_STBImage.nstbi_is_16_bit(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stbi_zlib_decode_buffer(arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBImage.stbi_zlib_decode_buffer(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int._wrap(_STBImage.stbi_zlib_decode_buffer(arg0, arg1))

    @staticmethod
    @overload
    def nstbi_loadf_from_memory(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf_from_memory(long,int,int[],int[],int[],int)"""
        return int._wrap(_STBImage.nstbi_loadf_from_memory(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_zlib_decode_noheader_malloc(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_zlib_decode_noheader_malloc(long,int,long)"""
        return int._wrap(_STBImage.nstbi_zlib_decode_noheader_malloc(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def stbi_zlib_decode_malloc_guesssize(arg0: 'ByteBuffer', arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_zlib_decode_malloc_guesssize(java.nio.ByteBuffer,int)"""
        return ByteBuffer._wrap(_STBImage.stbi_zlib_decode_malloc_guesssize(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbi_load_16_from_callbacks(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16_from_callbacks(long,long,int[],int[],int[],int)"""
        return int._wrap(_STBImage.nstbi_load_16_from_callbacks(_long.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_is_hdr(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_hdr(java.nio.ByteBuffer)"""
        return bool._wrap(_STBImage.stbi_is_hdr(arg0))

    @staticmethod
    @overload
    def stbi_convert_iphone_png_to_rgb_thread(arg0: bool):
        """public static void org.lwjgl.stb.STBImage.stbi_convert_iphone_png_to_rgb_thread(boolean)"""
        _STBImage.stbi_convert_iphone_png_to_rgb_thread(_boolean.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_load_gif_from_memory(arg0: 'ByteBuffer', arg1: 'PointerBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_gif_from_memory(java.nio.ByteBuffer,org.lwjgl.PointerBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ByteBuffer._wrap(_STBImage.stbi_load_gif_from_memory(arg0, arg1, arg2, arg3, arg4, arg5, _int.valueOf(arg6)))

    @staticmethod
    @overload
    def nstbi_load_from_callbacks(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_from_callbacks(long,long,int[],int[],int[],int)"""
        return int._wrap(_STBImage.nstbi_load_from_callbacks(_long.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_zlib_decode_malloc(arg0: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_zlib_decode_malloc(java.nio.ByteBuffer)"""
        return ByteBuffer._wrap(_STBImage.stbi_zlib_decode_malloc(arg0))

    @staticmethod
    @overload
    def nstbi_is_hdr(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_hdr(long)"""
        return int._wrap(_STBImage.nstbi_is_hdr(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstbi_is_16_bit_from_memory(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_16_bit_from_memory(long,int)"""
        return int._wrap(_STBImage.nstbi_is_16_bit_from_memory(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def stbi_is_16_bit_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_16_bit_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long)"""
        return bool._wrap(_STBImage.stbi_is_16_bit_from_callbacks(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def stbi_info_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool._wrap(_STBImage.stbi_info_from_callbacks(arg0, _long.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def stbi_loadf(arg0: 'CharSequence', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf(java.lang.CharSequence,int[],int[],int[],int)"""
        return FloatBuffer._wrap(_STBImage.stbi_loadf(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_load_from_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_from_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ByteBuffer._wrap(_STBImage.stbi_load_from_memory(arg0, arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_is_16_bit_from_memory(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_16_bit_from_memory(java.nio.ByteBuffer)"""
        return bool._wrap(_STBImage.stbi_is_16_bit_from_memory(arg0))

    @staticmethod
    @overload
    def nstbi_load(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load(long,int[],int[],int[],int)"""
        return int._wrap(_STBImage.nstbi_load(_long.valueOf(arg0), arg1, arg2, arg3, _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_loadf_from_callbacks(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf_from_callbacks(long,long,int[],int[],int[],int)"""
        return int._wrap(_STBImage.nstbi_loadf_from_callbacks(_long.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_is_hdr_from_callbacks(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_hdr_from_callbacks(long,long)"""
        return int._wrap(_STBImage.nstbi_is_hdr_from_callbacks(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbi_info(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info(long,long,long,long)"""
        return int._wrap(_STBImage.nstbi_info(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def stbi_load_16_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,int[],int[],int[],int)"""
        return ShortBuffer._wrap(_STBImage.stbi_load_16_from_callbacks(arg0, _long.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_load_from_callbacks(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_from_callbacks(long,long,long,long,long,int)"""
        return int._wrap(_STBImage.nstbi_load_from_callbacks(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_load_16_from_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16_from_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ShortBuffer._wrap(_STBImage.stbi_load_16_from_memory(arg0, arg1, arg2, arg3, _int.valueOf(arg4))) 
 
 
# CLASS: org.lwjgl.stb.STBEasyFont
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import org.lwjgl.stb.STBEasyFont as _STBEasyFont
_STBEasyFont = _STBEasyFont
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBEasyFont():
    """org.lwjgl.stb.STBEasyFont"""
 
    @staticmethod
    def _wrap(java_value: _STBEasyFont) -> 'STBEasyFont':
        return STBEasyFont(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBEasyFont):
        """
        Dynamic initializer for STBEasyFont.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBEasyFont__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBEasyFont__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def stb_easy_font_width(arg0: 'CharSequence') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_width(java.lang.CharSequence)"""
        return int._wrap(_STBEasyFont.stb_easy_font_width(arg0))

    @staticmethod
    @overload
    def stb_easy_font_spacing(arg0: float):
        """public static native void org.lwjgl.stb.STBEasyFont.stb_easy_font_spacing(float)"""
        _STBEasyFont.stb_easy_font_spacing(_float.valueOf(arg0))

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
    def stb_easy_font_width(arg0: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_width(java.nio.ByteBuffer)"""
        return int._wrap(_STBEasyFont.stb_easy_font_width(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nstb_easy_font_height(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBEasyFont.nstb_easy_font_height(long)"""
        return int._wrap(_STBEasyFont.nstb_easy_font_height(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_easy_font_print(arg0: float, arg1: float, arg2: 'ByteBuffer', arg3: 'ByteBuffer', arg4: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_print(float,float,java.nio.ByteBuffer,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int._wrap(_STBEasyFont.stb_easy_font_print(_float.valueOf(arg0), _float.valueOf(arg1), arg2, arg3, arg4))

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
    def stb_easy_font_height(arg0: 'CharSequence') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_height(java.lang.CharSequence)"""
        return int._wrap(_STBEasyFont.stb_easy_font_height(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def stb_easy_font_print(arg0: float, arg1: float, arg2: 'CharSequence', arg3: 'ByteBuffer', arg4: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_print(float,float,java.lang.CharSequence,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int._wrap(_STBEasyFont.stb_easy_font_print(_float.valueOf(arg0), _float.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def nstb_easy_font_width(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBEasyFont.nstb_easy_font_width(long)"""
        return int._wrap(_STBEasyFont.nstb_easy_font_width(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_easy_font_height(arg0: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_height(java.nio.ByteBuffer)"""
        return int._wrap(_STBEasyFont.stb_easy_font_height(arg0))

    @staticmethod
    @overload
    def nstb_easy_font_print(arg0: float, arg1: float, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBEasyFont.nstb_easy_font_print(float,float,long,long,long,int)"""
        return int._wrap(_STBEasyFont.nstb_easy_font_print(_float.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5)))

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
 
 
# CLASS: org.lwjgl.stb.STBRectPack
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBRectPack as _STBRectPack
_STBRectPack = _STBRectPack
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBRectPack():
    """org.lwjgl.stb.STBRectPack"""
 
    @staticmethod
    def _wrap(java_value: _STBRectPack) -> 'STBRectPack':
        return STBRectPack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBRectPack):
        """
        Dynamic initializer for STBRectPack.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBRectPack__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBRectPack__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nstbrp_setup_allow_out_of_mem(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBRectPack.nstbrp_setup_allow_out_of_mem(long,int)"""
        _STBRectPack.nstbrp_setup_allow_out_of_mem(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def stbrp_setup_heuristic(arg0: 'STBRPContext', arg1: int):
        """public static void org.lwjgl.stb.STBRectPack.stbrp_setup_heuristic(org.lwjgl.stb.STBRPContext,int)"""
        _STBRectPack.stbrp_setup_heuristic(arg0, _int.valueOf(arg1))

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
    def nstbrp_init_target(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.stb.STBRectPack.nstbrp_init_target(long,int,int,long,int)"""
        _STBRectPack.nstbrp_init_target(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

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
    def nstbrp_setup_heuristic(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBRectPack.nstbrp_setup_heuristic(long,int)"""
        _STBRectPack.nstbrp_setup_heuristic(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def stbrp_pack_rects(arg0: 'STBRPContext', arg1: 'Buffer') -> int:
        """public static int org.lwjgl.stb.STBRectPack.stbrp_pack_rects(org.lwjgl.stb.STBRPContext,org.lwjgl.stb.STBRPRect$Buffer)"""
        return int._wrap(_STBRectPack.stbrp_pack_rects(arg0, arg1))

    @staticmethod
    @overload
    def stbrp_setup_allow_out_of_mem(arg0: 'STBRPContext', arg1: bool):
        """public static void org.lwjgl.stb.STBRectPack.stbrp_setup_allow_out_of_mem(org.lwjgl.stb.STBRPContext,boolean)"""
        _STBRectPack.stbrp_setup_allow_out_of_mem(arg0, _boolean.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nstbrp_pack_rects(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBRectPack.nstbrp_pack_rects(long,long,int)"""
        return int._wrap(_STBRectPack.nstbrp_pack_rects(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def stbrp_init_target(arg0: 'STBRPContext', arg1: int, arg2: int, arg3: 'Buffer'):
        """public static void org.lwjgl.stb.STBRectPack.stbrp_init_target(org.lwjgl.stb.STBRPContext,int,int,org.lwjgl.stb.STBRPNode$Buffer)"""
        _STBRectPack.stbrp_init_target(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.stb.STBIReadCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.stb.STBIReadCallback as _STBIReadCallback
_STBIReadCallback = _STBIReadCallback
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
import org.lwjgl.stb.STBIReadCallbackI as _STBIReadCallbackI
_STBIReadCallbackI = _STBIReadCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBIReadCallback():
    """org.lwjgl.stb.STBIReadCallback"""
 
    @staticmethod
    def _wrap(java_value: _STBIReadCallback) -> 'STBIReadCallback':
        return STBIReadCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBIReadCallback):
        """
        Dynamic initializer for STBIReadCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBIReadCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBIReadCallback__wrapper":
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

    @staticmethod
    @overload
    def getData(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBIReadCallback.getData(long,int)"""
        return ByteBuffer._wrap(_STBIReadCallback.getData(_long.valueOf(arg0), _int.valueOf(arg1)))

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract int org.lwjgl.stb.STBIReadCallbackI.invoke(long,long,int)"""
        pass

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
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIReadCallbackI.callback(long,long)"""
        super(_STBIReadCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'STBIReadCallbackI') -> 'STBIReadCallback':
        """public static org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIReadCallback.create(org.lwjgl.stb.STBIReadCallbackI)"""
        return STBIReadCallback._wrap(_STBIReadCallback.create(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBIReadCallback':
        """public static org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIReadCallback.create(long)"""
        return STBIReadCallback._wrap(_STBIReadCallback.create(_long.valueOf(arg0)))

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

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIReadCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(STBIReadCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBIReadCallback':
        """public static org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIReadCallback.createSafe(long)"""
        return STBIReadCallback._wrap(_STBIReadCallback.createSafe(_long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.stb.STBImageResize
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.nio.ShortBuffer as ShortBuffer
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Float as _float
import org.lwjgl.stb.STBImageResize as _STBImageResize
_STBImageResize = _STBImageResize
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBImageResize():
    """org.lwjgl.stb.STBImageResize"""
 
    @staticmethod
    def _wrap(java_value: _STBImageResize) -> 'STBImageResize':
        return STBImageResize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBImageResize):
        """
        Dynamic initializer for STBImageResize.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBImageResize__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBImageResize__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def stbir_resize(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int,int,int,int,int,int,int)"""
        return bool._wrap(_STBImageResize.stbir_resize(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16)))

    @staticmethod
    @overload
    def stbir_resize_uint8_srgb_edgemode(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint8_srgb_edgemode(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int,int)"""
        return bool._wrap(_STBImageResize.stbir_resize_uint8_srgb_edgemode(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11)))

    @staticmethod
    @overload
    def stbir_resize_uint8_generic(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint8_generic(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int,int,int,int)"""
        return bool._wrap(_STBImageResize.stbir_resize_uint8_generic(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13)))

    @staticmethod
    @overload
    def stbir_resize_subpixel(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: float, arg18: float, arg19: float, arg20: float) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_subpixel(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int,int,int,int,int,int,int,float,float,float,float)"""
        return bool._wrap(_STBImageResize.stbir_resize_subpixel(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16), _float.valueOf(arg17), _float.valueOf(arg18), _float.valueOf(arg19), _float.valueOf(arg20)))

    @staticmethod
    @overload
    def nstbir_resize_float(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_float(float[],int,int,int,float[],int,int,int,int)"""
        return int._wrap(_STBImageResize.nstbir_resize_float(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8)))

    @staticmethod
    @overload
    def nstbir_resize_uint8_generic(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint8_generic(long,int,int,int,long,int,int,int,int,int,int,int,int,int,long)"""
        return int._wrap(_STBImageResize.nstbir_resize_uint8_generic(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _long.valueOf(arg14)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nstbir_resize_float_generic(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_float_generic(float[],int,int,int,float[],int,int,int,int,int,int,int,int,int,long)"""
        return int._wrap(_STBImageResize.nstbir_resize_float_generic(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _long.valueOf(arg14)))

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
    def nstbir_resize_uint8_srgb(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint8_srgb(long,int,int,int,long,int,int,int,int,int,int)"""
        return int._wrap(_STBImageResize.nstbir_resize_uint8_srgb(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10)))

    @staticmethod
    @overload
    def stbir_resize_float_generic(arg0: 'FloatBuffer', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_float_generic(java.nio.FloatBuffer,int,int,int,java.nio.FloatBuffer,int,int,int,int,int,int,int,int,int)"""
        return bool._wrap(_STBImageResize.stbir_resize_float_generic(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13)))

    @staticmethod
    @overload
    def nstbir_resize_subpixel(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: float, arg19: float, arg20: float, arg21: float) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_subpixel(long,int,int,int,long,int,int,int,int,int,int,int,int,int,int,int,int,long,float,float,float,float)"""
        return int._wrap(_STBImageResize.nstbir_resize_subpixel(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16), _long.valueOf(arg17), _float.valueOf(arg18), _float.valueOf(arg19), _float.valueOf(arg20), _float.valueOf(arg21)))

    @staticmethod
    @overload
    def nstbir_resize_float(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_float(long,int,int,int,long,int,int,int,int)"""
        return int._wrap(_STBImageResize.nstbir_resize_float(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8)))

    @staticmethod
    @overload
    def stbir_resize_region(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: float, arg18: float, arg19: float, arg20: float) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_region(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int,int,int,int,int,int,int,float,float,float,float)"""
        return bool._wrap(_STBImageResize.stbir_resize_region(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16), _float.valueOf(arg17), _float.valueOf(arg18), _float.valueOf(arg19), _float.valueOf(arg20)))

    @staticmethod
    @overload
    def nstbir_resize_uint8_srgb_edgemode(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint8_srgb_edgemode(long,int,int,int,long,int,int,int,int,int,int,int)"""
        return int._wrap(_STBImageResize.nstbir_resize_uint8_srgb_edgemode(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11)))

    @staticmethod
    @overload
    def stbir_resize_float_generic(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_float_generic(float[],int,int,int,float[],int,int,int,int,int,int,int,int,int)"""
        return bool._wrap(_STBImageResize.stbir_resize_float_generic(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def stbir_resize_float(arg0: 'FloatBuffer', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer', arg5: int, arg6: int, arg7: int, arg8: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_float(java.nio.FloatBuffer,int,int,int,java.nio.FloatBuffer,int,int,int,int)"""
        return bool._wrap(_STBImageResize.stbir_resize_float(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8)))

    @staticmethod
    @overload
    def stbir_resize_uint8_srgb(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint8_srgb(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int)"""
        return bool._wrap(_STBImageResize.stbir_resize_uint8_srgb(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10)))

    @staticmethod
    @overload
    def stbir_resize_uint8(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint8(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int)"""
        return bool._wrap(_STBImageResize.stbir_resize_uint8(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nstbir_resize_uint16_generic(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint16_generic(long,int,int,int,long,int,int,int,int,int,int,int,int,int,long)"""
        return int._wrap(_STBImageResize.nstbir_resize_uint16_generic(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _long.valueOf(arg14)))

    @staticmethod
    @overload
    def stbir_resize_float(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int, arg6: int, arg7: int, arg8: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_float(float[],int,int,int,float[],int,int,int,int)"""
        return bool._wrap(_STBImageResize.stbir_resize_float(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8)))

    @staticmethod
    @overload
    def nstbir_resize_uint16_generic(arg0: 'short', arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint16_generic(short[],int,int,int,short[],int,int,int,int,int,int,int,int,int,long)"""
        return int._wrap(_STBImageResize.nstbir_resize_uint16_generic(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _long.valueOf(arg14)))

    @staticmethod
    @overload
    def stbir_resize_uint16_generic(arg0: 'short', arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint16_generic(short[],int,int,int,short[],int,int,int,int,int,int,int,int,int)"""
        return bool._wrap(_STBImageResize.stbir_resize_uint16_generic(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nstbir_resize_float_generic(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_float_generic(long,int,int,int,long,int,int,int,int,int,int,int,int,int,long)"""
        return int._wrap(_STBImageResize.nstbir_resize_float_generic(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _long.valueOf(arg14)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def stbir_resize_uint16_generic(arg0: 'ShortBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ShortBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint16_generic(java.nio.ShortBuffer,int,int,int,java.nio.ShortBuffer,int,int,int,int,int,int,int,int,int)"""
        return bool._wrap(_STBImageResize.stbir_resize_uint16_generic(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13)))

    @staticmethod
    @overload
    def nstbir_resize(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize(long,int,int,int,long,int,int,int,int,int,int,int,int,int,int,int,int,long)"""
        return int._wrap(_STBImageResize.nstbir_resize(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16), _long.valueOf(arg17)))

    @staticmethod
    @overload
    def nstbir_resize_region(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: float, arg19: float, arg20: float, arg21: float) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_region(long,int,int,int,long,int,int,int,int,int,int,int,int,int,int,int,int,long,float,float,float,float)"""
        return int._wrap(_STBImageResize.nstbir_resize_region(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16), _long.valueOf(arg17), _float.valueOf(arg18), _float.valueOf(arg19), _float.valueOf(arg20), _float.valueOf(arg21)))

    @staticmethod
    @overload
    def nstbir_resize_uint8(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint8(long,int,int,int,long,int,int,int,int)"""
        return int._wrap(_STBImageResize.nstbir_resize_uint8(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8)))

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
 
 
# CLASS: org.lwjgl.stb.STBTTFontinfo
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
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBTTFontinfo as _STBTTFontinfo_Buffer
_Buffer = _STBTTFontinfo_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.stb.STBTTFontinfo as _STBTTFontinfo
_STBTTFontinfo = _STBTTFontinfo
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBTTFontinfo():
    """org.lwjgl.stb.STBTTFontinfo"""
 
    @staticmethod
    def _wrap(java_value: _STBTTFontinfo) -> 'STBTTFontinfo':
        return STBTTFontinfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBTTFontinfo):
        """
        Dynamic initializer for STBTTFontinfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBTTFontinfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBTTFontinfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTFontinfo.mallocStack(_int.valueOf(arg0), arg1))

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
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.create(int)"""
        return Buffer._wrap(_STBTTFontinfo.create(_int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTFontinfo.sizeof()"""
        return int._wrap(super(STBTTFontinfo, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.create(long)"""
        return STBTTFontinfo._wrap(_STBTTFontinfo.create(_long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTFontinfo._wrap(_STBTTFontinfo.malloc(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTFontinfo._wrap(_STBTTFontinfo.callocStack(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.createSafe(long)"""
        return STBTTFontinfo._wrap(_STBTTFontinfo.createSafe(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTFontinfo(java.nio.ByteBuffer)"""
        val = _STBTTFontinfo(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.create(long,int)"""
        return Buffer._wrap(_STBTTFontinfo.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTFontinfo.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.mallocStack(int)"""
        return Buffer._wrap(_STBTTFontinfo.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.callocStack()"""
        return STBTTFontinfo._wrap(_STBTTFontinfo.callocStack())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTFontinfo._wrap(_STBTTFontinfo.mallocStack(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTFontinfo._wrap(_STBTTFontinfo.calloc(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc() -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.calloc()"""
        return STBTTFontinfo._wrap(_STBTTFontinfo.calloc())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def create() -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.create()"""
        return STBTTFontinfo._wrap(_STBTTFontinfo.create())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.callocStack(int)"""
        return Buffer._wrap(_STBTTFontinfo.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTFontinfo.callocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.createSafe(long,int)"""
        return Buffer._wrap(_STBTTFontinfo.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.malloc(int)"""
        return Buffer._wrap(_STBTTFontinfo.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.mallocStack()"""
        return STBTTFontinfo._wrap(_STBTTFontinfo.mallocStack())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def malloc() -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.malloc()"""
        return STBTTFontinfo._wrap(_STBTTFontinfo.malloc())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.calloc(int)"""
        return Buffer._wrap(_STBTTFontinfo.calloc(_int.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTFontinfo.calloc(_int.valueOf(arg0), arg1))

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

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address()) 
 
 
# CLASS: org.lwjgl.stb.STBIEOFCallback
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
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.stb.STBIEOFCallback as _STBIEOFCallback
_STBIEOFCallback = _STBIEOFCallback
import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
import org.lwjgl.stb.STBIEOFCallbackI as _STBIEOFCallbackI
_STBIEOFCallbackI = _STBIEOFCallbackI
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBIEOFCallback():
    """org.lwjgl.stb.STBIEOFCallback"""
 
    @staticmethod
    def _wrap(java_value: _STBIEOFCallback) -> 'STBIEOFCallback':
        return STBIEOFCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBIEOFCallback):
        """
        Dynamic initializer for STBIEOFCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBIEOFCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBIEOFCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: 'STBIEOFCallbackI') -> 'STBIEOFCallback':
        """public static org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIEOFCallback.create(org.lwjgl.stb.STBIEOFCallbackI)"""
        return STBIEOFCallback._wrap(_STBIEOFCallback.create(arg0))

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBIEOFCallback':
        """public static org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIEOFCallback.create(long)"""
        return STBIEOFCallback._wrap(_STBIEOFCallback.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBIEOFCallback':
        """public static org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIEOFCallback.createSafe(long)"""
        return STBIEOFCallback._wrap(_STBIEOFCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIEOFCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(STBIEOFCallbackI, self).getCallInterface())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract int org.lwjgl.stb.STBIEOFCallbackI.invoke(long)"""
        pass

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIEOFCallbackI.callback(long,long)"""
        super(_STBIEOFCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.stb.STBIIOCallbacks
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.stb.STBIIOCallbacks as _STBIIOCallbacks
_STBIIOCallbacks = _STBIIOCallbacks
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.stb.STBIReadCallback as _STBIReadCallback
_STBIReadCallback = _STBIReadCallback
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBISkipCallback as _STBISkipCallback
_STBISkipCallback = _STBISkipCallback
import org.lwjgl.stb.STBIEOFCallback as _STBIEOFCallback
_STBIEOFCallback = _STBIEOFCallback
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.stb.STBIIOCallbacks as _STBIIOCallbacks_Buffer
_Buffer = _STBIIOCallbacks_Buffer.Buffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBIIOCallbacks():
    """org.lwjgl.stb.STBIIOCallbacks"""
 
    @staticmethod
    def _wrap(java_value: _STBIIOCallbacks) -> 'STBIIOCallbacks':
        return STBIIOCallbacks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBIIOCallbacks):
        """
        Dynamic initializer for STBIIOCallbacks.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBIIOCallbacks__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBIIOCallbacks__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def neof(arg0: int, arg1: 'STBIEOFCallbackI'):
        """public static void org.lwjgl.stb.STBIIOCallbacks.neof(long,org.lwjgl.stb.STBIEOFCallbackI)"""
        _STBIIOCallbacks.neof(_long.valueOf(arg0), arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def neof(arg0: int) -> 'STBIEOFCallback':
        """public static org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIIOCallbacks.neof(long)"""
        return STBIEOFCallback._wrap(_STBIIOCallbacks.neof(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.createSafe(long,int)"""
        return Buffer._wrap(_STBIIOCallbacks.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nskip(arg0: int, arg1: 'STBISkipCallbackI'):
        """public static void org.lwjgl.stb.STBIIOCallbacks.nskip(long,org.lwjgl.stb.STBISkipCallbackI)"""
        _STBIIOCallbacks.nskip(_long.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBIIOCallbacks._wrap(_STBIIOCallbacks.mallocStack(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBIIOCallbacks.callocStack(_int.valueOf(arg0), arg1))

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
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.create(int)"""
        return Buffer._wrap(_STBIIOCallbacks.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.create(long,int)"""
        return Buffer._wrap(_STBIIOCallbacks.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack() -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.callocStack()"""
        return STBIIOCallbacks._wrap(_STBIIOCallbacks.callocStack())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBIIOCallbacks._wrap(_STBIIOCallbacks.callocStack(arg0))

    @staticmethod
    @overload
    def calloc() -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.calloc()"""
        return STBIIOCallbacks._wrap(_STBIIOCallbacks.calloc())

    @overload
    def read(self, arg0: 'STBIReadCallbackI') -> 'STBIIOCallbacks':
        """public org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.read(org.lwjgl.stb.STBIReadCallbackI)"""
        return 'STBIIOCallbacks'._wrap(super(_STBIIOCallbacks, self).read(arg0))

    @staticmethod
    @overload
    def malloc() -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.malloc()"""
        return STBIIOCallbacks._wrap(_STBIIOCallbacks.malloc())

    @overload
    def read(self) -> 'STBIReadCallback':
        """public org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIIOCallbacks.read()"""
        return 'STBIReadCallback'._wrap(super(STBIIOCallbacks, self).read())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBIIOCallbacks.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.calloc(org.lwjgl.system.MemoryStack)"""
        return STBIIOCallbacks._wrap(_STBIIOCallbacks.calloc(arg0))

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

    @overload
    def skip(self) -> 'STBISkipCallback':
        """public org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBIIOCallbacks.skip()"""
        return 'STBISkipCallback'._wrap(super(STBIIOCallbacks, self).skip())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.malloc(int)"""
        return Buffer._wrap(_STBIIOCallbacks.malloc(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBIIOCallbacks.mallocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def skip(self, arg0: 'STBISkipCallbackI') -> 'STBIIOCallbacks':
        """public org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.skip(org.lwjgl.stb.STBISkipCallbackI)"""
        return 'STBIIOCallbacks'._wrap(super(_STBIIOCallbacks, self).skip(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBIIOCallbacks.sizeof()"""
        return int._wrap(super(STBIIOCallbacks, self).sizeof())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBIIOCallbacks(java.nio.ByteBuffer)"""
        val = _STBIIOCallbacks(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def mallocStack() -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.mallocStack()"""
        return STBIIOCallbacks._wrap(_STBIIOCallbacks.mallocStack())

    @overload
    def set(self, arg0: 'STBIIOCallbacks') -> 'STBIIOCallbacks':
        """public org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.set(org.lwjgl.stb.STBIIOCallbacks)"""
        return 'STBIIOCallbacks'._wrap(super(_STBIIOCallbacks, self).set(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBIIOCallbacks.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.calloc(int)"""
        return Buffer._wrap(_STBIIOCallbacks.calloc(_int.valueOf(arg0)))

    @overload
    def eof(self) -> 'STBIEOFCallback':
        """public org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIIOCallbacks.eof()"""
        return 'STBIEOFCallback'._wrap(super(STBIIOCallbacks, self).eof())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.createSafe(long)"""
        return STBIIOCallbacks._wrap(_STBIIOCallbacks.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nread(arg0: int) -> 'STBIReadCallback':
        """public static org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIIOCallbacks.nread(long)"""
        return STBIReadCallback._wrap(_STBIIOCallbacks.nread(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.malloc(org.lwjgl.system.MemoryStack)"""
        return STBIIOCallbacks._wrap(_STBIIOCallbacks.malloc(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.mallocStack(int)"""
        return Buffer._wrap(_STBIIOCallbacks.mallocStack(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'STBIReadCallbackI', arg1: 'STBISkipCallbackI', arg2: 'STBIEOFCallbackI') -> 'STBIIOCallbacks':
        """public org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.set(org.lwjgl.stb.STBIReadCallbackI,org.lwjgl.stb.STBISkipCallbackI,org.lwjgl.stb.STBIEOFCallbackI)"""
        return 'STBIIOCallbacks'._wrap(super(_STBIIOCallbacks, self).set(arg0, arg1, arg2))

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
    def nread(arg0: int, arg1: 'STBIReadCallbackI'):
        """public static void org.lwjgl.stb.STBIIOCallbacks.nread(long,org.lwjgl.stb.STBIReadCallbackI)"""
        _STBIIOCallbacks.nread(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.create(long)"""
        return STBIIOCallbacks._wrap(_STBIIOCallbacks.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.stb.STBIIOCallbacks.validate(long)"""
        _STBIIOCallbacks.validate(_long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create() -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.create()"""
        return STBIIOCallbacks._wrap(_STBIIOCallbacks.create())

    @overload
    def eof(self, arg0: 'STBIEOFCallbackI') -> 'STBIIOCallbacks':
        """public org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.eof(org.lwjgl.stb.STBIEOFCallbackI)"""
        return 'STBIIOCallbacks'._wrap(super(_STBIIOCallbacks, self).eof(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.callocStack(int)"""
        return Buffer._wrap(_STBIIOCallbacks.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nskip(arg0: int) -> 'STBISkipCallback':
        """public static org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBIIOCallbacks.nskip(long)"""
        return STBISkipCallback._wrap(_STBIIOCallbacks.nskip(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBTTBakedChar
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
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBTTBakedChar as _STBTTBakedChar
_STBTTBakedChar = _STBTTBakedChar
import java.lang.Integer as _int
import org.lwjgl.stb.STBTTBakedChar as _STBTTBakedChar_Buffer
_Buffer = _STBTTBakedChar_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBTTBakedChar():
    """org.lwjgl.stb.STBTTBakedChar"""
 
    @staticmethod
    def _wrap(java_value: _STBTTBakedChar) -> 'STBTTBakedChar':
        return STBTTBakedChar(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBTTBakedChar):
        """
        Dynamic initializer for STBTTBakedChar.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBTTBakedChar__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBTTBakedChar__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def xoff(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar.xoff()"""
        return float._wrap(super(STBTTBakedChar, self).xoff())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTBakedChar._wrap(_STBTTBakedChar.malloc(arg0))

    @staticmethod
    @overload
    def callocStack() -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.callocStack()"""
        return STBTTBakedChar._wrap(_STBTTBakedChar.callocStack())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def x0(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar.x0()"""
        return int._wrap(super(STBTTBakedChar, self).x0())

    @staticmethod
    @overload
    def ny0(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTBakedChar.ny0(long)"""
        return int._wrap(_STBTTBakedChar.ny0(_long.valueOf(arg0)))

    @overload
    def y1(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar.y1()"""
        return int._wrap(super(STBTTBakedChar, self).y1())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.mallocStack(int)"""
        return Buffer._wrap(_STBTTBakedChar.mallocStack(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create() -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.create()"""
        return STBTTBakedChar._wrap(_STBTTBakedChar.create())

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
    def nxoff(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTBakedChar.nxoff(long)"""
        return float._wrap(_STBTTBakedChar.nxoff(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTBakedChar._wrap(_STBTTBakedChar.callocStack(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.callocStack(int)"""
        return Buffer._wrap(_STBTTBakedChar.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.create(long,int)"""
        return Buffer._wrap(_STBTTBakedChar.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTBakedChar.sizeof()"""
        return int._wrap(super(STBTTBakedChar, self).sizeof())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.create(int)"""
        return Buffer._wrap(_STBTTBakedChar.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.calloc(int)"""
        return Buffer._wrap(_STBTTBakedChar.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTBakedChar.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.create(long)"""
        return STBTTBakedChar._wrap(_STBTTBakedChar.create(_long.valueOf(arg0)))

    @overload
    def y0(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar.y0()"""
        return int._wrap(super(STBTTBakedChar, self).y0())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def x1(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar.x1()"""
        return int._wrap(super(STBTTBakedChar, self).x1())

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
    def malloc() -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.malloc()"""
        return STBTTBakedChar._wrap(_STBTTBakedChar.malloc())

    @staticmethod
    @overload
    def nx1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTBakedChar.nx1(long)"""
        return int._wrap(_STBTTBakedChar.nx1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.calloc()"""
        return STBTTBakedChar._wrap(_STBTTBakedChar.calloc())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ny1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTBakedChar.ny1(long)"""
        return int._wrap(_STBTTBakedChar.ny1(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTBakedChar._wrap(_STBTTBakedChar.mallocStack(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTBakedChar.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.createSafe(long)"""
        return STBTTBakedChar._wrap(_STBTTBakedChar.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nx0(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTBakedChar.nx0(long)"""
        return int._wrap(_STBTTBakedChar.nx0(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTBakedChar._wrap(_STBTTBakedChar.calloc(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nyoff(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTBakedChar.nyoff(long)"""
        return float._wrap(_STBTTBakedChar.nyoff(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.mallocStack()"""
        return STBTTBakedChar._wrap(_STBTTBakedChar.mallocStack())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.malloc(int)"""
        return Buffer._wrap(_STBTTBakedChar.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTBakedChar.calloc(_int.valueOf(arg0), arg1))

    @overload
    def xadvance(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar.xadvance()"""
        return float._wrap(super(STBTTBakedChar, self).xadvance())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTBakedChar.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.createSafe(long,int)"""
        return Buffer._wrap(_STBTTBakedChar.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTBakedChar(java.nio.ByteBuffer)"""
        val = _STBTTBakedChar(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @overload
    def yoff(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar.yoff()"""
        return float._wrap(super(STBTTBakedChar, self).yoff())

    @staticmethod
    @overload
    def nxadvance(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTBakedChar.nxadvance(long)"""
        return float._wrap(_STBTTBakedChar.nxadvance(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBTTPackContext
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
import org.lwjgl.stb.STBTTPackContext as _STBTTPackContext_Buffer
_Buffer = _STBTTPackContext_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBRPNode as _STBRPNode_Buffer
_Buffer = _STBRPNode_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.stb.STBRPContext as _STBRPContext
_STBRPContext = _STBRPContext
import org.lwjgl.stb.STBTTPackContext as _STBTTPackContext
_STBTTPackContext = _STBTTPackContext
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBTTPackContext():
    """org.lwjgl.stb.STBTTPackContext"""
 
    @staticmethod
    def _wrap(java_value: _STBTTPackContext) -> 'STBTTPackContext':
        return STBTTPackContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBTTPackContext):
        """
        Dynamic initializer for STBTTPackContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBTTPackContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBTTPackContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackContext.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nuser_allocator_context(arg0: int) -> int:
        """public static long org.lwjgl.stb.STBTTPackContext.nuser_allocator_context(long)"""
        return int._wrap(_STBTTPackContext.nuser_allocator_context(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.create(long)"""
        return STBTTPackContext._wrap(_STBTTPackContext.create(_long.valueOf(arg0)))

    @overload
    def height(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.height()"""
        return int._wrap(super(STBTTPackContext, self).height())

    @staticmethod
    @overload
    def nv_oversample(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nv_oversample(long)"""
        return int._wrap(_STBTTPackContext.nv_oversample(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.calloc()"""
        return STBTTPackContext._wrap(_STBTTPackContext.calloc())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def npixels(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTTPackContext.npixels(long,int)"""
        return ByteBuffer._wrap(_STBTTPackContext.npixels(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackContext(java.nio.ByteBuffer)"""
        val = _STBTTPackContext(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def nodes(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBTTPackContext.nodes(int)"""
        return 'Buffer'._wrap(super(_STBTTPackContext, self).nodes(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def malloc() -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.malloc()"""
        return STBTTPackContext._wrap(_STBTTPackContext.malloc())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.callocStack(int)"""
        return Buffer._wrap(_STBTTPackContext.callocStack(_int.valueOf(arg0)))

    @overload
    def h_oversample(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.h_oversample()"""
        return int._wrap(super(STBTTPackContext, self).h_oversample())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.calloc(int)"""
        return Buffer._wrap(_STBTTPackContext.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackContext._wrap(_STBTTPackContext.calloc(arg0))

    @staticmethod
    @overload
    def create() -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.create()"""
        return STBTTPackContext._wrap(_STBTTPackContext.create())

    @staticmethod
    @overload
    def nheight(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nheight(long)"""
        return int._wrap(_STBTTPackContext.nheight(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackContext._wrap(_STBTTPackContext.callocStack(arg0))

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

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.sizeof()"""
        return int._wrap(super(STBTTPackContext, self).sizeof())

    @overload
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBTTPackContext.pixels(int)"""
        return 'ByteBuffer'._wrap(super(_STBTTPackContext, self).pixels(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackContext._wrap(_STBTTPackContext.mallocStack(arg0))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackContext._wrap(_STBTTPackContext.malloc(arg0))

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
    def nstride_in_bytes(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nstride_in_bytes(long)"""
        return int._wrap(_STBTTPackContext.nstride_in_bytes(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nskip_missing(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nskip_missing(long)"""
        return int._wrap(_STBTTPackContext.nskip_missing(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.mallocStack()"""
        return STBTTPackContext._wrap(_STBTTPackContext.mallocStack())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackContext.callocStack(_int.valueOf(arg0), arg1))

    @overload
    def padding(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.padding()"""
        return int._wrap(super(STBTTPackContext, self).padding())

    @staticmethod
    @overload
    def callocStack() -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.callocStack()"""
        return STBTTPackContext._wrap(_STBTTPackContext.callocStack())

    @overload
    def v_oversample(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.v_oversample()"""
        return int._wrap(super(STBTTPackContext, self).v_oversample())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.create(int)"""
        return Buffer._wrap(_STBTTPackContext.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.create(long,int)"""
        return Buffer._wrap(_STBTTPackContext.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nh_oversample(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nh_oversample(long)"""
        return int._wrap(_STBTTPackContext.nh_oversample(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.malloc(int)"""
        return Buffer._wrap(_STBTTPackContext.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def npack_info(arg0: int) -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBTTPackContext.npack_info(long)"""
        return STBRPContext._wrap(_STBTTPackContext.npack_info(_long.valueOf(arg0)))

    @overload
    def user_allocator_context(self) -> int:
        """public long org.lwjgl.stb.STBTTPackContext.user_allocator_context()"""
        return int._wrap(super(STBTTPackContext, self).user_allocator_context())

    @overload
    def skip_missing(self) -> bool:
        """public boolean org.lwjgl.stb.STBTTPackContext.skip_missing()"""
        return bool._wrap(super(STBTTPackContext, self).skip_missing())

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

    @overload
    def pack_info(self) -> 'STBRPContext':
        """public org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBTTPackContext.pack_info()"""
        return 'STBRPContext'._wrap(super(STBTTPackContext, self).pack_info())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.createSafe(long)"""
        return STBTTPackContext._wrap(_STBTTPackContext.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.createSafe(long,int)"""
        return Buffer._wrap(_STBTTPackContext.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nwidth(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nwidth(long)"""
        return int._wrap(_STBTTPackContext.nwidth(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def npadding(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.npadding(long)"""
        return int._wrap(_STBTTPackContext.npadding(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nnodes(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBTTPackContext.nnodes(long,int)"""
        return Buffer._wrap(_STBTTPackContext.nnodes(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @overload
    def width(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.width()"""
        return int._wrap(super(STBTTPackContext, self).width())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackContext.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.mallocStack(int)"""
        return Buffer._wrap(_STBTTPackContext.mallocStack(_int.valueOf(arg0)))

    @overload
    def stride_in_bytes(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.stride_in_bytes()"""
        return int._wrap(super(STBTTPackContext, self).stride_in_bytes())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackContext.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBTTPackRange
from pyquantum_helper import import_once as _import_once
import org.lwjgl.stb.STBTTPackedchar as _STBTTPackedchar_Buffer
_Buffer = _STBTTPackedchar_Buffer.Buffer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
from builtins import float
import org.lwjgl.stb.STBTTPackRange as _STBTTPackRange
_STBTTPackRange = _STBTTPackRange
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import java.lang.Byte as _byte
import org.lwjgl.stb.STBTTPackRange as _STBTTPackRange_Buffer
_Buffer = _STBTTPackRange_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBTTPackRange():
    """org.lwjgl.stb.STBTTPackRange"""
 
    @staticmethod
    def _wrap(java_value: _STBTTPackRange) -> 'STBTTPackRange':
        return STBTTPackRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBTTPackRange):
        """
        Dynamic initializer for STBTTPackRange.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBTTPackRange__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBTTPackRange__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def narray_of_unicode_codepoints(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTTPackRange.narray_of_unicode_codepoints(long,java.nio.IntBuffer)"""
        _STBTTPackRange.narray_of_unicode_codepoints(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackRange.callocStack(_int.valueOf(arg0), arg1))

    @overload
    def first_unicode_codepoint_in_range(self) -> int:
        """public int org.lwjgl.stb.STBTTPackRange.first_unicode_codepoint_in_range()"""
        return int._wrap(super(STBTTPackRange, self).first_unicode_codepoint_in_range())

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.stb.STBTTPackRange.validate(long)"""
        _STBTTPackRange.validate(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nh_oversample(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackRange.nh_oversample(long,byte)"""
        _STBTTPackRange.nh_oversample(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackRange._wrap(_STBTTPackRange.mallocStack(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.create(long,int)"""
        return Buffer._wrap(_STBTTPackRange.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nfirst_unicode_codepoint_in_range(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackRange.nfirst_unicode_codepoint_in_range(long)"""
        return int._wrap(_STBTTPackRange.nfirst_unicode_codepoint_in_range(_long.valueOf(arg0)))

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
    def set(self, arg0: 'STBTTPackRange') -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.set(org.lwjgl.stb.STBTTPackRange)"""
        return 'STBTTPackRange'._wrap(super(_STBTTPackRange, self).set(arg0))

    @overload
    def first_unicode_codepoint_in_range(self, arg0: int) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.first_unicode_codepoint_in_range(int)"""
        return 'STBTTPackRange'._wrap(super(_STBTTPackRange, self).first_unicode_codepoint_in_range(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nnum_chars(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackRange.nnum_chars(long,int)"""
        _STBTTPackRange.nnum_chars(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.malloc(int)"""
        return Buffer._wrap(_STBTTPackRange.malloc(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackRange.calloc(_int.valueOf(arg0), arg1))

    @overload
    def v_oversample(self) -> int:
        """public byte org.lwjgl.stb.STBTTPackRange.v_oversample()"""
        return int._wrap(super(STBTTPackRange, self).v_oversample())

    @overload
    def chardata_for_range(self) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackRange.chardata_for_range()"""
        return 'Buffer'._wrap(super(STBTTPackRange, self).chardata_for_range())

    @overload
    def h_oversample(self) -> int:
        """public byte org.lwjgl.stb.STBTTPackRange.h_oversample()"""
        return int._wrap(super(STBTTPackRange, self).h_oversample())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.createSafe(long,int)"""
        return Buffer._wrap(_STBTTPackRange.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def font_size(self) -> float:
        """public float org.lwjgl.stb.STBTTPackRange.font_size()"""
        return float._wrap(super(STBTTPackRange, self).font_size())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackRange._wrap(_STBTTPackRange.malloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.calloc(int)"""
        return Buffer._wrap(_STBTTPackRange.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.calloc()"""
        return STBTTPackRange._wrap(_STBTTPackRange.calloc())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def num_chars(self, arg0: int) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.num_chars(int)"""
        return 'STBTTPackRange'._wrap(super(_STBTTPackRange, self).num_chars(_int.valueOf(arg0)))

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
    def callocStack() -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.callocStack()"""
        return STBTTPackRange._wrap(_STBTTPackRange.callocStack())

    @staticmethod
    @overload
    def narray_of_unicode_codepoints(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.stb.STBTTPackRange.narray_of_unicode_codepoints(long)"""
        return IntBuffer._wrap(_STBTTPackRange.narray_of_unicode_codepoints(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackRange._wrap(_STBTTPackRange.calloc(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: float, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'Buffer', arg5: int, arg6: int) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.set(float,int,java.nio.IntBuffer,int,org.lwjgl.stb.STBTTPackedchar$Buffer,byte,byte)"""
        return 'STBTTPackRange'._wrap(super(_STBTTPackRange, self).set(_float.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), arg4, _byte.valueOf(arg5), _byte.valueOf(arg6)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackRange.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.create(long)"""
        return STBTTPackRange._wrap(_STBTTPackRange.create(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackRange(java.nio.ByteBuffer)"""
        val = _STBTTPackRange(arg0)
        self.__wrapper = val

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nv_oversample(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackRange.nv_oversample(long,byte)"""
        _STBTTPackRange.nv_oversample(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def nnum_chars(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackRange.nnum_chars(long)"""
        return int._wrap(_STBTTPackRange.nnum_chars(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.createSafe(long)"""
        return STBTTPackRange._wrap(_STBTTPackRange.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nfont_size(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackRange.nfont_size(long)"""
        return float._wrap(_STBTTPackRange.nfont_size(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nh_oversample(arg0: int) -> int:
        """public static byte org.lwjgl.stb.STBTTPackRange.nh_oversample(long)"""
        return int._wrap(_STBTTPackRange.nh_oversample(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nfirst_unicode_codepoint_in_range(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackRange.nfirst_unicode_codepoint_in_range(long,int)"""
        _STBTTPackRange.nfirst_unicode_codepoint_in_range(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def h_oversample(self, arg0: int) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.h_oversample(byte)"""
        return 'STBTTPackRange'._wrap(super(_STBTTPackRange, self).h_oversample(_byte.valueOf(arg0)))

    @overload
    def font_size(self, arg0: float) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.font_size(float)"""
        return 'STBTTPackRange'._wrap(super(_STBTTPackRange, self).font_size(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.callocStack(int)"""
        return Buffer._wrap(_STBTTPackRange.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.mallocStack()"""
        return STBTTPackRange._wrap(_STBTTPackRange.mallocStack())

    @staticmethod
    @overload
    def malloc() -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.malloc()"""
        return STBTTPackRange._wrap(_STBTTPackRange.malloc())

    @overload
    def array_of_unicode_codepoints(self, arg0: 'IntBuffer') -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.array_of_unicode_codepoints(java.nio.IntBuffer)"""
        return 'STBTTPackRange'._wrap(super(_STBTTPackRange, self).array_of_unicode_codepoints(arg0))

    @staticmethod
    @overload
    def nv_oversample(arg0: int) -> int:
        """public static byte org.lwjgl.stb.STBTTPackRange.nv_oversample(long)"""
        return int._wrap(_STBTTPackRange.nv_oversample(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nchardata_for_range(arg0: int, arg1: 'Buffer'):
        """public static void org.lwjgl.stb.STBTTPackRange.nchardata_for_range(long,org.lwjgl.stb.STBTTPackedchar$Buffer)"""
        _STBTTPackRange.nchardata_for_range(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.create(int)"""
        return Buffer._wrap(_STBTTPackRange.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackRange._wrap(_STBTTPackRange.callocStack(arg0))

    @staticmethod
    @overload
    def create() -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.create()"""
        return STBTTPackRange._wrap(_STBTTPackRange.create())

    @overload
    def num_chars(self) -> int:
        """public int org.lwjgl.stb.STBTTPackRange.num_chars()"""
        return int._wrap(super(STBTTPackRange, self).num_chars())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def array_of_unicode_codepoints(self) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.stb.STBTTPackRange.array_of_unicode_codepoints()"""
        return 'IntBuffer'._wrap(super(STBTTPackRange, self).array_of_unicode_codepoints())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def nchardata_for_range(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackRange.nchardata_for_range(long)"""
        return Buffer._wrap(_STBTTPackRange.nchardata_for_range(_long.valueOf(arg0)))

    @overload
    def v_oversample(self, arg0: int) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.v_oversample(byte)"""
        return 'STBTTPackRange'._wrap(super(_STBTTPackRange, self).v_oversample(_byte.valueOf(arg0)))

    @overload
    def chardata_for_range(self, arg0: 'Buffer') -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.chardata_for_range(org.lwjgl.stb.STBTTPackedchar$Buffer)"""
        return 'STBTTPackRange'._wrap(super(_STBTTPackRange, self).chardata_for_range(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTPackRange.malloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTPackRange.sizeof()"""
        return int._wrap(super(STBTTPackRange, self).sizeof())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nfont_size(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackRange.nfont_size(long,float)"""
        _STBTTPackRange.nfont_size(_long.valueOf(arg0), _float.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.mallocStack(int)"""
        return Buffer._wrap(_STBTTPackRange.mallocStack(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBIEOFCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import org.lwjgl.stb.STBIEOFCallbackI as _STBIEOFCallbackI
_STBIEOFCallbackI = _STBIEOFCallbackI
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class STBIEOFCallbackI():
    """org.lwjgl.stb.STBIEOFCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _STBIEOFCallbackI) -> 'STBIEOFCallbackI':
        return STBIEOFCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBIEOFCallbackI):
        """
        Dynamic initializer for STBIEOFCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBIEOFCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBIEOFCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract int org.lwjgl.stb.STBIEOFCallbackI.invoke(long)"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIEOFCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(STBIEOFCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIEOFCallbackI.callback(long,long)"""
        super(_STBIEOFCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.stb.STBTTPackedchar$Buffer
from pyquantum_helper import import_once as _import_once
import org.lwjgl.stb.STBTTPackedchar as _STBTTPackedchar_Buffer
_Buffer = _STBTTPackedchar_Buffer.Buffer
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.lang.Short as _short
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
import java.lang.Float as _float
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
    """org.lwjgl.stb.STBTTPackedchar.Buffer"""
 
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

    @overload
    def xadvance(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar$Buffer.xadvance()"""
        return float._wrap(super(Buffer, self).xadvance())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def y1(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar$Buffer.y1()"""
        return int._wrap(super(Buffer, self).y1())

    @overload
    def xoff(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar$Buffer.xoff()"""
        return float._wrap(super(Buffer, self).xoff())

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
    def yoff(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar$Buffer.yoff()"""
        return float._wrap(super(Buffer, self).yoff())

    @overload
    def x1(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar$Buffer.x1()"""
        return int._wrap(super(Buffer, self).x1())

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
    def xoff2(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.xoff2(float)"""
        return 'Buffer'._wrap(super(_Buffer, self).xoff2(_float.valueOf(arg0)))

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
    def xoff(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.xoff(float)"""
        return 'Buffer'._wrap(super(_Buffer, self).xoff(_float.valueOf(arg0)))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def xoff2(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar$Buffer.xoff2()"""
        return float._wrap(super(Buffer, self).xoff2())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTPackedchar$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def y0(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar$Buffer.y0()"""
        return int._wrap(super(Buffer, self).y0())

    @overload
    def xadvance(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.xadvance(float)"""
        return 'Buffer'._wrap(super(_Buffer, self).xadvance(_float.valueOf(arg0)))

    @overload
    def y0(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.y0(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).y0(_short.valueOf(arg0)))

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def x0(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.x0(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).x0(_short.valueOf(arg0)))

    @overload
    def x1(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.x1(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).x1(_short.valueOf(arg0)))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def y1(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.y1(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).y1(_short.valueOf(arg0)))

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackedchar$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def yoff(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.yoff(float)"""
        return 'Buffer'._wrap(super(_Buffer, self).yoff(_float.valueOf(arg0)))

    @overload
    def yoff2(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar$Buffer.yoff2()"""
        return float._wrap(super(Buffer, self).yoff2())

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
    def x0(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar$Buffer.x0()"""
        return int._wrap(super(Buffer, self).x0())

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
    def yoff2(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.yoff2(float)"""
        return 'Buffer'._wrap(super(_Buffer, self).yoff2(_float.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.stb.STBIZlibCompress
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.lwjgl.stb.STBIZlibCompress as _STBIZlibCompress
_STBIZlibCompress = _STBIZlibCompress
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
import org.lwjgl.stb.STBIZlibCompressI as _STBIZlibCompressI
_STBIZlibCompressI = _STBIZlibCompressI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBIZlibCompress():
    """org.lwjgl.stb.STBIZlibCompress"""
 
    @staticmethod
    def _wrap(java_value: _STBIZlibCompress) -> 'STBIZlibCompress':
        return STBIZlibCompress(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBIZlibCompress):
        """
        Dynamic initializer for STBIZlibCompress.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBIZlibCompress__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBIZlibCompress__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract long org.lwjgl.stb.STBIZlibCompressI.invoke(long,int,long,int)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBIZlibCompress':
        """public static org.lwjgl.stb.STBIZlibCompress org.lwjgl.stb.STBIZlibCompress.createSafe(long)"""
        return STBIZlibCompress._wrap(_STBIZlibCompress.createSafe(_long.valueOf(arg0)))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBIZlibCompress':
        """public static org.lwjgl.stb.STBIZlibCompress org.lwjgl.stb.STBIZlibCompress.create(long)"""
        return STBIZlibCompress._wrap(_STBIZlibCompress.create(_long.valueOf(arg0)))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIZlibCompressI.callback(long,long)"""
        super(_STBIZlibCompressI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIZlibCompressI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(STBIZlibCompressI, self).getCallInterface())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: 'STBIZlibCompressI') -> 'STBIZlibCompress':
        """public static org.lwjgl.stb.STBIZlibCompress org.lwjgl.stb.STBIZlibCompress.create(org.lwjgl.stb.STBIZlibCompressI)"""
        return STBIZlibCompress._wrap(_STBIZlibCompress.create(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBTTVertex$Buffer
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
import org.lwjgl.stb.STBTTVertex as _STBTTVertex_Buffer
_Buffer = _STBTTVertex_Buffer.Buffer
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
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
    """org.lwjgl.stb.STBTTVertex.Buffer"""
 
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
    def cy(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.cy()"""
        return int._wrap(super(Buffer, self).cy())

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
    def type(self) -> int:
        """public byte org.lwjgl.stb.STBTTVertex$Buffer.type()"""
        return int._wrap(super(Buffer, self).type())

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
    def cx1(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.cx1()"""
        return int._wrap(super(Buffer, self).cx1())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTVertex$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTVertex$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def x(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.x()"""
        return int._wrap(super(Buffer, self).x())

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
    def cx(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.cx()"""
        return int._wrap(super(Buffer, self).cx())

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
    def cy1(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.cy1()"""
        return int._wrap(super(Buffer, self).cy1())

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
    def y(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.y()"""
        return int._wrap(super(Buffer, self).y())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBTruetype
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.CharSequence as CharSequence
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
from builtins import float
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import org.lwjgl.stb.STBTruetype as _STBTruetype
_STBTruetype = _STBTruetype
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
import org.lwjgl.stb.STBTTVertex as _STBTTVertex_Buffer
_Buffer = _STBTTVertex_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBTruetype():
    """org.lwjgl.stb.STBTruetype"""
 
    @staticmethod
    def _wrap(java_value: _STBTruetype) -> 'STBTruetype':
        return STBTruetype(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBTruetype):
        """
        Dynamic initializer for STBTruetype.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBTruetype__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBTruetype__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmap(arg0: int, arg1: float, arg2: float, arg3: int, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmap(long,float,float,int,int[],int[],int[],int[])"""
        return int._wrap(_STBTruetype.nstbtt_GetCodepointBitmap(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def nstbtt_PackFontRange(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_PackFontRange(long,long,int,float,int,int,long)"""
        return int._wrap(_STBTruetype.nstbtt_PackFontRange(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def stbtt_CompareUTF8toUTF16_bigendian(arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_CompareUTF8toUTF16_bigendian(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return bool._wrap(_STBTruetype.stbtt_CompareUTF8toUTF16_bigendian(arg0, arg1))

    @staticmethod
    @overload
    def nstbtt_GetPackedQuad(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'float', arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetPackedQuad(long,int,int,int,float[],float[],long,int)"""
        _STBTruetype.nstbtt_GetPackedQuad(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, _long.valueOf(arg6), _int.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_FindGlyphIndex(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_FindGlyphIndex(long,int)"""
        return int._wrap(_STBTruetype.nstbtt_FindGlyphIndex(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_GetPackedQuad(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetPackedQuad(long,int,int,int,long,long,long,int)"""
        _STBTruetype.nstbtt_GetPackedQuad(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_GetFontNameString(arg0: 'STBTTFontinfo', arg1: int, arg2: int, arg3: int, arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetFontNameString(org.lwjgl.stb.STBTTFontinfo,int,int,int,int)"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetFontNameString(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapBox(arg0: int, arg1: int, arg2: float, arg3: float, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapBox(long,int,float,float,int[],int[],int[],int[])"""
        _STBTruetype.nstbtt_GetCodepointBitmapBox(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @staticmethod
    @overload
    def stbtt_GetNumberOfFonts(arg0: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetNumberOfFonts(java.nio.ByteBuffer)"""
        return int._wrap(_STBTruetype.stbtt_GetNumberOfFonts(arg0))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBox(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int') -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBox(long,int,int[],int[],int[],int[])"""
        return int._wrap(_STBTruetype.nstbtt_GetCodepointBox(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def nstbtt_GetCodepointShape(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointShape(long,int,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetCodepointShape(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_PackEnd(arg0: 'STBTTPackContext'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_PackEnd(org.lwjgl.stb.STBTTPackContext)"""
        _STBTruetype.stbtt_PackEnd(arg0)

    @staticmethod
    @overload
    def stbtt_PackFontRange(arg0: 'STBTTPackContext', arg1: 'ByteBuffer', arg2: int, arg3: float, arg4: int, arg5: 'Buffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_PackFontRange(org.lwjgl.stb.STBTTPackContext,java.nio.ByteBuffer,int,float,int,org.lwjgl.stb.STBTTPackedchar$Buffer)"""
        return bool._wrap(_STBTruetype.stbtt_PackFontRange(arg0, arg1, _int.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def nstbtt_GetGlyphHMetrics(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphHMetrics(long,int,long,long)"""
        _STBTruetype.nstbtt_GetGlyphHMetrics(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def stbtt_GetCodepointShape(arg0: 'STBTTFontinfo', arg1: int, arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetCodepointShape(org.lwjgl.stb.STBTTFontinfo,int,org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBTruetype.stbtt_GetCodepointShape(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stbtt_FindGlyphIndex(arg0: 'STBTTFontinfo', arg1: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_FindGlyphIndex(org.lwjgl.stb.STBTTFontinfo,int)"""
        return int._wrap(_STBTruetype.stbtt_FindGlyphIndex(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmap(arg0: int, arg1: float, arg2: float, arg3: int, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmap(long,float,float,int,int[],int[],int[],int[])"""
        return int._wrap(_STBTruetype.nstbtt_GetGlyphBitmap(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def nstbtt_GetNumberOfFonts(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetNumberOfFonts(long)"""
        return int._wrap(_STBTruetype.nstbtt_GetNumberOfFonts(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointHMetrics(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointHMetrics(long,int,long,long)"""
        _STBTruetype.nstbtt_GetCodepointHMetrics(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def stbtt_PackBegin(arg0: 'STBTTPackContext', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_PackBegin(org.lwjgl.stb.STBTTPackContext,java.nio.ByteBuffer,int,int,int,int,long)"""
        return bool._wrap(_STBTruetype.stbtt_PackBegin(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def nstbtt_ScaleForMappingEmToPixels(arg0: int, arg1: float) -> float:
        """public static native float org.lwjgl.stb.STBTruetype.nstbtt_ScaleForMappingEmToPixels(long,float)"""
        return float._wrap(_STBTruetype.nstbtt_ScaleForMappingEmToPixels(_long.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_FreeBitmap(arg0: 'ByteBuffer', arg1: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_FreeBitmap(java.nio.ByteBuffer,long)"""
        _STBTruetype.stbtt_FreeBitmap(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def nstbtt_GetGlyphSDF(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphSDF(long,float,int,int,byte,float,long,long,long,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetGlyphSDF(_long.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _byte.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def nstbtt_GetGlyphHMetrics(arg0: int, arg1: int, arg2: 'int', arg3: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphHMetrics(long,int,int[],int[])"""
        _STBTruetype.nstbtt_GetGlyphHMetrics(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapBox(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IntBuffer', arg7: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapBox(org.lwjgl.stb.STBTTFontinfo,int,float,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _STBTruetype.stbtt_GetCodepointBitmapBox(arg0, _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @staticmethod
    @overload
    def nstbtt_GetFontBoundingBox(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetFontBoundingBox(long,long,long,long,long)"""
        _STBTruetype.nstbtt_GetFontBoundingBox(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def nstbtt_FreeBitmap(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_FreeBitmap(long,long)"""
        _STBTruetype.nstbtt_FreeBitmap(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def stbtt_ScaleForPixelHeight(arg0: 'STBTTFontinfo', arg1: float) -> float:
        """public static float org.lwjgl.stb.STBTruetype.stbtt_ScaleForPixelHeight(org.lwjgl.stb.STBTTFontinfo,float)"""
        return float._wrap(_STBTruetype.stbtt_ScaleForPixelHeight(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointKernAdvance(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointKernAdvance(long,int,int)"""
        return int._wrap(_STBTruetype.nstbtt_GetCodepointKernAdvance(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_GetGlyphShape(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphShape(long,int,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetGlyphShape(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBox(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBox(long,int,long,long,long,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetCodepointBox(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapBox(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IntBuffer', arg7: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapBox(org.lwjgl.stb.STBTTFontinfo,int,float,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _STBTruetype.stbtt_GetGlyphBitmapBox(arg0, _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def stbtt_GetScaledFontVMetrics(arg0: 'ByteBuffer', arg1: int, arg2: float, arg3: 'float', arg4: 'float', arg5: 'float'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetScaledFontVMetrics(java.nio.ByteBuffer,int,float,float[],float[],float[])"""
        _STBTruetype.stbtt_GetScaledFontVMetrics(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, arg4, arg5)

    @staticmethod
    @overload
    def stbtt_FindSVGDoc(arg0: 'STBTTFontinfo', arg1: int) -> int:
        """public static long org.lwjgl.stb.STBTruetype.stbtt_FindSVGDoc(org.lwjgl.stb.STBTTFontinfo,int)"""
        return int._wrap(_STBTruetype.stbtt_FindSVGDoc(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_PackFontRangesPackRects(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_PackFontRangesPackRects(long,long,int)"""
        _STBTruetype.nstbtt_PackFontRangesPackRects(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def stbtt_MakeCodepointBitmap(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeCodepointBitmap(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,int)"""
        _STBTruetype.stbtt_MakeCodepointBitmap(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_GetFontNameString(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetFontNameString(long,long,int,int,int,int)"""
        return int._wrap(_STBTruetype.nstbtt_GetFontNameString(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapBoxSubpixel(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapBoxSubpixel(long,int,float,float,float,float,int[],int[],int[],int[])"""
        _STBTruetype.nstbtt_GetCodepointBitmapBoxSubpixel(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def nstbtt_GetCodepointSDF(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointSDF(long,float,int,int,byte,float,long,long,long,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetCodepointSDF(_long.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _byte.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def stbtt_GetFontVMetrics(arg0: 'STBTTFontinfo', arg1: 'int', arg2: 'int', arg3: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetFontVMetrics(org.lwjgl.stb.STBTTFontinfo,int[],int[],int[])"""
        _STBTruetype.stbtt_GetFontVMetrics(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def stbtt_GetGlyphSDF(arg0: 'STBTTFontinfo', arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphSDF(org.lwjgl.stb.STBTTFontinfo,float,int,int,byte,float,int[],int[],int[],int[])"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetGlyphSDF(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _byte.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def stbtt_GetGlyphShape(arg0: 'STBTTFontinfo', arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphShape(org.lwjgl.stb.STBTTFontinfo,int)"""
        return Buffer._wrap(_STBTruetype.stbtt_GetGlyphShape(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,float,float,float,float,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetCodepointBitmapSubpixel(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def nstbtt_GetKerningTableLength(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetKerningTableLength(long)"""
        return int._wrap(_STBTruetype.nstbtt_GetKerningTableLength(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstbtt_Rasterize(arg0: int, arg1: float, arg2: int, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_Rasterize(long,float,long,int,float,float,float,float,int,int,int,long)"""
        _STBTruetype.nstbtt_Rasterize(_long.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _long.valueOf(arg11))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapSubpixel(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapSubpixel(long,float,float,float,float,int,long,long,long,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetCodepointBitmapSubpixel(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def nstbtt_MakeGlyphBitmap(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeGlyphBitmap(long,long,int,int,int,float,float,int)"""
        _STBTruetype.nstbtt_MakeGlyphBitmap(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_GetBakedQuad(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetBakedQuad(long,int,int,int,long,long,long,int)"""
        _STBTruetype.nstbtt_GetBakedQuad(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_PackFontRangesGatherRects(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_PackFontRangesGatherRects(long,long,long,int,long)"""
        return int._wrap(_STBTruetype.nstbtt_PackFontRangesGatherRects(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbtt_MakeCodepointBitmap(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeCodepointBitmap(long,long,int,int,int,float,float,int)"""
        _STBTruetype.nstbtt_MakeCodepointBitmap(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_BakeFontBitmap(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_BakeFontBitmap(long,int,float,long,int,int,int,int,long)"""
        return int._wrap(_STBTruetype.nstbtt_BakeFontBitmap(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def stbtt_GetGlyphSDF(arg0: 'STBTTFontinfo', arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphSDF(org.lwjgl.stb.STBTTFontinfo,float,int,int,byte,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetGlyphSDF(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _byte.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def nstbtt_GetCodepointSDF(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointSDF(long,float,int,int,byte,float,int[],int[],int[],int[])"""
        return int._wrap(_STBTruetype.nstbtt_GetCodepointSDF(_long.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _byte.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapBoxSubpixel(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapBoxSubpixel(org.lwjgl.stb.STBTTFontinfo,int,float,float,float,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _STBTruetype.stbtt_GetGlyphBitmapBoxSubpixel(arg0, _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def stbtt_FreeSDF(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_FreeSDF(java.nio.ByteBuffer)"""
        _STBTruetype.stbtt_FreeSDF(arg0)

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapBoxSubpixel(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapBoxSubpixel(long,int,float,float,float,float,long,long,long,long)"""
        _STBTruetype.nstbtt_GetGlyphBitmapBoxSubpixel(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def nstbtt_GetGlyphSDF(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphSDF(long,float,int,int,byte,float,int[],int[],int[],int[])"""
        return int._wrap(_STBTruetype.nstbtt_GetGlyphSDF(_long.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _byte.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmap(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: int, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmap(org.lwjgl.stb.STBTTFontinfo,float,float,int,int[],int[],int[],int[])"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetGlyphBitmap(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def stbtt_MakeGlyphBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeGlyphBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int)"""
        _STBTruetype.stbtt_MakeGlyphBitmapSubpixel(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9))

    @staticmethod
    @overload
    def stbtt_GetFontVMetricsOS2(arg0: 'STBTTFontinfo', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetFontVMetricsOS2(org.lwjgl.stb.STBTTFontinfo,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool._wrap(_STBTruetype.stbtt_GetFontVMetricsOS2(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stbtt_GetKerningTable(arg0: 'STBTTFontinfo', arg1: 'Buffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetKerningTable(org.lwjgl.stb.STBTTFontinfo,org.lwjgl.stb.STBTTKerningentry$Buffer)"""
        return int._wrap(_STBTruetype.stbtt_GetKerningTable(arg0, arg1))

    @staticmethod
    @overload
    def nstbtt_MakeGlyphBitmapSubpixelPrefilter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'float', arg12: 'float', arg13: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeGlyphBitmapSubpixelPrefilter(long,long,int,int,int,float,float,float,float,int,int,float[],float[],int)"""
        _STBTruetype.nstbtt_MakeGlyphBitmapSubpixelPrefilter(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11, arg12, _int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_MakeCodepointBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeCodepointBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int)"""
        _STBTruetype.stbtt_MakeCodepointBitmapSubpixel(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9))

    @staticmethod
    @overload
    def stbtt_GetBakedQuad(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer', arg5: 'FloatBuffer', arg6: 'STBTTAlignedQuad', arg7: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetBakedQuad(org.lwjgl.stb.STBTTBakedChar$Buffer,int,int,int,java.nio.FloatBuffer,java.nio.FloatBuffer,org.lwjgl.stb.STBTTAlignedQuad,boolean)"""
        _STBTruetype.stbtt_GetBakedQuad(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, _boolean.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_MakeGlyphBitmapSubpixel(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeGlyphBitmapSubpixel(long,long,int,int,int,float,float,float,float,int)"""
        _STBTruetype.nstbtt_MakeGlyphBitmapSubpixel(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9))

    @staticmethod
    @overload
    def stbtt_FreeShape(arg0: 'STBTTFontinfo', arg1: 'Buffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_FreeShape(org.lwjgl.stb.STBTTFontinfo,org.lwjgl.stb.STBTTVertex$Buffer)"""
        _STBTruetype.stbtt_FreeShape(arg0, arg1)

    @staticmethod
    @overload
    def stbtt_FindMatchingFont(arg0: 'ByteBuffer', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_FindMatchingFont(java.nio.ByteBuffer,java.lang.CharSequence,int)"""
        return int._wrap(_STBTruetype.stbtt_FindMatchingFont(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_MakeCodepointBitmapSubpixelPrefilter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeCodepointBitmapSubpixelPrefilter(long,long,int,int,int,float,float,float,float,int,int,long,long,int)"""
        _STBTruetype.nstbtt_MakeCodepointBitmapSubpixelPrefilter(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _long.valueOf(arg11), _long.valueOf(arg12), _int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_GetFontOffsetForIndex(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetFontOffsetForIndex(java.nio.ByteBuffer,int)"""
        return int._wrap(_STBTruetype.stbtt_GetFontOffsetForIndex(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_FindMatchingFont(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_FindMatchingFont(long,long,int)"""
        return int._wrap(_STBTruetype.nstbtt_FindMatchingFont(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_PackSetOversampling(arg0: 'STBTTPackContext', arg1: int, arg2: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_PackSetOversampling(org.lwjgl.stb.STBTTPackContext,int,int)"""
        _STBTruetype.stbtt_PackSetOversampling(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def stbtt_GetPackedQuad(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer', arg5: 'FloatBuffer', arg6: 'STBTTAlignedQuad', arg7: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetPackedQuad(org.lwjgl.stb.STBTTPackedchar$Buffer,int,int,int,java.nio.FloatBuffer,java.nio.FloatBuffer,org.lwjgl.stb.STBTTAlignedQuad,boolean)"""
        _STBTruetype.stbtt_GetPackedQuad(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, _boolean.valueOf(arg7))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBox(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int') -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBox(long,int,int[],int[],int[],int[])"""
        return int._wrap(_STBTruetype.nstbtt_GetGlyphBox(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def nstbtt_GetCodepointSVG(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointSVG(long,int,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetCodepointSVG(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_PackFontRanges(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_PackFontRanges(long,long,int,long,int)"""
        return int._wrap(_STBTruetype.nstbtt_PackFontRanges(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBox(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBox(long,int,long,long,long,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetGlyphBox(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def stbtt_GetFontBoundingBox(arg0: 'STBTTFontinfo', arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetFontBoundingBox(org.lwjgl.stb.STBTTFontinfo,int[],int[],int[],int[])"""
        _STBTruetype.stbtt_GetFontBoundingBox(arg0, arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def stbtt_PackFontRangesPackRects(arg0: 'STBTTPackContext', arg1: 'Buffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_PackFontRangesPackRects(org.lwjgl.stb.STBTTPackContext,org.lwjgl.stb.STBRPRect$Buffer)"""
        _STBTruetype.stbtt_PackFontRangesPackRects(arg0, arg1)

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapBoxSubpixel(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapBoxSubpixel(long,int,float,float,float,float,int[],int[],int[],int[])"""
        _STBTruetype.nstbtt_GetGlyphBitmapBoxSubpixel(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def stbtt_GetCodepointSDF(arg0: 'STBTTFontinfo', arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointSDF(org.lwjgl.stb.STBTTFontinfo,float,int,int,byte,float,int[],int[],int[],int[])"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetCodepointSDF(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _byte.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nstbtt_GetKerningTable(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetKerningTable(long,long,int)"""
        return int._wrap(_STBTruetype.nstbtt_GetKerningTable(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_GetFontVMetricsOS2(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetFontVMetricsOS2(long,long,long,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetFontVMetricsOS2(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def stbtt_MakeGlyphBitmapSubpixelPrefilter(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'float', arg12: 'float', arg13: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeGlyphBitmapSubpixelPrefilter(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int,int,float[],float[],int)"""
        _STBTruetype.stbtt_MakeGlyphBitmapSubpixelPrefilter(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11, arg12, _int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_BakeFontBitmap(arg0: 'ByteBuffer', arg1: float, arg2: 'ByteBuffer', arg3: int, arg4: int, arg5: int, arg6: 'Buffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_BakeFontBitmap(java.nio.ByteBuffer,float,java.nio.ByteBuffer,int,int,int,org.lwjgl.stb.STBTTBakedChar$Buffer)"""
        return int._wrap(_STBTruetype.stbtt_BakeFontBitmap(arg0, _float.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmap(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: int, arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IntBuffer', arg7: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmap(org.lwjgl.stb.STBTTFontinfo,float,float,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetGlyphBitmap(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def stbtt_GetPackedQuad(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'float', arg6: 'STBTTAlignedQuad', arg7: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetPackedQuad(org.lwjgl.stb.STBTTPackedchar$Buffer,int,int,int,float[],float[],org.lwjgl.stb.STBTTAlignedQuad,boolean)"""
        _STBTruetype.stbtt_GetPackedQuad(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, _boolean.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_GetCodepointBox(arg0: 'STBTTFontinfo', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBox(org.lwjgl.stb.STBTTFontinfo,int,int[],int[],int[],int[])"""
        return bool._wrap(_STBTruetype.stbtt_GetCodepointBox(arg0, _int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def stbtt_ScaleForMappingEmToPixels(arg0: 'STBTTFontinfo', arg1: float) -> float:
        """public static float org.lwjgl.stb.STBTruetype.stbtt_ScaleForMappingEmToPixels(org.lwjgl.stb.STBTTFontinfo,float)"""
        return float._wrap(_STBTruetype.stbtt_ScaleForMappingEmToPixels(arg0, _float.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_GetKerningTableLength(arg0: 'STBTTFontinfo') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetKerningTableLength(org.lwjgl.stb.STBTTFontinfo)"""
        return int._wrap(_STBTruetype.stbtt_GetKerningTableLength(arg0))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,float,float,float,float,int,int[],int[],int[],int[])"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetGlyphBitmapSubpixel(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def nstbtt_PackEnd(arg0: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_PackEnd(long)"""
        _STBTruetype.nstbtt_PackEnd(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nstbtt_GetFontVMetrics(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetFontVMetrics(long,int[],int[],int[])"""
        _STBTruetype.nstbtt_GetFontVMetrics(_long.valueOf(arg0), arg1, arg2, arg3)

    @staticmethod
    @overload
    def nstbtt_GetFontOffsetForIndex(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetFontOffsetForIndex(long,int)"""
        return int._wrap(_STBTruetype.nstbtt_GetFontOffsetForIndex(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapBox(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapBox(org.lwjgl.stb.STBTTFontinfo,int,float,float,int[],int[],int[],int[])"""
        _STBTruetype.stbtt_GetGlyphBitmapBox(arg0, _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapBox(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapBox(long,int,float,float,long,long,long,long)"""
        _STBTruetype.nstbtt_GetGlyphBitmapBox(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_Rasterize(arg0: 'STBTTBitmap', arg1: float, arg2: 'Buffer', arg3: float, arg4: float, arg5: float, arg6: float, arg7: int, arg8: int, arg9: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_Rasterize(org.lwjgl.stb.STBTTBitmap,float,org.lwjgl.stb.STBTTVertex$Buffer,float,float,float,float,int,int,boolean)"""
        _STBTruetype.stbtt_Rasterize(arg0, _float.valueOf(arg1), arg2, _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _boolean.valueOf(arg9))

    @staticmethod
    @overload
    def nstbtt_FreeShape(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_FreeShape(long,long)"""
        _STBTruetype.nstbtt_FreeShape(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nstbtt_GetCodepointHMetrics(arg0: int, arg1: int, arg2: 'int', arg3: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointHMetrics(long,int,int[],int[])"""
        _STBTruetype.nstbtt_GetCodepointHMetrics(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def stbtt_GetCodepointHMetrics(arg0: 'STBTTFontinfo', arg1: int, arg2: 'int', arg3: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointHMetrics(org.lwjgl.stb.STBTTFontinfo,int,int[],int[])"""
        _STBTruetype.stbtt_GetCodepointHMetrics(arg0, _int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def STBTT_POINT_SIZE(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.STBTT_POINT_SIZE(int)"""
        return int._wrap(_STBTruetype.STBTT_POINT_SIZE(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nstbtt_GetBakedQuad(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'float', arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetBakedQuad(long,int,int,int,float[],float[],long,int)"""
        _STBTruetype.nstbtt_GetBakedQuad(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, _long.valueOf(arg6), _int.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,float,float,float,float,int,int[],int[],int[],int[])"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetCodepointBitmapSubpixel(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def nstbtt_GetFontVMetricsOS2(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int') -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetFontVMetricsOS2(long,int[],int[],int[])"""
        return int._wrap(_STBTruetype.nstbtt_GetFontVMetricsOS2(_long.valueOf(arg0), arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapBox(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapBox(long,int,float,float,long,long,long,long)"""
        _STBTruetype.nstbtt_GetCodepointBitmapBox(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_GetGlyphHMetrics(arg0: 'STBTTFontinfo', arg1: int, arg2: 'int', arg3: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphHMetrics(org.lwjgl.stb.STBTTFontinfo,int,int[],int[])"""
        _STBTruetype.stbtt_GetGlyphHMetrics(arg0, _int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def stbtt_GetCodepointBox(arg0: 'STBTTFontinfo', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBox(org.lwjgl.stb.STBTTFontinfo,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool._wrap(_STBTruetype.stbtt_GetCodepointBox(arg0, _int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def nstbtt_GetScaledFontVMetrics(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetScaledFontVMetrics(long,int,float,long,long,long)"""
        _STBTruetype.nstbtt_GetScaledFontVMetrics(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def stbtt_GetCodepointShape(arg0: 'STBTTFontinfo', arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointShape(org.lwjgl.stb.STBTTFontinfo,int)"""
        return Buffer._wrap(_STBTruetype.stbtt_GetCodepointShape(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapSubpixel(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapSubpixel(long,float,float,float,float,int,long,long,long,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetGlyphBitmapSubpixel(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def stbtt_PackSetSkipMissingCodepoints(arg0: 'STBTTPackContext', arg1: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_PackSetSkipMissingCodepoints(org.lwjgl.stb.STBTTPackContext,boolean)"""
        _STBTruetype.stbtt_PackSetSkipMissingCodepoints(arg0, _boolean.valueOf(arg1))

    @staticmethod
    @overload
    def nstbtt_GetGlyphKernAdvance(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphKernAdvance(long,int,int)"""
        return int._wrap(_STBTruetype.nstbtt_GetGlyphKernAdvance(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapBox(arg0: int, arg1: int, arg2: float, arg3: float, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapBox(long,int,float,float,int[],int[],int[],int[])"""
        _STBTruetype.nstbtt_GetGlyphBitmapBox(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @staticmethod
    @overload
    def nstbtt_FreeSDF(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_FreeSDF(long,long)"""
        _STBTruetype.nstbtt_FreeSDF(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nstbtt_PackBegin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_PackBegin(long,long,int,int,int,int,long)"""
        return int._wrap(_STBTruetype.nstbtt_PackBegin(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def stbtt_MakeCodepointBitmapSubpixelPrefilter(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'float', arg12: 'float', arg13: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeCodepointBitmapSubpixelPrefilter(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int,int,float[],float[],int)"""
        _STBTruetype.stbtt_MakeCodepointBitmapSubpixelPrefilter(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11, arg12, _int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_GetScaledFontVMetrics(arg0: 'ByteBuffer', arg1: int, arg2: float, arg3: 'FloatBuffer', arg4: 'FloatBuffer', arg5: 'FloatBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetScaledFontVMetrics(java.nio.ByteBuffer,int,float,java.nio.FloatBuffer,java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        _STBTruetype.stbtt_GetScaledFontVMetrics(arg0, _int.valueOf(arg1), _float.valueOf(arg2), arg3, arg4, arg5)

    @staticmethod
    @overload
    def nstbtt_FindSVGDoc(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_FindSVGDoc(long,int)"""
        return int._wrap(_STBTruetype.nstbtt_FindSVGDoc(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_FreeBitmap(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_FreeBitmap(java.nio.ByteBuffer)"""
        _STBTruetype.stbtt_FreeBitmap(arg0)

    @staticmethod
    @overload
    def stbtt_FindMatchingFont(arg0: 'ByteBuffer', arg1: 'ByteBuffer', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_FindMatchingFont(java.nio.ByteBuffer,java.nio.ByteBuffer,int)"""
        return int._wrap(_STBTruetype.stbtt_FindMatchingFont(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_GetGlyphBox(arg0: 'STBTTFontinfo', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBox(org.lwjgl.stb.STBTTFontinfo,int,int[],int[],int[],int[])"""
        return bool._wrap(_STBTruetype.stbtt_GetGlyphBox(arg0, _int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def nstbtt_MakeGlyphBitmapSubpixelPrefilter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeGlyphBitmapSubpixelPrefilter(long,long,int,int,int,float,float,float,float,int,int,long,long,int)"""
        _STBTruetype.nstbtt_MakeGlyphBitmapSubpixelPrefilter(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _long.valueOf(arg11), _long.valueOf(arg12), _int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_PackFontRanges(arg0: 'STBTTPackContext', arg1: 'ByteBuffer', arg2: int, arg3: 'Buffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_PackFontRanges(org.lwjgl.stb.STBTTPackContext,java.nio.ByteBuffer,int,org.lwjgl.stb.STBTTPackRange$Buffer)"""
        return bool._wrap(_STBTruetype.stbtt_PackFontRanges(arg0, arg1, _int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapBoxSubpixel(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapBoxSubpixel(org.lwjgl.stb.STBTTFontinfo,int,float,float,float,float,int[],int[],int[],int[])"""
        _STBTruetype.stbtt_GetGlyphBitmapBoxSubpixel(arg0, _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapSubpixel(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapSubpixel(long,float,float,float,float,int,int[],int[],int[],int[])"""
        return int._wrap(_STBTruetype.nstbtt_GetGlyphBitmapSubpixel(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def stbtt_InitFont(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int) -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_InitFont(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int)"""
        return bool._wrap(_STBTruetype.stbtt_InitFont(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_IsGlyphEmpty(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_IsGlyphEmpty(long,int)"""
        return int._wrap(_STBTruetype.nstbtt_IsGlyphEmpty(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmap(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmap(long,float,float,int,long,long,long,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetCodepointBitmap(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmap(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: int, arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IntBuffer', arg7: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmap(org.lwjgl.stb.STBTTFontinfo,float,float,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetCodepointBitmap(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def stbtt_IsGlyphEmpty(arg0: 'STBTTFontinfo', arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_IsGlyphEmpty(org.lwjgl.stb.STBTTFontinfo,int)"""
        return bool._wrap(_STBTruetype.stbtt_IsGlyphEmpty(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_MakeCodepointBitmapSubpixel(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeCodepointBitmapSubpixel(long,long,int,int,int,float,float,float,float,int)"""
        _STBTruetype.nstbtt_MakeCodepointBitmapSubpixel(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9))

    @staticmethod
    @overload
    def stbtt_InitFont(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_InitFont(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer)"""
        return bool._wrap(_STBTruetype.stbtt_InitFont(arg0, arg1))

    @staticmethod
    @overload
    def stbtt_GetFontVMetricsOS2(arg0: 'STBTTFontinfo', arg1: 'int', arg2: 'int', arg3: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetFontVMetricsOS2(org.lwjgl.stb.STBTTFontinfo,int[],int[],int[])"""
        return bool._wrap(_STBTruetype.stbtt_GetFontVMetricsOS2(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stbtt_GetCodepointHMetrics(arg0: 'STBTTFontinfo', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointHMetrics(org.lwjgl.stb.STBTTFontinfo,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _STBTruetype.stbtt_GetCodepointHMetrics(arg0, _int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def stbtt_PackFontRangesGatherRects(arg0: 'STBTTPackContext', arg1: 'STBTTFontinfo', arg2: 'Buffer', arg3: 'Buffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_PackFontRangesGatherRects(org.lwjgl.stb.STBTTPackContext,org.lwjgl.stb.STBTTFontinfo,org.lwjgl.stb.STBTTPackRange$Buffer,org.lwjgl.stb.STBRPRect$Buffer)"""
        return int._wrap(_STBTruetype.stbtt_PackFontRangesGatherRects(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stbtt_GetFontVMetrics(arg0: 'STBTTFontinfo', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetFontVMetrics(org.lwjgl.stb.STBTTFontinfo,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _STBTruetype.stbtt_GetFontVMetrics(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def stbtt_GetFontBoundingBox(arg0: 'STBTTFontinfo', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetFontBoundingBox(org.lwjgl.stb.STBTTFontinfo,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _STBTruetype.stbtt_GetFontBoundingBox(arg0, arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def stbtt_MakeGlyphBitmap(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeGlyphBitmap(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,int)"""
        _STBTruetype.stbtt_MakeGlyphBitmap(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_PackFontRangesRenderIntoRects(arg0: 'STBTTPackContext', arg1: 'STBTTFontinfo', arg2: 'Buffer', arg3: 'Buffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_PackFontRangesRenderIntoRects(org.lwjgl.stb.STBTTPackContext,org.lwjgl.stb.STBTTFontinfo,org.lwjgl.stb.STBTTPackRange$Buffer,org.lwjgl.stb.STBRPRect$Buffer)"""
        return bool._wrap(_STBTruetype.stbtt_PackFontRangesRenderIntoRects(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapBox(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapBox(org.lwjgl.stb.STBTTFontinfo,int,float,float,int[],int[],int[],int[])"""
        _STBTruetype.stbtt_GetCodepointBitmapBox(arg0, _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @staticmethod
    @overload
    def stbtt_GetBakedQuad(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'float', arg6: 'STBTTAlignedQuad', arg7: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetBakedQuad(org.lwjgl.stb.STBTTBakedChar$Buffer,int,int,int,float[],float[],org.lwjgl.stb.STBTTAlignedQuad,boolean)"""
        _STBTruetype.stbtt_GetBakedQuad(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, _boolean.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_GetCodepointSVG(arg0: 'STBTTFontinfo', arg1: int, arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetCodepointSVG(org.lwjgl.stb.STBTTFontinfo,int,org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBTruetype.stbtt_GetCodepointSVG(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stbtt_GetGlyphShape(arg0: 'STBTTFontinfo', arg1: int, arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetGlyphShape(org.lwjgl.stb.STBTTFontinfo,int,org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBTruetype.stbtt_GetGlyphShape(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nstbtt_PackFontRangesRenderIntoRects(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_PackFontRangesRenderIntoRects(long,long,long,int,long)"""
        return int._wrap(_STBTruetype.nstbtt_PackFontRangesRenderIntoRects(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def stbtt_GetGlyphSVG(arg0: 'STBTTFontinfo', arg1: int, arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetGlyphSVG(org.lwjgl.stb.STBTTFontinfo,int,org.lwjgl.PointerBuffer)"""
        return int._wrap(_STBTruetype.stbtt_GetGlyphSVG(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nstbtt_PackSetSkipMissingCodepoints(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_PackSetSkipMissingCodepoints(long,int)"""
        _STBTruetype.nstbtt_PackSetSkipMissingCodepoints(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nstbtt_GetFontVMetrics(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetFontVMetrics(long,long,long,long)"""
        _STBTruetype.nstbtt_GetFontVMetrics(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def stbtt_GetGlyphHMetrics(arg0: 'STBTTFontinfo', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphHMetrics(org.lwjgl.stb.STBTTFontinfo,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _STBTruetype.stbtt_GetGlyphHMetrics(arg0, _int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def stbtt_GetGlyphBox(arg0: 'STBTTFontinfo', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBox(org.lwjgl.stb.STBTTFontinfo,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool._wrap(_STBTruetype.stbtt_GetGlyphBox(arg0, _int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def nstbtt_InitFont(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_InitFont(long,long,int)"""
        return int._wrap(_STBTruetype.nstbtt_InitFont(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_MakeCodepointBitmapSubpixelPrefilter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'float', arg12: 'float', arg13: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeCodepointBitmapSubpixelPrefilter(long,long,int,int,int,float,float,float,float,int,int,float[],float[],int)"""
        _STBTruetype.nstbtt_MakeCodepointBitmapSubpixelPrefilter(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11, arg12, _int.valueOf(arg13))

    @staticmethod
    @overload
    def nstbtt_GetGlyphSVG(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphSVG(long,int,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetGlyphSVG(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapBoxSubpixel(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapBoxSubpixel(org.lwjgl.stb.STBTTFontinfo,int,float,float,float,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _STBTruetype.stbtt_GetCodepointBitmapBoxSubpixel(arg0, _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def nstbtt_GetScaledFontVMetrics(arg0: int, arg1: int, arg2: float, arg3: 'float', arg4: 'float', arg5: 'float'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetScaledFontVMetrics(long,int,float,float[],float[],float[])"""
        _STBTruetype.nstbtt_GetScaledFontVMetrics(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), arg3, arg4, arg5)

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmap(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: int, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmap(org.lwjgl.stb.STBTTFontinfo,float,float,int,int[],int[],int[],int[])"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetCodepointBitmap(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def stbtt_MakeCodepointBitmapSubpixelPrefilter(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'FloatBuffer', arg12: 'FloatBuffer', arg13: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeCodepointBitmapSubpixelPrefilter(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int,int,java.nio.FloatBuffer,java.nio.FloatBuffer,int)"""
        _STBTruetype.stbtt_MakeCodepointBitmapSubpixelPrefilter(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11, arg12, _int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,float,float,float,float,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetGlyphBitmapSubpixel(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapBoxSubpixel(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapBoxSubpixel(org.lwjgl.stb.STBTTFontinfo,int,float,float,float,float,int[],int[],int[],int[])"""
        _STBTruetype.stbtt_GetCodepointBitmapBoxSubpixel(arg0, _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapBoxSubpixel(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapBoxSubpixel(long,int,float,float,float,float,long,long,long,long)"""
        _STBTruetype.nstbtt_GetCodepointBitmapBoxSubpixel(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def stbtt_GetCodepointKernAdvance(arg0: 'STBTTFontinfo', arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetCodepointKernAdvance(org.lwjgl.stb.STBTTFontinfo,int,int)"""
        return int._wrap(_STBTruetype.stbtt_GetCodepointKernAdvance(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_GetGlyphKernAdvance(arg0: 'STBTTFontinfo', arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetGlyphKernAdvance(org.lwjgl.stb.STBTTFontinfo,int,int)"""
        return int._wrap(_STBTruetype.stbtt_GetGlyphKernAdvance(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_GetCodepointSDF(arg0: 'STBTTFontinfo', arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointSDF(org.lwjgl.stb.STBTTFontinfo,float,int,int,byte,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer._wrap(_STBTruetype.stbtt_GetCodepointSDF(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _byte.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmap(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmap(long,float,float,int,long,long,long,long)"""
        return int._wrap(_STBTruetype.nstbtt_GetGlyphBitmap(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def nstbtt_PackSetOversampling(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_PackSetOversampling(long,int,int)"""
        _STBTruetype.nstbtt_PackSetOversampling(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nstbtt_GetFontBoundingBox(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetFontBoundingBox(long,int[],int[],int[],int[])"""
        _STBTruetype.nstbtt_GetFontBoundingBox(_long.valueOf(arg0), arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def stbtt_MakeGlyphBitmapSubpixelPrefilter(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'FloatBuffer', arg12: 'FloatBuffer', arg13: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeGlyphBitmapSubpixelPrefilter(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int,int,java.nio.FloatBuffer,java.nio.FloatBuffer,int)"""
        _STBTruetype.stbtt_MakeGlyphBitmapSubpixelPrefilter(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11, arg12, _int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_PackBegin(arg0: 'STBTTPackContext', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_PackBegin(org.lwjgl.stb.STBTTPackContext,java.nio.ByteBuffer,int,int,int,int)"""
        return bool._wrap(_STBTruetype.stbtt_PackBegin(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapSubpixel(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapSubpixel(long,float,float,float,float,int,int[],int[],int[],int[])"""
        return int._wrap(_STBTruetype.nstbtt_GetCodepointBitmapSubpixel(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def nstbtt_ScaleForPixelHeight(arg0: int, arg1: float) -> float:
        """public static native float org.lwjgl.stb.STBTruetype.nstbtt_ScaleForPixelHeight(long,float)"""
        return float._wrap(_STBTruetype.nstbtt_ScaleForPixelHeight(_long.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_FreeSDF(arg0: 'ByteBuffer', arg1: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_FreeSDF(java.nio.ByteBuffer,long)"""
        _STBTruetype.stbtt_FreeSDF(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def nstbtt_CompareUTF8toUTF16_bigendian(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_CompareUTF8toUTF16_bigendian(long,int,long,int)"""
        return int._wrap(_STBTruetype.nstbtt_CompareUTF8toUTF16_bigendian(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))) 
 
 
# CLASS: org.lwjgl.stb.STBTTAlignedQuad
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.stb.STBTTAlignedQuad as _STBTTAlignedQuad_Buffer
_Buffer = _STBTTAlignedQuad_Buffer.Buffer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.stb.STBTTAlignedQuad as _STBTTAlignedQuad
_STBTTAlignedQuad = _STBTTAlignedQuad
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBTTAlignedQuad():
    """org.lwjgl.stb.STBTTAlignedQuad"""
 
    @staticmethod
    def _wrap(java_value: _STBTTAlignedQuad) -> 'STBTTAlignedQuad':
        return STBTTAlignedQuad(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBTTAlignedQuad):
        """
        Dynamic initializer for STBTTAlignedQuad.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBTTAlignedQuad__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBTTAlignedQuad__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def y1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.y1()"""
        return float._wrap(super(STBTTAlignedQuad, self).y1())

    @staticmethod
    @overload
    def ny1(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.ny1(long)"""
        return float._wrap(_STBTTAlignedQuad.ny1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.createSafe(long)"""
        return STBTTAlignedQuad._wrap(_STBTTAlignedQuad.createSafe(_long.valueOf(arg0)))

    @overload
    def t0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.t0()"""
        return float._wrap(super(STBTTAlignedQuad, self).t0())

    @staticmethod
    @overload
    def calloc() -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.calloc()"""
        return STBTTAlignedQuad._wrap(_STBTTAlignedQuad.calloc())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTAlignedQuad(java.nio.ByteBuffer)"""
        val = _STBTTAlignedQuad(arg0)
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
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTAlignedQuad.mallocStack(_int.valueOf(arg0), arg1))

    @overload
    def s1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.s1()"""
        return float._wrap(super(STBTTAlignedQuad, self).s1())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTAlignedQuad.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.calloc(int)"""
        return Buffer._wrap(_STBTTAlignedQuad.calloc(_int.valueOf(arg0)))

    @overload
    def x0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.x0()"""
        return float._wrap(super(STBTTAlignedQuad, self).x0())

    @overload
    def s0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.s0()"""
        return float._wrap(super(STBTTAlignedQuad, self).s0())

    @staticmethod
    @overload
    def ny0(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.ny0(long)"""
        return float._wrap(_STBTTAlignedQuad.ny0(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTAlignedQuad._wrap(_STBTTAlignedQuad.malloc(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTAlignedQuad._wrap(_STBTTAlignedQuad.callocStack(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTAlignedQuad.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ns0(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.ns0(long)"""
        return float._wrap(_STBTTAlignedQuad.ns0(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.createSafe(long,int)"""
        return Buffer._wrap(_STBTTAlignedQuad.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def create(arg0: int) -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.create(long)"""
        return STBTTAlignedQuad._wrap(_STBTTAlignedQuad.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.malloc()"""
        return STBTTAlignedQuad._wrap(_STBTTAlignedQuad.malloc())

    @staticmethod
    @overload
    def callocStack() -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.callocStack()"""
        return STBTTAlignedQuad._wrap(_STBTTAlignedQuad.callocStack())

    @staticmethod
    @overload
    def nx1(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.nx1(long)"""
        return float._wrap(_STBTTAlignedQuad.nx1(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.create(long,int)"""
        return Buffer._wrap(_STBTTAlignedQuad.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTAlignedQuad.sizeof()"""
        return int._wrap(super(STBTTAlignedQuad, self).sizeof())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTAlignedQuad.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTAlignedQuad._wrap(_STBTTAlignedQuad.calloc(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def ns1(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.ns1(long)"""
        return float._wrap(_STBTTAlignedQuad.ns1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.mallocStack(int)"""
        return Buffer._wrap(_STBTTAlignedQuad.mallocStack(_int.valueOf(arg0)))

    @overload
    def t1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.t1()"""
        return float._wrap(super(STBTTAlignedQuad, self).t1())

    @overload
    def y0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.y0()"""
        return float._wrap(super(STBTTAlignedQuad, self).y0())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.callocStack(int)"""
        return Buffer._wrap(_STBTTAlignedQuad.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nt1(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.nt1(long)"""
        return float._wrap(_STBTTAlignedQuad.nt1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTAlignedQuad._wrap(_STBTTAlignedQuad.mallocStack(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.malloc(int)"""
        return Buffer._wrap(_STBTTAlignedQuad.malloc(_int.valueOf(arg0)))

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
    def mallocStack() -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.mallocStack()"""
        return STBTTAlignedQuad._wrap(_STBTTAlignedQuad.mallocStack())

    @staticmethod
    @overload
    def nx0(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.nx0(long)"""
        return float._wrap(_STBTTAlignedQuad.nx0(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nt0(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.nt0(long)"""
        return float._wrap(_STBTTAlignedQuad.nt0(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.create(int)"""
        return Buffer._wrap(_STBTTAlignedQuad.create(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def x1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.x1()"""
        return float._wrap(super(STBTTAlignedQuad, self).x1())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.create()"""
        return STBTTAlignedQuad._wrap(_STBTTAlignedQuad.create())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBRPContext$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.stb.STBRPNode as _STBRPNode
_STBRPNode = _STBRPNode
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.stb.STBRPContext as _STBRPContext_Buffer
_Buffer = _STBRPContext_Buffer.Buffer
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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBRPNode as _STBRPNode_Buffer
_Buffer = _STBRPNode_Buffer.Buffer
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
    """org.lwjgl.stb.STBRPContext.Buffer"""
 
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

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def init_mode(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.init_mode()"""
        return int._wrap(super(Buffer, self).init_mode())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def align(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.align()"""
        return int._wrap(super(Buffer, self).align())

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
    def free_head(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext$Buffer.free_head()"""
        return 'STBRPNode'._wrap(super(Buffer, self).free_head())

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

    @overload
    def heuristic(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.heuristic()"""
        return int._wrap(super(Buffer, self).heuristic())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def width(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.width()"""
        return int._wrap(super(Buffer, self).width())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPContext$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBRPContext$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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
    def height(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.height()"""
        return int._wrap(super(Buffer, self).height())

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
    def active_head(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext$Buffer.active_head()"""
        return 'STBRPNode'._wrap(super(Buffer, self).active_head())

    @overload
    def extra(self) -> 'Buffer':
        """public org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPContext$Buffer.extra()"""
        return 'Buffer'._wrap(super(Buffer, self).extra())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def num_nodes(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.num_nodes()"""
        return int._wrap(super(Buffer, self).num_nodes())

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
    def extra(self, arg0: int) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext$Buffer.extra(int)"""
        return 'STBRPNode'._wrap(super(_Buffer, self).extra(_int.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.stb.STBRPRect$Buffer
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
import java.lang.Boolean as _boolean
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
import org.lwjgl.stb.STBRPRect as _STBRPRect_Buffer
_Buffer = _STBRPRect_Buffer.Buffer
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
    """org.lwjgl.stb.STBRPRect.Buffer"""
 
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
    def id(self) -> int:
        """public int org.lwjgl.stb.STBRPRect$Buffer.id()"""
        return int._wrap(super(Buffer, self).id())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def was_packed(self) -> bool:
        """public boolean org.lwjgl.stb.STBRPRect$Buffer.was_packed()"""
        return bool._wrap(super(Buffer, self).was_packed())

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
    def x(self) -> int:
        """public int org.lwjgl.stb.STBRPRect$Buffer.x()"""
        return int._wrap(super(Buffer, self).x())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def y(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.y(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).y(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBRPRect$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
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
    def h(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.h(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).h(_int.valueOf(arg0)))

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
    def w(self) -> int:
        """public int org.lwjgl.stb.STBRPRect$Buffer.w()"""
        return int._wrap(super(Buffer, self).w())

    @overload
    def y(self) -> int:
        """public int org.lwjgl.stb.STBRPRect$Buffer.y()"""
        return int._wrap(super(Buffer, self).y())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPRect$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def x(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.x(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).x(_int.valueOf(arg0)))

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
    def was_packed(self, arg0: bool) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.was_packed(boolean)"""
        return 'Buffer'._wrap(super(_Buffer, self).was_packed(_boolean.valueOf(arg0)))

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
    def w(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.w(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).w(_int.valueOf(arg0)))

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
    def id(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.id(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).id(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def h(self) -> int:
        """public int org.lwjgl.stb.STBRPRect$Buffer.h()"""
        return int._wrap(super(Buffer, self).h())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBRPRect
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.stb.STBRPRect as _STBRPRect_Buffer
_Buffer = _STBRPRect_Buffer.Buffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBRPRect as _STBRPRect
_STBRPRect = _STBRPRect
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBRPRect():
    """org.lwjgl.stb.STBRPRect"""
 
    @staticmethod
    def _wrap(java_value: _STBRPRect) -> 'STBRPRect':
        return STBRPRect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBRPRect):
        """
        Dynamic initializer for STBRPRect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBRPRect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBRPRect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.set(int,int,int,int,int,boolean)"""
        return 'STBRPRect'._wrap(super(_STBRPRect, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5)))

    @overload
    def w(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.w()"""
        return int._wrap(super(STBRPRect, self).w())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.sizeof()"""
        return int._wrap(super(STBRPRect, self).sizeof())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.callocStack(int)"""
        return Buffer._wrap(_STBRPRect.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.createSafe(long)"""
        return STBRPRect._wrap(_STBRPRect.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPRect._wrap(_STBRPRect.mallocStack(arg0))

    @overload
    def set(self, arg0: 'STBRPRect') -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.set(org.lwjgl.stb.STBRPRect)"""
        return 'STBRPRect'._wrap(super(_STBRPRect, self).set(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.create(int)"""
        return Buffer._wrap(_STBRPRect.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.malloc()"""
        return STBRPRect._wrap(_STBRPRect.malloc())

    @overload
    def id(self, arg0: int) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.id(int)"""
        return 'STBRPRect'._wrap(super(_STBRPRect, self).id(_int.valueOf(arg0)))

    @overload
    def was_packed(self) -> bool:
        """public boolean org.lwjgl.stb.STBRPRect.was_packed()"""
        return bool._wrap(super(STBRPRect, self).was_packed())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.ny(long)"""
        return int._wrap(_STBRPRect.ny(_long.valueOf(arg0)))

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
    def nwas_packed(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.nwas_packed(long)"""
        return int._wrap(_STBRPRect.nwas_packed(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ny(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.ny(long,int)"""
        _STBRPRect.ny(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create() -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.create()"""
        return STBRPRect._wrap(_STBRPRect.create())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.create(long,int)"""
        return Buffer._wrap(_STBRPRect.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nw(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.nw(long)"""
        return int._wrap(_STBRPRect.nw(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.callocStack()"""
        return STBRPRect._wrap(_STBRPRect.callocStack())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.createSafe(long,int)"""
        return Buffer._wrap(_STBRPRect.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def h(self, arg0: int) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.h(int)"""
        return 'STBRPRect'._wrap(super(_STBRPRect, self).h(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPRect.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def calloc() -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.calloc()"""
        return STBRPRect._wrap(_STBRPRect.calloc())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPRect._wrap(_STBRPRect.callocStack(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.malloc(int)"""
        return Buffer._wrap(_STBRPRect.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nw(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.nw(long,int)"""
        _STBRPRect.nw(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.mallocStack(int)"""
        return Buffer._wrap(_STBRPRect.mallocStack(_int.valueOf(arg0)))

    @overload
    def id(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.id()"""
        return int._wrap(super(STBRPRect, self).id())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def h(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.h()"""
        return int._wrap(super(STBRPRect, self).h())

    @staticmethod
    @overload
    def mallocStack() -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.mallocStack()"""
        return STBRPRect._wrap(_STBRPRect.mallocStack())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPRect.mallocStack(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def w(self, arg0: int) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.w(int)"""
        return 'STBRPRect'._wrap(super(_STBRPRect, self).w(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.calloc(org.lwjgl.system.MemoryStack)"""
        return STBRPRect._wrap(_STBRPRect.calloc(arg0))

    @staticmethod
    @overload
    def nh(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.nh(long)"""
        return int._wrap(_STBRPRect.nh(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nid(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.nid(long,int)"""
        _STBRPRect.nid(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.create(long)"""
        return STBRPRect._wrap(_STBRPRect.create(_long.valueOf(arg0)))

    @overload
    def y(self, arg0: int) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.y(int)"""
        return 'STBRPRect'._wrap(super(_STBRPRect, self).y(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nwas_packed(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.nwas_packed(long,int)"""
        _STBRPRect.nwas_packed(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def y(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.y()"""
        return int._wrap(super(STBRPRect, self).y())

    @staticmethod
    @overload
    def nh(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.nh(long,int)"""
        _STBRPRect.nh(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nx(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.nx(long,int)"""
        _STBRPRect.nx(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def nid(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.nid(long)"""
        return int._wrap(_STBRPRect.nid(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.calloc(int)"""
        return Buffer._wrap(_STBRPRect.calloc(_int.valueOf(arg0)))

    @overload
    def was_packed(self, arg0: bool) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.was_packed(boolean)"""
        return 'STBRPRect'._wrap(super(_STBRPRect, self).was_packed(_boolean.valueOf(arg0)))

    @overload
    def x(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.x()"""
        return int._wrap(super(STBRPRect, self).x())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.malloc(org.lwjgl.system.MemoryStack)"""
        return STBRPRect._wrap(_STBRPRect.malloc(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPRect.callocStack(_int.valueOf(arg0), arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.nx(long)"""
        return int._wrap(_STBRPRect.nx(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPRect(java.nio.ByteBuffer)"""
        val = _STBRPRect(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def x(self, arg0: int) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.x(int)"""
        return 'STBRPRect'._wrap(super(_STBRPRect, self).x(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPRect.malloc(_int.valueOf(arg0), arg1)) 
 
 
# CLASS: org.lwjgl.stb.STBTTFontinfo$Buffer
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
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import org.lwjgl.stb.STBTTFontinfo as _STBTTFontinfo_Buffer
_Buffer = _STBTTFontinfo_Buffer.Buffer
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
    """org.lwjgl.stb.STBTTFontinfo.Buffer"""
 
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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

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
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

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
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTFontinfo$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTFontinfo$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBTTVertex
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
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.stb.STBTTVertex as _STBTTVertex_Buffer
_Buffer = _STBTTVertex_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import org.lwjgl.stb.STBTTVertex as _STBTTVertex
_STBTTVertex = _STBTTVertex
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBTTVertex():
    """org.lwjgl.stb.STBTTVertex"""
 
    @staticmethod
    def _wrap(java_value: _STBTTVertex) -> 'STBTTVertex':
        return STBTTVertex(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBTTVertex):
        """
        Dynamic initializer for STBTTVertex.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBTTVertex__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBTTVertex__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ntype(arg0: int) -> int:
        """public static byte org.lwjgl.stb.STBTTVertex.ntype(long)"""
        return int._wrap(_STBTTVertex.ntype(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTVertex.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.callocStack(int)"""
        return Buffer._wrap(_STBTTVertex.callocStack(_int.valueOf(arg0)))

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
    def ncx(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.ncx(long)"""
        return int._wrap(_STBTTVertex.ncx(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.ny(long)"""
        return int._wrap(_STBTTVertex.ny(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.malloc()"""
        return STBTTVertex._wrap(_STBTTVertex.malloc())

    @overload
    def cx1(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.cx1()"""
        return int._wrap(super(STBTTVertex, self).cx1())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTVertex._wrap(_STBTTVertex.calloc(arg0))

    @staticmethod
    @overload
    def create() -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.create()"""
        return STBTTVertex._wrap(_STBTTVertex.create())

    @overload
    def cy1(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.cy1()"""
        return int._wrap(super(STBTTVertex, self).cy1())

    @overload
    def y(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.y()"""
        return int._wrap(super(STBTTVertex, self).y())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.mallocStack(int)"""
        return Buffer._wrap(_STBTTVertex.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTVertex.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc() -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.calloc()"""
        return STBTTVertex._wrap(_STBTTVertex.calloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.createSafe(long,int)"""
        return Buffer._wrap(_STBTTVertex.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTVertex.sizeof()"""
        return int._wrap(super(STBTTVertex, self).sizeof())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.createSafe(long)"""
        return STBTTVertex._wrap(_STBTTVertex.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTVertex._wrap(_STBTTVertex.malloc(arg0))

    @staticmethod
    @overload
    def ncy1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.ncy1(long)"""
        return int._wrap(_STBTTVertex.ncy1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.calloc(int)"""
        return Buffer._wrap(_STBTTVertex.calloc(_int.valueOf(arg0)))

    @overload
    def type(self) -> int:
        """public byte org.lwjgl.stb.STBTTVertex.type()"""
        return int._wrap(super(STBTTVertex, self).type())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTVertex.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ncy(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.ncy(long)"""
        return int._wrap(_STBTTVertex.ncy(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def callocStack() -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.callocStack()"""
        return STBTTVertex._wrap(_STBTTVertex.callocStack())

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.mallocStack()"""
        return STBTTVertex._wrap(_STBTTVertex.mallocStack())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTVertex._wrap(_STBTTVertex.mallocStack(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.create(long)"""
        return STBTTVertex._wrap(_STBTTVertex.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTVertex._wrap(_STBTTVertex.callocStack(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.malloc(int)"""
        return Buffer._wrap(_STBTTVertex.malloc(_int.valueOf(arg0)))

    @overload
    def x(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.x()"""
        return int._wrap(super(STBTTVertex, self).x())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBTTVertex.mallocStack(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTVertex(java.nio.ByteBuffer)"""
        val = _STBTTVertex(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.nx(long)"""
        return int._wrap(_STBTTVertex.nx(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def cx(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.cx()"""
        return int._wrap(super(STBTTVertex, self).cx())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def ncx1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.ncx1(long)"""
        return int._wrap(_STBTTVertex.ncx1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.create(long,int)"""
        return Buffer._wrap(_STBTTVertex.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def cy(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.cy()"""
        return int._wrap(super(STBTTVertex, self).cy())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.create(int)"""
        return Buffer._wrap(_STBTTVertex.create(_int.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBTTKerningentry$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.stb.STBTTKerningentry as _STBTTKerningentry_Buffer
_Buffer = _STBTTKerningentry_Buffer.Buffer
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
    """org.lwjgl.stb.STBTTKerningentry.Buffer"""
 
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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTKerningentry$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTKerningentry$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @overload
    def advance(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry$Buffer.advance()"""
        return int._wrap(super(Buffer, self).advance())

    @overload
    def glyph1(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry$Buffer.glyph1()"""
        return int._wrap(super(Buffer, self).glyph1())

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
    def glyph2(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry$Buffer.glyph2()"""
        return int._wrap(super(Buffer, self).glyph2())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBTTPackRange$Buffer
from pyquantum_helper import import_once as _import_once
import org.lwjgl.stb.STBTTPackedchar as _STBTTPackedchar_Buffer
_Buffer = _STBTTPackedchar_Buffer.Buffer
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Byte as _byte
import org.lwjgl.stb.STBTTPackRange as _STBTTPackRange_Buffer
_Buffer = _STBTTPackRange_Buffer.Buffer
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
import java.lang.Float as _float
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.stb.STBTTPackRange.Buffer"""
 
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
    def h_oversample(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.h_oversample(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).h_oversample(_byte.valueOf(arg0)))

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
    def array_of_unicode_codepoints(self) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.stb.STBTTPackRange$Buffer.array_of_unicode_codepoints()"""
        return 'IntBuffer'._wrap(super(Buffer, self).array_of_unicode_codepoints())

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
    def v_oversample(self) -> int:
        """public byte org.lwjgl.stb.STBTTPackRange$Buffer.v_oversample()"""
        return int._wrap(super(Buffer, self).v_oversample())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackRange$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTPackRange$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def num_chars(self) -> int:
        """public int org.lwjgl.stb.STBTTPackRange$Buffer.num_chars()"""
        return int._wrap(super(Buffer, self).num_chars())

    @overload
    def v_oversample(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.v_oversample(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).v_oversample(_byte.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def chardata_for_range(self, arg0: 'Buffer') -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.chardata_for_range(org.lwjgl.stb.STBTTPackedchar$Buffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).chardata_for_range(arg0))

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
    def first_unicode_codepoint_in_range(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.first_unicode_codepoint_in_range(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).first_unicode_codepoint_in_range(_int.valueOf(arg0)))

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
    def font_size(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.font_size(float)"""
        return 'Buffer'._wrap(super(_Buffer, self).font_size(_float.valueOf(arg0)))

    @overload
    def num_chars(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.num_chars(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).num_chars(_int.valueOf(arg0)))

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
    def font_size(self) -> float:
        """public float org.lwjgl.stb.STBTTPackRange$Buffer.font_size()"""
        return float._wrap(super(Buffer, self).font_size())

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

    @overload
    def h_oversample(self) -> int:
        """public byte org.lwjgl.stb.STBTTPackRange$Buffer.h_oversample()"""
        return int._wrap(super(Buffer, self).h_oversample())

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

    @overload
    def array_of_unicode_codepoints(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.array_of_unicode_codepoints(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).array_of_unicode_codepoints(arg0))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def chardata_for_range(self) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.chardata_for_range()"""
        return 'Buffer'._wrap(super(Buffer, self).chardata_for_range())

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
    def first_unicode_codepoint_in_range(self) -> int:
        """public int org.lwjgl.stb.STBTTPackRange$Buffer.first_unicode_codepoint_in_range()"""
        return int._wrap(super(Buffer, self).first_unicode_codepoint_in_range())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBVorbisAlloc
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.stb.STBVorbisAlloc as _STBVorbisAlloc
_STBVorbisAlloc = _STBVorbisAlloc
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
import org.lwjgl.stb.STBVorbisAlloc as _STBVorbisAlloc_Buffer
_Buffer = _STBVorbisAlloc_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBVorbisAlloc():
    """org.lwjgl.stb.STBVorbisAlloc"""
 
    @staticmethod
    def _wrap(java_value: _STBVorbisAlloc) -> 'STBVorbisAlloc':
        return STBVorbisAlloc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBVorbisAlloc):
        """
        Dynamic initializer for STBVorbisAlloc.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBVorbisAlloc__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBVorbisAlloc__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.malloc(int)"""
        return Buffer._wrap(_STBVorbisAlloc.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.stb.STBVorbisAlloc.validate(long)"""
        _STBVorbisAlloc.validate(_long.valueOf(arg0))

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
    def nalloc_buffer_length_in_bytes(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisAlloc.nalloc_buffer_length_in_bytes(long)"""
        return int._wrap(_STBVorbisAlloc.nalloc_buffer_length_in_bytes(_long.valueOf(arg0)))

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
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBVorbisAlloc.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def set(self, arg0: 'STBVorbisAlloc') -> 'STBVorbisAlloc':
        """public org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.set(org.lwjgl.stb.STBVorbisAlloc)"""
        return 'STBVorbisAlloc'._wrap(super(_STBVorbisAlloc, self).set(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.create(long,int)"""
        return Buffer._wrap(_STBVorbisAlloc.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.calloc(int)"""
        return Buffer._wrap(_STBVorbisAlloc.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.mallocStack(int)"""
        return Buffer._wrap(_STBVorbisAlloc.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.callocStack(int)"""
        return Buffer._wrap(_STBVorbisAlloc.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.create()"""
        return STBVorbisAlloc._wrap(_STBVorbisAlloc.create())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.createSafe(long)"""
        return STBVorbisAlloc._wrap(_STBVorbisAlloc.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.mallocStack()"""
        return STBVorbisAlloc._wrap(_STBVorbisAlloc.mallocStack())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.malloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisAlloc._wrap(_STBVorbisAlloc.malloc(arg0))

    @overload
    def alloc_buffer(self, arg0: 'ByteBuffer') -> 'STBVorbisAlloc':
        """public org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.alloc_buffer(java.nio.ByteBuffer)"""
        return 'STBVorbisAlloc'._wrap(super(_STBVorbisAlloc, self).alloc_buffer(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBVorbisAlloc.mallocStack(_int.valueOf(arg0), arg1))

    @overload
    def alloc_buffer_length_in_bytes(self) -> int:
        """public int org.lwjgl.stb.STBVorbisAlloc.alloc_buffer_length_in_bytes()"""
        return int._wrap(super(STBVorbisAlloc, self).alloc_buffer_length_in_bytes())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBVorbisAlloc.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.calloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisAlloc._wrap(_STBVorbisAlloc.calloc(arg0))

    @staticmethod
    @overload
    def nalloc_buffer(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBVorbisAlloc.nalloc_buffer(long)"""
        return ByteBuffer._wrap(_STBVorbisAlloc.nalloc_buffer(_long.valueOf(arg0)))

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
    def malloc() -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.malloc()"""
        return STBVorbisAlloc._wrap(_STBVorbisAlloc.malloc())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBVorbisAlloc._wrap(_STBVorbisAlloc.callocStack(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.create(long)"""
        return STBVorbisAlloc._wrap(_STBVorbisAlloc.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBVorbisAlloc._wrap(_STBVorbisAlloc.mallocStack(arg0))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.create(int)"""
        return Buffer._wrap(_STBVorbisAlloc.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nalloc_buffer_length_in_bytes(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBVorbisAlloc.nalloc_buffer_length_in_bytes(long,int)"""
        _STBVorbisAlloc.nalloc_buffer_length_in_bytes(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nalloc_buffer(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBVorbisAlloc.nalloc_buffer(long,java.nio.ByteBuffer)"""
        _STBVorbisAlloc.nalloc_buffer(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def callocStack() -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.callocStack()"""
        return STBVorbisAlloc._wrap(_STBVorbisAlloc.callocStack())

    @overload
    def alloc_buffer(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBVorbisAlloc.alloc_buffer()"""
        return 'ByteBuffer'._wrap(super(STBVorbisAlloc, self).alloc_buffer())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def calloc() -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.calloc()"""
        return STBVorbisAlloc._wrap(_STBVorbisAlloc.calloc())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.createSafe(long,int)"""
        return Buffer._wrap(_STBVorbisAlloc.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBVorbisAlloc.sizeof()"""
        return int._wrap(super(STBVorbisAlloc, self).sizeof())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBVorbisAlloc.callocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisAlloc(java.nio.ByteBuffer)"""
        val = _STBVorbisAlloc(arg0)
        self.__wrapper = val

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address()) 
 
 
# CLASS: org.lwjgl.stb.STBRPNode
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.stb.STBRPNode as _STBRPNode
_STBRPNode = _STBRPNode
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.stb.STBRPNode as _STBRPNode_Buffer
_Buffer = _STBRPNode_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBRPNode():
    """org.lwjgl.stb.STBRPNode"""
 
    @staticmethod
    def _wrap(java_value: _STBRPNode) -> 'STBRPNode':
        return STBRPNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBRPNode):
        """
        Dynamic initializer for STBRPNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBRPNode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBRPNode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBRPNode.sizeof()"""
        return int._wrap(super(STBRPNode, self).sizeof())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.callocStack(int)"""
        return Buffer._wrap(_STBRPNode.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nnext(arg0: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.nnext(long)"""
        return STBRPNode._wrap(_STBRPNode.nnext(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPNode._wrap(_STBRPNode.callocStack(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPNode(java.nio.ByteBuffer)"""
        val = _STBRPNode(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.calloc(int)"""
        return Buffer._wrap(_STBRPNode.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.calloc()"""
        return STBRPNode._wrap(_STBRPNode.calloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.createSafe(long,int)"""
        return Buffer._wrap(_STBRPNode.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.calloc(org.lwjgl.system.MemoryStack)"""
        return STBRPNode._wrap(_STBRPNode.calloc(arg0))

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
    def createSafe(arg0: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.createSafe(long)"""
        return STBRPNode._wrap(_STBRPNode.createSafe(_long.valueOf(arg0)))

    @overload
    def next(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.next()"""
        return 'STBRPNode'._wrap(super(STBRPNode, self).next())

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPNode.nx(long)"""
        return int._wrap(_STBRPNode.nx(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.create()"""
        return STBRPNode._wrap(_STBRPNode.create())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def x(self) -> int:
        """public int org.lwjgl.stb.STBRPNode.x()"""
        return int._wrap(super(STBRPNode, self).x())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.create(int)"""
        return Buffer._wrap(_STBRPNode.create(_int.valueOf(arg0)))

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
    def mallocStack() -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.mallocStack()"""
        return STBRPNode._wrap(_STBRPNode.mallocStack())

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.create(long)"""
        return STBRPNode._wrap(_STBRPNode.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.malloc()"""
        return STBRPNode._wrap(_STBRPNode.malloc())

    @staticmethod
    @overload
    def callocStack() -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.callocStack()"""
        return STBRPNode._wrap(_STBRPNode.callocStack())

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPNode.ny(long)"""
        return int._wrap(_STBRPNode.ny(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPNode.malloc(_int.valueOf(arg0), arg1))

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
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.malloc(int)"""
        return Buffer._wrap(_STBRPNode.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.create(long,int)"""
        return Buffer._wrap(_STBRPNode.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.mallocStack(int)"""
        return Buffer._wrap(_STBRPNode.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPNode.mallocStack(_int.valueOf(arg0), arg1))

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
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPNode.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_STBRPNode.callocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPNode._wrap(_STBRPNode.mallocStack(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def y(self) -> int:
        """public int org.lwjgl.stb.STBRPNode.y()"""
        return int._wrap(super(STBRPNode, self).y())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.malloc(org.lwjgl.system.MemoryStack)"""
        return STBRPNode._wrap(_STBRPNode.malloc(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address()) 
 
 
# CLASS: org.lwjgl.stb.STBImageWrite
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import org.lwjgl.stb.STBImageWrite as _STBImageWrite
_STBImageWrite = _STBImageWrite
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBImageWrite():
    """org.lwjgl.stb.STBImageWrite"""
 
    @staticmethod
    def _wrap(java_value: _STBImageWrite) -> 'STBImageWrite':
        return STBImageWrite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBImageWrite):
        """
        Dynamic initializer for STBImageWrite.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBImageWrite__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBImageWrite__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def stbi_write_tga(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_tga(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer)"""
        return bool._wrap(_STBImageWrite.stbi_write_tga(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def stbi_write_jpg_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'ByteBuffer', arg6: int) -> int:
        """public static int org.lwjgl.stb.STBImageWrite.stbi_write_jpg_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,java.nio.ByteBuffer,int)"""
        return int._wrap(_STBImageWrite.stbi_write_jpg_to_func(arg0, _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _int.valueOf(arg6)))

    @staticmethod
    @overload
    def stbi_write_bmp(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_bmp(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer)"""
        return bool._wrap(_STBImageWrite.stbi_write_bmp(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def stbi_write_png(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_png(java.lang.CharSequence,int,int,int,java.nio.ByteBuffer,int)"""
        return bool._wrap(_STBImageWrite.stbi_write_png(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def stbi_write_png(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_png(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int)"""
        return bool._wrap(_STBImageWrite.stbi_write_png(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_write_bmp_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_bmp_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,java.nio.ByteBuffer)"""
        return bool._wrap(_STBImageWrite.stbi_write_bmp_to_func(arg0, _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def nstbi_write_hdr_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_hdr_to_func(long,long,int,int,int,long)"""
        return int._wrap(_STBImageWrite.nstbi_write_hdr_to_func(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_write_hdr(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'float') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr(java.nio.ByteBuffer,int,int,int,float[])"""
        return bool._wrap(_STBImageWrite.stbi_write_hdr(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def stbi_write_png_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'ByteBuffer', arg6: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_png_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,java.nio.ByteBuffer,int)"""
        return bool._wrap(_STBImageWrite.stbi_write_png_to_func(arg0, _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _int.valueOf(arg6)))

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
    def nstbi_write_jpg(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_jpg(long,int,int,int,long,int)"""
        return int._wrap(_STBImageWrite.nstbi_write_jpg(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_write_hdr(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'float') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr(java.lang.CharSequence,int,int,int,float[])"""
        return bool._wrap(_STBImageWrite.stbi_write_hdr(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def nstbi_write_bmp(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_bmp(long,int,int,int,long)"""
        return int._wrap(_STBImageWrite.nstbi_write_bmp(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_write_png(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_png(long,int,int,int,long,int)"""
        return int._wrap(_STBImageWrite.nstbi_write_png(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def stbi_write_jpg(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_jpg(java.lang.CharSequence,int,int,int,java.nio.ByteBuffer,int)"""
        return bool._wrap(_STBImageWrite.stbi_write_jpg(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_write_hdr_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float') -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_hdr_to_func(long,long,int,int,int,float[])"""
        return int._wrap(_STBImageWrite.nstbi_write_hdr_to_func(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def stbi_write_hdr(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr(java.lang.CharSequence,int,int,int,java.nio.FloatBuffer)"""
        return bool._wrap(_STBImageWrite.stbi_write_hdr(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def nstbi_write_hdr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float') -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_hdr(long,int,int,int,float[])"""
        return int._wrap(_STBImageWrite.nstbi_write_hdr(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def nstbi_flip_vertically_on_write(arg0: int):
        """public static native void org.lwjgl.stb.STBImageWrite.nstbi_flip_vertically_on_write(int)"""
        _STBImageWrite.nstbi_flip_vertically_on_write(_int.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_flip_vertically_on_write(arg0: bool):
        """public static void org.lwjgl.stb.STBImageWrite.stbi_flip_vertically_on_write(boolean)"""
        _STBImageWrite.stbi_flip_vertically_on_write(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def stbi_write_tga(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_tga(java.lang.CharSequence,int,int,int,java.nio.ByteBuffer)"""
        return bool._wrap(_STBImageWrite.stbi_write_tga(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def nstbi_write_png_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_png_to_func(long,long,int,int,int,long,int)"""
        return int._wrap(_STBImageWrite.nstbi_write_png_to_func(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6)))

    @staticmethod
    @overload
    def stbi_write_hdr_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'FloatBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,java.nio.FloatBuffer)"""
        return bool._wrap(_STBImageWrite.stbi_write_hdr_to_func(arg0, _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nstbi_write_jpg_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_jpg_to_func(long,long,int,int,int,long,int)"""
        return int._wrap(_STBImageWrite.nstbi_write_jpg_to_func(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6)))

    @staticmethod
    @overload
    def nstbi_write_tga_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_tga_to_func(long,long,int,int,int,long)"""
        return int._wrap(_STBImageWrite.nstbi_write_tga_to_func(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_write_hdr_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,float[])"""
        return bool._wrap(_STBImageWrite.stbi_write_hdr_to_func(arg0, _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nstbi_write_tga(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_tga(long,int,int,int,long)"""
        return int._wrap(_STBImageWrite.nstbi_write_tga(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_write_jpg(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_jpg(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int)"""
        return bool._wrap(_STBImageWrite.stbi_write_jpg(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_write_hdr(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr(java.nio.ByteBuffer,int,int,int,java.nio.FloatBuffer)"""
        return bool._wrap(_STBImageWrite.stbi_write_hdr(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def stbi_write_tga_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_tga_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,java.nio.ByteBuffer)"""
        return bool._wrap(_STBImageWrite.stbi_write_tga_to_func(arg0, _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def nstbi_write_hdr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_hdr(long,int,int,int,long)"""
        return int._wrap(_STBImageWrite.nstbi_write_hdr(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_write_bmp_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_bmp_to_func(long,long,int,int,int,long)"""
        return int._wrap(_STBImageWrite.nstbi_write_bmp_to_func(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def stbi_write_bmp(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_bmp(java.lang.CharSequence,int,int,int,java.nio.ByteBuffer)"""
        return bool._wrap(_STBImageWrite.stbi_write_bmp(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.stb.STBVorbisAlloc$Buffer
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
import org.lwjgl.stb.STBVorbisAlloc as _STBVorbisAlloc_Buffer
_Buffer = _STBVorbisAlloc_Buffer.Buffer
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
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.stb.STBVorbisAlloc.Buffer"""
 
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
    def alloc_buffer_length_in_bytes(self) -> int:
        """public int org.lwjgl.stb.STBVorbisAlloc$Buffer.alloc_buffer_length_in_bytes()"""
        return int._wrap(super(Buffer, self).alloc_buffer_length_in_bytes())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisAlloc$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBVorbisAlloc$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
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
    def alloc_buffer(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBVorbisAlloc$Buffer.alloc_buffer()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).alloc_buffer())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def alloc_buffer(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc$Buffer.alloc_buffer(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).alloc_buffer(arg0))

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBIWriteCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
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
from abc import abstractmethod, ABC
import org.lwjgl.stb.STBIWriteCallback as _STBIWriteCallback
_STBIWriteCallback = _STBIWriteCallback
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
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import org.lwjgl.stb.STBIWriteCallbackI as _STBIWriteCallbackI
_STBIWriteCallbackI = _STBIWriteCallbackI
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class STBIWriteCallback():
    """org.lwjgl.stb.STBIWriteCallback"""
 
    @staticmethod
    def _wrap(java_value: _STBIWriteCallback) -> 'STBIWriteCallback':
        return STBIWriteCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _STBIWriteCallback):
        """
        Dynamic initializer for STBIWriteCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_STBIWriteCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_STBIWriteCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: 'STBIWriteCallbackI') -> 'STBIWriteCallback':
        """public static org.lwjgl.stb.STBIWriteCallback org.lwjgl.stb.STBIWriteCallback.create(org.lwjgl.stb.STBIWriteCallbackI)"""
        return STBIWriteCallback._wrap(_STBIWriteCallback.create(arg0))

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIWriteCallbackI.callback(long,long)"""
        super(_STBIWriteCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBIWriteCallback':
        """public static org.lwjgl.stb.STBIWriteCallback org.lwjgl.stb.STBIWriteCallback.create(long)"""
        return STBIWriteCallback._wrap(_STBIWriteCallback.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def getData(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBIWriteCallback.getData(long,int)"""
        return ByteBuffer._wrap(_STBIWriteCallback.getData(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBIWriteCallback':
        """public static org.lwjgl.stb.STBIWriteCallback org.lwjgl.stb.STBIWriteCallback.createSafe(long)"""
        return STBIWriteCallback._wrap(_STBIWriteCallback.createSafe(_long.valueOf(arg0)))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIWriteCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(STBIWriteCallbackI, self).getCallInterface())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.stb.STBIWriteCallbackI.invoke(long,long,int)"""
        pass