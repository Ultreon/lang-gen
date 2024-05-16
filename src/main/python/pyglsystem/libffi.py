from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.libffi.LibFFI as __LibFFI
__LibFFI = __LibFFI
import org.lwjgl.system.libffi.FFIClosure as __FFIClosure
__FFIClosure = __FFIClosure
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class LibFFI():
    """org.lwjgl.system.libffi.LibFFI"""
 
    @staticmethod
    def __wrap(java_value: __LibFFI) -> 'LibFFI':
        return LibFFI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LibFFI):
        """
        Dynamic initializer for LibFFI.
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
    def ffi_prep_cif_var(arg0: 'FFICIF', arg1: int, arg2: int, arg3: 'FFIType', arg4: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_prep_cif_var(org.lwjgl.system.libffi.FFICIF,int,int,org.lwjgl.system.libffi.FFIType,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__LibFFI.ffi_prep_cif_var(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def ffi_closure_alloc(arg0: int, arg1: 'PointerBuffer') -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.LibFFI.ffi_closure_alloc(long,org.lwjgl.PointerBuffer)"""
        return FFIClosure.__wrap(__LibFFI.ffi_closure_alloc(__long.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nffi_closure_free(arg0: int):
        """public static native void org.lwjgl.system.libffi.LibFFI.nffi_closure_free(long)"""
        __LibFFI.nffi_closure_free(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nffi_call(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.libffi.LibFFI.nffi_call(long,long,long,long)"""
        __LibFFI.nffi_call(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ffi_closure_free(arg0: 'FFIClosure'):
        """public static void org.lwjgl.system.libffi.LibFFI.ffi_closure_free(org.lwjgl.system.libffi.FFIClosure)"""
        __LibFFI.ffi_closure_free(arg0)

    @staticmethod
    @overload
    def nffi_get_struct_offsets(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_get_struct_offsets(int,long,long)"""
        return int.__wrap(__LibFFI.nffi_get_struct_offsets(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def ffi_prep_cif(arg0: 'FFICIF', arg1: int, arg2: 'FFIType', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_prep_cif(org.lwjgl.system.libffi.FFICIF,int,org.lwjgl.system.libffi.FFIType,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__LibFFI.ffi_prep_cif(arg0, __int.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def nffi_prep_closure_loc(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_prep_closure_loc(long,long,long,long,long)"""
        return int.__wrap(__LibFFI.nffi_prep_closure_loc(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nffi_prep_cif_var(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_prep_cif_var(long,int,int,int,long,long)"""
        return int.__wrap(__LibFFI.nffi_prep_cif_var(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def nffi_closure_alloc(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.libffi.LibFFI.nffi_closure_alloc(long,long)"""
        return int.__wrap(__LibFFI.nffi_closure_alloc(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def ffi_get_struct_offsets(arg0: int, arg1: 'FFIType', arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_get_struct_offsets(int,org.lwjgl.system.libffi.FFIType,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__LibFFI.ffi_get_struct_offsets(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def ffi_call(arg0: 'FFICIF', arg1: int, arg2: 'ByteBuffer', arg3: 'PointerBuffer'):
        """public static void org.lwjgl.system.libffi.LibFFI.ffi_call(org.lwjgl.system.libffi.FFICIF,long,java.nio.ByteBuffer,org.lwjgl.PointerBuffer)"""
        __LibFFI.ffi_call(arg0, __long.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nffi_prep_cif(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_prep_cif(long,int,int,long,long)"""
        return int.__wrap(__LibFFI.nffi_prep_cif(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

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
    def ffi_prep_closure_loc(arg0: 'FFIClosure', arg1: 'FFICIF', arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_prep_closure_loc(org.lwjgl.system.libffi.FFIClosure,org.lwjgl.system.libffi.FFICIF,long,long,long)"""
        return int.__wrap(__LibFFI.ffi_prep_closure_loc(arg0, arg1, __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.lwjgl.system.libffi.LibFFI
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.libffi.LibFFI as __LibFFI
__LibFFI = __LibFFI
import org.lwjgl.system.libffi.FFIClosure as __FFIClosure
__FFIClosure = __FFIClosure
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class LibFFI():
    """org.lwjgl.system.libffi.LibFFI"""
 
    @staticmethod
    def __wrap(java_value: __LibFFI) -> 'LibFFI':
        return LibFFI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LibFFI):
        """
        Dynamic initializer for LibFFI.
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
    def ffi_prep_cif_var(arg0: 'FFICIF', arg1: int, arg2: int, arg3: 'FFIType', arg4: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_prep_cif_var(org.lwjgl.system.libffi.FFICIF,int,int,org.lwjgl.system.libffi.FFIType,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__LibFFI.ffi_prep_cif_var(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def ffi_closure_alloc(arg0: int, arg1: 'PointerBuffer') -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.LibFFI.ffi_closure_alloc(long,org.lwjgl.PointerBuffer)"""
        return FFIClosure.__wrap(__LibFFI.ffi_closure_alloc(__long.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nffi_closure_free(arg0: int):
        """public static native void org.lwjgl.system.libffi.LibFFI.nffi_closure_free(long)"""
        __LibFFI.nffi_closure_free(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nffi_call(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.libffi.LibFFI.nffi_call(long,long,long,long)"""
        __LibFFI.nffi_call(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ffi_closure_free(arg0: 'FFIClosure'):
        """public static void org.lwjgl.system.libffi.LibFFI.ffi_closure_free(org.lwjgl.system.libffi.FFIClosure)"""
        __LibFFI.ffi_closure_free(arg0)

    @staticmethod
    @overload
    def nffi_get_struct_offsets(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_get_struct_offsets(int,long,long)"""
        return int.__wrap(__LibFFI.nffi_get_struct_offsets(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def ffi_prep_cif(arg0: 'FFICIF', arg1: int, arg2: 'FFIType', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_prep_cif(org.lwjgl.system.libffi.FFICIF,int,org.lwjgl.system.libffi.FFIType,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__LibFFI.ffi_prep_cif(arg0, __int.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def nffi_prep_closure_loc(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_prep_closure_loc(long,long,long,long,long)"""
        return int.__wrap(__LibFFI.nffi_prep_closure_loc(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nffi_prep_cif_var(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_prep_cif_var(long,int,int,int,long,long)"""
        return int.__wrap(__LibFFI.nffi_prep_cif_var(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def nffi_closure_alloc(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.libffi.LibFFI.nffi_closure_alloc(long,long)"""
        return int.__wrap(__LibFFI.nffi_closure_alloc(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def ffi_get_struct_offsets(arg0: int, arg1: 'FFIType', arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_get_struct_offsets(int,org.lwjgl.system.libffi.FFIType,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__LibFFI.ffi_get_struct_offsets(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def ffi_call(arg0: 'FFICIF', arg1: int, arg2: 'ByteBuffer', arg3: 'PointerBuffer'):
        """public static void org.lwjgl.system.libffi.LibFFI.ffi_call(org.lwjgl.system.libffi.FFICIF,long,java.nio.ByteBuffer,org.lwjgl.PointerBuffer)"""
        __LibFFI.ffi_call(arg0, __long.valueOf(arg1), arg2, arg3)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nffi_prep_cif(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.libffi.LibFFI.nffi_prep_cif(long,int,int,long,long)"""
        return int.__wrap(__LibFFI.nffi_prep_cif(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

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
    def ffi_prep_closure_loc(arg0: 'FFIClosure', arg1: 'FFICIF', arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.libffi.LibFFI.ffi_prep_closure_loc(org.lwjgl.system.libffi.FFIClosure,org.lwjgl.system.libffi.FFICIF,long,long,long)"""
        return int.__wrap(__LibFFI.ffi_prep_closure_loc(arg0, arg1, __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.lwjgl.system.libffi.LibFFI 
 
 
# CLASS: org.lwjgl.system.libffi.FFICIF$Buffer
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
import org.lwjgl.system.libffi.FFICIF as __FFICIF_Buffer
__Buffer = __FFICIF_Buffer.Buffer
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.libffi.FFIType as __FFIType
__FFIType = __FFIType
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
 
class Buffer(pyglsystem.__StructBuffer, pyglsystem.StructBuffer, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.libffi.FFICIF.Buffer"""
 
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
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def bytes(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF$Buffer.bytes()"""
        return int.__wrap(super(Buffer, self).bytes())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def arg_types(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFICIF$Buffer.arg_types(int)"""
        return 'pygl.PointerBuffer'.__wrap(super(__Buffer, self).arg_types(__int.valueOf(arg0)))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @overload
    def rtype(self) -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFICIF$Buffer.rtype()"""
        return 'FFIType'.__wrap(super(Buffer, self).rtype())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFICIF$Buffer(java.nio.ByteBuffer)"""
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
    def flags(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.libffi.FFICIF$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def nargs(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF$Buffer.nargs()"""
        return int.__wrap(super(Buffer, self).nargs())

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
    def abi(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF$Buffer.abi()"""
        return int.__wrap(super(Buffer, self).abi())

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
 
 
# CLASS: org.lwjgl.system.libffi.FFIType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.libffi.FFIType as __FFIType
__FFIType = __FFIType
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
import org.lwjgl.system.libffi.FFIType as __FFIType_Buffer
__Buffer = __FFIType_Buffer.Buffer
from builtins import bool
from builtins import int
 
class FFIType(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.libffi.FFIType"""
 
    @staticmethod
    def __wrap(java_value: __FFIType) -> 'FFIType':
        return FFIType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FFIType):
        """
        Dynamic initializer for FFIType.
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
    def calloc(arg0: 'MemoryStack') -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.calloc(org.lwjgl.system.MemoryStack)"""
        return FFIType.__wrap(__FFIType.calloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.calloc(int)"""
        return Buffer.__wrap(__FFIType.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.create()"""
        return FFIType.__wrap(__FFIType.create())

    @overload
    def set(self, arg0: 'FFIType') -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.set(org.lwjgl.system.libffi.FFIType)"""
        return 'FFIType'.__wrap(super(__FFIType, self).set(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.createSafe(long)"""
        return FFIType.__wrap(__FFIType.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nalignment(arg0: int, arg1: int):
        """public static void org.lwjgl.system.libffi.FFIType.nalignment(long,short)"""
        __FFIType.nalignment(__long.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFIType(java.nio.ByteBuffer)"""
        val = __FFIType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.malloc(int)"""
        return Buffer.__wrap(__FFIType.malloc(__int.valueOf(arg0)))

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
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'PointerBuffer') -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.set(long,short,short,org.lwjgl.PointerBuffer)"""
        return 'FFIType'.__wrap(super(__FFIType, self).set(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def malloc() -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.malloc()"""
        return FFIType.__wrap(__FFIType.malloc())

    @overload
    def alignment(self, arg0: int) -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.alignment(short)"""
        return 'FFIType'.__wrap(super(__FFIType, self).alignment(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def nsize(arg0: int) -> int:
        """public static long org.lwjgl.system.libffi.FFIType.nsize(long)"""
        return int.__wrap(__FFIType.nsize(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.libffi.FFIType.nsize(long,long)"""
        __FFIType.nsize(__long.valueOf(arg0), __long.valueOf(arg1))

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
    def nalignment(arg0: int) -> int:
        """public static short org.lwjgl.system.libffi.FFIType.nalignment(long)"""
        return int.__wrap(__FFIType.nalignment(__long.valueOf(arg0)))

    @overload
    def size(self, arg0: int) -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.size(long)"""
        return 'FFIType'.__wrap(super(__FFIType, self).size(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def elements(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFIType.elements(int)"""
        return 'pygl.PointerBuffer'.__wrap(super(__FFIType, self).elements(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.malloc(org.lwjgl.system.MemoryStack)"""
        return FFIType.__wrap(__FFIType.malloc(arg0))

    @staticmethod
    @overload
    def ntype(arg0: int) -> int:
        """public static short org.lwjgl.system.libffi.FFIType.ntype(long)"""
        return int.__wrap(__FFIType.ntype(__long.valueOf(arg0)))

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

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.create(int)"""
        return Buffer.__wrap(__FFIType.create(__int.valueOf(arg0)))

    @overload
    def size(self) -> int:
        """public long org.lwjgl.system.libffi.FFIType.size()"""
        return int.__wrap(super(FFIType, self).size())

    @staticmethod
    @overload
    def create(arg0: int) -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.create(long)"""
        return FFIType.__wrap(__FFIType.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__FFIType.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.createSafe(long,int)"""
        return Buffer.__wrap(__FFIType.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.create(long,int)"""
        return Buffer.__wrap(__FFIType.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__FFIType.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def alignment(self) -> int:
        """public short org.lwjgl.system.libffi.FFIType.alignment()"""
        return int.__wrap(super(FFIType, self).alignment())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.libffi.FFIType.sizeof()"""
        return int.__wrap(super(FFIType, self).sizeof())

    @staticmethod
    @overload
    def nelements(arg0: int, arg1: 'PointerBuffer'):
        """public static void org.lwjgl.system.libffi.FFIType.nelements(long,org.lwjgl.PointerBuffer)"""
        __FFIType.nelements(__long.valueOf(arg0), arg1)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def nelements(arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFIType.nelements(long,int)"""
        return pygl.PointerBuffer.__wrap(__FFIType.nelements(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ntype(arg0: int, arg1: int):
        """public static void org.lwjgl.system.libffi.FFIType.ntype(long,short)"""
        __FFIType.ntype(__long.valueOf(arg0), __short.valueOf(arg1))

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
    def elements(self, arg0: 'PointerBuffer') -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.elements(org.lwjgl.PointerBuffer)"""
        return 'FFIType'.__wrap(super(__FFIType, self).elements(arg0))

    @overload
    def type(self) -> int:
        """public short org.lwjgl.system.libffi.FFIType.type()"""
        return int.__wrap(super(FFIType, self).type())

    @staticmethod
    @overload
    def calloc() -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.calloc()"""
        return FFIType.__wrap(__FFIType.calloc())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def type(self, arg0: int) -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFIType.type(short)"""
        return 'FFIType'.__wrap(super(__FFIType, self).type(__short.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.libffi.FFIClosure
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.libffi.FFIClosure as __FFIClosure_Buffer
__Buffer = __FFIClosure_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import org.lwjgl.system.libffi.FFIClosure as __FFIClosure
__FFIClosure = __FFIClosure
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
 
class FFIClosure(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.libffi.FFIClosure"""
 
    @staticmethod
    def __wrap(java_value: __FFIClosure) -> 'FFIClosure':
        return FFIClosure(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FFIClosure):
        """
        Dynamic initializer for FFIClosure.
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
    def fun(self) -> int:
        """public long org.lwjgl.system.libffi.FFIClosure.fun()"""
        return int.__wrap(super(FFIClosure, self).fun())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nuser_data(arg0: int) -> int:
        """public static long org.lwjgl.system.libffi.FFIClosure.nuser_data(long)"""
        return int.__wrap(__FFIClosure.nuser_data(__long.valueOf(arg0)))

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
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__FFIClosure.malloc(__int.valueOf(arg0), arg1))

    @overload
    def user_data(self) -> int:
        """public long org.lwjgl.system.libffi.FFIClosure.user_data()"""
        return int.__wrap(super(FFIClosure, self).user_data())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.createSafe(long,int)"""
        return Buffer.__wrap(__FFIClosure.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.calloc(int)"""
        return Buffer.__wrap(__FFIClosure.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nfun(arg0: int) -> int:
        """public static long org.lwjgl.system.libffi.FFIClosure.nfun(long)"""
        return int.__wrap(__FFIClosure.nfun(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.libffi.FFIClosure.sizeof()"""
        return int.__wrap(super(FFIClosure, self).sizeof())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.calloc(org.lwjgl.system.MemoryStack)"""
        return FFIClosure.__wrap(__FFIClosure.calloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__FFIClosure.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def calloc() -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.calloc()"""
        return FFIClosure.__wrap(__FFIClosure.calloc())

    @staticmethod
    @overload
    def create(arg0: int) -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.create(long)"""
        return FFIClosure.__wrap(__FFIClosure.create(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFIClosure(java.nio.ByteBuffer)"""
        val = __FFIClosure(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.malloc(org.lwjgl.system.MemoryStack)"""
        return FFIClosure.__wrap(__FFIClosure.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.create(long,int)"""
        return Buffer.__wrap(__FFIClosure.create(__long.valueOf(arg0), __int.valueOf(arg1)))

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
    def malloc() -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.malloc()"""
        return FFIClosure.__wrap(__FFIClosure.malloc())

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
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.malloc(int)"""
        return Buffer.__wrap(__FFIClosure.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def cif(self) -> 'FFICIF':
        """public org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFIClosure.cif()"""
        return 'FFICIF'.__wrap(super(FFIClosure, self).cif())

    @staticmethod
    @overload
    def create() -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.create()"""
        return FFIClosure.__wrap(__FFIClosure.create())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'FFIClosure':
        """public static org.lwjgl.system.libffi.FFIClosure org.lwjgl.system.libffi.FFIClosure.createSafe(long)"""
        return FFIClosure.__wrap(__FFIClosure.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFIClosure$Buffer org.lwjgl.system.libffi.FFIClosure.create(int)"""
        return Buffer.__wrap(__FFIClosure.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def ncif(arg0: int) -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFIClosure.ncif(long)"""
        return FFICIF.__wrap(__FFIClosure.ncif(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.system.libffi.FFIClosure$Buffer
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
import org.lwjgl.system.libffi.FFIClosure as __FFIClosure_Buffer
__Buffer = __FFIClosure_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
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
 
class Buffer(pyglsystem.__StructBuffer, pyglsystem.StructBuffer, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.libffi.FFIClosure.Buffer"""
 
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
    def user_data(self) -> int:
        """public long org.lwjgl.system.libffi.FFIClosure$Buffer.user_data()"""
        return int.__wrap(super(Buffer, self).user_data())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFIClosure$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.libffi.FFIClosure$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def cif(self) -> 'FFICIF':
        """public org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFIClosure$Buffer.cif()"""
        return 'FFICIF'.__wrap(super(Buffer, self).cif())

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
    def fun(self) -> int:
        """public long org.lwjgl.system.libffi.FFIClosure$Buffer.fun()"""
        return int.__wrap(super(Buffer, self).fun()) 
 
 
# CLASS: org.lwjgl.system.libffi.FFIType$Buffer
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
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

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
import org.lwjgl.system.libffi.FFIType as __FFIType_Buffer
__Buffer = __FFIType_Buffer.Buffer
from builtins import int
 
class Buffer(pyglsystem.__StructBuffer, pyglsystem.StructBuffer, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.libffi.FFIType.Buffer"""
 
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
    def elements(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFIType$Buffer.elements(int)"""
        return 'pygl.PointerBuffer'.__wrap(super(__Buffer, self).elements(__int.valueOf(arg0)))

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
    def type(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.type(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).type(__short.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFIType$Buffer(java.nio.ByteBuffer)"""
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

    @overload
    def alignment(self) -> int:
        """public short org.lwjgl.system.libffi.FFIType$Buffer.alignment()"""
        return int.__wrap(super(Buffer, self).alignment())

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
    def type(self) -> int:
        """public short org.lwjgl.system.libffi.FFIType$Buffer.type()"""
        return int.__wrap(super(Buffer, self).type())

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
    def size(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.size(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).size(__long.valueOf(arg0)))

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
    def alignment(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.alignment(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).alignment(__short.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.libffi.FFIType$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def elements(self, arg0: 'PointerBuffer') -> 'Buffer':
        """public org.lwjgl.system.libffi.FFIType$Buffer org.lwjgl.system.libffi.FFIType$Buffer.elements(org.lwjgl.PointerBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).elements(arg0))

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

    @overload
    def size(self) -> int:
        """public long org.lwjgl.system.libffi.FFIType$Buffer.size()"""
        return int.__wrap(super(Buffer, self).size())

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
 
 
# CLASS: org.lwjgl.system.libffi.FFICIF
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.libffi.FFIType as __FFIType
__FFIType = __FFIType
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.libffi.FFICIF as __FFICIF_Buffer
__Buffer = __FFICIF_Buffer.Buffer
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
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import bool
from builtins import int
 
class FFICIF(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.libffi.FFICIF"""
 
    @staticmethod
    def __wrap(java_value: __FFICIF) -> 'FFICIF':
        return FFICIF(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FFICIF):
        """
        Dynamic initializer for FFICIF.
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
    def abi(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF.abi()"""
        return int.__wrap(super(FFICIF, self).abi())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF.sizeof()"""
        return int.__wrap(super(FFICIF, self).sizeof())

    @staticmethod
    @overload
    def nrtype(arg0: int) -> 'FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFICIF.nrtype(long)"""
        return FFIType.__wrap(__FFICIF.nrtype(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__FFICIF.malloc(__int.valueOf(arg0), arg1))

    @overload
    def nargs(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF.nargs()"""
        return int.__wrap(super(FFICIF, self).nargs())

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
    def create(arg0: int) -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.create(long)"""
        return FFICIF.__wrap(__FFICIF.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.createSafe(long,int)"""
        return Buffer.__wrap(__FFICIF.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

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
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__FFICIF.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nabi(arg0: int) -> int:
        """public static int org.lwjgl.system.libffi.FFICIF.nabi(long)"""
        return int.__wrap(__FFICIF.nabi(__long.valueOf(arg0)))

    @overload
    def bytes(self) -> int:
        """public int org.lwjgl.system.libffi.FFICIF.bytes()"""
        return int.__wrap(super(FFICIF, self).bytes())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.malloc(org.lwjgl.system.MemoryStack)"""
        return FFICIF.__wrap(__FFICIF.malloc(arg0))

    @overload
    def arg_types(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFICIF.arg_types(int)"""
        return 'pygl.PointerBuffer'.__wrap(super(__FFICIF, self).arg_types(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nnargs(arg0: int) -> int:
        """public static int org.lwjgl.system.libffi.FFICIF.nnargs(long)"""
        return int.__wrap(__FFICIF.nnargs(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.malloc()"""
        return FFICIF.__wrap(__FFICIF.malloc())

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.libffi.FFICIF.nflags(long)"""
        return int.__wrap(__FFICIF.nflags(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def narg_types(arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.libffi.FFICIF.narg_types(long,int)"""
        return pygl.PointerBuffer.__wrap(__FFICIF.narg_types(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.create(int)"""
        return Buffer.__wrap(__FFICIF.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.malloc(int)"""
        return Buffer.__wrap(__FFICIF.malloc(__int.valueOf(arg0)))

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
    def calloc() -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.calloc()"""
        return FFICIF.__wrap(__FFICIF.calloc())

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
        """public int org.lwjgl.system.libffi.FFICIF.flags()"""
        return int.__wrap(super(FFICIF, self).flags())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def create() -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.create()"""
        return FFICIF.__wrap(__FFICIF.create())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.calloc(org.lwjgl.system.MemoryStack)"""
        return FFICIF.__wrap(__FFICIF.calloc(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def rtype(self) -> 'FFIType':
        """public org.lwjgl.system.libffi.FFIType org.lwjgl.system.libffi.FFICIF.rtype()"""
        return 'FFIType'.__wrap(super(FFICIF, self).rtype())

    @staticmethod
    @overload
    def nbytes(arg0: int) -> int:
        """public static int org.lwjgl.system.libffi.FFICIF.nbytes(long)"""
        return int.__wrap(__FFICIF.nbytes(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.create(long,int)"""
        return Buffer.__wrap(__FFICIF.create(__long.valueOf(arg0), __int.valueOf(arg1)))

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.libffi.FFICIF(java.nio.ByteBuffer)"""
        val = __FFICIF(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.libffi.FFICIF$Buffer org.lwjgl.system.libffi.FFICIF.calloc(int)"""
        return Buffer.__wrap(__FFICIF.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.libffi.FFICIF.createSafe(long)"""
        return FFICIF.__wrap(__FFICIF.createSafe(__long.valueOf(arg0)))