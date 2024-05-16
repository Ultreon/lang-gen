from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import org.lwjgl.system.linux.liburing.IOURingRecvmsgOut as __IOURingRecvmsgOut_Buffer
__Buffer = __IOURingRecvmsgOut_Buffer.Buffer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def controllen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.controllen()"""
        return int.__wrap(super(Buffer, self).controllen())

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def payloadlen(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.payloadlen(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).payloadlen(__int.valueOf(arg0)))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def namelen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.namelen()"""
        return int.__wrap(super(Buffer, self).namelen())

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
    def payloadlen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.payloadlen()"""
        return int.__wrap(super(Buffer, self).payloadlen())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

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

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def namelen(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.namelen(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).namelen(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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
    def controllen(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.controllen(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).controllen(__int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__int.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1)))

 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import org.lwjgl.system.linux.liburing.IOURingRecvmsgOut as __IOURingRecvmsgOut_Buffer
__Buffer = __IOURingRecvmsgOut_Buffer.Buffer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def controllen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.controllen()"""
        return int.__wrap(super(Buffer, self).controllen())

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def payloadlen(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.payloadlen(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).payloadlen(__int.valueOf(arg0)))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def namelen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.namelen()"""
        return int.__wrap(super(Buffer, self).namelen())

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
    def payloadlen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.payloadlen()"""
        return int.__wrap(super(Buffer, self).payloadlen())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

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

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def namelen(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.namelen(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).namelen(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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
    def controllen(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.controllen(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).controllen(__int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__int.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1)))

 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Short as __short
import org.lwjgl.system.linux.liburing.IOURingBufReg as __IOURingBufReg_Buffer
__Buffer = __IOURingBufReg_Buffer.Buffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingBufReg.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def resv(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.resv(int,long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv(__int.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def resv(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.resv(int)"""
        return int.__wrap(super(__Buffer, self).resv(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def bgid(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.bgid(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).bgid(__short.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def resv(self, arg0: 'LongBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.resv(java.nio.LongBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv(arg0))

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.ring_entries()"""
        return int.__wrap(super(Buffer, self).ring_entries())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def ring_addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.ring_addr()"""
        return int.__wrap(super(Buffer, self).ring_addr())

    @overload
    def bgid(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.bgid()"""
        return int.__wrap(super(Buffer, self).bgid())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.flags(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__short.valueOf(arg0)))

    @overload
    def resv(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.resv()"""
        return 'LongBuffer'.__wrap(super(Buffer, self).resv())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def flags(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def ring_addr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.ring_addr(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_addr(__long.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

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

    @overload
    def ring_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.ring_entries(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_entries(__int.valueOf(arg0)))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSyncCancelReg
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingSyncCancelReg as __IOURingSyncCancelReg
__IOURingSyncCancelReg = __IOURingSyncCancelReg
try:
    from pyglsystem import linux
except ImportError:
    linux = __import_once__("pyglsystem.linux")

import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import org.lwjgl.system.linux.liburing.IOURingSyncCancelReg as __IOURingSyncCancelReg_Buffer
__Buffer = __IOURingSyncCancelReg_Buffer.Buffer
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.KernelTimespec as __KernelTimespec
__KernelTimespec = __KernelTimespec
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingSyncCancelReg():
    """org.lwjgl.system.linux.liburing.IOURingSyncCancelReg"""
 
    @staticmethod
    def __wrap(java_value: __IOURingSyncCancelReg) -> 'IOURingSyncCancelReg':
        return IOURingSyncCancelReg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingSyncCancelReg):
        """
        Dynamic initializer for IOURingSyncCancelReg.
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
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.addr()"""
        return int.__wrap(super(IOURingSyncCancelReg, self).addr())

    @staticmethod
    @overload
    def ntimeout(arg0: int, arg1: 'KernelTimespec'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.ntimeout(long,org.lwjgl.system.linux.KernelTimespec)"""
        __IOURingSyncCancelReg.ntimeout(__long.valueOf(arg0), arg1)

    @overload
    def flags(self, arg0: int) -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.flags(int)"""
        return 'IOURingSyncCancelReg'.__wrap(super(__IOURingSyncCancelReg, self).flags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.create(long)"""
        return IOURingSyncCancelReg.__wrap(__IOURingSyncCancelReg.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntimeout(arg0: int) -> 'linux.KernelTimespec':
        """public static org.lwjgl.system.linux.KernelTimespec org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.ntimeout(long)"""
        return linux.KernelTimespec.__wrap(__IOURingSyncCancelReg.ntimeout(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def npad(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.npad(long)"""
        return LongBuffer.__wrap(__IOURingSyncCancelReg.npad(__long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.nflags(long)"""
        return int.__wrap(__IOURingSyncCancelReg.nflags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nfd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.nfd(long,int)"""
        __IOURingSyncCancelReg.nfd(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def timeout(self, arg0: 'KernelTimespec') -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.timeout(org.lwjgl.system.linux.KernelTimespec)"""
        return 'IOURingSyncCancelReg'.__wrap(super(__IOURingSyncCancelReg, self).timeout(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.create(long,int)"""
        return Buffer.__wrap(__IOURingSyncCancelReg.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.npad(long,int,long)"""
        __IOURingSyncCancelReg.npad(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.calloc(int)"""
        return Buffer.__wrap(__IOURingSyncCancelReg.calloc(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg(java.nio.ByteBuffer)"""
        val = __IOURingSyncCancelReg(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def nfd(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.nfd(long)"""
        return int.__wrap(__IOURingSyncCancelReg.nfd(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: 'LongBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.npad(long,java.nio.LongBuffer)"""
        __IOURingSyncCancelReg.npad(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.create(int)"""
        return Buffer.__wrap(__IOURingSyncCancelReg.create(__int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def addr(self, arg0: int) -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.addr(long)"""
        return 'IOURingSyncCancelReg'.__wrap(super(__IOURingSyncCancelReg, self).addr(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.npad(long,int)"""
        return int.__wrap(__IOURingSyncCancelReg.npad(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.flags()"""
        return int.__wrap(super(IOURingSyncCancelReg, self).flags())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSyncCancelReg.__wrap(__IOURingSyncCancelReg.malloc(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def fd(self, arg0: int) -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.fd(int)"""
        return 'IOURingSyncCancelReg'.__wrap(super(__IOURingSyncCancelReg, self).fd(__int.valueOf(arg0)))

    @overload
    def fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.fd()"""
        return int.__wrap(super(IOURingSyncCancelReg, self).fd())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingSyncCancelReg.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingSyncCancelReg.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create() -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.create()"""
        return IOURingSyncCancelReg.__wrap(__IOURingSyncCancelReg.create())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingSyncCancelReg.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.nflags(long,int)"""
        __IOURingSyncCancelReg.nflags(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'KernelTimespec') -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.set(long,int,int,org.lwjgl.system.linux.KernelTimespec)"""
        return 'IOURingSyncCancelReg'.__wrap(super(__IOURingSyncCancelReg, self).set(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.createSafe(long)"""
        return IOURingSyncCancelReg.__wrap(__IOURingSyncCancelReg.createSafe(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingSyncCancelReg') -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.set(org.lwjgl.system.linux.liburing.IOURingSyncCancelReg)"""
        return 'IOURingSyncCancelReg'.__wrap(super(__IOURingSyncCancelReg, self).set(arg0))

    @staticmethod
    @overload
    def naddr(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.naddr(long)"""
        return int.__wrap(__IOURingSyncCancelReg.naddr(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc() -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.malloc()"""
        return IOURingSyncCancelReg.__wrap(__IOURingSyncCancelReg.malloc())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def calloc() -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.calloc()"""
        return IOURingSyncCancelReg.__wrap(__IOURingSyncCancelReg.calloc())

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
    def calloc(arg0: 'MemoryStack') -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSyncCancelReg.__wrap(__IOURingSyncCancelReg.calloc(arg0))

    @overload
    def timeout(self) -> 'linux.KernelTimespec':
        """public org.lwjgl.system.linux.KernelTimespec org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.timeout()"""
        return 'linux.KernelTimespec'.__wrap(super(IOURingSyncCancelReg, self).timeout())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.malloc(int)"""
        return Buffer.__wrap(__IOURingSyncCancelReg.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.sizeof()"""
        return int.__wrap(super(IOURingSyncCancelReg, self).sizeof())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def timeout(self, arg0: 'Consumer') -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.timeout(java.util.function.Consumer<org.lwjgl.system.linux.KernelTimespec>)"""
        return 'IOURingSyncCancelReg'.__wrap(super(__IOURingSyncCancelReg, self).timeout(arg0))

    @staticmethod
    @overload
    def naddr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.naddr(long,long)"""
        __IOURingSyncCancelReg.naddr(__long.valueOf(arg0), __long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.linux.liburing.IOSQRingOffsets as __IOSQRingOffsets_Buffer
__Buffer = __IOSQRingOffsets_Buffer.Buffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOSQRingOffsets.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def array(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.array()"""
        return int.__wrap(super(Buffer, self).array())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.head()"""
        return int.__wrap(super(Buffer, self).head())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.ring_mask()"""
        return int.__wrap(super(Buffer, self).ring_mask())

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.tail()"""
        return int.__wrap(super(Buffer, self).tail())

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
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.ring_entries()"""
        return int.__wrap(super(Buffer, self).ring_entries())

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def array(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.array(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).array(__int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def dropped(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.dropped()"""
        return int.__wrap(super(Buffer, self).dropped())

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
    def head(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.head(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).head(__int.valueOf(arg0)))

    @overload
    def tail(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.tail(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).tail(__int.valueOf(arg0)))

    @overload
    def ring_mask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.ring_mask(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_mask(__int.valueOf(arg0)))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

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
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__int.valueOf(arg0)))

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

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def dropped(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.dropped(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dropped(__int.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def ring_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.ring_entries(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_entries(__int.valueOf(arg0)))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingParams$Buffer
from pyquantum_helper import import_once as __import_once__
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.linux.liburing.IOCQRingOffsets as __IOCQRingOffsets
__IOCQRingOffsets = __IOCQRingOffsets
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
import org.lwjgl.system.linux.liburing.IOURingParams as __IOURingParams_Buffer
__Buffer = __IOURingParams_Buffer.Buffer
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.liburing.IOSQRingOffsets as __IOSQRingOffsets
__IOSQRingOffsets = __IOSQRingOffsets
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingParams.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def cq_off(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.cq_off(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOCQRingOffsets>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cq_off(arg0))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def sq_off(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_off(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOSQRingOffsets>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sq_off(arg0))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def resv(self, arg0: int) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.resv(int)"""
        return int.__wrap(super(__Buffer, self).resv(__int.valueOf(arg0)))

    @overload
    def sq_thread_idle(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_thread_idle()"""
        return int.__wrap(super(Buffer, self).sq_thread_idle())

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def cq_off(self, arg0: 'IOCQRingOffsets') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.cq_off(org.lwjgl.system.linux.liburing.IOCQRingOffsets)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cq_off(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def wq_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.wq_fd()"""
        return int.__wrap(super(Buffer, self).wq_fd())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def sq_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_entries()"""
        return int.__wrap(super(Buffer, self).sq_entries())

    @overload
    def features(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.features()"""
        return int.__wrap(super(Buffer, self).features())

    @overload
    def sq_off(self, arg0: 'IOSQRingOffsets') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_off(org.lwjgl.system.linux.liburing.IOSQRingOffsets)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sq_off(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def cq_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.cq_entries()"""
        return int.__wrap(super(Buffer, self).cq_entries())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def resv(self) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.resv()"""
        return 'IntBuffer'.__wrap(super(Buffer, self).resv())

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
    def features(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.features(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).features(__int.valueOf(arg0)))

    @overload
    def resv(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.resv(int,int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def cq_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.cq_entries(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cq_entries(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__int.valueOf(arg0)))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def sq_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_entries(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sq_entries(__int.valueOf(arg0)))

    @overload
    def sq_off(self) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_off()"""
        return 'IOSQRingOffsets'.__wrap(super(Buffer, self).sq_off())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def sq_thread_cpu(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_thread_cpu(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sq_thread_cpu(__int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def wq_fd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.wq_fd(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).wq_fd(__int.valueOf(arg0)))

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
    def sq_thread_idle(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_thread_idle(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sq_thread_idle(__int.valueOf(arg0)))

    @overload
    def resv(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.resv(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv(arg0))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

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
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def cq_off(self) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams$Buffer.cq_off()"""
        return 'IOCQRingOffsets'.__wrap(super(Buffer, self).cq_off())

    @overload
    def sq_thread_cpu(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_thread_cpu()"""
        return int.__wrap(super(Buffer, self).sq_thread_cpu())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURing
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingSQ as __IOURingSQ
__IOURingSQ = __IOURingSQ
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.linux.liburing.IOURing as __IOURing
__IOURing = __IOURing
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.liburing.IOURing as __IOURing_Buffer
__Buffer = __IOURing_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.linux.liburing.IOURingCQ as __IOURingCQ
__IOURingCQ = __IOURingCQ
from builtins import bool
from builtins import int
 
class IOURing():
    """org.lwjgl.system.linux.liburing.IOURing"""
 
    @staticmethod
    def __wrap(java_value: __IOURing) -> 'IOURing':
        return IOURing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURing):
        """
        Dynamic initializer for IOURing.
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
    def sq(self, arg0: 'IOURingSQ') -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.sq(org.lwjgl.system.linux.liburing.IOURingSQ)"""
        return 'IOURing'.__wrap(super(__IOURing, self).sq(arg0))

    @overload
    def enter_ring_fd(self, arg0: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.enter_ring_fd(int)"""
        return 'IOURing'.__wrap(super(__IOURing, self).enter_ring_fd(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.create()"""
        return IOURing.__wrap(__IOURing.create())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.createSafe(long)"""
        return IOURing.__wrap(__IOURing.createSafe(__long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nint_flags(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURing.nint_flags(long)"""
        return int.__wrap(__IOURing.nint_flags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nfeatures(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nfeatures(long,int)"""
        __IOURing.nfeatures(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def int_flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURing.int_flags()"""
        return int.__wrap(super(IOURing, self).int_flags())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nenter_ring_fd(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURing.nenter_ring_fd(long)"""
        return int.__wrap(__IOURing.nenter_ring_fd(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_fd(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURing.nring_fd(long)"""
        return int.__wrap(__IOURing.nring_fd(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nint_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nint_flags(long,byte)"""
        __IOURing.nint_flags(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURing.nflags(long)"""
        return int.__wrap(__IOURing.nflags(__long.valueOf(arg0)))

    @overload
    def int_flags(self, arg0: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.int_flags(byte)"""
        return 'IOURing'.__wrap(super(__IOURing, self).int_flags(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.createSafe(long,int)"""
        return Buffer.__wrap(__IOURing.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def sq(self) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURing.sq()"""
        return 'IOURingSQ'.__wrap(super(IOURing, self).sq())

    @staticmethod
    @overload
    def npad2(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURing.npad2(long)"""
        return int.__wrap(__IOURing.npad2(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURing.npad(long)"""
        return ByteBuffer.__wrap(__IOURing.npad(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.malloc(int)"""
        return Buffer.__wrap(__IOURing.malloc(__int.valueOf(arg0)))

    @overload
    def sq(self, arg0: 'Consumer') -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.sq(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingSQ>)"""
        return 'IOURing'.__wrap(super(__IOURing, self).sq(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def nring_fd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nring_fd(long,int)"""
        __IOURing.nring_fd(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURing.__wrap(__IOURing.calloc(arg0))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def flags(self, arg0: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.flags(int)"""
        return 'IOURing'.__wrap(super(__IOURing, self).flags(__int.valueOf(arg0)))

    @overload
    def features(self, arg0: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.features(int)"""
        return 'IOURing'.__wrap(super(__IOURing, self).features(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURing.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc() -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.calloc()"""
        return IOURing.__wrap(__IOURing.calloc())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nflags(long,int)"""
        __IOURing.nflags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def ncq(arg0: int) -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURing.ncq(long)"""
        return IOURingCQ.__wrap(__IOURing.ncq(__long.valueOf(arg0)))

    @overload
    def features(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing.features()"""
        return int.__wrap(super(IOURing, self).features())

    @overload
    def set(self, arg0: 'IOURing') -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.set(org.lwjgl.system.linux.liburing.IOURing)"""
        return 'IOURing'.__wrap(super(__IOURing, self).set(arg0))

    @staticmethod
    @overload
    def malloc() -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.malloc()"""
        return IOURing.__wrap(__IOURing.malloc())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def enter_ring_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing.enter_ring_fd()"""
        return int.__wrap(super(IOURing, self).enter_ring_fd())

    @staticmethod
    @overload
    def nsq(arg0: int) -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURing.nsq(long)"""
        return IOURingSQ.__wrap(__IOURing.nsq(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nenter_ring_fd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nenter_ring_fd(long,int)"""
        __IOURing.nenter_ring_fd(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: 'IOURingSQ', arg1: 'IOURingCQ', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.set(org.lwjgl.system.linux.liburing.IOURingSQ,org.lwjgl.system.linux.liburing.IOURingCQ,int,int,int,int,byte)"""
        return 'IOURing'.__wrap(super(__IOURing, self).set(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __byte.valueOf(arg6)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURing(java.nio.ByteBuffer)"""
        val = __IOURing(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.create(int)"""
        return Buffer.__wrap(__IOURing.create(__int.valueOf(arg0)))

    @overload
    def cq(self, arg0: 'Consumer') -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.cq(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingCQ>)"""
        return 'IOURing'.__wrap(super(__IOURing, self).cq(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.create(long,int)"""
        return Buffer.__wrap(__IOURing.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURing.malloc(__int.valueOf(arg0), arg1))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing.flags()"""
        return int.__wrap(super(IOURing, self).flags())

    @overload
    def ring_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing.ring_fd()"""
        return int.__wrap(super(IOURing, self).ring_fd())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing.sizeof()"""
        return int.__wrap(super(IOURing, self).sizeof())

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURing.npad(long,int)"""
        return int.__wrap(__IOURing.npad(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nsq(arg0: int, arg1: 'IOURingSQ'):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nsq(long,org.lwjgl.system.linux.liburing.IOURingSQ)"""
        __IOURing.nsq(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nfeatures(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURing.nfeatures(long)"""
        return int.__wrap(__IOURing.nfeatures(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.create(long)"""
        return IOURing.__wrap(__IOURing.create(__long.valueOf(arg0)))

    @overload
    def ring_fd(self, arg0: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.ring_fd(int)"""
        return 'IOURing'.__wrap(super(__IOURing, self).ring_fd(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.npad(long,int,byte)"""
        __IOURing.npad(__long.valueOf(arg0), __int.valueOf(arg1), __byte.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.validate(long)"""
        __IOURing.validate(__long.valueOf(arg0))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURing.__wrap(__IOURing.malloc(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def npad(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURing.npad(long,java.nio.ByteBuffer)"""
        __IOURing.npad(__long.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def cq(self) -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURing.cq()"""
        return 'IOURingCQ'.__wrap(super(IOURing, self).cq())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def cq(self, arg0: 'IOURingCQ') -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.cq(org.lwjgl.system.linux.liburing.IOURingCQ)"""
        return 'IOURing'.__wrap(super(__IOURing, self).cq(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.calloc(int)"""
        return Buffer.__wrap(__IOURing.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def npad2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.npad2(long,int)"""
        __IOURing.npad2(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def ncq(arg0: int, arg1: 'IOURingCQ'):
        """public static void org.lwjgl.system.linux.liburing.IOURing.ncq(long,org.lwjgl.system.linux.liburing.IOURingCQ)"""
        __IOURing.ncq(__long.valueOf(arg0), arg1) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate as __IOURingRSRCUpdate_Buffer
__Buffer = __IOURingRSRCUpdate_Buffer.Buffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.resv(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv(__int.valueOf(arg0)))

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def offset(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.offset(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).offset(__int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def offset(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.offset()"""
        return int.__wrap(super(Buffer, self).offset())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def data(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.data(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).data(__long.valueOf(arg0)))

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
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.data()"""
        return int.__wrap(super(Buffer, self).data())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def resv(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.resv()"""
        return int.__wrap(super(Buffer, self).resv())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingProbe
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.linux.liburing.IOURingProbeOp as __IOURingProbeOp
__IOURingProbeOp = __IOURingProbeOp
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.function.Consumer as Consumer
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import java.lang.Short as __short
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.lwjgl.system.linux.liburing.IOURingProbe as __IOURingProbe_Buffer
__Buffer = __IOURingProbe_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.liburing.IOURingProbeOp as __IOURingProbeOp_Buffer
__Buffer = __IOURingProbeOp_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.linux.liburing.IOURingProbe as __IOURingProbe
__IOURingProbe = __IOURingProbe
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class IOURingProbe():
    """org.lwjgl.system.linux.liburing.IOURingProbe"""
 
    @staticmethod
    def __wrap(java_value: __IOURingProbe) -> 'IOURingProbe':
        return IOURingProbe(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingProbe):
        """
        Dynamic initializer for IOURingProbe.
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
    def createSafe(arg0: int) -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.createSafe(long)"""
        return IOURingProbe.__wrap(__IOURingProbe.createSafe(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingProbe(java.nio.ByteBuffer)"""
        val = __IOURingProbe(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingProbe.sizeof()"""
        return int.__wrap(super(IOURingProbe, self).sizeof())

    @overload
    def resv(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingProbe.resv()"""
        return int.__wrap(super(IOURingProbe, self).resv())

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingProbe.nresv(long)"""
        return int.__wrap(__IOURingProbe.nresv(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.calloc(int)"""
        return Buffer.__wrap(__IOURingProbe.calloc(__int.valueOf(arg0)))

    @overload
    def ops_len(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbe.ops_len()"""
        return int.__wrap(super(IOURingProbe, self).ops_len())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def create() -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.create()"""
        return IOURingProbe.__wrap(__IOURingProbe.create())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nops(arg0: int, arg1: 'Buffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nops(long,org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer)"""
        __IOURingProbe.nops(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nresv2(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingProbe.nresv2(long)"""
        return IntBuffer.__wrap(__IOURingProbe.nresv2(__long.valueOf(arg0)))

    @overload
    def last_op(self, arg0: int) -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.last_op(byte)"""
        return 'IOURingProbe'.__wrap(super(__IOURingProbe, self).last_op(__byte.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingProbe') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.set(org.lwjgl.system.linux.liburing.IOURingProbe)"""
        return 'IOURingProbe'.__wrap(super(__IOURingProbe, self).set(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.create(long,int)"""
        return Buffer.__wrap(__IOURingProbe.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nresv2(long,int,int)"""
        __IOURingProbe.nresv2(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nlast_op(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nlast_op(long,byte)"""
        __IOURingProbe.nlast_op(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def calloc() -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.calloc()"""
        return IOURingProbe.__wrap(__IOURingProbe.calloc())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nresv(long,short)"""
        __IOURingProbe.nresv(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def nops(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.nops(long)"""
        return Buffer.__wrap(__IOURingProbe.nops(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingProbe.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.malloc(int)"""
        return Buffer.__wrap(__IOURingProbe.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def ops(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbe.ops(int)"""
        return 'IOURingProbeOp'.__wrap(super(__IOURingProbe, self).ops(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingProbe.__wrap(__IOURingProbe.calloc(arg0))

    @overload
    def ops_len(self, arg0: int) -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.ops_len(byte)"""
        return 'IOURingProbe'.__wrap(super(__IOURingProbe, self).ops_len(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.create(long)"""
        return IOURingProbe.__wrap(__IOURingProbe.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingProbe.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nops(arg0: int, arg1: int) -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbe.nops(long,int)"""
        return IOURingProbeOp.__wrap(__IOURingProbe.nops(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingProbe.nresv2(long,int)"""
        return int.__wrap(__IOURingProbe.nresv2(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def ops(self, arg0: 'Buffer') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.ops(org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer)"""
        return 'IOURingProbe'.__wrap(super(__IOURingProbe, self).ops(arg0))

    @staticmethod
    @overload
    def nops(arg0: int, arg1: int, arg2: 'IOURingProbeOp'):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nops(long,int,org.lwjgl.system.linux.liburing.IOURingProbeOp)"""
        __IOURingProbe.nops(__long.valueOf(arg0), __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingProbe.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingProbe.__wrap(__IOURingProbe.malloc(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.set(byte,byte,short,org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer)"""
        return 'IOURingProbe'.__wrap(super(__IOURingProbe, self).set(__byte.valueOf(arg0), __byte.valueOf(arg1), __short.valueOf(arg2), arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc() -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.malloc()"""
        return IOURingProbe.__wrap(__IOURingProbe.malloc())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def resv(self, arg0: int) -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.resv(short)"""
        return 'IOURingProbe'.__wrap(super(__IOURingProbe, self).resv(__short.valueOf(arg0)))

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
    def nresv2(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nresv2(long,java.nio.IntBuffer)"""
        __IOURingProbe.nresv2(__long.valueOf(arg0), arg1)

    @overload
    def last_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbe.last_op()"""
        return int.__wrap(super(IOURingProbe, self).last_op())

    @overload
    def ops(self, arg0: int, arg1: 'IOURingProbeOp') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.ops(int,org.lwjgl.system.linux.liburing.IOURingProbeOp)"""
        return 'IOURingProbe'.__wrap(super(__IOURingProbe, self).ops(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nops_len(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingProbe.nops_len(long)"""
        return int.__wrap(__IOURingProbe.nops_len(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def ops(self, arg0: int, arg1: 'Consumer') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.ops(int,java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingProbeOp>)"""
        return 'IOURingProbe'.__wrap(super(__IOURingProbe, self).ops(__int.valueOf(arg0), arg1))

    @overload
    def ops(self, arg0: 'Consumer') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.ops(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer>)"""
        return 'IOURingProbe'.__wrap(super(__IOURingProbe, self).ops(arg0))

    @overload
    def ops(self) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.ops()"""
        return 'Buffer'.__wrap(super(IOURingProbe, self).ops())

    @staticmethod
    @overload
    def nlast_op(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingProbe.nlast_op(long)"""
        return int.__wrap(__IOURingProbe.nlast_op(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nops_len(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nops_len(long,byte)"""
        __IOURingProbe.nops_len(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.create(int)"""
        return Buffer.__wrap(__IOURingProbe.create(__int.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingCQE$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import org.lwjgl.system.linux.liburing.IOURingCQE as __IOURingCQE_Buffer
__Buffer = __IOURingCQE_Buffer.Buffer
import java.lang.Long as __long
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingCQE.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def res(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.res()"""
        return int.__wrap(super(Buffer, self).res())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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
    def user_data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.user_data()"""
        return int.__wrap(super(Buffer, self).user_data())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def user_data(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.user_data(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).user_data(__long.valueOf(arg0)))

    @overload
    def big_cqe(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.big_cqe(int,long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).big_cqe(__int.valueOf(arg0), __long.valueOf(arg1)))

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
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def big_cqe(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.big_cqe(int)"""
        return int.__wrap(super(__Buffer, self).big_cqe(__int.valueOf(arg0)))

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

    @overload
    def big_cqe(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.big_cqe()"""
        return 'LongBuffer'.__wrap(super(Buffer, self).big_cqe())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def res(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.res(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).res(__int.valueOf(arg0)))

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__int.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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
    def big_cqe(self, arg0: 'LongBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.big_cqe(java.nio.LongBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).big_cqe(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBufRing
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingBufRing as __IOURingBufRing
__IOURingBufRing = __IOURingBufRing
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import org.lwjgl.system.linux.liburing.IOURingBuf as __IOURingBuf_Buffer
__Buffer = __IOURingBuf_Buffer.Buffer
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import org.lwjgl.system.linux.liburing.IOURingBufRing as __IOURingBufRing_Buffer
__Buffer = __IOURingBufRing_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import org.lwjgl.system.linux.liburing.IOURingBuf as __IOURingBuf
__IOURingBuf = __IOURingBuf
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingBufRing():
    """org.lwjgl.system.linux.liburing.IOURingBufRing"""
 
    @staticmethod
    def __wrap(java_value: __IOURingBufRing) -> 'IOURingBufRing':
        return IOURingBufRing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingBufRing):
        """
        Dynamic initializer for IOURingBufRing.
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
    def nbufs(arg0: int, arg1: 'Buffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.nbufs(long,org.lwjgl.system.linux.liburing.IOURingBuf$Buffer)"""
        __IOURingBufRing.nbufs(__long.valueOf(arg0), arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nresv1(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.nresv1(long,long)"""
        __IOURingBufRing.nresv1(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def resv1(self, arg0: int) -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.resv1(long)"""
        return 'IOURingBufRing'.__wrap(super(__IOURingBufRing, self).resv1(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv3(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.nresv3(long,short)"""
        __IOURingBufRing.nresv3(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.create(long)"""
        return IOURingBufRing.__wrap(__IOURingBufRing.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.create(int)"""
        return Buffer.__wrap(__IOURingBufRing.create(__int.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nresv1(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingBufRing.nresv1(long)"""
        return int.__wrap(__IOURingBufRing.nresv1(__long.valueOf(arg0)))

    @overload
    def tail(self, arg0: int) -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.tail(short)"""
        return 'IOURingBufRing'.__wrap(super(__IOURingBufRing, self).tail(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.calloc()"""
        return IOURingBufRing.__wrap(__IOURingBufRing.calloc())

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.nresv2(long,int)"""
        __IOURingBufRing.nresv2(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBufRing.__wrap(__IOURingBufRing.calloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.calloc(int)"""
        return Buffer.__wrap(__IOURingBufRing.calloc(__int.valueOf(arg0)))

    @overload
    def resv3(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufRing.resv3()"""
        return int.__wrap(super(IOURingBufRing, self).resv3())

    @staticmethod
    @overload
    def nresv3(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBufRing.nresv3(long)"""
        return int.__wrap(__IOURingBufRing.nresv3(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def ntail(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.ntail(long,short)"""
        __IOURingBufRing.ntail(__long.valueOf(arg0), __short.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nbufs(arg0: int, arg1: int, arg2: 'IOURingBuf'):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.nbufs(long,int,org.lwjgl.system.linux.liburing.IOURingBuf)"""
        __IOURingBufRing.nbufs(__long.valueOf(arg0), __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def ntail(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBufRing.ntail(long)"""
        return int.__wrap(__IOURingBufRing.ntail(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nbufs(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.nbufs(long)"""
        return Buffer.__wrap(__IOURingBufRing.nbufs(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.create(long,int)"""
        return Buffer.__wrap(__IOURingBufRing.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def bufs(self) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.bufs()"""
        return 'Buffer'.__wrap(super(IOURingBufRing, self).bufs())

    @overload
    def bufs(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBufRing.bufs(int)"""
        return 'IOURingBuf'.__wrap(super(__IOURingBufRing, self).bufs(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.malloc()"""
        return IOURingBufRing.__wrap(__IOURingBufRing.malloc())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBufRing.__wrap(__IOURingBufRing.malloc(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nbufs(arg0: int, arg1: int) -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBufRing.nbufs(long,int)"""
        return IOURingBuf.__wrap(__IOURingBufRing.nbufs(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def bufs(self, arg0: 'Buffer') -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.bufs(org.lwjgl.system.linux.liburing.IOURingBuf$Buffer)"""
        return 'IOURingBufRing'.__wrap(super(__IOURingBufRing, self).bufs(arg0))

    @overload
    def set(self, arg0: 'IOURingBufRing') -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.set(org.lwjgl.system.linux.liburing.IOURingBufRing)"""
        return 'IOURingBufRing'.__wrap(super(__IOURingBufRing, self).set(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingBufRing.nresv2(long)"""
        return int.__wrap(__IOURingBufRing.nresv2(__long.valueOf(arg0)))

    @overload
    def resv1(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufRing.resv1()"""
        return int.__wrap(super(IOURingBufRing, self).resv1())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingBufRing(java.nio.ByteBuffer)"""
        val = __IOURingBufRing(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufRing.resv2()"""
        return int.__wrap(super(IOURingBufRing, self).resv2())

    @overload
    def bufs(self, arg0: int, arg1: 'Consumer') -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.bufs(int,java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingBuf>)"""
        return 'IOURingBufRing'.__wrap(super(__IOURingBufRing, self).bufs(__int.valueOf(arg0), arg1))

    @overload
    def tail(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufRing.tail()"""
        return int.__wrap(super(IOURingBufRing, self).tail())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingBufRing.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufRing.sizeof()"""
        return int.__wrap(super(IOURingBufRing, self).sizeof())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.malloc(int)"""
        return Buffer.__wrap(__IOURingBufRing.malloc(__int.valueOf(arg0)))

    @overload
    def resv2(self, arg0: int) -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.resv2(int)"""
        return 'IOURingBufRing'.__wrap(super(__IOURingBufRing, self).resv2(__int.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def create() -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.create()"""
        return IOURingBufRing.__wrap(__IOURingBufRing.create())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def resv3(self, arg0: int) -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.resv3(short)"""
        return 'IOURingBufRing'.__wrap(super(__IOURingBufRing, self).resv3(__short.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingBufRing.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.createSafe(long)"""
        return IOURingBufRing.__wrap(__IOURingBufRing.createSafe(__long.valueOf(arg0)))

    @overload
    def bufs(self, arg0: 'Consumer') -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.bufs(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingBuf$Buffer>)"""
        return 'IOURingBufRing'.__wrap(super(__IOURingBufRing, self).bufs(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingBufRing.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def bufs(self, arg0: int, arg1: 'IOURingBuf') -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.bufs(int,org.lwjgl.system.linux.liburing.IOURingBuf)"""
        return 'IOURingBufRing'.__wrap(super(__IOURingBufRing, self).bufs(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 as __IOURingRSRCUpdate2_Buffer
__Buffer = __IOURingRSRCUpdate2_Buffer.Buffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def data(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.data(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).data(__long.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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
    def tags(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.tags()"""
        return int.__wrap(super(Buffer, self).tags())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
    def nr(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.nr()"""
        return int.__wrap(super(Buffer, self).nr())

    @overload
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.data()"""
        return int.__wrap(super(Buffer, self).data())

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def resv2(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.resv2(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv2(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def resv(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.resv()"""
        return int.__wrap(super(Buffer, self).resv())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.resv(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv(__int.valueOf(arg0)))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def tags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.tags(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).tags(__long.valueOf(arg0)))

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
    def offset(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.offset(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).offset(__int.valueOf(arg0)))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def offset(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.offset()"""
        return int.__wrap(super(Buffer, self).offset())

    @overload
    def nr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.nr(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).nr(__int.valueOf(arg0)))

    @overload
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.resv2()"""
        return int.__wrap(super(Buffer, self).resv2())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.linux.liburing.IOURingBuf as __IOURingBuf_Buffer
__Buffer = __IOURingBuf_Buffer.Buffer
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Short as __short
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.liburing.IOURingBufRing as __IOURingBufRing_Buffer
__Buffer = __IOURingBufRing_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import org.lwjgl.system.linux.liburing.IOURingBuf as __IOURingBuf
__IOURingBuf = __IOURingBuf
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingBufRing.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def bufs(self, arg0: 'Buffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs(org.lwjgl.system.linux.liburing.IOURingBuf$Buffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).bufs(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def bufs(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs(int)"""
        return 'IOURingBuf'.__wrap(super(__Buffer, self).bufs(__int.valueOf(arg0)))

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def bufs(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingBuf$Buffer>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).bufs(arg0))

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
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def resv1(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv1()"""
        return int.__wrap(super(Buffer, self).resv1())

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def resv3(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv3()"""
        return int.__wrap(super(Buffer, self).resv3())

    @overload
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv2()"""
        return int.__wrap(super(Buffer, self).resv2())

    @overload
    def tail(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.tail(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).tail(__short.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def bufs(self, arg0: int, arg1: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs(int,java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingBuf>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).bufs(__int.valueOf(arg0), arg1))

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
    def tail(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.tail()"""
        return int.__wrap(super(Buffer, self).tail())

    @overload
    def resv2(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv2(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv2(__int.valueOf(arg0)))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def bufs(self) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs()"""
        return 'Buffer'.__wrap(super(Buffer, self).bufs())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @overload
    def resv1(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv1(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv1(__long.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @overload
    def bufs(self, arg0: int, arg1: 'IOURingBuf') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs(int,org.lwjgl.system.linux.liburing.IOURingBuf)"""
        return 'Buffer'.__wrap(super(__Buffer, self).bufs(__int.valueOf(arg0), arg1))

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

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def resv3(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv3(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv3(__short.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRestriction
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.linux.liburing.IOURingRestriction as __IOURingRestriction
__IOURingRestriction = __IOURingRestriction
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingRestriction as __IOURingRestriction_Buffer
__Buffer = __IOURingRestriction_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingRestriction():
    """org.lwjgl.system.linux.liburing.IOURingRestriction"""
 
    @staticmethod
    def __wrap(java_value: __IOURingRestriction) -> 'IOURingRestriction':
        return IOURingRestriction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingRestriction):
        """
        Dynamic initializer for IOURingRestriction.
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
    def createSafe(arg0: int) -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.createSafe(long)"""
        return IOURingRestriction.__wrap(__IOURingRestriction.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingRestriction.nresv2(long)"""
        return IntBuffer.__wrap(__IOURingRestriction.nresv2(__long.valueOf(arg0)))

    @overload
    def sqe_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction.sqe_op()"""
        return int.__wrap(super(IOURingRestriction, self).sqe_op())

    @staticmethod
    @overload
    def malloc() -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.malloc()"""
        return IOURingRestriction.__wrap(__IOURingRestriction.malloc())

    @overload
    def register_op(self, arg0: int) -> 'IOURingRestriction':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.register_op(byte)"""
        return 'IOURingRestriction'.__wrap(super(__IOURingRestriction, self).register_op(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def nopcode(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingRestriction.nopcode(long)"""
        return int.__wrap(__IOURingRestriction.nopcode(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nopcode(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nopcode(long,short)"""
        __IOURingRestriction.nopcode(__long.valueOf(arg0), __short.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.calloc(int)"""
        return Buffer.__wrap(__IOURingRestriction.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.create(long)"""
        return IOURingRestriction.__wrap(__IOURingRestriction.create(__long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingRestriction.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingRestriction.nresv(long)"""
        return int.__wrap(__IOURingRestriction.nresv(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingRestriction') -> 'IOURingRestriction':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.set(org.lwjgl.system.linux.liburing.IOURingRestriction)"""
        return 'IOURingRestriction'.__wrap(super(__IOURingRestriction, self).set(arg0))

    @overload
    def sqe_flags(self, arg0: int) -> 'IOURingRestriction':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.sqe_flags(byte)"""
        return 'IOURingRestriction'.__wrap(super(__IOURingRestriction, self).sqe_flags(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRestriction.__wrap(__IOURingRestriction.calloc(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nresv2(long,java.nio.IntBuffer)"""
        __IOURingRestriction.nresv2(__long.valueOf(arg0), arg1)

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRestriction.nresv2(long,int)"""
        return int.__wrap(__IOURingRestriction.nresv2(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nregister_op(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nregister_op(long,byte)"""
        __IOURingRestriction.nregister_op(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRestriction.__wrap(__IOURingRestriction.malloc(arg0))

    @overload
    def opcode(self, arg0: int) -> 'IOURingRestriction':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.opcode(short)"""
        return 'IOURingRestriction'.__wrap(super(__IOURingRestriction, self).opcode(__short.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def calloc() -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.calloc()"""
        return IOURingRestriction.__wrap(__IOURingRestriction.calloc())

    @overload
    def register_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction.register_op()"""
        return int.__wrap(super(IOURingRestriction, self).register_op())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nsqe_flags(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingRestriction.nsqe_flags(long)"""
        return int.__wrap(__IOURingRestriction.nsqe_flags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nresv2(long,int,int)"""
        __IOURingRestriction.nresv2(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRestriction.sizeof()"""
        return int.__wrap(super(IOURingRestriction, self).sizeof())

    @staticmethod
    @overload
    def nsqe_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nsqe_flags(long,byte)"""
        __IOURingRestriction.nsqe_flags(__long.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRestriction(java.nio.ByteBuffer)"""
        val = __IOURingRestriction(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.create(long,int)"""
        return Buffer.__wrap(__IOURingRestriction.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nresv(long,byte)"""
        __IOURingRestriction.nresv(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingRestriction.calloc(__int.valueOf(arg0), arg1))

    @overload
    def sqe_flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction.sqe_flags()"""
        return int.__wrap(super(IOURingRestriction, self).sqe_flags())

    @staticmethod
    @overload
    def nsqe_op(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingRestriction.nsqe_op(long)"""
        return int.__wrap(__IOURingRestriction.nsqe_op(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.create(int)"""
        return Buffer.__wrap(__IOURingRestriction.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.create()"""
        return IOURingRestriction.__wrap(__IOURingRestriction.create())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def opcode(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingRestriction.opcode()"""
        return int.__wrap(super(IOURingRestriction, self).opcode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nregister_op(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingRestriction.nregister_op(long)"""
        return int.__wrap(__IOURingRestriction.nregister_op(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.malloc(int)"""
        return Buffer.__wrap(__IOURingRestriction.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingRestriction.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nsqe_op(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nsqe_op(long,byte)"""
        __IOURingRestriction.nsqe_op(__long.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def sqe_op(self, arg0: int) -> 'IOURingRestriction':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.sqe_op(byte)"""
        return 'IOURingRestriction'.__wrap(super(__IOURingRestriction, self).sqe_op(__byte.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCRegister
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.linux.liburing.IOURingRSRCRegister as __IOURingRSRCRegister_Buffer
__Buffer = __IOURingRSRCRegister_Buffer.Buffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.linux.liburing.IOURingRSRCRegister as __IOURingRSRCRegister
__IOURingRSRCRegister = __IOURingRSRCRegister
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingRSRCRegister():
    """org.lwjgl.system.linux.liburing.IOURingRSRCRegister"""
 
    @staticmethod
    def __wrap(java_value: __IOURingRSRCRegister) -> 'IOURingRSRCRegister':
        return IOURingRSRCRegister(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingRSRCRegister):
        """
        Dynamic initializer for IOURingRSRCRegister.
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
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.flags()"""
        return int.__wrap(super(IOURingRSRCRegister, self).flags())

    @staticmethod
    @overload
    def ntags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ntags(long,long)"""
        __IOURingRSRCRegister.ntags(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingRSRCRegister.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.sizeof()"""
        return int.__wrap(super(IOURingRSRCRegister, self).sizeof())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create(long,int)"""
        return Buffer.__wrap(__IOURingRSRCRegister.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc()"""
        return IOURingRSRCRegister.__wrap(__IOURingRSRCRegister.malloc())

    @staticmethod
    @overload
    def ndata(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ndata(long)"""
        return int.__wrap(__IOURingRSRCRegister.ndata(__long.valueOf(arg0)))

    @overload
    def resv2(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.resv2()"""
        return int.__wrap(super(IOURingRSRCRegister, self).resv2())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc(int)"""
        return Buffer.__wrap(__IOURingRSRCRegister.calloc(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.set(int,int,long,long,long)"""
        return 'IOURingRSRCRegister'.__wrap(super(__IOURingRSRCRegister, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nflags(long)"""
        return int.__wrap(__IOURingRSRCRegister.nflags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nresv2(long,long)"""
        __IOURingRSRCRegister.nresv2(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def tags(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.tags(long)"""
        return 'IOURingRSRCRegister'.__wrap(super(__IOURingRSRCRegister, self).tags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.createSafe(long)"""
        return IOURingRSRCRegister.__wrap(__IOURingRSRCRegister.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc(int)"""
        return Buffer.__wrap(__IOURingRSRCRegister.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nnr(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nnr(long)"""
        return int.__wrap(__IOURingRSRCRegister.nnr(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def data(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.data(long)"""
        return 'IOURingRSRCRegister'.__wrap(super(__IOURingRSRCRegister, self).data(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingRSRCRegister') -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.set(org.lwjgl.system.linux.liburing.IOURingRSRCRegister)"""
        return 'IOURingRSRCRegister'.__wrap(super(__IOURingRSRCRegister, self).set(arg0))

    @overload
    def nr(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nr()"""
        return int.__wrap(super(IOURingRSRCRegister, self).nr())

    @overload
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.data()"""
        return int.__wrap(super(IOURingRSRCRegister, self).data())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def ndata(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ndata(long,long)"""
        __IOURingRSRCRegister.ndata(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def create() -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create()"""
        return IOURingRSRCRegister.__wrap(__IOURingRSRCRegister.create())

    @overload
    def resv2(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.resv2(long)"""
        return 'IOURingRSRCRegister'.__wrap(super(__IOURingRSRCRegister, self).resv2(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister(java.nio.ByteBuffer)"""
        val = __IOURingRSRCRegister(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingRSRCRegister.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nflags(long,int)"""
        __IOURingRSRCRegister.nflags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingRSRCRegister.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCRegister.__wrap(__IOURingRSRCRegister.malloc(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nnr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nnr(long,int)"""
        __IOURingRSRCRegister.nnr(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def ntags(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ntags(long)"""
        return int.__wrap(__IOURingRSRCRegister.ntags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create(int)"""
        return Buffer.__wrap(__IOURingRSRCRegister.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc()"""
        return IOURingRSRCRegister.__wrap(__IOURingRSRCRegister.calloc())

    @overload
    def tags(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.tags()"""
        return int.__wrap(super(IOURingRSRCRegister, self).tags())

    @overload
    def nr(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nr(int)"""
        return 'IOURingRSRCRegister'.__wrap(super(__IOURingRSRCRegister, self).nr(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

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

    @overload
    def flags(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.flags(int)"""
        return 'IOURingRSRCRegister'.__wrap(super(__IOURingRSRCRegister, self).flags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nresv2(long)"""
        return int.__wrap(__IOURingRSRCRegister.nresv2(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCRegister.__wrap(__IOURingRSRCRegister.calloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create(long)"""
        return IOURingRSRCRegister.__wrap(__IOURingRSRCRegister.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSQ
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import org.lwjgl.system.linux.liburing.IOURingSQ as __IOURingSQ_Buffer
__Buffer = __IOURingSQ_Buffer.Buffer
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingSQ as __IOURingSQ
__IOURingSQ = __IOURingSQ
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.liburing.IOURingSQE as __IOURingSQE
__IOURingSQE = __IOURingSQE
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingSQ():
    """org.lwjgl.system.linux.liburing.IOURingSQ"""
 
    @staticmethod
    def __wrap(java_value: __IOURingSQ) -> 'IOURingSQ':
        return IOURingSQ(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingSQ):
        """
        Dynamic initializer for IOURingSQ.
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
    def nkhead(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nkhead(long,java.nio.IntBuffer)"""
        __IOURingSQ.nkhead(__long.valueOf(arg0), arg1)

    @overload
    def ring_entries(self, arg0: int) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.ring_entries(int)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).ring_entries(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nsqe_head(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQ.nsqe_head(long)"""
        return int.__wrap(__IOURingSQ.nsqe_head(__long.valueOf(arg0)))

    @overload
    def ktail(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.ktail(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingSQ, self).ktail(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def npad(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.npad(long)"""
        return IntBuffer.__wrap(__IOURingSQ.npad(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nkring_entries(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nkring_entries(long,java.nio.IntBuffer)"""
        __IOURingSQ.nkring_entries(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def npad(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.npad(long,java.nio.IntBuffer)"""
        __IOURingSQ.npad(__long.valueOf(arg0), arg1)

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ.sizeof()"""
        return int.__wrap(super(IOURingSQ, self).sizeof())

    @staticmethod
    @overload
    def nkhead(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nkhead(long,int)"""
        return IntBuffer.__wrap(__IOURingSQ.nkhead(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def khead(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.khead(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingSQ, self).khead(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.create(long,int)"""
        return Buffer.__wrap(__IOURingSQ.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def narray(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.narray(long,int)"""
        return IntBuffer.__wrap(__IOURingSQ.narray(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nkring_mask(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nkring_mask(long,java.nio.IntBuffer)"""
        __IOURingSQ.nkring_mask(__long.valueOf(arg0), arg1)

    @overload
    def sqe_head(self, arg0: int) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.sqe_head(int)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).sqe_head(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nsqe_head(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nsqe_head(long,int)"""
        __IOURingSQ.nsqe_head(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create() -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.create()"""
        return IOURingSQ.__wrap(__IOURingSQ.create())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.calloc(int)"""
        return Buffer.__wrap(__IOURingSQ.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nkdropped(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nkdropped(long,int)"""
        return IntBuffer.__wrap(__IOURingSQ.nkdropped(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nring_ptr(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nring_ptr(long,java.nio.ByteBuffer)"""
        __IOURingSQ.nring_ptr(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nring_sz(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQ.nring_sz(long)"""
        return int.__wrap(__IOURingSQ.nring_sz(__long.valueOf(arg0)))

    @overload
    def sqe_tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ.sqe_tail()"""
        return int.__wrap(super(IOURingSQ, self).sqe_tail())

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQ.npad(long,int)"""
        return int.__wrap(__IOURingSQ.npad(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def khead(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.khead(java.nio.IntBuffer)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).khead(arg0))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSQ.__wrap(__IOURingSQ.malloc(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.createSafe(long)"""
        return IOURingSQ.__wrap(__IOURingSQ.createSafe(__long.valueOf(arg0)))

    @overload
    def kflags(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.kflags(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingSQ, self).kflags(__int.valueOf(arg0)))

    @overload
    def ring_sz(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQ.ring_sz()"""
        return int.__wrap(super(IOURingSQ, self).ring_sz())

    @staticmethod
    @overload
    def narray(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.narray(long,java.nio.IntBuffer)"""
        __IOURingSQ.narray(__long.valueOf(arg0), arg1)

    @overload
    def kflags(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.kflags(java.nio.IntBuffer)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).kflags(arg0))

    @overload
    def kdropped(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.kdropped(java.nio.IntBuffer)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).kdropped(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def nring_mask(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQ.nring_mask(long)"""
        return int.__wrap(__IOURingSQ.nring_mask(__long.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ.ring_entries()"""
        return int.__wrap(super(IOURingSQ, self).ring_entries())

    @staticmethod
    @overload
    def nring_sz(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nring_sz(long,long)"""
        __IOURingSQ.nring_sz(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def ring_mask(self, arg0: int) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.ring_mask(int)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).ring_mask(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSQ.__wrap(__IOURingSQ.calloc(arg0))

    @staticmethod
    @overload
    def nring_mask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nring_mask(long,int)"""
        __IOURingSQ.nring_mask(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.npad(long,int,int)"""
        __IOURingSQ.npad(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def kring_entries(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.kring_entries(java.nio.IntBuffer)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).kring_entries(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def ktail(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.ktail(java.nio.IntBuffer)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).ktail(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nktail(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nktail(long,java.nio.IntBuffer)"""
        __IOURingSQ.nktail(__long.valueOf(arg0), arg1)

    @overload
    def ring_ptr(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQ.ring_ptr()"""
        return 'ByteBuffer'.__wrap(super(IOURingSQ, self).ring_ptr())

    @overload
    def set(self, arg0: 'IntBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IntBuffer', arg7: 'IOURingSQE', arg8: int, arg9: int, arg10: 'ByteBuffer', arg11: int, arg12: int) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.set(java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.system.linux.liburing.IOURingSQE,int,int,java.nio.ByteBuffer,int,int)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).set(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, __int.valueOf(arg8), __int.valueOf(arg9), arg10, __int.valueOf(arg11), __int.valueOf(arg12)))

    @overload
    def sqe_tail(self, arg0: int) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.sqe_tail(int)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).sqe_tail(__int.valueOf(arg0)))

    @overload
    def array(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.array(java.nio.IntBuffer)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).array(arg0))

    @overload
    def kring_entries(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.kring_entries(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingSQ, self).kring_entries(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nkring_entries(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nkring_entries(long,int)"""
        return IntBuffer.__wrap(__IOURingSQ.nkring_entries(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingSQ.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingSQ.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nktail(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nktail(long,int)"""
        return IntBuffer.__wrap(__IOURingSQ.nktail(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def kdropped(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.kdropped(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingSQ, self).kdropped(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nkring_mask(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nkring_mask(long,int)"""
        return IntBuffer.__wrap(__IOURingSQ.nkring_mask(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nkflags(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nkflags(long,int)"""
        return IntBuffer.__wrap(__IOURingSQ.nkflags(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def set(self, arg0: 'IOURingSQ') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.set(org.lwjgl.system.linux.liburing.IOURingSQ)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).set(arg0))

    @staticmethod
    @overload
    def nsqe_tail(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQ.nsqe_tail(long)"""
        return int.__wrap(__IOURingSQ.nsqe_tail(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsqe_tail(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nsqe_tail(long,int)"""
        __IOURingSQ.nsqe_tail(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSQ(java.nio.ByteBuffer)"""
        val = __IOURingSQ(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ.ring_mask()"""
        return int.__wrap(super(IOURingSQ, self).ring_mask())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.create(int)"""
        return Buffer.__wrap(__IOURingSQ.create(__int.valueOf(arg0)))

    @overload
    def sqes(self, arg0: 'IOURingSQE') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.sqes(org.lwjgl.system.linux.liburing.IOURingSQE)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).sqes(arg0))

    @overload
    def sqe_head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ.sqe_head()"""
        return int.__wrap(super(IOURingSQ, self).sqe_head())

    @staticmethod
    @overload
    def nring_ptr(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nring_ptr(long)"""
        return ByteBuffer.__wrap(__IOURingSQ.nring_ptr(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def kring_mask(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.kring_mask(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingSQ, self).kring_mask(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.calloc()"""
        return IOURingSQ.__wrap(__IOURingSQ.calloc())

    @staticmethod
    @overload
    def nsqes(arg0: int) -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQ.nsqes(long)"""
        return IOURingSQE.__wrap(__IOURingSQ.nsqes(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.malloc(int)"""
        return Buffer.__wrap(__IOURingSQ.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingSQ.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def kring_mask(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.kring_mask(java.nio.IntBuffer)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).kring_mask(arg0))

    @staticmethod
    @overload
    def nsqes(arg0: int, arg1: 'IOURingSQE'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nsqes(long,org.lwjgl.system.linux.liburing.IOURingSQE)"""
        __IOURingSQ.nsqes(__long.valueOf(arg0), arg1)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def array(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.array(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingSQ, self).array(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nring_entries(long,int)"""
        __IOURingSQ.nring_entries(__long.valueOf(arg0), __int.valueOf(arg1))

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
    def malloc() -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.malloc()"""
        return IOURingSQ.__wrap(__IOURingSQ.malloc())

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.create(long)"""
        return IOURingSQ.__wrap(__IOURingSQ.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQ.nring_entries(long)"""
        return int.__wrap(__IOURingSQ.nring_entries(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.validate(long)"""
        __IOURingSQ.validate(__long.valueOf(arg0))

    @overload
    def ring_ptr(self, arg0: 'ByteBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.ring_ptr(java.nio.ByteBuffer)"""
        return 'IOURingSQ'.__wrap(super(__IOURingSQ, self).ring_ptr(arg0))

    @staticmethod
    @overload
    def nkflags(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nkflags(long,java.nio.IntBuffer)"""
        __IOURingSQ.nkflags(__long.valueOf(arg0), arg1)

    @overload
    def sqes(self) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQ.sqes()"""
        return 'IOURingSQE'.__wrap(super(IOURingSQ, self).sqes())

    @staticmethod
    @overload
    def nkdropped(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nkdropped(long,java.nio.IntBuffer)"""
        __IOURingSQ.nkdropped(__long.valueOf(arg0), arg1) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import org.lwjgl.system.linux.liburing.IOURingRSRCRegister as __IOURingRSRCRegister_Buffer
__Buffer = __IOURingRSRCRegister_Buffer.Buffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingRSRCRegister.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def resv2(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.resv2()"""
        return int.__wrap(super(Buffer, self).resv2())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.data()"""
        return int.__wrap(super(Buffer, self).data())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def resv2(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.resv2(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv2(__long.valueOf(arg0)))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def tags(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.tags()"""
        return int.__wrap(super(Buffer, self).tags())

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
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def data(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.data(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).data(__long.valueOf(arg0)))

    @overload
    def tags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.tags(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).tags(__long.valueOf(arg0)))

    @overload
    def nr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.nr(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).nr(__int.valueOf(arg0)))

    @overload
    def nr(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.nr()"""
        return int.__wrap(super(Buffer, self).nr())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

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

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 as __IOURingRSRCUpdate2_Buffer
__Buffer = __IOURingRSRCUpdate2_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 as __IOURingRSRCUpdate2
__IOURingRSRCUpdate2 = __IOURingRSRCUpdate2
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingRSRCUpdate2():
    """org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2"""
 
    @staticmethod
    def __wrap(java_value: __IOURingRSRCUpdate2) -> 'IOURingRSRCUpdate2':
        return IOURingRSRCUpdate2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingRSRCUpdate2):
        """
        Dynamic initializer for IOURingRSRCUpdate2.
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
    def nr(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nr()"""
        return int.__wrap(super(IOURingRSRCUpdate2, self).nr())

    @staticmethod
    @overload
    def ndata(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.ndata(long)"""
        return int.__wrap(__IOURingRSRCUpdate2.ndata(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nresv(long,int)"""
        __IOURingRSRCUpdate2.nresv(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def calloc() -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.calloc()"""
        return IOURingRSRCUpdate2.__wrap(__IOURingRSRCUpdate2.calloc())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.calloc(int)"""
        return Buffer.__wrap(__IOURingRSRCUpdate2.calloc(__int.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def offset(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.offset(int)"""
        return 'IOURingRSRCUpdate2'.__wrap(super(__IOURingRSRCUpdate2, self).offset(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2(java.nio.ByteBuffer)"""
        val = __IOURingRSRCUpdate2(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def offset(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.offset()"""
        return int.__wrap(super(IOURingRSRCUpdate2, self).offset())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def nr(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nr(int)"""
        return 'IOURingRSRCUpdate2'.__wrap(super(__IOURingRSRCUpdate2, self).nr(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.malloc(int)"""
        return Buffer.__wrap(__IOURingRSRCUpdate2.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nnr(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nnr(long)"""
        return int.__wrap(__IOURingRSRCUpdate2.nnr(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntags(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.ntags(long)"""
        return int.__wrap(__IOURingRSRCUpdate2.ntags(__long.valueOf(arg0)))

    @overload
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.data()"""
        return int.__wrap(super(IOURingRSRCUpdate2, self).data())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.create(long)"""
        return IOURingRSRCUpdate2.__wrap(__IOURingRSRCUpdate2.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.createSafe(long)"""
        return IOURingRSRCUpdate2.__wrap(__IOURingRSRCUpdate2.createSafe(__long.valueOf(arg0)))

    @overload
    def tags(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.tags()"""
        return int.__wrap(super(IOURingRSRCUpdate2, self).tags())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def noffset(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.noffset(long)"""
        return int.__wrap(__IOURingRSRCUpdate2.noffset(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingRSRCUpdate2') -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.set(org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2)"""
        return 'IOURingRSRCUpdate2'.__wrap(super(__IOURingRSRCUpdate2, self).set(arg0))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nresv2(long,int)"""
        __IOURingRSRCUpdate2.nresv2(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nresv2(long)"""
        return int.__wrap(__IOURingRSRCUpdate2.nresv2(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.sizeof()"""
        return int.__wrap(super(IOURingRSRCUpdate2, self).sizeof())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.set(int,int,long,long,int,int)"""
        return 'IOURingRSRCUpdate2'.__wrap(super(__IOURingRSRCUpdate2, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def noffset(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.noffset(long,int)"""
        __IOURingRSRCUpdate2.noffset(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def resv(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.resv(int)"""
        return 'IOURingRSRCUpdate2'.__wrap(super(__IOURingRSRCUpdate2, self).resv(__int.valueOf(arg0)))

    @overload
    def resv(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.resv()"""
        return int.__wrap(super(IOURingRSRCUpdate2, self).resv())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.resv2()"""
        return int.__wrap(super(IOURingRSRCUpdate2, self).resv2())

    @overload
    def data(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.data(long)"""
        return 'IOURingRSRCUpdate2'.__wrap(super(__IOURingRSRCUpdate2, self).data(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCUpdate2.__wrap(__IOURingRSRCUpdate2.malloc(arg0))

    @staticmethod
    @overload
    def malloc() -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.malloc()"""
        return IOURingRSRCUpdate2.__wrap(__IOURingRSRCUpdate2.malloc())

    @overload
    def resv2(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.resv2(int)"""
        return 'IOURingRSRCUpdate2'.__wrap(super(__IOURingRSRCUpdate2, self).resv2(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingRSRCUpdate2.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nresv(long)"""
        return int.__wrap(__IOURingRSRCUpdate2.nresv(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.create()"""
        return IOURingRSRCUpdate2.__wrap(__IOURingRSRCUpdate2.create())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.create(long,int)"""
        return Buffer.__wrap(__IOURingRSRCUpdate2.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ntags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.ntags(long,long)"""
        __IOURingRSRCUpdate2.ntags(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def nnr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nnr(long,int)"""
        __IOURingRSRCUpdate2.nnr(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCUpdate2.__wrap(__IOURingRSRCUpdate2.calloc(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingRSRCUpdate2.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingRSRCUpdate2.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def tags(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.tags(long)"""
        return 'IOURingRSRCUpdate2'.__wrap(super(__IOURingRSRCUpdate2, self).tags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.create(int)"""
        return Buffer.__wrap(__IOURingRSRCUpdate2.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def ndata(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.ndata(long,long)"""
        __IOURingRSRCUpdate2.ndata(__long.valueOf(arg0), __long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBuf
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import org.lwjgl.system.linux.liburing.IOURingBuf as __IOURingBuf_Buffer
__Buffer = __IOURingBuf_Buffer.Buffer
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import org.lwjgl.system.linux.liburing.IOURingBuf as __IOURingBuf
__IOURingBuf = __IOURingBuf
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingBuf():
    """org.lwjgl.system.linux.liburing.IOURingBuf"""
 
    @staticmethod
    def __wrap(java_value: __IOURingBuf) -> 'IOURingBuf':
        return IOURingBuf(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingBuf):
        """
        Dynamic initializer for IOURingBuf.
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
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBuf.addr()"""
        return int.__wrap(super(IOURingBuf, self).addr())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.malloc(int)"""
        return Buffer.__wrap(__IOURingBuf.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingBuf.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nbid(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBuf.nbid(long)"""
        return int.__wrap(__IOURingBuf.nbid(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.create(long,int)"""
        return Buffer.__wrap(__IOURingBuf.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nlen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBuf.nlen(long,int)"""
        __IOURingBuf.nlen(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingBuf(java.nio.ByteBuffer)"""
        val = __IOURingBuf(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc() -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.calloc()"""
        return IOURingBuf.__wrap(__IOURingBuf.calloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingBuf.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.create(int)"""
        return Buffer.__wrap(__IOURingBuf.create(__int.valueOf(arg0)))

    @overload
    def addr(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.addr(long)"""
        return 'IOURingBuf'.__wrap(super(__IOURingBuf, self).addr(__long.valueOf(arg0)))

    @overload
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBuf.len()"""
        return int.__wrap(super(IOURingBuf, self).len())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBuf.__wrap(__IOURingBuf.calloc(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBuf.nresv(long)"""
        return int.__wrap(__IOURingBuf.nresv(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBuf.sizeof()"""
        return int.__wrap(super(IOURingBuf, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def set(self, arg0: 'IOURingBuf') -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.set(org.lwjgl.system.linux.liburing.IOURingBuf)"""
        return 'IOURingBuf'.__wrap(super(__IOURingBuf, self).set(arg0))

    @staticmethod
    @overload
    def nbid(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBuf.nbid(long,short)"""
        __IOURingBuf.nbid(__long.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.set(long,int,short,short)"""
        return 'IOURingBuf'.__wrap(super(__IOURingBuf, self).set(__long.valueOf(arg0), __int.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingBuf.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.calloc(int)"""
        return Buffer.__wrap(__IOURingBuf.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nlen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingBuf.nlen(long)"""
        return int.__wrap(__IOURingBuf.nlen(__long.valueOf(arg0)))

    @overload
    def resv(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBuf.resv()"""
        return int.__wrap(super(IOURingBuf, self).resv())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def bid(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.bid(short)"""
        return 'IOURingBuf'.__wrap(super(__IOURingBuf, self).bid(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBuf.__wrap(__IOURingBuf.malloc(arg0))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBuf.nresv(long,short)"""
        __IOURingBuf.nresv(__long.valueOf(arg0), __short.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.create(long)"""
        return IOURingBuf.__wrap(__IOURingBuf.create(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def resv(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.resv(short)"""
        return 'IOURingBuf'.__wrap(super(__IOURingBuf, self).resv(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def naddr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBuf.naddr(long,long)"""
        __IOURingBuf.naddr(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def len(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.len(int)"""
        return 'IOURingBuf'.__wrap(super(__IOURingBuf, self).len(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.create()"""
        return IOURingBuf.__wrap(__IOURingBuf.create())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.createSafe(long)"""
        return IOURingBuf.__wrap(__IOURingBuf.createSafe(__long.valueOf(arg0)))

    @overload
    def bid(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBuf.bid()"""
        return int.__wrap(super(IOURingBuf, self).bid())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def naddr(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingBuf.naddr(long)"""
        return int.__wrap(__IOURingBuf.naddr(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.malloc()"""
        return IOURingBuf.__wrap(__IOURingBuf.malloc()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.LibIOURing
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import org.lwjgl.system.linux.liburing.LibIOURing as __LibIOURing
__LibIOURing = __LibIOURing
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LibIOURing():
    """org.lwjgl.system.linux.liburing.LibIOURing"""
 
    @staticmethod
    def __wrap(java_value: __LibIOURing) -> 'LibIOURing':
        return LibIOURing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LibIOURing):
        """
        Dynamic initializer for LibIOURing.
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
    def io_uring_enter2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibIOURing.io_uring_enter2(int,int,int,int,long,int)"""
        return int.__wrap(__LibIOURing.io_uring_enter2(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def io_uring_setup(arg0: int, arg1: 'IOURingParams') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibIOURing.io_uring_setup(int,org.lwjgl.system.linux.liburing.IOURingParams)"""
        return int.__wrap(__LibIOURing.io_uring_setup(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nio_uring_register(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibIOURing.nio_uring_register(int,int,long,int)"""
        return int.__wrap(__LibIOURing.nio_uring_register(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def io_uring_register(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibIOURing.io_uring_register(int,int,long,int)"""
        return int.__wrap(__LibIOURing.io_uring_register(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

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
    def nio_uring_setup(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibIOURing.nio_uring_setup(int,long)"""
        return int.__wrap(__LibIOURing.nio_uring_setup(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_enter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibIOURing.io_uring_enter(int,int,int,int,long)"""
        return int.__wrap(__LibIOURing.io_uring_enter(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nio_uring_enter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibIOURing.nio_uring_enter(int,int,int,int,long)"""
        return int.__wrap(__LibIOURing.nio_uring_enter(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nio_uring_enter2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibIOURing.nio_uring_enter2(int,int,int,int,long,int)"""
        return int.__wrap(__LibIOURing.nio_uring_enter2(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingProbe$Buffer
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.linux.liburing.IOURingProbeOp as __IOURingProbeOp
__IOURingProbeOp = __IOURingProbeOp
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Short as __short
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import org.lwjgl.system.linux.liburing.IOURingProbe as __IOURingProbe_Buffer
__Buffer = __IOURingProbe_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.liburing.IOURingProbeOp as __IOURingProbeOp_Buffer
__Buffer = __IOURingProbeOp_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingProbe.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def resv(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.resv()"""
        return int.__wrap(super(Buffer, self).resv())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def ops(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops(int)"""
        return 'IOURingProbeOp'.__wrap(super(__Buffer, self).ops(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @overload
    def last_op(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.last_op(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).last_op(__byte.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def ops(self, arg0: int, arg1: 'IOURingProbeOp') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops(int,org.lwjgl.system.linux.liburing.IOURingProbeOp)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ops(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ops(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ops(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def ops(self, arg0: int, arg1: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops(int,java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingProbeOp>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ops(__int.valueOf(arg0), arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

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

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def ops(self) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops()"""
        return 'Buffer'.__wrap(super(Buffer, self).ops())

    @overload
    def ops_len(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops_len()"""
        return int.__wrap(super(Buffer, self).ops_len())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @overload
    def last_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.last_op()"""
        return int.__wrap(super(Buffer, self).last_op())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def ops(self, arg0: 'Buffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops(org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ops(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.resv(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv(__short.valueOf(arg0)))

    @overload
    def ops_len(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops_len(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ops_len(__byte.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCUpdate
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate as __IOURingRSRCUpdate
__IOURingRSRCUpdate = __IOURingRSRCUpdate
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate as __IOURingRSRCUpdate_Buffer
__Buffer = __IOURingRSRCUpdate_Buffer.Buffer
 
class IOURingRSRCUpdate():
    """org.lwjgl.system.linux.liburing.IOURingRSRCUpdate"""
 
    @staticmethod
    def __wrap(java_value: __IOURingRSRCUpdate) -> 'IOURingRSRCUpdate':
        return IOURingRSRCUpdate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingRSRCUpdate):
        """
        Dynamic initializer for IOURingRSRCUpdate.
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
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.sizeof()"""
        return int.__wrap(super(IOURingRSRCUpdate, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.create(int)"""
        return Buffer.__wrap(__IOURingRSRCUpdate.create(__int.valueOf(arg0)))

    @overload
    def resv(self, arg0: int) -> 'IOURingRSRCUpdate':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.resv(int)"""
        return 'IOURingRSRCUpdate'.__wrap(super(__IOURingRSRCUpdate, self).resv(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.malloc()"""
        return IOURingRSRCUpdate.__wrap(__IOURingRSRCUpdate.malloc())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.createSafe(long)"""
        return IOURingRSRCUpdate.__wrap(__IOURingRSRCUpdate.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingRSRCUpdate.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def offset(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.offset()"""
        return int.__wrap(super(IOURingRSRCUpdate, self).offset())

    @overload
    def data(self, arg0: int) -> 'IOURingRSRCUpdate':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.data(long)"""
        return 'IOURingRSRCUpdate'.__wrap(super(__IOURingRSRCUpdate, self).data(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> 'IOURingRSRCUpdate':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.set(int,int,long)"""
        return 'IOURingRSRCUpdate'.__wrap(super(__IOURingRSRCUpdate, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def ndata(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.ndata(long)"""
        return int.__wrap(__IOURingRSRCUpdate.ndata(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate(java.nio.ByteBuffer)"""
        val = __IOURingRSRCUpdate(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCUpdate.__wrap(__IOURingRSRCUpdate.calloc(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.create(long)"""
        return IOURingRSRCUpdate.__wrap(__IOURingRSRCUpdate.create(__long.valueOf(arg0)))

    @overload
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.data()"""
        return int.__wrap(super(IOURingRSRCUpdate, self).data())

    @staticmethod
    @overload
    def calloc() -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.calloc()"""
        return IOURingRSRCUpdate.__wrap(__IOURingRSRCUpdate.calloc())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.calloc(int)"""
        return Buffer.__wrap(__IOURingRSRCUpdate.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.create(long,int)"""
        return Buffer.__wrap(__IOURingRSRCUpdate.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.malloc(int)"""
        return Buffer.__wrap(__IOURingRSRCUpdate.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.nresv(long,int)"""
        __IOURingRSRCUpdate.nresv(__long.valueOf(arg0), __int.valueOf(arg1))

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
    def create() -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.create()"""
        return IOURingRSRCUpdate.__wrap(__IOURingRSRCUpdate.create())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingRSRCUpdate.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingRSRCUpdate.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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

    @overload
    def set(self, arg0: 'IOURingRSRCUpdate') -> 'IOURingRSRCUpdate':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.set(org.lwjgl.system.linux.liburing.IOURingRSRCUpdate)"""
        return 'IOURingRSRCUpdate'.__wrap(super(__IOURingRSRCUpdate, self).set(arg0))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCUpdate.__wrap(__IOURingRSRCUpdate.malloc(arg0))

    @staticmethod
    @overload
    def noffset(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.noffset(long,int)"""
        __IOURingRSRCUpdate.noffset(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def resv(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.resv()"""
        return int.__wrap(super(IOURingRSRCUpdate, self).resv())

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.nresv(long)"""
        return int.__wrap(__IOURingRSRCUpdate.nresv(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def noffset(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.noffset(long)"""
        return int.__wrap(__IOURingRSRCUpdate.noffset(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def offset(self, arg0: int) -> 'IOURingRSRCUpdate':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.offset(int)"""
        return 'IOURingRSRCUpdate'.__wrap(super(__IOURingRSRCUpdate, self).offset(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndata(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.ndata(long,long)"""
        __IOURingRSRCUpdate.ndata(__long.valueOf(arg0), __long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingCQ
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingCQ as __IOURingCQ_Buffer
__Buffer = __IOURingCQ_Buffer.Buffer
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
import org.lwjgl.system.linux.liburing.IOURingCQE as __IOURingCQE
__IOURingCQE = __IOURingCQE
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
import org.lwjgl.system.linux.liburing.IOURingCQ as __IOURingCQ
__IOURingCQ = __IOURingCQ
from builtins import bool
from builtins import int
 
class IOURingCQ():
    """org.lwjgl.system.linux.liburing.IOURingCQ"""
 
    @staticmethod
    def __wrap(java_value: __IOURingCQ) -> 'IOURingCQ':
        return IOURingCQ(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingCQ):
        """
        Dynamic initializer for IOURingCQ.
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
    def koverflow(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.koverflow(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingCQ, self).koverflow(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IntBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IOURingCQE', arg7: 'ByteBuffer', arg8: int, arg9: int) -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.set(java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.system.linux.liburing.IOURingCQE,java.nio.ByteBuffer,int,int)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).set(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, __int.valueOf(arg8), __int.valueOf(arg9)))

    @staticmethod
    @overload
    def nring_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nring_entries(long,int)"""
        __IOURingCQ.nring_entries(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.create(long)"""
        return IOURingCQ.__wrap(__IOURingCQ.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.createSafe(long)"""
        return IOURingCQ.__wrap(__IOURingCQ.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nkflags(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nkflags(long,java.nio.IntBuffer)"""
        __IOURingCQ.nkflags(__long.valueOf(arg0), arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nring_ptr(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nring_ptr(long)"""
        return ByteBuffer.__wrap(__IOURingCQ.nring_ptr(__long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def kring_mask(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.kring_mask(java.nio.IntBuffer)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).kring_mask(arg0))

    @overload
    def kflags(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.kflags(java.nio.IntBuffer)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).kflags(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def koverflow(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.koverflow(java.nio.IntBuffer)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).koverflow(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def ring_sz(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQ.ring_sz()"""
        return int.__wrap(super(IOURingCQ, self).ring_sz())

    @staticmethod
    @overload
    def nkring_entries(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nkring_entries(long,java.nio.IntBuffer)"""
        __IOURingCQ.nkring_entries(__long.valueOf(arg0), arg1)

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQ.ring_entries()"""
        return int.__wrap(super(IOURingCQ, self).ring_entries())

    @overload
    def cqes(self) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQ.cqes()"""
        return 'IOURingCQE'.__wrap(super(IOURingCQ, self).cqes())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.create(int)"""
        return Buffer.__wrap(__IOURingCQ.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingCQ.nring_entries(long)"""
        return int.__wrap(__IOURingCQ.nring_entries(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def set(self, arg0: 'IOURingCQ') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.set(org.lwjgl.system.linux.liburing.IOURingCQ)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).set(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingCQ.malloc(__int.valueOf(arg0), arg1))

    @overload
    def ktail(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.ktail(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingCQ, self).ktail(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.create()"""
        return IOURingCQ.__wrap(__IOURingCQ.create())

    @overload
    def kflags(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.kflags(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingCQ, self).kflags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.validate(long)"""
        __IOURingCQ.validate(__long.valueOf(arg0))

    @overload
    def ktail(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.ktail(java.nio.IntBuffer)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).ktail(arg0))

    @overload
    def kring_mask(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.kring_mask(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingCQ, self).kring_mask(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def khead(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.khead(java.nio.IntBuffer)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).khead(arg0))

    @staticmethod
    @overload
    def nktail(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nktail(long,java.nio.IntBuffer)"""
        __IOURingCQ.nktail(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nkring_mask(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nkring_mask(long,int)"""
        return IntBuffer.__wrap(__IOURingCQ.nkring_mask(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nkoverflow(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nkoverflow(long,java.nio.IntBuffer)"""
        __IOURingCQ.nkoverflow(__long.valueOf(arg0), arg1)

    @overload
    def khead(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.khead(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingCQ, self).khead(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nkoverflow(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nkoverflow(long,int)"""
        return IntBuffer.__wrap(__IOURingCQ.nkoverflow(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.create(long,int)"""
        return Buffer.__wrap(__IOURingCQ.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingCQ.npad(long,int)"""
        return int.__wrap(__IOURingCQ.npad(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.malloc(int)"""
        return Buffer.__wrap(__IOURingCQ.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQ.sizeof()"""
        return int.__wrap(super(IOURingCQ, self).sizeof())

    @staticmethod
    @overload
    def npad(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.npad(long,java.nio.IntBuffer)"""
        __IOURingCQ.npad(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def npad(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.npad(long)"""
        return IntBuffer.__wrap(__IOURingCQ.npad(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nring_sz(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nring_sz(long,long)"""
        __IOURingCQ.nring_sz(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def kring_entries(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.kring_entries(int)"""
        return 'IntBuffer'.__wrap(super(__IOURingCQ, self).kring_entries(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingCQ(java.nio.ByteBuffer)"""
        val = __IOURingCQ(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ring_ptr(self, arg0: 'ByteBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.ring_ptr(java.nio.ByteBuffer)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).ring_ptr(arg0))

    @staticmethod
    @overload
    def malloc() -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.malloc()"""
        return IOURingCQ.__wrap(__IOURingCQ.malloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingCQ.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.calloc(int)"""
        return Buffer.__wrap(__IOURingCQ.calloc(__int.valueOf(arg0)))

    @overload
    def ring_ptr(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingCQ.ring_ptr()"""
        return 'ByteBuffer'.__wrap(super(IOURingCQ, self).ring_ptr())

    @staticmethod
    @overload
    def nkhead(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nkhead(long,java.nio.IntBuffer)"""
        __IOURingCQ.nkhead(__long.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nktail(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nktail(long,int)"""
        return IntBuffer.__wrap(__IOURingCQ.nktail(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingCQ.__wrap(__IOURingCQ.calloc(arg0))

    @staticmethod
    @overload
    def ncqes(arg0: int, arg1: 'IOURingCQE'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.ncqes(long,org.lwjgl.system.linux.liburing.IOURingCQE)"""
        __IOURingCQ.ncqes(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def calloc() -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.calloc()"""
        return IOURingCQ.__wrap(__IOURingCQ.calloc())

    @staticmethod
    @overload
    def nkflags(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nkflags(long,int)"""
        return IntBuffer.__wrap(__IOURingCQ.nkflags(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def nring_mask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nring_mask(long,int)"""
        __IOURingCQ.nring_mask(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nring_mask(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingCQ.nring_mask(long)"""
        return int.__wrap(__IOURingCQ.nring_mask(__long.valueOf(arg0)))

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQ.ring_mask()"""
        return int.__wrap(super(IOURingCQ, self).ring_mask())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingCQ.calloc(__int.valueOf(arg0), arg1))

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
    def malloc(arg0: 'MemoryStack') -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingCQ.__wrap(__IOURingCQ.malloc(arg0))

    @staticmethod
    @overload
    def nkring_entries(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nkring_entries(long,int)"""
        return IntBuffer.__wrap(__IOURingCQ.nkring_entries(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ncqes(arg0: int) -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQ.ncqes(long)"""
        return IOURingCQE.__wrap(__IOURingCQ.ncqes(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_sz(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingCQ.nring_sz(long)"""
        return int.__wrap(__IOURingCQ.nring_sz(__long.valueOf(arg0)))

    @overload
    def ring_entries(self, arg0: int) -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.ring_entries(int)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).ring_entries(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nkring_mask(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nkring_mask(long,java.nio.IntBuffer)"""
        __IOURingCQ.nkring_mask(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def cqes(self, arg0: 'IOURingCQE') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.cqes(org.lwjgl.system.linux.liburing.IOURingCQE)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).cqes(arg0))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.npad(long,int,int)"""
        __IOURingCQ.npad(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def kring_entries(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.kring_entries(java.nio.IntBuffer)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).kring_entries(arg0))

    @staticmethod
    @overload
    def nkhead(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nkhead(long,int)"""
        return IntBuffer.__wrap(__IOURingCQ.nkhead(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nring_ptr(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nring_ptr(long,java.nio.ByteBuffer)"""
        __IOURingCQ.nring_ptr(__long.valueOf(arg0), arg1)

    @overload
    def ring_mask(self, arg0: int) -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.ring_mask(int)"""
        return 'IOURingCQ'.__wrap(super(__IOURingCQ, self).ring_mask(__int.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRecvmsgOut
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingRecvmsgOut as __IOURingRecvmsgOut
__IOURingRecvmsgOut = __IOURingRecvmsgOut
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.linux.liburing.IOURingRecvmsgOut as __IOURingRecvmsgOut_Buffer
__Buffer = __IOURingRecvmsgOut_Buffer.Buffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingRecvmsgOut():
    """org.lwjgl.system.linux.liburing.IOURingRecvmsgOut"""
 
    @staticmethod
    def __wrap(java_value: __IOURingRecvmsgOut) -> 'IOURingRecvmsgOut':
        return IOURingRecvmsgOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingRecvmsgOut):
        """
        Dynamic initializer for IOURingRecvmsgOut.
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
    def malloc(arg0: 'MemoryStack') -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRecvmsgOut.__wrap(__IOURingRecvmsgOut.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.create(long,int)"""
        return Buffer.__wrap(__IOURingRecvmsgOut.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.nflags(long,int)"""
        __IOURingRecvmsgOut.nflags(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nnamelen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.nnamelen(long)"""
        return int.__wrap(__IOURingRecvmsgOut.nnamelen(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.set(int,int,int,int)"""
        return 'IOURingRecvmsgOut'.__wrap(super(__IOURingRecvmsgOut, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def payloadlen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.payloadlen()"""
        return int.__wrap(super(IOURingRecvmsgOut, self).payloadlen())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.create(int)"""
        return Buffer.__wrap(__IOURingRecvmsgOut.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nnamelen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.nnamelen(long,int)"""
        __IOURingRecvmsgOut.nnamelen(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.malloc(int)"""
        return Buffer.__wrap(__IOURingRecvmsgOut.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRecvmsgOut.__wrap(__IOURingRecvmsgOut.calloc(arg0))

    @overload
    def namelen(self, arg0: int) -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.namelen(int)"""
        return 'IOURingRecvmsgOut'.__wrap(super(__IOURingRecvmsgOut, self).namelen(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def npayloadlen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.npayloadlen(long,int)"""
        __IOURingRecvmsgOut.npayloadlen(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def ncontrollen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.ncontrollen(long)"""
        return int.__wrap(__IOURingRecvmsgOut.ncontrollen(__long.valueOf(arg0)))

    @overload
    def payloadlen(self, arg0: int) -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.payloadlen(int)"""
        return 'IOURingRecvmsgOut'.__wrap(super(__IOURingRecvmsgOut, self).payloadlen(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingRecvmsgOut') -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.set(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut)"""
        return 'IOURingRecvmsgOut'.__wrap(super(__IOURingRecvmsgOut, self).set(arg0))

    @overload
    def controllen(self, arg0: int) -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.controllen(int)"""
        return 'IOURingRecvmsgOut'.__wrap(super(__IOURingRecvmsgOut, self).controllen(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def namelen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.namelen()"""
        return int.__wrap(super(IOURingRecvmsgOut, self).namelen())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingRecvmsgOut.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def npayloadlen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.npayloadlen(long)"""
        return int.__wrap(__IOURingRecvmsgOut.npayloadlen(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.malloc()"""
        return IOURingRecvmsgOut.__wrap(__IOURingRecvmsgOut.malloc())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.createSafe(long)"""
        return IOURingRecvmsgOut.__wrap(__IOURingRecvmsgOut.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingRecvmsgOut.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.nflags(long)"""
        return int.__wrap(__IOURingRecvmsgOut.nflags(__long.valueOf(arg0)))

    @overload
    def flags(self, arg0: int) -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.flags(int)"""
        return 'IOURingRecvmsgOut'.__wrap(super(__IOURingRecvmsgOut, self).flags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncontrollen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.ncontrollen(long,int)"""
        __IOURingRecvmsgOut.ncontrollen(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc() -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.calloc()"""
        return IOURingRecvmsgOut.__wrap(__IOURingRecvmsgOut.calloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingRecvmsgOut.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.flags()"""
        return int.__wrap(super(IOURingRecvmsgOut, self).flags())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.sizeof()"""
        return int.__wrap(super(IOURingRecvmsgOut, self).sizeof())

    @staticmethod
    @overload
    def create() -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.create()"""
        return IOURingRecvmsgOut.__wrap(__IOURingRecvmsgOut.create())

    @overload
    def controllen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.controllen()"""
        return int.__wrap(super(IOURingRecvmsgOut, self).controllen())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.calloc(int)"""
        return Buffer.__wrap(__IOURingRecvmsgOut.calloc(__int.valueOf(arg0)))

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut(java.nio.ByteBuffer)"""
        val = __IOURingRecvmsgOut(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.create(long)"""
        return IOURingRecvmsgOut.__wrap(__IOURingRecvmsgOut.create(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBuf$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.linux.liburing.IOURingBuf as __IOURingBuf_Buffer
__Buffer = __IOURingBuf_Buffer.Buffer
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Short as __short
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingBuf.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def bid(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.bid(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).bid(__short.valueOf(arg0)))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.resv(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv(__short.valueOf(arg0)))

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
    def bid(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.bid()"""
        return int.__wrap(super(Buffer, self).bid())

    @overload
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.addr()"""
        return int.__wrap(super(Buffer, self).addr())

    @overload
    def len(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.len(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).len(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def addr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.addr(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).addr(__long.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

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

    @overload
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.len()"""
        return int.__wrap(super(Buffer, self).len())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def resv(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.resv()"""
        return int.__wrap(super(Buffer, self).resv())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOSQRingOffsets
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.linux.liburing.IOSQRingOffsets as __IOSQRingOffsets_Buffer
__Buffer = __IOSQRingOffsets_Buffer.Buffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.liburing.IOSQRingOffsets as __IOSQRingOffsets
__IOSQRingOffsets = __IOSQRingOffsets
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOSQRingOffsets():
    """org.lwjgl.system.linux.liburing.IOSQRingOffsets"""
 
    @staticmethod
    def __wrap(java_value: __IOSQRingOffsets) -> 'IOSQRingOffsets':
        return IOSQRingOffsets(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOSQRingOffsets):
        """
        Dynamic initializer for IOSQRingOffsets.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def tail(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.tail(int)"""
        return 'IOSQRingOffsets'.__wrap(super(__IOSQRingOffsets, self).tail(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.create(long)"""
        return IOSQRingOffsets.__wrap(__IOSQRingOffsets.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntail(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.ntail(long)"""
        return int.__wrap(__IOSQRingOffsets.ntail(__long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nring_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.nring_entries(long)"""
        return int.__wrap(__IOSQRingOffsets.nring_entries(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOSQRingOffsets.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.nflags(long)"""
        return int.__wrap(__IOSQRingOffsets.nflags(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.sizeof()"""
        return int.__wrap(super(IOSQRingOffsets, self).sizeof())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.create(long,int)"""
        return Buffer.__wrap(__IOSQRingOffsets.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.malloc(int)"""
        return Buffer.__wrap(__IOSQRingOffsets.malloc(__int.valueOf(arg0)))

    @overload
    def ring_mask(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.ring_mask(int)"""
        return 'IOSQRingOffsets'.__wrap(super(__IOSQRingOffsets, self).ring_mask(__int.valueOf(arg0)))

    @overload
    def head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.head()"""
        return int.__wrap(super(IOSQRingOffsets, self).head())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.malloc(org.lwjgl.system.MemoryStack)"""
        return IOSQRingOffsets.__wrap(__IOSQRingOffsets.malloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.calloc(org.lwjgl.system.MemoryStack)"""
        return IOSQRingOffsets.__wrap(__IOSQRingOffsets.calloc(arg0))

    @overload
    def set(self, arg0: 'IOSQRingOffsets') -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.set(org.lwjgl.system.linux.liburing.IOSQRingOffsets)"""
        return 'IOSQRingOffsets'.__wrap(super(__IOSQRingOffsets, self).set(arg0))

    @staticmethod
    @overload
    def create() -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.create()"""
        return IOSQRingOffsets.__wrap(__IOSQRingOffsets.create())

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nresv2(long,long)"""
        __IOSQRingOffsets.nresv2(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def ndropped(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.ndropped(long,int)"""
        __IOSQRingOffsets.ndropped(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def ring_entries(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.ring_entries(int)"""
        return 'IOSQRingOffsets'.__wrap(super(__IOSQRingOffsets, self).ring_entries(__int.valueOf(arg0)))

    @overload
    def tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.tail()"""
        return int.__wrap(super(IOSQRingOffsets, self).tail())

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nflags(long,int)"""
        __IOSQRingOffsets.nflags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nresv1(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.nresv1(long)"""
        return int.__wrap(__IOSQRingOffsets.nresv1(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nhead(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.nhead(long)"""
        return int.__wrap(__IOSQRingOffsets.nhead(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def array(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.array(int)"""
        return 'IOSQRingOffsets'.__wrap(super(__IOSQRingOffsets, self).array(__int.valueOf(arg0)))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.flags()"""
        return int.__wrap(super(IOSQRingOffsets, self).flags())

    @staticmethod
    @overload
    def nhead(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nhead(long,int)"""
        __IOSQRingOffsets.nhead(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.createSafe(long,int)"""
        return Buffer.__wrap(__IOSQRingOffsets.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.create(int)"""
        return Buffer.__wrap(__IOSQRingOffsets.create(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets(java.nio.ByteBuffer)"""
        val = __IOSQRingOffsets(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def head(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.head(int)"""
        return 'IOSQRingOffsets'.__wrap(super(__IOSQRingOffsets, self).head(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOSQRingOffsets.nresv2(long)"""
        return int.__wrap(__IOSQRingOffsets.nresv2(__long.valueOf(arg0)))

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.ring_entries()"""
        return int.__wrap(super(IOSQRingOffsets, self).ring_entries())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.createSafe(long)"""
        return IOSQRingOffsets.__wrap(__IOSQRingOffsets.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.calloc(int)"""
        return Buffer.__wrap(__IOSQRingOffsets.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nring_mask(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.nring_mask(long)"""
        return int.__wrap(__IOSQRingOffsets.nring_mask(__long.valueOf(arg0)))

    @overload
    def dropped(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.dropped()"""
        return int.__wrap(super(IOSQRingOffsets, self).dropped())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOSQRingOffsets.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nresv1(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nresv1(long,int)"""
        __IOSQRingOffsets.nresv1(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nring_mask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nring_mask(long,int)"""
        __IOSQRingOffsets.nring_mask(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def flags(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.flags(int)"""
        return 'IOSQRingOffsets'.__wrap(super(__IOSQRingOffsets, self).flags(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.set(int,int,int,int,int,int,int)"""
        return 'IOSQRingOffsets'.__wrap(super(__IOSQRingOffsets, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

    @staticmethod
    @overload
    def narray(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.narray(long)"""
        return int.__wrap(__IOSQRingOffsets.narray(__long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def calloc() -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.calloc()"""
        return IOSQRingOffsets.__wrap(__IOSQRingOffsets.calloc())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def narray(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.narray(long,int)"""
        __IOSQRingOffsets.narray(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def ndropped(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.ndropped(long)"""
        return int.__wrap(__IOSQRingOffsets.ndropped(__long.valueOf(arg0)))

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.ring_mask()"""
        return int.__wrap(super(IOSQRingOffsets, self).ring_mask())

    @staticmethod
    @overload
    def nring_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nring_entries(long,int)"""
        __IOSQRingOffsets.nring_entries(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def array(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.array()"""
        return int.__wrap(super(IOSQRingOffsets, self).array())

    @overload
    def dropped(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.dropped(int)"""
        return 'IOSQRingOffsets'.__wrap(super(__IOSQRingOffsets, self).dropped(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ntail(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.ntail(long,int)"""
        __IOSQRingOffsets.ntail(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def malloc() -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.malloc()"""
        return IOSQRingOffsets.__wrap(__IOSQRingOffsets.malloc()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOCQRingOffsets
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOCQRingOffsets as __IOCQRingOffsets_Buffer
__Buffer = __IOCQRingOffsets_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.linux.liburing.IOCQRingOffsets as __IOCQRingOffsets
__IOCQRingOffsets = __IOCQRingOffsets
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOCQRingOffsets():
    """org.lwjgl.system.linux.liburing.IOCQRingOffsets"""
 
    @staticmethod
    def __wrap(java_value: __IOCQRingOffsets) -> 'IOCQRingOffsets':
        return IOCQRingOffsets(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOCQRingOffsets):
        """
        Dynamic initializer for IOCQRingOffsets.
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
    def set(self, arg0: 'IOCQRingOffsets') -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.set(org.lwjgl.system.linux.liburing.IOCQRingOffsets)"""
        return 'IOCQRingOffsets'.__wrap(super(__IOCQRingOffsets, self).set(arg0))

    @staticmethod
    @overload
    def ntail(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.ntail(long,int)"""
        __IOCQRingOffsets.ntail(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def tail(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.tail(int)"""
        return 'IOCQRingOffsets'.__wrap(super(__IOCQRingOffsets, self).tail(__int.valueOf(arg0)))

    @overload
    def cqes(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.cqes()"""
        return int.__wrap(super(IOCQRingOffsets, self).cqes())

    @overload
    def tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.tail()"""
        return int.__wrap(super(IOCQRingOffsets, self).tail())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def flags(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.flags(int)"""
        return 'IOCQRingOffsets'.__wrap(super(__IOCQRingOffsets, self).flags(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets(java.nio.ByteBuffer)"""
        val = __IOCQRingOffsets(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.ring_mask()"""
        return int.__wrap(super(IOCQRingOffsets, self).ring_mask())

    @staticmethod
    @overload
    def nresv1(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nresv1(long,int)"""
        __IOCQRingOffsets.nresv1(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def ntail(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.ntail(long)"""
        return int.__wrap(__IOCQRingOffsets.ntail(__long.valueOf(arg0)))

    @overload
    def head(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.head(int)"""
        return 'IOCQRingOffsets'.__wrap(super(__IOCQRingOffsets, self).head(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv1(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.nresv1(long)"""
        return int.__wrap(__IOCQRingOffsets.nresv1(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.flags()"""
        return int.__wrap(super(IOCQRingOffsets, self).flags())

    @staticmethod
    @overload
    def malloc() -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.malloc()"""
        return IOCQRingOffsets.__wrap(__IOCQRingOffsets.malloc())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nring_mask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nring_mask(long,int)"""
        __IOCQRingOffsets.nring_mask(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.create(long)"""
        return IOCQRingOffsets.__wrap(__IOCQRingOffsets.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.create(long,int)"""
        return Buffer.__wrap(__IOCQRingOffsets.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc() -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.calloc()"""
        return IOCQRingOffsets.__wrap(__IOCQRingOffsets.calloc())

    @staticmethod
    @overload
    def nring_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nring_entries(long,int)"""
        __IOCQRingOffsets.nring_entries(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.malloc(int)"""
        return Buffer.__wrap(__IOCQRingOffsets.malloc(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.set(int,int,int,int,int,int,int)"""
        return 'IOCQRingOffsets'.__wrap(super(__IOCQRingOffsets, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.sizeof()"""
        return int.__wrap(super(IOCQRingOffsets, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def cqes(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.cqes(int)"""
        return 'IOCQRingOffsets'.__wrap(super(__IOCQRingOffsets, self).cqes(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nresv2(long,long)"""
        __IOCQRingOffsets.nresv2(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def ring_entries(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.ring_entries(int)"""
        return 'IOCQRingOffsets'.__wrap(super(__IOCQRingOffsets, self).ring_entries(__int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.create(int)"""
        return Buffer.__wrap(__IOCQRingOffsets.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def noverflow(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.noverflow(long,int)"""
        __IOCQRingOffsets.noverflow(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nring_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.nring_entries(long)"""
        return int.__wrap(__IOCQRingOffsets.nring_entries(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncqes(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.ncqes(long)"""
        return int.__wrap(__IOCQRingOffsets.ncqes(__long.valueOf(arg0)))

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.ring_entries()"""
        return int.__wrap(super(IOCQRingOffsets, self).ring_entries())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.createSafe(long)"""
        return IOCQRingOffsets.__wrap(__IOCQRingOffsets.createSafe(__long.valueOf(arg0)))

    @overload
    def head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.head()"""
        return int.__wrap(super(IOCQRingOffsets, self).head())

    @overload
    def overflow(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.overflow()"""
        return int.__wrap(super(IOCQRingOffsets, self).overflow())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.malloc(org.lwjgl.system.MemoryStack)"""
        return IOCQRingOffsets.__wrap(__IOCQRingOffsets.malloc(arg0))

    @staticmethod
    @overload
    def nring_mask(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.nring_mask(long)"""
        return int.__wrap(__IOCQRingOffsets.nring_mask(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.nflags(long)"""
        return int.__wrap(__IOCQRingOffsets.nflags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOCQRingOffsets.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nflags(long,int)"""
        __IOCQRingOffsets.nflags(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def ring_mask(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.ring_mask(int)"""
        return 'IOCQRingOffsets'.__wrap(super(__IOCQRingOffsets, self).ring_mask(__int.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def create() -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.create()"""
        return IOCQRingOffsets.__wrap(__IOCQRingOffsets.create())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.calloc(org.lwjgl.system.MemoryStack)"""
        return IOCQRingOffsets.__wrap(__IOCQRingOffsets.calloc(arg0))

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
    def ncqes(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.ncqes(long,int)"""
        __IOCQRingOffsets.ncqes(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nhead(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nhead(long,int)"""
        __IOCQRingOffsets.nhead(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nhead(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.nhead(long)"""
        return int.__wrap(__IOCQRingOffsets.nhead(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOCQRingOffsets.nresv2(long)"""
        return int.__wrap(__IOCQRingOffsets.nresv2(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def noverflow(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.noverflow(long)"""
        return int.__wrap(__IOCQRingOffsets.noverflow(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.createSafe(long,int)"""
        return Buffer.__wrap(__IOCQRingOffsets.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def overflow(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.overflow(int)"""
        return 'IOCQRingOffsets'.__wrap(super(__IOCQRingOffsets, self).overflow(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOCQRingOffsets.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.calloc(int)"""
        return Buffer.__wrap(__IOCQRingOffsets.calloc(__int.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSQE$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.linux.liburing.IOURingSQE as __IOURingSQE_Buffer
__Buffer = __IOURingSQE_Buffer.Buffer
import java.nio.ShortBuffer as ShortBuffer
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Short as __short
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingSQE.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def addr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).addr(__long.valueOf(arg0)))

    @overload
    def timeout_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.timeout_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).timeout_flags(__int.valueOf(arg0)))

    @overload
    def msg_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.msg_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).msg_flags(__int.valueOf(arg0)))

    @overload
    def unlink_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.unlink_flags()"""
        return int.__wrap(super(Buffer, self).unlink_flags())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def fadvise_advice(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fadvise_advice()"""
        return int.__wrap(super(Buffer, self).fadvise_advice())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __pad3(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad3(int,short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).__pad3(__int.valueOf(arg0), __short.valueOf(arg1)))

    @overload
    def user_data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.user_data()"""
        return int.__wrap(super(Buffer, self).user_data())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def personality(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.personality(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).personality(__short.valueOf(arg0)))

    @overload
    def addr_len(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr_len(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).addr_len(__short.valueOf(arg0)))

    @overload
    def user_data(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.user_data(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).user_data(__long.valueOf(arg0)))

    @overload
    def ioprio(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.ioprio(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ioprio(__short.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def cmd(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).cmd())

    @overload
    def hardlink_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.hardlink_flags()"""
        return int.__wrap(super(Buffer, self).hardlink_flags())

    @overload
    def xattr_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.xattr_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).xattr_flags(__int.valueOf(arg0)))

    @overload
    def accept_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.accept_flags()"""
        return int.__wrap(super(Buffer, self).accept_flags())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def rw_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.rw_flags()"""
        return int.__wrap(super(Buffer, self).rw_flags())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def accept_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.accept_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).accept_flags(__int.valueOf(arg0)))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def xattr_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.xattr_flags()"""
        return int.__wrap(super(Buffer, self).xattr_flags())

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def __pad2(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad2(int)"""
        return int.__wrap(super(__Buffer, self).__pad2(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr()"""
        return int.__wrap(super(Buffer, self).addr())

    @overload
    def poll32_events(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.poll32_events()"""
        return int.__wrap(super(Buffer, self).poll32_events())

    @overload
    def timeout_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.timeout_flags()"""
        return int.__wrap(super(Buffer, self).timeout_flags())

    @overload
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.len()"""
        return int.__wrap(super(Buffer, self).len())

    @overload
    def splice_off_in(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_off_in()"""
        return int.__wrap(super(Buffer, self).splice_off_in())

    @overload
    def __pad1(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad1()"""
        return int.__wrap(super(Buffer, self).__pad1())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def fadvise_advice(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fadvise_advice(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).fadvise_advice(__int.valueOf(arg0)))

    @overload
    def uring_cmd_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.uring_cmd_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).uring_cmd_flags(__int.valueOf(arg0)))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.flags(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__byte.valueOf(arg0)))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def __pad3(self, arg0: 'ShortBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad3(java.nio.ShortBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).__pad3(arg0))

    @overload
    def __pad2(self, arg0: 'LongBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad2(java.nio.LongBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).__pad2(arg0))

    @overload
    def addr2(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr2()"""
        return int.__wrap(super(Buffer, self).addr2())

    @overload
    def __pad3(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad3()"""
        return 'ShortBuffer'.__wrap(super(Buffer, self).__pad3())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def opcode(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.opcode(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).opcode(__byte.valueOf(arg0)))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def cmd(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cmd(arg0))

    @overload
    def cancel_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cancel_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cancel_flags(__int.valueOf(arg0)))

    @overload
    def buf_index(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.buf_index()"""
        return int.__wrap(super(Buffer, self).buf_index())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addr3(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr3()"""
        return int.__wrap(super(Buffer, self).addr3())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

    @overload
    def personality(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.personality()"""
        return int.__wrap(super(Buffer, self).personality())

    @overload
    def open_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.open_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).open_flags(__int.valueOf(arg0)))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def fd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fd(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).fd(__int.valueOf(arg0)))

    @overload
    def __pad1(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad1(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).__pad1(__int.valueOf(arg0)))

    @overload
    def off(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.off()"""
        return int.__wrap(super(Buffer, self).off())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def open_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.open_flags()"""
        return int.__wrap(super(Buffer, self).open_flags())

    @overload
    def hardlink_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.hardlink_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).hardlink_flags(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def rename_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.rename_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).rename_flags(__int.valueOf(arg0)))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def addr_len(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr_len()"""
        return int.__wrap(super(Buffer, self).addr_len())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @overload
    def msg_ring_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.msg_ring_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).msg_ring_flags(__int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fd()"""
        return int.__wrap(super(Buffer, self).fd())

    @overload
    def msg_ring_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.msg_ring_flags()"""
        return int.__wrap(super(Buffer, self).msg_ring_flags())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def poll32_events(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.poll32_events(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).poll32_events(__int.valueOf(arg0)))

    @overload
    def buf_index(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.buf_index(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).buf_index(__short.valueOf(arg0)))

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
    def sync_range_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.sync_range_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sync_range_flags(__int.valueOf(arg0)))

    @overload
    def rw_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.rw_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).rw_flags(__int.valueOf(arg0)))

    @overload
    def file_index(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.file_index(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).file_index(__int.valueOf(arg0)))

    @overload
    def fsync_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fsync_flags()"""
        return int.__wrap(super(Buffer, self).fsync_flags())

    @overload
    def off(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.off(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).off(__long.valueOf(arg0)))

    @overload
    def splice_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_flags()"""
        return int.__wrap(super(Buffer, self).splice_flags())

    @overload
    def buf_group(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.buf_group(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).buf_group(__short.valueOf(arg0)))

    @overload
    def cmd(self, arg0: int) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd(int)"""
        return int.__wrap(super(__Buffer, self).cmd(__int.valueOf(arg0)))

    @overload
    def ioprio(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.ioprio()"""
        return int.__wrap(super(Buffer, self).ioprio())

    @overload
    def poll_events(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.poll_events()"""
        return int.__wrap(super(Buffer, self).poll_events())

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def splice_fd_in(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_fd_in(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).splice_fd_in(__int.valueOf(arg0)))

    @overload
    def cancel_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cancel_flags()"""
        return int.__wrap(super(Buffer, self).cancel_flags())

    @overload
    def buf_group(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.buf_group()"""
        return int.__wrap(super(Buffer, self).buf_group())

    @overload
    def sync_range_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.sync_range_flags()"""
        return int.__wrap(super(Buffer, self).sync_range_flags())

    @overload
    def cmd(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd(int,byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cmd(__int.valueOf(arg0), __byte.valueOf(arg1)))

    @overload
    def splice_off_in(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_off_in(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).splice_off_in(__long.valueOf(arg0)))

    @overload
    def __pad2(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad2(int,long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).__pad2(__int.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def addr2(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr2(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).addr2(__long.valueOf(arg0)))

    @overload
    def splice_fd_in(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_fd_in()"""
        return int.__wrap(super(Buffer, self).splice_fd_in())

    @overload
    def addr3(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr3(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).addr3(__long.valueOf(arg0)))

    @overload
    def file_index(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.file_index()"""
        return int.__wrap(super(Buffer, self).file_index())

    @overload
    def __pad3(self, arg0: int) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad3(int)"""
        return int.__wrap(super(__Buffer, self).__pad3(__int.valueOf(arg0)))

    @overload
    def opcode(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.opcode()"""
        return int.__wrap(super(Buffer, self).opcode())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def splice_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).splice_flags(__int.valueOf(arg0)))

    @overload
    def cmd_op(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd_op(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cmd_op(__int.valueOf(arg0)))

    @overload
    def statx_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.statx_flags()"""
        return int.__wrap(super(Buffer, self).statx_flags())

    @overload
    def __pad2(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad2()"""
        return 'LongBuffer'.__wrap(super(Buffer, self).__pad2())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def fsync_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fsync_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).fsync_flags(__int.valueOf(arg0)))

    @overload
    def cmd_op(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd_op()"""
        return int.__wrap(super(Buffer, self).cmd_op())

    @overload
    def len(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.len(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).len(__int.valueOf(arg0)))

    @overload
    def rename_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.rename_flags()"""
        return int.__wrap(super(Buffer, self).rename_flags())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def uring_cmd_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.uring_cmd_flags()"""
        return int.__wrap(super(Buffer, self).uring_cmd_flags())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def poll_events(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.poll_events(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).poll_events(__short.valueOf(arg0)))

    @overload
    def statx_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.statx_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).statx_flags(__int.valueOf(arg0)))

    @overload
    def msg_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.msg_flags()"""
        return int.__wrap(super(Buffer, self).msg_flags())

    @overload
    def unlink_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.unlink_flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).unlink_flags(__int.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Short as __short
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import org.lwjgl.system.linux.liburing.IOURingRestriction as __IOURingRestriction_Buffer
__Buffer = __IOURingRestriction_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingRestriction.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def sqe_op(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.sqe_op(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sqe_op(__byte.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def register_op(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.register_op(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).register_op(__byte.valueOf(arg0)))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def opcode(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.opcode(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).opcode(__short.valueOf(arg0)))

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def sqe_flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.sqe_flags()"""
        return int.__wrap(super(Buffer, self).sqe_flags())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def sqe_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.sqe_flags(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sqe_flags(__byte.valueOf(arg0)))

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
    def register_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.register_op()"""
        return int.__wrap(super(Buffer, self).register_op())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def sqe_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.sqe_op()"""
        return int.__wrap(super(Buffer, self).sqe_op())

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
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def opcode(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.opcode()"""
        return int.__wrap(super(Buffer, self).opcode())

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

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

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

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
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.LibURing
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import java.nio.IntBuffer as IntBuffer
from builtins import type
try:
    from pyglsystem import linux
except ImportError:
    linux = __import_once__("pyglsystem.linux")

import org.lwjgl.system.linux.CMsghdr as __CMsghdr
__CMsghdr = __CMsghdr
import java.lang.Class as __Class
__Class = __Class
import java.lang.Short as __short
import org.lwjgl.system.linux.liburing.IOURingSQE as __IOURingSQE
__IOURingSQE = __IOURingSQE
from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import org.lwjgl.system.linux.liburing.LibURing as __LibURing
__LibURing = __LibURing
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

import org.lwjgl.system.linux.liburing.IOURingBufRing as __IOURingBufRing
__IOURingBufRing = __IOURingBufRing
import org.lwjgl.system.linux.liburing.IOURingRecvmsgOut as __IOURingRecvmsgOut
__IOURingRecvmsgOut = __IOURingRecvmsgOut
import java.nio.LongBuffer as LongBuffer
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.linux.liburing.IOURingProbe as __IOURingProbe
__IOURingProbe = __IOURingProbe
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class LibURing():
    """org.lwjgl.system.linux.liburing.LibURing"""
 
    @staticmethod
    def __wrap(java_value: __LibURing) -> 'LibURing':
        return LibURing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LibURing):
        """
        Dynamic initializer for LibURing.
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
    def nio_uring_prep_mkdirat(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_mkdirat(long,int,long,int)"""
        __LibURing.nio_uring_prep_mkdirat(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_unregister_files(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_files(long)"""
        return int.__wrap(__LibURing.nio_uring_unregister_files(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_submit_and_wait_timeout(arg0: 'IOURing', arg1: 'PointerBuffer', arg2: 'KernelTimespec', arg3: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_submit_and_wait_timeout(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer,org.lwjgl.system.linux.KernelTimespec,long)"""
        return int.__wrap(__LibURing.io_uring_submit_and_wait_timeout(arg0, arg1, arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def io_uring_prep_msg_ring_fd(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_msg_ring_fd(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,long,int)"""
        __LibURing.io_uring_prep_msg_ring_fd(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_prep_writev(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_writev(long,int,long,int,int)"""
        __LibURing.nio_uring_prep_writev(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_close(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_close(org.lwjgl.system.linux.liburing.IOURingSQE,int)"""
        __LibURing.io_uring_prep_close(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_prep_renameat(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_renameat(long,int,long,int,long,int)"""
        __LibURing.nio_uring_prep_renameat(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_prep_socket_direct_alloc(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_socket_direct_alloc(long,int,int,int,int)"""
        __LibURing.nio_uring_prep_socket_direct_alloc(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def io_uring_prep_readv2(arg0: 'IOURingSQE', arg1: int, arg2: 'Buffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_readv2(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.IOVec$Buffer,int,int)"""
        __LibURing.io_uring_prep_readv2(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_sync_file_range(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_sync_file_range(long,int,int,int,int)"""
        __LibURing.nio_uring_prep_sync_file_range(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_mlock_size(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.io_uring_mlock_size(int,int)"""
        return int.__wrap(__LibURing.io_uring_mlock_size(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_prep_accept_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'Sockaddr', arg3: 'IntBuffer', arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_accept_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Sockaddr,java.nio.IntBuffer,int,int)"""
        __LibURing.io_uring_prep_accept_direct(arg0, __int.valueOf(arg1), arg2, arg3, __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_unregister_personality(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_personality(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int.__wrap(__LibURing.io_uring_unregister_personality(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_prep_poll_add(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_poll_add(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        __LibURing.io_uring_prep_poll_add(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_linkat(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: 'ByteBuffer', arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_linkat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_linkat(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4, __int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_register_iowq_aff(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_iowq_aff(long,long,long)"""
        return int.__wrap(__LibURing.nio_uring_register_iowq_aff(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_cq_eventfd_toggle(arg0: int, arg1: bool) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_cq_eventfd_toggle(long,boolean)"""
        return int.__wrap(__LibURing.nio_uring_cq_eventfd_toggle(__long.valueOf(arg0), __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_buf_ring_advance(arg0: 'IOURingBufRing', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_buf_ring_advance(org.lwjgl.system.linux.liburing.IOURingBufRing,int)"""
        __LibURing.io_uring_buf_ring_advance(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_prep_rename(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: 'CharSequence'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_rename(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,java.lang.CharSequence)"""
        __LibURing.io_uring_prep_rename(arg0, arg1, arg2)

    @staticmethod
    @overload
    def io_uring_prep_timeout_update(arg0: 'IOURingSQE', arg1: 'KernelTimespec', arg2: int, arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_timeout_update(org.lwjgl.system.linux.liburing.IOURingSQE,org.lwjgl.system.linux.KernelTimespec,long,int)"""
        __LibURing.io_uring_prep_timeout_update(arg0, arg1, __long.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_link_timeout(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_link_timeout(long,long,int)"""
        __LibURing.nio_uring_prep_link_timeout(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_register_buffers(arg0: 'IOURing', arg1: 'Buffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_buffers(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.IOVec$Buffer)"""
        return int.__wrap(__LibURing.io_uring_register_buffers(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_multishot_accept(arg0: 'IOURingSQE', arg1: int, arg2: 'Sockaddr', arg3: 'IntBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_multishot_accept(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Sockaddr,java.nio.IntBuffer,int)"""
        __LibURing.io_uring_prep_multishot_accept(arg0, __int.valueOf(arg1), arg2, arg3, __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_wait_cqe_timeout(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_wait_cqe_timeout(long,long,long)"""
        return int.__wrap(__LibURing.nio_uring_wait_cqe_timeout(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_queue_exit(arg0: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_queue_exit(long)"""
        __LibURing.nio_uring_queue_exit(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nio_uring_register_files_sparse(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_files_sparse(long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_files_sparse(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_unregister_eventfd(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_eventfd(long)"""
        return int.__wrap(__LibURing.nio_uring_unregister_eventfd(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_wait_cqe_nr(arg0: 'IOURing', arg1: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_wait_cqe_nr(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__LibURing.io_uring_wait_cqe_nr(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_recv_multishot(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_recv_multishot(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_recv_multishot(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_provide_buffers(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_provide_buffers(long,long,int,int,int,int)"""
        __LibURing.nio_uring_prep_provide_buffers(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_register_buffers_sparse(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_buffers_sparse(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int.__wrap(__LibURing.io_uring_register_buffers_sparse(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_sqe_set_flags(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_sqe_set_flags(org.lwjgl.system.linux.liburing.IOURingSQE,int)"""
        __LibURing.io_uring_sqe_set_flags(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_prep_link(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: 'CharSequence', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_link(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,java.lang.CharSequence,int)"""
        __LibURing.io_uring_prep_link(arg0, arg1, arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def __io_uring_sqring_wait(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.__io_uring_sqring_wait(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.__io_uring_sqring_wait(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_send_zc_fixed(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_send_zc_fixed(long,int,long,long,int,int,int)"""
        __LibURing.nio_uring_prep_send_zc_fixed(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @staticmethod
    @overload
    def io_uring_prep_sendto(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: 'Sockaddr', arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_sendto(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,org.lwjgl.system.linux.Sockaddr,int)"""
        __LibURing.io_uring_prep_sendto(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4, __int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_prep_msg_ring_fd_alloc(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_msg_ring_fd_alloc(long,int,int,long,int)"""
        __LibURing.nio_uring_prep_msg_ring_fd_alloc(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_get_sqe(arg0: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_get_sqe(long)"""
        return int.__wrap(__LibURing.nio_uring_get_sqe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_buf_ring_cq_advance(arg0: 'IOURing', arg1: 'IOURingBufRing', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_buf_ring_cq_advance(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingBufRing,int)"""
        __LibURing.io_uring_buf_ring_cq_advance(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_mlock_size_params(arg0: int, arg1: 'IOURingParams') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_mlock_size_params(int,org.lwjgl.system.linux.liburing.IOURingParams)"""
        return int.__wrap(__LibURing.io_uring_mlock_size_params(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def io_uring_unregister_ring_fd(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_ring_fd(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_unregister_ring_fd(arg0))

    @staticmethod
    @overload
    def nio_uring_register_files_tags(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_files_tags(long,long,long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_files_tags(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def io_uring_recvmsg_payload_length(arg0: 'IOURingRecvmsgOut', arg1: int, arg2: 'Msghdr') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_payload_length(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut,int,org.lwjgl.system.linux.Msghdr)"""
        return int.__wrap(__LibURing.io_uring_recvmsg_payload_length(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def io_uring_peek_batch_cqe(arg0: 'IOURing', arg1: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_peek_batch_cqe(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__LibURing.io_uring_peek_batch_cqe(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_sqe_set_data(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_sqe_set_data(org.lwjgl.system.linux.liburing.IOURingSQE,long)"""
        __LibURing.io_uring_sqe_set_data(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_wait_cqes(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_wait_cqes(long,long,int,long,long)"""
        return int.__wrap(__LibURing.nio_uring_wait_cqes(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def io_uring_prep_nop(arg0: 'IOURingSQE'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_nop(org.lwjgl.system.linux.liburing.IOURingSQE)"""
        __LibURing.io_uring_prep_nop(arg0)

    @staticmethod
    @overload
    def nio_uring_recvmsg_validate(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_validate(long,int,long)"""
        return int.__wrap(__LibURing.nio_uring_recvmsg_validate(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_get_sqe(arg0: 'IOURing') -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.LibURing.io_uring_get_sqe(org.lwjgl.system.linux.liburing.IOURing)"""
        return IOURingSQE.__wrap(__LibURing.io_uring_get_sqe(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_read(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_read(long,int,long,int,int)"""
        __LibURing.nio_uring_prep_read(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_submit_and_wait(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_submit_and_wait(long,int)"""
        return int.__wrap(__LibURing.nio_uring_submit_and_wait(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_sqe_set_data64(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_sqe_set_data64(long,long)"""
        __LibURing.nio_uring_sqe_set_data64(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_prep_linkat(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int, arg4: 'CharSequence', arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_linkat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int,java.lang.CharSequence,int)"""
        __LibURing.io_uring_prep_linkat(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4, __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_recvmsg_cmsg_firsthdr(arg0: 'IOURingRecvmsgOut', arg1: 'Msghdr') -> 'linux.CMsghdr':
        """public static org.lwjgl.system.linux.CMsghdr org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_cmsg_firsthdr(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut,org.lwjgl.system.linux.Msghdr)"""
        return linux.CMsghdr.__wrap(__LibURing.io_uring_recvmsg_cmsg_firsthdr(arg0, arg1))

    @staticmethod
    @overload
    def n__io_uring_sqring_wait(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.n__io_uring_sqring_wait(long)"""
        return int.__wrap(__LibURing.n__io_uring_sqring_wait(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_unregister_files(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_files(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_unregister_files(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_symlink(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_symlink(long,long,long)"""
        __LibURing.nio_uring_prep_symlink(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_socket_direct_alloc(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_socket_direct_alloc(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,int)"""
        __LibURing.io_uring_prep_socket_direct_alloc(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_register_buf_ring(arg0: 'IOURing', arg1: 'IOURingBufReg', arg2: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_buf_ring(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingBufReg,int)"""
        return int.__wrap(__LibURing.io_uring_register_buf_ring(arg0, arg1, __int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nio_uring_unregister_iowq_aff(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_iowq_aff(long)"""
        return int.__wrap(__LibURing.nio_uring_unregister_iowq_aff(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_unregister_ring_fd(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_ring_fd(long)"""
        return int.__wrap(__LibURing.nio_uring_unregister_ring_fd(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_sync_file_range(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_sync_file_range(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,int)"""
        __LibURing.io_uring_prep_sync_file_range(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_free_buf_ring(arg0: 'IOURing', arg1: 'IOURingBufRing', arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_free_buf_ring(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingBufRing,int,int)"""
        return int.__wrap(__LibURing.io_uring_free_buf_ring(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nio_uring_sq_ready(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_sq_ready(long)"""
        return int.__wrap(__LibURing.nio_uring_sq_ready(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_cq_has_overflow(arg0: int) -> bool:
        """public static native boolean org.lwjgl.system.linux.liburing.LibURing.nio_uring_cq_has_overflow(long)"""
        return bool.__wrap(__LibURing.nio_uring_cq_has_overflow(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_prep_openat_direct(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_openat_direct(long,int,long,int,int,int)"""
        __LibURing.nio_uring_prep_openat_direct(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_splice(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_splice(org.lwjgl.system.linux.liburing.IOURingSQE,int,long,int,long,int,int)"""
        __LibURing.io_uring_prep_splice(arg0, __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @staticmethod
    @overload
    def io_uring_prep_remove_buffers(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_remove_buffers(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        __LibURing.io_uring_prep_remove_buffers(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_register_files_sparse(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_files_sparse(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int.__wrap(__LibURing.io_uring_register_files_sparse(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_epoll_ctl(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_epoll_ctl(long,int,int,int,long)"""
        __LibURing.nio_uring_prep_epoll_ctl(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_openat_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int,int,int)"""
        __LibURing.io_uring_prep_openat_direct(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_prep_openat2_direct(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_openat2_direct(long,int,long,long,int)"""
        __LibURing.nio_uring_prep_openat2_direct(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def io_uring_register_buffers_tags(arg0: 'IOURing', arg1: 'Buffer', arg2: 'LongBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_buffers_tags(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.IOVec$Buffer,java.nio.LongBuffer)"""
        return int.__wrap(__LibURing.io_uring_register_buffers_tags(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nio_uring_prep_timeout_remove(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_timeout_remove(long,long,int)"""
        __LibURing.nio_uring_prep_timeout_remove(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_recvmsg_cmsg_nexthdr(arg0: 'IOURingRecvmsgOut', arg1: 'Msghdr', arg2: 'CMsghdr') -> 'linux.CMsghdr':
        """public static org.lwjgl.system.linux.CMsghdr org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_cmsg_nexthdr(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut,org.lwjgl.system.linux.Msghdr,org.lwjgl.system.linux.CMsghdr)"""
        return linux.CMsghdr.__wrap(__LibURing.io_uring_recvmsg_cmsg_nexthdr(arg0, arg1, arg2))

    @staticmethod
    @overload
    def io_uring_get_probe() -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.LibURing.io_uring_get_probe()"""
        return IOURingProbe.__wrap(__LibURing.io_uring_get_probe())

    @staticmethod
    @overload
    def io_uring_prep_getxattr(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: 'ByteBuffer', arg3: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_getxattr(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        __LibURing.io_uring_prep_getxattr(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def io_uring_sqe_set_data64(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_sqe_set_data64(org.lwjgl.system.linux.liburing.IOURingSQE,long)"""
        __LibURing.io_uring_sqe_set_data64(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_recvmsg_name(arg0: 'IOURingRecvmsgOut') -> int:
        """public static long org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_name(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut)"""
        return int.__wrap(__LibURing.io_uring_recvmsg_name(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_symlinkat(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_symlinkat(long,long,int,long)"""
        __LibURing.nio_uring_prep_symlinkat(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_write(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_write(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_write(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_renameat(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: 'ByteBuffer', arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_renameat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_renameat(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4, __int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_prep_rename(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_rename(long,long,long)"""
        __LibURing.nio_uring_prep_rename(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_read(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_read(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_read(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_files_update(arg0: 'IOURingSQE', arg1: 'IntBuffer', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_files_update(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.IntBuffer,int)"""
        __LibURing.io_uring_prep_files_update(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_recvmsg_payload_length(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_payload_length(long,int,long)"""
        return int.__wrap(__LibURing.nio_uring_recvmsg_payload_length(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_prep_send(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_send(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_send(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_enable_rings(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_enable_rings(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_enable_rings(arg0))

    @staticmethod
    @overload
    def io_uring_setup(arg0: int, arg1: 'IOURingParams') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_setup(int,org.lwjgl.system.linux.liburing.IOURingParams)"""
        return int.__wrap(__LibURing.io_uring_setup(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def io_uring_get_probe_ring(arg0: 'IOURing') -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.LibURing.io_uring_get_probe_ring(org.lwjgl.system.linux.liburing.IOURing)"""
        return IOURingProbe.__wrap(__LibURing.io_uring_get_probe_ring(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def io_uring_register_restrictions(arg0: 'IOURing', arg1: 'Buffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_restrictions(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer)"""
        return int.__wrap(__LibURing.io_uring_register_restrictions(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_connect(arg0: 'IOURingSQE', arg1: int, arg2: 'Sockaddr', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_connect(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Sockaddr,int)"""
        __LibURing.io_uring_prep_connect(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_openat2(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: 'OpenHow'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat2(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,org.lwjgl.system.linux.OpenHow)"""
        __LibURing.io_uring_prep_openat2(arg0, __int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def io_uring_prep_getxattr(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: 'ByteBuffer', arg3: 'CharSequence'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_getxattr(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,java.nio.ByteBuffer,java.lang.CharSequence)"""
        __LibURing.io_uring_prep_getxattr(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def nio_uring_prep_setxattr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_setxattr(long,long,long,long,int,int)"""
        __LibURing.nio_uring_prep_setxattr(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_wait_cqes(arg0: 'IOURing', arg1: 'PointerBuffer', arg2: 'KernelTimespec', arg3: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_wait_cqes(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer,org.lwjgl.system.linux.KernelTimespec,long)"""
        return int.__wrap(__LibURing.io_uring_wait_cqes(arg0, arg1, arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def io_uring_register_files_update_tag(arg0: 'IOURing', arg1: int, arg2: 'IntBuffer', arg3: 'LongBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_files_update_tag(org.lwjgl.system.linux.liburing.IOURing,int,java.nio.IntBuffer,java.nio.LongBuffer)"""
        return int.__wrap(__LibURing.io_uring_register_files_update_tag(arg0, __int.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def nio_uring_prep_write(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_write(long,int,long,int,int)"""
        __LibURing.nio_uring_prep_write(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_unlinkat(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_unlinkat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_unlinkat(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_enter2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_enter2(int,int,int,int,long,long)"""
        return int.__wrap(__LibURing.io_uring_enter2(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def io_uring_prep_epoll_ctl(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: 'EpollEvent'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_epoll_ctl(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,org.lwjgl.system.linux.EpollEvent)"""
        __LibURing.io_uring_prep_epoll_ctl(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)

    @staticmethod
    @overload
    def nio_uring_setup_buf_ring(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_setup_buf_ring(long,int,int,int,long)"""
        return int.__wrap(__LibURing.nio_uring_setup_buf_ring(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nio_uring_prep_cancel_fd(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_cancel_fd(long,int,int)"""
        __LibURing.nio_uring_prep_cancel_fd(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nio_uring_prep_recvmsg_multishot(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_recvmsg_multishot(long,int,long,int)"""
        __LibURing.nio_uring_prep_recvmsg_multishot(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_openat(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int,int)"""
        __LibURing.io_uring_prep_openat(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_openat_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int,int)"""
        __LibURing.io_uring_prep_openat_direct(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_cqe_seen(arg0: 'IOURing', arg1: 'IOURingCQE'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_cqe_seen(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingCQE)"""
        __LibURing.io_uring_cqe_seen(arg0, arg1)

    @staticmethod
    @overload
    def nio_uring_register_buffers_update_tag(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_buffers_update_tag(long,int,long,long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_buffers_update_tag(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def nio_uring_prep_socket_direct(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_socket_direct(long,int,int,int,int,int)"""
        __LibURing.nio_uring_prep_socket_direct(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_statx(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int, arg4: int, arg5: 'Statx'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_statx(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int,int,org.lwjgl.system.linux.Statx)"""
        __LibURing.io_uring_prep_statx(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), arg5)

    @staticmethod
    @overload
    def io_uring_prep_fgetxattr(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fgetxattr(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        __LibURing.io_uring_prep_fgetxattr(arg0, __int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def nio_uring_register_file_alloc_range(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_file_alloc_range(long,int,int)"""
        return int.__wrap(__LibURing.nio_uring_register_file_alloc_range(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_prep_fallocate(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_fallocate(long,int,int,long,long)"""
        __LibURing.nio_uring_prep_fallocate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_fadvise(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_fadvise(long,int,int,long,int)"""
        __LibURing.nio_uring_prep_fadvise(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_recv(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_recv(long,int,long,long,int)"""
        __LibURing.nio_uring_prep_recv(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_cqe_get_data64(arg0: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_cqe_get_data64(long)"""
        return int.__wrap(__LibURing.nio_uring_cqe_get_data64(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_fgetxattr(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fgetxattr(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,java.nio.ByteBuffer)"""
        __LibURing.io_uring_prep_fgetxattr(arg0, __int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def nio_uring_register_iowq_max_workers(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_iowq_max_workers(long,long)"""
        return int.__wrap(__LibURing.nio_uring_register_iowq_max_workers(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_prep_renameat(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int, arg4: 'CharSequence', arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_renameat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int,java.lang.CharSequence,int)"""
        __LibURing.io_uring_prep_renameat(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4, __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_openat2(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: 'OpenHow'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat2(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,org.lwjgl.system.linux.OpenHow)"""
        __LibURing.io_uring_prep_openat2(arg0, __int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def nio_uring_register_eventfd(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_eventfd(long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_eventfd(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_setup_buf_ring(arg0: 'IOURing', arg1: int, arg2: int, arg3: int, arg4: 'IntBuffer') -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.LibURing.io_uring_setup_buf_ring(org.lwjgl.system.linux.liburing.IOURing,int,int,int,java.nio.IntBuffer)"""
        return IOURingBufRing.__wrap(__LibURing.io_uring_setup_buf_ring(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def nio_uring_register_files(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_files(long,long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_files(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_prep_openat2(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_openat2(long,int,long,long)"""
        __LibURing.nio_uring_prep_openat2(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_shutdown(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_shutdown(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        __LibURing.io_uring_prep_shutdown(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_recvmsg_multishot(arg0: 'IOURingSQE', arg1: int, arg2: 'Msghdr', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_recvmsg_multishot(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Msghdr,int)"""
        __LibURing.io_uring_prep_recvmsg_multishot(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_read_fixed(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_read_fixed(long,int,long,int,int,int)"""
        __LibURing.nio_uring_prep_read_fixed(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_fsetxattr(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: 'ByteBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fsetxattr(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_fsetxattr(arg0, __int.valueOf(arg1), arg2, arg3, __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_close_ring_fd(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_close_ring_fd(long)"""
        return int.__wrap(__LibURing.nio_uring_close_ring_fd(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_sqring_wait(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_sqring_wait(long)"""
        return int.__wrap(__LibURing.nio_uring_sqring_wait(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_unregister_iowq_aff(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_iowq_aff(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_unregister_iowq_aff(arg0))

    @staticmethod
    @overload
    def io_uring_get_events(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_get_events(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_get_events(arg0))

    @staticmethod
    @overload
    def io_uring_prep_cancel(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_cancel(org.lwjgl.system.linux.liburing.IOURingSQE,long,int)"""
        __LibURing.io_uring_prep_cancel(arg0, __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_prep_poll_multishot(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_poll_multishot(long,int,int)"""
        __LibURing.nio_uring_prep_poll_multishot(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_register_files_update(arg0: 'IOURing', arg1: int, arg2: 'IntBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_files_update(org.lwjgl.system.linux.liburing.IOURing,int,java.nio.IntBuffer)"""
        return int.__wrap(__LibURing.io_uring_register_files_update(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def io_uring_prep_fsync(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fsync(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        __LibURing.io_uring_prep_fsync(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_prep_close(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_close(long,int)"""
        __LibURing.nio_uring_prep_close(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_prep_recv_multishot(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_recv_multishot(long,int,long,long,int)"""
        __LibURing.nio_uring_prep_recv_multishot(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_get_probe() -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_get_probe()"""
        return int.__wrap(__LibURing.nio_uring_get_probe())

    @staticmethod
    @overload
    def io_uring_prep_mkdir(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_mkdir(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,int)"""
        __LibURing.io_uring_prep_mkdir(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_socket_direct(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_socket_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,int,int)"""
        __LibURing.io_uring_prep_socket_direct(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_unlink(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_unlink(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_unlink(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_register_personality(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_personality(long)"""
        return int.__wrap(__LibURing.nio_uring_register_personality(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_prep_readv2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_readv2(long,int,long,int,int,int)"""
        __LibURing.nio_uring_prep_readv2(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_prep_socket(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_socket(long,int,int,int,int)"""
        __LibURing.nio_uring_prep_socket(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_register_sync_cancel(arg0: 'IOURing', arg1: 'IOURingSyncCancelReg') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_sync_cancel(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingSyncCancelReg)"""
        return int.__wrap(__LibURing.io_uring_register_sync_cancel(arg0, arg1))

    @staticmethod
    @overload
    def nio_uring_prep_fgetxattr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_fgetxattr(long,int,long,long,int)"""
        __LibURing.nio_uring_prep_fgetxattr(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_register_files(arg0: 'IOURing', arg1: 'IntBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_files(org.lwjgl.system.linux.liburing.IOURing,java.nio.IntBuffer)"""
        return int.__wrap(__LibURing.io_uring_register_files(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_openat2_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: 'OpenHow', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat2_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,org.lwjgl.system.linux.OpenHow,int)"""
        __LibURing.io_uring_prep_openat2_direct(arg0, __int.valueOf(arg1), arg2, arg3, __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_buf_ring_advance(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_buf_ring_advance(long,int)"""
        __LibURing.nio_uring_buf_ring_advance(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_opcode_supported(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_opcode_supported(long,int)"""
        return int.__wrap(__LibURing.nio_uring_opcode_supported(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_poll_update(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_poll_update(long,long,long,int,int)"""
        __LibURing.nio_uring_prep_poll_update(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_accept(arg0: 'IOURingSQE', arg1: int, arg2: 'Sockaddr', arg3: 'IntBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_accept(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Sockaddr,java.nio.IntBuffer,int)"""
        __LibURing.io_uring_prep_accept(arg0, __int.valueOf(arg1), arg2, arg3, __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_connect(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_connect(long,int,long,int)"""
        __LibURing.nio_uring_prep_connect(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_msg_ring_cqe_flags(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_msg_ring_cqe_flags(long,int,int,long,int,int)"""
        __LibURing.nio_uring_prep_msg_ring_cqe_flags(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_symlink(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: 'CharSequence'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_symlink(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,java.lang.CharSequence)"""
        __LibURing.io_uring_prep_symlink(arg0, arg1, arg2)

    @staticmethod
    @overload
    def io_uring_prep_sendmsg_zc(arg0: 'IOURingSQE', arg1: int, arg2: 'Msghdr', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_sendmsg_zc(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Msghdr,int)"""
        __LibURing.io_uring_prep_sendmsg_zc(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_rename(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_rename(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        __LibURing.io_uring_prep_rename(arg0, arg1, arg2)

    @staticmethod
    @overload
    def nio_uring_register_files_update_tag(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_files_update_tag(long,int,long,long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_files_update_tag(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def nio_uring_setup(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_setup(int,long)"""
        return int.__wrap(__LibURing.nio_uring_setup(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_cancel64(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_cancel64(long,long,int)"""
        __LibURing.nio_uring_prep_cancel64(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_openat2_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: 'OpenHow', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat2_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,org.lwjgl.system.linux.OpenHow,int)"""
        __LibURing.io_uring_prep_openat2_direct(arg0, __int.valueOf(arg1), arg2, arg3, __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_poll_remove(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_poll_remove(long,long)"""
        __LibURing.nio_uring_prep_poll_remove(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_major_version() -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.io_uring_major_version()"""
        return int.__wrap(__LibURing.io_uring_major_version())

    @staticmethod
    @overload
    def io_uring_cqe_get_data(arg0: 'IOURingCQE') -> int:
        """public static long org.lwjgl.system.linux.liburing.LibURing.io_uring_cqe_get_data(org.lwjgl.system.linux.liburing.IOURingCQE)"""
        return int.__wrap(__LibURing.io_uring_cqe_get_data(arg0))

    @staticmethod
    @overload
    def io_uring_prep_mkdirat(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_mkdirat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_mkdirat(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_unregister_personality(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_personality(long,int)"""
        return int.__wrap(__LibURing.nio_uring_unregister_personality(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_sendmsg(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_sendmsg(long,int,long,int)"""
        __LibURing.nio_uring_prep_sendmsg(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_msg_ring_fd_alloc(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_msg_ring_fd_alloc(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,long,int)"""
        __LibURing.io_uring_prep_msg_ring_fd_alloc(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_statx(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int, arg5: 'Statx'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_statx(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int,org.lwjgl.system.linux.Statx)"""
        __LibURing.io_uring_prep_statx(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), arg5)

    @staticmethod
    @overload
    def io_uring_recvmsg_validate(arg0: 'ByteBuffer', arg1: 'Msghdr') -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_validate(java.nio.ByteBuffer,org.lwjgl.system.linux.Msghdr)"""
        return IOURingRecvmsgOut.__wrap(__LibURing.io_uring_recvmsg_validate(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_provide_buffers(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_provide_buffers(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,int,int,int)"""
        __LibURing.io_uring_prep_provide_buffers(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_setxattr(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: 'ByteBuffer', arg3: 'ByteBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_setxattr(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,java.nio.ByteBuffer,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_setxattr(arg0, arg1, arg2, arg3, __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_socket(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_socket(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,int)"""
        __LibURing.io_uring_prep_socket(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_queue_init(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_queue_init(int,long,int)"""
        return int.__wrap(__LibURing.nio_uring_queue_init(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_register_files_tags(arg0: 'IOURing', arg1: 'IntBuffer', arg2: 'LongBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_files_tags(org.lwjgl.system.linux.liburing.IOURing,java.nio.IntBuffer,java.nio.LongBuffer)"""
        return int.__wrap(__LibURing.io_uring_register_files_tags(arg0, arg1, arg2))

    @staticmethod
    @overload
    def io_uring_sq_ready(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_sq_ready(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_sq_ready(arg0))

    @staticmethod
    @overload
    def io_uring_peek_cqe(arg0: 'IOURing', arg1: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_peek_cqe(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__LibURing.io_uring_peek_cqe(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_msg_ring_cqe_flags(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_msg_ring_cqe_flags(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,long,int,int)"""
        __LibURing.io_uring_prep_msg_ring_cqe_flags(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_submit(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_submit(long)"""
        return int.__wrap(__LibURing.nio_uring_submit(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_send_zc_fixed(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_send_zc_fixed(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int,int)"""
        __LibURing.io_uring_prep_send_zc_fixed(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def nio_uring_free_probe(arg0: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_free_probe(long)"""
        __LibURing.nio_uring_free_probe(__long.valueOf(arg0))

    @staticmethod
    @overload
    def io_uring_prep_writev2(arg0: 'IOURingSQE', arg1: int, arg2: 'Buffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_writev2(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.IOVec$Buffer,int,int)"""
        __LibURing.io_uring_prep_writev2(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_enter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_enter(int,int,int,int,long)"""
        return int.__wrap(__LibURing.nio_uring_enter(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nio_uring_prep_accept_direct(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_accept_direct(long,int,long,long,int,int)"""
        __LibURing.nio_uring_prep_accept_direct(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_register_buffers(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_buffers(long,long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_buffers(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_register_eventfd_async(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_eventfd_async(long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_eventfd_async(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_unlinkat(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_unlinkat(long,int,long,int)"""
        __LibURing.nio_uring_prep_unlinkat(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_register_files_update(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_files_update(long,int,long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_files_update(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nio_uring_prep_accept(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_accept(long,int,long,long,int)"""
        __LibURing.nio_uring_prep_accept(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_cq_eventfd_toggle(arg0: 'IOURing', arg1: bool) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_cq_eventfd_toggle(org.lwjgl.system.linux.liburing.IOURing,boolean)"""
        return int.__wrap(__LibURing.io_uring_cq_eventfd_toggle(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_register_eventfd(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_eventfd(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int.__wrap(__LibURing.io_uring_register_eventfd(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_register_probe(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_probe(long,long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_probe(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_register_iowq_max_workers(arg0: 'IOURing', arg1: 'IntBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_iowq_max_workers(org.lwjgl.system.linux.liburing.IOURing,java.nio.IntBuffer)"""
        return int.__wrap(__LibURing.io_uring_register_iowq_max_workers(arg0, arg1))

    @staticmethod
    @overload
    def nio_uring_prep_fsync(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_fsync(long,int,int)"""
        __LibURing.nio_uring_prep_fsync(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_queue_mmap(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_queue_mmap(int,long,long)"""
        return int.__wrap(__LibURing.nio_uring_queue_mmap(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_prep_recv(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_recv(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_recv(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_mkdir(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_mkdir(long,long,int)"""
        __LibURing.nio_uring_prep_mkdir(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_cq_eventfd_enabled(arg0: int) -> bool:
        """public static native boolean org.lwjgl.system.linux.liburing.LibURing.nio_uring_cq_eventfd_enabled(long)"""
        return bool.__wrap(__LibURing.nio_uring_cq_eventfd_enabled(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_register_buffers_tags(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_buffers_tags(long,long,long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_buffers_tags(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def io_uring_unregister_buf_ring(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_buf_ring(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int.__wrap(__LibURing.io_uring_unregister_buf_ring(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_submit(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_submit(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_submit(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_link(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_link(long,long,long,int)"""
        __LibURing.nio_uring_prep_link(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_prep_sendmsg(arg0: 'IOURingSQE', arg1: int, arg2: 'Msghdr', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_sendmsg(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Msghdr,int)"""
        __LibURing.io_uring_prep_sendmsg(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_setxattr(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: 'ByteBuffer', arg3: 'CharSequence', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_setxattr(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,java.nio.ByteBuffer,java.lang.CharSequence,int)"""
        __LibURing.io_uring_prep_setxattr(arg0, arg1, arg2, arg3, __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_peek_batch_cqe(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_peek_batch_cqe(long,long,int)"""
        return int.__wrap(__LibURing.nio_uring_peek_batch_cqe(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_buf_ring_cq_advance(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_buf_ring_cq_advance(long,long,int)"""
        __LibURing.nio_uring_buf_ring_cq_advance(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_register_restrictions(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_restrictions(long,long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_restrictions(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_prep_msg_ring(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_msg_ring(long,int,int,long,int)"""
        __LibURing.nio_uring_prep_msg_ring(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_sqe_set_data(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_sqe_set_data(long,long)"""
        __LibURing.nio_uring_sqe_set_data(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_prep_fsetxattr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_fsetxattr(long,int,long,long,int,int)"""
        __LibURing.nio_uring_prep_fsetxattr(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_submit_and_get_events(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_submit_and_get_events(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_submit_and_get_events(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_writev2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_writev2(long,int,long,int,int,int)"""
        __LibURing.nio_uring_prep_writev2(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_prep_linkat(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_linkat(long,int,long,int,long,int)"""
        __LibURing.nio_uring_prep_linkat(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_msg_ring(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_msg_ring(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,long,int)"""
        __LibURing.io_uring_prep_msg_ring(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_send_zc(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_send_zc(long,int,long,long,int,int)"""
        __LibURing.nio_uring_prep_send_zc(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_tee(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_tee(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,int)"""
        __LibURing.io_uring_prep_tee(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_recvmsg_name(arg0: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_name(long)"""
        return int.__wrap(__LibURing.nio_uring_recvmsg_name(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_poll_remove(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_poll_remove(org.lwjgl.system.linux.liburing.IOURingSQE,long)"""
        __LibURing.io_uring_prep_poll_remove(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_unregister_buffers(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_buffers(long)"""
        return int.__wrap(__LibURing.nio_uring_unregister_buffers(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_unlink(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_unlink(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,int)"""
        __LibURing.io_uring_prep_unlink(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_cqe_get_data64(arg0: 'IOURingCQE') -> int:
        """public static long org.lwjgl.system.linux.liburing.LibURing.io_uring_cqe_get_data64(org.lwjgl.system.linux.liburing.IOURingCQE)"""
        return int.__wrap(__LibURing.io_uring_cqe_get_data64(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_tee(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_tee(long,int,int,int,int)"""
        __LibURing.nio_uring_prep_tee(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_sendmsg_zc(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_sendmsg_zc(long,int,long,int)"""
        __LibURing.nio_uring_prep_sendmsg_zc(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_read_fixed(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_read_fixed(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int)"""
        __LibURing.io_uring_prep_read_fixed(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_recvmsg(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_recvmsg(long,int,long,int)"""
        __LibURing.nio_uring_prep_recvmsg(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_wait_cqe_nr(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_wait_cqe_nr(long,long,int)"""
        return int.__wrap(__LibURing.nio_uring_wait_cqe_nr(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_wait_cqe(arg0: 'IOURing', arg1: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_wait_cqe(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__LibURing.io_uring_wait_cqe(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_cq_eventfd_enabled(arg0: 'IOURing') -> bool:
        """public static boolean org.lwjgl.system.linux.liburing.LibURing.io_uring_cq_eventfd_enabled(org.lwjgl.system.linux.liburing.IOURing)"""
        return bool.__wrap(__LibURing.io_uring_cq_eventfd_enabled(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_getxattr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_getxattr(long,long,long,long,int)"""
        __LibURing.nio_uring_prep_getxattr(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_enter2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_enter2(int,int,int,int,long,long)"""
        return int.__wrap(__LibURing.nio_uring_enter2(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def nio_uring_register_sync_cancel(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_sync_cancel(long,long)"""
        return int.__wrap(__LibURing.nio_uring_register_sync_cancel(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_wait_cqe_timeout(arg0: 'IOURing', arg1: 'PointerBuffer', arg2: 'KernelTimespec') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_wait_cqe_timeout(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer,org.lwjgl.system.linux.KernelTimespec)"""
        return int.__wrap(__LibURing.io_uring_wait_cqe_timeout(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nio_uring_recvmsg_payload(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_payload(long,long)"""
        return int.__wrap(__LibURing.nio_uring_recvmsg_payload(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_ring_dontfork(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_ring_dontfork(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_ring_dontfork(arg0))

    @staticmethod
    @overload
    def nio_uring_unregister_buf_ring(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_buf_ring(long,int)"""
        return int.__wrap(__LibURing.nio_uring_unregister_buf_ring(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_recvmsg_cmsg_firsthdr(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_cmsg_firsthdr(long,long)"""
        return int.__wrap(__LibURing.nio_uring_recvmsg_cmsg_firsthdr(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_readv(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_readv(long,int,long,int,int)"""
        __LibURing.nio_uring_prep_readv(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_cancel64(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_cancel64(org.lwjgl.system.linux.liburing.IOURingSQE,long,int)"""
        __LibURing.io_uring_prep_cancel64(arg0, __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_queue_init_params(arg0: int, arg1: 'IOURing', arg2: 'IOURingParams') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_queue_init_params(int,org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingParams)"""
        return int.__wrap(__LibURing.io_uring_queue_init_params(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def nio_uring_prep_remove_buffers(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_remove_buffers(long,int,int)"""
        __LibURing.nio_uring_prep_remove_buffers(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_poll_update(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_poll_update(org.lwjgl.system.linux.liburing.IOURingSQE,long,long,int,int)"""
        __LibURing.io_uring_prep_poll_update(arg0, __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_multishot_accept_direct(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_multishot_accept_direct(long,int,long,long,int)"""
        __LibURing.nio_uring_prep_multishot_accept_direct(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_multishot_accept(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_multishot_accept(long,int,long,long,int)"""
        __LibURing.nio_uring_prep_multishot_accept(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_register_ring_fd(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_ring_fd(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_register_ring_fd(arg0))

    @staticmethod
    @overload
    def io_uring_prep_symlinkat(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: int, arg3: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_symlinkat(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,int,java.nio.ByteBuffer)"""
        __LibURing.io_uring_prep_symlinkat(arg0, arg1, __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def io_uring_buf_ring_add(arg0: 'IOURingBufRing', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_buf_ring_add(org.lwjgl.system.linux.liburing.IOURingBufRing,java.nio.ByteBuffer,short,int,int)"""
        __LibURing.io_uring_buf_ring_add(arg0, arg1, __short.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_link(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_link(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_link(arg0, arg1, arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_buf_ring_mask(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_buf_ring_mask(int)"""
        return int.__wrap(__LibURing.io_uring_buf_ring_mask(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_ring_dontfork(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_ring_dontfork(long)"""
        return int.__wrap(__LibURing.nio_uring_ring_dontfork(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_recvmsg(arg0: 'IOURingSQE', arg1: int, arg2: 'Msghdr', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_recvmsg(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Msghdr,int)"""
        __LibURing.io_uring_prep_recvmsg(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_register_file_alloc_range(arg0: 'IOURing', arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_file_alloc_range(org.lwjgl.system.linux.liburing.IOURing,int,int)"""
        return int.__wrap(__LibURing.io_uring_register_file_alloc_range(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_free_buf_ring(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_free_buf_ring(long,long,int,int)"""
        return int.__wrap(__LibURing.nio_uring_free_buf_ring(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nio_uring_prep_files_update(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_files_update(long,long,int,int)"""
        __LibURing.nio_uring_prep_files_update(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_buf_ring_init(arg0: 'IOURingBufRing'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_buf_ring_init(org.lwjgl.system.linux.liburing.IOURingBufRing)"""
        __LibURing.io_uring_buf_ring_init(arg0)

    @staticmethod
    @overload
    def io_uring_prep_unlinkat(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_unlinkat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int)"""
        __LibURing.io_uring_prep_unlinkat(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_send(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_send(long,int,long,long,int)"""
        __LibURing.nio_uring_prep_send(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_cancel_fd(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_cancel_fd(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        __LibURing.io_uring_prep_cancel_fd(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_send_zc(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_send_zc(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int)"""
        __LibURing.io_uring_prep_send_zc(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_register(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.io_uring_register(int,int,long,int)"""
        return int.__wrap(__LibURing.io_uring_register(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def io_uring_unregister_eventfd(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_eventfd(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_unregister_eventfd(arg0))

    @staticmethod
    @overload
    def io_uring_prep_timeout_remove(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_timeout_remove(org.lwjgl.system.linux.liburing.IOURingSQE,long,int)"""
        __LibURing.io_uring_prep_timeout_remove(arg0, __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_cq_ready(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_cq_ready(long)"""
        return int.__wrap(__LibURing.nio_uring_cq_ready(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_register_eventfd_async(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_eventfd_async(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int.__wrap(__LibURing.io_uring_register_eventfd_async(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_register_buf_ring(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_buf_ring(long,long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_buf_ring(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_sqring_wait(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_sqring_wait(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_sqring_wait(arg0))

    @staticmethod
    @overload
    def nio_uring_cqe_seen(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_cqe_seen(long,long)"""
        __LibURing.nio_uring_cqe_seen(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_prep_writev(arg0: 'IOURingSQE', arg1: int, arg2: 'Buffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_writev(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.IOVec$Buffer,int)"""
        __LibURing.io_uring_prep_writev(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_symlinkat(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: int, arg3: 'CharSequence'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_symlinkat(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,int,java.lang.CharSequence)"""
        __LibURing.io_uring_prep_symlinkat(arg0, arg1, __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nio_uring_sq_space_left(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_sq_space_left(long)"""
        return int.__wrap(__LibURing.nio_uring_sq_space_left(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_prep_timeout_update(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_timeout_update(long,long,long,int)"""
        __LibURing.nio_uring_prep_timeout_update(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_msg_ring_fd(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_msg_ring_fd(long,int,int,int,long,int)"""
        __LibURing.nio_uring_prep_msg_ring_fd(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_enter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_enter(int,int,int,int,long)"""
        return int.__wrap(__LibURing.io_uring_enter(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def io_uring_prep_mkdirat(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_mkdirat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int)"""
        __LibURing.io_uring_prep_mkdirat(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_fsetxattr(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: 'ByteBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fsetxattr(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_fsetxattr(arg0, __int.valueOf(arg1), arg2, arg3, __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_cq_ready(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_cq_ready(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_cq_ready(arg0))

    @staticmethod
    @overload
    def nio_uring_get_events(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_get_events(long)"""
        return int.__wrap(__LibURing.nio_uring_get_events(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_readv(arg0: 'IOURingSQE', arg1: int, arg2: 'Buffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_readv(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.IOVec$Buffer,int)"""
        __LibURing.io_uring_prep_readv(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_sendto(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_sendto(long,int,long,long,int,long,int)"""
        __LibURing.nio_uring_prep_sendto(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6))

    @staticmethod
    @overload
    def io_uring_prep_link_timeout(arg0: 'IOURingSQE', arg1: 'KernelTimespec', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_link_timeout(org.lwjgl.system.linux.liburing.IOURingSQE,org.lwjgl.system.linux.KernelTimespec,int)"""
        __LibURing.io_uring_prep_link_timeout(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_wait_cqe(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_wait_cqe(long,long)"""
        return int.__wrap(__LibURing.nio_uring_wait_cqe(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_prep_fadvise(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fadvise(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,long,int)"""
        __LibURing.io_uring_prep_fadvise(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_free_probe(arg0: 'IOURingProbe'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_free_probe(org.lwjgl.system.linux.liburing.IOURingProbe)"""
        __LibURing.io_uring_free_probe(arg0)

    @staticmethod
    @overload
    def nio_uring_prep_nop(arg0: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_nop(long)"""
        __LibURing.nio_uring_prep_nop(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_timeout(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_timeout(long,long,int,int)"""
        __LibURing.nio_uring_prep_timeout(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_sqe_set_flags(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_sqe_set_flags(long,int)"""
        __LibURing.nio_uring_sqe_set_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_register_buffers_update_tag(arg0: 'IOURing', arg1: int, arg2: 'Buffer', arg3: 'LongBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_buffers_update_tag(org.lwjgl.system.linux.liburing.IOURing,int,org.lwjgl.system.linux.IOVec$Buffer,java.nio.LongBuffer)"""
        return int.__wrap(__LibURing.io_uring_register_buffers_update_tag(arg0, __int.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def io_uring_prep_poll_multishot(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_poll_multishot(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        __LibURing.io_uring_prep_poll_multishot(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_queue_init_params(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_queue_init_params(int,long,long)"""
        return int.__wrap(__LibURing.nio_uring_queue_init_params(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_prep_multishot_accept_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'Sockaddr', arg3: 'IntBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_multishot_accept_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Sockaddr,java.nio.IntBuffer,int)"""
        __LibURing.io_uring_prep_multishot_accept_direct(arg0, __int.valueOf(arg1), arg2, arg3, __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_close_direct(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_close_direct(long,int)"""
        __LibURing.nio_uring_prep_close_direct(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_prep_close_direct(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_close_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int)"""
        __LibURing.io_uring_prep_close_direct(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_register_personality(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_personality(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_register_personality(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_unlink(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_unlink(long,long,int)"""
        __LibURing.nio_uring_prep_unlink(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_recvmsg_cmsg_nexthdr(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_cmsg_nexthdr(long,long,long)"""
        return int.__wrap(__LibURing.nio_uring_recvmsg_cmsg_nexthdr(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_prep_symlink(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_symlink(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        __LibURing.io_uring_prep_symlink(arg0, arg1, arg2)

    @staticmethod
    @overload
    def nio_uring_submit_and_get_events(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_submit_and_get_events(long)"""
        return int.__wrap(__LibURing.nio_uring_submit_and_get_events(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_cqe_get_data(arg0: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_cqe_get_data(long)"""
        return int.__wrap(__LibURing.nio_uring_cqe_get_data(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_write_fixed(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_write_fixed(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int)"""
        __LibURing.io_uring_prep_write_fixed(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_shutdown(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_shutdown(long,int,int)"""
        __LibURing.nio_uring_prep_shutdown(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_openat(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int)"""
        __LibURing.io_uring_prep_openat(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_queue_mmap(arg0: int, arg1: 'IOURingParams', arg2: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_queue_mmap(int,org.lwjgl.system.linux.liburing.IOURingParams,org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_queue_mmap(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def io_uring_close_ring_fd(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_close_ring_fd(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_close_ring_fd(arg0))

    @staticmethod
    @overload
    def io_uring_prep_fallocate(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fallocate(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,long,long)"""
        __LibURing.io_uring_prep_fallocate(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_madvise(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_madvise(long,long,long,int)"""
        __LibURing.nio_uring_prep_madvise(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_register_ring_fd(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_ring_fd(long)"""
        return int.__wrap(__LibURing.nio_uring_register_ring_fd(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_prep_poll_add(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_poll_add(long,int,int)"""
        __LibURing.nio_uring_prep_poll_add(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_enable_rings(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_enable_rings(long)"""
        return int.__wrap(__LibURing.nio_uring_enable_rings(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_peek_cqe(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_peek_cqe(long,long)"""
        return int.__wrap(__LibURing.nio_uring_peek_cqe(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_register_probe(arg0: 'IOURing', arg1: 'IOURingProbe', arg2: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_probe(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingProbe,int)"""
        return int.__wrap(__LibURing.io_uring_register_probe(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_register_iowq_aff(arg0: 'IOURing', arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_iowq_aff(org.lwjgl.system.linux.liburing.IOURing,long,long)"""
        return int.__wrap(__LibURing.io_uring_register_iowq_aff(arg0, __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_prep_cancel(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_cancel(long,long,int)"""
        __LibURing.nio_uring_prep_cancel(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_register_buffers_sparse(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_buffers_sparse(long,int)"""
        return int.__wrap(__LibURing.nio_uring_register_buffers_sparse(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_send_set_addr(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_send_set_addr(long,long,short)"""
        __LibURing.nio_uring_prep_send_set_addr(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_mlock_size_params(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_mlock_size_params(int,long)"""
        return int.__wrap(__LibURing.nio_uring_mlock_size_params(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_queue_init(arg0: int, arg1: 'IOURing', arg2: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_queue_init(int,org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int.__wrap(__LibURing.io_uring_queue_init(__int.valueOf(arg0), arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_prep_statx(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_statx(long,int,long,int,int,long)"""
        __LibURing.nio_uring_prep_statx(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_sq_space_left(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_sq_space_left(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_sq_space_left(arg0))

    @staticmethod
    @overload
    def io_uring_opcode_supported(arg0: 'IOURingProbe', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_opcode_supported(org.lwjgl.system.linux.liburing.IOURingProbe,int)"""
        return int.__wrap(__LibURing.io_uring_opcode_supported(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def io_uring_queue_exit(arg0: 'IOURing'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_queue_exit(org.lwjgl.system.linux.liburing.IOURing)"""
        __LibURing.io_uring_queue_exit(arg0)

    @staticmethod
    @overload
    def nio_uring_prep_splice(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_splice(long,int,long,int,long,int,int)"""
        __LibURing.nio_uring_prep_splice(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @staticmethod
    @overload
    def io_uring_submit_and_wait(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_submit_and_wait(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int.__wrap(__LibURing.io_uring_submit_and_wait(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_recvmsg_payload(arg0: 'IOURingRecvmsgOut', arg1: 'Msghdr') -> int:
        """public static long org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_payload(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut,org.lwjgl.system.linux.Msghdr)"""
        return int.__wrap(__LibURing.io_uring_recvmsg_payload(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_send_set_addr(arg0: 'IOURingSQE', arg1: 'Sockaddr', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_send_set_addr(org.lwjgl.system.linux.liburing.IOURingSQE,org.lwjgl.system.linux.Sockaddr,short)"""
        __LibURing.io_uring_prep_send_set_addr(arg0, arg1, __short.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_unregister_buffers(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_buffers(org.lwjgl.system.linux.liburing.IOURing)"""
        return int.__wrap(__LibURing.io_uring_unregister_buffers(arg0))

    @staticmethod
    @overload
    def io_uring_prep_mkdir(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_mkdir(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_mkdir(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_madvise(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_madvise(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,int)"""
        __LibURing.io_uring_prep_madvise(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_prep_openat(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_openat(long,int,long,int,int)"""
        __LibURing.nio_uring_prep_openat(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_write_fixed(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_write_fixed(long,int,long,int,int,int)"""
        __LibURing.nio_uring_prep_write_fixed(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_timeout(arg0: 'IOURingSQE', arg1: 'KernelTimespec', arg2: int, arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_timeout(org.lwjgl.system.linux.liburing.IOURingSQE,org.lwjgl.system.linux.KernelTimespec,int,int)"""
        __LibURing.io_uring_prep_timeout(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_cq_has_overflow(arg0: 'IOURing') -> bool:
        """public static boolean org.lwjgl.system.linux.liburing.LibURing.io_uring_cq_has_overflow(org.lwjgl.system.linux.liburing.IOURing)"""
        return bool.__wrap(__LibURing.io_uring_cq_has_overflow(arg0))

    @staticmethod
    @overload
    def io_uring_check_version(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.linux.liburing.LibURing.io_uring_check_version(int,int)"""
        return bool.__wrap(__LibURing.io_uring_check_version(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_minor_version() -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.io_uring_minor_version()"""
        return int.__wrap(__LibURing.io_uring_minor_version())

    @staticmethod
    @overload
    def nio_uring_get_probe_ring(arg0: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_get_probe_ring(long)"""
        return int.__wrap(__LibURing.nio_uring_get_probe_ring(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_submit_and_wait_timeout(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_submit_and_wait_timeout(long,long,int,long,long)"""
        return int.__wrap(__LibURing.nio_uring_submit_and_wait_timeout(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingParams
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.linux.liburing.IOURingParams as __IOURingParams_Buffer
__Buffer = __IOURingParams_Buffer.Buffer
import org.lwjgl.system.linux.liburing.IOURingParams as __IOURingParams
__IOURingParams = __IOURingParams
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
import org.lwjgl.system.linux.liburing.IOCQRingOffsets as __IOCQRingOffsets
__IOCQRingOffsets = __IOCQRingOffsets
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.liburing.IOSQRingOffsets as __IOSQRingOffsets
__IOSQRingOffsets = __IOSQRingOffsets
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingParams():
    """org.lwjgl.system.linux.liburing.IOURingParams"""
 
    @staticmethod
    def __wrap(java_value: __IOURingParams) -> 'IOURingParams':
        return IOURingParams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingParams):
        """
        Dynamic initializer for IOURingParams.
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
    def malloc(arg0: 'MemoryStack') -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingParams.__wrap(__IOURingParams.malloc(arg0))

    @staticmethod
    @overload
    def nsq_thread_idle(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nsq_thread_idle(long,int)"""
        __IOURingParams.nsq_thread_idle(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'IntBuffer', arg8: 'IOSQRingOffsets', arg9: 'IOCQRingOffsets') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.set(int,int,int,int,int,int,int,java.nio.IntBuffer,org.lwjgl.system.linux.liburing.IOSQRingOffsets,org.lwjgl.system.linux.liburing.IOCQRingOffsets)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7, arg8, arg9))

    @staticmethod
    @overload
    def nsq_off(arg0: int, arg1: 'IOSQRingOffsets'):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nsq_off(long,org.lwjgl.system.linux.liburing.IOSQRingOffsets)"""
        __IOURingParams.nsq_off(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nresv(long,int,int)"""
        __IOURingParams.nresv(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nresv(long,int)"""
        return int.__wrap(__IOURingParams.nresv(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def flags(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.flags(int)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).flags(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def resv(self, arg0: int, arg1: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.resv(int,int)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).resv(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nresv(long,java.nio.IntBuffer)"""
        __IOURingParams.nresv(__long.valueOf(arg0), arg1)

    @overload
    def features(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.features()"""
        return int.__wrap(super(IOURingParams, self).features())

    @overload
    def sq_off(self, arg0: 'Consumer') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.sq_off(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOSQRingOffsets>)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).sq_off(arg0))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nflags(long,int)"""
        __IOURingParams.nflags(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.flags()"""
        return int.__wrap(super(IOURingParams, self).flags())

    @staticmethod
    @overload
    def create() -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.create()"""
        return IOURingParams.__wrap(__IOURingParams.create())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingParams.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nflags(long)"""
        return int.__wrap(__IOURingParams.nflags(__long.valueOf(arg0)))

    @overload
    def cq_off(self, arg0: 'IOCQRingOffsets') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.cq_off(org.lwjgl.system.linux.liburing.IOCQRingOffsets)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).cq_off(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingParams(java.nio.ByteBuffer)"""
        val = __IOURingParams(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.create(long,int)"""
        return Buffer.__wrap(__IOURingParams.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ncq_off(arg0: int, arg1: 'IOCQRingOffsets'):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.ncq_off(long,org.lwjgl.system.linux.liburing.IOCQRingOffsets)"""
        __IOURingParams.ncq_off(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.calloc(int)"""
        return Buffer.__wrap(__IOURingParams.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nfeatures(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nfeatures(long,int)"""
        __IOURingParams.nfeatures(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nsq_thread_cpu(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nsq_thread_cpu(long)"""
        return int.__wrap(__IOURingParams.nsq_thread_cpu(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def calloc() -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.calloc()"""
        return IOURingParams.__wrap(__IOURingParams.calloc())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def sq_entries(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.sq_entries(int)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).sq_entries(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncq_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.ncq_entries(long,int)"""
        __IOURingParams.ncq_entries(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.malloc(int)"""
        return Buffer.__wrap(__IOURingParams.malloc(__int.valueOf(arg0)))

    @overload
    def cq_entries(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.cq_entries(int)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).cq_entries(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.create(long)"""
        return IOURingParams.__wrap(__IOURingParams.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsq_thread_cpu(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nsq_thread_cpu(long,int)"""
        __IOURingParams.nsq_thread_cpu(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nfeatures(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nfeatures(long)"""
        return int.__wrap(__IOURingParams.nfeatures(__long.valueOf(arg0)))

    @overload
    def wq_fd(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.wq_fd(int)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).wq_fd(__int.valueOf(arg0)))

    @overload
    def sq_off(self) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams.sq_off()"""
        return 'IOSQRingOffsets'.__wrap(super(IOURingParams, self).sq_off())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nsq_thread_idle(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nsq_thread_idle(long)"""
        return int.__wrap(__IOURingParams.nsq_thread_idle(__long.valueOf(arg0)))

    @overload
    def sq_thread_idle(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.sq_thread_idle()"""
        return int.__wrap(super(IOURingParams, self).sq_thread_idle())

    @staticmethod
    @overload
    def nsq_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nsq_entries(long,int)"""
        __IOURingParams.nsq_entries(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingParams.__wrap(__IOURingParams.calloc(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.sizeof()"""
        return int.__wrap(super(IOURingParams, self).sizeof())

    @overload
    def features(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.features(int)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).features(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncq_off(arg0: int) -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams.ncq_off(long)"""
        return IOCQRingOffsets.__wrap(__IOURingParams.ncq_off(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.create(int)"""
        return Buffer.__wrap(__IOURingParams.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nwq_fd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nwq_fd(long,int)"""
        __IOURingParams.nwq_fd(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def resv(self, arg0: int) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.resv(int)"""
        return int.__wrap(super(__IOURingParams, self).resv(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nsq_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nsq_entries(long)"""
        return int.__wrap(__IOURingParams.nsq_entries(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncq_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.ncq_entries(long)"""
        return int.__wrap(__IOURingParams.ncq_entries(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingParams.calloc(__int.valueOf(arg0), arg1))

    @overload
    def sq_thread_idle(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.sq_thread_idle(int)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).sq_thread_idle(__int.valueOf(arg0)))

    @overload
    def sq_thread_cpu(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.sq_thread_cpu()"""
        return int.__wrap(super(IOURingParams, self).sq_thread_cpu())

    @staticmethod
    @overload
    def malloc() -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.malloc()"""
        return IOURingParams.__wrap(__IOURingParams.malloc())

    @staticmethod
    @overload
    def nsq_off(arg0: int) -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams.nsq_off(long)"""
        return IOSQRingOffsets.__wrap(__IOURingParams.nsq_off(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingParams.malloc(__int.valueOf(arg0), arg1))

    @overload
    def cq_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.cq_entries()"""
        return int.__wrap(super(IOURingParams, self).cq_entries())

    @overload
    def resv(self, arg0: 'IntBuffer') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.resv(java.nio.IntBuffer)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).resv(arg0))

    @overload
    def cq_off(self) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams.cq_off()"""
        return 'IOCQRingOffsets'.__wrap(super(IOURingParams, self).cq_off())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.createSafe(long)"""
        return IOURingParams.__wrap(__IOURingParams.createSafe(__long.valueOf(arg0)))

    @overload
    def resv(self) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingParams.resv()"""
        return 'IntBuffer'.__wrap(super(IOURingParams, self).resv())

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
    def nresv(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingParams.nresv(long)"""
        return IntBuffer.__wrap(__IOURingParams.nresv(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingParams') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.set(org.lwjgl.system.linux.liburing.IOURingParams)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).set(arg0))

    @overload
    def sq_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.sq_entries()"""
        return int.__wrap(super(IOURingParams, self).sq_entries())

    @overload
    def cq_off(self, arg0: 'Consumer') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.cq_off(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOCQRingOffsets>)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).cq_off(arg0))

    @overload
    def wq_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.wq_fd()"""
        return int.__wrap(super(IOURingParams, self).wq_fd())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def sq_thread_cpu(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.sq_thread_cpu(int)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).sq_thread_cpu(__int.valueOf(arg0)))

    @overload
    def sq_off(self, arg0: 'IOSQRingOffsets') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.sq_off(org.lwjgl.system.linux.liburing.IOSQRingOffsets)"""
        return 'IOURingParams'.__wrap(super(__IOURingParams, self).sq_off(arg0))

    @staticmethod
    @overload
    def nwq_fd(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nwq_fd(long)"""
        return int.__wrap(__IOURingParams.nwq_fd(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingCQ$Buffer
from pyquantum_helper import import_once as __import_once__
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingCQ as __IOURingCQ_Buffer
__Buffer = __IOURingCQ_Buffer.Buffer
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.linux.liburing.IOURingCQE as __IOURingCQE
__IOURingCQE = __IOURingCQE
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingCQ.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def khead(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.khead(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).khead(arg0))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def kflags(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kflags(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).kflags(__int.valueOf(arg0)))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def ktail(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ktail(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ktail(arg0))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def cqes(self, arg0: 'IOURingCQE') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.cqes(org.lwjgl.system.linux.liburing.IOURingCQE)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cqes(arg0))

    @overload
    def kring_mask(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kring_mask(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).kring_mask(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def kring_mask(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kring_mask(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).kring_mask(__int.valueOf(arg0)))

    @overload
    def ring_ptr(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_ptr(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_ptr(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def cqes(self) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.cqes()"""
        return 'IOURingCQE'.__wrap(super(Buffer, self).cqes())

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
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def ring_mask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_mask(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_mask(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def ring_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_entries(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_entries(__int.valueOf(arg0)))

    @overload
    def koverflow(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.koverflow(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).koverflow(arg0))

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_mask()"""
        return int.__wrap(super(Buffer, self).ring_mask())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def kring_entries(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kring_entries(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).kring_entries(__int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

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

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_entries()"""
        return int.__wrap(super(Buffer, self).ring_entries())

    @overload
    def kflags(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kflags(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).kflags(arg0))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def kring_entries(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kring_entries(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).kring_entries(arg0))

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def khead(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.khead(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).khead(__int.valueOf(arg0)))

    @overload
    def ring_ptr(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_ptr()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).ring_ptr())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def koverflow(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.koverflow(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).koverflow(__int.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def ktail(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ktail(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).ktail(__int.valueOf(arg0)))

    @overload
    def ring_sz(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_sz()"""
        return int.__wrap(super(Buffer, self).ring_sz())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import org.lwjgl.system.linux.liburing.IOCQRingOffsets as __IOCQRingOffsets_Buffer
__Buffer = __IOCQRingOffsets_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOCQRingOffsets.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def head(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.head(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).head(__int.valueOf(arg0)))

    @overload
    def tail(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.tail(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).tail(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.tail()"""
        return int.__wrap(super(Buffer, self).tail())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def cqes(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.cqes(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cqes(__int.valueOf(arg0)))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def overflow(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.overflow(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).overflow(__int.valueOf(arg0)))

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
    def ring_mask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.ring_mask(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_mask(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def ring_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.ring_entries(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_entries(__int.valueOf(arg0)))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def cqes(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.cqes()"""
        return int.__wrap(super(Buffer, self).cqes())

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def overflow(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.overflow()"""
        return int.__wrap(super(Buffer, self).overflow())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

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

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__int.valueOf(arg0)))

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
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.head()"""
        return int.__wrap(super(Buffer, self).head())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.ring_entries()"""
        return int.__wrap(super(Buffer, self).ring_entries())

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.ring_mask()"""
        return int.__wrap(super(Buffer, self).ring_mask())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBufReg
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.linux.liburing.IOURingBufReg as __IOURingBufReg
__IOURingBufReg = __IOURingBufReg
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import org.lwjgl.system.linux.liburing.IOURingBufReg as __IOURingBufReg_Buffer
__Buffer = __IOURingBufReg_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingBufReg():
    """org.lwjgl.system.linux.liburing.IOURingBufReg"""
 
    @staticmethod
    def __wrap(java_value: __IOURingBufReg) -> 'IOURingBufReg':
        return IOURingBufReg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingBufReg):
        """
        Dynamic initializer for IOURingBufReg.
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
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufReg.sizeof()"""
        return int.__wrap(super(IOURingBufReg, self).sizeof())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingBufReg(java.nio.ByteBuffer)"""
        val = __IOURingBufReg(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nring_addr(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingBufReg.nring_addr(long)"""
        return int.__wrap(__IOURingBufReg.nring_addr(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingBufReg.nresv(long)"""
        return LongBuffer.__wrap(__IOURingBufReg.nresv(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'LongBuffer') -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.set(long,int,short,short,java.nio.LongBuffer)"""
        return 'IOURingBufReg'.__wrap(super(__IOURingBufReg, self).set(__long.valueOf(arg0), __int.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def nring_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nring_entries(long,int)"""
        __IOURingBufReg.nring_entries(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingBufReg.nresv(long,int)"""
        return int.__wrap(__IOURingBufReg.nresv(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def calloc() -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.calloc()"""
        return IOURingBufReg.__wrap(__IOURingBufReg.calloc())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.createSafe(long)"""
        return IOURingBufReg.__wrap(__IOURingBufReg.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingBufReg.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def set(self, arg0: 'IOURingBufReg') -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.set(org.lwjgl.system.linux.liburing.IOURingBufReg)"""
        return 'IOURingBufReg'.__wrap(super(__IOURingBufReg, self).set(arg0))

    @overload
    def bgid(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufReg.bgid()"""
        return int.__wrap(super(IOURingBufReg, self).bgid())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.calloc(int)"""
        return Buffer.__wrap(__IOURingBufReg.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.create(long,int)"""
        return Buffer.__wrap(__IOURingBufReg.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def bgid(self, arg0: int) -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.bgid(short)"""
        return 'IOURingBufReg'.__wrap(super(__IOURingBufReg, self).bgid(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingBufReg.nring_entries(long)"""
        return int.__wrap(__IOURingBufReg.nring_entries(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.malloc(int)"""
        return Buffer.__wrap(__IOURingBufReg.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nbgid(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBufReg.nbgid(long)"""
        return int.__wrap(__IOURingBufReg.nbgid(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nring_addr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nring_addr(long,long)"""
        __IOURingBufReg.nring_addr(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBufReg.nflags(long)"""
        return int.__wrap(__IOURingBufReg.nflags(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nbgid(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nbgid(long,short)"""
        __IOURingBufReg.nbgid(__long.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def ring_entries(self, arg0: int) -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.ring_entries(int)"""
        return 'IOURingBufReg'.__wrap(super(__IOURingBufReg, self).ring_entries(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: 'LongBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nresv(long,java.nio.LongBuffer)"""
        __IOURingBufReg.nresv(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nresv(long,int,long)"""
        __IOURingBufReg.nresv(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingBufReg.calloc(__int.valueOf(arg0), arg1))

    @overload
    def ring_addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufReg.ring_addr()"""
        return int.__wrap(super(IOURingBufReg, self).ring_addr())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.create(int)"""
        return Buffer.__wrap(__IOURingBufReg.create(__int.valueOf(arg0)))

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufReg.ring_entries()"""
        return int.__wrap(super(IOURingBufReg, self).ring_entries())

    @overload
    def resv(self, arg0: 'LongBuffer') -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.resv(java.nio.LongBuffer)"""
        return 'IOURingBufReg'.__wrap(super(__IOURingBufReg, self).resv(arg0))

    @overload
    def resv(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingBufReg.resv()"""
        return 'LongBuffer'.__wrap(super(IOURingBufReg, self).resv())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingBufReg.malloc(__int.valueOf(arg0), arg1))

    @overload
    def ring_addr(self, arg0: int) -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.ring_addr(long)"""
        return 'IOURingBufReg'.__wrap(super(__IOURingBufReg, self).ring_addr(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.create()"""
        return IOURingBufReg.__wrap(__IOURingBufReg.create())

    @staticmethod
    @overload
    def malloc() -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.malloc()"""
        return IOURingBufReg.__wrap(__IOURingBufReg.malloc())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBufReg.__wrap(__IOURingBufReg.malloc(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def resv(self, arg0: int, arg1: int) -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.resv(int,long)"""
        return 'IOURingBufReg'.__wrap(super(__IOURingBufReg, self).resv(__int.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def flags(self, arg0: int) -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.flags(short)"""
        return 'IOURingBufReg'.__wrap(super(__IOURingBufReg, self).flags(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBufReg.__wrap(__IOURingBufReg.calloc(arg0))

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
    def create(arg0: int) -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.create(long)"""
        return IOURingBufReg.__wrap(__IOURingBufReg.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nflags(long,short)"""
        __IOURingBufReg.nflags(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def resv(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufReg.resv(int)"""
        return int.__wrap(super(__IOURingBufReg, self).resv(__int.valueOf(arg0)))

    @overload
    def flags(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufReg.flags()"""
        return int.__wrap(super(IOURingBufReg, self).flags()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.linux.liburing.IOURingFileIndexRange as __IOURingFileIndexRange_Buffer
__Buffer = __IOURingFileIndexRange_Buffer.Buffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingFileIndexRange.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def off(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.off()"""
        return int.__wrap(super(Buffer, self).off())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

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

    @overload
    def len(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.len(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).len(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.resv(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv(__long.valueOf(arg0)))

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def off(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.off(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).off(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @overload
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.len()"""
        return int.__wrap(super(Buffer, self).len())

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

    @overload
    def resv(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.resv()"""
        return int.__wrap(super(Buffer, self).resv())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingProbeOp
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import org.lwjgl.system.linux.liburing.IOURingProbeOp as __IOURingProbeOp
__IOURingProbeOp = __IOURingProbeOp
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import org.lwjgl.system.linux.liburing.IOURingProbeOp as __IOURingProbeOp_Buffer
__Buffer = __IOURingProbeOp_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingProbeOp():
    """org.lwjgl.system.linux.liburing.IOURingProbeOp"""
 
    @staticmethod
    def __wrap(java_value: __IOURingProbeOp) -> 'IOURingProbeOp':
        return IOURingProbeOp(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingProbeOp):
        """
        Dynamic initializer for IOURingProbeOp.
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
    def flags(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.flags(short)"""
        return 'IOURingProbeOp'.__wrap(super(__IOURingProbeOp, self).flags(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbeOp.nresv2(long,int)"""
        __IOURingProbeOp.nresv2(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingProbeOp.nflags(long)"""
        return int.__wrap(__IOURingProbeOp.nflags(__long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.calloc(int)"""
        return Buffer.__wrap(__IOURingProbeOp.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingProbeOp.nresv2(long)"""
        return int.__wrap(__IOURingProbeOp.nresv2(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp(java.nio.ByteBuffer)"""
        val = __IOURingProbeOp(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingProbeOp.__wrap(__IOURingProbeOp.calloc(arg0))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingProbeOp.__wrap(__IOURingProbeOp.malloc(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.set(byte,byte,short,int)"""
        return 'IOURingProbeOp'.__wrap(super(__IOURingProbeOp, self).set(__byte.valueOf(arg0), __byte.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.create(long)"""
        return IOURingProbeOp.__wrap(__IOURingProbeOp.create(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingProbeOp.sizeof()"""
        return int.__wrap(super(IOURingProbeOp, self).sizeof())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def op(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.op(byte)"""
        return 'IOURingProbeOp'.__wrap(super(__IOURingProbeOp, self).op(__byte.valueOf(arg0)))

    @overload
    def resv(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.resv(byte)"""
        return 'IOURingProbeOp'.__wrap(super(__IOURingProbeOp, self).resv(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingProbeOp.nresv(long)"""
        return int.__wrap(__IOURingProbeOp.nresv(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def resv(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbeOp.resv()"""
        return int.__wrap(super(IOURingProbeOp, self).resv())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc() -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.calloc()"""
        return IOURingProbeOp.__wrap(__IOURingProbeOp.calloc())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbeOp.op()"""
        return int.__wrap(super(IOURingProbeOp, self).op())

    @overload
    def resv2(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.resv2(int)"""
        return 'IOURingProbeOp'.__wrap(super(__IOURingProbeOp, self).resv2(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingProbeOp.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.malloc()"""
        return IOURingProbeOp.__wrap(__IOURingProbeOp.malloc())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingProbeOp.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.create(int)"""
        return Buffer.__wrap(__IOURingProbeOp.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.malloc(int)"""
        return Buffer.__wrap(__IOURingProbeOp.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbeOp.nresv(long,byte)"""
        __IOURingProbeOp.nresv(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.create(long,int)"""
        return Buffer.__wrap(__IOURingProbeOp.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingProbeOp.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def flags(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingProbeOp.flags()"""
        return int.__wrap(super(IOURingProbeOp, self).flags())

    @staticmethod
    @overload
    def create() -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.create()"""
        return IOURingProbeOp.__wrap(__IOURingProbeOp.create())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nop(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbeOp.nop(long,byte)"""
        __IOURingProbeOp.nop(__long.valueOf(arg0), __byte.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.createSafe(long)"""
        return IOURingProbeOp.__wrap(__IOURingProbeOp.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbeOp.nflags(long,short)"""
        __IOURingProbeOp.nflags(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nop(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingProbeOp.nop(long)"""
        return int.__wrap(__IOURingProbeOp.nop(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingProbeOp') -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.set(org.lwjgl.system.linux.liburing.IOURingProbeOp)"""
        return 'IOURingProbeOp'.__wrap(super(__IOURingProbeOp, self).set(arg0))

    @overload
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingProbeOp.resv2()"""
        return int.__wrap(super(IOURingProbeOp, self).resv2()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingGeteventsArg
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingGeteventsArg as __IOURingGeteventsArg_Buffer
__Buffer = __IOURingGeteventsArg_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.linux.liburing.IOURingGeteventsArg as __IOURingGeteventsArg
__IOURingGeteventsArg = __IOURingGeteventsArg
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingGeteventsArg():
    """org.lwjgl.system.linux.liburing.IOURingGeteventsArg"""
 
    @staticmethod
    def __wrap(java_value: __IOURingGeteventsArg) -> 'IOURingGeteventsArg':
        return IOURingGeteventsArg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingGeteventsArg):
        """
        Dynamic initializer for IOURingGeteventsArg.
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
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.create(int)"""
        return Buffer.__wrap(__IOURingGeteventsArg.create(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingGeteventsArg.__wrap(__IOURingGeteventsArg.calloc(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingGeteventsArg.malloc(__int.valueOf(arg0), arg1))

    @overload
    def ts(self, arg0: int) -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.ts(long)"""
        return 'IOURingGeteventsArg'.__wrap(super(__IOURingGeteventsArg, self).ts(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingGeteventsArg.__wrap(__IOURingGeteventsArg.malloc(arg0))

    @overload
    def pad(self, arg0: int) -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.pad(int)"""
        return 'IOURingGeteventsArg'.__wrap(super(__IOURingGeteventsArg, self).pad(__int.valueOf(arg0)))

    @overload
    def sigmask(self, arg0: int) -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.sigmask(long)"""
        return 'IOURingGeteventsArg'.__wrap(super(__IOURingGeteventsArg, self).sigmask(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def calloc() -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.calloc()"""
        return IOURingGeteventsArg.__wrap(__IOURingGeteventsArg.calloc())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nts(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nts(long,long)"""
        __IOURingGeteventsArg.nts(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nts(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nts(long)"""
        return int.__wrap(__IOURingGeteventsArg.nts(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingGeteventsArg.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.create(long,int)"""
        return Buffer.__wrap(__IOURingGeteventsArg.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def pad(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingGeteventsArg.pad()"""
        return int.__wrap(super(IOURingGeteventsArg, self).pad())

    @staticmethod
    @overload
    def nsigmask(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nsigmask(long)"""
        return int.__wrap(__IOURingGeteventsArg.nsigmask(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def sigmask(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingGeteventsArg.sigmask()"""
        return int.__wrap(super(IOURingGeteventsArg, self).sigmask())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg(java.nio.ByteBuffer)"""
        val = __IOURingGeteventsArg(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingGeteventsArg.npad(long,int)"""
        __IOURingGeteventsArg.npad(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def npad(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingGeteventsArg.npad(long)"""
        return int.__wrap(__IOURingGeteventsArg.npad(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.malloc()"""
        return IOURingGeteventsArg.__wrap(__IOURingGeteventsArg.malloc())

    @staticmethod
    @overload
    def nsigmask_sz(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nsigmask_sz(long,int)"""
        __IOURingGeteventsArg.nsigmask_sz(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def sigmask_sz(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingGeteventsArg.sigmask_sz()"""
        return int.__wrap(super(IOURingGeteventsArg, self).sigmask_sz())

    @overload
    def ts(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingGeteventsArg.ts()"""
        return int.__wrap(super(IOURingGeteventsArg, self).ts())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def set(self, arg0: 'IOURingGeteventsArg') -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.set(org.lwjgl.system.linux.liburing.IOURingGeteventsArg)"""
        return 'IOURingGeteventsArg'.__wrap(super(__IOURingGeteventsArg, self).set(arg0))

    @overload
    def sigmask_sz(self, arg0: int) -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.sigmask_sz(int)"""
        return 'IOURingGeteventsArg'.__wrap(super(__IOURingGeteventsArg, self).sigmask_sz(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingGeteventsArg.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.calloc(int)"""
        return Buffer.__wrap(__IOURingGeteventsArg.calloc(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.set(long,int,int,long)"""
        return 'IOURingGeteventsArg'.__wrap(super(__IOURingGeteventsArg, self).set(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.createSafe(long)"""
        return IOURingGeteventsArg.__wrap(__IOURingGeteventsArg.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nsigmask_sz(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nsigmask_sz(long)"""
        return int.__wrap(__IOURingGeteventsArg.nsigmask_sz(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nsigmask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nsigmask(long,long)"""
        __IOURingGeteventsArg.nsigmask(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingGeteventsArg.sizeof()"""
        return int.__wrap(super(IOURingGeteventsArg, self).sizeof())

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.create(long)"""
        return IOURingGeteventsArg.__wrap(__IOURingGeteventsArg.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.malloc(int)"""
        return Buffer.__wrap(__IOURingGeteventsArg.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.create()"""
        return IOURingGeteventsArg.__wrap(__IOURingGeteventsArg.create()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURing$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingSQ as __IOURingSQ
__IOURingSQ = __IOURingSQ
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import org.lwjgl.system.linux.liburing.IOURingCQ as __IOURingCQ
__IOURingCQ = __IOURingCQ
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.liburing.IOURing as __IOURing_Buffer
__Buffer = __IOURing_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURing.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__int.valueOf(arg0)))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def ring_fd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.ring_fd(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_fd(__int.valueOf(arg0)))

    @overload
    def sq(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.sq(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingSQ>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sq(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def ring_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing$Buffer.ring_fd()"""
        return int.__wrap(super(Buffer, self).ring_fd())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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
    def cq(self) -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURing$Buffer.cq()"""
        return 'IOURingCQ'.__wrap(super(Buffer, self).cq())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def sq(self) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURing$Buffer.sq()"""
        return 'IOURingSQ'.__wrap(super(Buffer, self).sq())

    @overload
    def cq(self, arg0: 'IOURingCQ') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.cq(org.lwjgl.system.linux.liburing.IOURingCQ)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cq(arg0))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def int_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.int_flags(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).int_flags(__byte.valueOf(arg0)))

    @overload
    def sq(self, arg0: 'IOURingSQ') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.sq(org.lwjgl.system.linux.liburing.IOURingSQ)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sq(arg0))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def features(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing$Buffer.features()"""
        return int.__wrap(super(Buffer, self).features())

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

    @overload
    def enter_ring_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing$Buffer.enter_ring_fd()"""
        return int.__wrap(super(Buffer, self).enter_ring_fd())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def enter_ring_fd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.enter_ring_fd(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).enter_ring_fd(__int.valueOf(arg0)))

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
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @overload
    def features(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.features(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).features(__int.valueOf(arg0)))

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

    @overload
    def cq(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.cq(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingCQ>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cq(arg0))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def int_flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURing$Buffer.int_flags()"""
        return int.__wrap(super(Buffer, self).int_flags())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingCQE
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.linux.liburing.IOURingCQE as __IOURingCQE
__IOURingCQE = __IOURingCQE
import org.lwjgl.system.linux.liburing.IOURingCQE as __IOURingCQE_Buffer
__Buffer = __IOURingCQE_Buffer.Buffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingCQE():
    """org.lwjgl.system.linux.liburing.IOURingCQE"""
 
    @staticmethod
    def __wrap(java_value: __IOURingCQE) -> 'IOURingCQE':
        return IOURingCQE(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingCQE):
        """
        Dynamic initializer for IOURingCQE.
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
    def big_cqe(self, arg0: int, arg1: int) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.big_cqe(int,long)"""
        return 'IOURingCQE'.__wrap(super(__IOURingCQE, self).big_cqe(__int.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def user_data(self, arg0: int) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.user_data(long)"""
        return 'IOURingCQE'.__wrap(super(__IOURingCQE, self).user_data(__long.valueOf(arg0)))

    @overload
    def res(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQE.res()"""
        return int.__wrap(super(IOURingCQE, self).res())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQE.nflags(long,int)"""
        __IOURingCQE.nflags(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def big_cqe(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQE.big_cqe(int)"""
        return int.__wrap(super(__IOURingCQE, self).big_cqe(__int.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def calloc() -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.calloc()"""
        return IOURingCQE.__wrap(__IOURingCQE.calloc())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.create(int)"""
        return Buffer.__wrap(__IOURingCQE.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingCQE.nflags(long)"""
        return int.__wrap(__IOURingCQE.nflags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.malloc(int)"""
        return Buffer.__wrap(__IOURingCQE.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.calloc(int)"""
        return Buffer.__wrap(__IOURingCQE.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nres(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingCQE.nres(long)"""
        return int.__wrap(__IOURingCQE.nres(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.createSafe(long)"""
        return IOURingCQE.__wrap(__IOURingCQE.createSafe(__long.valueOf(arg0)))

    @overload
    def flags(self, arg0: int) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.flags(int)"""
        return 'IOURingCQE'.__wrap(super(__IOURingCQE, self).flags(__int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def nbig_cqe(arg0: int, arg1: 'LongBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQE.nbig_cqe(long,java.nio.LongBuffer)"""
        __IOURingCQE.nbig_cqe(__long.valueOf(arg0), arg1)

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nuser_data(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingCQE.nuser_data(long)"""
        return int.__wrap(__IOURingCQE.nuser_data(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nbig_cqe(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingCQE.nbig_cqe(long)"""
        return LongBuffer.__wrap(__IOURingCQE.nbig_cqe(__long.valueOf(arg0)))

    @overload
    def res(self, arg0: int) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.res(int)"""
        return 'IOURingCQE'.__wrap(super(__IOURingCQE, self).res(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nuser_data(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQE.nuser_data(long,long)"""
        __IOURingCQE.nuser_data(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def big_cqe(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingCQE.big_cqe()"""
        return 'LongBuffer'.__wrap(super(IOURingCQE, self).big_cqe())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingCQE(java.nio.ByteBuffer)"""
        val = __IOURingCQE(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.create(long)"""
        return IOURingCQE.__wrap(__IOURingCQE.create(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingCQE') -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.set(org.lwjgl.system.linux.liburing.IOURingCQE)"""
        return 'IOURingCQE'.__wrap(super(__IOURingCQE, self).set(arg0))

    @overload
    def big_cqe(self, arg0: 'LongBuffer') -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.big_cqe(java.nio.LongBuffer)"""
        return 'IOURingCQE'.__wrap(super(__IOURingCQE, self).big_cqe(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingCQE.__wrap(__IOURingCQE.calloc(arg0))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQE.flags()"""
        return int.__wrap(super(IOURingCQE, self).flags())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingCQE.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nbig_cqe(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingCQE.nbig_cqe(long,int)"""
        return int.__wrap(__IOURingCQE.nbig_cqe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQE.sizeof()"""
        return int.__wrap(super(IOURingCQE, self).sizeof())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'LongBuffer') -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.set(long,int,int,java.nio.LongBuffer)"""
        return 'IOURingCQE'.__wrap(super(__IOURingCQE, self).set(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingCQE.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc() -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.malloc()"""
        return IOURingCQE.__wrap(__IOURingCQE.malloc())

    @staticmethod
    @overload
    def nres(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQE.nres(long,int)"""
        __IOURingCQE.nres(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nbig_cqe(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQE.nbig_cqe(long,int,long)"""
        __IOURingCQE.nbig_cqe(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.create(long,int)"""
        return Buffer.__wrap(__IOURingCQE.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def create() -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.create()"""
        return IOURingCQE.__wrap(__IOURingCQE.create())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingCQE.__wrap(__IOURingCQE.malloc(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def user_data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQE.user_data()"""
        return int.__wrap(super(IOURingCQE, self).user_data())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingCQE.createSafe(__long.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
try:
    from pyglsystem import linux
except ImportError:
    linux = __import_once__("pyglsystem.linux")

import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.linux.liburing.IOURingSyncCancelReg as __IOURingSyncCancelReg_Buffer
__Buffer = __IOURingSyncCancelReg_Buffer.Buffer
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.KernelTimespec as __KernelTimespec
__KernelTimespec = __KernelTimespec
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.addr(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).addr(__long.valueOf(arg0)))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def timeout(self, arg0: 'KernelTimespec') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.timeout(org.lwjgl.system.linux.KernelTimespec)"""
        return 'Buffer'.__wrap(super(__Buffer, self).timeout(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def fd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.fd(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).fd(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.addr()"""
        return int.__wrap(super(Buffer, self).addr())

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
    def timeout(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.timeout(java.util.function.Consumer<org.lwjgl.system.linux.KernelTimespec>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).timeout(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

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

    @overload
    def timeout(self) -> 'linux.KernelTimespec':
        """public org.lwjgl.system.linux.KernelTimespec org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.timeout()"""
        return 'linux.KernelTimespec'.__wrap(super(Buffer, self).timeout())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

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
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__int.valueOf(arg0)))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.fd()"""
        return int.__wrap(super(Buffer, self).fd())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.linux.liburing.IOURingGeteventsArg as __IOURingGeteventsArg_Buffer
__Buffer = __IOURingGeteventsArg_Buffer.Buffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingGeteventsArg.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def ts(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.ts(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ts(__long.valueOf(arg0)))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def sigmask(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.sigmask()"""
        return int.__wrap(super(Buffer, self).sigmask())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def pad(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.pad(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).pad(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def sigmask_sz(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.sigmask_sz(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sigmask_sz(__int.valueOf(arg0)))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def sigmask_sz(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.sigmask_sz()"""
        return int.__wrap(super(Buffer, self).sigmask_sz())

    @overload
    def pad(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.pad()"""
        return int.__wrap(super(Buffer, self).pad())

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
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def ts(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.ts()"""
        return int.__wrap(super(Buffer, self).ts())

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

    @overload
    def sigmask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.sigmask(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sigmask(__long.valueOf(arg0)))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

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
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingFileIndexRange
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.lwjgl.system.linux.liburing.IOURingFileIndexRange as __IOURingFileIndexRange_Buffer
__Buffer = __IOURingFileIndexRange_Buffer.Buffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.linux.liburing.IOURingFileIndexRange as __IOURingFileIndexRange
__IOURingFileIndexRange = __IOURingFileIndexRange
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class IOURingFileIndexRange():
    """org.lwjgl.system.linux.liburing.IOURingFileIndexRange"""
 
    @staticmethod
    def __wrap(java_value: __IOURingFileIndexRange) -> 'IOURingFileIndexRange':
        return IOURingFileIndexRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingFileIndexRange):
        """
        Dynamic initializer for IOURingFileIndexRange.
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
    def calloc(arg0: 'MemoryStack') -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingFileIndexRange.__wrap(__IOURingFileIndexRange.calloc(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingFileIndexRange.__wrap(__IOURingFileIndexRange.malloc(arg0))

    @overload
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingFileIndexRange.len()"""
        return int.__wrap(super(IOURingFileIndexRange, self).len())

    @overload
    def len(self, arg0: int) -> 'IOURingFileIndexRange':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.len(int)"""
        return 'IOURingFileIndexRange'.__wrap(super(__IOURingFileIndexRange, self).len(__int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.createSafe(long)"""
        return IOURingFileIndexRange.__wrap(__IOURingFileIndexRange.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.malloc(int)"""
        return Buffer.__wrap(__IOURingFileIndexRange.malloc(__int.valueOf(arg0)))

    @overload
    def off(self, arg0: int) -> 'IOURingFileIndexRange':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.off(int)"""
        return 'IOURingFileIndexRange'.__wrap(super(__IOURingFileIndexRange, self).off(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nlen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingFileIndexRange.nlen(long)"""
        return int.__wrap(__IOURingFileIndexRange.nlen(__long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.calloc()"""
        return IOURingFileIndexRange.__wrap(__IOURingFileIndexRange.calloc())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def off(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingFileIndexRange.off()"""
        return int.__wrap(super(IOURingFileIndexRange, self).off())

    @staticmethod
    @overload
    def noff(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingFileIndexRange.noff(long,int)"""
        __IOURingFileIndexRange.noff(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> 'IOURingFileIndexRange':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.set(int,int,long)"""
        return 'IOURingFileIndexRange'.__wrap(super(__IOURingFileIndexRange, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingFileIndexRange.sizeof()"""
        return int.__wrap(super(IOURingFileIndexRange, self).sizeof())

    @overload
    def resv(self, arg0: int) -> 'IOURingFileIndexRange':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.resv(long)"""
        return 'IOURingFileIndexRange'.__wrap(super(__IOURingFileIndexRange, self).resv(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingFileIndexRange.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc() -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.malloc()"""
        return IOURingFileIndexRange.__wrap(__IOURingFileIndexRange.malloc())

    @overload
    def set(self, arg0: 'IOURingFileIndexRange') -> 'IOURingFileIndexRange':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.set(org.lwjgl.system.linux.liburing.IOURingFileIndexRange)"""
        return 'IOURingFileIndexRange'.__wrap(super(__IOURingFileIndexRange, self).set(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingFileIndexRange.calloc(__int.valueOf(arg0), arg1))

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
    def nlen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingFileIndexRange.nlen(long,int)"""
        __IOURingFileIndexRange.nlen(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingFileIndexRange.nresv(long,long)"""
        __IOURingFileIndexRange.nresv(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingFileIndexRange.nresv(long)"""
        return int.__wrap(__IOURingFileIndexRange.nresv(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.create()"""
        return IOURingFileIndexRange.__wrap(__IOURingFileIndexRange.create())

    @staticmethod
    @overload
    def noff(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingFileIndexRange.noff(long)"""
        return int.__wrap(__IOURingFileIndexRange.noff(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.calloc(int)"""
        return Buffer.__wrap(__IOURingFileIndexRange.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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
    def create(arg0: int) -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.create(long)"""
        return IOURingFileIndexRange.__wrap(__IOURingFileIndexRange.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.create(long,int)"""
        return Buffer.__wrap(__IOURingFileIndexRange.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingFileIndexRange.malloc(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange(java.nio.ByteBuffer)"""
        val = __IOURingFileIndexRange(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.create(int)"""
        return Buffer.__wrap(__IOURingFileIndexRange.create(__int.valueOf(arg0)))

    @overload
    def resv(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingFileIndexRange.resv()"""
        return int.__wrap(super(IOURingFileIndexRange, self).resv()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Short as __short
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.linux.liburing.IOURingProbeOp as __IOURingProbeOp_Buffer
__Buffer = __IOURingProbeOp_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingProbeOp.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

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
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def resv(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.resv()"""
        return int.__wrap(super(Buffer, self).resv())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.resv2()"""
        return int.__wrap(super(Buffer, self).resv2())

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

    @overload
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.resv(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv(__byte.valueOf(arg0)))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @overload
    def resv2(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.resv2(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).resv2(__int.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.flags(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__short.valueOf(arg0)))

    @overload
    def flags(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

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

    @overload
    def op(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.op(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).op(__byte.valueOf(arg0)))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.op()"""
        return int.__wrap(super(Buffer, self).op())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSQE
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import org.lwjgl.system.linux.liburing.IOURingSQE as __IOURingSQE_Buffer
__Buffer = __IOURingSQE_Buffer.Buffer
import java.nio.ShortBuffer as ShortBuffer
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import java.lang.Short as __short
import org.lwjgl.system.linux.liburing.IOURingSQE as __IOURingSQE
__IOURingSQE = __IOURingSQE
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class IOURingSQE():
    """org.lwjgl.system.linux.liburing.IOURingSQE"""
 
    @staticmethod
    def __wrap(java_value: __IOURingSQE) -> 'IOURingSQE':
        return IOURingSQE(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IOURingSQE):
        """
        Dynamic initializer for IOURingSQE.
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
    def n__pad2(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingSQE.n__pad2(long)"""
        return LongBuffer.__wrap(__IOURingSQE.n__pad2(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncmd(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.ncmd(long,int,byte)"""
        __IOURingSQE.ncmd(__long.valueOf(arg0), __int.valueOf(arg1), __byte.valueOf(arg2))

    @staticmethod
    @overload
    def nfile_index(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nfile_index(long)"""
        return int.__wrap(__IOURingSQE.nfile_index(__long.valueOf(arg0)))

    @overload
    def cmd(self, arg0: int) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE.cmd(int)"""
        return int.__wrap(super(__IOURingSQE, self).cmd(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nsync_range_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nsync_range_flags(long)"""
        return int.__wrap(__IOURingSQE.nsync_range_flags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncmd(arg0: int, arg1: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingSQE.ncmd(long,int)"""
        return int.__wrap(__IOURingSQE.ncmd(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def npoll_events(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.npoll_events(long,short)"""
        __IOURingSQE.npoll_events(__long.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def accept_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.accept_flags()"""
        return int.__wrap(super(IOURingSQE, self).accept_flags())

    @staticmethod
    @overload
    def nhardlink_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nhardlink_flags(long)"""
        return int.__wrap(__IOURingSQE.nhardlink_flags(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def n__pad3(arg0: int, arg1: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.n__pad3(long,int)"""
        return int.__wrap(__IOURingSQE.n__pad3(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def fadvise_advice(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.fadvise_advice()"""
        return int.__wrap(super(IOURingSQE, self).fadvise_advice())

    @staticmethod
    @overload
    def nsplice_off_in(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_off_in(long)"""
        return int.__wrap(__IOURingSQE.nsplice_off_in(__long.valueOf(arg0)))

    @overload
    def splice_fd_in(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.splice_fd_in()"""
        return int.__wrap(super(IOURingSQE, self).splice_fd_in())

    @overload
    def __pad3(self, arg0: int, arg1: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.__pad3(int,short)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).__pad3(__int.valueOf(arg0), __short.valueOf(arg1)))

    @overload
    def msg_ring_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.msg_ring_flags()"""
        return int.__wrap(super(IOURingSQE, self).msg_ring_flags())

    @staticmethod
    @overload
    def nopen_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nopen_flags(long)"""
        return int.__wrap(__IOURingSQE.nopen_flags(__long.valueOf(arg0)))

    @overload
    def ioprio(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.ioprio(short)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).ioprio(__short.valueOf(arg0)))

    @overload
    def timeout_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.timeout_flags()"""
        return int.__wrap(super(IOURingSQE, self).timeout_flags())

    @overload
    def xattr_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.xattr_flags()"""
        return int.__wrap(super(IOURingSQE, self).xattr_flags())

    @staticmethod
    @overload
    def naddr_len(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.naddr_len(long,short)"""
        __IOURingSQE.naddr_len(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def n__pad2(arg0: int, arg1: 'LongBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.n__pad2(long,java.nio.LongBuffer)"""
        __IOURingSQE.n__pad2(__long.valueOf(arg0), arg1)

    @overload
    def splice_off_in(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.splice_off_in(long)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).splice_off_in(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nlen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nlen(long)"""
        return int.__wrap(__IOURingSQE.nlen(__long.valueOf(arg0)))

    @overload
    def addr_len(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.addr_len()"""
        return int.__wrap(super(IOURingSQE, self).addr_len())

    @staticmethod
    @overload
    def nbuf_group(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nbuf_group(long,short)"""
        __IOURingSQE.nbuf_group(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def nuring_cmd_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nuring_cmd_flags(long,int)"""
        __IOURingSQE.nuring_cmd_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def rename_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.rename_flags()"""
        return int.__wrap(super(IOURingSQE, self).rename_flags())

    @overload
    def poll_events(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.poll_events()"""
        return int.__wrap(super(IOURingSQE, self).poll_events())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingSQE.calloc(__int.valueOf(arg0), arg1))

    @overload
    def splice_off_in(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.splice_off_in()"""
        return int.__wrap(super(IOURingSQE, self).splice_off_in())

    @overload
    def buf_index(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.buf_index()"""
        return int.__wrap(super(IOURingSQE, self).buf_index())

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingSQE.nflags(long)"""
        return int.__wrap(__IOURingSQE.nflags(__long.valueOf(arg0)))

    @overload
    def buf_index(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.buf_index(short)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).buf_index(__short.valueOf(arg0)))

    @overload
    def personality(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.personality()"""
        return int.__wrap(super(IOURingSQE, self).personality())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def poll32_events(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.poll32_events()"""
        return int.__wrap(super(IOURingSQE, self).poll32_events())

    @overload
    def __pad3(self, arg0: int) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.__pad3(int)"""
        return int.__wrap(super(__IOURingSQE, self).__pad3(__int.valueOf(arg0)))

    @overload
    def fd(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.fd(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).fd(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.create(long)"""
        return IOURingSQE.__wrap(__IOURingSQE.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncmd_op(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.ncmd_op(long,int)"""
        __IOURingSQE.ncmd_op(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def cmd(self, arg0: 'ByteBuffer') -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.cmd(java.nio.ByteBuffer)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).cmd(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.calloc(int)"""
        return Buffer.__wrap(__IOURingSQE.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nfsync_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nfsync_flags(long)"""
        return int.__wrap(__IOURingSQE.nfsync_flags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def n__pad3(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.n__pad3(long,int,short)"""
        __IOURingSQE.n__pad3(__long.valueOf(arg0), __int.valueOf(arg1), __short.valueOf(arg2))

    @overload
    def flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE.flags()"""
        return int.__wrap(super(IOURingSQE, self).flags())

    @overload
    def set(self, arg0: 'IOURingSQE') -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.set(org.lwjgl.system.linux.liburing.IOURingSQE)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).set(arg0))

    @staticmethod
    @overload
    def nopcode(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nopcode(long,byte)"""
        __IOURingSQE.nopcode(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def npoll_events(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.npoll_events(long)"""
        return int.__wrap(__IOURingSQE.npoll_events(__long.valueOf(arg0)))

    @overload
    def open_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.open_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).open_flags(__int.valueOf(arg0)))

    @overload
    def __pad3(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.linux.liburing.IOURingSQE.__pad3()"""
        return 'ShortBuffer'.__wrap(super(IOURingSQE, self).__pad3())

    @overload
    def user_data(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.user_data(long)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).user_data(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def naccept_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.naccept_flags(long)"""
        return int.__wrap(__IOURingSQE.naccept_flags(__long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def n__pad1(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.n__pad1(long,int)"""
        __IOURingSQE.n__pad1(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def naddr2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.naddr2(long,long)"""
        __IOURingSQE.naddr2(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def ncmd(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQE.ncmd(long)"""
        return ByteBuffer.__wrap(__IOURingSQE.ncmd(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def cancel_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.cancel_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).cancel_flags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def naddr3(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.naddr3(long)"""
        return int.__wrap(__IOURingSQE.naddr3(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def naddr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.naddr(long,long)"""
        __IOURingSQE.naddr(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nmsg_ring_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nmsg_ring_flags(long)"""
        return int.__wrap(__IOURingSQE.nmsg_ring_flags(__long.valueOf(arg0)))

    @overload
    def hardlink_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.hardlink_flags()"""
        return int.__wrap(super(IOURingSQE, self).hardlink_flags())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def off(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.off()"""
        return int.__wrap(super(IOURingSQE, self).off())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__IOURingSQE.malloc(__int.valueOf(arg0), arg1))

    @overload
    def open_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.open_flags()"""
        return int.__wrap(super(IOURingSQE, self).open_flags())

    @overload
    def __pad1(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.__pad1(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).__pad1(__int.valueOf(arg0)))

    @overload
    def __pad2(self, arg0: 'LongBuffer') -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.__pad2(java.nio.LongBuffer)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).__pad2(arg0))

    @staticmethod
    @overload
    def malloc() -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.malloc()"""
        return IOURingSQE.__wrap(__IOURingSQE.malloc())

    @staticmethod
    @overload
    def n__pad2(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.n__pad2(long,int,long)"""
        __IOURingSQE.n__pad2(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @overload
    def poll32_events(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.poll32_events(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).poll32_events(__int.valueOf(arg0)))

    @overload
    def cmd(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQE.cmd()"""
        return 'ByteBuffer'.__wrap(super(IOURingSQE, self).cmd())

    @staticmethod
    @overload
    def nrename_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nrename_flags(long)"""
        return int.__wrap(__IOURingSQE.nrename_flags(__long.valueOf(arg0)))

    @overload
    def timeout_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.timeout_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).timeout_flags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nrename_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nrename_flags(long,int)"""
        __IOURingSQE.nrename_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __pad2(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.__pad2(int)"""
        return int.__wrap(super(__IOURingSQE, self).__pad2(__int.valueOf(arg0)))

    @overload
    def hardlink_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.hardlink_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).hardlink_flags(__int.valueOf(arg0)))

    @overload
    def file_index(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.file_index()"""
        return int.__wrap(super(IOURingSQE, self).file_index())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def __pad2(self, arg0: int, arg1: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.__pad2(int,long)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).__pad2(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nxattr_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nxattr_flags(long,int)"""
        __IOURingSQE.nxattr_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def cancel_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.cancel_flags()"""
        return int.__wrap(super(IOURingSQE, self).cancel_flags())

    @overload
    def accept_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.accept_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).accept_flags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.calloc()"""
        return IOURingSQE.__wrap(__IOURingSQE.calloc())

    @overload
    def len(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.len(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).len(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nbuf_index(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nbuf_index(long,short)"""
        __IOURingSQE.nbuf_index(__long.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def splice_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.splice_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).splice_flags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def n__pad1(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.n__pad1(long)"""
        return int.__wrap(__IOURingSQE.n__pad1(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncancel_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.ncancel_flags(long,int)"""
        __IOURingSQE.ncancel_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nioprio(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.nioprio(long)"""
        return int.__wrap(__IOURingSQE.nioprio(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmsg_ring_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nmsg_ring_flags(long,int)"""
        __IOURingSQE.nmsg_ring_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nsplice_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_flags(long)"""
        return int.__wrap(__IOURingSQE.nsplice_flags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nflags(long,byte)"""
        __IOURingSQE.nflags(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def noff(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.noff(long)"""
        return int.__wrap(__IOURingSQE.noff(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmsg_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nmsg_flags(long,int)"""
        __IOURingSQE.nmsg_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def ncmd_op(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.ncmd_op(long)"""
        return int.__wrap(__IOURingSQE.ncmd_op(__long.valueOf(arg0)))

    @overload
    def cmd_op(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.cmd_op(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).cmd_op(__int.valueOf(arg0)))

    @overload
    def splice_fd_in(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.splice_fd_in(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).splice_fd_in(__int.valueOf(arg0)))

    @overload
    def fsync_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.fsync_flags()"""
        return int.__wrap(super(IOURingSQE, self).fsync_flags())

    @staticmethod
    @overload
    def n__pad3(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.linux.liburing.IOURingSQE.n__pad3(long)"""
        return ShortBuffer.__wrap(__IOURingSQE.n__pad3(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.createSafe(long,int)"""
        return Buffer.__wrap(__IOURingSQE.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nbuf_group(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.nbuf_group(long)"""
        return int.__wrap(__IOURingSQE.nbuf_group(__long.valueOf(arg0)))

    @overload
    def off(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.off(long)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).off(__long.valueOf(arg0)))

    @overload
    def opcode(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE.opcode()"""
        return int.__wrap(super(IOURingSQE, self).opcode())

    @overload
    def fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.fd()"""
        return int.__wrap(super(IOURingSQE, self).fd())

    @staticmethod
    @overload
    def nbuf_index(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.nbuf_index(long)"""
        return int.__wrap(__IOURingSQE.nbuf_index(__long.valueOf(arg0)))

    @overload
    def opcode(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.opcode(byte)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).opcode(__byte.valueOf(arg0)))

    @overload
    def addr(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.addr(long)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).addr(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncmd(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.ncmd(long,java.nio.ByteBuffer)"""
        __IOURingSQE.ncmd(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nfd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nfd(long,int)"""
        __IOURingSQE.nfd(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def poll_events(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.poll_events(short)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).poll_events(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def nunlink_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nunlink_flags(long)"""
        return int.__wrap(__IOURingSQE.nunlink_flags(__long.valueOf(arg0)))

    @overload
    def msg_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.msg_flags()"""
        return int.__wrap(super(IOURingSQE, self).msg_flags())

    @staticmethod
    @overload
    def nmsg_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nmsg_flags(long)"""
        return int.__wrap(__IOURingSQE.nmsg_flags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncancel_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.ncancel_flags(long)"""
        return int.__wrap(__IOURingSQE.ncancel_flags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nhardlink_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nhardlink_flags(long,int)"""
        __IOURingSQE.nhardlink_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def naddr2(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.naddr2(long)"""
        return int.__wrap(__IOURingSQE.naddr2(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstatx_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nstatx_flags(long)"""
        return int.__wrap(__IOURingSQE.nstatx_flags(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.sizeof()"""
        return int.__wrap(super(IOURingSQE, self).sizeof())

    @overload
    def sync_range_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.sync_range_flags()"""
        return int.__wrap(super(IOURingSQE, self).sync_range_flags())

    @overload
    def msg_ring_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.msg_ring_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).msg_ring_flags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nuring_cmd_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nuring_cmd_flags(long)"""
        return int.__wrap(__IOURingSQE.nuring_cmd_flags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.malloc(int)"""
        return Buffer.__wrap(__IOURingSQE.malloc(__int.valueOf(arg0)))

    @overload
    def addr_len(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.addr_len(short)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).addr_len(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.create(int)"""
        return Buffer.__wrap(__IOURingSQE.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def npoll32_events(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.npoll32_events(long,int)"""
        __IOURingSQE.npoll32_events(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def sync_range_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.sync_range_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).sync_range_flags(__int.valueOf(arg0)))

    @overload
    def uring_cmd_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.uring_cmd_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).uring_cmd_flags(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def noff(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.noff(long,long)"""
        __IOURingSQE.noff(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nstatx_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nstatx_flags(long,int)"""
        __IOURingSQE.nstatx_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def naddr3(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.naddr3(long,long)"""
        __IOURingSQE.naddr3(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def addr2(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.addr2()"""
        return int.__wrap(super(IOURingSQE, self).addr2())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def npersonality(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.npersonality(long)"""
        return int.__wrap(__IOURingSQE.npersonality(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSQE.__wrap(__IOURingSQE.malloc(arg0))

    @overload
    def statx_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.statx_flags()"""
        return int.__wrap(super(IOURingSQE, self).statx_flags())

    @overload
    def user_data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.user_data()"""
        return int.__wrap(super(IOURingSQE, self).user_data())

    @overload
    def personality(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.personality(short)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).personality(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def naddr(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.naddr(long)"""
        return int.__wrap(__IOURingSQE.naddr(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nuser_data(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.nuser_data(long)"""
        return int.__wrap(__IOURingSQE.nuser_data(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nfadvise_advice(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nfadvise_advice(long,int)"""
        __IOURingSQE.nfadvise_advice(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nsplice_off_in(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_off_in(long,long)"""
        __IOURingSQE.nsplice_off_in(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def fadvise_advice(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.fadvise_advice(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).fadvise_advice(__int.valueOf(arg0)))

    @overload
    def __pad3(self, arg0: 'ShortBuffer') -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.__pad3(java.nio.ShortBuffer)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).__pad3(arg0))

    @staticmethod
    @overload
    def nsplice_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_flags(long,int)"""
        __IOURingSQE.nsplice_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nfsync_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nfsync_flags(long,int)"""
        __IOURingSQE.nfsync_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nsplice_fd_in(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_fd_in(long,int)"""
        __IOURingSQE.nsplice_fd_in(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nuser_data(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nuser_data(long,long)"""
        __IOURingSQE.nuser_data(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def n__pad2(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.n__pad2(long,int)"""
        return int.__wrap(__IOURingSQE.n__pad2(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSQE(java.nio.ByteBuffer)"""
        val = __IOURingSQE(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def uring_cmd_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.uring_cmd_flags()"""
        return int.__wrap(super(IOURingSQE, self).uring_cmd_flags())

    @staticmethod
    @overload
    def nxattr_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nxattr_flags(long)"""
        return int.__wrap(__IOURingSQE.nxattr_flags(__long.valueOf(arg0)))

    @overload
    def buf_group(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.buf_group(short)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).buf_group(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def nrw_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nrw_flags(long)"""
        return int.__wrap(__IOURingSQE.nrw_flags(__long.valueOf(arg0)))

    @overload
    def flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.flags(byte)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).flags(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def nopcode(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingSQE.nopcode(long)"""
        return int.__wrap(__IOURingSQE.nopcode(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nrw_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nrw_flags(long,int)"""
        __IOURingSQE.nrw_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nunlink_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nunlink_flags(long,int)"""
        __IOURingSQE.nunlink_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nsync_range_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nsync_range_flags(long,int)"""
        __IOURingSQE.nsync_range_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nopen_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nopen_flags(long,int)"""
        __IOURingSQE.nopen_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nfadvise_advice(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nfadvise_advice(long)"""
        return int.__wrap(__IOURingSQE.nfadvise_advice(__long.valueOf(arg0)))

    @overload
    def cmd(self, arg0: int, arg1: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.cmd(int,byte)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).cmd(__int.valueOf(arg0), __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def nfd(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nfd(long)"""
        return int.__wrap(__IOURingSQE.nfd(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def npersonality(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.npersonality(long,short)"""
        __IOURingSQE.npersonality(__long.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def unlink_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.unlink_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).unlink_flags(__int.valueOf(arg0)))

    @overload
    def fsync_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.fsync_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).fsync_flags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ntimeout_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.ntimeout_flags(long,int)"""
        __IOURingSQE.ntimeout_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def splice_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.splice_flags()"""
        return int.__wrap(super(IOURingSQE, self).splice_flags())

    @staticmethod
    @overload
    def naddr_len(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.naddr_len(long)"""
        return int.__wrap(__IOURingSQE.naddr_len(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsplice_fd_in(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_fd_in(long)"""
        return int.__wrap(__IOURingSQE.nsplice_fd_in(__long.valueOf(arg0)))

    @overload
    def rw_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.rw_flags()"""
        return int.__wrap(super(IOURingSQE, self).rw_flags())

    @overload
    def __pad1(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.__pad1()"""
        return int.__wrap(super(IOURingSQE, self).__pad1())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSQE.__wrap(__IOURingSQE.calloc(arg0))

    @overload
    def file_index(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.file_index(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).file_index(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nlen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nlen(long,int)"""
        __IOURingSQE.nlen(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def npoll32_events(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.npoll32_events(long)"""
        return int.__wrap(__IOURingSQE.npoll32_events(__long.valueOf(arg0)))

    @overload
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.len()"""
        return int.__wrap(super(IOURingSQE, self).len())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.create(long,int)"""
        return Buffer.__wrap(__IOURingSQE.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nfile_index(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nfile_index(long,int)"""
        __IOURingSQE.nfile_index(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def msg_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.msg_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).msg_flags(__int.valueOf(arg0)))

    @overload
    def addr3(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.addr3()"""
        return int.__wrap(super(IOURingSQE, self).addr3())

    @staticmethod
    @overload
    def nioprio(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nioprio(long,short)"""
        __IOURingSQE.nioprio(__long.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def cmd_op(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.cmd_op()"""
        return int.__wrap(super(IOURingSQE, self).cmd_op())

    @staticmethod
    @overload
    def ntimeout_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.ntimeout_flags(long)"""
        return int.__wrap(__IOURingSQE.ntimeout_flags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.create()"""
        return IOURingSQE.__wrap(__IOURingSQE.create())

    @overload
    def unlink_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.unlink_flags()"""
        return int.__wrap(super(IOURingSQE, self).unlink_flags())

    @staticmethod
    @overload
    def naccept_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.naccept_flags(long,int)"""
        __IOURingSQE.naccept_flags(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def ioprio(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.ioprio()"""
        return int.__wrap(super(IOURingSQE, self).ioprio())

    @overload
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.addr()"""
        return int.__wrap(super(IOURingSQE, self).addr())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.createSafe(long)"""
        return IOURingSQE.__wrap(__IOURingSQE.createSafe(__long.valueOf(arg0)))

    @overload
    def buf_group(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.buf_group()"""
        return int.__wrap(super(IOURingSQE, self).buf_group())

    @overload
    def addr3(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.addr3(long)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).addr3(__long.valueOf(arg0)))

    @overload
    def __pad2(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingSQE.__pad2()"""
        return 'LongBuffer'.__wrap(super(IOURingSQE, self).__pad2())

    @overload
    def addr2(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.addr2(long)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).addr2(__long.valueOf(arg0)))

    @overload
    def statx_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.statx_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).statx_flags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def n__pad3(arg0: int, arg1: 'ShortBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.n__pad3(long,java.nio.ShortBuffer)"""
        __IOURingSQE.n__pad3(__long.valueOf(arg0), arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def rw_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.rw_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).rw_flags(__int.valueOf(arg0)))

    @overload
    def rename_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.rename_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).rename_flags(__int.valueOf(arg0)))

    @overload
    def xattr_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.xattr_flags(int)"""
        return 'IOURingSQE'.__wrap(super(__IOURingSQE, self).xattr_flags(__int.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSQ$Buffer
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.linux.liburing.IOURingSQ as __IOURingSQ_Buffer
__Buffer = __IOURingSQ_Buffer.Buffer
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import org.lwjgl.system.linux.liburing.IOURingSQE as __IOURingSQE
__IOURingSQE = __IOURingSQE
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingSQ.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def ktail(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ktail(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).ktail(__int.valueOf(arg0)))

    @overload
    def kring_mask(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kring_mask(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).kring_mask(__int.valueOf(arg0)))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def khead(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.khead(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).khead(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def ring_ptr(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_ptr()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).ring_ptr())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def array(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.array(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).array(arg0))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def ktail(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ktail(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ktail(arg0))

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_entries()"""
        return int.__wrap(super(Buffer, self).ring_entries())

    @overload
    def kdropped(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kdropped(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).kdropped(__int.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def ring_sz(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_sz()"""
        return int.__wrap(super(Buffer, self).ring_sz())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def sqes(self) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqes()"""
        return 'IOURingSQE'.__wrap(super(Buffer, self).sqes())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def kflags(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kflags(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).kflags(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def sqe_tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqe_tail()"""
        return int.__wrap(super(Buffer, self).sqe_tail())

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
    def ring_ptr(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_ptr(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_ptr(arg0))

    @overload
    def kdropped(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kdropped(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).kdropped(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_mask()"""
        return int.__wrap(super(Buffer, self).ring_mask())

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
    def kring_mask(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kring_mask(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).kring_mask(arg0))

    @overload
    def kring_entries(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kring_entries(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).kring_entries(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def ring_mask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_mask(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_mask(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def sqe_head(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqe_head(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sqe_head(__int.valueOf(arg0)))

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
    def kflags(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kflags(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).kflags(__int.valueOf(arg0)))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def kring_entries(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kring_entries(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).kring_entries(arg0))

    @overload
    def sqe_head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqe_head()"""
        return int.__wrap(super(Buffer, self).sqe_head())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def khead(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.khead(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).khead(__int.valueOf(arg0)))

    @overload
    def sqes(self, arg0: 'IOURingSQE') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqes(org.lwjgl.system.linux.liburing.IOURingSQE)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sqes(arg0))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def array(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.array(int)"""
        return 'IntBuffer'.__wrap(super(__Buffer, self).array(__int.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def ring_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_entries(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ring_entries(__int.valueOf(arg0)))

    @overload
    def sqe_tail(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqe_tail(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).sqe_tail(__int.valueOf(arg0)))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1)))