from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.system.linux.liburing.IOURingRSRCRegister as _IOURingRSRCRegister_Buffer
_Buffer = _IOURingRSRCRegister_Buffer.Buffer
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
import org.lwjgl.system.linux.liburing.IOURingRSRCRegister as _IOURingRSRCRegister
_IOURingRSRCRegister = _IOURingRSRCRegister
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingRSRCRegister():
    """org.lwjgl.system.linux.liburing.IOURingRSRCRegister"""
 
    @staticmethod
    def _wrap(java_value: _IOURingRSRCRegister) -> 'IOURingRSRCRegister':
        return IOURingRSRCRegister(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingRSRCRegister):
        """
        Dynamic initializer for IOURingRSRCRegister.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingRSRCRegister__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingRSRCRegister__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create() -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create()"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.create())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.createSafe(long)"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.createSafe(_long.valueOf(arg0)))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.flags()"""
        return int._wrap(super(IOURingRSRCRegister, self).flags())

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nresv2(long)"""
        return int._wrap(_IOURingRSRCRegister.nresv2(_long.valueOf(arg0)))

    @overload
    def nr(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nr(int)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).nr(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.set(int,int,long,long,long)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nflags(long)"""
        return int._wrap(_IOURingRSRCRegister.nflags(_long.valueOf(arg0)))

    @overload
    def nr(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nr()"""
        return int._wrap(super(IOURingRSRCRegister, self).nr())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.sizeof()"""
        return int._wrap(super(IOURingRSRCRegister, self).sizeof())

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
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create(long,int)"""
        return Buffer._wrap(_IOURingRSRCRegister.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def ndata(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ndata(long,long)"""
        _IOURingRSRCRegister.ndata(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def tags(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.tags(long)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).tags(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister(java.nio.ByteBuffer)"""
        val = _IOURingRSRCRegister(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRSRCRegister.calloc(_int.valueOf(arg0), arg1))

    @overload
    def tags(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.tags()"""
        return int._wrap(super(IOURingRSRCRegister, self).tags())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc(int)"""
        return Buffer._wrap(_IOURingRSRCRegister.malloc(_int.valueOf(arg0)))

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
    def malloc(arg0: 'MemoryStack') -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.malloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc(int)"""
        return Buffer._wrap(_IOURingRSRCRegister.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nnr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nnr(long,int)"""
        _IOURingRSRCRegister.nnr(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resv2(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.resv2()"""
        return int._wrap(super(IOURingRSRCRegister, self).resv2())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def calloc() -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc()"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.calloc())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRSRCRegister.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nnr(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nnr(long)"""
        return int._wrap(_IOURingRSRCRegister.nnr(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create(int)"""
        return Buffer._wrap(_IOURingRSRCRegister.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ntags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ntags(long,long)"""
        _IOURingRSRCRegister.ntags(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.data()"""
        return int._wrap(super(IOURingRSRCRegister, self).data())

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nflags(long,int)"""
        _IOURingRSRCRegister.nflags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create(long)"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc()"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.malloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.createSafe(long,int)"""
        return Buffer._wrap(_IOURingRSRCRegister.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def flags(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.flags(int)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndata(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ndata(long)"""
        return int._wrap(_IOURingRSRCRegister.ndata(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nresv2(long,long)"""
        _IOURingRSRCRegister.nresv2(_long.valueOf(arg0), _long.valueOf(arg1))

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
    def resv2(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.resv2(long)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).resv2(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.calloc(arg0))

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
    def data(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.data(long)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).data(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntags(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ntags(long)"""
        return int._wrap(_IOURingRSRCRegister.ntags(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingRSRCRegister') -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.set(org.lwjgl.system.linux.liburing.IOURingRSRCRegister)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).set(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCRegister
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.system.linux.liburing.IOURingRSRCRegister as _IOURingRSRCRegister_Buffer
_Buffer = _IOURingRSRCRegister_Buffer.Buffer
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
import org.lwjgl.system.linux.liburing.IOURingRSRCRegister as _IOURingRSRCRegister
_IOURingRSRCRegister = _IOURingRSRCRegister
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingRSRCRegister():
    """org.lwjgl.system.linux.liburing.IOURingRSRCRegister"""
 
    @staticmethod
    def _wrap(java_value: _IOURingRSRCRegister) -> 'IOURingRSRCRegister':
        return IOURingRSRCRegister(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingRSRCRegister):
        """
        Dynamic initializer for IOURingRSRCRegister.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingRSRCRegister__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingRSRCRegister__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create() -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create()"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.create())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.createSafe(long)"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.createSafe(_long.valueOf(arg0)))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.flags()"""
        return int._wrap(super(IOURingRSRCRegister, self).flags())

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nresv2(long)"""
        return int._wrap(_IOURingRSRCRegister.nresv2(_long.valueOf(arg0)))

    @overload
    def nr(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nr(int)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).nr(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.set(int,int,long,long,long)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nflags(long)"""
        return int._wrap(_IOURingRSRCRegister.nflags(_long.valueOf(arg0)))

    @overload
    def nr(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nr()"""
        return int._wrap(super(IOURingRSRCRegister, self).nr())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.sizeof()"""
        return int._wrap(super(IOURingRSRCRegister, self).sizeof())

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
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create(long,int)"""
        return Buffer._wrap(_IOURingRSRCRegister.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def ndata(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ndata(long,long)"""
        _IOURingRSRCRegister.ndata(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def tags(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.tags(long)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).tags(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister(java.nio.ByteBuffer)"""
        val = _IOURingRSRCRegister(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRSRCRegister.calloc(_int.valueOf(arg0), arg1))

    @overload
    def tags(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.tags()"""
        return int._wrap(super(IOURingRSRCRegister, self).tags())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc(int)"""
        return Buffer._wrap(_IOURingRSRCRegister.malloc(_int.valueOf(arg0)))

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
    def malloc(arg0: 'MemoryStack') -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.malloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc(int)"""
        return Buffer._wrap(_IOURingRSRCRegister.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nnr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nnr(long,int)"""
        _IOURingRSRCRegister.nnr(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resv2(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.resv2()"""
        return int._wrap(super(IOURingRSRCRegister, self).resv2())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def calloc() -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc()"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.calloc())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRSRCRegister.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nnr(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nnr(long)"""
        return int._wrap(_IOURingRSRCRegister.nnr(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create(int)"""
        return Buffer._wrap(_IOURingRSRCRegister.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ntags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ntags(long,long)"""
        _IOURingRSRCRegister.ntags(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.data()"""
        return int._wrap(super(IOURingRSRCRegister, self).data())

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nflags(long,int)"""
        _IOURingRSRCRegister.nflags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.create(long)"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.malloc()"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.malloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister.createSafe(long,int)"""
        return Buffer._wrap(_IOURingRSRCRegister.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def flags(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.flags(int)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndata(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ndata(long)"""
        return int._wrap(_IOURingRSRCRegister.ndata(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCRegister.nresv2(long,long)"""
        _IOURingRSRCRegister.nresv2(_long.valueOf(arg0), _long.valueOf(arg1))

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
    def resv2(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.resv2(long)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).resv2(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingRSRCRegister':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCRegister._wrap(_IOURingRSRCRegister.calloc(arg0))

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
    def data(self, arg0: int) -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.data(long)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).data(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntags(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCRegister.ntags(long)"""
        return int._wrap(_IOURingRSRCRegister.ntags(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingRSRCRegister') -> 'IOURingRSRCRegister':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister org.lwjgl.system.linux.liburing.IOURingRSRCRegister.set(org.lwjgl.system.linux.liburing.IOURingRSRCRegister)"""
        return 'IOURingRSRCRegister'._wrap(super(_IOURingRSRCRegister, self).set(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCRegister 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOCQRingOffsets
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
import org.lwjgl.system.linux.liburing.IOCQRingOffsets as _IOCQRingOffsets_Buffer
_Buffer = _IOCQRingOffsets_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.linux.liburing.IOCQRingOffsets as _IOCQRingOffsets
_IOCQRingOffsets = _IOCQRingOffsets
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOCQRingOffsets():
    """org.lwjgl.system.linux.liburing.IOCQRingOffsets"""
 
    @staticmethod
    def _wrap(java_value: _IOCQRingOffsets) -> 'IOCQRingOffsets':
        return IOCQRingOffsets(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOCQRingOffsets):
        """
        Dynamic initializer for IOCQRingOffsets.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOCQRingOffsets__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOCQRingOffsets__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.create(int)"""
        return Buffer._wrap(_IOCQRingOffsets.create(_int.valueOf(arg0)))

    @overload
    def overflow(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.overflow()"""
        return int._wrap(super(IOCQRingOffsets, self).overflow())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.create(long,int)"""
        return Buffer._wrap(_IOCQRingOffsets.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.create(long)"""
        return IOCQRingOffsets._wrap(_IOCQRingOffsets.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.nflags(long)"""
        return int._wrap(_IOCQRingOffsets.nflags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.nring_entries(long)"""
        return int._wrap(_IOCQRingOffsets.nring_entries(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncqes(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.ncqes(long,int)"""
        _IOCQRingOffsets.ncqes(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nresv1(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.nresv1(long)"""
        return int._wrap(_IOCQRingOffsets.nresv1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nflags(long,int)"""
        _IOCQRingOffsets.nflags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.ring_mask()"""
        return int._wrap(super(IOCQRingOffsets, self).ring_mask())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def ntail(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.ntail(long,int)"""
        _IOCQRingOffsets.ntail(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def flags(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.flags(int)"""
        return 'IOCQRingOffsets'._wrap(super(_IOCQRingOffsets, self).flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.malloc(int)"""
        return Buffer._wrap(_IOCQRingOffsets.malloc(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOCQRingOffsets') -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.set(org.lwjgl.system.linux.liburing.IOCQRingOffsets)"""
        return 'IOCQRingOffsets'._wrap(super(_IOCQRingOffsets, self).set(arg0))

    @staticmethod
    @overload
    def noverflow(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.noverflow(long)"""
        return int._wrap(_IOCQRingOffsets.noverflow(_long.valueOf(arg0)))

    @overload
    def tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.tail()"""
        return int._wrap(super(IOCQRingOffsets, self).tail())

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nresv2(long,long)"""
        _IOCQRingOffsets.nresv2(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def malloc() -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.malloc()"""
        return IOCQRingOffsets._wrap(_IOCQRingOffsets.malloc())

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
    def nring_mask(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.nring_mask(long)"""
        return int._wrap(_IOCQRingOffsets.nring_mask(_long.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.sizeof()"""
        return int._wrap(super(IOCQRingOffsets, self).sizeof())

    @staticmethod
    @overload
    def create() -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.create()"""
        return IOCQRingOffsets._wrap(_IOCQRingOffsets.create())

    @overload
    def tail(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.tail(int)"""
        return 'IOCQRingOffsets'._wrap(super(_IOCQRingOffsets, self).tail(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nhead(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.nhead(long)"""
        return int._wrap(_IOCQRingOffsets.nhead(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ntail(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.ntail(long)"""
        return int._wrap(_IOCQRingOffsets.ntail(_long.valueOf(arg0)))

    @overload
    def head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.head()"""
        return int._wrap(super(IOCQRingOffsets, self).head())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nring_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nring_entries(long,int)"""
        _IOCQRingOffsets.nring_entries(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nhead(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nhead(long,int)"""
        _IOCQRingOffsets.nhead(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.createSafe(long,int)"""
        return Buffer._wrap(_IOCQRingOffsets.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.calloc(int)"""
        return Buffer._wrap(_IOCQRingOffsets.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.malloc(org.lwjgl.system.MemoryStack)"""
        return IOCQRingOffsets._wrap(_IOCQRingOffsets.malloc(arg0))

    @overload
    def cqes(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.cqes(int)"""
        return 'IOCQRingOffsets'._wrap(super(_IOCQRingOffsets, self).cqes(_int.valueOf(arg0)))

    @overload
    def ring_mask(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.ring_mask(int)"""
        return 'IOCQRingOffsets'._wrap(super(_IOCQRingOffsets, self).ring_mask(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.createSafe(long)"""
        return IOCQRingOffsets._wrap(_IOCQRingOffsets.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def noverflow(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.noverflow(long,int)"""
        _IOCQRingOffsets.noverflow(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOCQRingOffsets.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc() -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.calloc()"""
        return IOCQRingOffsets._wrap(_IOCQRingOffsets.calloc())

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.ring_entries()"""
        return int._wrap(super(IOCQRingOffsets, self).ring_entries())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.set(int,int,int,int,int,int,int)"""
        return 'IOCQRingOffsets'._wrap(super(_IOCQRingOffsets, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.calloc(org.lwjgl.system.MemoryStack)"""
        return IOCQRingOffsets._wrap(_IOCQRingOffsets.calloc(arg0))

    @staticmethod
    @overload
    def nresv1(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nresv1(long,int)"""
        _IOCQRingOffsets.nresv1(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets(java.nio.ByteBuffer)"""
        val = _IOCQRingOffsets(arg0)
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

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.flags()"""
        return int._wrap(super(IOCQRingOffsets, self).flags())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOCQRingOffsets.malloc(_int.valueOf(arg0), arg1))

    @overload
    def cqes(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets.cqes()"""
        return int._wrap(super(IOCQRingOffsets, self).cqes())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def ring_entries(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.ring_entries(int)"""
        return 'IOCQRingOffsets'._wrap(super(_IOCQRingOffsets, self).ring_entries(_int.valueOf(arg0)))

    @overload
    def overflow(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.overflow(int)"""
        return 'IOCQRingOffsets'._wrap(super(_IOCQRingOffsets, self).overflow(_int.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOCQRingOffsets.nresv2(long)"""
        return int._wrap(_IOCQRingOffsets.nresv2(_long.valueOf(arg0)))

    @overload
    def head(self, arg0: int) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOCQRingOffsets.head(int)"""
        return 'IOCQRingOffsets'._wrap(super(_IOCQRingOffsets, self).head(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_mask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOCQRingOffsets.nring_mask(long,int)"""
        _IOCQRingOffsets.nring_mask(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def ncqes(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOCQRingOffsets.ncqes(long)"""
        return int._wrap(_IOCQRingOffsets.ncqes(_long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRestriction
from pyquantum_helper import import_once as _import_once
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
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import org.lwjgl.system.linux.liburing.IOURingRestriction as _IOURingRestriction_Buffer
_Buffer = _IOURingRestriction_Buffer.Buffer
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Integer as _int
import java.lang.Byte as _byte
import org.lwjgl.system.linux.liburing.IOURingRestriction as _IOURingRestriction
_IOURingRestriction = _IOURingRestriction
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
 
class IOURingRestriction():
    """org.lwjgl.system.linux.liburing.IOURingRestriction"""
 
    @staticmethod
    def _wrap(java_value: _IOURingRestriction) -> 'IOURingRestriction':
        return IOURingRestriction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingRestriction):
        """
        Dynamic initializer for IOURingRestriction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingRestriction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingRestriction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc() -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.malloc()"""
        return IOURingRestriction._wrap(_IOURingRestriction.malloc())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nresv2(long,int,int)"""
        _IOURingRestriction.nresv2(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def sqe_flags(self, arg0: int) -> 'IOURingRestriction':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.sqe_flags(byte)"""
        return 'IOURingRestriction'._wrap(super(_IOURingRestriction, self).sqe_flags(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRestriction.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRestriction.nresv2(long,int)"""
        return int._wrap(_IOURingRestriction.nresv2(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.create(long,int)"""
        return Buffer._wrap(_IOURingRestriction.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create() -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.create()"""
        return IOURingRestriction._wrap(_IOURingRestriction.create())

    @staticmethod
    @overload
    def nsqe_flags(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingRestriction.nsqe_flags(long)"""
        return int._wrap(_IOURingRestriction.nsqe_flags(_long.valueOf(arg0)))

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
    def calloc() -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.calloc()"""
        return IOURingRestriction._wrap(_IOURingRestriction.calloc())

    @overload
    def set(self, arg0: 'IOURingRestriction') -> 'IOURingRestriction':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.set(org.lwjgl.system.linux.liburing.IOURingRestriction)"""
        return 'IOURingRestriction'._wrap(super(_IOURingRestriction, self).set(arg0))

    @staticmethod
    @overload
    def nregister_op(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingRestriction.nregister_op(long)"""
        return int._wrap(_IOURingRestriction.nregister_op(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRestriction._wrap(_IOURingRestriction.malloc(arg0))

    @staticmethod
    @overload
    def nsqe_op(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingRestriction.nsqe_op(long)"""
        return int._wrap(_IOURingRestriction.nsqe_op(_long.valueOf(arg0)))

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
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.calloc(int)"""
        return Buffer._wrap(_IOURingRestriction.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRestriction.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nopcode(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nopcode(long,short)"""
        _IOURingRestriction.nopcode(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def nregister_op(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nregister_op(long,byte)"""
        _IOURingRestriction.nregister_op(_long.valueOf(arg0), _byte.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRestriction._wrap(_IOURingRestriction.calloc(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRestriction(java.nio.ByteBuffer)"""
        val = _IOURingRestriction(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def sqe_flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction.sqe_flags()"""
        return int._wrap(super(IOURingRestriction, self).sqe_flags())

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nresv2(long,java.nio.IntBuffer)"""
        _IOURingRestriction.nresv2(_long.valueOf(arg0), arg1)

    @overload
    def register_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction.register_op()"""
        return int._wrap(super(IOURingRestriction, self).register_op())

    @staticmethod
    @overload
    def nsqe_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nsqe_flags(long,byte)"""
        _IOURingRestriction.nsqe_flags(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingRestriction.nresv(long)"""
        return int._wrap(_IOURingRestriction.nresv(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nopcode(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingRestriction.nopcode(long)"""
        return int._wrap(_IOURingRestriction.nopcode(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsqe_op(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nsqe_op(long,byte)"""
        _IOURingRestriction.nsqe_op(_long.valueOf(arg0), _byte.valueOf(arg1))

    @overload
    def register_op(self, arg0: int) -> 'IOURingRestriction':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.register_op(byte)"""
        return 'IOURingRestriction'._wrap(super(_IOURingRestriction, self).register_op(_byte.valueOf(arg0)))

    @overload
    def sqe_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction.sqe_op()"""
        return int._wrap(super(IOURingRestriction, self).sqe_op())

    @overload
    def opcode(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingRestriction.opcode()"""
        return int._wrap(super(IOURingRestriction, self).opcode())

    @overload
    def opcode(self, arg0: int) -> 'IOURingRestriction':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.opcode(short)"""
        return 'IOURingRestriction'._wrap(super(_IOURingRestriction, self).opcode(_short.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRestriction.sizeof()"""
        return int._wrap(super(IOURingRestriction, self).sizeof())

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.create(long)"""
        return IOURingRestriction._wrap(_IOURingRestriction.create(_long.valueOf(arg0)))

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
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.createSafe(long,int)"""
        return Buffer._wrap(_IOURingRestriction.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def sqe_op(self, arg0: int) -> 'IOURingRestriction':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.sqe_op(byte)"""
        return 'IOURingRestriction'._wrap(super(_IOURingRestriction, self).sqe_op(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.create(int)"""
        return Buffer._wrap(_IOURingRestriction.create(_int.valueOf(arg0)))

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
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction.malloc(int)"""
        return Buffer._wrap(_IOURingRestriction.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRestriction.nresv(long,byte)"""
        _IOURingRestriction.nresv(_long.valueOf(arg0), _byte.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingRestriction':
        """public static org.lwjgl.system.linux.liburing.IOURingRestriction org.lwjgl.system.linux.liburing.IOURingRestriction.createSafe(long)"""
        return IOURingRestriction._wrap(_IOURingRestriction.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingRestriction.nresv2(long)"""
        return IntBuffer._wrap(_IOURingRestriction.nresv2(_long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.LibURing
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.linux.liburing.LibURing as _LibURing
_LibURing = _LibURing
try:
    from pyglsystem import linux
except ImportError:
    linux = _import_once("pyglsystem.linux")

import java.lang.Short as _short
import java.lang.Boolean as _boolean
import org.lwjgl.system.linux.liburing.IOURingRecvmsgOut as _IOURingRecvmsgOut
_IOURingRecvmsgOut = _IOURingRecvmsgOut
import org.lwjgl.system.linux.liburing.IOURingBufRing as _IOURingBufRing
_IOURingBufRing = _IOURingBufRing
from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import org.lwjgl.system.linux.CMsghdr as _CMsghdr
_CMsghdr = _CMsghdr
import java.lang.Object as _object
import java.nio.LongBuffer as LongBuffer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.linux.liburing.IOURingProbe as _IOURingProbe
_IOURingProbe = _IOURingProbe
import org.lwjgl.system.linux.liburing.IOURingSQE as _IOURingSQE
_IOURingSQE = _IOURingSQE
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibURing():
    """org.lwjgl.system.linux.liburing.LibURing"""
 
    @staticmethod
    def _wrap(java_value: _LibURing) -> 'LibURing':
        return LibURing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibURing):
        """
        Dynamic initializer for LibURing.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibURing__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibURing__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def io_uring_prep_readv(arg0: 'IOURingSQE', arg1: int, arg2: 'Buffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_readv(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.IOVec$Buffer,int)"""
        _LibURing.io_uring_prep_readv(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_close_direct(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_close_direct(long,int)"""
        _LibURing.nio_uring_prep_close_direct(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_prep_fsetxattr(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: 'ByteBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fsetxattr(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_fsetxattr(arg0, _int.valueOf(arg1), arg2, arg3, _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_fallocate(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_fallocate(long,int,int,long,long)"""
        _LibURing.nio_uring_prep_fallocate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_sendmsg_zc(arg0: 'IOURingSQE', arg1: int, arg2: 'Msghdr', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_sendmsg_zc(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Msghdr,int)"""
        _LibURing.io_uring_prep_sendmsg_zc(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_cq_eventfd_toggle(arg0: int, arg1: bool) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_cq_eventfd_toggle(long,boolean)"""
        return int._wrap(_LibURing.nio_uring_cq_eventfd_toggle(_long.valueOf(arg0), _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_shutdown(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_shutdown(long,int,int)"""
        _LibURing.nio_uring_prep_shutdown(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nio_uring_register_buf_ring(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_buf_ring(long,long,int)"""
        return int._wrap(_LibURing.nio_uring_register_buf_ring(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_cq_eventfd_enabled(arg0: 'IOURing') -> bool:
        """public static boolean org.lwjgl.system.linux.liburing.LibURing.io_uring_cq_eventfd_enabled(org.lwjgl.system.linux.liburing.IOURing)"""
        return bool._wrap(_LibURing.io_uring_cq_eventfd_enabled(arg0))

    @staticmethod
    @overload
    def nio_uring_recvmsg_cmsg_firsthdr(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_cmsg_firsthdr(long,long)"""
        return int._wrap(_LibURing.nio_uring_recvmsg_cmsg_firsthdr(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_free_probe(arg0: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_free_probe(long)"""
        _LibURing.nio_uring_free_probe(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_read_fixed(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_read_fixed(long,int,long,int,int,int)"""
        _LibURing.nio_uring_prep_read_fixed(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_fallocate(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fallocate(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,long,long)"""
        _LibURing.io_uring_prep_fallocate(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_msg_ring(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_msg_ring(long,int,int,long,int)"""
        _LibURing.nio_uring_prep_msg_ring(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_cancel_fd(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_cancel_fd(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        _LibURing.io_uring_prep_cancel_fd(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_prep_files_update(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_files_update(long,long,int,int)"""
        _LibURing.nio_uring_prep_files_update(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_enter2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_enter2(int,int,int,int,long,long)"""
        return int._wrap(_LibURing.io_uring_enter2(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def io_uring_unregister_buffers(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_buffers(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_unregister_buffers(arg0))

    @staticmethod
    @overload
    def io_uring_register_iowq_max_workers(arg0: 'IOURing', arg1: 'IntBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_iowq_max_workers(org.lwjgl.system.linux.liburing.IOURing,java.nio.IntBuffer)"""
        return int._wrap(_LibURing.io_uring_register_iowq_max_workers(arg0, arg1))

    @staticmethod
    @overload
    def nio_uring_mlock_size_params(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_mlock_size_params(int,long)"""
        return int._wrap(_LibURing.nio_uring_mlock_size_params(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_sqe_set_data64(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_sqe_set_data64(long,long)"""
        _LibURing.nio_uring_sqe_set_data64(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_prep_renameat(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int, arg4: 'CharSequence', arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_renameat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int,java.lang.CharSequence,int)"""
        _LibURing.io_uring_prep_renameat(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), arg4, _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_major_version() -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.io_uring_major_version()"""
        return int._wrap(_LibURing.io_uring_major_version())

    @staticmethod
    @overload
    def io_uring_prep_send(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_send(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_send(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_sync_file_range(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_sync_file_range(long,int,int,int,int)"""
        _LibURing.nio_uring_prep_sync_file_range(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_unregister_buf_ring(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_buf_ring(long,int)"""
        return int._wrap(_LibURing.nio_uring_unregister_buf_ring(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_link(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_link(long,long,long,int)"""
        _LibURing.nio_uring_prep_link(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_cancel_fd(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_cancel_fd(long,int,int)"""
        _LibURing.nio_uring_prep_cancel_fd(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_sqe_set_data(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_sqe_set_data(long,long)"""
        _LibURing.nio_uring_sqe_set_data(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_prep_write(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_write(long,int,long,int,int)"""
        _LibURing.nio_uring_prep_write(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_socket(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_socket(long,int,int,int,int)"""
        _LibURing.nio_uring_prep_socket(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_openat2_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: 'OpenHow', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat2_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,org.lwjgl.system.linux.OpenHow,int)"""
        _LibURing.io_uring_prep_openat2_direct(arg0, _int.valueOf(arg1), arg2, arg3, _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_msg_ring_fd_alloc(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_msg_ring_fd_alloc(long,int,int,long,int)"""
        _LibURing.nio_uring_prep_msg_ring_fd_alloc(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_buf_ring_init(arg0: 'IOURingBufRing'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_buf_ring_init(org.lwjgl.system.linux.liburing.IOURingBufRing)"""
        _LibURing.io_uring_buf_ring_init(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def io_uring_prep_fsync(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fsync(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        _LibURing.io_uring_prep_fsync(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_buf_ring_mask(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_buf_ring_mask(int)"""
        return int._wrap(_LibURing.io_uring_buf_ring_mask(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_linkat(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: 'ByteBuffer', arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_linkat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_linkat(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), arg4, _int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_prep_write_fixed(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_write_fixed(long,int,long,int,int,int)"""
        _LibURing.nio_uring_prep_write_fixed(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_openat2(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: 'OpenHow'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat2(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,org.lwjgl.system.linux.OpenHow)"""
        _LibURing.io_uring_prep_openat2(arg0, _int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def nio_uring_prep_timeout_remove(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_timeout_remove(long,long,int)"""
        _LibURing.nio_uring_prep_timeout_remove(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_send_set_addr(arg0: 'IOURingSQE', arg1: 'Sockaddr', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_send_set_addr(org.lwjgl.system.linux.liburing.IOURingSQE,org.lwjgl.system.linux.Sockaddr,short)"""
        _LibURing.io_uring_prep_send_set_addr(arg0, arg1, _short.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_recv(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_recv(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_recv(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def io_uring_cq_has_overflow(arg0: 'IOURing') -> bool:
        """public static boolean org.lwjgl.system.linux.liburing.LibURing.io_uring_cq_has_overflow(org.lwjgl.system.linux.liburing.IOURing)"""
        return bool._wrap(_LibURing.io_uring_cq_has_overflow(arg0))

    @staticmethod
    @overload
    def io_uring_sqe_set_flags(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_sqe_set_flags(org.lwjgl.system.linux.liburing.IOURingSQE,int)"""
        _LibURing.io_uring_sqe_set_flags(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_prep_poll_remove(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_poll_remove(long,long)"""
        _LibURing.nio_uring_prep_poll_remove(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_prep_recv(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_recv(long,int,long,long,int)"""
        _LibURing.nio_uring_prep_recv(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_register_restrictions(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_restrictions(long,long,int)"""
        return int._wrap(_LibURing.nio_uring_register_restrictions(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_prep_socket_direct(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_socket_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,int,int)"""
        _LibURing.io_uring_prep_socket_direct(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_fsetxattr(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: 'ByteBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fsetxattr(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_fsetxattr(arg0, _int.valueOf(arg1), arg2, arg3, _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_register_probe(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_probe(long,long,int)"""
        return int._wrap(_LibURing.nio_uring_register_probe(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_prep_readv2(arg0: 'IOURingSQE', arg1: int, arg2: 'Buffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_readv2(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.IOVec$Buffer,int,int)"""
        _LibURing.io_uring_prep_readv2(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_send_zc(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_send_zc(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int)"""
        _LibURing.io_uring_prep_send_zc(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_getxattr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_getxattr(long,long,long,long,int)"""
        _LibURing.nio_uring_prep_getxattr(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_close_ring_fd(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_close_ring_fd(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_close_ring_fd(arg0))

    @staticmethod
    @overload
    def nio_uring_submit_and_get_events(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_submit_and_get_events(long)"""
        return int._wrap(_LibURing.nio_uring_submit_and_get_events(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_setup_buf_ring(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_setup_buf_ring(long,int,int,int,long)"""
        return int._wrap(_LibURing.nio_uring_setup_buf_ring(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def io_uring_unregister_personality(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_personality(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int._wrap(_LibURing.io_uring_unregister_personality(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_prep_poll_remove(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_poll_remove(org.lwjgl.system.linux.liburing.IOURingSQE,long)"""
        _LibURing.io_uring_prep_poll_remove(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_register_buf_ring(arg0: 'IOURing', arg1: 'IOURingBufReg', arg2: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_buf_ring(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingBufReg,int)"""
        return int._wrap(_LibURing.io_uring_register_buf_ring(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_cqe_get_data(arg0: 'IOURingCQE') -> int:
        """public static long org.lwjgl.system.linux.liburing.LibURing.io_uring_cqe_get_data(org.lwjgl.system.linux.liburing.IOURingCQE)"""
        return int._wrap(_LibURing.io_uring_cqe_get_data(arg0))

    @staticmethod
    @overload
    def io_uring_prep_openat_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int,int,int)"""
        _LibURing.io_uring_prep_openat_direct(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_register_files(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_files(long,long,int)"""
        return int._wrap(_LibURing.nio_uring_register_files(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_queue_mmap(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_queue_mmap(int,long,long)"""
        return int._wrap(_LibURing.nio_uring_queue_mmap(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_prep_read(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_read(long,int,long,int,int)"""
        _LibURing.nio_uring_prep_read(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_cqe_get_data64(arg0: 'IOURingCQE') -> int:
        """public static long org.lwjgl.system.linux.liburing.LibURing.io_uring_cqe_get_data64(org.lwjgl.system.linux.liburing.IOURingCQE)"""
        return int._wrap(_LibURing.io_uring_cqe_get_data64(arg0))

    @staticmethod
    @overload
    def io_uring_prep_rename(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_rename(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        _LibURing.io_uring_prep_rename(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_prep_files_update(arg0: 'IOURingSQE', arg1: 'IntBuffer', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_files_update(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.IntBuffer,int)"""
        _LibURing.io_uring_prep_files_update(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_openat2(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: 'OpenHow'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat2(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,org.lwjgl.system.linux.OpenHow)"""
        _LibURing.io_uring_prep_openat2(arg0, _int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def io_uring_register_files_update(arg0: 'IOURing', arg1: int, arg2: 'IntBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_files_update(org.lwjgl.system.linux.liburing.IOURing,int,java.nio.IntBuffer)"""
        return int._wrap(_LibURing.io_uring_register_files_update(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nio_uring_prep_send_set_addr(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_send_set_addr(long,long,short)"""
        _LibURing.nio_uring_prep_send_set_addr(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_prep_openat2(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_openat2(long,int,long,long)"""
        _LibURing.nio_uring_prep_openat2(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_wait_cqe_nr(arg0: 'IOURing', arg1: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_wait_cqe_nr(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer)"""
        return int._wrap(_LibURing.io_uring_wait_cqe_nr(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_register_ring_fd(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_ring_fd(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_register_ring_fd(arg0))

    @staticmethod
    @overload
    def io_uring_prep_openat2_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: 'OpenHow', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat2_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,org.lwjgl.system.linux.OpenHow,int)"""
        _LibURing.io_uring_prep_openat2_direct(arg0, _int.valueOf(arg1), arg2, arg3, _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_queue_exit(arg0: 'IOURing'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_queue_exit(org.lwjgl.system.linux.liburing.IOURing)"""
        _LibURing.io_uring_queue_exit(arg0)

    @staticmethod
    @overload
    def nio_uring_enter2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_enter2(int,int,int,int,long,long)"""
        return int._wrap(_LibURing.nio_uring_enter2(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def io_uring_prep_openat(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int,int)"""
        _LibURing.io_uring_prep_openat(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_unregister_buffers(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_buffers(long)"""
        return int._wrap(_LibURing.nio_uring_unregister_buffers(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_ring_dontfork(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_ring_dontfork(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_ring_dontfork(arg0))

    @staticmethod
    @overload
    def io_uring_prep_link_timeout(arg0: 'IOURingSQE', arg1: 'KernelTimespec', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_link_timeout(org.lwjgl.system.linux.liburing.IOURingSQE,org.lwjgl.system.linux.KernelTimespec,int)"""
        _LibURing.io_uring_prep_link_timeout(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_register_buffers_update_tag(arg0: 'IOURing', arg1: int, arg2: 'Buffer', arg3: 'LongBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_buffers_update_tag(org.lwjgl.system.linux.liburing.IOURing,int,org.lwjgl.system.linux.IOVec$Buffer,java.nio.LongBuffer)"""
        return int._wrap(_LibURing.io_uring_register_buffers_update_tag(arg0, _int.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def io_uring_free_probe(arg0: 'IOURingProbe'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_free_probe(org.lwjgl.system.linux.liburing.IOURingProbe)"""
        _LibURing.io_uring_free_probe(arg0)

    @staticmethod
    @overload
    def nio_uring_prep_multishot_accept_direct(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_multishot_accept_direct(long,int,long,long,int)"""
        _LibURing.nio_uring_prep_multishot_accept_direct(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_poll_multishot(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_poll_multishot(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        _LibURing.io_uring_prep_poll_multishot(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_queue_exit(arg0: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_queue_exit(long)"""
        _LibURing.nio_uring_queue_exit(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_openat_direct(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_openat_direct(long,int,long,int,int,int)"""
        _LibURing.nio_uring_prep_openat_direct(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_register(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.io_uring_register(int,int,long,int)"""
        return int._wrap(_LibURing.io_uring_register(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

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
    def nio_uring_prep_openat2_direct(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_openat2_direct(long,int,long,long,int)"""
        _LibURing.nio_uring_prep_openat2_direct(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_poll_update(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_poll_update(long,long,long,int,int)"""
        _LibURing.nio_uring_prep_poll_update(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_msg_ring(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_msg_ring(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,long,int)"""
        _LibURing.io_uring_prep_msg_ring(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_unregister_files(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_files(long)"""
        return int._wrap(_LibURing.nio_uring_unregister_files(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_unregister_iowq_aff(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_iowq_aff(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_unregister_iowq_aff(arg0))

    @staticmethod
    @overload
    def io_uring_free_buf_ring(arg0: 'IOURing', arg1: 'IOURingBufRing', arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_free_buf_ring(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingBufRing,int,int)"""
        return int._wrap(_LibURing.io_uring_free_buf_ring(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def io_uring_queue_init(arg0: int, arg1: 'IOURing', arg2: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_queue_init(int,org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int._wrap(_LibURing.io_uring_queue_init(_int.valueOf(arg0), arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_setup_buf_ring(arg0: 'IOURing', arg1: int, arg2: int, arg3: int, arg4: 'IntBuffer') -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.LibURing.io_uring_setup_buf_ring(org.lwjgl.system.linux.liburing.IOURing,int,int,int,java.nio.IntBuffer)"""
        return IOURingBufRing._wrap(_LibURing.io_uring_setup_buf_ring(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def io_uring_wait_cqe_timeout(arg0: 'IOURing', arg1: 'PointerBuffer', arg2: 'KernelTimespec') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_wait_cqe_timeout(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer,org.lwjgl.system.linux.KernelTimespec)"""
        return int._wrap(_LibURing.io_uring_wait_cqe_timeout(arg0, arg1, arg2))

    @staticmethod
    @overload
    def io_uring_register_personality(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_personality(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_register_personality(arg0))

    @staticmethod
    @overload
    def io_uring_prep_fgetxattr(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fgetxattr(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,java.nio.ByteBuffer)"""
        _LibURing.io_uring_prep_fgetxattr(arg0, _int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def io_uring_prep_openat_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int,int)"""
        _LibURing.io_uring_prep_openat_direct(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_unlink(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_unlink(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,int)"""
        _LibURing.io_uring_prep_unlink(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_prep_fgetxattr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_fgetxattr(long,int,long,long,int)"""
        _LibURing.nio_uring_prep_fgetxattr(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_linkat(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_linkat(long,int,long,int,long,int)"""
        _LibURing.nio_uring_prep_linkat(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_prep_rename(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_rename(long,long,long)"""
        _LibURing.nio_uring_prep_rename(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_submit(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_submit(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_submit(arg0))

    @staticmethod
    @overload
    def nio_uring_wait_cqes(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_wait_cqes(long,long,int,long,long)"""
        return int._wrap(_LibURing.nio_uring_wait_cqes(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def io_uring_prep_close_direct(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_close_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int)"""
        _LibURing.io_uring_prep_close_direct(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_register_buffers(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_buffers(long,long,int)"""
        return int._wrap(_LibURing.nio_uring_register_buffers(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_register_buffers(arg0: 'IOURing', arg1: 'Buffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_buffers(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.IOVec$Buffer)"""
        return int._wrap(_LibURing.io_uring_register_buffers(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_openat(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_openat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int)"""
        _LibURing.io_uring_prep_openat(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_close(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_close(long,int)"""
        _LibURing.nio_uring_prep_close(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_register_sync_cancel(arg0: 'IOURing', arg1: 'IOURingSyncCancelReg') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_sync_cancel(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingSyncCancelReg)"""
        return int._wrap(_LibURing.io_uring_register_sync_cancel(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_writev2(arg0: 'IOURingSQE', arg1: int, arg2: 'Buffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_writev2(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.IOVec$Buffer,int,int)"""
        _LibURing.io_uring_prep_writev2(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_remove_buffers(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_remove_buffers(long,int,int)"""
        _LibURing.nio_uring_prep_remove_buffers(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_register_iowq_aff(arg0: 'IOURing', arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_iowq_aff(org.lwjgl.system.linux.liburing.IOURing,long,long)"""
        return int._wrap(_LibURing.io_uring_register_iowq_aff(arg0, _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_recvmsg_name(arg0: 'IOURingRecvmsgOut') -> int:
        """public static long org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_name(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut)"""
        return int._wrap(_LibURing.io_uring_recvmsg_name(arg0))

    @staticmethod
    @overload
    def nio_uring_register_eventfd_async(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_eventfd_async(long,int)"""
        return int._wrap(_LibURing.nio_uring_register_eventfd_async(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_recvmsg_multishot(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_recvmsg_multishot(long,int,long,int)"""
        _LibURing.nio_uring_prep_recvmsg_multishot(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_multishot_accept(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_multishot_accept(long,int,long,long,int)"""
        _LibURing.nio_uring_prep_multishot_accept(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_queue_mmap(arg0: int, arg1: 'IOURingParams', arg2: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_queue_mmap(int,org.lwjgl.system.linux.liburing.IOURingParams,org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_queue_mmap(_int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def io_uring_submit_and_wait(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_submit_and_wait(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int._wrap(_LibURing.io_uring_submit_and_wait(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_prep_splice(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_splice(org.lwjgl.system.linux.liburing.IOURingSQE,int,long,int,long,int,int)"""
        _LibURing.io_uring_prep_splice(arg0, _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @staticmethod
    @overload
    def io_uring_prep_multishot_accept_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'Sockaddr', arg3: 'IntBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_multishot_accept_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Sockaddr,java.nio.IntBuffer,int)"""
        _LibURing.io_uring_prep_multishot_accept_direct(arg0, _int.valueOf(arg1), arg2, arg3, _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_write(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_write(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_write(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_unregister_eventfd(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_eventfd(long)"""
        return int._wrap(_LibURing.nio_uring_unregister_eventfd(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_unregister_buf_ring(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_buf_ring(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int._wrap(_LibURing.io_uring_unregister_buf_ring(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_recvmsg_payload(arg0: 'IOURingRecvmsgOut', arg1: 'Msghdr') -> int:
        """public static long org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_payload(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut,org.lwjgl.system.linux.Msghdr)"""
        return int._wrap(_LibURing.io_uring_recvmsg_payload(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_mlock_size_params(arg0: int, arg1: 'IOURingParams') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_mlock_size_params(int,org.lwjgl.system.linux.liburing.IOURingParams)"""
        return int._wrap(_LibURing.io_uring_mlock_size_params(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def io_uring_prep_read(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_read(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_read(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_buf_ring_cq_advance(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_buf_ring_cq_advance(long,long,int)"""
        _LibURing.nio_uring_buf_ring_cq_advance(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_prep_setxattr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_setxattr(long,long,long,long,int,int)"""
        _LibURing.nio_uring_prep_setxattr(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_queue_init_params(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_queue_init_params(int,long,long)"""
        return int._wrap(_LibURing.nio_uring_queue_init_params(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_prep_socket_direct_alloc(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_socket_direct_alloc(long,int,int,int,int)"""
        _LibURing.nio_uring_prep_socket_direct_alloc(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_readv2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_readv2(long,int,long,int,int,int)"""
        _LibURing.nio_uring_prep_readv2(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_sendmsg(arg0: 'IOURingSQE', arg1: int, arg2: 'Msghdr', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_sendmsg(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Msghdr,int)"""
        _LibURing.io_uring_prep_sendmsg(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_register_buffers_tags(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_buffers_tags(long,long,long,int)"""
        return int._wrap(_LibURing.nio_uring_register_buffers_tags(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nio_uring_recvmsg_payload(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_payload(long,long)"""
        return int._wrap(_LibURing.nio_uring_recvmsg_payload(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_sqe_set_data(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_sqe_set_data(org.lwjgl.system.linux.liburing.IOURingSQE,long)"""
        _LibURing.io_uring_sqe_set_data(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_prep_sendmsg_zc(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_sendmsg_zc(long,int,long,int)"""
        _LibURing.nio_uring_prep_sendmsg_zc(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_unregister_eventfd(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_eventfd(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_unregister_eventfd(arg0))

    @staticmethod
    @overload
    def io_uring_register_files_tags(arg0: 'IOURing', arg1: 'IntBuffer', arg2: 'LongBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_files_tags(org.lwjgl.system.linux.liburing.IOURing,java.nio.IntBuffer,java.nio.LongBuffer)"""
        return int._wrap(_LibURing.io_uring_register_files_tags(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nio_uring_prep_recv_multishot(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_recv_multishot(long,int,long,long,int)"""
        _LibURing.nio_uring_prep_recv_multishot(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_wait_cqes(arg0: 'IOURing', arg1: 'PointerBuffer', arg2: 'KernelTimespec', arg3: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_wait_cqes(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer,org.lwjgl.system.linux.KernelTimespec,long)"""
        return int._wrap(_LibURing.io_uring_wait_cqes(arg0, arg1, arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def io_uring_queue_init_params(arg0: int, arg1: 'IOURing', arg2: 'IOURingParams') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_queue_init_params(int,org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingParams)"""
        return int._wrap(_LibURing.io_uring_queue_init_params(_int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def io_uring_prep_unlinkat(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_unlinkat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_unlinkat(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_cq_has_overflow(arg0: int) -> bool:
        """public static native boolean org.lwjgl.system.linux.liburing.LibURing.nio_uring_cq_has_overflow(long)"""
        return bool._wrap(_LibURing.nio_uring_cq_has_overflow(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_tee(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_tee(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,int)"""
        _LibURing.io_uring_prep_tee(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_sync_file_range(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_sync_file_range(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,int)"""
        _LibURing.io_uring_prep_sync_file_range(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_get_probe() -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_get_probe()"""
        return int._wrap(_LibURing.nio_uring_get_probe())

    @staticmethod
    @overload
    def io_uring_prep_symlinkat(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: int, arg3: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_symlinkat(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,int,java.nio.ByteBuffer)"""
        _LibURing.io_uring_prep_symlinkat(arg0, arg1, _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nio_uring_setup(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_setup(int,long)"""
        return int._wrap(_LibURing.nio_uring_setup(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_recvmsg_payload_length(arg0: 'IOURingRecvmsgOut', arg1: int, arg2: 'Msghdr') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_payload_length(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut,int,org.lwjgl.system.linux.Msghdr)"""
        return int._wrap(_LibURing.io_uring_recvmsg_payload_length(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nio_uring_close_ring_fd(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_close_ring_fd(long)"""
        return int._wrap(_LibURing.nio_uring_close_ring_fd(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_close(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_close(org.lwjgl.system.linux.liburing.IOURingSQE,int)"""
        _LibURing.io_uring_prep_close(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_prep_unlinkat(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_unlinkat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int)"""
        _LibURing.io_uring_prep_unlinkat(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_setxattr(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: 'ByteBuffer', arg3: 'CharSequence', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_setxattr(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,java.nio.ByteBuffer,java.lang.CharSequence,int)"""
        _LibURing.io_uring_prep_setxattr(arg0, arg1, arg2, arg3, _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_get_sqe(arg0: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_get_sqe(long)"""
        return int._wrap(_LibURing.nio_uring_get_sqe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_peek_batch_cqe(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_peek_batch_cqe(long,long,int)"""
        return int._wrap(_LibURing.nio_uring_peek_batch_cqe(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_wait_cqe(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_wait_cqe(long,long)"""
        return int._wrap(_LibURing.nio_uring_wait_cqe(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_prep_linkat(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int, arg4: 'CharSequence', arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_linkat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int,java.lang.CharSequence,int)"""
        _LibURing.io_uring_prep_linkat(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), arg4, _int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_peek_cqe(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_peek_cqe(long,long)"""
        return int._wrap(_LibURing.nio_uring_peek_cqe(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_sqring_wait(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_sqring_wait(long)"""
        return int._wrap(_LibURing.nio_uring_sqring_wait(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_recvmsg_multishot(arg0: 'IOURingSQE', arg1: int, arg2: 'Msghdr', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_recvmsg_multishot(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Msghdr,int)"""
        _LibURing.io_uring_prep_recvmsg_multishot(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_fadvise(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fadvise(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,long,int)"""
        _LibURing.io_uring_prep_fadvise(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_register_eventfd(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_eventfd(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int._wrap(_LibURing.io_uring_register_eventfd(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_writev2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_writev2(long,int,long,int,int,int)"""
        _LibURing.nio_uring_prep_writev2(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_register_files_sparse(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_files_sparse(long,int)"""
        return int._wrap(_LibURing.nio_uring_register_files_sparse(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_check_version(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.linux.liburing.LibURing.io_uring_check_version(int,int)"""
        return bool._wrap(_LibURing.io_uring_check_version(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_readv(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_readv(long,int,long,int,int)"""
        _LibURing.nio_uring_prep_readv(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_cq_ready(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_cq_ready(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_cq_ready(arg0))

    @staticmethod
    @overload
    def nio_uring_register_eventfd(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_eventfd(long,int)"""
        return int._wrap(_LibURing.nio_uring_register_eventfd(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_prep_mkdir(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_mkdir(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,int)"""
        _LibURing.io_uring_prep_mkdir(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_register_files_update_tag(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_files_update_tag(long,int,long,long,int)"""
        return int._wrap(_LibURing.nio_uring_register_files_update_tag(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nio_uring_prep_mkdirat(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_mkdirat(long,int,long,int)"""
        _LibURing.nio_uring_prep_mkdirat(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_writev(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_writev(long,int,long,int,int)"""
        _LibURing.nio_uring_prep_writev(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_socket_direct(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_socket_direct(long,int,int,int,int,int)"""
        _LibURing.nio_uring_prep_socket_direct(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_get_events(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_get_events(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_get_events(arg0))

    @staticmethod
    @overload
    def io_uring_register_file_alloc_range(arg0: 'IOURing', arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_file_alloc_range(org.lwjgl.system.linux.liburing.IOURing,int,int)"""
        return int._wrap(_LibURing.io_uring_register_file_alloc_range(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_free_buf_ring(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_free_buf_ring(long,long,int,int)"""
        return int._wrap(_LibURing.nio_uring_free_buf_ring(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def io_uring_sqe_set_data64(arg0: 'IOURingSQE', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_sqe_set_data64(org.lwjgl.system.linux.liburing.IOURingSQE,long)"""
        _LibURing.io_uring_sqe_set_data64(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_recvmsg_validate(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_validate(long,int,long)"""
        return int._wrap(_LibURing.nio_uring_recvmsg_validate(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def __io_uring_sqring_wait(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.__io_uring_sqring_wait(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.__io_uring_sqring_wait(arg0))

    @staticmethod
    @overload
    def nio_uring_recvmsg_cmsg_nexthdr(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_cmsg_nexthdr(long,long,long)"""
        return int._wrap(_LibURing.nio_uring_recvmsg_cmsg_nexthdr(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_prep_read_fixed(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_read_fixed(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int)"""
        _LibURing.io_uring_prep_read_fixed(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_recvmsg_name(arg0: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_name(long)"""
        return int._wrap(_LibURing.nio_uring_recvmsg_name(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_register_files_sparse(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_files_sparse(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int._wrap(_LibURing.io_uring_register_files_sparse(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_prep_getxattr(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: 'ByteBuffer', arg3: 'CharSequence'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_getxattr(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,java.nio.ByteBuffer,java.lang.CharSequence)"""
        _LibURing.io_uring_prep_getxattr(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def nio_uring_sq_ready(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_sq_ready(long)"""
        return int._wrap(_LibURing.nio_uring_sq_ready(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_cqe_get_data64(arg0: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_cqe_get_data64(long)"""
        return int._wrap(_LibURing.nio_uring_cqe_get_data64(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_prep_sendmsg(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_sendmsg(long,int,long,int)"""
        _LibURing.nio_uring_prep_sendmsg(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_shutdown(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_shutdown(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        _LibURing.io_uring_prep_shutdown(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_symlink(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: 'CharSequence'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_symlink(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,java.lang.CharSequence)"""
        _LibURing.io_uring_prep_symlink(arg0, arg1, arg2)

    @staticmethod
    @overload
    def io_uring_prep_epoll_ctl(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: 'EpollEvent'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_epoll_ctl(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,org.lwjgl.system.linux.EpollEvent)"""
        _LibURing.io_uring_prep_epoll_ctl(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4)

    @staticmethod
    @overload
    def io_uring_prep_cancel(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_cancel(org.lwjgl.system.linux.liburing.IOURingSQE,long,int)"""
        _LibURing.io_uring_prep_cancel(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_socket_direct_alloc(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_socket_direct_alloc(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,int)"""
        _LibURing.io_uring_prep_socket_direct_alloc(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_ring_dontfork(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_ring_dontfork(long)"""
        return int._wrap(_LibURing.nio_uring_ring_dontfork(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_register_iowq_aff(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_iowq_aff(long,long,long)"""
        return int._wrap(_LibURing.nio_uring_register_iowq_aff(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_prep_mkdirat(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_mkdirat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_mkdirat(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_sq_space_left(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_sq_space_left(long)"""
        return int._wrap(_LibURing.nio_uring_sq_space_left(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_prep_timeout(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_timeout(long,long,int,int)"""
        _LibURing.nio_uring_prep_timeout(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_wait_cqe(arg0: 'IOURing', arg1: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_wait_cqe(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer)"""
        return int._wrap(_LibURing.io_uring_wait_cqe(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_provide_buffers(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_provide_buffers(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,int,int,int)"""
        _LibURing.io_uring_prep_provide_buffers(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_nop(arg0: 'IOURingSQE'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_nop(org.lwjgl.system.linux.liburing.IOURingSQE)"""
        _LibURing.io_uring_prep_nop(arg0)

    @staticmethod
    @overload
    def nio_uring_prep_nop(arg0: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_nop(long)"""
        _LibURing.nio_uring_prep_nop(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_unlink(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_unlink(long,long,int)"""
        _LibURing.nio_uring_prep_unlink(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_get_sqe(arg0: 'IOURing') -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.LibURing.io_uring_get_sqe(org.lwjgl.system.linux.liburing.IOURing)"""
        return IOURingSQE._wrap(_LibURing.io_uring_get_sqe(arg0))

    @staticmethod
    @overload
    def nio_uring_prep_fsync(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_fsync(long,int,int)"""
        _LibURing.nio_uring_prep_fsync(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_accept_direct(arg0: 'IOURingSQE', arg1: int, arg2: 'Sockaddr', arg3: 'IntBuffer', arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_accept_direct(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Sockaddr,java.nio.IntBuffer,int,int)"""
        _LibURing.io_uring_prep_accept_direct(arg0, _int.valueOf(arg1), arg2, arg3, _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_sq_ready(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_sq_ready(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_sq_ready(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nio_uring_prep_symlink(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_symlink(long,long,long)"""
        _LibURing.nio_uring_prep_symlink(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_register_file_alloc_range(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_file_alloc_range(long,int,int)"""
        return int._wrap(_LibURing.nio_uring_register_file_alloc_range(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_prep_link(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_link(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_link(arg0, arg1, arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_provide_buffers(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_provide_buffers(long,long,int,int,int,int)"""
        _LibURing.nio_uring_prep_provide_buffers(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_get_events(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_get_events(long)"""
        return int._wrap(_LibURing.nio_uring_get_events(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_connect(arg0: 'IOURingSQE', arg1: int, arg2: 'Sockaddr', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_connect(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Sockaddr,int)"""
        _LibURing.io_uring_prep_connect(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_cancel64(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_cancel64(long,long,int)"""
        _LibURing.nio_uring_prep_cancel64(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_register_buffers_tags(arg0: 'IOURing', arg1: 'Buffer', arg2: 'LongBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_buffers_tags(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.IOVec$Buffer,java.nio.LongBuffer)"""
        return int._wrap(_LibURing.io_uring_register_buffers_tags(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nio_uring_unregister_iowq_aff(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_iowq_aff(long)"""
        return int._wrap(_LibURing.nio_uring_unregister_iowq_aff(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_prep_recvmsg(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_recvmsg(long,int,long,int)"""
        _LibURing.nio_uring_prep_recvmsg(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_msg_ring_fd(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_msg_ring_fd(long,int,int,int,long,int)"""
        _LibURing.nio_uring_prep_msg_ring_fd(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_poll_add(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_poll_add(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        _LibURing.io_uring_prep_poll_add(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_prep_link_timeout(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_link_timeout(long,long,int)"""
        _LibURing.nio_uring_prep_link_timeout(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_write_fixed(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_write_fixed(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int)"""
        _LibURing.io_uring_prep_write_fixed(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_submit_and_get_events(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_submit_and_get_events(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_submit_and_get_events(arg0))

    @staticmethod
    @overload
    def io_uring_unregister_files(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_files(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_unregister_files(arg0))

    @staticmethod
    @overload
    def io_uring_register_buffers_sparse(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_buffers_sparse(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int._wrap(_LibURing.io_uring_register_buffers_sparse(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_unlinkat(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_unlinkat(long,int,long,int)"""
        _LibURing.nio_uring_prep_unlinkat(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_renameat(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_renameat(long,int,long,int,long,int)"""
        _LibURing.nio_uring_prep_renameat(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_symlink(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_symlink(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        _LibURing.io_uring_prep_symlink(arg0, arg1, arg2)

    @staticmethod
    @overload
    def nio_uring_cqe_seen(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_cqe_seen(long,long)"""
        _LibURing.nio_uring_cqe_seen(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_prep_poll_add(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_poll_add(long,int,int)"""
        _LibURing.nio_uring_prep_poll_add(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_accept(arg0: 'IOURingSQE', arg1: int, arg2: 'Sockaddr', arg3: 'IntBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_accept(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Sockaddr,java.nio.IntBuffer,int)"""
        _LibURing.io_uring_prep_accept(arg0, _int.valueOf(arg1), arg2, arg3, _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_wait_cqe_nr(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_wait_cqe_nr(long,long,int)"""
        return int._wrap(_LibURing.nio_uring_wait_cqe_nr(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_submit_and_wait_timeout(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_submit_and_wait_timeout(long,long,int,long,long)"""
        return int._wrap(_LibURing.nio_uring_submit_and_wait_timeout(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def io_uring_prep_writev(arg0: 'IOURingSQE', arg1: int, arg2: 'Buffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_writev(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.IOVec$Buffer,int)"""
        _LibURing.io_uring_prep_writev(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_prep_send_zc_fixed(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_send_zc_fixed(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int,int)"""
        _LibURing.io_uring_prep_send_zc_fixed(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_prep_sendto(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_sendto(long,int,long,long,int,long,int)"""
        _LibURing.nio_uring_prep_sendto(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6))

    @staticmethod
    @overload
    def io_uring_prep_statx(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int, arg5: 'Statx'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_statx(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,int,org.lwjgl.system.linux.Statx)"""
        _LibURing.io_uring_prep_statx(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), arg5)

    @staticmethod
    @overload
    def nio_uring_queue_init(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_queue_init(int,long,int)"""
        return int._wrap(_LibURing.nio_uring_queue_init(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def io_uring_enter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_enter(int,int,int,int,long)"""
        return int._wrap(_LibURing.io_uring_enter(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nio_uring_prep_timeout_update(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_timeout_update(long,long,long,int)"""
        _LibURing.nio_uring_prep_timeout_update(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_register_files_update(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_files_update(long,int,long,int)"""
        return int._wrap(_LibURing.nio_uring_register_files_update(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def io_uring_submit_and_wait_timeout(arg0: 'IOURing', arg1: 'PointerBuffer', arg2: 'KernelTimespec', arg3: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_submit_and_wait_timeout(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer,org.lwjgl.system.linux.KernelTimespec,long)"""
        return int._wrap(_LibURing.io_uring_submit_and_wait_timeout(arg0, arg1, arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def io_uring_prep_timeout_update(arg0: 'IOURingSQE', arg1: 'KernelTimespec', arg2: int, arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_timeout_update(org.lwjgl.system.linux.liburing.IOURingSQE,org.lwjgl.system.linux.KernelTimespec,long,int)"""
        _LibURing.io_uring_prep_timeout_update(arg0, arg1, _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_peek_cqe(arg0: 'IOURing', arg1: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_peek_cqe(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer)"""
        return int._wrap(_LibURing.io_uring_peek_cqe(arg0, arg1))

    @staticmethod
    @overload
    def nio_uring_sqe_set_flags(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_sqe_set_flags(long,int)"""
        _LibURing.nio_uring_sqe_set_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nio_uring_register_sync_cancel(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_sync_cancel(long,long)"""
        return int._wrap(_LibURing.nio_uring_register_sync_cancel(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_recvmsg_cmsg_nexthdr(arg0: 'IOURingRecvmsgOut', arg1: 'Msghdr', arg2: 'CMsghdr') -> 'linux.CMsghdr':
        """public static org.lwjgl.system.linux.CMsghdr org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_cmsg_nexthdr(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut,org.lwjgl.system.linux.Msghdr,org.lwjgl.system.linux.CMsghdr)"""
        return linux.CMsghdr._wrap(_LibURing.io_uring_recvmsg_cmsg_nexthdr(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def io_uring_prep_recv_multishot(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_recv_multishot(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_recv_multishot(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_symlinkat(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_symlinkat(long,long,int,long)"""
        _LibURing.nio_uring_prep_symlinkat(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_buf_ring_add(arg0: 'IOURingBufRing', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_buf_ring_add(org.lwjgl.system.linux.liburing.IOURingBufRing,java.nio.ByteBuffer,short,int,int)"""
        _LibURing.io_uring_buf_ring_add(arg0, arg1, _short.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_sqring_wait(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_sqring_wait(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_sqring_wait(arg0))

    @staticmethod
    @overload
    def io_uring_prep_timeout(arg0: 'IOURingSQE', arg1: 'KernelTimespec', arg2: int, arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_timeout(org.lwjgl.system.linux.liburing.IOURingSQE,org.lwjgl.system.linux.KernelTimespec,int,int)"""
        _LibURing.io_uring_prep_timeout(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_prep_send_zc(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_send_zc(long,int,long,long,int,int)"""
        _LibURing.nio_uring_prep_send_zc(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_enable_rings(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_enable_rings(long)"""
        return int._wrap(_LibURing.nio_uring_enable_rings(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_multishot_accept(arg0: 'IOURingSQE', arg1: int, arg2: 'Sockaddr', arg3: 'IntBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_multishot_accept(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Sockaddr,java.nio.IntBuffer,int)"""
        _LibURing.io_uring_prep_multishot_accept(arg0, _int.valueOf(arg1), arg2, arg3, _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_poll_multishot(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_poll_multishot(long,int,int)"""
        _LibURing.nio_uring_prep_poll_multishot(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_buf_ring_cq_advance(arg0: 'IOURing', arg1: 'IOURingBufRing', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_buf_ring_cq_advance(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingBufRing,int)"""
        _LibURing.io_uring_buf_ring_cq_advance(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_prep_statx(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_statx(long,int,long,int,int,long)"""
        _LibURing.nio_uring_prep_statx(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_remove_buffers(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_remove_buffers(org.lwjgl.system.linux.liburing.IOURingSQE,int,int)"""
        _LibURing.io_uring_prep_remove_buffers(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_prep_splice(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_splice(long,int,long,int,long,int,int)"""
        _LibURing.nio_uring_prep_splice(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @staticmethod
    @overload
    def nio_uring_unregister_ring_fd(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_ring_fd(long)"""
        return int._wrap(_LibURing.nio_uring_unregister_ring_fd(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_symlinkat(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: int, arg3: 'CharSequence'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_symlinkat(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,int,java.lang.CharSequence)"""
        _LibURing.io_uring_prep_symlinkat(arg0, arg1, _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nio_uring_buf_ring_advance(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_buf_ring_advance(long,int)"""
        _LibURing.nio_uring_buf_ring_advance(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_get_probe() -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.LibURing.io_uring_get_probe()"""
        return IOURingProbe._wrap(_LibURing.io_uring_get_probe())

    @staticmethod
    @overload
    def io_uring_peek_batch_cqe(arg0: 'IOURing', arg1: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_peek_batch_cqe(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.PointerBuffer)"""
        return int._wrap(_LibURing.io_uring_peek_batch_cqe(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_fgetxattr(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_fgetxattr(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        _LibURing.io_uring_prep_fgetxattr(arg0, _int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def io_uring_prep_msg_ring_fd(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_msg_ring_fd(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,long,int)"""
        _LibURing.io_uring_prep_msg_ring_fd(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_cancel64(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_cancel64(org.lwjgl.system.linux.liburing.IOURingSQE,long,int)"""
        _LibURing.io_uring_prep_cancel64(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_minor_version() -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.io_uring_minor_version()"""
        return int._wrap(_LibURing.io_uring_minor_version())

    @staticmethod
    @overload
    def io_uring_recvmsg_validate(arg0: 'ByteBuffer', arg1: 'Msghdr') -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_validate(java.nio.ByteBuffer,org.lwjgl.system.linux.Msghdr)"""
        return IOURingRecvmsgOut._wrap(_LibURing.io_uring_recvmsg_validate(arg0, arg1))

    @staticmethod
    @overload
    def nio_uring_unregister_personality(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_unregister_personality(long,int)"""
        return int._wrap(_LibURing.nio_uring_unregister_personality(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_buf_ring_advance(arg0: 'IOURingBufRing', arg1: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_buf_ring_advance(org.lwjgl.system.linux.liburing.IOURingBufRing,int)"""
        _LibURing.io_uring_buf_ring_advance(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_register_restrictions(arg0: 'IOURing', arg1: 'Buffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_restrictions(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer)"""
        return int._wrap(_LibURing.io_uring_register_restrictions(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def nio_uring_cq_eventfd_enabled(arg0: int) -> bool:
        """public static native boolean org.lwjgl.system.linux.liburing.LibURing.nio_uring_cq_eventfd_enabled(long)"""
        return bool._wrap(_LibURing.nio_uring_cq_eventfd_enabled(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_mkdirat(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_mkdirat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int)"""
        _LibURing.io_uring_prep_mkdirat(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def n__io_uring_sqring_wait(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.n__io_uring_sqring_wait(long)"""
        return int._wrap(_LibURing.n__io_uring_sqring_wait(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_prep_rename(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: 'CharSequence'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_rename(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,java.lang.CharSequence)"""
        _LibURing.io_uring_prep_rename(arg0, arg1, arg2)

    @staticmethod
    @overload
    def nio_uring_prep_fadvise(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_fadvise(long,int,int,long,int)"""
        _LibURing.nio_uring_prep_fadvise(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_madvise(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_madvise(long,long,long,int)"""
        _LibURing.nio_uring_prep_madvise(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_register_buffers_sparse(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_buffers_sparse(long,int)"""
        return int._wrap(_LibURing.nio_uring_register_buffers_sparse(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_register_personality(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_personality(long)"""
        return int._wrap(_LibURing.nio_uring_register_personality(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_prep_fsetxattr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_fsetxattr(long,int,long,long,int,int)"""
        _LibURing.nio_uring_prep_fsetxattr(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def nio_uring_prep_accept(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_accept(long,int,long,long,int)"""
        _LibURing.nio_uring_prep_accept(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_openat(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_openat(long,int,long,int,int)"""
        _LibURing.nio_uring_prep_openat(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_unlink(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_unlink(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_unlink(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_cqe_seen(arg0: 'IOURing', arg1: 'IOURingCQE'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_cqe_seen(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingCQE)"""
        _LibURing.io_uring_cqe_seen(arg0, arg1)

    @staticmethod
    @overload
    def nio_uring_wait_cqe_timeout(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_wait_cqe_timeout(long,long,long)"""
        return int._wrap(_LibURing.nio_uring_wait_cqe_timeout(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_register_ring_fd(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_ring_fd(long)"""
        return int._wrap(_LibURing.nio_uring_register_ring_fd(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_opcode_supported(arg0: 'IOURingProbe', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_opcode_supported(org.lwjgl.system.linux.liburing.IOURingProbe,int)"""
        return int._wrap(_LibURing.io_uring_opcode_supported(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_cancel(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_cancel(long,long,int)"""
        _LibURing.nio_uring_prep_cancel(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_unregister_ring_fd(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_unregister_ring_fd(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_unregister_ring_fd(arg0))

    @staticmethod
    @overload
    def io_uring_prep_getxattr(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: 'ByteBuffer', arg3: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_getxattr(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        _LibURing.io_uring_prep_getxattr(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def io_uring_prep_poll_update(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_poll_update(org.lwjgl.system.linux.liburing.IOURingSQE,long,long,int,int)"""
        _LibURing.io_uring_prep_poll_update(arg0, _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_accept_direct(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_accept_direct(long,int,long,long,int,int)"""
        _LibURing.nio_uring_prep_accept_direct(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_link(arg0: 'IOURingSQE', arg1: 'CharSequence', arg2: 'CharSequence', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_link(org.lwjgl.system.linux.liburing.IOURingSQE,java.lang.CharSequence,java.lang.CharSequence,int)"""
        _LibURing.io_uring_prep_link(arg0, arg1, arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_register_iowq_max_workers(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_iowq_max_workers(long,long)"""
        return int._wrap(_LibURing.nio_uring_register_iowq_max_workers(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_prep_timeout_remove(arg0: 'IOURingSQE', arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_timeout_remove(org.lwjgl.system.linux.liburing.IOURingSQE,long,int)"""
        _LibURing.io_uring_prep_timeout_remove(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_setup(arg0: int, arg1: 'IOURingParams') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_setup(int,org.lwjgl.system.linux.liburing.IOURingParams)"""
        return int._wrap(_LibURing.io_uring_setup(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def io_uring_prep_msg_ring_fd_alloc(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_msg_ring_fd_alloc(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,long,int)"""
        _LibURing.io_uring_prep_msg_ring_fd_alloc(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_register_buffers_update_tag(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_buffers_update_tag(long,int,long,long,int)"""
        return int._wrap(_LibURing.nio_uring_register_buffers_update_tag(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def io_uring_prep_sendto(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: 'Sockaddr', arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_sendto(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,org.lwjgl.system.linux.Sockaddr,int)"""
        _LibURing.io_uring_prep_sendto(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), arg4, _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_register_files_update_tag(arg0: 'IOURing', arg1: int, arg2: 'IntBuffer', arg3: 'LongBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_files_update_tag(org.lwjgl.system.linux.liburing.IOURing,int,java.nio.IntBuffer,java.nio.LongBuffer)"""
        return int._wrap(_LibURing.io_uring_register_files_update_tag(arg0, _int.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def io_uring_register_probe(arg0: 'IOURing', arg1: 'IOURingProbe', arg2: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_probe(org.lwjgl.system.linux.liburing.IOURing,org.lwjgl.system.linux.liburing.IOURingProbe,int)"""
        return int._wrap(_LibURing.io_uring_register_probe(arg0, arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_enter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_enter(int,int,int,int,long)"""
        return int._wrap(_LibURing.nio_uring_enter(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nio_uring_prep_connect(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_connect(long,int,long,int)"""
        _LibURing.nio_uring_prep_connect(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3))

    @staticmethod
    @overload
    def nio_uring_register_files_tags(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_register_files_tags(long,long,long,int)"""
        return int._wrap(_LibURing.nio_uring_register_files_tags(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nio_uring_prep_epoll_ctl(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_epoll_ctl(long,int,int,int,long)"""
        _LibURing.nio_uring_prep_epoll_ctl(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_send_zc_fixed(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_send_zc_fixed(long,int,long,long,int,int,int)"""
        _LibURing.nio_uring_prep_send_zc_fixed(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @staticmethod
    @overload
    def nio_uring_recvmsg_payload_length(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_recvmsg_payload_length(long,int,long)"""
        return int._wrap(_LibURing.nio_uring_recvmsg_payload_length(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nio_uring_prep_mkdir(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_mkdir(long,long,int)"""
        _LibURing.nio_uring_prep_mkdir(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def io_uring_prep_socket(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_socket(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,int,int)"""
        _LibURing.io_uring_prep_socket(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_submit_and_wait(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_submit_and_wait(long,int)"""
        return int._wrap(_LibURing.nio_uring_submit_and_wait(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_prep_statx(arg0: 'IOURingSQE', arg1: int, arg2: 'CharSequence', arg3: int, arg4: int, arg5: 'Statx'):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_statx(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.lang.CharSequence,int,int,org.lwjgl.system.linux.Statx)"""
        _LibURing.io_uring_prep_statx(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), arg5)

    @staticmethod
    @overload
    def io_uring_prep_madvise(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_madvise(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_madvise(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_cq_ready(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_cq_ready(long)"""
        return int._wrap(_LibURing.nio_uring_cq_ready(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_cqe_get_data(arg0: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_cqe_get_data(long)"""
        return int._wrap(_LibURing.nio_uring_cqe_get_data(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_get_probe_ring(arg0: 'IOURing') -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.LibURing.io_uring_get_probe_ring(org.lwjgl.system.linux.liburing.IOURing)"""
        return IOURingProbe._wrap(_LibURing.io_uring_get_probe_ring(arg0))

    @staticmethod
    @overload
    def io_uring_sq_space_left(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_sq_space_left(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_sq_space_left(arg0))

    @staticmethod
    @overload
    def io_uring_prep_recvmsg(arg0: 'IOURingSQE', arg1: int, arg2: 'Msghdr', arg3: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_recvmsg(org.lwjgl.system.linux.liburing.IOURingSQE,int,org.lwjgl.system.linux.Msghdr,int)"""
        _LibURing.io_uring_prep_recvmsg(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))

    @staticmethod
    @overload
    def io_uring_mlock_size(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.io_uring_mlock_size(int,int)"""
        return int._wrap(_LibURing.io_uring_mlock_size(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_prep_send(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_send(long,int,long,long,int)"""
        _LibURing.nio_uring_prep_send(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def io_uring_prep_msg_ring_cqe_flags(arg0: 'IOURingSQE', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_msg_ring_cqe_flags(org.lwjgl.system.linux.liburing.IOURingSQE,int,int,long,int,int)"""
        _LibURing.io_uring_prep_msg_ring_cqe_flags(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_enable_rings(arg0: 'IOURing') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_enable_rings(org.lwjgl.system.linux.liburing.IOURing)"""
        return int._wrap(_LibURing.io_uring_enable_rings(arg0))

    @staticmethod
    @overload
    def io_uring_prep_renameat(arg0: 'IOURingSQE', arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: 'ByteBuffer', arg5: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_renameat(org.lwjgl.system.linux.liburing.IOURingSQE,int,java.nio.ByteBuffer,int,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_renameat(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), arg4, _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_prep_mkdir(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_mkdir(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_mkdir(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def nio_uring_get_probe_ring(arg0: int) -> int:
        """public static native long org.lwjgl.system.linux.liburing.LibURing.nio_uring_get_probe_ring(long)"""
        return int._wrap(_LibURing.nio_uring_get_probe_ring(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def io_uring_register_files(arg0: 'IOURing', arg1: 'IntBuffer') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_files(org.lwjgl.system.linux.liburing.IOURing,java.nio.IntBuffer)"""
        return int._wrap(_LibURing.io_uring_register_files(arg0, arg1))

    @staticmethod
    @overload
    def nio_uring_prep_tee(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_tee(long,int,int,int,int)"""
        _LibURing.nio_uring_prep_tee(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def nio_uring_prep_msg_ring_cqe_flags(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.linux.liburing.LibURing.nio_uring_prep_msg_ring_cqe_flags(long,int,int,long,int,int)"""
        _LibURing.nio_uring_prep_msg_ring_cqe_flags(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def io_uring_cq_eventfd_toggle(arg0: 'IOURing', arg1: bool) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_cq_eventfd_toggle(org.lwjgl.system.linux.liburing.IOURing,boolean)"""
        return int._wrap(_LibURing.io_uring_cq_eventfd_toggle(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def nio_uring_submit(arg0: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_submit(long)"""
        return int._wrap(_LibURing.nio_uring_submit(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nio_uring_opcode_supported(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibURing.nio_uring_opcode_supported(long,int)"""
        return int._wrap(_LibURing.nio_uring_opcode_supported(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_register_eventfd_async(arg0: 'IOURing', arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibURing.io_uring_register_eventfd_async(org.lwjgl.system.linux.liburing.IOURing,int)"""
        return int._wrap(_LibURing.io_uring_register_eventfd_async(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def io_uring_recvmsg_cmsg_firsthdr(arg0: 'IOURingRecvmsgOut', arg1: 'Msghdr') -> 'linux.CMsghdr':
        """public static org.lwjgl.system.linux.CMsghdr org.lwjgl.system.linux.liburing.LibURing.io_uring_recvmsg_cmsg_firsthdr(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut,org.lwjgl.system.linux.Msghdr)"""
        return linux.CMsghdr._wrap(_LibURing.io_uring_recvmsg_cmsg_firsthdr(arg0, arg1))

    @staticmethod
    @overload
    def io_uring_prep_setxattr(arg0: 'IOURingSQE', arg1: 'ByteBuffer', arg2: 'ByteBuffer', arg3: 'ByteBuffer', arg4: int):
        """public static void org.lwjgl.system.linux.liburing.LibURing.io_uring_prep_setxattr(org.lwjgl.system.linux.liburing.IOURingSQE,java.nio.ByteBuffer,java.nio.ByteBuffer,java.nio.ByteBuffer,int)"""
        _LibURing.io_uring_prep_setxattr(arg0, arg1, arg2, arg3, _int.valueOf(arg4)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    from pyglsystem import linux
except ImportError:
    linux = _import_once("pyglsystem.linux")

import org.lwjgl.system.linux.KernelTimespec as _KernelTimespec
_KernelTimespec = _KernelTimespec
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
import org.lwjgl.system.linux.liburing.IOURingSyncCancelReg as _IOURingSyncCancelReg_Buffer
_Buffer = _IOURingSyncCancelReg_Buffer.Buffer
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
    """org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.Buffer"""
 
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
    def timeout(self, arg0: 'KernelTimespec') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.timeout(org.lwjgl.system.linux.KernelTimespec)"""
        return 'Buffer'._wrap(super(_Buffer, self).timeout(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.fd()"""
        return int._wrap(super(Buffer, self).fd())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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

    @overload
    def timeout(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.timeout(java.util.function.Consumer<org.lwjgl.system.linux.KernelTimespec>)"""
        return 'Buffer'._wrap(super(_Buffer, self).timeout(arg0))

    @overload
    def timeout(self) -> 'linux.KernelTimespec':
        """public org.lwjgl.system.linux.KernelTimespec org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.timeout()"""
        return 'linux.KernelTimespec'._wrap(super(Buffer, self).timeout())

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
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.flags()"""
        return int._wrap(super(Buffer, self).flags())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer(long,int)"""
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
    def addr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.addr(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).addr(_long.valueOf(arg0)))

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
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.addr()"""
        return int._wrap(super(Buffer, self).addr())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).flags(_int.valueOf(arg0)))

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def fd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer.fd(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).fd(_int.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.system.linux.liburing.IOURingBufRing as _IOURingBufRing_Buffer
_Buffer = _IOURingBufRing_Buffer.Buffer
import java.lang.Short as _short
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.linux.liburing.IOURingBuf as _IOURingBuf_Buffer
_Buffer = _IOURingBuf_Buffer.Buffer
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
import org.lwjgl.system.linux.liburing.IOURingBuf as _IOURingBuf
_IOURingBuf = _IOURingBuf
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
    """org.lwjgl.system.linux.liburing.IOURingBufRing.Buffer"""
 
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

    @overload
    def resv1(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv1(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv1(_long.valueOf(arg0)))

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
    def bufs(self, arg0: int, arg1: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs(int,java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingBuf>)"""
        return 'Buffer'._wrap(super(_Buffer, self).bufs(_int.valueOf(arg0), arg1))

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
    def bufs(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingBuf$Buffer>)"""
        return 'Buffer'._wrap(super(_Buffer, self).bufs(arg0))

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
    def resv3(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv3(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv3(_short.valueOf(arg0)))

    @overload
    def resv1(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv1()"""
        return int._wrap(super(Buffer, self).resv1())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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
    def bufs(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs(int)"""
        return 'IOURingBuf'._wrap(super(_Buffer, self).bufs(_int.valueOf(arg0)))

    @overload
    def tail(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.tail()"""
        return int._wrap(super(Buffer, self).tail())

    @overload
    def bufs(self, arg0: 'Buffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs(org.lwjgl.system.linux.liburing.IOURingBuf$Buffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).bufs(arg0))

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
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv2()"""
        return int._wrap(super(Buffer, self).resv2())

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
    def resv2(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv2(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv2(_int.valueOf(arg0)))

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
    def resv3(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.resv3()"""
        return int._wrap(super(Buffer, self).resv3())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def bufs(self, arg0: int, arg1: 'IOURingBuf') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs(int,org.lwjgl.system.linux.liburing.IOURingBuf)"""
        return 'Buffer'._wrap(super(_Buffer, self).bufs(_int.valueOf(arg0), arg1))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def bufs(self) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.bufs()"""
        return 'Buffer'._wrap(super(Buffer, self).bufs())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def tail(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer.tail(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).tail(_short.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingParams$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.system.linux.liburing.IOURingParams as _IOURingParams_Buffer
_Buffer = _IOURingParams_Buffer.Buffer
import java.util.function.Consumer as Consumer
import org.lwjgl.system.linux.liburing.IOSQRingOffsets as _IOSQRingOffsets
_IOSQRingOffsets = _IOSQRingOffsets
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.linux.liburing.IOCQRingOffsets as _IOCQRingOffsets
_IOCQRingOffsets = _IOCQRingOffsets
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
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingParams.Buffer"""
 
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
    def cq_off(self) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams$Buffer.cq_off()"""
        return 'IOCQRingOffsets'._wrap(super(Buffer, self).cq_off())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def sq_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_entries()"""
        return int._wrap(super(Buffer, self).sq_entries())

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
    def wq_fd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.wq_fd(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).wq_fd(_int.valueOf(arg0)))

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
    def sq_thread_idle(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_thread_idle(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).sq_thread_idle(_int.valueOf(arg0)))

    @overload
    def sq_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_entries(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).sq_entries(_int.valueOf(arg0)))

    @overload
    def cq_off(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.cq_off(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOCQRingOffsets>)"""
        return 'Buffer'._wrap(super(_Buffer, self).cq_off(arg0))

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
    def resv(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.resv(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv(arg0))

    @overload
    def cq_off(self, arg0: 'IOCQRingOffsets') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.cq_off(org.lwjgl.system.linux.liburing.IOCQRingOffsets)"""
        return 'Buffer'._wrap(super(_Buffer, self).cq_off(arg0))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def features(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.features(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).features(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def wq_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.wq_fd()"""
        return int._wrap(super(Buffer, self).wq_fd())

    @overload
    def sq_off(self, arg0: 'IOSQRingOffsets') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_off(org.lwjgl.system.linux.liburing.IOSQRingOffsets)"""
        return 'Buffer'._wrap(super(_Buffer, self).sq_off(arg0))

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def sq_thread_cpu(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_thread_cpu(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).sq_thread_cpu(_int.valueOf(arg0)))

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
    def cq_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.cq_entries()"""
        return int._wrap(super(Buffer, self).cq_entries())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.flags()"""
        return int._wrap(super(Buffer, self).flags())

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
    def cq_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.cq_entries(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).cq_entries(_int.valueOf(arg0)))

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
    def sq_off(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_off(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOSQRingOffsets>)"""
        return 'Buffer'._wrap(super(_Buffer, self).sq_off(arg0))

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
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).flags(_int.valueOf(arg0)))

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
    def sq_thread_idle(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_thread_idle()"""
        return int._wrap(super(Buffer, self).sq_thread_idle())

    @overload
    def resv(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.resv(int,int)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def sq_thread_cpu(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_thread_cpu()"""
        return int._wrap(super(Buffer, self).sq_thread_cpu())

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
    def sq_off(self) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams$Buffer.sq_off()"""
        return 'IOSQRingOffsets'._wrap(super(Buffer, self).sq_off())

    @overload
    def features(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.features()"""
        return int._wrap(super(Buffer, self).features())

    @overload
    def resv(self, arg0: int) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams$Buffer.resv(int)"""
        return int._wrap(super(_Buffer, self).resv(_int.valueOf(arg0)))

    @overload
    def resv(self) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingParams$Buffer.resv()"""
        return 'IntBuffer'._wrap(super(Buffer, self).resv())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSQE$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.lang.Short as _short
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Byte as _byte
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.linux.liburing.IOURingSQE as _IOURingSQE_Buffer
_Buffer = _IOURingSQE_Buffer.Buffer
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
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
import java.nio.LongBuffer as LongBuffer
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
    """org.lwjgl.system.linux.liburing.IOURingSQE.Buffer"""
 
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
    def addr_len(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr_len()"""
        return int._wrap(super(Buffer, self).addr_len())

    @overload
    def poll32_events(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.poll32_events(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).poll32_events(_int.valueOf(arg0)))

    @overload
    def addr2(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr2()"""
        return int._wrap(super(Buffer, self).addr2())

    @overload
    def sync_range_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.sync_range_flags()"""
        return int._wrap(super(Buffer, self).sync_range_flags())

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
    def __pad3(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad3(int,short)"""
        return 'Buffer'._wrap(super(_Buffer, self).__pad3(_int.valueOf(arg0), _short.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def xattr_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.xattr_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).xattr_flags(_int.valueOf(arg0)))

    @overload
    def ioprio(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.ioprio()"""
        return int._wrap(super(Buffer, self).ioprio())

    @overload
    def personality(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.personality()"""
        return int._wrap(super(Buffer, self).personality())

    @overload
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr()"""
        return int._wrap(super(Buffer, self).addr())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @overload
    def open_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.open_flags()"""
        return int._wrap(super(Buffer, self).open_flags())

    @overload
    def unlink_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.unlink_flags()"""
        return int._wrap(super(Buffer, self).unlink_flags())

    @overload
    def uring_cmd_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.uring_cmd_flags()"""
        return int._wrap(super(Buffer, self).uring_cmd_flags())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @overload
    def rw_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.rw_flags()"""
        return int._wrap(super(Buffer, self).rw_flags())

    @overload
    def buf_group(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.buf_group(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).buf_group(_short.valueOf(arg0)))

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
    def splice_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_flags()"""
        return int._wrap(super(Buffer, self).splice_flags())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def cmd(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).cmd(arg0))

    @overload
    def addr2(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr2(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).addr2(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def cmd(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).cmd())

    @overload
    def ioprio(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.ioprio(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).ioprio(_short.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def poll_events(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.poll_events()"""
        return int._wrap(super(Buffer, self).poll_events())

    @overload
    def cancel_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cancel_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).cancel_flags(_int.valueOf(arg0)))

    @overload
    def addr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).addr(_long.valueOf(arg0)))

    @overload
    def fsync_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fsync_flags()"""
        return int._wrap(super(Buffer, self).fsync_flags())

    @overload
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.len()"""
        return int._wrap(super(Buffer, self).len())

    @overload
    def fadvise_advice(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fadvise_advice(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).fadvise_advice(_int.valueOf(arg0)))

    @overload
    def poll32_events(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.poll32_events()"""
        return int._wrap(super(Buffer, self).poll32_events())

    @overload
    def splice_off_in(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_off_in(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).splice_off_in(_long.valueOf(arg0)))

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def __pad2(self, arg0: 'LongBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad2(java.nio.LongBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).__pad2(arg0))

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
    def hardlink_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.hardlink_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).hardlink_flags(_int.valueOf(arg0)))

    @overload
    def rename_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.rename_flags()"""
        return int._wrap(super(Buffer, self).rename_flags())

    @overload
    def opcode(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.opcode()"""
        return int._wrap(super(Buffer, self).opcode())

    @overload
    def cmd_op(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd_op(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).cmd_op(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @overload
    def __pad3(self, arg0: int) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad3(int)"""
        return int._wrap(super(_Buffer, self).__pad3(_int.valueOf(arg0)))

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
    def off(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.off()"""
        return int._wrap(super(Buffer, self).off())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def user_data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.user_data()"""
        return int._wrap(super(Buffer, self).user_data())

    @overload
    def splice_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).splice_flags(_int.valueOf(arg0)))

    @overload
    def cmd(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd(int,byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cmd(_int.valueOf(arg0), _byte.valueOf(arg1)))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def timeout_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.timeout_flags()"""
        return int._wrap(super(Buffer, self).timeout_flags())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __pad1(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad1()"""
        return int._wrap(super(Buffer, self).__pad1())

    @overload
    def __pad1(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad1(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).__pad1(_int.valueOf(arg0)))

    @overload
    def __pad3(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad3()"""
        return 'ShortBuffer'._wrap(super(Buffer, self).__pad3())

    @overload
    def xattr_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.xattr_flags()"""
        return int._wrap(super(Buffer, self).xattr_flags())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def msg_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.msg_flags()"""
        return int._wrap(super(Buffer, self).msg_flags())

    @overload
    def msg_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.msg_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).msg_flags(_int.valueOf(arg0)))

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def rename_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.rename_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).rename_flags(_int.valueOf(arg0)))

    @overload
    def unlink_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.unlink_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).unlink_flags(_int.valueOf(arg0)))

    @overload
    def __pad2(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad2()"""
        return 'LongBuffer'._wrap(super(Buffer, self).__pad2())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def fsync_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fsync_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).fsync_flags(_int.valueOf(arg0)))

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
    def addr3(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr3()"""
        return int._wrap(super(Buffer, self).addr3())

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @overload
    def accept_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.accept_flags()"""
        return int._wrap(super(Buffer, self).accept_flags())

    @overload
    def open_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.open_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).open_flags(_int.valueOf(arg0)))

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
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.flags(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).flags(_byte.valueOf(arg0)))

    @overload
    def cmd_op(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd_op()"""
        return int._wrap(super(Buffer, self).cmd_op())

    @overload
    def splice_off_in(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_off_in()"""
        return int._wrap(super(Buffer, self).splice_off_in())

    @overload
    def accept_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.accept_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).accept_flags(_int.valueOf(arg0)))

    @overload
    def addr3(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr3(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).addr3(_long.valueOf(arg0)))

    @overload
    def fadvise_advice(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fadvise_advice()"""
        return int._wrap(super(Buffer, self).fadvise_advice())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def addr_len(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.addr_len(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).addr_len(_short.valueOf(arg0)))

    @overload
    def cancel_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cancel_flags()"""
        return int._wrap(super(Buffer, self).cancel_flags())

    @overload
    def buf_index(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.buf_index()"""
        return int._wrap(super(Buffer, self).buf_index())

    @overload
    def poll_events(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.poll_events(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).poll_events(_short.valueOf(arg0)))

    @overload
    def file_index(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.file_index()"""
        return int._wrap(super(Buffer, self).file_index())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def user_data(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.user_data(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).user_data(_long.valueOf(arg0)))

    @overload
    def file_index(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.file_index(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).file_index(_int.valueOf(arg0)))

    @overload
    def hardlink_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.hardlink_flags()"""
        return int._wrap(super(Buffer, self).hardlink_flags())

    @overload
    def rw_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.rw_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).rw_flags(_int.valueOf(arg0)))

    @overload
    def timeout_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.timeout_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).timeout_flags(_int.valueOf(arg0)))

    @overload
    def buf_index(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.buf_index(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).buf_index(_short.valueOf(arg0)))

    @overload
    def statx_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.statx_flags()"""
        return int._wrap(super(Buffer, self).statx_flags())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def msg_ring_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.msg_ring_flags()"""
        return int._wrap(super(Buffer, self).msg_ring_flags())

    @overload
    def len(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.len(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).len(_int.valueOf(arg0)))

    @overload
    def uring_cmd_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.uring_cmd_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).uring_cmd_flags(_int.valueOf(arg0)))

    @overload
    def msg_ring_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.msg_ring_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).msg_ring_flags(_int.valueOf(arg0)))

    @overload
    def buf_group(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.buf_group()"""
        return int._wrap(super(Buffer, self).buf_group())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def cmd(self, arg0: int) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.cmd(int)"""
        return int._wrap(super(_Buffer, self).cmd(_int.valueOf(arg0)))

    @overload
    def sync_range_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.sync_range_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).sync_range_flags(_int.valueOf(arg0)))

    @overload
    def fd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fd(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).fd(_int.valueOf(arg0)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def splice_fd_in(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_fd_in()"""
        return int._wrap(super(Buffer, self).splice_fd_in())

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
    def off(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.off(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).off(_long.valueOf(arg0)))

    @overload
    def __pad3(self, arg0: 'ShortBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad3(java.nio.ShortBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).__pad3(arg0))

    @overload
    def fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.fd()"""
        return int._wrap(super(Buffer, self).fd())

    @overload
    def __pad2(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad2(int,long)"""
        return 'Buffer'._wrap(super(_Buffer, self).__pad2(_int.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.flags()"""
        return int._wrap(super(Buffer, self).flags())

    @overload
    def __pad2(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.__pad2(int)"""
        return int._wrap(super(_Buffer, self).__pad2(_int.valueOf(arg0)))

    @overload
    def personality(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.personality(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).personality(_short.valueOf(arg0)))

    @overload
    def statx_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.statx_flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).statx_flags(_int.valueOf(arg0)))

    @overload
    def splice_fd_in(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.splice_fd_in(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).splice_fd_in(_int.valueOf(arg0)))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def opcode(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE$Buffer.opcode(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).opcode(_byte.valueOf(arg0)))

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingProbeOp
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
import java.lang.Short as _short
import java.lang.Integer as _int
import org.lwjgl.system.linux.liburing.IOURingProbeOp as _IOURingProbeOp
_IOURingProbeOp = _IOURingProbeOp
import java.lang.Byte as _byte
import org.lwjgl.system.linux.liburing.IOURingProbeOp as _IOURingProbeOp_Buffer
_Buffer = _IOURingProbeOp_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingProbeOp():
    """org.lwjgl.system.linux.liburing.IOURingProbeOp"""
 
    @staticmethod
    def _wrap(java_value: _IOURingProbeOp) -> 'IOURingProbeOp':
        return IOURingProbeOp(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingProbeOp):
        """
        Dynamic initializer for IOURingProbeOp.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingProbeOp__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingProbeOp__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'IOURingProbeOp') -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.set(org.lwjgl.system.linux.liburing.IOURingProbeOp)"""
        return 'IOURingProbeOp'._wrap(super(_IOURingProbeOp, self).set(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.create(long,int)"""
        return Buffer._wrap(_IOURingProbeOp.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp(java.nio.ByteBuffer)"""
        val = _IOURingProbeOp(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingProbeOp._wrap(_IOURingProbeOp.calloc(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingProbeOp.malloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingProbeOp.nresv2(long)"""
        return int._wrap(_IOURingProbeOp.nresv2(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.calloc(int)"""
        return Buffer._wrap(_IOURingProbeOp.calloc(_int.valueOf(arg0)))

    @overload
    def resv(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.resv(byte)"""
        return 'IOURingProbeOp'._wrap(super(_IOURingProbeOp, self).resv(_byte.valueOf(arg0)))

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
    def malloc() -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.malloc()"""
        return IOURingProbeOp._wrap(_IOURingProbeOp.malloc())

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.create(long)"""
        return IOURingProbeOp._wrap(_IOURingProbeOp.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.malloc(int)"""
        return Buffer._wrap(_IOURingProbeOp.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.calloc()"""
        return IOURingProbeOp._wrap(_IOURingProbeOp.calloc())

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
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingProbeOp.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def resv(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbeOp.resv()"""
        return int._wrap(super(IOURingProbeOp, self).resv())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingProbeOp.resv2()"""
        return int._wrap(super(IOURingProbeOp, self).resv2())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingProbeOp._wrap(_IOURingProbeOp.malloc(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.set(byte,byte,short,int)"""
        return 'IOURingProbeOp'._wrap(super(_IOURingProbeOp, self).set(_byte.valueOf(arg0), _byte.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbeOp.nresv(long,byte)"""
        _IOURingProbeOp.nresv(_long.valueOf(arg0), _byte.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingProbeOp.nresv(long)"""
        return int._wrap(_IOURingProbeOp.nresv(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.create()"""
        return IOURingProbeOp._wrap(_IOURingProbeOp.create())

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingProbeOp.nflags(long)"""
        return int._wrap(_IOURingProbeOp.nflags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbeOp.nresv2(long,int)"""
        _IOURingProbeOp.nresv2(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resv2(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.resv2(int)"""
        return 'IOURingProbeOp'._wrap(super(_IOURingProbeOp, self).resv2(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nop(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingProbeOp.nop(long)"""
        return int._wrap(_IOURingProbeOp.nop(_long.valueOf(arg0)))

    @overload
    def flags(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingProbeOp.flags()"""
        return int._wrap(super(IOURingProbeOp, self).flags())

    @staticmethod
    @overload
    def nop(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbeOp.nop(long,byte)"""
        _IOURingProbeOp.nop(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.createSafe(long,int)"""
        return Buffer._wrap(_IOURingProbeOp.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def op(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.op(byte)"""
        return 'IOURingProbeOp'._wrap(super(_IOURingProbeOp, self).op(_byte.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbeOp.op()"""
        return int._wrap(super(IOURingProbeOp, self).op())

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbeOp.nflags(long,short)"""
        _IOURingProbeOp.nflags(_long.valueOf(arg0), _short.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.createSafe(long)"""
        return IOURingProbeOp._wrap(_IOURingProbeOp.createSafe(_long.valueOf(arg0)))

    @overload
    def flags(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbeOp.flags(short)"""
        return 'IOURingProbeOp'._wrap(super(_IOURingProbeOp, self).flags(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp.create(int)"""
        return Buffer._wrap(_IOURingProbeOp.create(_int.valueOf(arg0)))

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
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingProbeOp.sizeof()"""
        return int._wrap(super(IOURingProbeOp, self).sizeof())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer
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
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.linux.liburing.IOSQRingOffsets as _IOSQRingOffsets_Buffer
_Buffer = _IOSQRingOffsets_Buffer.Buffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOSQRingOffsets.Buffer"""
 
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
    def ring_mask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.ring_mask(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_mask(_int.valueOf(arg0)))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.ring_mask()"""
        return int._wrap(super(Buffer, self).ring_mask())

    @overload
    def dropped(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.dropped()"""
        return int._wrap(super(Buffer, self).dropped())

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
    def tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.tail()"""
        return int._wrap(super(Buffer, self).tail())

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
    def head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.head()"""
        return int._wrap(super(Buffer, self).head())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def array(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.array(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).array(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.ring_entries()"""
        return int._wrap(super(Buffer, self).ring_entries())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).flags(_int.valueOf(arg0)))

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
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.flags()"""
        return int._wrap(super(Buffer, self).flags())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def ring_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.ring_entries(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_entries(_int.valueOf(arg0)))

    @overload
    def tail(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.tail(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).tail(_int.valueOf(arg0)))

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
    def array(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.array()"""
        return int._wrap(super(Buffer, self).array())

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
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def dropped(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.dropped(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).dropped(_int.valueOf(arg0)))

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
    def head(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer.head(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).head(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURing$Buffer
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
import java.lang.Byte as _byte
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
import org.lwjgl.system.linux.liburing.IOURing as _IOURing_Buffer
_Buffer = _IOURing_Buffer.Buffer
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import org.lwjgl.system.linux.liburing.IOURingSQ as _IOURingSQ
_IOURingSQ = _IOURingSQ
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import org.lwjgl.system.linux.liburing.IOURingCQ as _IOURingCQ
_IOURingCQ = _IOURingCQ
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURing.Buffer"""
 
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
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing$Buffer.flags()"""
        return int._wrap(super(Buffer, self).flags())

    @overload
    def ring_fd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.ring_fd(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_fd(_int.valueOf(arg0)))

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
    def features(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.features(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).features(_int.valueOf(arg0)))

    @overload
    def int_flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURing$Buffer.int_flags()"""
        return int._wrap(super(Buffer, self).int_flags())

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
    def enter_ring_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing$Buffer.enter_ring_fd()"""
        return int._wrap(super(Buffer, self).enter_ring_fd())

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
    def sq(self) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURing$Buffer.sq()"""
        return 'IOURingSQ'._wrap(super(Buffer, self).sq())

    @overload
    def enter_ring_fd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.enter_ring_fd(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).enter_ring_fd(_int.valueOf(arg0)))

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
    def features(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing$Buffer.features()"""
        return int._wrap(super(Buffer, self).features())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def sq(self, arg0: 'IOURingSQ') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.sq(org.lwjgl.system.linux.liburing.IOURingSQ)"""
        return 'Buffer'._wrap(super(_Buffer, self).sq(arg0))

    @overload
    def sq(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.sq(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingSQ>)"""
        return 'Buffer'._wrap(super(_Buffer, self).sq(arg0))

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
    def int_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.int_flags(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).int_flags(_byte.valueOf(arg0)))

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
    def cq(self) -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURing$Buffer.cq()"""
        return 'IOURingCQ'._wrap(super(Buffer, self).cq())

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
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer(long,int)"""
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

    @overload
    def ring_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing$Buffer.ring_fd()"""
        return int._wrap(super(Buffer, self).ring_fd())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).flags(_int.valueOf(arg0)))

    @overload
    def cq(self, arg0: 'IOURingCQ') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.cq(org.lwjgl.system.linux.liburing.IOURingCQ)"""
        return 'Buffer'._wrap(super(_Buffer, self).cq(arg0))

    @overload
    def cq(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing$Buffer.cq(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingCQ>)"""
        return 'Buffer'._wrap(super(_Buffer, self).cq(arg0))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURing
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
import org.lwjgl.system.linux.liburing.IOURing as _IOURing_Buffer
_Buffer = _IOURing_Buffer.Buffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.system.linux.liburing.IOURingSQ as _IOURingSQ
_IOURingSQ = _IOURingSQ
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.system.linux.liburing.IOURing as _IOURing
_IOURing = _IOURing
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.lwjgl.system.linux.liburing.IOURingCQ as _IOURingCQ
_IOURingCQ = _IOURingCQ
import java.lang.Byte as _byte
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURing():
    """org.lwjgl.system.linux.liburing.IOURing"""
 
    @staticmethod
    def _wrap(java_value: _IOURing) -> 'IOURing':
        return IOURing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURing):
        """
        Dynamic initializer for IOURing.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURing__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURing__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURing.malloc(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: 'IOURing') -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.set(org.lwjgl.system.linux.liburing.IOURing)"""
        return 'IOURing'._wrap(super(_IOURing, self).set(arg0))

    @staticmethod
    @overload
    def malloc() -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.malloc()"""
        return IOURing._wrap(_IOURing.malloc())

    @overload
    def features(self, arg0: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.features(int)"""
        return 'IOURing'._wrap(super(_IOURing, self).features(_int.valueOf(arg0)))

    @overload
    def enter_ring_fd(self, arg0: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.enter_ring_fd(int)"""
        return 'IOURing'._wrap(super(_IOURing, self).enter_ring_fd(_int.valueOf(arg0)))

    @overload
    def sq(self) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURing.sq()"""
        return 'IOURingSQ'._wrap(super(IOURing, self).sq())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ncq(arg0: int) -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURing.ncq(long)"""
        return IOURingCQ._wrap(_IOURing.ncq(_long.valueOf(arg0)))

    @overload
    def cq(self) -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURing.cq()"""
        return 'IOURingCQ'._wrap(super(IOURing, self).cq())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.createSafe(long,int)"""
        return Buffer._wrap(_IOURing.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def cq(self, arg0: 'IOURingCQ') -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.cq(org.lwjgl.system.linux.liburing.IOURingCQ)"""
        return 'IOURing'._wrap(super(_IOURing, self).cq(arg0))

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
    def nint_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nint_flags(long,byte)"""
        _IOURing.nint_flags(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURing._wrap(_IOURing.malloc(arg0))

    @overload
    def cq(self, arg0: 'Consumer') -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.cq(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingCQ>)"""
        return 'IOURing'._wrap(super(_IOURing, self).cq(arg0))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nflags(long,int)"""
        _IOURing.nflags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def sq(self, arg0: 'IOURingSQ') -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.sq(org.lwjgl.system.linux.liburing.IOURingSQ)"""
        return 'IOURing'._wrap(super(_IOURing, self).sq(arg0))

    @overload
    def ring_fd(self, arg0: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.ring_fd(int)"""
        return 'IOURing'._wrap(super(_IOURing, self).ring_fd(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.create(long,int)"""
        return Buffer._wrap(_IOURing.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def enter_ring_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing.enter_ring_fd()"""
        return int._wrap(super(IOURing, self).enter_ring_fd())

    @staticmethod
    @overload
    def npad2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.npad2(long,int)"""
        _IOURing.npad2(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def npad(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURing.npad(long)"""
        return ByteBuffer._wrap(_IOURing.npad(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsq(arg0: int, arg1: 'IOURingSQ'):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nsq(long,org.lwjgl.system.linux.liburing.IOURingSQ)"""
        _IOURing.nsq(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nfeatures(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nfeatures(long,int)"""
        _IOURing.nfeatures(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURing.nflags(long)"""
        return int._wrap(_IOURing.nflags(_long.valueOf(arg0)))

    @overload
    def flags(self, arg0: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.flags(int)"""
        return 'IOURing'._wrap(super(_IOURing, self).flags(_int.valueOf(arg0)))

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
    def ring_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing.ring_fd()"""
        return int._wrap(super(IOURing, self).ring_fd())

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.create(long)"""
        return IOURing._wrap(_IOURing.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURing._wrap(_IOURing.calloc(arg0))

    @staticmethod
    @overload
    def nfeatures(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURing.nfeatures(long)"""
        return int._wrap(_IOURing.nfeatures(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def npad2(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURing.npad2(long)"""
        return int._wrap(_IOURing.npad2(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.validate(long)"""
        _IOURing.validate(_long.valueOf(arg0))

    @overload
    def sq(self, arg0: 'Consumer') -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.sq(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingSQ>)"""
        return 'IOURing'._wrap(super(_IOURing, self).sq(arg0))

    @staticmethod
    @overload
    def nring_fd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nring_fd(long,int)"""
        _IOURing.nring_fd(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nring_fd(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURing.nring_fd(long)"""
        return int._wrap(_IOURing.nring_fd(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def npad(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURing.npad(long,java.nio.ByteBuffer)"""
        _IOURing.npad(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nenter_ring_fd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.nenter_ring_fd(long,int)"""
        _IOURing.nenter_ring_fd(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: 'IOURingSQ', arg1: 'IOURingCQ', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.set(org.lwjgl.system.linux.liburing.IOURingSQ,org.lwjgl.system.linux.liburing.IOURingCQ,int,int,int,int,byte)"""
        return 'IOURing'._wrap(super(_IOURing, self).set(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _byte.valueOf(arg6)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def features(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing.features()"""
        return int._wrap(super(IOURing, self).features())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURing.calloc(_int.valueOf(arg0), arg1))

    @overload
    def int_flags(self, arg0: int) -> 'IOURing':
        """public org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.int_flags(byte)"""
        return 'IOURing'._wrap(super(_IOURing, self).int_flags(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def nsq(arg0: int) -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURing.nsq(long)"""
        return IOURingSQ._wrap(_IOURing.nsq(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURing.npad(long,int,byte)"""
        _IOURing.npad(_long.valueOf(arg0), _int.valueOf(arg1), _byte.valueOf(arg2))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.create(int)"""
        return Buffer._wrap(_IOURing.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURing.npad(long,int)"""
        return int._wrap(_IOURing.npad(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nenter_ring_fd(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURing.nenter_ring_fd(long)"""
        return int._wrap(_IOURing.nenter_ring_fd(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.malloc(int)"""
        return Buffer._wrap(_IOURing.malloc(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURing(java.nio.ByteBuffer)"""
        val = _IOURing(arg0)
        self.__wrapper = val

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing.flags()"""
        return int._wrap(super(IOURing, self).flags())

    @staticmethod
    @overload
    def calloc() -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.calloc()"""
        return IOURing._wrap(_IOURing.calloc())

    @staticmethod
    @overload
    def create() -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.create()"""
        return IOURing._wrap(_IOURing.create())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURing':
        """public static org.lwjgl.system.linux.liburing.IOURing org.lwjgl.system.linux.liburing.IOURing.createSafe(long)"""
        return IOURing._wrap(_IOURing.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def ncq(arg0: int, arg1: 'IOURingCQ'):
        """public static void org.lwjgl.system.linux.liburing.IOURing.ncq(long,org.lwjgl.system.linux.liburing.IOURingCQ)"""
        _IOURing.ncq(_long.valueOf(arg0), arg1)

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURing$Buffer org.lwjgl.system.linux.liburing.IOURing.calloc(int)"""
        return Buffer._wrap(_IOURing.calloc(_int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURing.sizeof()"""
        return int._wrap(super(IOURing, self).sizeof())

    @staticmethod
    @overload
    def nint_flags(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURing.nint_flags(long)"""
        return int._wrap(_IOURing.nint_flags(_long.valueOf(arg0)))

    @overload
    def int_flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURing.int_flags()"""
        return int._wrap(super(IOURing, self).int_flags())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer
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
import org.lwjgl.system.linux.liburing.IOURingRSRCRegister as _IOURingRSRCRegister_Buffer
_Buffer = _IOURingRSRCRegister_Buffer.Buffer
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
    """org.lwjgl.system.linux.liburing.IOURingRSRCRegister.Buffer"""
 
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
    def resv2(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.resv2()"""
        return int._wrap(super(Buffer, self).resv2())

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

    @overload
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.data()"""
        return int._wrap(super(Buffer, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def nr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.nr(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).nr(_int.valueOf(arg0)))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @overload
    def nr(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.nr()"""
        return int._wrap(super(Buffer, self).nr())

    @overload
    def tags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.tags(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).tags(_long.valueOf(arg0)))

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
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def resv2(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.resv2(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv2(_long.valueOf(arg0)))

    @overload
    def tags(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.tags()"""
        return int._wrap(super(Buffer, self).tags())

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
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).flags(_int.valueOf(arg0)))

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
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.flags()"""
        return int._wrap(super(Buffer, self).flags())

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

    @overload
    def data(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCRegister$Buffer.data(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).data(_long.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSyncCancelReg
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.system.linux.liburing.IOURingSyncCancelReg as _IOURingSyncCancelReg
_IOURingSyncCancelReg = _IOURingSyncCancelReg
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
    from pyglsystem import linux
except ImportError:
    linux = _import_once("pyglsystem.linux")

import org.lwjgl.system.linux.KernelTimespec as _KernelTimespec
_KernelTimespec = _KernelTimespec
import java.nio.LongBuffer as LongBuffer
import org.lwjgl.system.linux.liburing.IOURingSyncCancelReg as _IOURingSyncCancelReg_Buffer
_Buffer = _IOURingSyncCancelReg_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingSyncCancelReg():
    """org.lwjgl.system.linux.liburing.IOURingSyncCancelReg"""
 
    @staticmethod
    def _wrap(java_value: _IOURingSyncCancelReg) -> 'IOURingSyncCancelReg':
        return IOURingSyncCancelReg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingSyncCancelReg):
        """
        Dynamic initializer for IOURingSyncCancelReg.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingSyncCancelReg__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingSyncCancelReg__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def npad(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.npad(long)"""
        return LongBuffer._wrap(_IOURingSyncCancelReg.npad(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.nflags(long)"""
        return int._wrap(_IOURingSyncCancelReg.nflags(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addr(self, arg0: int) -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.addr(long)"""
        return 'IOURingSyncCancelReg'._wrap(super(_IOURingSyncCancelReg, self).addr(_long.valueOf(arg0)))

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
    def malloc() -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.malloc()"""
        return IOURingSyncCancelReg._wrap(_IOURingSyncCancelReg.malloc())

    @overload
    def set(self, arg0: 'IOURingSyncCancelReg') -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.set(org.lwjgl.system.linux.liburing.IOURingSyncCancelReg)"""
        return 'IOURingSyncCancelReg'._wrap(super(_IOURingSyncCancelReg, self).set(arg0))

    @staticmethod
    @overload
    def create() -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.create()"""
        return IOURingSyncCancelReg._wrap(_IOURingSyncCancelReg.create())

    @staticmethod
    @overload
    def nfd(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.nfd(long)"""
        return int._wrap(_IOURingSyncCancelReg.nfd(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nfd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.nfd(long,int)"""
        _IOURingSyncCancelReg.nfd(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSyncCancelReg._wrap(_IOURingSyncCancelReg.calloc(arg0))

    @staticmethod
    @overload
    def naddr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.naddr(long,long)"""
        _IOURingSyncCancelReg.naddr(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def timeout(self) -> 'linux.KernelTimespec':
        """public org.lwjgl.system.linux.KernelTimespec org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.timeout()"""
        return 'linux.KernelTimespec'._wrap(super(IOURingSyncCancelReg, self).timeout())

    @staticmethod
    @overload
    def naddr(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.naddr(long)"""
        return int._wrap(_IOURingSyncCancelReg.naddr(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.npad(long,int,long)"""
        _IOURingSyncCancelReg.npad(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.calloc(int)"""
        return Buffer._wrap(_IOURingSyncCancelReg.calloc(_int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.fd()"""
        return int._wrap(super(IOURingSyncCancelReg, self).fd())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.create(int)"""
        return Buffer._wrap(_IOURingSyncCancelReg.create(_int.valueOf(arg0)))

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
    def malloc(arg0: 'MemoryStack') -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSyncCancelReg._wrap(_IOURingSyncCancelReg.malloc(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.malloc(int)"""
        return Buffer._wrap(_IOURingSyncCancelReg.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: 'LongBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.npad(long,java.nio.LongBuffer)"""
        _IOURingSyncCancelReg.npad(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.createSafe(long,int)"""
        return Buffer._wrap(_IOURingSyncCancelReg.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def flags(self, arg0: int) -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.flags(int)"""
        return 'IOURingSyncCancelReg'._wrap(super(_IOURingSyncCancelReg, self).flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.createSafe(long)"""
        return IOURingSyncCancelReg._wrap(_IOURingSyncCancelReg.createSafe(_long.valueOf(arg0)))

    @overload
    def fd(self, arg0: int) -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.fd(int)"""
        return 'IOURingSyncCancelReg'._wrap(super(_IOURingSyncCancelReg, self).fd(_int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.flags()"""
        return int._wrap(super(IOURingSyncCancelReg, self).flags())

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.npad(long,int)"""
        return int._wrap(_IOURingSyncCancelReg.npad(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def timeout(self, arg0: 'Consumer') -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.timeout(java.util.function.Consumer<org.lwjgl.system.linux.KernelTimespec>)"""
        return 'IOURingSyncCancelReg'._wrap(super(_IOURingSyncCancelReg, self).timeout(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.create(long)"""
        return IOURingSyncCancelReg._wrap(_IOURingSyncCancelReg.create(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg(java.nio.ByteBuffer)"""
        val = _IOURingSyncCancelReg(arg0)
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'KernelTimespec') -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.set(long,int,int,org.lwjgl.system.linux.KernelTimespec)"""
        return 'IOURingSyncCancelReg'._wrap(super(_IOURingSyncCancelReg, self).set(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def ntimeout(arg0: int, arg1: 'KernelTimespec'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.ntimeout(long,org.lwjgl.system.linux.KernelTimespec)"""
        _IOURingSyncCancelReg.ntimeout(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def ntimeout(arg0: int) -> 'linux.KernelTimespec':
        """public static org.lwjgl.system.linux.KernelTimespec org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.ntimeout(long)"""
        return linux.KernelTimespec._wrap(_IOURingSyncCancelReg.ntimeout(_long.valueOf(arg0)))

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
        """public int org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.sizeof()"""
        return int._wrap(super(IOURingSyncCancelReg, self).sizeof())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingSyncCancelReg.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.nflags(long,int)"""
        _IOURingSyncCancelReg.nflags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.create(long,int)"""
        return Buffer._wrap(_IOURingSyncCancelReg.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.addr()"""
        return int._wrap(super(IOURingSyncCancelReg, self).addr())

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
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg$Buffer org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingSyncCancelReg.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc() -> 'IOURingSyncCancelReg':
        """public static org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.calloc()"""
        return IOURingSyncCancelReg._wrap(_IOURingSyncCancelReg.calloc())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def timeout(self, arg0: 'KernelTimespec') -> 'IOURingSyncCancelReg':
        """public org.lwjgl.system.linux.liburing.IOURingSyncCancelReg org.lwjgl.system.linux.liburing.IOURingSyncCancelReg.timeout(org.lwjgl.system.linux.KernelTimespec)"""
        return 'IOURingSyncCancelReg'._wrap(super(_IOURingSyncCancelReg, self).timeout(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.linux.liburing.IOURingRecvmsgOut as _IOURingRecvmsgOut_Buffer
_Buffer = _IOURingRecvmsgOut_Buffer.Buffer
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
    """org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.Buffer"""
 
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
    def namelen(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.namelen(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).namelen(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def namelen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.namelen()"""
        return int._wrap(super(Buffer, self).namelen())

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
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.flags()"""
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
    def payloadlen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.payloadlen()"""
        return int._wrap(super(Buffer, self).payloadlen())

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
    def controllen(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.controllen(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).controllen(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer(java.nio.ByteBuffer)"""
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
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer(long,int)"""
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
    def controllen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.controllen()"""
        return int._wrap(super(Buffer, self).controllen())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).flags(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def payloadlen(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer.payloadlen(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).payloadlen(_int.valueOf(arg0)))

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer
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
import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate as _IOURingRSRCUpdate_Buffer
_Buffer = _IOURingRSRCUpdate_Buffer.Buffer
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
    """org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.Buffer"""
 
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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer(long,int)"""
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
    def offset(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.offset(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).offset(_int.valueOf(arg0)))

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
    def offset(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.offset()"""
        return int._wrap(super(Buffer, self).offset())

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
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.resv(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv(_int.valueOf(arg0)))

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
    def data(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.data(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).data(_long.valueOf(arg0)))

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.data()"""
        return int._wrap(super(Buffer, self).data())

    @overload
    def resv(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer.resv()"""
        return int._wrap(super(Buffer, self).resv())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBuf$Buffer
from pyquantum_helper import import_once as _import_once
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
import org.lwjgl.system.linux.liburing.IOURingBuf as _IOURingBuf_Buffer
_Buffer = _IOURingBuf_Buffer.Buffer
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
    """org.lwjgl.system.linux.liburing.IOURingBuf.Buffer"""
 
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
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.len()"""
        return int._wrap(super(Buffer, self).len())

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
    def addr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.addr(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).addr(_long.valueOf(arg0)))

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
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def bid(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.bid(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).bid(_short.valueOf(arg0)))

    @overload
    def resv(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.resv()"""
        return int._wrap(super(Buffer, self).resv())

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
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.resv(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv(_short.valueOf(arg0)))

    @overload
    def bid(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.bid()"""
        return int._wrap(super(Buffer, self).bid())

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

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer(long,int)"""
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

    @overload
    def len(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.len(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).len(_int.valueOf(arg0)))

    @overload
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBuf$Buffer.addr()"""
        return int._wrap(super(Buffer, self).addr())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.LibIOURing
from builtins import str
import org.lwjgl.system.linux.liburing.LibIOURing as _LibIOURing
_LibIOURing = _LibIOURing
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibIOURing():
    """org.lwjgl.system.linux.liburing.LibIOURing"""
 
    @staticmethod
    def _wrap(java_value: _LibIOURing) -> 'LibIOURing':
        return LibIOURing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibIOURing):
        """
        Dynamic initializer for LibIOURing.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibIOURing__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibIOURing__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nio_uring_enter2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibIOURing.nio_uring_enter2(int,int,int,int,long,int)"""
        return int._wrap(_LibIOURing.nio_uring_enter2(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5)))

    @staticmethod
    @overload
    def io_uring_register(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibIOURing.io_uring_register(int,int,long,int)"""
        return int._wrap(_LibIOURing.io_uring_register(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nio_uring_enter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibIOURing.nio_uring_enter(int,int,int,int,long)"""
        return int._wrap(_LibIOURing.nio_uring_enter(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def io_uring_enter2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibIOURing.io_uring_enter2(int,int,int,int,long,int)"""
        return int._wrap(_LibIOURing.io_uring_enter2(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5)))

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def io_uring_enter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.LibIOURing.io_uring_enter(int,int,int,int,long)"""
        return int._wrap(_LibIOURing.io_uring_enter(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

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
    def io_uring_setup(arg0: int, arg1: 'IOURingParams') -> int:
        """public static int org.lwjgl.system.linux.liburing.LibIOURing.io_uring_setup(int,org.lwjgl.system.linux.liburing.IOURingParams)"""
        return int._wrap(_LibIOURing.io_uring_setup(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nio_uring_setup(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibIOURing.nio_uring_setup(int,long)"""
        return int._wrap(_LibIOURing.nio_uring_setup(_int.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nio_uring_register(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.linux.liburing.LibIOURing.nio_uring_register(int,int,long,int)"""
        return int._wrap(_LibIOURing.nio_uring_register(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRecvmsgOut
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.linux.liburing.IOURingRecvmsgOut as _IOURingRecvmsgOut_Buffer
_Buffer = _IOURingRecvmsgOut_Buffer.Buffer
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
import org.lwjgl.system.linux.liburing.IOURingRecvmsgOut as _IOURingRecvmsgOut
_IOURingRecvmsgOut = _IOURingRecvmsgOut
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingRecvmsgOut():
    """org.lwjgl.system.linux.liburing.IOURingRecvmsgOut"""
 
    @staticmethod
    def _wrap(java_value: _IOURingRecvmsgOut) -> 'IOURingRecvmsgOut':
        return IOURingRecvmsgOut(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingRecvmsgOut):
        """
        Dynamic initializer for IOURingRecvmsgOut.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingRecvmsgOut__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingRecvmsgOut__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def payloadlen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.payloadlen()"""
        return int._wrap(super(IOURingRecvmsgOut, self).payloadlen())

    @overload
    def namelen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.namelen()"""
        return int._wrap(super(IOURingRecvmsgOut, self).namelen())

    @staticmethod
    @overload
    def nnamelen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.nnamelen(long)"""
        return int._wrap(_IOURingRecvmsgOut.nnamelen(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingRecvmsgOut') -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.set(org.lwjgl.system.linux.liburing.IOURingRecvmsgOut)"""
        return 'IOURingRecvmsgOut'._wrap(super(_IOURingRecvmsgOut, self).set(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.createSafe(long)"""
        return IOURingRecvmsgOut._wrap(_IOURingRecvmsgOut.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRecvmsgOut.calloc(_int.valueOf(arg0), arg1))

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
    def malloc() -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.malloc()"""
        return IOURingRecvmsgOut._wrap(_IOURingRecvmsgOut.malloc())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRecvmsgOut.malloc(_int.valueOf(arg0), arg1))

    @overload
    def controllen(self, arg0: int) -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.controllen(int)"""
        return 'IOURingRecvmsgOut'._wrap(super(_IOURingRecvmsgOut, self).controllen(_int.valueOf(arg0)))

    @overload
    def payloadlen(self, arg0: int) -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.payloadlen(int)"""
        return 'IOURingRecvmsgOut'._wrap(super(_IOURingRecvmsgOut, self).payloadlen(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncontrollen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.ncontrollen(long,int)"""
        _IOURingRecvmsgOut.ncontrollen(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRecvmsgOut._wrap(_IOURingRecvmsgOut.malloc(arg0))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.flags()"""
        return int._wrap(super(IOURingRecvmsgOut, self).flags())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.set(int,int,int,int)"""
        return 'IOURingRecvmsgOut'._wrap(super(_IOURingRecvmsgOut, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.sizeof()"""
        return int._wrap(super(IOURingRecvmsgOut, self).sizeof())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut(java.nio.ByteBuffer)"""
        val = _IOURingRecvmsgOut(arg0)
        self.__wrapper = val

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
    def nnamelen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.nnamelen(long,int)"""
        _IOURingRecvmsgOut.nnamelen(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.create(int)"""
        return Buffer._wrap(_IOURingRecvmsgOut.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.nflags(long)"""
        return int._wrap(_IOURingRecvmsgOut.nflags(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.malloc(int)"""
        return Buffer._wrap(_IOURingRecvmsgOut.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.nflags(long,int)"""
        _IOURingRecvmsgOut.nflags(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc() -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.calloc()"""
        return IOURingRecvmsgOut._wrap(_IOURingRecvmsgOut.calloc())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRecvmsgOut._wrap(_IOURingRecvmsgOut.calloc(arg0))

    @staticmethod
    @overload
    def create() -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.create()"""
        return IOURingRecvmsgOut._wrap(_IOURingRecvmsgOut.create())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.createSafe(long,int)"""
        return Buffer._wrap(_IOURingRecvmsgOut.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def namelen(self, arg0: int) -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.namelen(int)"""
        return 'IOURingRecvmsgOut'._wrap(super(_IOURingRecvmsgOut, self).namelen(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.create(long,int)"""
        return Buffer._wrap(_IOURingRecvmsgOut.create(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def controllen(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.controllen()"""
        return int._wrap(super(IOURingRecvmsgOut, self).controllen())

    @staticmethod
    @overload
    def npayloadlen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.npayloadlen(long)"""
        return int._wrap(_IOURingRecvmsgOut.npayloadlen(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def npayloadlen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.npayloadlen(long,int)"""
        _IOURingRecvmsgOut.npayloadlen(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def ncontrollen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.ncontrollen(long)"""
        return int._wrap(_IOURingRecvmsgOut.ncontrollen(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingRecvmsgOut':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.create(long)"""
        return IOURingRecvmsgOut._wrap(_IOURingRecvmsgOut.create(_long.valueOf(arg0)))

    @overload
    def flags(self, arg0: int) -> 'IOURingRecvmsgOut':
        """public org.lwjgl.system.linux.liburing.IOURingRecvmsgOut org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.flags(int)"""
        return 'IOURingRecvmsgOut'._wrap(super(_IOURingRecvmsgOut, self).flags(_int.valueOf(arg0)))

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
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRecvmsgOut$Buffer org.lwjgl.system.linux.liburing.IOURingRecvmsgOut.calloc(int)"""
        return Buffer._wrap(_IOURingRecvmsgOut.calloc(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingCQ
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
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
import org.lwjgl.system.linux.liburing.IOURingCQ as _IOURingCQ
_IOURingCQ = _IOURingCQ
import java.lang.Integer as _int
import org.lwjgl.system.linux.liburing.IOURingCQ as _IOURingCQ_Buffer
_Buffer = _IOURingCQ_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import org.lwjgl.system.linux.liburing.IOURingCQE as _IOURingCQE
_IOURingCQE = _IOURingCQE
import java.lang.Class as _Class
_Class = _Class
 
class IOURingCQ():
    """org.lwjgl.system.linux.liburing.IOURingCQ"""
 
    @staticmethod
    def _wrap(java_value: _IOURingCQ) -> 'IOURingCQ':
        return IOURingCQ(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingCQ):
        """
        Dynamic initializer for IOURingCQ.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingCQ__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingCQ__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'IOURingCQ') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.set(org.lwjgl.system.linux.liburing.IOURingCQ)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).set(arg0))

    @overload
    def kring_entries(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.kring_entries(int)"""
        return 'IntBuffer'._wrap(super(_IOURingCQ, self).kring_entries(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.npad(long,java.nio.IntBuffer)"""
        _IOURingCQ.npad(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def malloc() -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.malloc()"""
        return IOURingCQ._wrap(_IOURingCQ.malloc())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingCQ.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nkring_entries(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nkring_entries(long,java.nio.IntBuffer)"""
        _IOURingCQ.nkring_entries(_long.valueOf(arg0), arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nring_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingCQ.nring_entries(long)"""
        return int._wrap(_IOURingCQ.nring_entries(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nring_entries(long,int)"""
        _IOURingCQ.nring_entries(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def ring_ptr(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingCQ.ring_ptr()"""
        return 'ByteBuffer'._wrap(super(IOURingCQ, self).ring_ptr())

    @staticmethod
    @overload
    def nring_ptr(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nring_ptr(long,java.nio.ByteBuffer)"""
        _IOURingCQ.nring_ptr(_long.valueOf(arg0), arg1)

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
    def nring_mask(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingCQ.nring_mask(long)"""
        return int._wrap(_IOURingCQ.nring_mask(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nkring_entries(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nkring_entries(long,int)"""
        return IntBuffer._wrap(_IOURingCQ.nkring_entries(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.createSafe(long,int)"""
        return Buffer._wrap(_IOURingCQ.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.validate(long)"""
        _IOURingCQ.validate(_long.valueOf(arg0))

    @overload
    def cqes(self) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQ.cqes()"""
        return 'IOURingCQE'._wrap(super(IOURingCQ, self).cqes())

    @overload
    def cqes(self, arg0: 'IOURingCQE') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.cqes(org.lwjgl.system.linux.liburing.IOURingCQE)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).cqes(arg0))

    @overload
    def ring_entries(self, arg0: int) -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.ring_entries(int)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).ring_entries(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nkhead(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nkhead(long,int)"""
        return IntBuffer._wrap(_IOURingCQ.nkhead(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def koverflow(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.koverflow(int)"""
        return 'IntBuffer'._wrap(super(_IOURingCQ, self).koverflow(_int.valueOf(arg0)))

    @overload
    def ktail(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.ktail(int)"""
        return 'IntBuffer'._wrap(super(_IOURingCQ, self).ktail(_int.valueOf(arg0)))

    @overload
    def khead(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.khead(int)"""
        return 'IntBuffer'._wrap(super(_IOURingCQ, self).khead(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nkflags(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nkflags(long,java.nio.IntBuffer)"""
        _IOURingCQ.nkflags(_long.valueOf(arg0), arg1)

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingCQ._wrap(_IOURingCQ.malloc(arg0))

    @staticmethod
    @overload
    def ncqes(arg0: int) -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQ.ncqes(long)"""
        return IOURingCQE._wrap(_IOURingCQ.ncqes(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nkring_mask(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nkring_mask(long,java.nio.IntBuffer)"""
        _IOURingCQ.nkring_mask(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nktail(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nktail(long,int)"""
        return IntBuffer._wrap(_IOURingCQ.nktail(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def nring_sz(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingCQ.nring_sz(long)"""
        return int._wrap(_IOURingCQ.nring_sz(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingCQ(java.nio.ByteBuffer)"""
        val = _IOURingCQ(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.malloc(int)"""
        return Buffer._wrap(_IOURingCQ.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.npad(long,int,int)"""
        _IOURingCQ.npad(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def kring_mask(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.kring_mask(int)"""
        return 'IntBuffer'._wrap(super(_IOURingCQ, self).kring_mask(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_sz(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nring_sz(long,long)"""
        _IOURingCQ.nring_sz(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.create(long)"""
        return IOURingCQ._wrap(_IOURingCQ.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nkoverflow(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nkoverflow(long,java.nio.IntBuffer)"""
        _IOURingCQ.nkoverflow(_long.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.create(long,int)"""
        return Buffer._wrap(_IOURingCQ.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def ktail(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.ktail(java.nio.IntBuffer)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).ktail(arg0))

    @overload
    def set(self, arg0: 'IntBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IOURingCQE', arg7: 'ByteBuffer', arg8: int, arg9: int) -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.set(java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.system.linux.liburing.IOURingCQE,java.nio.ByteBuffer,int,int)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).set(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, _int.valueOf(arg8), _int.valueOf(arg9)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.createSafe(long)"""
        return IOURingCQ._wrap(_IOURingCQ.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.calloc(int)"""
        return Buffer._wrap(_IOURingCQ.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_mask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nring_mask(long,int)"""
        _IOURingCQ.nring_mask(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingCQ._wrap(_IOURingCQ.calloc(arg0))

    @overload
    def khead(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.khead(java.nio.IntBuffer)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).khead(arg0))

    @staticmethod
    @overload
    def nktail(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nktail(long,java.nio.IntBuffer)"""
        _IOURingCQ.nktail(_long.valueOf(arg0), arg1)

    @overload
    def kflags(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.kflags(int)"""
        return 'IntBuffer'._wrap(super(_IOURingCQ, self).kflags(_int.valueOf(arg0)))

    @overload
    def kflags(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.kflags(java.nio.IntBuffer)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).kflags(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def ncqes(arg0: int, arg1: 'IOURingCQE'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.ncqes(long,org.lwjgl.system.linux.liburing.IOURingCQE)"""
        _IOURingCQ.ncqes(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingCQ.malloc(_int.valueOf(arg0), arg1))

    @overload
    def ring_ptr(self, arg0: 'ByteBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.ring_ptr(java.nio.ByteBuffer)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).ring_ptr(arg0))

    @staticmethod
    @overload
    def npad(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.npad(long)"""
        return IntBuffer._wrap(_IOURingCQ.npad(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_ptr(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nring_ptr(long)"""
        return ByteBuffer._wrap(_IOURingCQ.nring_ptr(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nkhead(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQ.nkhead(long,java.nio.IntBuffer)"""
        _IOURingCQ.nkhead(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ.create(int)"""
        return Buffer._wrap(_IOURingCQ.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.calloc()"""
        return IOURingCQ._wrap(_IOURingCQ.calloc())

    @staticmethod
    @overload
    def nkring_mask(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nkring_mask(long,int)"""
        return IntBuffer._wrap(_IOURingCQ.nkring_mask(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def kring_entries(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.kring_entries(java.nio.IntBuffer)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).kring_entries(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQ.ring_mask()"""
        return int._wrap(super(IOURingCQ, self).ring_mask())

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingCQ.npad(long,int)"""
        return int._wrap(_IOURingCQ.npad(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def kring_mask(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.kring_mask(java.nio.IntBuffer)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).kring_mask(arg0))

    @staticmethod
    @overload
    def create() -> 'IOURingCQ':
        """public static org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.create()"""
        return IOURingCQ._wrap(_IOURingCQ.create())

    @staticmethod
    @overload
    def nkoverflow(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nkoverflow(long,int)"""
        return IntBuffer._wrap(_IOURingCQ.nkoverflow(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def koverflow(self, arg0: 'IntBuffer') -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.koverflow(java.nio.IntBuffer)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).koverflow(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQ.sizeof()"""
        return int._wrap(super(IOURingCQ, self).sizeof())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @overload
    def ring_mask(self, arg0: int) -> 'IOURingCQ':
        """public org.lwjgl.system.linux.liburing.IOURingCQ org.lwjgl.system.linux.liburing.IOURingCQ.ring_mask(int)"""
        return 'IOURingCQ'._wrap(super(_IOURingCQ, self).ring_mask(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nkflags(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ.nkflags(long,int)"""
        return IntBuffer._wrap(_IOURingCQ.nkflags(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def ring_sz(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQ.ring_sz()"""
        return int._wrap(super(IOURingCQ, self).ring_sz())

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQ.ring_entries()"""
        return int._wrap(super(IOURingCQ, self).ring_entries())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBufReg
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
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Integer as _int
import org.lwjgl.system.linux.liburing.IOURingBufReg as _IOURingBufReg_Buffer
_Buffer = _IOURingBufReg_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.linux.liburing.IOURingBufReg as _IOURingBufReg
_IOURingBufReg = _IOURingBufReg
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingBufReg():
    """org.lwjgl.system.linux.liburing.IOURingBufReg"""
 
    @staticmethod
    def _wrap(java_value: _IOURingBufReg) -> 'IOURingBufReg':
        return IOURingBufReg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingBufReg):
        """
        Dynamic initializer for IOURingBufReg.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingBufReg__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingBufReg__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def flags(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufReg.flags()"""
        return int._wrap(super(IOURingBufReg, self).flags())

    @staticmethod
    @overload
    def nring_addr(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingBufReg.nring_addr(long)"""
        return int._wrap(_IOURingBufReg.nring_addr(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.create(int)"""
        return Buffer._wrap(_IOURingBufReg.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.malloc()"""
        return IOURingBufReg._wrap(_IOURingBufReg.malloc())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def resv(self, arg0: 'LongBuffer') -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.resv(java.nio.LongBuffer)"""
        return 'IOURingBufReg'._wrap(super(_IOURingBufReg, self).resv(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.createSafe(long)"""
        return IOURingBufReg._wrap(_IOURingBufReg.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create() -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.create()"""
        return IOURingBufReg._wrap(_IOURingBufReg.create())

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nresv(long,int,long)"""
        _IOURingBufReg.nresv(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingBufReg.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufReg.sizeof()"""
        return int._wrap(super(IOURingBufReg, self).sizeof())

    @staticmethod
    @overload
    def calloc() -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.calloc()"""
        return IOURingBufReg._wrap(_IOURingBufReg.calloc())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: 'LongBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nresv(long,java.nio.LongBuffer)"""
        _IOURingBufReg.nresv(_long.valueOf(arg0), arg1)

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
    def nresv(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingBufReg.nresv(long,int)"""
        return int._wrap(_IOURingBufReg.nresv(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def resv(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingBufReg.resv()"""
        return 'LongBuffer'._wrap(super(IOURingBufReg, self).resv())

    @overload
    def bgid(self, arg0: int) -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.bgid(short)"""
        return 'IOURingBufReg'._wrap(super(_IOURingBufReg, self).bgid(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBufReg.nflags(long)"""
        return int._wrap(_IOURingBufReg.nflags(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'LongBuffer') -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.set(long,int,short,short,java.nio.LongBuffer)"""
        return 'IOURingBufReg'._wrap(super(_IOURingBufReg, self).set(_long.valueOf(arg0), _int.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), arg4))

    @overload
    def bgid(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufReg.bgid()"""
        return int._wrap(super(IOURingBufReg, self).bgid())

    @overload
    def resv(self, arg0: int, arg1: int) -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.resv(int,long)"""
        return 'IOURingBufReg'._wrap(super(_IOURingBufReg, self).resv(_int.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufReg.ring_entries()"""
        return int._wrap(super(IOURingBufReg, self).ring_entries())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def set(self, arg0: 'IOURingBufReg') -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.set(org.lwjgl.system.linux.liburing.IOURingBufReg)"""
        return 'IOURingBufReg'._wrap(super(_IOURingBufReg, self).set(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.calloc(int)"""
        return Buffer._wrap(_IOURingBufReg.calloc(_int.valueOf(arg0)))

    @overload
    def ring_addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufReg.ring_addr()"""
        return int._wrap(super(IOURingBufReg, self).ring_addr())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingBufReg(java.nio.ByteBuffer)"""
        val = _IOURingBufReg(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.malloc(int)"""
        return Buffer._wrap(_IOURingBufReg.malloc(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.createSafe(long,int)"""
        return Buffer._wrap(_IOURingBufReg.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBufReg._wrap(_IOURingBufReg.malloc(arg0))

    @overload
    def flags(self, arg0: int) -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.flags(short)"""
        return 'IOURingBufReg'._wrap(super(_IOURingBufReg, self).flags(_short.valueOf(arg0)))

    @overload
    def resv(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufReg.resv(int)"""
        return int._wrap(super(_IOURingBufReg, self).resv(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_addr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nring_addr(long,long)"""
        _IOURingBufReg.nring_addr(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.create(long,int)"""
        return Buffer._wrap(_IOURingBufReg.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def ring_addr(self, arg0: int) -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.ring_addr(long)"""
        return 'IOURingBufReg'._wrap(super(_IOURingBufReg, self).ring_addr(_long.valueOf(arg0)))

    @overload
    def ring_entries(self, arg0: int) -> 'IOURingBufReg':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.ring_entries(int)"""
        return 'IOURingBufReg'._wrap(super(_IOURingBufReg, self).ring_entries(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBufReg._wrap(_IOURingBufReg.calloc(arg0))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nflags(long,short)"""
        _IOURingBufReg.nflags(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def nring_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingBufReg.nring_entries(long)"""
        return int._wrap(_IOURingBufReg.nring_entries(_long.valueOf(arg0)))

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
    def nbgid(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBufReg.nbgid(long)"""
        return int._wrap(_IOURingBufReg.nbgid(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingBufReg.nresv(long)"""
        return LongBuffer._wrap(_IOURingBufReg.nresv(_long.valueOf(arg0)))

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
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingBufReg.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nring_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nring_entries(long,int)"""
        _IOURingBufReg.nring_entries(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nbgid(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufReg.nbgid(long,short)"""
        _IOURingBufReg.nbgid(_long.valueOf(arg0), _short.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingBufReg':
        """public static org.lwjgl.system.linux.liburing.IOURingBufReg org.lwjgl.system.linux.liburing.IOURingBufReg.create(long)"""
        return IOURingBufReg._wrap(_IOURingBufReg.create(_long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingProbe
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.lang.Short as _short
import java.util.function.Consumer as Consumer
import java.lang.Byte as _byte
import org.lwjgl.system.linux.liburing.IOURingProbeOp as _IOURingProbeOp_Buffer
_Buffer = _IOURingProbeOp_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.linux.liburing.IOURingProbeOp as _IOURingProbeOp
_IOURingProbeOp = _IOURingProbeOp
import org.lwjgl.system.linux.liburing.IOURingProbe as _IOURingProbe
_IOURingProbe = _IOURingProbe
import org.lwjgl.system.linux.liburing.IOURingProbe as _IOURingProbe_Buffer
_Buffer = _IOURingProbe_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingProbe():
    """org.lwjgl.system.linux.liburing.IOURingProbe"""
 
    @staticmethod
    def _wrap(java_value: _IOURingProbe) -> 'IOURingProbe':
        return IOURingProbe(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingProbe):
        """
        Dynamic initializer for IOURingProbe.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingProbe__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingProbe__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def ops(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbe.ops(int)"""
        return 'IOURingProbeOp'._wrap(super(_IOURingProbe, self).ops(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingProbe._wrap(_IOURingProbe.calloc(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.createSafe(long,int)"""
        return Buffer._wrap(_IOURingProbe.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.createSafe(long)"""
        return IOURingProbe._wrap(_IOURingProbe.createSafe(_long.valueOf(arg0)))

    @overload
    def ops_len(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbe.ops_len()"""
        return int._wrap(super(IOURingProbe, self).ops_len())

    @staticmethod
    @overload
    def create() -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.create()"""
        return IOURingProbe._wrap(_IOURingProbe.create())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingProbe.sizeof()"""
        return int._wrap(super(IOURingProbe, self).sizeof())

    @staticmethod
    @overload
    def nops(arg0: int, arg1: int) -> 'IOURingProbeOp':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbe.nops(long,int)"""
        return IOURingProbeOp._wrap(_IOURingProbe.nops(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.create(long)"""
        return IOURingProbe._wrap(_IOURingProbe.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingProbe.nresv2(long,int)"""
        return int._wrap(_IOURingProbe.nresv2(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def nops(arg0: int, arg1: 'Buffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nops(long,org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer)"""
        _IOURingProbe.nops(_long.valueOf(arg0), arg1)

    @overload
    def resv(self, arg0: int) -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.resv(short)"""
        return 'IOURingProbe'._wrap(super(_IOURingProbe, self).resv(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def nops(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.nops(long)"""
        return Buffer._wrap(_IOURingProbe.nops(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingProbe._wrap(_IOURingProbe.malloc(arg0))

    @staticmethod
    @overload
    def nlast_op(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nlast_op(long,byte)"""
        _IOURingProbe.nlast_op(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nresv2(long,int,int)"""
        _IOURingProbe.nresv2(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nops(arg0: int, arg1: int, arg2: 'IOURingProbeOp'):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nops(long,int,org.lwjgl.system.linux.liburing.IOURingProbeOp)"""
        _IOURingProbe.nops(_long.valueOf(arg0), _int.valueOf(arg1), arg2)

    @overload
    def ops_len(self, arg0: int) -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.ops_len(byte)"""
        return 'IOURingProbe'._wrap(super(_IOURingProbe, self).ops_len(_byte.valueOf(arg0)))

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
    def ops(self, arg0: 'Consumer') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.ops(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer>)"""
        return 'IOURingProbe'._wrap(super(_IOURingProbe, self).ops(arg0))

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingProbe.nresv(long)"""
        return int._wrap(_IOURingProbe.nresv(_long.valueOf(arg0)))

    @overload
    def ops(self, arg0: 'Buffer') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.ops(org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer)"""
        return 'IOURingProbe'._wrap(super(_IOURingProbe, self).ops(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.set(byte,byte,short,org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer)"""
        return 'IOURingProbe'._wrap(super(_IOURingProbe, self).set(_byte.valueOf(arg0), _byte.valueOf(arg1), _short.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.create(long,int)"""
        return Buffer._wrap(_IOURingProbe.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def last_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbe.last_op()"""
        return int._wrap(super(IOURingProbe, self).last_op())

    @staticmethod
    @overload
    def nops_len(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingProbe.nops_len(long)"""
        return int._wrap(_IOURingProbe.nops_len(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nresv2(long,java.nio.IntBuffer)"""
        _IOURingProbe.nresv2(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.create(int)"""
        return Buffer._wrap(_IOURingProbe.create(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def ops(self) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.ops()"""
        return 'Buffer'._wrap(super(IOURingProbe, self).ops())

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nresv(long,short)"""
        _IOURingProbe.nresv(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.malloc(int)"""
        return Buffer._wrap(_IOURingProbe.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nlast_op(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingProbe.nlast_op(long)"""
        return int._wrap(_IOURingProbe.nlast_op(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nops_len(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingProbe.nops_len(long,byte)"""
        _IOURingProbe.nops_len(_long.valueOf(arg0), _byte.valueOf(arg1))

    @overload
    def ops(self, arg0: int, arg1: 'Consumer') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.ops(int,java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingProbeOp>)"""
        return 'IOURingProbe'._wrap(super(_IOURingProbe, self).ops(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc() -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.calloc()"""
        return IOURingProbe._wrap(_IOURingProbe.calloc())

    @staticmethod
    @overload
    def malloc() -> 'IOURingProbe':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.malloc()"""
        return IOURingProbe._wrap(_IOURingProbe.malloc())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingProbe.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingProbe.calloc(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingProbe(java.nio.ByteBuffer)"""
        val = _IOURingProbe(arg0)
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

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe.calloc(int)"""
        return Buffer._wrap(_IOURingProbe.calloc(_int.valueOf(arg0)))

    @overload
    def resv(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingProbe.resv()"""
        return int._wrap(super(IOURingProbe, self).resv())

    @overload
    def set(self, arg0: 'IOURingProbe') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.set(org.lwjgl.system.linux.liburing.IOURingProbe)"""
        return 'IOURingProbe'._wrap(super(_IOURingProbe, self).set(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def ops(self, arg0: int, arg1: 'IOURingProbeOp') -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.ops(int,org.lwjgl.system.linux.liburing.IOURingProbeOp)"""
        return 'IOURingProbe'._wrap(super(_IOURingProbe, self).ops(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nresv2(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingProbe.nresv2(long)"""
        return IntBuffer._wrap(_IOURingProbe.nresv2(_long.valueOf(arg0)))

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
    def last_op(self, arg0: int) -> 'IOURingProbe':
        """public org.lwjgl.system.linux.liburing.IOURingProbe org.lwjgl.system.linux.liburing.IOURingProbe.last_op(byte)"""
        return 'IOURingProbe'._wrap(super(_IOURingProbe, self).last_op(_byte.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSQ$Buffer
from pyquantum_helper import import_once as _import_once
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
import org.lwjgl.system.linux.liburing.IOURingSQ as _IOURingSQ_Buffer
_Buffer = _IOURingSQ_Buffer.Buffer
import org.lwjgl.system.linux.liburing.IOURingSQE as _IOURingSQE
_IOURingSQE = _IOURingSQE
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingSQ.Buffer"""
 
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
    def sqe_head(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqe_head(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).sqe_head(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def kdropped(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kdropped(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).kdropped(_int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def kflags(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kflags(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).kflags(arg0))

    @overload
    def sqe_head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqe_head()"""
        return int._wrap(super(Buffer, self).sqe_head())

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
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_mask()"""
        return int._wrap(super(Buffer, self).ring_mask())

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
    def khead(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.khead(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).khead(arg0))

    @overload
    def sqes(self, arg0: 'IOURingSQE') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqes(org.lwjgl.system.linux.liburing.IOURingSQE)"""
        return 'Buffer'._wrap(super(_Buffer, self).sqes(arg0))

    @overload
    def kflags(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kflags(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).kflags(_int.valueOf(arg0)))

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
    def kring_entries(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kring_entries(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).kring_entries(arg0))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def ring_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_entries(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_entries(_int.valueOf(arg0)))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def kring_mask(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kring_mask(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).kring_mask(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def ring_ptr(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_ptr(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_ptr(arg0))

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
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_entries()"""
        return int._wrap(super(Buffer, self).ring_entries())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def ktail(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ktail(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).ktail(arg0))

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
    def khead(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.khead(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).khead(_int.valueOf(arg0)))

    @overload
    def kring_mask(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kring_mask(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).kring_mask(_int.valueOf(arg0)))

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
    def sqes(self) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqes()"""
        return 'IOURingSQE'._wrap(super(Buffer, self).sqes())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def array(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.array(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).array(_int.valueOf(arg0)))

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
    def kring_entries(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kring_entries(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).kring_entries(_int.valueOf(arg0)))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def ring_ptr(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_ptr()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).ring_ptr())

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
    def ring_sz(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_sz()"""
        return int._wrap(super(Buffer, self).ring_sz())

    @overload
    def sqe_tail(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqe_tail(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).sqe_tail(_int.valueOf(arg0)))

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
    def kdropped(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.kdropped(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).kdropped(arg0))

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
    def array(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.array(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).array(arg0))

    @overload
    def sqe_tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.sqe_tail()"""
        return int._wrap(super(Buffer, self).sqe_tail())

    @overload
    def ktail(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ktail(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).ktail(_int.valueOf(arg0)))

    @overload
    def ring_mask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ$Buffer.ring_mask(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_mask(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOSQRingOffsets
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
import org.lwjgl.system.linux.liburing.IOSQRingOffsets as _IOSQRingOffsets
_IOSQRingOffsets = _IOSQRingOffsets
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.linux.liburing.IOSQRingOffsets as _IOSQRingOffsets_Buffer
_Buffer = _IOSQRingOffsets_Buffer.Buffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOSQRingOffsets():
    """org.lwjgl.system.linux.liburing.IOSQRingOffsets"""
 
    @staticmethod
    def _wrap(java_value: _IOSQRingOffsets) -> 'IOSQRingOffsets':
        return IOSQRingOffsets(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOSQRingOffsets):
        """
        Dynamic initializer for IOSQRingOffsets.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOSQRingOffsets__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOSQRingOffsets__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def dropped(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.dropped(int)"""
        return 'IOSQRingOffsets'._wrap(super(_IOSQRingOffsets, self).dropped(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ntail(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.ntail(long,int)"""
        _IOSQRingOffsets.ntail(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.createSafe(long)"""
        return IOSQRingOffsets._wrap(_IOSQRingOffsets.createSafe(_long.valueOf(arg0)))

    @overload
    def array(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.array(int)"""
        return 'IOSQRingOffsets'._wrap(super(_IOSQRingOffsets, self).array(_int.valueOf(arg0)))

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.ring_mask()"""
        return int._wrap(super(IOSQRingOffsets, self).ring_mask())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nring_mask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nring_mask(long,int)"""
        _IOSQRingOffsets.nring_mask(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def ring_entries(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.ring_entries(int)"""
        return 'IOSQRingOffsets'._wrap(super(_IOSQRingOffsets, self).ring_entries(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nhead(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.nhead(long)"""
        return int._wrap(_IOSQRingOffsets.nhead(_long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.sizeof()"""
        return int._wrap(super(IOSQRingOffsets, self).sizeof())

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.nflags(long)"""
        return int._wrap(_IOSQRingOffsets.nflags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.calloc(org.lwjgl.system.MemoryStack)"""
        return IOSQRingOffsets._wrap(_IOSQRingOffsets.calloc(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.createSafe(long,int)"""
        return Buffer._wrap(_IOSQRingOffsets.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nresv1(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nresv1(long,int)"""
        _IOSQRingOffsets.nresv1(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nresv2(long,long)"""
        _IOSQRingOffsets.nresv2(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.tail()"""
        return int._wrap(super(IOSQRingOffsets, self).tail())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def array(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.array()"""
        return int._wrap(super(IOSQRingOffsets, self).array())

    @overload
    def tail(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.tail(int)"""
        return 'IOSQRingOffsets'._wrap(super(_IOSQRingOffsets, self).tail(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.calloc(int)"""
        return Buffer._wrap(_IOSQRingOffsets.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOSQRingOffsets.nresv2(long)"""
        return int._wrap(_IOSQRingOffsets.nresv2(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.malloc(int)"""
        return Buffer._wrap(_IOSQRingOffsets.malloc(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.set(int,int,int,int,int,int,int)"""
        return 'IOSQRingOffsets'._wrap(super(_IOSQRingOffsets, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

    @overload
    def ring_mask(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.ring_mask(int)"""
        return 'IOSQRingOffsets'._wrap(super(_IOSQRingOffsets, self).ring_mask(_int.valueOf(arg0)))

    @overload
    def flags(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.flags(int)"""
        return 'IOSQRingOffsets'._wrap(super(_IOSQRingOffsets, self).flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.create(long,int)"""
        return Buffer._wrap(_IOSQRingOffsets.create(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def narray(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.narray(long)"""
        return int._wrap(_IOSQRingOffsets.narray(_long.valueOf(arg0)))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.flags()"""
        return int._wrap(super(IOSQRingOffsets, self).flags())

    @overload
    def dropped(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.dropped()"""
        return int._wrap(super(IOSQRingOffsets, self).dropped())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOSQRingOffsets.malloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.malloc(org.lwjgl.system.MemoryStack)"""
        return IOSQRingOffsets._wrap(_IOSQRingOffsets.malloc(arg0))

    @staticmethod
    @overload
    def narray(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.narray(long,int)"""
        _IOSQRingOffsets.narray(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets(java.nio.ByteBuffer)"""
        val = _IOSQRingOffsets(arg0)
        self.__wrapper = val

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def head(self, arg0: int) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.head(int)"""
        return 'IOSQRingOffsets'._wrap(super(_IOSQRingOffsets, self).head(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def ndropped(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.ndropped(long,int)"""
        _IOSQRingOffsets.ndropped(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc() -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.calloc()"""
        return IOSQRingOffsets._wrap(_IOSQRingOffsets.calloc())

    @overload
    def head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.head()"""
        return int._wrap(super(IOSQRingOffsets, self).head())

    @staticmethod
    @overload
    def ndropped(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.ndropped(long)"""
        return int._wrap(_IOSQRingOffsets.ndropped(_long.valueOf(arg0)))

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOSQRingOffsets.ring_entries()"""
        return int._wrap(super(IOSQRingOffsets, self).ring_entries())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.create(int)"""
        return Buffer._wrap(_IOSQRingOffsets.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nhead(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nhead(long,int)"""
        _IOSQRingOffsets.nhead(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.create(long)"""
        return IOSQRingOffsets._wrap(_IOSQRingOffsets.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_mask(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.nring_mask(long)"""
        return int._wrap(_IOSQRingOffsets.nring_mask(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOSQRingOffsets') -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.set(org.lwjgl.system.linux.liburing.IOSQRingOffsets)"""
        return 'IOSQRingOffsets'._wrap(super(_IOSQRingOffsets, self).set(arg0))

    @staticmethod
    @overload
    def nring_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nring_entries(long,int)"""
        _IOSQRingOffsets.nring_entries(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def malloc() -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.malloc()"""
        return IOSQRingOffsets._wrap(_IOSQRingOffsets.malloc())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOSQRingOffsets.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOSQRingOffsets.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nring_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.nring_entries(long)"""
        return int._wrap(_IOSQRingOffsets.nring_entries(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOSQRingOffsets.create()"""
        return IOSQRingOffsets._wrap(_IOSQRingOffsets.create())

    @staticmethod
    @overload
    def ntail(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.ntail(long)"""
        return int._wrap(_IOSQRingOffsets.ntail(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nresv1(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOSQRingOffsets.nresv1(long)"""
        return int._wrap(_IOSQRingOffsets.nresv1(_long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOSQRingOffsets.nflags(long,int)"""
        _IOSQRingOffsets.nflags(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingCQ$Buffer
from pyquantum_helper import import_once as _import_once
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
import org.lwjgl.system.linux.liburing.IOURingCQ as _IOURingCQ_Buffer
_Buffer = _IOURingCQ_Buffer.Buffer
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import org.lwjgl.system.linux.liburing.IOURingCQE as _IOURingCQE
_IOURingCQE = _IOURingCQE
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingCQ.Buffer"""
 
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
    def kflags(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kflags(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).kflags(arg0))

    @overload
    def ring_ptr(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_ptr()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).ring_ptr())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def ring_mask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_mask(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_mask(_int.valueOf(arg0)))

    @overload
    def khead(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.khead(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).khead(arg0))

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
    def ring_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_entries(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_entries(_int.valueOf(arg0)))

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
    def ring_ptr(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_ptr(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_ptr(arg0))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def kring_mask(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kring_mask(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).kring_mask(arg0))

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_mask()"""
        return int._wrap(super(Buffer, self).ring_mask())

    @overload
    def koverflow(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.koverflow(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).koverflow(arg0))

    @overload
    def ktail(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ktail(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).ktail(_int.valueOf(arg0)))

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
    def kring_mask(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kring_mask(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).kring_mask(_int.valueOf(arg0)))

    @overload
    def cqes(self, arg0: 'IOURingCQE') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.cqes(org.lwjgl.system.linux.liburing.IOURingCQE)"""
        return 'Buffer'._wrap(super(_Buffer, self).cqes(arg0))

    @overload
    def ring_sz(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_sz()"""
        return int._wrap(super(Buffer, self).ring_sz())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def ktail(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ktail(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).ktail(arg0))

    @overload
    def khead(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.khead(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).khead(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def koverflow(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.koverflow(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).koverflow(_int.valueOf(arg0)))

    @overload
    def kring_entries(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQ$Buffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kring_entries(java.nio.IntBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).kring_entries(arg0))

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
    def cqes(self) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.cqes()"""
        return 'IOURingCQE'._wrap(super(Buffer, self).cqes())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def kflags(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kflags(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).kflags(_int.valueOf(arg0)))

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
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.ring_entries()"""
        return int._wrap(super(Buffer, self).ring_entries())

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
    def kring_entries(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingCQ$Buffer.kring_entries(int)"""
        return 'IntBuffer'._wrap(super(_Buffer, self).kring_entries(_int.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer
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
import org.lwjgl.system.linux.liburing.IOURingFileIndexRange as _IOURingFileIndexRange_Buffer
_Buffer = _IOURingFileIndexRange_Buffer.Buffer
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
    """org.lwjgl.system.linux.liburing.IOURingFileIndexRange.Buffer"""
 
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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def len(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.len(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).len(_int.valueOf(arg0)))

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
    def resv(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.resv()"""
        return int._wrap(super(Buffer, self).resv())

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
    def off(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.off(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).off(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def off(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.off()"""
        return int._wrap(super(Buffer, self).off())

    @overload
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.resv(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv(_long.valueOf(arg0)))

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
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer(long,int)"""
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

    @overload
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer.len()"""
        return int._wrap(super(Buffer, self).len())

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
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBufRing
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
import org.lwjgl.system.linux.liburing.IOURingBufRing as _IOURingBufRing_Buffer
_Buffer = _IOURingBufRing_Buffer.Buffer
import org.lwjgl.system.linux.liburing.IOURingBuf as _IOURingBuf
_IOURingBuf = _IOURingBuf
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.lwjgl.system.linux.liburing.IOURingBuf as _IOURingBuf_Buffer
_Buffer = _IOURingBuf_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.linux.liburing.IOURingBufRing as _IOURingBufRing
_IOURingBufRing = _IOURingBufRing
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingBufRing():
    """org.lwjgl.system.linux.liburing.IOURingBufRing"""
 
    @staticmethod
    def _wrap(java_value: _IOURingBufRing) -> 'IOURingBufRing':
        return IOURingBufRing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingBufRing):
        """
        Dynamic initializer for IOURingBufRing.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingBufRing__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingBufRing__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def resv1(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufRing.resv1()"""
        return int._wrap(super(IOURingBufRing, self).resv1())

    @staticmethod
    @overload
    def nbufs(arg0: int, arg1: 'Buffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.nbufs(long,org.lwjgl.system.linux.liburing.IOURingBuf$Buffer)"""
        _IOURingBufRing.nbufs(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nbufs(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.nbufs(long)"""
        return Buffer._wrap(_IOURingBufRing.nbufs(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingBufRing.malloc(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: 'IOURingBufRing') -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.set(org.lwjgl.system.linux.liburing.IOURingBufRing)"""
        return 'IOURingBufRing'._wrap(super(_IOURingBufRing, self).set(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingBufRing.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def bufs(self, arg0: 'Consumer') -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.bufs(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingBuf$Buffer>)"""
        return 'IOURingBufRing'._wrap(super(_IOURingBufRing, self).bufs(arg0))

    @overload
    def bufs(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBufRing.bufs(int)"""
        return 'IOURingBuf'._wrap(super(_IOURingBufRing, self).bufs(_int.valueOf(arg0)))

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
    def nresv3(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBufRing.nresv3(long)"""
        return int._wrap(_IOURingBufRing.nresv3(_long.valueOf(arg0)))

    @overload
    def bufs(self) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.bufs()"""
        return 'Buffer'._wrap(super(IOURingBufRing, self).bufs())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.createSafe(long)"""
        return IOURingBufRing._wrap(_IOURingBufRing.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntail(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.ntail(long,short)"""
        _IOURingBufRing.ntail(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def malloc() -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.malloc()"""
        return IOURingBufRing._wrap(_IOURingBufRing.malloc())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingBufRing(java.nio.ByteBuffer)"""
        val = _IOURingBufRing(arg0)
        self.__wrapper = val

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
    def tail(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufRing.tail()"""
        return int._wrap(super(IOURingBufRing, self).tail())

    @overload
    def resv3(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufRing.resv3()"""
        return int._wrap(super(IOURingBufRing, self).resv3())

    @overload
    def bufs(self, arg0: int, arg1: 'Consumer') -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.bufs(int,java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingBuf>)"""
        return 'IOURingBufRing'._wrap(super(_IOURingBufRing, self).bufs(_int.valueOf(arg0), arg1))

    @overload
    def bufs(self, arg0: 'Buffer') -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.bufs(org.lwjgl.system.linux.liburing.IOURingBuf$Buffer)"""
        return 'IOURingBufRing'._wrap(super(_IOURingBufRing, self).bufs(arg0))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBufRing._wrap(_IOURingBufRing.malloc(arg0))

    @staticmethod
    @overload
    def nresv3(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.nresv3(long,short)"""
        _IOURingBufRing.nresv3(_long.valueOf(arg0), _short.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufRing.resv2()"""
        return int._wrap(super(IOURingBufRing, self).resv2())

    @overload
    def resv3(self, arg0: int) -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.resv3(short)"""
        return 'IOURingBufRing'._wrap(super(_IOURingBufRing, self).resv3(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBufRing._wrap(_IOURingBufRing.calloc(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.create(long)"""
        return IOURingBufRing._wrap(_IOURingBufRing.create(_long.valueOf(arg0)))

    @overload
    def resv1(self, arg0: int) -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.resv1(long)"""
        return 'IOURingBufRing'._wrap(super(_IOURingBufRing, self).resv1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv1(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingBufRing.nresv1(long)"""
        return int._wrap(_IOURingBufRing.nresv1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.create(long,int)"""
        return Buffer._wrap(_IOURingBufRing.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufRing.sizeof()"""
        return int._wrap(super(IOURingBufRing, self).sizeof())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def bufs(self, arg0: int, arg1: 'IOURingBuf') -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.bufs(int,org.lwjgl.system.linux.liburing.IOURingBuf)"""
        return 'IOURingBufRing'._wrap(super(_IOURingBufRing, self).bufs(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.calloc(int)"""
        return Buffer._wrap(_IOURingBufRing.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.createSafe(long,int)"""
        return Buffer._wrap(_IOURingBufRing.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.create(int)"""
        return Buffer._wrap(_IOURingBufRing.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.calloc()"""
        return IOURingBufRing._wrap(_IOURingBufRing.calloc())

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingBufRing.nresv2(long)"""
        return int._wrap(_IOURingBufRing.nresv2(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingBufRing':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.create()"""
        return IOURingBufRing._wrap(_IOURingBufRing.create())

    @staticmethod
    @overload
    def nresv1(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.nresv1(long,long)"""
        _IOURingBufRing.nresv1(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBufRing$Buffer org.lwjgl.system.linux.liburing.IOURingBufRing.malloc(int)"""
        return Buffer._wrap(_IOURingBufRing.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.nresv2(long,int)"""
        _IOURingBufRing.nresv2(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nbufs(arg0: int, arg1: int, arg2: 'IOURingBuf'):
        """public static void org.lwjgl.system.linux.liburing.IOURingBufRing.nbufs(long,int,org.lwjgl.system.linux.liburing.IOURingBuf)"""
        _IOURingBufRing.nbufs(_long.valueOf(arg0), _int.valueOf(arg1), arg2)

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
    def ntail(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBufRing.ntail(long)"""
        return int._wrap(_IOURingBufRing.ntail(_long.valueOf(arg0)))

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
    def tail(self, arg0: int) -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.tail(short)"""
        return 'IOURingBufRing'._wrap(super(_IOURingBufRing, self).tail(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def nbufs(arg0: int, arg1: int) -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBufRing.nbufs(long,int)"""
        return IOURingBuf._wrap(_IOURingBufRing.nbufs(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def resv2(self, arg0: int) -> 'IOURingBufRing':
        """public org.lwjgl.system.linux.liburing.IOURingBufRing org.lwjgl.system.linux.liburing.IOURingBufRing.resv2(int)"""
        return 'IOURingBufRing'._wrap(super(_IOURingBufRing, self).resv2(_int.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingParams
from pyquantum_helper import import_once as _import_once
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
import org.lwjgl.system.linux.liburing.IOURingParams as _IOURingParams_Buffer
_Buffer = _IOURingParams_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import org.lwjgl.system.linux.liburing.IOSQRingOffsets as _IOSQRingOffsets
_IOSQRingOffsets = _IOSQRingOffsets
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.linux.liburing.IOCQRingOffsets as _IOCQRingOffsets
_IOCQRingOffsets = _IOCQRingOffsets
import org.lwjgl.system.linux.liburing.IOURingParams as _IOURingParams
_IOURingParams = _IOURingParams
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingParams():
    """org.lwjgl.system.linux.liburing.IOURingParams"""
 
    @staticmethod
    def _wrap(java_value: _IOURingParams) -> 'IOURingParams':
        return IOURingParams(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingParams):
        """
        Dynamic initializer for IOURingParams.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingParams__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingParams__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ncq_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.ncq_entries(long)"""
        return int._wrap(_IOURingParams.ncq_entries(_long.valueOf(arg0)))

    @overload
    def cq_off(self, arg0: 'IOCQRingOffsets') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.cq_off(org.lwjgl.system.linux.liburing.IOCQRingOffsets)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).cq_off(arg0))

    @staticmethod
    @overload
    def nsq_thread_cpu(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nsq_thread_cpu(long)"""
        return int._wrap(_IOURingParams.nsq_thread_cpu(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsq_off(arg0: int) -> 'IOSQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams.nsq_off(long)"""
        return IOSQRingOffsets._wrap(_IOURingParams.nsq_off(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.create()"""
        return IOURingParams._wrap(_IOURingParams.create())

    @staticmethod
    @overload
    def nfeatures(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nfeatures(long)"""
        return int._wrap(_IOURingParams.nfeatures(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nsq_off(arg0: int, arg1: 'IOSQRingOffsets'):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nsq_off(long,org.lwjgl.system.linux.liburing.IOSQRingOffsets)"""
        _IOURingParams.nsq_off(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingParams.malloc(_int.valueOf(arg0), arg1))

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
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.sizeof()"""
        return int._wrap(super(IOURingParams, self).sizeof())

    @overload
    def sq_thread_idle(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.sq_thread_idle()"""
        return int._wrap(super(IOURingParams, self).sq_thread_idle())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.malloc(int)"""
        return Buffer._wrap(_IOURingParams.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.calloc(int)"""
        return Buffer._wrap(_IOURingParams.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nwq_fd(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nwq_fd(long)"""
        return int._wrap(_IOURingParams.nwq_fd(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nwq_fd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nwq_fd(long,int)"""
        _IOURingParams.nwq_fd(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resv(self, arg0: 'IntBuffer') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.resv(java.nio.IntBuffer)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).resv(arg0))

    @overload
    def sq_off(self, arg0: 'Consumer') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.sq_off(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOSQRingOffsets>)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).sq_off(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.create(long)"""
        return IOURingParams._wrap(_IOURingParams.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingParams.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ncq_off(arg0: int, arg1: 'IOCQRingOffsets'):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.ncq_off(long,org.lwjgl.system.linux.liburing.IOCQRingOffsets)"""
        _IOURingParams.ncq_off(_long.valueOf(arg0), arg1)

    @overload
    def sq_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.sq_entries()"""
        return int._wrap(super(IOURingParams, self).sq_entries())

    @overload
    def cq_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.cq_entries()"""
        return int._wrap(super(IOURingParams, self).cq_entries())

    @overload
    def features(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.features()"""
        return int._wrap(super(IOURingParams, self).features())

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nresv(long,int)"""
        return int._wrap(_IOURingParams.nresv(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nresv(long,int,int)"""
        _IOURingParams.nresv(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingParams(java.nio.ByteBuffer)"""
        val = _IOURingParams(arg0)
        self.__wrapper = val

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def resv(self, arg0: int, arg1: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.resv(int,int)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).resv(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def cq_off(self) -> 'IOCQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams.cq_off()"""
        return 'IOCQRingOffsets'._wrap(super(IOURingParams, self).cq_off())

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
    def nsq_thread_idle(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nsq_thread_idle(long)"""
        return int._wrap(_IOURingParams.nsq_thread_idle(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsq_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nsq_entries(long,int)"""
        _IOURingParams.nsq_entries(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc() -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.calloc()"""
        return IOURingParams._wrap(_IOURingParams.calloc())

    @overload
    def features(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.features(int)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).features(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nflags(long,int)"""
        _IOURingParams.nflags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nsq_thread_idle(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nsq_thread_idle(long,int)"""
        _IOURingParams.nsq_thread_idle(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def sq_thread_cpu(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.sq_thread_cpu(int)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).sq_thread_cpu(_int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def flags(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.flags(int)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.create(int)"""
        return Buffer._wrap(_IOURingParams.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nflags(long)"""
        return int._wrap(_IOURingParams.nflags(_long.valueOf(arg0)))

    @overload
    def sq_entries(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.sq_entries(int)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).sq_entries(_int.valueOf(arg0)))

    @overload
    def wq_fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.wq_fd()"""
        return int._wrap(super(IOURingParams, self).wq_fd())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def resv(self, arg0: int) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.resv(int)"""
        return int._wrap(super(_IOURingParams, self).resv(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nresv(long,java.nio.IntBuffer)"""
        _IOURingParams.nresv(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def ncq_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.ncq_entries(long,int)"""
        _IOURingParams.ncq_entries(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def cq_off(self, arg0: 'Consumer') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.cq_off(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOCQRingOffsets>)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).cq_off(arg0))

    @overload
    def sq_thread_cpu(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.sq_thread_cpu()"""
        return int._wrap(super(IOURingParams, self).sq_thread_cpu())

    @overload
    def cq_entries(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.cq_entries(int)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).cq_entries(_int.valueOf(arg0)))

    @overload
    def sq_off(self) -> 'IOSQRingOffsets':
        """public org.lwjgl.system.linux.liburing.IOSQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams.sq_off()"""
        return 'IOSQRingOffsets'._wrap(super(IOURingParams, self).sq_off())

    @staticmethod
    @overload
    def nsq_thread_cpu(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nsq_thread_cpu(long,int)"""
        _IOURingParams.nsq_thread_cpu(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nresv(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingParams.nresv(long)"""
        return IntBuffer._wrap(_IOURingParams.nresv(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.createSafe(long,int)"""
        return Buffer._wrap(_IOURingParams.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def sq_off(self, arg0: 'IOSQRingOffsets') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.sq_off(org.lwjgl.system.linux.liburing.IOSQRingOffsets)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).sq_off(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingParams._wrap(_IOURingParams.calloc(arg0))

    @overload
    def wq_fd(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.wq_fd(int)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).wq_fd(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'IntBuffer', arg8: 'IOSQRingOffsets', arg9: 'IOCQRingOffsets') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.set(int,int,int,int,int,int,int,java.nio.IntBuffer,org.lwjgl.system.linux.liburing.IOSQRingOffsets,org.lwjgl.system.linux.liburing.IOCQRingOffsets)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7, arg8, arg9))

    @staticmethod
    @overload
    def nsq_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingParams.nsq_entries(long)"""
        return int._wrap(_IOURingParams.nsq_entries(_long.valueOf(arg0)))

    @overload
    def resv(self) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingParams.resv()"""
        return 'IntBuffer'._wrap(super(IOURingParams, self).resv())

    @staticmethod
    @overload
    def ncq_off(arg0: int) -> 'IOCQRingOffsets':
        """public static org.lwjgl.system.linux.liburing.IOCQRingOffsets org.lwjgl.system.linux.liburing.IOURingParams.ncq_off(long)"""
        return IOCQRingOffsets._wrap(_IOURingParams.ncq_off(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nfeatures(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingParams.nfeatures(long,int)"""
        _IOURingParams.nfeatures(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc() -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.malloc()"""
        return IOURingParams._wrap(_IOURingParams.malloc())

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
    def set(self, arg0: 'IOURingParams') -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.set(org.lwjgl.system.linux.liburing.IOURingParams)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).set(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.createSafe(long)"""
        return IOURingParams._wrap(_IOURingParams.createSafe(_long.valueOf(arg0)))

    @overload
    def sq_thread_idle(self, arg0: int) -> 'IOURingParams':
        """public org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.sq_thread_idle(int)"""
        return 'IOURingParams'._wrap(super(_IOURingParams, self).sq_thread_idle(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingParams':
        """public static org.lwjgl.system.linux.liburing.IOURingParams org.lwjgl.system.linux.liburing.IOURingParams.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingParams._wrap(_IOURingParams.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingParams$Buffer org.lwjgl.system.linux.liburing.IOURingParams.create(long,int)"""
        return Buffer._wrap(_IOURingParams.create(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingParams.flags()"""
        return int._wrap(super(IOURingParams, self).flags())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 as _IOURingRSRCUpdate2_Buffer
_Buffer = _IOURingRSRCUpdate2_Buffer.Buffer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 as _IOURingRSRCUpdate2
_IOURingRSRCUpdate2 = _IOURingRSRCUpdate2
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
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingRSRCUpdate2():
    """org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2"""
 
    @staticmethod
    def _wrap(java_value: _IOURingRSRCUpdate2) -> 'IOURingRSRCUpdate2':
        return IOURingRSRCUpdate2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingRSRCUpdate2):
        """
        Dynamic initializer for IOURingRSRCUpdate2.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingRSRCUpdate2__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingRSRCUpdate2__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.create(int)"""
        return Buffer._wrap(_IOURingRSRCUpdate2.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCUpdate2._wrap(_IOURingRSRCUpdate2.malloc(arg0))

    @overload
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.resv2()"""
        return int._wrap(super(IOURingRSRCUpdate2, self).resv2())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.sizeof()"""
        return int._wrap(super(IOURingRSRCUpdate2, self).sizeof())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.createSafe(long)"""
        return IOURingRSRCUpdate2._wrap(_IOURingRSRCUpdate2.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.ntags(long,long)"""
        _IOURingRSRCUpdate2.ntags(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.data()"""
        return int._wrap(super(IOURingRSRCUpdate2, self).data())

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
    def nnr(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nnr(long)"""
        return int._wrap(_IOURingRSRCUpdate2.nnr(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.malloc()"""
        return IOURingRSRCUpdate2._wrap(_IOURingRSRCUpdate2.malloc())

    @staticmethod
    @overload
    def ndata(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.ndata(long)"""
        return int._wrap(_IOURingRSRCUpdate2.ndata(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.create(long,int)"""
        return Buffer._wrap(_IOURingRSRCUpdate2.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create() -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.create()"""
        return IOURingRSRCUpdate2._wrap(_IOURingRSRCUpdate2.create())

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nresv(long)"""
        return int._wrap(_IOURingRSRCUpdate2.nresv(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.set(int,int,long,long,int,int)"""
        return 'IOURingRSRCUpdate2'._wrap(super(_IOURingRSRCUpdate2, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @overload
    def nr(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nr()"""
        return int._wrap(super(IOURingRSRCUpdate2, self).nr())

    @staticmethod
    @overload
    def calloc() -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.calloc()"""
        return IOURingRSRCUpdate2._wrap(_IOURingRSRCUpdate2.calloc())

    @overload
    def resv(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.resv(int)"""
        return 'IOURingRSRCUpdate2'._wrap(super(_IOURingRSRCUpdate2, self).resv(_int.valueOf(arg0)))

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
    def nnr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nnr(long,int)"""
        _IOURingRSRCUpdate2.nnr(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCUpdate2._wrap(_IOURingRSRCUpdate2.calloc(arg0))

    @overload
    def data(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.data(long)"""
        return 'IOURingRSRCUpdate2'._wrap(super(_IOURingRSRCUpdate2, self).data(_long.valueOf(arg0)))

    @overload
    def tags(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.tags()"""
        return int._wrap(super(IOURingRSRCUpdate2, self).tags())

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
    def nresv2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nresv2(long,int)"""
        _IOURingRSRCUpdate2.nresv2(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def offset(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.offset()"""
        return int._wrap(super(IOURingRSRCUpdate2, self).offset())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nresv2(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nresv2(long)"""
        return int._wrap(_IOURingRSRCUpdate2.nresv2(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.malloc(int)"""
        return Buffer._wrap(_IOURingRSRCUpdate2.malloc(_int.valueOf(arg0)))

    @overload
    def tags(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.tags(long)"""
        return 'IOURingRSRCUpdate2'._wrap(super(_IOURingRSRCUpdate2, self).tags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingRSRCUpdate2':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.create(long)"""
        return IOURingRSRCUpdate2._wrap(_IOURingRSRCUpdate2.create(_long.valueOf(arg0)))

    @overload
    def resv(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.resv()"""
        return int._wrap(super(IOURingRSRCUpdate2, self).resv())

    @staticmethod
    @overload
    def noffset(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.noffset(long)"""
        return int._wrap(_IOURingRSRCUpdate2.noffset(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntags(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.ntags(long)"""
        return int._wrap(_IOURingRSRCUpdate2.ntags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndata(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.ndata(long,long)"""
        _IOURingRSRCUpdate2.ndata(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRSRCUpdate2.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nresv(long,int)"""
        _IOURingRSRCUpdate2.nresv(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resv2(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.resv2(int)"""
        return 'IOURingRSRCUpdate2'._wrap(super(_IOURingRSRCUpdate2, self).resv2(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.calloc(int)"""
        return Buffer._wrap(_IOURingRSRCUpdate2.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def noffset(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.noffset(long,int)"""
        _IOURingRSRCUpdate2.noffset(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: 'IOURingRSRCUpdate2') -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.set(org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2)"""
        return 'IOURingRSRCUpdate2'._wrap(super(_IOURingRSRCUpdate2, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2(java.nio.ByteBuffer)"""
        val = _IOURingRSRCUpdate2(arg0)
        self.__wrapper = val

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRSRCUpdate2.malloc(_int.valueOf(arg0), arg1))

    @overload
    def offset(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.offset(int)"""
        return 'IOURingRSRCUpdate2'._wrap(super(_IOURingRSRCUpdate2, self).offset(_int.valueOf(arg0)))

    @overload
    def nr(self, arg0: int) -> 'IOURingRSRCUpdate2':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.nr(int)"""
        return 'IOURingRSRCUpdate2'._wrap(super(_IOURingRSRCUpdate2, self).nr(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.createSafe(long,int)"""
        return Buffer._wrap(_IOURingRSRCUpdate2.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSQ
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.system.linux.liburing.IOURingSQ as _IOURingSQ
_IOURingSQ = _IOURingSQ
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.linux.liburing.IOURingSQ as _IOURingSQ_Buffer
_Buffer = _IOURingSQ_Buffer.Buffer
import org.lwjgl.system.linux.liburing.IOURingSQE as _IOURingSQE
_IOURingSQE = _IOURingSQE
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingSQ():
    """org.lwjgl.system.linux.liburing.IOURingSQ"""
 
    @staticmethod
    def _wrap(java_value: _IOURingSQ) -> 'IOURingSQ':
        return IOURingSQ(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingSQ):
        """
        Dynamic initializer for IOURingSQ.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingSQ__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingSQ__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.createSafe(long)"""
        return IOURingSQ._wrap(_IOURingSQ.createSafe(_long.valueOf(arg0)))

    @overload
    def kring_entries(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.kring_entries(int)"""
        return 'IntBuffer'._wrap(super(_IOURingSQ, self).kring_entries(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IntBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IntBuffer', arg7: 'IOURingSQE', arg8: int, arg9: int, arg10: 'ByteBuffer', arg11: int, arg12: int) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.set(java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.system.linux.liburing.IOURingSQE,int,int,java.nio.ByteBuffer,int,int)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).set(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, _int.valueOf(arg8), _int.valueOf(arg9), arg10, _int.valueOf(arg11), _int.valueOf(arg12)))

    @staticmethod
    @overload
    def nkhead(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nkhead(long,java.nio.IntBuffer)"""
        _IOURingSQ.nkhead(_long.valueOf(arg0), arg1)

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ.sizeof()"""
        return int._wrap(super(IOURingSQ, self).sizeof())

    @staticmethod
    @overload
    def nkdropped(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nkdropped(long,int)"""
        return IntBuffer._wrap(_IOURingSQ.nkdropped(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.createSafe(long,int)"""
        return Buffer._wrap(_IOURingSQ.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def narray(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.narray(long,int)"""
        return IntBuffer._wrap(_IOURingSQ.narray(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def array(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.array(int)"""
        return 'IntBuffer'._wrap(super(_IOURingSQ, self).array(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSQ._wrap(_IOURingSQ.malloc(arg0))

    @staticmethod
    @overload
    def nktail(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nktail(long,java.nio.IntBuffer)"""
        _IOURingSQ.nktail(_long.valueOf(arg0), arg1)

    @overload
    def kflags(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.kflags(int)"""
        return 'IntBuffer'._wrap(super(_IOURingSQ, self).kflags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nkring_entries(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nkring_entries(long,int)"""
        return IntBuffer._wrap(_IOURingSQ.nkring_entries(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def sqe_tail(self, arg0: int) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.sqe_tail(int)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).sqe_tail(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.malloc(int)"""
        return Buffer._wrap(_IOURingSQ.malloc(_int.valueOf(arg0)))

    @overload
    def ktail(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.ktail(int)"""
        return 'IntBuffer'._wrap(super(_IOURingSQ, self).ktail(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_ptr(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nring_ptr(long,java.nio.ByteBuffer)"""
        _IOURingSQ.nring_ptr(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.npad(long,int,int)"""
        _IOURingSQ.npad(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def sqe_head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ.sqe_head()"""
        return int._wrap(super(IOURingSQ, self).sqe_head())

    @overload
    def ktail(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.ktail(java.nio.IntBuffer)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).ktail(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.calloc(int)"""
        return Buffer._wrap(_IOURingSQ.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nkring_mask(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nkring_mask(long,int)"""
        return IntBuffer._wrap(_IOURingSQ.nkring_mask(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nkhead(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nkhead(long,int)"""
        return IntBuffer._wrap(_IOURingSQ.nkhead(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def kring_entries(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.kring_entries(java.nio.IntBuffer)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).kring_entries(arg0))

    @overload
    def ring_ptr(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQ.ring_ptr()"""
        return 'ByteBuffer'._wrap(super(IOURingSQ, self).ring_ptr())

    @staticmethod
    @overload
    def nsqe_head(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQ.nsqe_head(long)"""
        return int._wrap(_IOURingSQ.nsqe_head(_long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ.ring_entries()"""
        return int._wrap(super(IOURingSQ, self).ring_entries())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSQ(java.nio.ByteBuffer)"""
        val = _IOURingSQ(arg0)
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def ring_entries(self, arg0: int) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.ring_entries(int)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).ring_entries(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQ.npad(long,int)"""
        return int._wrap(_IOURingSQ.npad(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def ring_ptr(self, arg0: 'ByteBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.ring_ptr(java.nio.ByteBuffer)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).ring_ptr(arg0))

    @staticmethod
    @overload
    def nsqes(arg0: int) -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQ.nsqes(long)"""
        return IOURingSQE._wrap(_IOURingSQ.nsqes(_long.valueOf(arg0)))

    @overload
    def kring_mask(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.kring_mask(int)"""
        return 'IntBuffer'._wrap(super(_IOURingSQ, self).kring_mask(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_sz(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nring_sz(long,long)"""
        _IOURingSQ.nring_sz(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.create(int)"""
        return Buffer._wrap(_IOURingSQ.create(_int.valueOf(arg0)))

    @overload
    def khead(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.khead(int)"""
        return 'IntBuffer'._wrap(super(_IOURingSQ, self).khead(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc() -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.malloc()"""
        return IOURingSQ._wrap(_IOURingSQ.malloc())

    @staticmethod
    @overload
    def npad(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.npad(long,java.nio.IntBuffer)"""
        _IOURingSQ.npad(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nring_entries(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQ.nring_entries(long)"""
        return int._wrap(_IOURingSQ.nring_entries(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingSQ.calloc(_int.valueOf(arg0), arg1))

    @overload
    def sqe_tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ.sqe_tail()"""
        return int._wrap(super(IOURingSQ, self).sqe_tail())

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.create(long)"""
        return IOURingSQ._wrap(_IOURingSQ.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nktail(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nktail(long,int)"""
        return IntBuffer._wrap(_IOURingSQ.nktail(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def ring_mask(self, arg0: int) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.ring_mask(int)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).ring_mask(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_entries(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nring_entries(long,int)"""
        _IOURingSQ.nring_entries(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQ.ring_mask()"""
        return int._wrap(super(IOURingSQ, self).ring_mask())

    @staticmethod
    @overload
    def create() -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.create()"""
        return IOURingSQ._wrap(_IOURingSQ.create())

    @overload
    def khead(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.khead(java.nio.IntBuffer)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).khead(arg0))

    @staticmethod
    @overload
    def npad(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.npad(long)"""
        return IntBuffer._wrap(_IOURingSQ.npad(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_mask(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQ.nring_mask(long)"""
        return int._wrap(_IOURingSQ.nring_mask(_long.valueOf(arg0)))

    @overload
    def kring_mask(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.kring_mask(java.nio.IntBuffer)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).kring_mask(arg0))

    @overload
    def kflags(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.kflags(java.nio.IntBuffer)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).kflags(arg0))

    @overload
    def sqes(self) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQ.sqes()"""
        return 'IOURingSQE'._wrap(super(IOURingSQ, self).sqes())

    @staticmethod
    @overload
    def nkdropped(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nkdropped(long,java.nio.IntBuffer)"""
        _IOURingSQ.nkdropped(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.create(long,int)"""
        return Buffer._wrap(_IOURingSQ.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def narray(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.narray(long,java.nio.IntBuffer)"""
        _IOURingSQ.narray(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nsqes(arg0: int, arg1: 'IOURingSQE'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nsqes(long,org.lwjgl.system.linux.liburing.IOURingSQE)"""
        _IOURingSQ.nsqes(_long.valueOf(arg0), arg1)

    @overload
    def kdropped(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.kdropped(int)"""
        return 'IntBuffer'._wrap(super(_IOURingSQ, self).kdropped(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nsqe_tail(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nsqe_tail(long,int)"""
        _IOURingSQ.nsqe_tail(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc() -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.calloc()"""
        return IOURingSQ._wrap(_IOURingSQ.calloc())

    @staticmethod
    @overload
    def nring_sz(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQ.nring_sz(long)"""
        return int._wrap(_IOURingSQ.nring_sz(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nkflags(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nkflags(long,int)"""
        return IntBuffer._wrap(_IOURingSQ.nkflags(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def sqes(self, arg0: 'IOURingSQE') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.sqes(org.lwjgl.system.linux.liburing.IOURingSQE)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).sqes(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def ring_sz(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQ.ring_sz()"""
        return int._wrap(super(IOURingSQ, self).ring_sz())

    @overload
    def sqe_head(self, arg0: int) -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.sqe_head(int)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).sqe_head(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nkring_mask(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nkring_mask(long,java.nio.IntBuffer)"""
        _IOURingSQ.nkring_mask(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.validate(long)"""
        _IOURingSQ.validate(_long.valueOf(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ$Buffer org.lwjgl.system.linux.liburing.IOURingSQ.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingSQ.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nsqe_tail(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQ.nsqe_tail(long)"""
        return int._wrap(_IOURingSQ.nsqe_tail(_long.valueOf(arg0)))

    @overload
    def kdropped(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.kdropped(java.nio.IntBuffer)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).kdropped(arg0))

    @staticmethod
    @overload
    def nkflags(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nkflags(long,java.nio.IntBuffer)"""
        _IOURingSQ.nkflags(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nring_ptr(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQ.nring_ptr(long)"""
        return ByteBuffer._wrap(_IOURingSQ.nring_ptr(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nring_mask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nring_mask(long,int)"""
        _IOURingSQ.nring_mask(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def nsqe_head(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nsqe_head(long,int)"""
        _IOURingSQ.nsqe_head(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: 'IOURingSQ') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.set(org.lwjgl.system.linux.liburing.IOURingSQ)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).set(arg0))

    @overload
    def array(self, arg0: 'IntBuffer') -> 'IOURingSQ':
        """public org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.array(java.nio.IntBuffer)"""
        return 'IOURingSQ'._wrap(super(_IOURingSQ, self).array(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingSQ':
        """public static org.lwjgl.system.linux.liburing.IOURingSQ org.lwjgl.system.linux.liburing.IOURingSQ.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSQ._wrap(_IOURingSQ.calloc(arg0))

    @staticmethod
    @overload
    def nkring_entries(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQ.nkring_entries(long,java.nio.IntBuffer)"""
        _IOURingSQ.nkring_entries(_long.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.lang.Short as _short
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.linux.liburing.IOURingBufReg as _IOURingBufReg_Buffer
_Buffer = _IOURingBufReg_Buffer.Buffer
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
import java.nio.LongBuffer as LongBuffer
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
    """org.lwjgl.system.linux.liburing.IOURingBufReg.Buffer"""
 
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
    def bgid(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.bgid()"""
        return int._wrap(super(Buffer, self).bgid())

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
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.flags(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).flags(_short.valueOf(arg0)))

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
    def resv(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.resv(int,long)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv(_int.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def ring_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.ring_entries(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_entries(_int.valueOf(arg0)))

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
    def bgid(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.bgid(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).bgid(_short.valueOf(arg0)))

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
    def ring_addr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.ring_addr(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_addr(_long.valueOf(arg0)))

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
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.ring_entries()"""
        return int._wrap(super(Buffer, self).ring_entries())

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
    def resv(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.resv()"""
        return 'LongBuffer'._wrap(super(Buffer, self).resv())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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
    def resv(self, arg0: 'LongBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.resv(java.nio.LongBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv(arg0))

    @overload
    def ring_addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.ring_addr()"""
        return int._wrap(super(Buffer, self).ring_addr())

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
    def resv(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.resv(int)"""
        return int._wrap(super(_Buffer, self).resv(_int.valueOf(arg0)))

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def flags(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBufReg$Buffer.flags()"""
        return int._wrap(super(Buffer, self).flags())

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
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingProbe$Buffer
from pyquantum_helper import import_once as _import_once
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
import org.lwjgl.system.linux.liburing.IOURingProbeOp as _IOURingProbeOp_Buffer
_Buffer = _IOURingProbeOp_Buffer.Buffer
import java.lang.Byte as _byte
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
import org.lwjgl.system.linux.liburing.IOURingProbeOp as _IOURingProbeOp
_IOURingProbeOp = _IOURingProbeOp
import org.lwjgl.system.linux.liburing.IOURingProbe as _IOURingProbe_Buffer
_Buffer = _IOURingProbe_Buffer.Buffer
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.linux.liburing.IOURingProbe.Buffer"""
 
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
    def ops(self, arg0: 'Buffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops(org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).ops(arg0))

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
    def last_op(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.last_op(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).last_op(_byte.valueOf(arg0)))

    @overload
    def ops(self, arg0: int, arg1: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops(int,java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingProbeOp>)"""
        return 'Buffer'._wrap(super(_Buffer, self).ops(_int.valueOf(arg0), arg1))

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
    def ops(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops(java.util.function.Consumer<org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer>)"""
        return 'Buffer'._wrap(super(_Buffer, self).ops(arg0))

    @overload
    def resv(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.resv()"""
        return int._wrap(super(Buffer, self).resv())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def last_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.last_op()"""
        return int._wrap(super(Buffer, self).last_op())

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
    def ops(self) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops()"""
        return 'Buffer'._wrap(super(Buffer, self).ops())

    @overload
    def ops_len(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops_len(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).ops_len(_byte.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def ops(self, arg0: int, arg1: 'IOURingProbeOp') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops(int,org.lwjgl.system.linux.liburing.IOURingProbeOp)"""
        return 'Buffer'._wrap(super(_Buffer, self).ops(_int.valueOf(arg0), arg1))

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
    def ops_len(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops_len()"""
        return int._wrap(super(Buffer, self).ops_len())

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
    def ops(self, arg0: int) -> 'IOURingProbeOp':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.ops(int)"""
        return 'IOURingProbeOp'._wrap(super(_Buffer, self).ops(_int.valueOf(arg0)))

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
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbe$Buffer org.lwjgl.system.linux.liburing.IOURingProbe$Buffer.resv(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv(_short.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer
from pyquantum_helper import import_once as _import_once
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
import org.lwjgl.system.linux.liburing.IOURingProbeOp as _IOURingProbeOp_Buffer
_Buffer = _IOURingProbeOp_Buffer.Buffer
import java.lang.Byte as _byte
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
    """org.lwjgl.system.linux.liburing.IOURingProbeOp.Buffer"""
 
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
    def op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.op()"""
        return int._wrap(super(Buffer, self).op())

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
    def op(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.op(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).op(_byte.valueOf(arg0)))

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
    def resv(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.resv()"""
        return int._wrap(super(Buffer, self).resv())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def resv2(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.resv2(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv2(_int.valueOf(arg0)))

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
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.resv2()"""
        return int._wrap(super(Buffer, self).resv2())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.flags(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).flags(_short.valueOf(arg0)))

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
    def flags(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.flags()"""
        return int._wrap(super(Buffer, self).flags())

    @overload
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer.resv(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv(_byte.valueOf(arg0)))

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingProbeOp$Buffer(long,int)"""
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
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingFileIndexRange
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
import org.lwjgl.system.linux.liburing.IOURingFileIndexRange as _IOURingFileIndexRange
_IOURingFileIndexRange = _IOURingFileIndexRange
import org.lwjgl.system.linux.liburing.IOURingFileIndexRange as _IOURingFileIndexRange_Buffer
_Buffer = _IOURingFileIndexRange_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingFileIndexRange():
    """org.lwjgl.system.linux.liburing.IOURingFileIndexRange"""
 
    @staticmethod
    def _wrap(java_value: _IOURingFileIndexRange) -> 'IOURingFileIndexRange':
        return IOURingFileIndexRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingFileIndexRange):
        """
        Dynamic initializer for IOURingFileIndexRange.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingFileIndexRange__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingFileIndexRange__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.malloc(int)"""
        return Buffer._wrap(_IOURingFileIndexRange.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.createSafe(long,int)"""
        return Buffer._wrap(_IOURingFileIndexRange.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingFileIndexRange.len()"""
        return int._wrap(super(IOURingFileIndexRange, self).len())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingFileIndexRange.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingFileIndexRange._wrap(_IOURingFileIndexRange.calloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.create(long)"""
        return IOURingFileIndexRange._wrap(_IOURingFileIndexRange.create(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingFileIndexRange') -> 'IOURingFileIndexRange':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.set(org.lwjgl.system.linux.liburing.IOURingFileIndexRange)"""
        return 'IOURingFileIndexRange'._wrap(super(_IOURingFileIndexRange, self).set(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.calloc(int)"""
        return Buffer._wrap(_IOURingFileIndexRange.calloc(_int.valueOf(arg0)))

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
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.create(int)"""
        return Buffer._wrap(_IOURingFileIndexRange.create(_int.valueOf(arg0)))

    @overload
    def len(self, arg0: int) -> 'IOURingFileIndexRange':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.len(int)"""
        return 'IOURingFileIndexRange'._wrap(super(_IOURingFileIndexRange, self).len(_int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingFileIndexRange.sizeof()"""
        return int._wrap(super(IOURingFileIndexRange, self).sizeof())

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
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingFileIndexRange.nresv(long,long)"""
        _IOURingFileIndexRange.nresv(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingFileIndexRange.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def noff(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingFileIndexRange.noff(long)"""
        return int._wrap(_IOURingFileIndexRange.noff(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nlen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingFileIndexRange.nlen(long,int)"""
        _IOURingFileIndexRange.nlen(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nlen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingFileIndexRange.nlen(long)"""
        return int._wrap(_IOURingFileIndexRange.nlen(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> 'IOURingFileIndexRange':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.set(int,int,long)"""
        return 'IOURingFileIndexRange'._wrap(super(_IOURingFileIndexRange, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingFileIndexRange._wrap(_IOURingFileIndexRange.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange$Buffer org.lwjgl.system.linux.liburing.IOURingFileIndexRange.create(long,int)"""
        return Buffer._wrap(_IOURingFileIndexRange.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingFileIndexRange.nresv(long)"""
        return int._wrap(_IOURingFileIndexRange.nresv(_long.valueOf(arg0)))

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
    def off(self, arg0: int) -> 'IOURingFileIndexRange':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.off(int)"""
        return 'IOURingFileIndexRange'._wrap(super(_IOURingFileIndexRange, self).off(_int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def resv(self, arg0: int) -> 'IOURingFileIndexRange':
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.resv(long)"""
        return 'IOURingFileIndexRange'._wrap(super(_IOURingFileIndexRange, self).resv(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.createSafe(long)"""
        return IOURingFileIndexRange._wrap(_IOURingFileIndexRange.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def create() -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.create()"""
        return IOURingFileIndexRange._wrap(_IOURingFileIndexRange.create())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def noff(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingFileIndexRange.noff(long,int)"""
        _IOURingFileIndexRange.noff(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resv(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingFileIndexRange.resv()"""
        return int._wrap(super(IOURingFileIndexRange, self).resv())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingFileIndexRange(java.nio.ByteBuffer)"""
        val = _IOURingFileIndexRange(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def malloc() -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.malloc()"""
        return IOURingFileIndexRange._wrap(_IOURingFileIndexRange.malloc())

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
    def calloc() -> 'IOURingFileIndexRange':
        """public static org.lwjgl.system.linux.liburing.IOURingFileIndexRange org.lwjgl.system.linux.liburing.IOURingFileIndexRange.calloc()"""
        return IOURingFileIndexRange._wrap(_IOURingFileIndexRange.calloc())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def off(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingFileIndexRange.off()"""
        return int._wrap(super(IOURingFileIndexRange, self).off())

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
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingBuf
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
import org.lwjgl.system.linux.liburing.IOURingBuf as _IOURingBuf
_IOURingBuf = _IOURingBuf
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Integer as _int
import org.lwjgl.system.linux.liburing.IOURingBuf as _IOURingBuf_Buffer
_Buffer = _IOURingBuf_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingBuf():
    """org.lwjgl.system.linux.liburing.IOURingBuf"""
 
    @staticmethod
    def _wrap(java_value: _IOURingBuf) -> 'IOURingBuf':
        return IOURingBuf(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingBuf):
        """
        Dynamic initializer for IOURingBuf.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingBuf__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingBuf__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addr(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.addr(long)"""
        return 'IOURingBuf'._wrap(super(_IOURingBuf, self).addr(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBuf._wrap(_IOURingBuf.malloc(arg0))

    @overload
    def bid(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.bid(short)"""
        return 'IOURingBuf'._wrap(super(_IOURingBuf, self).bid(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def nbid(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBuf.nbid(long)"""
        return int._wrap(_IOURingBuf.nbid(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBuf.nresv(long,short)"""
        _IOURingBuf.nresv(_long.valueOf(arg0), _short.valueOf(arg1))

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

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.create(int)"""
        return Buffer._wrap(_IOURingBuf.create(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def naddr(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingBuf.naddr(long)"""
        return int._wrap(_IOURingBuf.naddr(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.create(long,int)"""
        return Buffer._wrap(_IOURingBuf.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nbid(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBuf.nbid(long,short)"""
        _IOURingBuf.nbid(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.createSafe(long)"""
        return IOURingBuf._wrap(_IOURingBuf.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.malloc(int)"""
        return Buffer._wrap(_IOURingBuf.malloc(_int.valueOf(arg0)))

    @overload
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingBuf.addr()"""
        return int._wrap(super(IOURingBuf, self).addr())

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
    def resv(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.resv(short)"""
        return 'IOURingBuf'._wrap(super(_IOURingBuf, self).resv(_short.valueOf(arg0)))

    @overload
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBuf.len()"""
        return int._wrap(super(IOURingBuf, self).len())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingBuf.calloc(_int.valueOf(arg0), arg1))

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
    def naddr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBuf.naddr(long,long)"""
        _IOURingBuf.naddr(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def len(self, arg0: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.len(int)"""
        return 'IOURingBuf'._wrap(super(_IOURingBuf, self).len(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingBuf(java.nio.ByteBuffer)"""
        val = _IOURingBuf(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc() -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.calloc()"""
        return IOURingBuf._wrap(_IOURingBuf.calloc())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingBuf.malloc(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: 'IOURingBuf') -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.set(org.lwjgl.system.linux.liburing.IOURingBuf)"""
        return 'IOURingBuf'._wrap(super(_IOURingBuf, self).set(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.createSafe(long,int)"""
        return Buffer._wrap(_IOURingBuf.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'IOURingBuf':
        """public org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.set(long,int,short,short)"""
        return 'IOURingBuf'._wrap(super(_IOURingBuf, self).set(_long.valueOf(arg0), _int.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3)))

    @staticmethod
    @overload
    def nlen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingBuf.nlen(long,int)"""
        _IOURingBuf.nlen(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingBuf.sizeof()"""
        return int._wrap(super(IOURingBuf, self).sizeof())

    @staticmethod
    @overload
    def create() -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.create()"""
        return IOURingBuf._wrap(_IOURingBuf.create())

    @staticmethod
    @overload
    def malloc() -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.malloc()"""
        return IOURingBuf._wrap(_IOURingBuf.malloc())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf$Buffer org.lwjgl.system.linux.liburing.IOURingBuf.calloc(int)"""
        return Buffer._wrap(_IOURingBuf.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingBuf._wrap(_IOURingBuf.calloc(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def resv(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBuf.resv()"""
        return int._wrap(super(IOURingBuf, self).resv())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingBuf.nresv(long)"""
        return int._wrap(_IOURingBuf.nresv(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingBuf':
        """public static org.lwjgl.system.linux.liburing.IOURingBuf org.lwjgl.system.linux.liburing.IOURingBuf.create(long)"""
        return IOURingBuf._wrap(_IOURingBuf.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nlen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingBuf.nlen(long)"""
        return int._wrap(_IOURingBuf.nlen(_long.valueOf(arg0)))

    @overload
    def bid(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingBuf.bid()"""
        return int._wrap(super(IOURingBuf, self).bid())

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
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer
from pyquantum_helper import import_once as _import_once
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
import java.lang.Byte as _byte
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

import org.lwjgl.system.linux.liburing.IOURingRestriction as _IOURingRestriction_Buffer
_Buffer = _IOURingRestriction_Buffer.Buffer
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
    """org.lwjgl.system.linux.liburing.IOURingRestriction.Buffer"""
 
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
    def sqe_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.sqe_op()"""
        return int._wrap(super(Buffer, self).sqe_op())

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
    def opcode(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.opcode(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).opcode(_short.valueOf(arg0)))

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
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def sqe_flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.sqe_flags()"""
        return int._wrap(super(Buffer, self).sqe_flags())

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
    def opcode(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.opcode()"""
        return int._wrap(super(Buffer, self).opcode())

    @overload
    def register_op(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.register_op()"""
        return int._wrap(super(Buffer, self).register_op())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def sqe_op(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.sqe_op(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).sqe_op(_byte.valueOf(arg0)))

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
    def sqe_flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.sqe_flags(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).sqe_flags(_byte.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer(long,int)"""
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

    @overload
    def register_op(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer org.lwjgl.system.linux.liburing.IOURingRestriction$Buffer.register_op(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).register_op(_byte.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer
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
import org.lwjgl.system.linux.liburing.IOURingGeteventsArg as _IOURingGeteventsArg_Buffer
_Buffer = _IOURingGeteventsArg_Buffer.Buffer
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
    """org.lwjgl.system.linux.liburing.IOURingGeteventsArg.Buffer"""
 
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
    def pad(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.pad()"""
        return int._wrap(super(Buffer, self).pad())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
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
    def pad(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.pad(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).pad(_int.valueOf(arg0)))

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
    def sigmask_sz(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.sigmask_sz(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).sigmask_sz(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
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
    def ts(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.ts()"""
        return int._wrap(super(Buffer, self).ts())

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
    def sigmask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.sigmask(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).sigmask(_long.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def ts(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.ts(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).ts(_long.valueOf(arg0)))

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
    def sigmask_sz(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.sigmask_sz()"""
        return int._wrap(super(Buffer, self).sigmask_sz())

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
    def sigmask(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer.sigmask()"""
        return int._wrap(super(Buffer, self).sigmask())

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
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingCQE
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
import java.nio.LongBuffer as LongBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.linux.liburing.IOURingCQE as _IOURingCQE_Buffer
_Buffer = _IOURingCQE_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
import org.lwjgl.system.linux.liburing.IOURingCQE as _IOURingCQE
_IOURingCQE = _IOURingCQE
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingCQE():
    """org.lwjgl.system.linux.liburing.IOURingCQE"""
 
    @staticmethod
    def _wrap(java_value: _IOURingCQE) -> 'IOURingCQE':
        return IOURingCQE(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingCQE):
        """
        Dynamic initializer for IOURingCQE.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingCQE__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingCQE__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nres(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQE.nres(long,int)"""
        _IOURingCQE.nres(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.malloc(int)"""
        return Buffer._wrap(_IOURingCQE.malloc(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingCQE.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingCQE._wrap(_IOURingCQE.calloc(arg0))

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
    def res(self, arg0: int) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.res(int)"""
        return 'IOURingCQE'._wrap(super(_IOURingCQE, self).res(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'LongBuffer') -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.set(long,int,int,java.nio.LongBuffer)"""
        return 'IOURingCQE'._wrap(super(_IOURingCQE, self).set(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def nbig_cqe(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingCQE.nbig_cqe(long,int)"""
        return int._wrap(_IOURingCQE.nbig_cqe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQE.nflags(long,int)"""
        _IOURingCQE.nflags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def flags(self, arg0: int) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.flags(int)"""
        return 'IOURingCQE'._wrap(super(_IOURingCQE, self).flags(_int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQE.sizeof()"""
        return int._wrap(super(IOURingCQE, self).sizeof())

    @staticmethod
    @overload
    def nbig_cqe(arg0: int, arg1: 'LongBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQE.nbig_cqe(long,java.nio.LongBuffer)"""
        _IOURingCQE.nbig_cqe(_long.valueOf(arg0), arg1)

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
    def create() -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.create()"""
        return IOURingCQE._wrap(_IOURingCQE.create())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.createSafe(long,int)"""
        return Buffer._wrap(_IOURingCQE.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def nbig_cqe(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingCQE.nbig_cqe(long)"""
        return LongBuffer._wrap(_IOURingCQE.nbig_cqe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingCQE.malloc(_int.valueOf(arg0), arg1))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQE.flags()"""
        return int._wrap(super(IOURingCQE, self).flags())

    @overload
    def big_cqe(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingCQE.big_cqe()"""
        return 'LongBuffer'._wrap(super(IOURingCQE, self).big_cqe())

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
    def nbig_cqe(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQE.nbig_cqe(long,int,long)"""
        _IOURingCQE.nbig_cqe(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def nuser_data(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingCQE.nuser_data(long)"""
        return int._wrap(_IOURingCQE.nuser_data(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nuser_data(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingCQE.nuser_data(long,long)"""
        _IOURingCQE.nuser_data(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.calloc(int)"""
        return Buffer._wrap(_IOURingCQE.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingCQE.nflags(long)"""
        return int._wrap(_IOURingCQE.nflags(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingCQE(java.nio.ByteBuffer)"""
        val = _IOURingCQE(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def nres(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingCQE.nres(long)"""
        return int._wrap(_IOURingCQE.nres(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.create(long,int)"""
        return Buffer._wrap(_IOURingCQE.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def user_data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQE.user_data()"""
        return int._wrap(super(IOURingCQE, self).user_data())

    @overload
    def big_cqe(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQE.big_cqe(int)"""
        return int._wrap(super(_IOURingCQE, self).big_cqe(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingCQE._wrap(_IOURingCQE.malloc(arg0))

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
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE.create(int)"""
        return Buffer._wrap(_IOURingCQE.create(_int.valueOf(arg0)))

    @overload
    def big_cqe(self, arg0: int, arg1: int) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.big_cqe(int,long)"""
        return 'IOURingCQE'._wrap(super(_IOURingCQE, self).big_cqe(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.create(long)"""
        return IOURingCQE._wrap(_IOURingCQE.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.malloc()"""
        return IOURingCQE._wrap(_IOURingCQE.malloc())

    @overload
    def res(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQE.res()"""
        return int._wrap(super(IOURingCQE, self).res())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.createSafe(long)"""
        return IOURingCQE._wrap(_IOURingCQE.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'IOURingCQE':
        """public static org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.calloc()"""
        return IOURingCQE._wrap(_IOURingCQE.calloc())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: 'IOURingCQE') -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.set(org.lwjgl.system.linux.liburing.IOURingCQE)"""
        return 'IOURingCQE'._wrap(super(_IOURingCQE, self).set(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @overload
    def user_data(self, arg0: int) -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.user_data(long)"""
        return 'IOURingCQE'._wrap(super(_IOURingCQE, self).user_data(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def big_cqe(self, arg0: 'LongBuffer') -> 'IOURingCQE':
        """public org.lwjgl.system.linux.liburing.IOURingCQE org.lwjgl.system.linux.liburing.IOURingCQE.big_cqe(java.nio.LongBuffer)"""
        return 'IOURingCQE'._wrap(super(_IOURingCQE, self).big_cqe(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingGeteventsArg
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
import org.lwjgl.system.linux.liburing.IOURingGeteventsArg as _IOURingGeteventsArg
_IOURingGeteventsArg = _IOURingGeteventsArg
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.linux.liburing.IOURingGeteventsArg as _IOURingGeteventsArg_Buffer
_Buffer = _IOURingGeteventsArg_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingGeteventsArg():
    """org.lwjgl.system.linux.liburing.IOURingGeteventsArg"""
 
    @staticmethod
    def _wrap(java_value: _IOURingGeteventsArg) -> 'IOURingGeteventsArg':
        return IOURingGeteventsArg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingGeteventsArg):
        """
        Dynamic initializer for IOURingGeteventsArg.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingGeteventsArg__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingGeteventsArg__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg(java.nio.ByteBuffer)"""
        val = _IOURingGeteventsArg(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingGeteventsArg.malloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def sigmask_sz(self, arg0: int) -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.sigmask_sz(int)"""
        return 'IOURingGeteventsArg'._wrap(super(_IOURingGeteventsArg, self).sigmask_sz(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.malloc()"""
        return IOURingGeteventsArg._wrap(_IOURingGeteventsArg.malloc())

    @staticmethod
    @overload
    def npad(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingGeteventsArg.npad(long,int)"""
        _IOURingGeteventsArg.npad(_long.valueOf(arg0), _int.valueOf(arg1))

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
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.create(int)"""
        return Buffer._wrap(_IOURingGeteventsArg.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.create()"""
        return IOURingGeteventsArg._wrap(_IOURingGeteventsArg.create())

    @staticmethod
    @overload
    def nsigmask_sz(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nsigmask_sz(long,int)"""
        _IOURingGeteventsArg.nsigmask_sz(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def pad(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingGeteventsArg.pad()"""
        return int._wrap(super(IOURingGeteventsArg, self).pad())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingGeteventsArg.sizeof()"""
        return int._wrap(super(IOURingGeteventsArg, self).sizeof())

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.create(long)"""
        return IOURingGeteventsArg._wrap(_IOURingGeteventsArg.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsigmask_sz(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nsigmask_sz(long)"""
        return int._wrap(_IOURingGeteventsArg.nsigmask_sz(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def npad(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingGeteventsArg.npad(long)"""
        return int._wrap(_IOURingGeteventsArg.npad(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingGeteventsArg._wrap(_IOURingGeteventsArg.calloc(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingGeteventsArg.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nsigmask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nsigmask(long,long)"""
        _IOURingGeteventsArg.nsigmask(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def sigmask(self, arg0: int) -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.sigmask(long)"""
        return 'IOURingGeteventsArg'._wrap(super(_IOURingGeteventsArg, self).sigmask(_long.valueOf(arg0)))

    @overload
    def ts(self, arg0: int) -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.ts(long)"""
        return 'IOURingGeteventsArg'._wrap(super(_IOURingGeteventsArg, self).ts(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.calloc(int)"""
        return Buffer._wrap(_IOURingGeteventsArg.calloc(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'IOURingGeteventsArg') -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.set(org.lwjgl.system.linux.liburing.IOURingGeteventsArg)"""
        return 'IOURingGeteventsArg'._wrap(super(_IOURingGeteventsArg, self).set(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def ts(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingGeteventsArg.ts()"""
        return int._wrap(super(IOURingGeteventsArg, self).ts())

    @staticmethod
    @overload
    def nsigmask(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nsigmask(long)"""
        return int._wrap(_IOURingGeteventsArg.nsigmask(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.set(long,int,int,long)"""
        return 'IOURingGeteventsArg'._wrap(super(_IOURingGeteventsArg, self).set(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.malloc(int)"""
        return Buffer._wrap(_IOURingGeteventsArg.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.createSafe(long)"""
        return IOURingGeteventsArg._wrap(_IOURingGeteventsArg.createSafe(_long.valueOf(arg0)))

    @overload
    def pad(self, arg0: int) -> 'IOURingGeteventsArg':
        """public org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.pad(int)"""
        return 'IOURingGeteventsArg'._wrap(super(_IOURingGeteventsArg, self).pad(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingGeteventsArg._wrap(_IOURingGeteventsArg.malloc(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.create(long,int)"""
        return Buffer._wrap(_IOURingGeteventsArg.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def sigmask_sz(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingGeteventsArg.sigmask_sz()"""
        return int._wrap(super(IOURingGeteventsArg, self).sigmask_sz())

    @staticmethod
    @overload
    def nts(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nts(long)"""
        return int._wrap(_IOURingGeteventsArg.nts(_long.valueOf(arg0)))

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
    def calloc() -> 'IOURingGeteventsArg':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg org.lwjgl.system.linux.liburing.IOURingGeteventsArg.calloc()"""
        return IOURingGeteventsArg._wrap(_IOURingGeteventsArg.calloc())

    @overload
    def sigmask(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingGeteventsArg.sigmask()"""
        return int._wrap(super(IOURingGeteventsArg, self).sigmask())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingGeteventsArg$Buffer org.lwjgl.system.linux.liburing.IOURingGeteventsArg.createSafe(long,int)"""
        return Buffer._wrap(_IOURingGeteventsArg.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nts(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingGeteventsArg.nts(long,long)"""
        _IOURingGeteventsArg.nts(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCUpdate
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate as _IOURingRSRCUpdate_Buffer
_Buffer = _IOURingRSRCUpdate_Buffer.Buffer
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
import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate as _IOURingRSRCUpdate
_IOURingRSRCUpdate = _IOURingRSRCUpdate
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingRSRCUpdate():
    """org.lwjgl.system.linux.liburing.IOURingRSRCUpdate"""
 
    @staticmethod
    def _wrap(java_value: _IOURingRSRCUpdate) -> 'IOURingRSRCUpdate':
        return IOURingRSRCUpdate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingRSRCUpdate):
        """
        Dynamic initializer for IOURingRSRCUpdate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingRSRCUpdate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingRSRCUpdate__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def resv(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.resv()"""
        return int._wrap(super(IOURingRSRCUpdate, self).resv())

    @staticmethod
    @overload
    def calloc() -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.calloc()"""
        return IOURingRSRCUpdate._wrap(_IOURingRSRCUpdate.calloc())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRSRCUpdate.calloc(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> 'IOURingRSRCUpdate':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.set(int,int,long)"""
        return 'IOURingRSRCUpdate'._wrap(super(_IOURingRSRCUpdate, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.malloc()"""
        return IOURingRSRCUpdate._wrap(_IOURingRSRCUpdate.malloc())

    @staticmethod
    @overload
    def ndata(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.ndata(long)"""
        return int._wrap(_IOURingRSRCUpdate.ndata(_long.valueOf(arg0)))

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
    def noffset(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.noffset(long)"""
        return int._wrap(_IOURingRSRCUpdate.noffset(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.create()"""
        return IOURingRSRCUpdate._wrap(_IOURingRSRCUpdate.create())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.createSafe(long)"""
        return IOURingRSRCUpdate._wrap(_IOURingRSRCUpdate.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def offset(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.offset()"""
        return int._wrap(super(IOURingRSRCUpdate, self).offset())

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
    def set(self, arg0: 'IOURingRSRCUpdate') -> 'IOURingRSRCUpdate':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.set(org.lwjgl.system.linux.liburing.IOURingRSRCUpdate)"""
        return 'IOURingRSRCUpdate'._wrap(super(_IOURingRSRCUpdate, self).set(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingRSRCUpdate.malloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.sizeof()"""
        return int._wrap(super(IOURingRSRCUpdate, self).sizeof())

    @staticmethod
    @overload
    def nresv(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.nresv(long,int)"""
        _IOURingRSRCUpdate.nresv(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def ndata(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.ndata(long,long)"""
        _IOURingRSRCUpdate.ndata(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate(java.nio.ByteBuffer)"""
        val = _IOURingRSRCUpdate(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.malloc(int)"""
        return Buffer._wrap(_IOURingRSRCUpdate.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCUpdate._wrap(_IOURingRSRCUpdate.malloc(arg0))

    @overload
    def data(self, arg0: int) -> 'IOURingRSRCUpdate':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.data(long)"""
        return 'IOURingRSRCUpdate'._wrap(super(_IOURingRSRCUpdate, self).data(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.createSafe(long,int)"""
        return Buffer._wrap(_IOURingRSRCUpdate.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.create(long,int)"""
        return Buffer._wrap(_IOURingRSRCUpdate.create(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def resv(self, arg0: int) -> 'IOURingRSRCUpdate':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.resv(int)"""
        return 'IOURingRSRCUpdate'._wrap(super(_IOURingRSRCUpdate, self).resv(_int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def nresv(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.nresv(long)"""
        return int._wrap(_IOURingRSRCUpdate.nresv(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.calloc(int)"""
        return Buffer._wrap(_IOURingRSRCUpdate.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingRSRCUpdate._wrap(_IOURingRSRCUpdate.calloc(arg0))

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
    def create(arg0: int) -> 'IOURingRSRCUpdate':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.create(long)"""
        return IOURingRSRCUpdate._wrap(_IOURingRSRCUpdate.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def noffset(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.noffset(long,int)"""
        _IOURingRSRCUpdate.noffset(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def offset(self, arg0: int) -> 'IOURingRSRCUpdate':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.offset(int)"""
        return 'IOURingRSRCUpdate'._wrap(super(_IOURingRSRCUpdate, self).offset(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingRSRCUpdate$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.create(int)"""
        return Buffer._wrap(_IOURingRSRCUpdate.create(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate.data()"""
        return int._wrap(super(IOURingRSRCUpdate, self).data())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address()) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer
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
import org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2 as _IOURingRSRCUpdate2_Buffer
_Buffer = _IOURingRSRCUpdate2_Buffer.Buffer
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
    """org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2.Buffer"""
 
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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer(long,int)"""
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

    @overload
    def offset(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.offset(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).offset(_int.valueOf(arg0)))

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
    def data(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.data(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).data(_long.valueOf(arg0)))

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def resv2(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.resv2(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv2(_int.valueOf(arg0)))

    @overload
    def tags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.tags(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).tags(_long.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @overload
    def tags(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.tags()"""
        return int._wrap(super(Buffer, self).tags())

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
    def resv2(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.resv2()"""
        return int._wrap(super(Buffer, self).resv2())

    @overload
    def resv(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.resv(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).resv(_int.valueOf(arg0)))

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
    def nr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.nr(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).nr(_int.valueOf(arg0)))

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
    def data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.data()"""
        return int._wrap(super(Buffer, self).data())

    @overload
    def offset(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.offset()"""
        return int._wrap(super(Buffer, self).offset())

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

    @overload
    def nr(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.nr()"""
        return int._wrap(super(Buffer, self).nr())

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
    def resv(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingRSRCUpdate2$Buffer.resv()"""
        return int._wrap(super(Buffer, self).resv())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer
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
import org.lwjgl.system.linux.liburing.IOCQRingOffsets as _IOCQRingOffsets_Buffer
_Buffer = _IOCQRingOffsets_Buffer.Buffer
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
    """org.lwjgl.system.linux.liburing.IOCQRingOffsets.Buffer"""
 
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
    def cqes(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.cqes()"""
        return int._wrap(super(Buffer, self).cqes())

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
    def head(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.head(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).head(_int.valueOf(arg0)))

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
    def ring_mask(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.ring_mask()"""
        return int._wrap(super(Buffer, self).ring_mask())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @overload
    def tail(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.tail()"""
        return int._wrap(super(Buffer, self).tail())

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
    def overflow(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.overflow(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).overflow(_int.valueOf(arg0)))

    @overload
    def ring_mask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.ring_mask(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_mask(_int.valueOf(arg0)))

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
    def ring_entries(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.ring_entries()"""
        return int._wrap(super(Buffer, self).ring_entries())

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
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer(java.nio.ByteBuffer)"""
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

    @overload
    def tail(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.tail(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).tail(_int.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).flags(_int.valueOf(arg0)))

    @overload
    def head(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.head()"""
        return int._wrap(super(Buffer, self).head())

    @overload
    def ring_entries(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.ring_entries(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).ring_entries(_int.valueOf(arg0)))

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
    def overflow(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.overflow()"""
        return int._wrap(super(Buffer, self).overflow())

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
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.flags()"""
        return int._wrap(super(Buffer, self).flags())

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
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def cqes(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer org.lwjgl.system.linux.liburing.IOCQRingOffsets$Buffer.cqes(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).cqes(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingCQE$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.linux.liburing.IOURingCQE as _IOURingCQE_Buffer
_Buffer = _IOURingCQE_Buffer.Buffer
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
import java.nio.LongBuffer as LongBuffer
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
    """org.lwjgl.system.linux.liburing.IOURingCQE.Buffer"""
 
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
    def big_cqe(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.big_cqe()"""
        return 'LongBuffer'._wrap(super(Buffer, self).big_cqe())

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
    def res(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.res(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).res(_int.valueOf(arg0)))

    @overload
    def user_data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.user_data()"""
        return int._wrap(super(Buffer, self).user_data())

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
    def big_cqe(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.big_cqe(int)"""
        return int._wrap(super(_Buffer, self).big_cqe(_int.valueOf(arg0)))

    @overload
    def user_data(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.user_data(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).user_data(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer(long,int)"""
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
    def big_cqe(self, arg0: 'LongBuffer') -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.big_cqe(java.nio.LongBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).big_cqe(arg0))

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
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer(java.nio.ByteBuffer)"""
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
    def flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.flags()"""
        return int._wrap(super(Buffer, self).flags())

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
    def big_cqe(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.big_cqe(int,long)"""
        return 'Buffer'._wrap(super(_Buffer, self).big_cqe(_int.valueOf(arg0), _long.valueOf(arg1)))

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

    @overload
    def res(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.res()"""
        return int._wrap(super(Buffer, self).res())

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
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.linux.liburing.IOURingCQE$Buffer org.lwjgl.system.linux.liburing.IOURingCQE$Buffer.flags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).flags(_int.valueOf(arg0)))

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.linux.liburing.IOURingSQE
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.lang.Short as _short
import java.lang.Byte as _byte
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.linux.liburing.IOURingSQE as _IOURingSQE_Buffer
_Buffer = _IOURingSQE_Buffer.Buffer
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
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
import org.lwjgl.system.linux.liburing.IOURingSQE as _IOURingSQE
_IOURingSQE = _IOURingSQE
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IOURingSQE():
    """org.lwjgl.system.linux.liburing.IOURingSQE"""
 
    @staticmethod
    def _wrap(java_value: _IOURingSQE) -> 'IOURingSQE':
        return IOURingSQE(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IOURingSQE):
        """
        Dynamic initializer for IOURingSQE.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IOURingSQE__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IOURingSQE__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def flags(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE.flags()"""
        return int._wrap(super(IOURingSQE, self).flags())

    @overload
    def __pad2(self, arg0: int) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.__pad2(int)"""
        return int._wrap(super(_IOURingSQE, self).__pad2(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nuser_data(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nuser_data(long,long)"""
        _IOURingSQE.nuser_data(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def n__pad3(arg0: int, arg1: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.n__pad3(long,int)"""
        return int._wrap(_IOURingSQE.n__pad3(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def fd(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.fd(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).fd(_int.valueOf(arg0)))

    @overload
    def fsync_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.fsync_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).fsync_flags(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addr_len(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.addr_len()"""
        return int._wrap(super(IOURingSQE, self).addr_len())

    @staticmethod
    @overload
    def calloc() -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.calloc()"""
        return IOURingSQE._wrap(_IOURingSQE.calloc())

    @staticmethod
    @overload
    def ncmd_op(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.ncmd_op(long)"""
        return int._wrap(_IOURingSQE.ncmd_op(_long.valueOf(arg0)))

    @overload
    def fsync_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.fsync_flags()"""
        return int._wrap(super(IOURingSQE, self).fsync_flags())

    @overload
    def buf_index(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.buf_index()"""
        return int._wrap(super(IOURingSQE, self).buf_index())

    @staticmethod
    @overload
    def naccept_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.naccept_flags(long,int)"""
        _IOURingSQE.naccept_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def cancel_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.cancel_flags()"""
        return int._wrap(super(IOURingSQE, self).cancel_flags())

    @staticmethod
    @overload
    def n__pad1(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.n__pad1(long)"""
        return int._wrap(_IOURingSQE.n__pad1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsplice_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_flags(long,int)"""
        _IOURingSQE.nsplice_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nsync_range_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nsync_range_flags(long)"""
        return int._wrap(_IOURingSQE.nsync_range_flags(_long.valueOf(arg0)))

    @overload
    def statx_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.statx_flags()"""
        return int._wrap(super(IOURingSQE, self).statx_flags())

    @overload
    def hardlink_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.hardlink_flags()"""
        return int._wrap(super(IOURingSQE, self).hardlink_flags())

    @staticmethod
    @overload
    def nopcode(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingSQE.nopcode(long)"""
        return int._wrap(_IOURingSQE.nopcode(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingSQE.calloc(_int.valueOf(arg0), arg1))

    @overload
    def __pad3(self, arg0: int, arg1: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.__pad3(int,short)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).__pad3(_int.valueOf(arg0), _short.valueOf(arg1)))

    @overload
    def buf_group(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.buf_group(short)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).buf_group(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def nbuf_group(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nbuf_group(long,short)"""
        _IOURingSQE.nbuf_group(_long.valueOf(arg0), _short.valueOf(arg1))

    @overload
    def unlink_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.unlink_flags()"""
        return int._wrap(super(IOURingSQE, self).unlink_flags())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def user_data(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.user_data(long)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).user_data(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nsplice_off_in(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_off_in(long)"""
        return int._wrap(_IOURingSQE.nsplice_off_in(_long.valueOf(arg0)))

    @overload
    def addr(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.addr()"""
        return int._wrap(super(IOURingSQE, self).addr())

    @overload
    def poll32_events(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.poll32_events()"""
        return int._wrap(super(IOURingSQE, self).poll32_events())

    @overload
    def __pad2(self, arg0: int, arg1: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.__pad2(int,long)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).__pad2(_int.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def addr2(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.addr2()"""
        return int._wrap(super(IOURingSQE, self).addr2())

    @staticmethod
    @overload
    def nopen_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nopen_flags(long,int)"""
        _IOURingSQE.nopen_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def splice_fd_in(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.splice_fd_in(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).splice_fd_in(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nstatx_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nstatx_flags(long,int)"""
        _IOURingSQE.nstatx_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nuring_cmd_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nuring_cmd_flags(long,int)"""
        _IOURingSQE.nuring_cmd_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.flags(byte)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).flags(_byte.valueOf(arg0)))

    @overload
    def __pad2(self) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingSQE.__pad2()"""
        return 'LongBuffer'._wrap(super(IOURingSQE, self).__pad2())

    @overload
    def splice_off_in(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.splice_off_in()"""
        return int._wrap(super(IOURingSQE, self).splice_off_in())

    @overload
    def __pad1(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.__pad1()"""
        return int._wrap(super(IOURingSQE, self).__pad1())

    @staticmethod
    @overload
    def nfile_index(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nfile_index(long)"""
        return int._wrap(_IOURingSQE.nfile_index(_long.valueOf(arg0)))

    @overload
    def ioprio(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.ioprio()"""
        return int._wrap(super(IOURingSQE, self).ioprio())

    @overload
    def xattr_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.xattr_flags()"""
        return int._wrap(super(IOURingSQE, self).xattr_flags())

    @staticmethod
    @overload
    def nioprio(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nioprio(long,short)"""
        _IOURingSQE.nioprio(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def ncmd(arg0: int, arg1: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingSQE.ncmd(long,int)"""
        return int._wrap(_IOURingSQE.ncmd(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def len(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.len()"""
        return int._wrap(super(IOURingSQE, self).len())

    @overload
    def uring_cmd_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.uring_cmd_flags()"""
        return int._wrap(super(IOURingSQE, self).uring_cmd_flags())

    @staticmethod
    @overload
    def nfsync_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nfsync_flags(long)"""
        return int._wrap(_IOURingSQE.nfsync_flags(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def open_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.open_flags()"""
        return int._wrap(super(IOURingSQE, self).open_flags())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def npersonality(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.npersonality(long,short)"""
        _IOURingSQE.npersonality(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.createSafe(long)"""
        return IOURingSQE._wrap(_IOURingSQE.createSafe(_long.valueOf(arg0)))

    @overload
    def rename_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.rename_flags()"""
        return int._wrap(super(IOURingSQE, self).rename_flags())

    @overload
    def sync_range_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.sync_range_flags()"""
        return int._wrap(super(IOURingSQE, self).sync_range_flags())

    @overload
    def msg_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.msg_flags()"""
        return int._wrap(super(IOURingSQE, self).msg_flags())

    @overload
    def len(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.len(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).len(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static byte org.lwjgl.system.linux.liburing.IOURingSQE.nflags(long)"""
        return int._wrap(_IOURingSQE.nflags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def npoll32_events(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.npoll32_events(long)"""
        return int._wrap(_IOURingSQE.npoll32_events(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def noff(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.noff(long,long)"""
        _IOURingSQE.noff(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nlen(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nlen(long)"""
        return int._wrap(_IOURingSQE.nlen(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nrename_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nrename_flags(long)"""
        return int._wrap(_IOURingSQE.nrename_flags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def n__pad3(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.linux.liburing.IOURingSQE.n__pad3(long)"""
        return ShortBuffer._wrap(_IOURingSQE.n__pad3(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nrename_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nrename_flags(long,int)"""
        _IOURingSQE.nrename_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __pad3(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.linux.liburing.IOURingSQE.__pad3()"""
        return 'ShortBuffer'._wrap(super(IOURingSQE, self).__pad3())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def cmd(self, arg0: 'ByteBuffer') -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.cmd(java.nio.ByteBuffer)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).cmd(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def n__pad2(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.linux.liburing.IOURingSQE.n__pad2(long)"""
        return LongBuffer._wrap(_IOURingSQE.n__pad2(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def rw_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.rw_flags()"""
        return int._wrap(super(IOURingSQE, self).rw_flags())

    @overload
    def splice_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.splice_flags()"""
        return int._wrap(super(IOURingSQE, self).splice_flags())

    @staticmethod
    @overload
    def nioprio(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.nioprio(long)"""
        return int._wrap(_IOURingSQE.nioprio(_long.valueOf(arg0)))

    @overload
    def __pad3(self, arg0: 'ShortBuffer') -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.__pad3(java.nio.ShortBuffer)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).__pad3(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.create(int)"""
        return Buffer._wrap(_IOURingSQE.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_IOURingSQE.malloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def npoll_events(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.npoll_events(long)"""
        return int._wrap(_IOURingSQE.npoll_events(_long.valueOf(arg0)))

    @overload
    def cmd(self, arg0: int, arg1: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.cmd(int,byte)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).cmd(_int.valueOf(arg0), _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc() -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.malloc()"""
        return IOURingSQE._wrap(_IOURingSQE.malloc())

    @staticmethod
    @overload
    def nbuf_index(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.nbuf_index(long)"""
        return int._wrap(_IOURingSQE.nbuf_index(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.createSafe(long,int)"""
        return Buffer._wrap(_IOURingSQE.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def cmd_op(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.cmd_op(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).cmd_op(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nrw_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nrw_flags(long)"""
        return int._wrap(_IOURingSQE.nrw_flags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nfsync_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nfsync_flags(long,int)"""
        _IOURingSQE.nfsync_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.sizeof()"""
        return int._wrap(super(IOURingSQE, self).sizeof())

    @staticmethod
    @overload
    def nfadvise_advice(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nfadvise_advice(long,int)"""
        _IOURingSQE.nfadvise_advice(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nstatx_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nstatx_flags(long)"""
        return int._wrap(_IOURingSQE.nstatx_flags(_long.valueOf(arg0)))

    @overload
    def poll_events(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.poll_events()"""
        return int._wrap(super(IOURingSQE, self).poll_events())

    @staticmethod
    @overload
    def nopen_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nopen_flags(long)"""
        return int._wrap(_IOURingSQE.nopen_flags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncmd(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.ncmd(long,int,byte)"""
        _IOURingSQE.ncmd(_long.valueOf(arg0), _int.valueOf(arg1), _byte.valueOf(arg2))

    @overload
    def poll_events(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.poll_events(short)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).poll_events(_short.valueOf(arg0)))

    @overload
    def fadvise_advice(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.fadvise_advice(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).fadvise_advice(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.create()"""
        return IOURingSQE._wrap(_IOURingSQE.create())

    @staticmethod
    @overload
    def nmsg_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nmsg_flags(long,int)"""
        _IOURingSQE.nmsg_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.create(long)"""
        return IOURingSQE._wrap(_IOURingSQE.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def n__pad2(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.n__pad2(long,int)"""
        return int._wrap(_IOURingSQE.n__pad2(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def accept_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.accept_flags()"""
        return int._wrap(super(IOURingSQE, self).accept_flags())

    @staticmethod
    @overload
    def naccept_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.naccept_flags(long)"""
        return int._wrap(_IOURingSQE.naccept_flags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def n__pad2(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.n__pad2(long,int,long)"""
        _IOURingSQE.n__pad2(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def nhardlink_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nhardlink_flags(long)"""
        return int._wrap(_IOURingSQE.nhardlink_flags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def n__pad2(arg0: int, arg1: 'LongBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.n__pad2(long,java.nio.LongBuffer)"""
        _IOURingSQE.n__pad2(_long.valueOf(arg0), arg1)

    @overload
    def opcode(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.opcode(byte)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).opcode(_byte.valueOf(arg0)))

    @overload
    def uring_cmd_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.uring_cmd_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).uring_cmd_flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.calloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSQE._wrap(_IOURingSQE.calloc(arg0))

    @staticmethod
    @overload
    def nhardlink_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nhardlink_flags(long,int)"""
        _IOURingSQE.nhardlink_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nxattr_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nxattr_flags(long,int)"""
        _IOURingSQE.nxattr_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def cmd_op(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.cmd_op()"""
        return int._wrap(super(IOURingSQE, self).cmd_op())

    @overload
    def cmd(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQE.cmd()"""
        return 'ByteBuffer'._wrap(super(IOURingSQE, self).cmd())

    @staticmethod
    @overload
    def nopcode(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nopcode(long,byte)"""
        _IOURingSQE.nopcode(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def naddr(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.naddr(long)"""
        return int._wrap(_IOURingSQE.naddr(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nfadvise_advice(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nfadvise_advice(long)"""
        return int._wrap(_IOURingSQE.nfadvise_advice(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def naddr3(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.naddr3(long)"""
        return int._wrap(_IOURingSQE.naddr3(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def naddr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.naddr(long,long)"""
        _IOURingSQE.naddr(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nfd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nfd(long,int)"""
        _IOURingSQE.nfd(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nsplice_off_in(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_off_in(long,long)"""
        _IOURingSQE.nsplice_off_in(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def naddr_len(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.naddr_len(long)"""
        return int._wrap(_IOURingSQE.naddr_len(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def noff(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.noff(long)"""
        return int._wrap(_IOURingSQE.noff(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nbuf_index(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nbuf_index(long,short)"""
        _IOURingSQE.nbuf_index(_long.valueOf(arg0), _short.valueOf(arg1))

    @overload
    def addr3(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.addr3()"""
        return int._wrap(super(IOURingSQE, self).addr3())

    @overload
    def accept_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.accept_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).accept_flags(_int.valueOf(arg0)))

    @overload
    def __pad1(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.__pad1(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).__pad1(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def buf_index(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.buf_index(short)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).buf_index(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def nsplice_fd_in(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_fd_in(long)"""
        return int._wrap(_IOURingSQE.nsplice_fd_in(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def naddr2(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.naddr2(long,long)"""
        _IOURingSQE.naddr2(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def off(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.off(long)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).off(_long.valueOf(arg0)))

    @overload
    def splice_fd_in(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.splice_fd_in()"""
        return int._wrap(super(IOURingSQE, self).splice_fd_in())

    @overload
    def msg_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.msg_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).msg_flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nunlink_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nunlink_flags(long)"""
        return int._wrap(_IOURingSQE.nunlink_flags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncmd(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.ncmd(long,java.nio.ByteBuffer)"""
        _IOURingSQE.ncmd(_long.valueOf(arg0), arg1)

    @overload
    def personality(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.personality()"""
        return int._wrap(super(IOURingSQE, self).personality())

    @staticmethod
    @overload
    def ncmd(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.linux.liburing.IOURingSQE.ncmd(long)"""
        return ByteBuffer._wrap(_IOURingSQE.ncmd(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nlen(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nlen(long,int)"""
        _IOURingSQE.nlen(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def addr_len(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.addr_len(short)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).addr_len(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def npoll_events(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.npoll_events(long,short)"""
        _IOURingSQE.npoll_events(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def nsplice_fd_in(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_fd_in(long,int)"""
        _IOURingSQE.nsplice_fd_in(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def n__pad3(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.n__pad3(long,int,short)"""
        _IOURingSQE.n__pad3(_long.valueOf(arg0), _int.valueOf(arg1), _short.valueOf(arg2))

    @staticmethod
    @overload
    def nmsg_ring_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nmsg_ring_flags(long,int)"""
        _IOURingSQE.nmsg_ring_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def opcode(self) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE.opcode()"""
        return int._wrap(super(IOURingSQE, self).opcode())

    @staticmethod
    @overload
    def nmsg_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nmsg_flags(long)"""
        return int._wrap(_IOURingSQE.nmsg_flags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def naddr2(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.naddr2(long)"""
        return int._wrap(_IOURingSQE.naddr2(_long.valueOf(arg0)))

    @overload
    def splice_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.splice_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).splice_flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def n__pad3(arg0: int, arg1: 'ShortBuffer'):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.n__pad3(long,java.nio.ShortBuffer)"""
        _IOURingSQE.n__pad3(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def naddr3(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.naddr3(long,long)"""
        _IOURingSQE.naddr3(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def ncancel_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.ncancel_flags(long)"""
        return int._wrap(_IOURingSQE.ncancel_flags(_long.valueOf(arg0)))

    @overload
    def file_index(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.file_index(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).file_index(_int.valueOf(arg0)))

    @overload
    def buf_group(self) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.buf_group()"""
        return int._wrap(super(IOURingSQE, self).buf_group())

    @staticmethod
    @overload
    def naddr_len(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.naddr_len(long,short)"""
        _IOURingSQE.naddr_len(_long.valueOf(arg0), _short.valueOf(arg1))

    @overload
    def hardlink_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.hardlink_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).hardlink_flags(_int.valueOf(arg0)))

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
    def open_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.open_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).open_flags(_int.valueOf(arg0)))

    @overload
    def __pad3(self, arg0: int) -> int:
        """public short org.lwjgl.system.linux.liburing.IOURingSQE.__pad3(int)"""
        return int._wrap(super(_IOURingSQE, self).__pad3(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncancel_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.ncancel_flags(long,int)"""
        _IOURingSQE.ncancel_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nrw_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nrw_flags(long,int)"""
        _IOURingSQE.nrw_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nflags(long,byte)"""
        _IOURingSQE.nflags(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.malloc(int)"""
        return Buffer._wrap(_IOURingSQE.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def n__pad1(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.n__pad1(long,int)"""
        _IOURingSQE.n__pad1(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def fd(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.fd()"""
        return int._wrap(super(IOURingSQE, self).fd())

    @overload
    def timeout_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.timeout_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).timeout_flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.create(long,int)"""
        return Buffer._wrap(_IOURingSQE.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def npersonality(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.npersonality(long)"""
        return int._wrap(_IOURingSQE.npersonality(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntimeout_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.ntimeout_flags(long)"""
        return int._wrap(_IOURingSQE.ntimeout_flags(_long.valueOf(arg0)))

    @overload
    def personality(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.personality(short)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).personality(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def nunlink_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nunlink_flags(long,int)"""
        _IOURingSQE.nunlink_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def cmd(self, arg0: int) -> int:
        """public byte org.lwjgl.system.linux.liburing.IOURingSQE.cmd(int)"""
        return int._wrap(super(_IOURingSQE, self).cmd(_int.valueOf(arg0)))

    @overload
    def rename_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.rename_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).rename_flags(_int.valueOf(arg0)))

    @overload
    def timeout_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.timeout_flags()"""
        return int._wrap(super(IOURingSQE, self).timeout_flags())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'IOURingSQE':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.malloc(org.lwjgl.system.MemoryStack)"""
        return IOURingSQE._wrap(_IOURingSQE.malloc(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def nuring_cmd_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nuring_cmd_flags(long)"""
        return int._wrap(_IOURingSQE.nuring_cmd_flags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntimeout_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.ntimeout_flags(long,int)"""
        _IOURingSQE.ntimeout_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nsplice_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nsplice_flags(long)"""
        return int._wrap(_IOURingSQE.nsplice_flags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nfile_index(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nfile_index(long,int)"""
        _IOURingSQE.nfile_index(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nbuf_group(arg0: int) -> int:
        """public static short org.lwjgl.system.linux.liburing.IOURingSQE.nbuf_group(long)"""
        return int._wrap(_IOURingSQE.nbuf_group(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncmd_op(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.ncmd_op(long,int)"""
        _IOURingSQE.ncmd_op(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def cancel_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.cancel_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).cancel_flags(_int.valueOf(arg0)))

    @overload
    def fadvise_advice(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.fadvise_advice()"""
        return int._wrap(super(IOURingSQE, self).fadvise_advice())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.linux.liburing.IOURingSQE$Buffer org.lwjgl.system.linux.liburing.IOURingSQE.calloc(int)"""
        return Buffer._wrap(_IOURingSQE.calloc(_int.valueOf(arg0)))

    @overload
    def ioprio(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.ioprio(short)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).ioprio(_short.valueOf(arg0)))

    @overload
    def splice_off_in(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.splice_off_in(long)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).splice_off_in(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def sync_range_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.sync_range_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).sync_range_flags(_int.valueOf(arg0)))

    @overload
    def addr3(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.addr3(long)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).addr3(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmsg_ring_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nmsg_ring_flags(long)"""
        return int._wrap(_IOURingSQE.nmsg_ring_flags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def npoll32_events(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.npoll32_events(long,int)"""
        _IOURingSQE.npoll32_events(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nuser_data(arg0: int) -> int:
        """public static long org.lwjgl.system.linux.liburing.IOURingSQE.nuser_data(long)"""
        return int._wrap(_IOURingSQE.nuser_data(_long.valueOf(arg0)))

    @overload
    def msg_ring_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.msg_ring_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).msg_ring_flags(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.linux.liburing.IOURingSQE(java.nio.ByteBuffer)"""
        val = _IOURingSQE(arg0)
        self.__wrapper = val

    @overload
    def set(self, arg0: 'IOURingSQE') -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.set(org.lwjgl.system.linux.liburing.IOURingSQE)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).set(arg0))

    @overload
    def __pad2(self, arg0: 'LongBuffer') -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.__pad2(java.nio.LongBuffer)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).__pad2(arg0))

    @overload
    def off(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.off()"""
        return int._wrap(super(IOURingSQE, self).off())

    @overload
    def msg_ring_flags(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.msg_ring_flags()"""
        return int._wrap(super(IOURingSQE, self).msg_ring_flags())

    @overload
    def statx_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.statx_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).statx_flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nfd(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nfd(long)"""
        return int._wrap(_IOURingSQE.nfd(_long.valueOf(arg0)))

    @overload
    def user_data(self) -> int:
        """public long org.lwjgl.system.linux.liburing.IOURingSQE.user_data()"""
        return int._wrap(super(IOURingSQE, self).user_data())

    @overload
    def unlink_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.unlink_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).unlink_flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nxattr_flags(arg0: int) -> int:
        """public static int org.lwjgl.system.linux.liburing.IOURingSQE.nxattr_flags(long)"""
        return int._wrap(_IOURingSQE.nxattr_flags(_long.valueOf(arg0)))

    @overload
    def addr2(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.addr2(long)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).addr2(_long.valueOf(arg0)))

    @overload
    def xattr_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.xattr_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).xattr_flags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nsync_range_flags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.linux.liburing.IOURingSQE.nsync_range_flags(long,int)"""
        _IOURingSQE.nsync_range_flags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def file_index(self) -> int:
        """public int org.lwjgl.system.linux.liburing.IOURingSQE.file_index()"""
        return int._wrap(super(IOURingSQE, self).file_index())

    @overload
    def rw_flags(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.rw_flags(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).rw_flags(_int.valueOf(arg0)))

    @overload
    def poll32_events(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.poll32_events(int)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).poll32_events(_int.valueOf(arg0)))

    @overload
    def addr(self, arg0: int) -> 'IOURingSQE':
        """public org.lwjgl.system.linux.liburing.IOURingSQE org.lwjgl.system.linux.liburing.IOURingSQE.addr(long)"""
        return 'IOURingSQE'._wrap(super(_IOURingSQE, self).addr(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())