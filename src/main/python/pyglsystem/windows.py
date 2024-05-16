from __future__ import annotations
from overload import overload


 
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
import org.lwjgl.system.windows.HARDWAREINPUT as _HARDWAREINPUT_Buffer
_Buffer = _HARDWAREINPUT_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.windows.HARDWAREINPUT as _HARDWAREINPUT
_HARDWAREINPUT = _HARDWAREINPUT
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HARDWAREINPUT():
    """org.lwjgl.system.windows.HARDWAREINPUT"""
 
    @staticmethod
    def _wrap(java_value: _HARDWAREINPUT) -> 'HARDWAREINPUT':
        return HARDWAREINPUT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HARDWAREINPUT):
        """
        Dynamic initializer for HARDWAREINPUT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HARDWAREINPUT__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HARDWAREINPUT__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.create(long,int)"""
        return Buffer._wrap(_HARDWAREINPUT.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nwParamH(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.HARDWAREINPUT.nwParamH(long,short)"""
        _HARDWAREINPUT.nwParamH(_long.valueOf(arg0), _short.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def wParamH(self, arg0: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.wParamH(short)"""
        return 'HARDWAREINPUT'._wrap(super(_HARDWAREINPUT, self).wParamH(_short.valueOf(arg0)))

    @overload
    def wParamL(self) -> int:
        """public short org.lwjgl.system.windows.HARDWAREINPUT.wParamL()"""
        return int._wrap(super(HARDWAREINPUT, self).wParamL())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_HARDWAREINPUT.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_HARDWAREINPUT.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.malloc(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.malloc(arg0))

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
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.create(int)"""
        return Buffer._wrap(_HARDWAREINPUT.create(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def calloc() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.calloc()"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.calloc())

    @staticmethod
    @overload
    def nwParamL(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.HARDWAREINPUT.nwParamL(long,short)"""
        _HARDWAREINPUT.nwParamL(_long.valueOf(arg0), _short.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.HARDWAREINPUT(java.nio.ByteBuffer)"""
        val = _HARDWAREINPUT(arg0)
        self.__wrapper = val

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.HARDWAREINPUT.sizeof()"""
        return int._wrap(super(HARDWAREINPUT, self).sizeof())

    @staticmethod
    @overload
    def create() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.create()"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.create())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_HARDWAREINPUT.malloc(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.set(int,short,short)"""
        return 'HARDWAREINPUT'._wrap(super(_HARDWAREINPUT, self).set(_int.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.create(long)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.create(_long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def malloc() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.malloc()"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.malloc())

    @staticmethod
    @overload
    def mallocStack() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.mallocStack()"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.mallocStack())

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
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.malloc(int)"""
        return Buffer._wrap(_HARDWAREINPUT.malloc(_int.valueOf(arg0)))

    @overload
    def uMsg(self, arg0: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.uMsg(int)"""
        return 'HARDWAREINPUT'._wrap(super(_HARDWAREINPUT, self).uMsg(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'HARDWAREINPUT') -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.set(org.lwjgl.system.windows.HARDWAREINPUT)"""
        return 'HARDWAREINPUT'._wrap(super(_HARDWAREINPUT, self).set(arg0))

    @overload
    def uMsg(self) -> int:
        """public int org.lwjgl.system.windows.HARDWAREINPUT.uMsg()"""
        return int._wrap(super(HARDWAREINPUT, self).uMsg())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.mallocStack(int)"""
        return Buffer._wrap(_HARDWAREINPUT.mallocStack(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.createSafe(long)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.calloc(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.calloc(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.mallocStack(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def wParamL(self, arg0: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.wParamL(short)"""
        return 'HARDWAREINPUT'._wrap(super(_HARDWAREINPUT, self).wParamL(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def nwParamH(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.HARDWAREINPUT.nwParamH(long)"""
        return int._wrap(_HARDWAREINPUT.nwParamH(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nwParamL(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.HARDWAREINPUT.nwParamL(long)"""
        return int._wrap(_HARDWAREINPUT.nwParamL(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nuMsg(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.HARDWAREINPUT.nuMsg(long)"""
        return int._wrap(_HARDWAREINPUT.nuMsg(_long.valueOf(arg0)))

    @overload
    def wParamH(self) -> int:
        """public short org.lwjgl.system.windows.HARDWAREINPUT.wParamH()"""
        return int._wrap(super(HARDWAREINPUT, self).wParamH())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.calloc(int)"""
        return Buffer._wrap(_HARDWAREINPUT.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.callocStack(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.callocStack(arg0))

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
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_HARDWAREINPUT.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.callocStack()"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.callocStack())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.callocStack(int)"""
        return Buffer._wrap(_HARDWAREINPUT.callocStack(_int.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.createSafe(long,int)"""
        return Buffer._wrap(_HARDWAREINPUT.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nuMsg(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.HARDWAREINPUT.nuMsg(long,int)"""
        _HARDWAREINPUT.nuMsg(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

 
 
 
# CLASS: org.lwjgl.system.windows.HARDWAREINPUT
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
import org.lwjgl.system.windows.HARDWAREINPUT as _HARDWAREINPUT_Buffer
_Buffer = _HARDWAREINPUT_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.windows.HARDWAREINPUT as _HARDWAREINPUT
_HARDWAREINPUT = _HARDWAREINPUT
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HARDWAREINPUT():
    """org.lwjgl.system.windows.HARDWAREINPUT"""
 
    @staticmethod
    def _wrap(java_value: _HARDWAREINPUT) -> 'HARDWAREINPUT':
        return HARDWAREINPUT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HARDWAREINPUT):
        """
        Dynamic initializer for HARDWAREINPUT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HARDWAREINPUT__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HARDWAREINPUT__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.create(long,int)"""
        return Buffer._wrap(_HARDWAREINPUT.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nwParamH(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.HARDWAREINPUT.nwParamH(long,short)"""
        _HARDWAREINPUT.nwParamH(_long.valueOf(arg0), _short.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def wParamH(self, arg0: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.wParamH(short)"""
        return 'HARDWAREINPUT'._wrap(super(_HARDWAREINPUT, self).wParamH(_short.valueOf(arg0)))

    @overload
    def wParamL(self) -> int:
        """public short org.lwjgl.system.windows.HARDWAREINPUT.wParamL()"""
        return int._wrap(super(HARDWAREINPUT, self).wParamL())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_HARDWAREINPUT.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_HARDWAREINPUT.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.malloc(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.malloc(arg0))

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
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.create(int)"""
        return Buffer._wrap(_HARDWAREINPUT.create(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def calloc() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.calloc()"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.calloc())

    @staticmethod
    @overload
    def nwParamL(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.HARDWAREINPUT.nwParamL(long,short)"""
        _HARDWAREINPUT.nwParamL(_long.valueOf(arg0), _short.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.HARDWAREINPUT(java.nio.ByteBuffer)"""
        val = _HARDWAREINPUT(arg0)
        self.__wrapper = val

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.HARDWAREINPUT.sizeof()"""
        return int._wrap(super(HARDWAREINPUT, self).sizeof())

    @staticmethod
    @overload
    def create() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.create()"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.create())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_HARDWAREINPUT.malloc(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.set(int,short,short)"""
        return 'HARDWAREINPUT'._wrap(super(_HARDWAREINPUT, self).set(_int.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.create(long)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.create(_long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def malloc() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.malloc()"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.malloc())

    @staticmethod
    @overload
    def mallocStack() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.mallocStack()"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.mallocStack())

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
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.malloc(int)"""
        return Buffer._wrap(_HARDWAREINPUT.malloc(_int.valueOf(arg0)))

    @overload
    def uMsg(self, arg0: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.uMsg(int)"""
        return 'HARDWAREINPUT'._wrap(super(_HARDWAREINPUT, self).uMsg(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'HARDWAREINPUT') -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.set(org.lwjgl.system.windows.HARDWAREINPUT)"""
        return 'HARDWAREINPUT'._wrap(super(_HARDWAREINPUT, self).set(arg0))

    @overload
    def uMsg(self) -> int:
        """public int org.lwjgl.system.windows.HARDWAREINPUT.uMsg()"""
        return int._wrap(super(HARDWAREINPUT, self).uMsg())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.mallocStack(int)"""
        return Buffer._wrap(_HARDWAREINPUT.mallocStack(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.createSafe(long)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.calloc(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.calloc(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.mallocStack(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def wParamL(self, arg0: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.wParamL(short)"""
        return 'HARDWAREINPUT'._wrap(super(_HARDWAREINPUT, self).wParamL(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def nwParamH(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.HARDWAREINPUT.nwParamH(long)"""
        return int._wrap(_HARDWAREINPUT.nwParamH(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nwParamL(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.HARDWAREINPUT.nwParamL(long)"""
        return int._wrap(_HARDWAREINPUT.nwParamL(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nuMsg(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.HARDWAREINPUT.nuMsg(long)"""
        return int._wrap(_HARDWAREINPUT.nuMsg(_long.valueOf(arg0)))

    @overload
    def wParamH(self) -> int:
        """public short org.lwjgl.system.windows.HARDWAREINPUT.wParamH()"""
        return int._wrap(super(HARDWAREINPUT, self).wParamH())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.calloc(int)"""
        return Buffer._wrap(_HARDWAREINPUT.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.callocStack(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.callocStack(arg0))

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
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_HARDWAREINPUT.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.callocStack()"""
        return HARDWAREINPUT._wrap(_HARDWAREINPUT.callocStack())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.callocStack(int)"""
        return Buffer._wrap(_HARDWAREINPUT.callocStack(_int.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.createSafe(long,int)"""
        return Buffer._wrap(_HARDWAREINPUT.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nuMsg(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.HARDWAREINPUT.nuMsg(long,int)"""
        _HARDWAREINPUT.nuMsg(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

 
 
 
# CLASS: org.lwjgl.system.windows.HARDWAREINPUT 
 
 
# CLASS: org.lwjgl.system.windows.WindowsUtil
from builtins import str
from pyquantum_helper import override
import org.lwjgl.system.windows.WindowsUtil as _WindowsUtil
_WindowsUtil = _WindowsUtil
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WindowsUtil():
    """org.lwjgl.system.windows.WindowsUtil"""
 
    @staticmethod
    def _wrap(java_value: _WindowsUtil) -> 'WindowsUtil':
        return WindowsUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowsUtil):
        """
        Dynamic initializer for WindowsUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowsUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowsUtil__wrapper":
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

    @staticmethod
    @overload
    def windowsThrowException(arg0: str):
        """public static void org.lwjgl.system.windows.WindowsUtil.windowsThrowException(java.lang.String)"""
        _WindowsUtil.windowsThrowException(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.windows.LARGE_INTEGER
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
import org.lwjgl.system.windows.LARGE_INTEGER as _LARGE_INTEGER
_LARGE_INTEGER = _LARGE_INTEGER
import java.lang.Integer as _int
import org.lwjgl.system.windows.LARGE_INTEGER as _LARGE_INTEGER_Buffer
_Buffer = _LARGE_INTEGER_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LARGE_INTEGER():
    """org.lwjgl.system.windows.LARGE_INTEGER"""
 
    @staticmethod
    def _wrap(java_value: _LARGE_INTEGER) -> 'LARGE_INTEGER':
        return LARGE_INTEGER(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LARGE_INTEGER):
        """
        Dynamic initializer for LARGE_INTEGER.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LARGE_INTEGER__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LARGE_INTEGER__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nu_HighPart(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.LARGE_INTEGER.nu_HighPart(long)"""
        return int._wrap(_LARGE_INTEGER.nu_HighPart(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.createSafe(long)"""
        return LARGE_INTEGER._wrap(_LARGE_INTEGER.createSafe(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.LARGE_INTEGER(java.nio.ByteBuffer)"""
        val = _LARGE_INTEGER(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def nu_LowPart(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.LARGE_INTEGER.nu_LowPart(long,int)"""
        _LARGE_INTEGER.nu_LowPart(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.malloc(int)"""
        return Buffer._wrap(_LARGE_INTEGER.malloc(_int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.LARGE_INTEGER.sizeof()"""
        return int._wrap(super(LARGE_INTEGER, self).sizeof())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_LARGE_INTEGER.calloc(_int.valueOf(arg0), arg1))

    @overload
    def QuadPart(self, arg0: int) -> 'LARGE_INTEGER':
        """public org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.QuadPart(long)"""
        return 'LARGE_INTEGER'._wrap(super(_LARGE_INTEGER, self).QuadPart(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.calloc(int)"""
        return Buffer._wrap(_LARGE_INTEGER.calloc(_int.valueOf(arg0)))

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
    def create() -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.create()"""
        return LARGE_INTEGER._wrap(_LARGE_INTEGER.create())

    @staticmethod
    @overload
    def malloc() -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.malloc()"""
        return LARGE_INTEGER._wrap(_LARGE_INTEGER.malloc())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def create(arg0: int) -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.create(long)"""
        return LARGE_INTEGER._wrap(_LARGE_INTEGER.create(_long.valueOf(arg0)))

    @overload
    def u_HighPart(self) -> int:
        """public int org.lwjgl.system.windows.LARGE_INTEGER.u_HighPart()"""
        return int._wrap(super(LARGE_INTEGER, self).u_HighPart())

    @overload
    def set(self, arg0: 'LARGE_INTEGER') -> 'LARGE_INTEGER':
        """public org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.set(org.lwjgl.system.windows.LARGE_INTEGER)"""
        return 'LARGE_INTEGER'._wrap(super(_LARGE_INTEGER, self).set(arg0))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.malloc(org.lwjgl.system.MemoryStack)"""
        return LARGE_INTEGER._wrap(_LARGE_INTEGER.malloc(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.createSafe(long,int)"""
        return Buffer._wrap(_LARGE_INTEGER.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nQuadPart(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.LARGE_INTEGER.nQuadPart(long,long)"""
        _LARGE_INTEGER.nQuadPart(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.create(int)"""
        return Buffer._wrap(_LARGE_INTEGER.create(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nu_LowPart(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.LARGE_INTEGER.nu_LowPart(long)"""
        return int._wrap(_LARGE_INTEGER.nu_LowPart(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_LARGE_INTEGER.malloc(_int.valueOf(arg0), arg1))

    @overload
    def u_LowPart(self, arg0: int) -> 'LARGE_INTEGER':
        """public org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.u_LowPart(int)"""
        return 'LARGE_INTEGER'._wrap(super(_LARGE_INTEGER, self).u_LowPart(_int.valueOf(arg0)))

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
    def calloc() -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.calloc()"""
        return LARGE_INTEGER._wrap(_LARGE_INTEGER.calloc())

    @staticmethod
    @overload
    def nQuadPart(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.LARGE_INTEGER.nQuadPart(long)"""
        return int._wrap(_LARGE_INTEGER.nQuadPart(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.create(long,int)"""
        return Buffer._wrap(_LARGE_INTEGER.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.calloc(org.lwjgl.system.MemoryStack)"""
        return LARGE_INTEGER._wrap(_LARGE_INTEGER.calloc(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def u_HighPart(self, arg0: int) -> 'LARGE_INTEGER':
        """public org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.u_HighPart(int)"""
        return 'LARGE_INTEGER'._wrap(super(_LARGE_INTEGER, self).u_HighPart(_int.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def u_LowPart(self) -> int:
        """public int org.lwjgl.system.windows.LARGE_INTEGER.u_LowPart()"""
        return int._wrap(super(LARGE_INTEGER, self).u_LowPart())

    @staticmethod
    @overload
    def nu_HighPart(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.LARGE_INTEGER.nu_HighPart(long,int)"""
        _LARGE_INTEGER.nu_HighPart(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def QuadPart(self) -> int:
        """public long org.lwjgl.system.windows.LARGE_INTEGER.QuadPart()"""
        return int._wrap(super(LARGE_INTEGER, self).QuadPart())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address()) 
 
 
# CLASS: org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer
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
import org.lwjgl.system.windows.RECT as _RECT
_RECT = _RECT
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
import org.lwjgl.system.windows.WINDOWPLACEMENT as _WINDOWPLACEMENT_Buffer
_Buffer = _WINDOWPLACEMENT_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.windows.POINT as _POINT
_POINT = _POINT
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.windows.WINDOWPLACEMENT.Buffer"""
 
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
    def ptMaxPosition(self, arg0: 'POINT') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMaxPosition(org.lwjgl.system.windows.POINT)"""
        return 'Buffer'._wrap(super(_Buffer, self).ptMaxPosition(arg0))

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
    def ptMaxPosition(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMaxPosition(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'Buffer'._wrap(super(_Buffer, self).ptMaxPosition(arg0))

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
    def length(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.length(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).length(_int.valueOf(arg0)))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.flags()"""
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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def length(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.length()"""
        return int._wrap(super(Buffer, self).length())

    @overload
    def showCmd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.showCmd(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).showCmd(_int.valueOf(arg0)))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def rcNormalPosition(self, arg0: 'RECT') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.rcNormalPosition(org.lwjgl.system.windows.RECT)"""
        return 'Buffer'._wrap(super(_Buffer, self).rcNormalPosition(arg0))

    @overload
    def ptMinPosition(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMinPosition(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'Buffer'._wrap(super(_Buffer, self).ptMinPosition(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def rcNormalPosition(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.rcNormalPosition()"""
        return 'RECT'._wrap(super(Buffer, self).rcNormalPosition())

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
    def ptMinPosition(self, arg0: 'POINT') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMinPosition(org.lwjgl.system.windows.POINT)"""
        return 'Buffer'._wrap(super(_Buffer, self).ptMinPosition(arg0))

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
    def showCmd(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.showCmd()"""
        return int._wrap(super(Buffer, self).showCmd())

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
    def ptMinPosition(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMinPosition()"""
        return 'POINT'._wrap(super(Buffer, self).ptMinPosition())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.flags(int)"""
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

    @overload
    def ptMaxPosition(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMaxPosition()"""
        return 'POINT'._wrap(super(Buffer, self).ptMaxPosition())

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
    def rcNormalPosition(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.rcNormalPosition(java.util.function.Consumer<org.lwjgl.system.windows.RECT>)"""
        return 'Buffer'._wrap(super(_Buffer, self).rcNormalPosition(arg0))

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
 
 
# CLASS: org.lwjgl.system.windows.MONITORINFOEX$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.util.function.Consumer as Consumer
import org.lwjgl.system.windows.MONITORINFOEX as _MONITORINFOEX_Buffer
_Buffer = _MONITORINFOEX_Buffer.Buffer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.windows.RECT as _RECT
_RECT = _RECT
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
    """org.lwjgl.system.windows.MONITORINFOEX.Buffer"""
 
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
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.MONITORINFOEX$Buffer.dwFlags()"""
        return int._wrap(super(Buffer, self).dwFlags())

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
    def cbSize(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX$Buffer.cbSize(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).cbSize(_int.valueOf(arg0)))

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
    def rcWork(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX$Buffer.rcWork()"""
        return 'RECT'._wrap(super(Buffer, self).rcWork())

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
    def cbSize(self) -> int:
        """public int org.lwjgl.system.windows.MONITORINFOEX$Buffer.cbSize()"""
        return int._wrap(super(Buffer, self).cbSize())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @overload
    def szDeviceString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.MONITORINFOEX$Buffer.szDeviceString()"""
        return str._wrap(super(Buffer, self).szDeviceString())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.MONITORINFOEX$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def szDevice(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.MONITORINFOEX$Buffer.szDevice()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).szDevice())

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
        """public org.lwjgl.system.windows.MONITORINFOEX$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def rcMonitor(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX$Buffer.rcMonitor()"""
        return 'RECT'._wrap(super(Buffer, self).rcMonitor())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.Crypt32$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.windows.Crypt32 as _Crypt32_Functions
_Functions = _Crypt32_Functions.Functions
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.system.windows.Crypt32.Functions"""
 
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
 
 
# CLASS: org.lwjgl.system.windows.WindowProc
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

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.system.windows.WindowProcI as _WindowProcI
_WindowProcI = _WindowProcI
import org.lwjgl.system.windows.WindowProc as _WindowProc
_WindowProc = _WindowProc
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WindowProc():
    """org.lwjgl.system.windows.WindowProc"""
 
    @staticmethod
    def _wrap(java_value: _WindowProc) -> 'WindowProc':
        return WindowProc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowProc):
        """
        Dynamic initializer for WindowProc.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowProc__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowProc__wrapper":
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
    def createSafe(arg0: int) -> 'WindowProc':
        """public static org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WindowProc.createSafe(long)"""
        return WindowProc._wrap(_WindowProc.createSafe(_long.valueOf(arg0)))

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

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.windows.WindowProcI.callback(long,long)"""
        super(_WindowProcI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.windows.WindowProcI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(WindowProcI, self).getCallInterface())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @staticmethod
    @overload
    def create(arg0: 'WindowProcI') -> 'WindowProc':
        """public static org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WindowProc.create(org.lwjgl.system.windows.WindowProcI)"""
        return WindowProc._wrap(_WindowProc.create(arg0))

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
    def create(arg0: int) -> 'WindowProc':
        """public static org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WindowProc.create(long)"""
        return WindowProc._wrap(_WindowProc.create(_long.valueOf(arg0)))

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract long org.lwjgl.system.windows.WindowProcI.invoke(long,int,long,long)"""
        pass 
 
 
# CLASS: org.lwjgl.system.windows.POINTL
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
import org.lwjgl.system.windows.POINTL as _POINTL
_POINTL = _POINTL
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import org.lwjgl.system.windows.POINTL as _POINTL_Buffer
_Buffer = _POINTL_Buffer.Buffer
import java.lang.Class as _Class
_Class = _Class
 
class POINTL():
    """org.lwjgl.system.windows.POINTL"""
 
    @staticmethod
    def _wrap(java_value: _POINTL) -> 'POINTL':
        return POINTL(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _POINTL):
        """
        Dynamic initializer for POINTL.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_POINTL__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_POINTL__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'POINTL') -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.set(org.lwjgl.system.windows.POINTL)"""
        return 'POINTL'._wrap(super(_POINTL, self).set(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.calloc(org.lwjgl.system.MemoryStack)"""
        return POINTL._wrap(_POINTL.calloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.create(long,int)"""
        return Buffer._wrap(_POINTL.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_POINTL.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.malloc(int)"""
        return Buffer._wrap(_POINTL.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_POINTL.callocStack(_int.valueOf(arg0), arg1))

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
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.create(int)"""
        return Buffer._wrap(_POINTL.create(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.malloc(org.lwjgl.system.MemoryStack)"""
        return POINTL._wrap(_POINTL.malloc(arg0))

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.POINTL.ny(long)"""
        return int._wrap(_POINTL.ny(_long.valueOf(arg0)))

    @overload
    def y(self, arg0: int) -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.y(int)"""
        return 'POINTL'._wrap(super(_POINTL, self).y(_int.valueOf(arg0)))

    @overload
    def x(self) -> int:
        """public int org.lwjgl.system.windows.POINTL.x()"""
        return int._wrap(super(POINTL, self).x())

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
    def create(arg0: int) -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.create(long)"""
        return POINTL._wrap(_POINTL.create(_long.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.POINTL.nx(long)"""
        return int._wrap(_POINTL.nx(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.POINTL.sizeof()"""
        return int._wrap(super(POINTL, self).sizeof())

    @staticmethod
    @overload
    def malloc() -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.malloc()"""
        return POINTL._wrap(_POINTL.malloc())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.mallocStack(org.lwjgl.system.MemoryStack)"""
        return POINTL._wrap(_POINTL.mallocStack(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def mallocStack() -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.mallocStack()"""
        return POINTL._wrap(_POINTL.mallocStack())

    @overload
    def x(self, arg0: int) -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.x(int)"""
        return 'POINTL'._wrap(super(_POINTL, self).x(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.create()"""
        return POINTL._wrap(_POINTL.create())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_POINTL.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.callocStack(int)"""
        return Buffer._wrap(_POINTL.callocStack(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc() -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.calloc()"""
        return POINTL._wrap(_POINTL.calloc())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def y(self) -> int:
        """public int org.lwjgl.system.windows.POINTL.y()"""
        return int._wrap(super(POINTL, self).y())

    @staticmethod
    @overload
    def ny(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.POINTL.ny(long,int)"""
        _POINTL.ny(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: int, arg1: int) -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.set(int,int)"""
        return 'POINTL'._wrap(super(_POINTL, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.calloc(int)"""
        return Buffer._wrap(_POINTL.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.callocStack(org.lwjgl.system.MemoryStack)"""
        return POINTL._wrap(_POINTL.callocStack(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.mallocStack(int)"""
        return Buffer._wrap(_POINTL.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.createSafe(long,int)"""
        return Buffer._wrap(_POINTL.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack() -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.callocStack()"""
        return POINTL._wrap(_POINTL.callocStack())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_POINTL.mallocStack(_int.valueOf(arg0), arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.createSafe(long)"""
        return POINTL._wrap(_POINTL.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nx(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.POINTL.nx(long,int)"""
        _POINTL.nx(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.POINTL(java.nio.ByteBuffer)"""
        val = _POINTL(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.windows.TOUCHINPUT$Buffer
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
import org.lwjgl.system.windows.TOUCHINPUT as _TOUCHINPUT_Buffer
_Buffer = _TOUCHINPUT_Buffer.Buffer
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
    """org.lwjgl.system.windows.TOUCHINPUT.Buffer"""
 
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
    def y(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.y()"""
        return int._wrap(super(Buffer, self).y())

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
    def hSource(self) -> int:
        """public long org.lwjgl.system.windows.TOUCHINPUT$Buffer.hSource()"""
        return int._wrap(super(Buffer, self).hSource())

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
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.dwFlags()"""
        return int._wrap(super(Buffer, self).dwFlags())

    @overload
    def dwMask(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.dwMask()"""
        return int._wrap(super(Buffer, self).dwMask())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dwTime(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.dwTime()"""
        return int._wrap(super(Buffer, self).dwTime())

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
    def cxContact(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.cxContact()"""
        return int._wrap(super(Buffer, self).cxContact())

    @overload
    def cyContact(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.cyContact()"""
        return int._wrap(super(Buffer, self).cyContact())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.TOUCHINPUT$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def x(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.x()"""
        return int._wrap(super(Buffer, self).x())

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
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.TOUCHINPUT$Buffer.dwExtraInfo()"""
        return int._wrap(super(Buffer, self).dwExtraInfo())

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
    def dwID(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.dwID()"""
        return int._wrap(super(Buffer, self).dwID())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.TOUCHINPUT$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val 
 
 
# CLASS: org.lwjgl.system.windows.POINTL$Buffer
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
import org.lwjgl.system.windows.POINTL as _POINTL_Buffer
_Buffer = _POINTL_Buffer.Buffer
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
    """org.lwjgl.system.windows.POINTL.Buffer"""
 
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
        """public org.lwjgl.system.windows.POINTL$Buffer(java.nio.ByteBuffer)"""
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

    @overload
    def y(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL$Buffer.y(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).y(_int.valueOf(arg0)))

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
    def y(self) -> int:
        """public int org.lwjgl.system.windows.POINTL$Buffer.y()"""
        return int._wrap(super(Buffer, self).y())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def x(self) -> int:
        """public int org.lwjgl.system.windows.POINTL$Buffer.x()"""
        return int._wrap(super(Buffer, self).x())

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
    def x(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL$Buffer.x(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).x(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.POINTL$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
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
 
 
# CLASS: org.lwjgl.system.windows.GDI32$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.windows.GDI32 as _GDI32_Functions
_Functions = _GDI32_Functions.Functions
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.system.windows.GDI32.Functions"""
 
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
 
 
# CLASS: org.lwjgl.system.windows.POINT
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
import org.lwjgl.system.windows.POINT as _POINT_Buffer
_Buffer = _POINT_Buffer.Buffer
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
import org.lwjgl.system.windows.POINT as _POINT
_POINT = _POINT
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class POINT():
    """org.lwjgl.system.windows.POINT"""
 
    @staticmethod
    def _wrap(java_value: _POINT) -> 'POINT':
        return POINT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _POINT):
        """
        Dynamic initializer for POINT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_POINT__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_POINT__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.calloc(int)"""
        return Buffer._wrap(_POINT.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.malloc()"""
        return POINT._wrap(_POINT.malloc())

    @staticmethod
    @overload
    def create() -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.create()"""
        return POINT._wrap(_POINT.create())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.create(int)"""
        return Buffer._wrap(_POINT.create(_int.valueOf(arg0)))

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
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_POINT.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack() -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.mallocStack()"""
        return POINT._wrap(_POINT.mallocStack())

    @overload
    def x(self, arg0: int) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.x(int)"""
        return 'POINT'._wrap(super(_POINT, self).x(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.POINT.sizeof()"""
        return int._wrap(super(POINT, self).sizeof())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.create(long,int)"""
        return Buffer._wrap(_POINT.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def set(self, arg0: int, arg1: int) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.set(int,int)"""
        return 'POINT'._wrap(super(_POINT, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.mallocStack(int)"""
        return Buffer._wrap(_POINT.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.POINT.nx(long)"""
        return int._wrap(_POINT.nx(_long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.POINT(java.nio.ByteBuffer)"""
        val = _POINT(arg0)
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
    def y(self, arg0: int) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.y(int)"""
        return 'POINT'._wrap(super(_POINT, self).y(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_POINT.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.POINT.ny(long)"""
        return int._wrap(_POINT.ny(_long.valueOf(arg0)))

    @overload
    def y(self) -> int:
        """public int org.lwjgl.system.windows.POINT.y()"""
        return int._wrap(super(POINT, self).y())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_POINT.mallocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def x(self) -> int:
        """public int org.lwjgl.system.windows.POINT.x()"""
        return int._wrap(super(POINT, self).x())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.callocStack(int)"""
        return Buffer._wrap(_POINT.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.malloc(org.lwjgl.system.MemoryStack)"""
        return POINT._wrap(_POINT.malloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.calloc(org.lwjgl.system.MemoryStack)"""
        return POINT._wrap(_POINT.calloc(arg0))

    @staticmethod
    @overload
    def ny(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.POINT.ny(long,int)"""
        _POINT.ny(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return POINT._wrap(_POINT.mallocStack(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.malloc(int)"""
        return Buffer._wrap(_POINT.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.create(long)"""
        return POINT._wrap(_POINT.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_POINT.callocStack(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: 'POINT') -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.set(org.lwjgl.system.windows.POINT)"""
        return 'POINT'._wrap(super(_POINT, self).set(arg0))

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
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.createSafe(long,int)"""
        return Buffer._wrap(_POINT.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack() -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.callocStack()"""
        return POINT._wrap(_POINT.callocStack())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.createSafe(long)"""
        return POINT._wrap(_POINT.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.calloc()"""
        return POINT._wrap(_POINT.calloc())

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
    def nx(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.POINT.nx(long,int)"""
        _POINT.nx(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.callocStack(org.lwjgl.system.MemoryStack)"""
        return POINT._wrap(_POINT.callocStack(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer
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
import org.lwjgl.system.windows.DISPLAY_DEVICE as _DISPLAY_DEVICE_Buffer
_Buffer = _DISPLAY_DEVICE_Buffer.Buffer
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
    """org.lwjgl.system.windows.DISPLAY_DEVICE.Buffer"""
 
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
    def StateFlags(self) -> int:
        """public int org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.StateFlags()"""
        return int._wrap(super(Buffer, self).StateFlags())

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
    def DeviceNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceNameString()"""
        return str._wrap(super(Buffer, self).DeviceNameString())

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
        """public org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def cb(self) -> int:
        """public int org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.cb()"""
        return int._wrap(super(Buffer, self).cb())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @overload
    def DeviceString(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceString()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).DeviceString())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).stream())

    @overload
    def DeviceStringString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceStringString()"""
        return str._wrap(super(Buffer, self).DeviceStringString())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @overload
    def DeviceKeyString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceKeyString()"""
        return str._wrap(super(Buffer, self).DeviceKeyString())

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
    def DeviceIDString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceIDString()"""
        return str._wrap(super(Buffer, self).DeviceIDString())

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
    def DeviceID(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceID()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).DeviceID())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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
    def DeviceKey(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceKey()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).DeviceKey())

    @overload
    def DeviceName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceName()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).DeviceName())

    @overload
    def cb(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.cb(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).cb(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.INPUT
from pyquantum_helper import import_once as _import_once
import org.lwjgl.system.windows.INPUT as _INPUT_Buffer
_Buffer = _INPUT_Buffer.Buffer
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
import org.lwjgl.system.windows.INPUT as _INPUT
_INPUT = _INPUT
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import org.lwjgl.system.windows.MOUSEINPUT as _MOUSEINPUT
_MOUSEINPUT = _MOUSEINPUT
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.lwjgl.system.windows.HARDWAREINPUT as _HARDWAREINPUT
_HARDWAREINPUT = _HARDWAREINPUT
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.windows.KEYBDINPUT as _KEYBDINPUT
_KEYBDINPUT = _KEYBDINPUT
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class INPUT():
    """org.lwjgl.system.windows.INPUT"""
 
    @staticmethod
    def _wrap(java_value: _INPUT) -> 'INPUT':
        return INPUT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _INPUT):
        """
        Dynamic initializer for INPUT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_INPUT__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_INPUT__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def type(self, arg0: int) -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.type(int)"""
        return 'INPUT'._wrap(super(_INPUT, self).type(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_hi(arg0: int, arg1: 'HARDWAREINPUT'):
        """public static void org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_hi(long,org.lwjgl.system.windows.HARDWAREINPUT)"""
        _INPUT.nDUMMYUNIONNAME_hi(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def mallocStack() -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.mallocStack()"""
        return INPUT._wrap(_INPUT.mallocStack())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return INPUT._wrap(_INPUT.mallocStack(arg0))

    @overload
    def DUMMYUNIONNAME_mi(self, arg0: 'MOUSEINPUT') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_mi(org.lwjgl.system.windows.MOUSEINPUT)"""
        return 'INPUT'._wrap(super(_INPUT, self).DUMMYUNIONNAME_mi(arg0))

    @overload
    def DUMMYUNIONNAME_hi(self) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_hi()"""
        return 'HARDWAREINPUT'._wrap(super(INPUT, self).DUMMYUNIONNAME_hi())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_INPUT.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_ki(arg0: int) -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_ki(long)"""
        return KEYBDINPUT._wrap(_INPUT.nDUMMYUNIONNAME_ki(_long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.createSafe(long)"""
        return INPUT._wrap(_INPUT.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def DUMMYUNIONNAME_ki(self, arg0: 'KEYBDINPUT') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_ki(org.lwjgl.system.windows.KEYBDINPUT)"""
        return 'INPUT'._wrap(super(_INPUT, self).DUMMYUNIONNAME_ki(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.callocStack(int)"""
        return Buffer._wrap(_INPUT.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.create(long)"""
        return INPUT._wrap(_INPUT.create(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'INPUT') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.set(org.lwjgl.system.windows.INPUT)"""
        return 'INPUT'._wrap(super(_INPUT, self).set(arg0))

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
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.create(int)"""
        return Buffer._wrap(_INPUT.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_INPUT.malloc(_int.valueOf(arg0), arg1))

    @overload
    def DUMMYUNIONNAME_mi(self) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_mi()"""
        return 'MOUSEINPUT'._wrap(super(INPUT, self).DUMMYUNIONNAME_mi())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def type(self) -> int:
        """public int org.lwjgl.system.windows.INPUT.type()"""
        return int._wrap(super(INPUT, self).type())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.calloc(int)"""
        return Buffer._wrap(_INPUT.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ntype(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.INPUT.ntype(long,int)"""
        _INPUT.ntype(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.malloc(int)"""
        return Buffer._wrap(_INPUT.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_ki(arg0: int, arg1: 'KEYBDINPUT'):
        """public static void org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_ki(long,org.lwjgl.system.windows.KEYBDINPUT)"""
        _INPUT.nDUMMYUNIONNAME_ki(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_INPUT.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create() -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.create()"""
        return INPUT._wrap(_INPUT.create())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_mi(arg0: int, arg1: 'MOUSEINPUT'):
        """public static void org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_mi(long,org.lwjgl.system.windows.MOUSEINPUT)"""
        _INPUT.nDUMMYUNIONNAME_mi(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.mallocStack(int)"""
        return Buffer._wrap(_INPUT.mallocStack(_int.valueOf(arg0)))

    @overload
    def DUMMYUNIONNAME_ki(self) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_ki()"""
        return 'KEYBDINPUT'._wrap(super(INPUT, self).DUMMYUNIONNAME_ki())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.callocStack(org.lwjgl.system.MemoryStack)"""
        return INPUT._wrap(_INPUT.callocStack(arg0))

    @staticmethod
    @overload
    def calloc() -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.calloc()"""
        return INPUT._wrap(_INPUT.calloc())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.malloc(org.lwjgl.system.MemoryStack)"""
        return INPUT._wrap(_INPUT.malloc(arg0))

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_hi(arg0: int) -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_hi(long)"""
        return HARDWAREINPUT._wrap(_INPUT.nDUMMYUNIONNAME_hi(_long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.INPUT.sizeof()"""
        return int._wrap(super(INPUT, self).sizeof())

    @overload
    def DUMMYUNIONNAME_hi(self, arg0: 'HARDWAREINPUT') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_hi(org.lwjgl.system.windows.HARDWAREINPUT)"""
        return 'INPUT'._wrap(super(_INPUT, self).DUMMYUNIONNAME_hi(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.calloc(org.lwjgl.system.MemoryStack)"""
        return INPUT._wrap(_INPUT.calloc(arg0))

    @staticmethod
    @overload
    def ntype(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.INPUT.ntype(long)"""
        return int._wrap(_INPUT.ntype(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.create(long,int)"""
        return Buffer._wrap(_INPUT.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def DUMMYUNIONNAME_ki(self, arg0: 'Consumer') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_ki(java.util.function.Consumer<org.lwjgl.system.windows.KEYBDINPUT>)"""
        return 'INPUT'._wrap(super(_INPUT, self).DUMMYUNIONNAME_ki(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.INPUT(java.nio.ByteBuffer)"""
        val = _INPUT(arg0)
        self.__wrapper = val

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_INPUT.callocStack(_int.valueOf(arg0), arg1))

    @overload
    def DUMMYUNIONNAME_mi(self, arg0: 'Consumer') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_mi(java.util.function.Consumer<org.lwjgl.system.windows.MOUSEINPUT>)"""
        return 'INPUT'._wrap(super(_INPUT, self).DUMMYUNIONNAME_mi(arg0))

    @staticmethod
    @overload
    def callocStack() -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.callocStack()"""
        return INPUT._wrap(_INPUT.callocStack())

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
    def malloc() -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.malloc()"""
        return INPUT._wrap(_INPUT.malloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.createSafe(long,int)"""
        return Buffer._wrap(_INPUT.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def DUMMYUNIONNAME_hi(self, arg0: 'Consumer') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_hi(java.util.function.Consumer<org.lwjgl.system.windows.HARDWAREINPUT>)"""
        return 'INPUT'._wrap(super(_INPUT, self).DUMMYUNIONNAME_hi(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_mi(arg0: int) -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_mi(long)"""
        return MOUSEINPUT._wrap(_INPUT.nDUMMYUNIONNAME_mi(_long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.windows.Kernel32
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
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
import org.lwjgl.system.windows.Kernel32 as _Kernel32
_Kernel32 = _Kernel32
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Kernel32():
    """org.lwjgl.system.windows.Kernel32"""
 
    @staticmethod
    def _wrap(java_value: _Kernel32) -> 'Kernel32':
        return Kernel32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Kernel32):
        """
        Dynamic initializer for Kernel32.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Kernel32__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Kernel32__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def GetCurrentProcess() -> int:
        """public static long org.lwjgl.system.windows.Kernel32.GetCurrentProcess()"""
        return int._wrap(_Kernel32.GetCurrentProcess())

    @staticmethod
    @overload
    def GetThreadId(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetThreadId(long)"""
        return int._wrap(_Kernel32.GetThreadId(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def GetCurrentThread() -> int:
        """public static long org.lwjgl.system.windows.Kernel32.GetCurrentThread()"""
        return int._wrap(_Kernel32.GetCurrentThread())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def GetProcessId(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetProcessId(long)"""
        return int._wrap(_Kernel32.GetProcessId(_long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.windows.Kernel32.getLibrary()"""
        return pyglsystem.SharedLibrary._wrap(_Kernel32.getLibrary())

    @staticmethod
    @overload
    def GetCurrentThreadId() -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetCurrentThreadId()"""
        return int._wrap(_Kernel32.GetCurrentThreadId())

    @staticmethod
    @overload
    def GetCurrentProcessorNumber() -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetCurrentProcessorNumber()"""
        return int._wrap(_Kernel32.GetCurrentProcessorNumber())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def GetCurrentProcessId() -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetCurrentProcessId()"""
        return int._wrap(_Kernel32.GetCurrentProcessId())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def GetProcessIdOfThread(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetProcessIdOfThread(long)"""
        return int._wrap(_Kernel32.GetProcessIdOfThread(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.windows.Kernel32$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.lwjgl.system.windows.Kernel32 as _Kernel32_Functions
_Functions = _Kernel32_Functions.Functions
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.system.windows.Kernel32.Functions"""
 
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
 
 
# CLASS: org.lwjgl.system.windows.MONITORINFOEX
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.lwjgl.system.windows.MONITORINFOEX as _MONITORINFOEX
_MONITORINFOEX = _MONITORINFOEX
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
import org.lwjgl.system.windows.MONITORINFOEX as _MONITORINFOEX_Buffer
_Buffer = _MONITORINFOEX_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.windows.RECT as _RECT
_RECT = _RECT
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MONITORINFOEX():
    """org.lwjgl.system.windows.MONITORINFOEX"""
 
    @staticmethod
    def _wrap(java_value: _MONITORINFOEX) -> 'MONITORINFOEX':
        return MONITORINFOEX(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MONITORINFOEX):
        """
        Dynamic initializer for MONITORINFOEX.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MONITORINFOEX__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MONITORINFOEX__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def mallocStack() -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.mallocStack()"""
        return MONITORINFOEX._wrap(_MONITORINFOEX.mallocStack())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.callocStack(org.lwjgl.system.MemoryStack)"""
        return MONITORINFOEX._wrap(_MONITORINFOEX.callocStack(arg0))

    @staticmethod
    @overload
    def create() -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.create()"""
        return MONITORINFOEX._wrap(_MONITORINFOEX.create())

    @overload
    def cbSize(self) -> int:
        """public int org.lwjgl.system.windows.MONITORINFOEX.cbSize()"""
        return int._wrap(super(MONITORINFOEX, self).cbSize())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.malloc(int)"""
        return Buffer._wrap(_MONITORINFOEX.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MONITORINFOEX.mallocStack(_int.valueOf(arg0), arg1))

    @overload
    def rcWork(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX.rcWork()"""
        return 'RECT'._wrap(super(MONITORINFOEX, self).rcWork())

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.MONITORINFOEX.dwFlags()"""
        return int._wrap(super(MONITORINFOEX, self).dwFlags())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nszDeviceString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.MONITORINFOEX.nszDeviceString(long)"""
        return str._wrap(_MONITORINFOEX.nszDeviceString(_long.valueOf(arg0)))

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
    def callocStack() -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.callocStack()"""
        return MONITORINFOEX._wrap(_MONITORINFOEX.callocStack())

    @overload
    def cbSize(self, arg0: int) -> 'MONITORINFOEX':
        """public org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.cbSize(int)"""
        return 'MONITORINFOEX'._wrap(super(_MONITORINFOEX, self).cbSize(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.malloc(org.lwjgl.system.MemoryStack)"""
        return MONITORINFOEX._wrap(_MONITORINFOEX.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.create(int)"""
        return Buffer._wrap(_MONITORINFOEX.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.calloc()"""
        return MONITORINFOEX._wrap(_MONITORINFOEX.calloc())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.mallocStack(int)"""
        return Buffer._wrap(_MONITORINFOEX.mallocStack(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.MONITORINFOEX(java.nio.ByteBuffer)"""
        val = _MONITORINFOEX(arg0)
        self.__wrapper = val

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.MONITORINFOEX.sizeof()"""
        return int._wrap(super(MONITORINFOEX, self).sizeof())

    @overload
    def set(self, arg0: 'MONITORINFOEX') -> 'MONITORINFOEX':
        """public org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.set(org.lwjgl.system.windows.MONITORINFOEX)"""
        return 'MONITORINFOEX'._wrap(super(_MONITORINFOEX, self).set(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: int) -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.create(long)"""
        return MONITORINFOEX._wrap(_MONITORINFOEX.create(_long.valueOf(arg0)))

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
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MONITORINFOEX.callocStack(_int.valueOf(arg0), arg1))

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
    def ncbSize(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MONITORINFOEX.ncbSize(long)"""
        return int._wrap(_MONITORINFOEX.ncbSize(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.calloc(org.lwjgl.system.MemoryStack)"""
        return MONITORINFOEX._wrap(_MONITORINFOEX.calloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.create(long,int)"""
        return Buffer._wrap(_MONITORINFOEX.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nrcMonitor(arg0: int) -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX.nrcMonitor(long)"""
        return RECT._wrap(_MONITORINFOEX.nrcMonitor(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncbSize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MONITORINFOEX.ncbSize(long,int)"""
        _MONITORINFOEX.ncbSize(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.calloc(int)"""
        return Buffer._wrap(_MONITORINFOEX.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.createSafe(long)"""
        return MONITORINFOEX._wrap(_MONITORINFOEX.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MONITORINFOEX.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.callocStack(int)"""
        return Buffer._wrap(_MONITORINFOEX.callocStack(_int.valueOf(arg0)))

    @overload
    def rcMonitor(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX.rcMonitor()"""
        return 'RECT'._wrap(super(MONITORINFOEX, self).rcMonitor())

    @staticmethod
    @overload
    def nszDevice(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.MONITORINFOEX.nszDevice(long)"""
        return ByteBuffer._wrap(_MONITORINFOEX.nszDevice(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.createSafe(long,int)"""
        return Buffer._wrap(_MONITORINFOEX.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def szDevice(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.MONITORINFOEX.szDevice()"""
        return 'ByteBuffer'._wrap(super(MONITORINFOEX, self).szDevice())

    @staticmethod
    @overload
    def nrcWork(arg0: int) -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX.nrcWork(long)"""
        return RECT._wrap(_MONITORINFOEX.nrcWork(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.mallocStack(org.lwjgl.system.MemoryStack)"""
        return MONITORINFOEX._wrap(_MONITORINFOEX.mallocStack(arg0))

    @staticmethod
    @overload
    def malloc() -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.malloc()"""
        return MONITORINFOEX._wrap(_MONITORINFOEX.malloc())

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
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MONITORINFOEX.malloc(_int.valueOf(arg0), arg1))

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
    def ndwFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MONITORINFOEX.ndwFlags(long)"""
        return int._wrap(_MONITORINFOEX.ndwFlags(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def szDeviceString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.MONITORINFOEX.szDeviceString()"""
        return str._wrap(super(MONITORINFOEX, self).szDeviceString()) 
 
 
# CLASS: org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer
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
import org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR as _PIXELFORMATDESCRIPTOR_Buffer
_Buffer = _PIXELFORMATDESCRIPTOR_Buffer.Buffer
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
    """org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.Buffer"""
 
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
    def nSize(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.nSize(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).nSize(_short.valueOf(arg0)))

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
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @overload
    def iLayerType(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.iLayerType()"""
        return int._wrap(super(Buffer, self).iLayerType())

    @overload
    def cAccumBlueBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumBlueBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cAccumBlueBits(_byte.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @overload
    def cGreenBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cGreenBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cGreenBits(_byte.valueOf(arg0)))

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
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def cDepthBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cDepthBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cDepthBits(_byte.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def cBlueShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cBlueShift()"""
        return int._wrap(super(Buffer, self).cBlueShift())

    @overload
    def cGreenBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cGreenBits()"""
        return int._wrap(super(Buffer, self).cGreenBits())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def cRedShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cRedShift()"""
        return int._wrap(super(Buffer, self).cRedShift())

    @overload
    def cBlueShift(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cBlueShift(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cBlueShift(_byte.valueOf(arg0)))

    @overload
    def dwFlags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwFlags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).dwFlags(_int.valueOf(arg0)))

    @overload
    def cAlphaBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAlphaBits()"""
        return int._wrap(super(Buffer, self).cAlphaBits())

    @overload
    def dwDamageMask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwDamageMask(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).dwDamageMask(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def cAccumRedBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumRedBits()"""
        return int._wrap(super(Buffer, self).cAccumRedBits())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def iPixelType(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.iPixelType()"""
        return int._wrap(super(Buffer, self).iPixelType())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @overload
    def cAccumGreenBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumGreenBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cAccumGreenBits(_byte.valueOf(arg0)))

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwFlags()"""
        return int._wrap(super(Buffer, self).dwFlags())

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
    def cAuxBuffers(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAuxBuffers(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cAuxBuffers(_byte.valueOf(arg0)))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def cBlueBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cBlueBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cBlueBits(_byte.valueOf(arg0)))

    @overload
    def cRedBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cRedBits()"""
        return int._wrap(super(Buffer, self).cRedBits())

    @overload
    def cAlphaShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAlphaShift()"""
        return int._wrap(super(Buffer, self).cAlphaShift())

    @overload
    def cAlphaShift(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAlphaShift(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cAlphaShift(_byte.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def dwVisibleMask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwVisibleMask(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).dwVisibleMask(_int.valueOf(arg0)))

    @overload
    def nVersion(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.nVersion(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).nVersion(_short.valueOf(arg0)))

    @overload
    def iPixelType(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.iPixelType(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).iPixelType(_byte.valueOf(arg0)))

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def cRedBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cRedBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cRedBits(_byte.valueOf(arg0)))

    @overload
    def cStencilBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cStencilBits()"""
        return int._wrap(super(Buffer, self).cStencilBits())

    @overload
    def dwVisibleMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwVisibleMask()"""
        return int._wrap(super(Buffer, self).dwVisibleMask())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def bReserved(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.bReserved(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).bReserved(_byte.valueOf(arg0)))

    @overload
    def cAccumRedBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumRedBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cAccumRedBits(_byte.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0)))

    @overload
    def cStencilBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cStencilBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cStencilBits(_byte.valueOf(arg0)))

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
    def cAccumGreenBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumGreenBits()"""
        return int._wrap(super(Buffer, self).cAccumGreenBits())

    @overload
    def cAccumBlueBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumBlueBits()"""
        return int._wrap(super(Buffer, self).cAccumBlueBits())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @overload
    def cAccumAlphaBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumAlphaBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cAccumAlphaBits(_byte.valueOf(arg0)))

    @overload
    def cBlueBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cBlueBits()"""
        return int._wrap(super(Buffer, self).cBlueBits())

    @overload
    def cGreenShift(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cGreenShift(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cGreenShift(_byte.valueOf(arg0)))

    @overload
    def cAuxBuffers(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAuxBuffers()"""
        return int._wrap(super(Buffer, self).cAuxBuffers())

    @overload
    def cAccumBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumBits()"""
        return int._wrap(super(Buffer, self).cAccumBits())

    @overload
    def cDepthBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cDepthBits()"""
        return int._wrap(super(Buffer, self).cDepthBits())

    @overload
    def dwDamageMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwDamageMask()"""
        return int._wrap(super(Buffer, self).dwDamageMask())

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
    def nVersion(self) -> int:
        """public short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.nVersion()"""
        return int._wrap(super(Buffer, self).nVersion())

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

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def cColorBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cColorBits()"""
        return int._wrap(super(Buffer, self).cColorBits())

    @overload
    def cAccumAlphaBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumAlphaBits()"""
        return int._wrap(super(Buffer, self).cAccumAlphaBits())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer(long,int)"""
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
    def dwLayerMask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwLayerMask(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).dwLayerMask(_int.valueOf(arg0)))

    @overload
    def cAccumBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cAccumBits(_byte.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def cAlphaBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAlphaBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cAlphaBits(_byte.valueOf(arg0)))

    @overload
    def iLayerType(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.iLayerType(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).iLayerType(_byte.valueOf(arg0)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

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
    def cGreenShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cGreenShift()"""
        return int._wrap(super(Buffer, self).cGreenShift())

    @overload
    def dwLayerMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwLayerMask()"""
        return int._wrap(super(Buffer, self).dwLayerMask())

    @overload
    def bReserved(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.bReserved()"""
        return int._wrap(super(Buffer, self).bReserved())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def nSize(self) -> int:
        """public short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.nSize()"""
        return int._wrap(super(Buffer, self).nSize())

    @overload
    def cColorBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cColorBits(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cColorBits(_byte.valueOf(arg0)))

    @overload
    def cRedShift(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cRedShift(byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).cRedShift(_byte.valueOf(arg0)))

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.DISPLAY_DEVICE
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
import org.lwjgl.system.windows.DISPLAY_DEVICE as _DISPLAY_DEVICE
_DISPLAY_DEVICE = _DISPLAY_DEVICE
import org.lwjgl.system.windows.DISPLAY_DEVICE as _DISPLAY_DEVICE_Buffer
_Buffer = _DISPLAY_DEVICE_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DISPLAY_DEVICE():
    """org.lwjgl.system.windows.DISPLAY_DEVICE"""
 
    @staticmethod
    def _wrap(java_value: _DISPLAY_DEVICE) -> 'DISPLAY_DEVICE':
        return DISPLAY_DEVICE(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DISPLAY_DEVICE):
        """
        Dynamic initializer for DISPLAY_DEVICE.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DISPLAY_DEVICE__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DISPLAY_DEVICE__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nDeviceIDString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceIDString(long)"""
        return str._wrap(_DISPLAY_DEVICE.nDeviceIDString(_long.valueOf(arg0)))

    @overload
    def cb(self) -> int:
        """public int org.lwjgl.system.windows.DISPLAY_DEVICE.cb()"""
        return int._wrap(super(DISPLAY_DEVICE, self).cb())

    @overload
    def DeviceID(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceID()"""
        return 'ByteBuffer'._wrap(super(DISPLAY_DEVICE, self).DeviceID())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nDeviceName(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceName(long)"""
        return ByteBuffer._wrap(_DISPLAY_DEVICE.nDeviceName(_long.valueOf(arg0)))

    @overload
    def DeviceString(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceString()"""
        return 'ByteBuffer'._wrap(super(DISPLAY_DEVICE, self).DeviceString())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_DISPLAY_DEVICE.mallocStack(_int.valueOf(arg0), arg1))

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
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_DISPLAY_DEVICE.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ncb(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DISPLAY_DEVICE.ncb(long)"""
        return int._wrap(_DISPLAY_DEVICE.ncb(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncb(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.DISPLAY_DEVICE.ncb(long,int)"""
        _DISPLAY_DEVICE.ncb(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def DeviceKeyString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceKeyString()"""
        return str._wrap(super(DISPLAY_DEVICE, self).DeviceKeyString())

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
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.malloc(int)"""
        return Buffer._wrap(_DISPLAY_DEVICE.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.mallocStack(org.lwjgl.system.MemoryStack)"""
        return DISPLAY_DEVICE._wrap(_DISPLAY_DEVICE.mallocStack(arg0))

    @overload
    def DeviceIDString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceIDString()"""
        return str._wrap(super(DISPLAY_DEVICE, self).DeviceIDString())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_DISPLAY_DEVICE.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.calloc(int)"""
        return Buffer._wrap(_DISPLAY_DEVICE.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nDeviceNameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceNameString(long)"""
        return str._wrap(_DISPLAY_DEVICE.nDeviceNameString(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nDeviceKeyString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceKeyString(long)"""
        return str._wrap(_DISPLAY_DEVICE.nDeviceKeyString(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.create(int)"""
        return Buffer._wrap(_DISPLAY_DEVICE.create(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.DISPLAY_DEVICE(java.nio.ByteBuffer)"""
        val = _DISPLAY_DEVICE(arg0)
        self.__wrapper = val

    @overload
    def set(self, arg0: 'DISPLAY_DEVICE') -> 'DISPLAY_DEVICE':
        """public org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.set(org.lwjgl.system.windows.DISPLAY_DEVICE)"""
        return 'DISPLAY_DEVICE'._wrap(super(_DISPLAY_DEVICE, self).set(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.create(long)"""
        return DISPLAY_DEVICE._wrap(_DISPLAY_DEVICE.create(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.DISPLAY_DEVICE.sizeof()"""
        return int._wrap(super(DISPLAY_DEVICE, self).sizeof())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.createSafe(long,int)"""
        return Buffer._wrap(_DISPLAY_DEVICE.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nStateFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DISPLAY_DEVICE.nStateFlags(long)"""
        return int._wrap(_DISPLAY_DEVICE.nStateFlags(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nDeviceString(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceString(long)"""
        return ByteBuffer._wrap(_DISPLAY_DEVICE.nDeviceString(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.mallocStack(int)"""
        return Buffer._wrap(_DISPLAY_DEVICE.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.calloc(org.lwjgl.system.MemoryStack)"""
        return DISPLAY_DEVICE._wrap(_DISPLAY_DEVICE.calloc(arg0))

    @staticmethod
    @overload
    def nDeviceStringString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceStringString(long)"""
        return str._wrap(_DISPLAY_DEVICE.nDeviceStringString(_long.valueOf(arg0)))

    @overload
    def cb(self, arg0: int) -> 'DISPLAY_DEVICE':
        """public org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.cb(int)"""
        return 'DISPLAY_DEVICE'._wrap(super(_DISPLAY_DEVICE, self).cb(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.callocStack()"""
        return DISPLAY_DEVICE._wrap(_DISPLAY_DEVICE.callocStack())

    @staticmethod
    @overload
    def nDeviceID(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceID(long)"""
        return ByteBuffer._wrap(_DISPLAY_DEVICE.nDeviceID(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.createSafe(long)"""
        return DISPLAY_DEVICE._wrap(_DISPLAY_DEVICE.createSafe(_long.valueOf(arg0)))

    @overload
    def DeviceName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceName()"""
        return 'ByteBuffer'._wrap(super(DISPLAY_DEVICE, self).DeviceName())

    @staticmethod
    @overload
    def create() -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.create()"""
        return DISPLAY_DEVICE._wrap(_DISPLAY_DEVICE.create())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_DISPLAY_DEVICE.callocStack(_int.valueOf(arg0), arg1))

    @overload
    def DeviceNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceNameString()"""
        return str._wrap(super(DISPLAY_DEVICE, self).DeviceNameString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nDeviceKey(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceKey(long)"""
        return ByteBuffer._wrap(_DISPLAY_DEVICE.nDeviceKey(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.malloc()"""
        return DISPLAY_DEVICE._wrap(_DISPLAY_DEVICE.malloc())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.callocStack(int)"""
        return Buffer._wrap(_DISPLAY_DEVICE.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.malloc(org.lwjgl.system.MemoryStack)"""
        return DISPLAY_DEVICE._wrap(_DISPLAY_DEVICE.malloc(arg0))

    @staticmethod
    @overload
    def calloc() -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.calloc()"""
        return DISPLAY_DEVICE._wrap(_DISPLAY_DEVICE.calloc())

    @overload
    def DeviceKey(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceKey()"""
        return 'ByteBuffer'._wrap(super(DISPLAY_DEVICE, self).DeviceKey())

    @staticmethod
    @overload
    def mallocStack() -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.mallocStack()"""
        return DISPLAY_DEVICE._wrap(_DISPLAY_DEVICE.mallocStack())

    @overload
    def StateFlags(self) -> int:
        """public int org.lwjgl.system.windows.DISPLAY_DEVICE.StateFlags()"""
        return int._wrap(super(DISPLAY_DEVICE, self).StateFlags())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.create(long,int)"""
        return Buffer._wrap(_DISPLAY_DEVICE.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def DeviceStringString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceStringString()"""
        return str._wrap(super(DISPLAY_DEVICE, self).DeviceStringString())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.callocStack(org.lwjgl.system.MemoryStack)"""
        return DISPLAY_DEVICE._wrap(_DISPLAY_DEVICE.callocStack(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.windows.DEVMODE$Buffer
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
import org.lwjgl.system.windows.POINTL as _POINTL
_POINTL = _POINTL
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
import org.lwjgl.system.windows.DEVMODE as _DEVMODE_Buffer
_Buffer = _DEVMODE_Buffer.Buffer
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.windows.DEVMODE.Buffer"""
 
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
    def dmDefaultSource(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmDefaultSource()"""
        return int._wrap(super(Buffer, self).dmDefaultSource())

    @overload
    def dmPanningWidth(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmPanningWidth()"""
        return int._wrap(super(Buffer, self).dmPanningWidth())

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
    def dmDitherType(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmDitherType()"""
        return int._wrap(super(Buffer, self).dmDitherType())

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def dmPelsWidth(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmPelsWidth()"""
        return int._wrap(super(Buffer, self).dmPelsWidth())

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
    def dmPrintQuality(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmPrintQuality()"""
        return int._wrap(super(Buffer, self).dmPrintQuality())

    @overload
    def dmICMIntent(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmICMIntent()"""
        return int._wrap(super(Buffer, self).dmICMIntent())

    @overload
    def dmDriverExtra(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmDriverExtra()"""
        return int._wrap(super(Buffer, self).dmDriverExtra())

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
        """public org.lwjgl.system.windows.DEVMODE$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def dmDisplayFrequency(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmDisplayFrequency()"""
        return int._wrap(super(Buffer, self).dmDisplayFrequency())

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
    def dmScale(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmScale()"""
        return int._wrap(super(Buffer, self).dmScale())

    @overload
    def dmDuplex(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmDuplex()"""
        return int._wrap(super(Buffer, self).dmDuplex())

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
    def dmBitsPerPel(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmBitsPerPel()"""
        return int._wrap(super(Buffer, self).dmBitsPerPel())

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
    def dmLogPixels(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmLogPixels()"""
        return int._wrap(super(Buffer, self).dmLogPixels())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @overload
    def dmFields(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmFields()"""
        return int._wrap(super(Buffer, self).dmFields())

    @overload
    def dmFormNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DEVMODE$Buffer.dmFormNameString()"""
        return str._wrap(super(Buffer, self).dmFormNameString())

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
    def dmColor(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmColor()"""
        return int._wrap(super(Buffer, self).dmColor())

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
    def dmDisplayFixedOutput(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmDisplayFixedOutput()"""
        return int._wrap(super(Buffer, self).dmDisplayFixedOutput())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.DEVMODE$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def dmSize(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE$Buffer.dmSize(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).dmSize(_short.valueOf(arg0)))

    @overload
    def dmSpecVersion(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmSpecVersion()"""
        return int._wrap(super(Buffer, self).dmSpecVersion())

    @overload
    def dmReserved1(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmReserved1()"""
        return int._wrap(super(Buffer, self).dmReserved1())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dmSize(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmSize()"""
        return int._wrap(super(Buffer, self).dmSize())

    @overload
    def dmMediaType(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmMediaType()"""
        return int._wrap(super(Buffer, self).dmMediaType())

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
    def dmYResolution(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmYResolution()"""
        return int._wrap(super(Buffer, self).dmYResolution())

    @overload
    def dmDriverVersion(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmDriverVersion()"""
        return int._wrap(super(Buffer, self).dmDriverVersion())

    @overload
    def dmNup(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmNup()"""
        return int._wrap(super(Buffer, self).dmNup())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def dmCollate(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmCollate()"""
        return int._wrap(super(Buffer, self).dmCollate())

    @overload
    def dmPanningHeight(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmPanningHeight()"""
        return int._wrap(super(Buffer, self).dmPanningHeight())

    @overload
    def dmDeviceNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DEVMODE$Buffer.dmDeviceNameString()"""
        return str._wrap(super(Buffer, self).dmDeviceNameString())

    @overload
    def dmDriverExtra(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE$Buffer.dmDriverExtra(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).dmDriverExtra(_short.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def dmPaperLength(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmPaperLength()"""
        return int._wrap(super(Buffer, self).dmPaperLength())

    @overload
    def dmCopies(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmCopies()"""
        return int._wrap(super(Buffer, self).dmCopies())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def dmPosition(self) -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.DEVMODE$Buffer.dmPosition()"""
        return 'POINTL'._wrap(super(Buffer, self).dmPosition())

    @overload
    def dmDisplayOrientation(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmDisplayOrientation()"""
        return int._wrap(super(Buffer, self).dmDisplayOrientation())

    @overload
    def dmFormName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE$Buffer.dmFormName()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).dmFormName())

    @overload
    def dmReserved2(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmReserved2()"""
        return int._wrap(super(Buffer, self).dmReserved2())

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
    def dmDisplayFlags(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmDisplayFlags()"""
        return int._wrap(super(Buffer, self).dmDisplayFlags())

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
    def dmPaperSize(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmPaperSize()"""
        return int._wrap(super(Buffer, self).dmPaperSize())

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
    def dmTTOption(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmTTOption()"""
        return int._wrap(super(Buffer, self).dmTTOption())

    @overload
    def dmPaperWidth(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmPaperWidth()"""
        return int._wrap(super(Buffer, self).dmPaperWidth())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @overload
    def dmSpecVersion(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE$Buffer.dmSpecVersion(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).dmSpecVersion(_short.valueOf(arg0)))

    @overload
    def dmICMMethod(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmICMMethod()"""
        return int._wrap(super(Buffer, self).dmICMMethod())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def dmDeviceName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE$Buffer.dmDeviceName()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).dmDeviceName())

    @overload
    def dmOrientation(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmOrientation()"""
        return int._wrap(super(Buffer, self).dmOrientation())

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
    def dmPelsHeight(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmPelsHeight()"""
        return int._wrap(super(Buffer, self).dmPelsHeight())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.WindowsLibrary
import org.lwjgl.system.SharedLibrary as _SharedLibrary_Default
_Default = _SharedLibrary_Default.Default
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.lwjgl.system.FunctionProvider as _FunctionProvider
_FunctionProvider = _FunctionProvider
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.system.windows.WindowsLibrary as _WindowsLibrary
_WindowsLibrary = _WindowsLibrary
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WindowsLibrary():
    """org.lwjgl.system.windows.WindowsLibrary"""
 
    @staticmethod
    def _wrap(java_value: _WindowsLibrary) -> 'WindowsLibrary':
        return WindowsLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowsLibrary):
        """
        Dynamic initializer for WindowsLibrary.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowsLibrary__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowsLibrary__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.windows.WindowsLibrary.free()"""
        super(WindowsLibrary, self).free()

    @overload
    def getFunctionAddress(self, arg0: 'ByteBuffer') -> int:
        """public long org.lwjgl.system.windows.WindowsLibrary.getFunctionAddress(java.nio.ByteBuffer)"""
        return int._wrap(super(_WindowsLibrary, self).getFunctionAddress(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Default.getName()"""
        return str._wrap(super(pyglsystem.SharedLibrary$Default, self).getName())

    @overload
    def __init__(self, arg0: str):
        """public org.lwjgl.system.windows.WindowsLibrary(java.lang.String)"""
        val = _WindowsLibrary(arg0)
        self.__wrapper = val

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

    @override
    @overload
    def getPath(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.WindowsLibrary.getPath()"""
        return str._wrap(super(WindowsLibrary, self).getPath())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public org.lwjgl.system.windows.WindowsLibrary(java.lang.String,long)"""
        val = _WindowsLibrary(arg0, _long.valueOf(arg1))
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
 
 
# CLASS: org.lwjgl.system.windows.RECT$Buffer
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
import org.lwjgl.system.windows.RECT as _RECT_Buffer
_Buffer = _RECT_Buffer.Buffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.windows.RECT.Buffer"""
 
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
    def bottom(self) -> int:
        """public int org.lwjgl.system.windows.RECT$Buffer.bottom()"""
        return int._wrap(super(Buffer, self).bottom())

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

    @overload
    def right(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT$Buffer.right(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).right(_int.valueOf(arg0)))

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
    def right(self) -> int:
        """public int org.lwjgl.system.windows.RECT$Buffer.right()"""
        return int._wrap(super(Buffer, self).right())

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
    def bottom(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT$Buffer.bottom(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).bottom(_int.valueOf(arg0)))

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
    def top(self) -> int:
        """public int org.lwjgl.system.windows.RECT$Buffer.top()"""
        return int._wrap(super(Buffer, self).top())

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
    def top(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT$Buffer.top(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).top(_int.valueOf(arg0)))

    @overload
    def left(self) -> int:
        """public int org.lwjgl.system.windows.RECT$Buffer.left()"""
        return int._wrap(super(Buffer, self).left())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.RECT$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.RECT$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def left(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT$Buffer.left(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).left(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.Crypt32
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.lang.Object as _object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.windows.Crypt32 as _Crypt32
_Crypt32 = _Crypt32
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Crypt32():
    """org.lwjgl.system.windows.Crypt32"""
 
    @staticmethod
    def _wrap(java_value: _Crypt32) -> 'Crypt32':
        return Crypt32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Crypt32):
        """
        Dynamic initializer for Crypt32.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Crypt32__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Crypt32__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nCryptUnprotectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptUnprotectData(long,long,long,long,long,int,long)"""
        return int._wrap(_Crypt32.nCryptUnprotectData(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.windows.Crypt32.getLibrary()"""
        return pyglsystem.SharedLibrary._wrap(_Crypt32.getLibrary())

    @staticmethod
    @overload
    def nCryptProtectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptProtectData(long,long,long,long,long,int,long)"""
        return int._wrap(_Crypt32.nCryptProtectData(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

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
    def CryptUnprotectData(arg0: 'DATA_BLOB', arg1: 'PointerBuffer', arg2: 'DATA_BLOB', arg3: int, arg4: 'CRYPTPROTECT_PROMPTSTRUCT', arg5: int, arg6: 'DATA_BLOB') -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptUnprotectData(org.lwjgl.system.windows.DATA_BLOB,org.lwjgl.PointerBuffer,org.lwjgl.system.windows.DATA_BLOB,long,org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT,int,org.lwjgl.system.windows.DATA_BLOB)"""
        return bool._wrap(_Crypt32.CryptUnprotectData(arg0, arg1, arg2, _long.valueOf(arg3), arg4, _int.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def CryptProtectData(arg0: 'DATA_BLOB', arg1: 'ByteBuffer', arg2: 'DATA_BLOB', arg3: int, arg4: 'CRYPTPROTECT_PROMPTSTRUCT', arg5: int, arg6: 'DATA_BLOB') -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptProtectData(org.lwjgl.system.windows.DATA_BLOB,java.nio.ByteBuffer,org.lwjgl.system.windows.DATA_BLOB,long,org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT,int,org.lwjgl.system.windows.DATA_BLOB)"""
        return bool._wrap(_Crypt32.CryptProtectData(arg0, arg1, arg2, _long.valueOf(arg3), arg4, _int.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def nCryptUnprotectMemory(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptUnprotectMemory(long,int,int)"""
        return int._wrap(_Crypt32.nCryptUnprotectMemory(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def CryptUnprotectMemory(arg0: 'ByteBuffer', arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptUnprotectMemory(java.nio.ByteBuffer,int)"""
        return bool._wrap(_Crypt32.CryptUnprotectMemory(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nCryptProtectMemory(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptProtectMemory(long,int,int)"""
        return int._wrap(_Crypt32.nCryptProtectMemory(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def CryptProtectData(arg0: 'DATA_BLOB', arg1: 'CharSequence', arg2: 'DATA_BLOB', arg3: int, arg4: 'CRYPTPROTECT_PROMPTSTRUCT', arg5: int, arg6: 'DATA_BLOB') -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptProtectData(org.lwjgl.system.windows.DATA_BLOB,java.lang.CharSequence,org.lwjgl.system.windows.DATA_BLOB,long,org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT,int,org.lwjgl.system.windows.DATA_BLOB)"""
        return bool._wrap(_Crypt32.CryptProtectData(arg0, arg1, arg2, _long.valueOf(arg3), arg4, _int.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def nCryptUnprotectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptUnprotectData(long,long,long,long,long,int,long,long)"""
        return int._wrap(_Crypt32.nCryptUnprotectData(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nCryptProtectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptProtectData(long,long,long,long,long,int,long,long)"""
        return int._wrap(_Crypt32.nCryptProtectData(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nCryptProtectMemory(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptProtectMemory(long,int,int,long)"""
        return int._wrap(_Crypt32.nCryptProtectMemory(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def CryptProtectMemory(arg0: 'ByteBuffer', arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptProtectMemory(java.nio.ByteBuffer,int)"""
        return bool._wrap(_Crypt32.CryptProtectMemory(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nCryptUnprotectMemory(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptUnprotectMemory(long,int,int,long)"""
        return int._wrap(_Crypt32.nCryptUnprotectMemory(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.windows.WinBase
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.lwjgl.system.windows.WinBase as _WinBase
_WinBase = _WinBase
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WinBase():
    """org.lwjgl.system.windows.WinBase"""
 
    @staticmethod
    def _wrap(java_value: _WinBase) -> 'WinBase':
        return WinBase(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WinBase):
        """
        Dynamic initializer for WinBase.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WinBase__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WinBase__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nGetModuleHandle(arg0: int) -> int:
        """public static native long org.lwjgl.system.windows.WinBase.nGetModuleHandle(long)"""
        return int._wrap(_WinBase.nGetModuleHandle(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nLoadLibrary(arg0: int) -> int:
        """public static native long org.lwjgl.system.windows.WinBase.nLoadLibrary(long)"""
        return int._wrap(_WinBase.nLoadLibrary(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nLocalFree(arg0: int) -> int:
        """public static native long org.lwjgl.system.windows.WinBase.nLocalFree(long)"""
        return int._wrap(_WinBase.nLocalFree(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def GetProcAddress(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.windows.WinBase.GetProcAddress(long,java.nio.ByteBuffer)"""
        return int._wrap(_WinBase.GetProcAddress(_long.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def LoadLibrary(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.windows.WinBase.LoadLibrary(java.lang.CharSequence)"""
        return int._wrap(_WinBase.LoadLibrary(arg0))

    @staticmethod
    @overload
    def GetLastError() -> int:
        """public static native int org.lwjgl.system.windows.WinBase.GetLastError()"""
        return int._wrap(_WinBase.GetLastError())

    @staticmethod
    @overload
    def nGetModuleFileName(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.WinBase.nGetModuleFileName(long,long,int)"""
        return int._wrap(_WinBase.nGetModuleFileName(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

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
    def GetModuleHandle(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.windows.WinBase.GetModuleHandle(java.nio.ByteBuffer)"""
        return int._wrap(_WinBase.GetModuleHandle(arg0))

    @staticmethod
    @overload
    def nGetProcAddress(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.windows.WinBase.nGetProcAddress(long,long)"""
        return int._wrap(_WinBase.nGetProcAddress(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def getLastError() -> int:
        """public static native int org.lwjgl.system.windows.WinBase.getLastError()"""
        return int._wrap(_WinBase.getLastError())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def LoadLibrary(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.windows.WinBase.LoadLibrary(java.nio.ByteBuffer)"""
        return int._wrap(_WinBase.LoadLibrary(arg0))

    @staticmethod
    @overload
    def GetModuleFileName(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.windows.WinBase.GetModuleFileName(long,java.nio.ByteBuffer)"""
        return int._wrap(_WinBase.GetModuleFileName(_long.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def GetModuleHandle(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.windows.WinBase.GetModuleHandle(java.lang.CharSequence)"""
        return int._wrap(_WinBase.GetModuleHandle(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def GetModuleFileName(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.WinBase.GetModuleFileName(long,int)"""
        return str._wrap(_WinBase.GetModuleFileName(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def LocalFree(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WinBase.LocalFree(long)"""
        return int._wrap(_WinBase.LocalFree(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def GetProcAddress(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.windows.WinBase.GetProcAddress(long,java.lang.CharSequence)"""
        return int._wrap(_WinBase.GetProcAddress(_long.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nFreeLibrary(arg0: int) -> int:
        """public static native int org.lwjgl.system.windows.WinBase.nFreeLibrary(long)"""
        return int._wrap(_WinBase.nFreeLibrary(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def FreeLibrary(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.WinBase.FreeLibrary(long)"""
        return bool._wrap(_WinBase.FreeLibrary(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.windows.TOUCHINPUT
from pyquantum_helper import import_once as _import_once
import org.lwjgl.system.windows.TOUCHINPUT as _TOUCHINPUT
_TOUCHINPUT = _TOUCHINPUT
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
import org.lwjgl.system.windows.TOUCHINPUT as _TOUCHINPUT_Buffer
_Buffer = _TOUCHINPUT_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TOUCHINPUT():
    """org.lwjgl.system.windows.TOUCHINPUT"""
 
    @staticmethod
    def _wrap(java_value: _TOUCHINPUT) -> 'TOUCHINPUT':
        return TOUCHINPUT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TOUCHINPUT):
        """
        Dynamic initializer for TOUCHINPUT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TOUCHINPUT__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TOUCHINPUT__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.mallocStack(int)"""
        return Buffer._wrap(_TOUCHINPUT.mallocStack(_int.valueOf(arg0)))

    @overload
    def y(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.y()"""
        return int._wrap(super(TOUCHINPUT, self).y())

    @staticmethod
    @overload
    def malloc() -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.malloc()"""
        return TOUCHINPUT._wrap(_TOUCHINPUT.malloc())

    @staticmethod
    @overload
    def nhSource(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.TOUCHINPUT.nhSource(long)"""
        return int._wrap(_TOUCHINPUT.nhSource(_long.valueOf(arg0)))

    @overload
    def dwMask(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.dwMask()"""
        return int._wrap(super(TOUCHINPUT, self).dwMask())

    @staticmethod
    @overload
    def ndwTime(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ndwTime(long)"""
        return int._wrap(_TOUCHINPUT.ndwTime(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwMask(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ndwMask(long)"""
        return int._wrap(_TOUCHINPUT.ndwMask(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ncyContact(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ncyContact(long)"""
        return int._wrap(_TOUCHINPUT.ncyContact(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_TOUCHINPUT.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_TOUCHINPUT.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ndwFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ndwFlags(long)"""
        return int._wrap(_TOUCHINPUT.ndwFlags(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create() -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.create()"""
        return TOUCHINPUT._wrap(_TOUCHINPUT.create())

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
    def create(arg0: int) -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.create(long)"""
        return TOUCHINPUT._wrap(_TOUCHINPUT.create(_long.valueOf(arg0)))

    @overload
    def dwTime(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.dwTime()"""
        return int._wrap(super(TOUCHINPUT, self).dwTime())

    @overload
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.TOUCHINPUT.dwExtraInfo()"""
        return int._wrap(super(TOUCHINPUT, self).dwExtraInfo())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def cxContact(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.cxContact()"""
        return int._wrap(super(TOUCHINPUT, self).cxContact())

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
    def x(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.x()"""
        return int._wrap(super(TOUCHINPUT, self).x())

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ny(long)"""
        return int._wrap(_TOUCHINPUT.ny(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.nx(long)"""
        return int._wrap(_TOUCHINPUT.nx(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.create(int)"""
        return Buffer._wrap(_TOUCHINPUT.create(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.TOUCHINPUT(java.nio.ByteBuffer)"""
        val = _TOUCHINPUT(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.sizeof()"""
        return int._wrap(super(TOUCHINPUT, self).sizeof())

    @staticmethod
    @overload
    def mallocStack() -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.mallocStack()"""
        return TOUCHINPUT._wrap(_TOUCHINPUT.mallocStack())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.callocStack(int)"""
        return Buffer._wrap(_TOUCHINPUT.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.createSafe(long)"""
        return TOUCHINPUT._wrap(_TOUCHINPUT.createSafe(_long.valueOf(arg0)))

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.dwFlags()"""
        return int._wrap(super(TOUCHINPUT, self).dwFlags())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return TOUCHINPUT._wrap(_TOUCHINPUT.mallocStack(arg0))

    @staticmethod
    @overload
    def calloc() -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.calloc()"""
        return TOUCHINPUT._wrap(_TOUCHINPUT.calloc())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.callocStack(org.lwjgl.system.MemoryStack)"""
        return TOUCHINPUT._wrap(_TOUCHINPUT.callocStack(arg0))

    @overload
    def hSource(self) -> int:
        """public long org.lwjgl.system.windows.TOUCHINPUT.hSource()"""
        return int._wrap(super(TOUCHINPUT, self).hSource())

    @staticmethod
    @overload
    def callocStack() -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.callocStack()"""
        return TOUCHINPUT._wrap(_TOUCHINPUT.callocStack())

    @staticmethod
    @overload
    def ncxContact(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ncxContact(long)"""
        return int._wrap(_TOUCHINPUT.ncxContact(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwExtraInfo(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.TOUCHINPUT.ndwExtraInfo(long)"""
        return int._wrap(_TOUCHINPUT.ndwExtraInfo(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.calloc(int)"""
        return Buffer._wrap(_TOUCHINPUT.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwID(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ndwID(long)"""
        return int._wrap(_TOUCHINPUT.ndwID(_long.valueOf(arg0)))

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
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.create(long,int)"""
        return Buffer._wrap(_TOUCHINPUT.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_TOUCHINPUT.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_TOUCHINPUT.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.malloc(org.lwjgl.system.MemoryStack)"""
        return TOUCHINPUT._wrap(_TOUCHINPUT.malloc(arg0))

    @overload
    def dwID(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.dwID()"""
        return int._wrap(super(TOUCHINPUT, self).dwID())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.malloc(int)"""
        return Buffer._wrap(_TOUCHINPUT.malloc(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.calloc(org.lwjgl.system.MemoryStack)"""
        return TOUCHINPUT._wrap(_TOUCHINPUT.calloc(arg0))

    @overload
    def cyContact(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.cyContact()"""
        return int._wrap(super(TOUCHINPUT, self).cyContact())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.createSafe(long,int)"""
        return Buffer._wrap(_TOUCHINPUT.createSafe(_long.valueOf(arg0), _int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.WindowProcI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.system.windows.WindowProcI as _WindowProcI
_WindowProcI = _WindowProcI
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class WindowProcI():
    """org.lwjgl.system.windows.WindowProcI"""
 
    @staticmethod
    def _wrap(java_value: _WindowProcI) -> 'WindowProcI':
        return WindowProcI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WindowProcI):
        """
        Dynamic initializer for WindowProcI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WindowProcI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WindowProcI__wrapper":
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
        """public abstract long org.lwjgl.system.windows.WindowProcI.invoke(long,int,long,long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.windows.WindowProcI.callback(long,long)"""
        super(_WindowProcI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.windows.WindowProcI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(WindowProcI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.system.windows.DATA_BLOB
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
import org.lwjgl.system.windows.DATA_BLOB as _DATA_BLOB_Buffer
_Buffer = _DATA_BLOB_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.windows.DATA_BLOB as _DATA_BLOB
_DATA_BLOB = _DATA_BLOB
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DATA_BLOB():
    """org.lwjgl.system.windows.DATA_BLOB"""
 
    @staticmethod
    def _wrap(java_value: _DATA_BLOB) -> 'DATA_BLOB':
        return DATA_BLOB(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DATA_BLOB):
        """
        Dynamic initializer for DATA_BLOB.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DATA_BLOB__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DATA_BLOB__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def cbData(self) -> int:
        """public int org.lwjgl.system.windows.DATA_BLOB.cbData()"""
        return int._wrap(super(DATA_BLOB, self).cbData())

    @staticmethod
    @overload
    def create() -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.create()"""
        return DATA_BLOB._wrap(_DATA_BLOB.create())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.malloc(int)"""
        return Buffer._wrap(_DATA_BLOB.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.create(long,int)"""
        return Buffer._wrap(_DATA_BLOB.create(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_DATA_BLOB.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.malloc(org.lwjgl.system.MemoryStack)"""
        return DATA_BLOB._wrap(_DATA_BLOB.malloc(arg0))

    @staticmethod
    @overload
    def npbData(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.windows.DATA_BLOB.npbData(long,java.nio.ByteBuffer)"""
        _DATA_BLOB.npbData(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def calloc() -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.calloc()"""
        return DATA_BLOB._wrap(_DATA_BLOB.calloc())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_DATA_BLOB.malloc(_int.valueOf(arg0), arg1))

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
        """public int org.lwjgl.system.windows.DATA_BLOB.sizeof()"""
        return int._wrap(super(DATA_BLOB, self).sizeof())

    @staticmethod
    @overload
    def npbData(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DATA_BLOB.npbData(long)"""
        return ByteBuffer._wrap(_DATA_BLOB.npbData(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.DATA_BLOB(java.nio.ByteBuffer)"""
        val = _DATA_BLOB(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.createSafe(long)"""
        return DATA_BLOB._wrap(_DATA_BLOB.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.calloc(int)"""
        return Buffer._wrap(_DATA_BLOB.calloc(_int.valueOf(arg0)))

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
    def calloc(arg0: 'MemoryStack') -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.calloc(org.lwjgl.system.MemoryStack)"""
        return DATA_BLOB._wrap(_DATA_BLOB.calloc(arg0))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.windows.DATA_BLOB.validate(long)"""
        _DATA_BLOB.validate(_long.valueOf(arg0))

    @staticmethod
    @overload
    def ncbData(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DATA_BLOB.ncbData(long)"""
        return int._wrap(_DATA_BLOB.ncbData(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.create(long)"""
        return DATA_BLOB._wrap(_DATA_BLOB.create(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'DATA_BLOB') -> 'DATA_BLOB':
        """public org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.set(org.lwjgl.system.windows.DATA_BLOB)"""
        return 'DATA_BLOB'._wrap(super(_DATA_BLOB, self).set(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.createSafe(long,int)"""
        return Buffer._wrap(_DATA_BLOB.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.create(int)"""
        return Buffer._wrap(_DATA_BLOB.create(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def ncbData(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.DATA_BLOB.ncbData(long,int)"""
        _DATA_BLOB.ncbData(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def pbData(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DATA_BLOB.pbData()"""
        return 'ByteBuffer'._wrap(super(DATA_BLOB, self).pbData())

    @staticmethod
    @overload
    def malloc() -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.malloc()"""
        return DATA_BLOB._wrap(_DATA_BLOB.malloc())

    @overload
    def pbData(self, arg0: 'ByteBuffer') -> 'DATA_BLOB':
        """public org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.pbData(java.nio.ByteBuffer)"""
        return 'DATA_BLOB'._wrap(super(_DATA_BLOB, self).pbData(arg0))

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
 
 
# CLASS: org.lwjgl.system.windows.WNDCLASSEX$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.system.windows.WNDCLASSEX as _WNDCLASSEX_Buffer
_Buffer = _WNDCLASSEX_Buffer.Buffer
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
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.windows.WindowProc as _WindowProc
_WindowProc = _WindowProc
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.windows.WNDCLASSEX.Buffer"""
 
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
    def hIcon(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.hIcon(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).hIcon(_long.valueOf(arg0)))

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
    def lpszClassName(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszClassName(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).lpszClassName(arg0))

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
    def cbSize(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbSize()"""
        return int._wrap(super(Buffer, self).cbSize())

    @overload
    def lpszClassNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszClassNameString()"""
        return str._wrap(super(Buffer, self).lpszClassNameString())

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
    def hbrBackground(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX$Buffer.hbrBackground()"""
        return int._wrap(super(Buffer, self).hbrBackground())

    @overload
    def hCursor(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX$Buffer.hCursor()"""
        return int._wrap(super(Buffer, self).hCursor())

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
    def cbSize(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbSize(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).cbSize(_int.valueOf(arg0)))

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
    def hIcon(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX$Buffer.hIcon()"""
        return int._wrap(super(Buffer, self).hIcon())

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
    def hbrBackground(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.hbrBackground(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).hbrBackground(_long.valueOf(arg0)))

    @overload
    def lpszMenuNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszMenuNameString()"""
        return str._wrap(super(Buffer, self).lpszMenuNameString())

    @overload
    def hIconSm(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.hIconSm(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).hIconSm(_long.valueOf(arg0)))

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
    def hInstance(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX$Buffer.hInstance()"""
        return int._wrap(super(Buffer, self).hInstance())

    @overload
    def cbClsExtra(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbClsExtra()"""
        return int._wrap(super(Buffer, self).cbClsExtra())

    @overload
    def cbWndExtra(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbWndExtra(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).cbWndExtra(_int.valueOf(arg0)))

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
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def lpfnWndProc(self) -> 'WindowProc':
        """public org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpfnWndProc()"""
        return 'WindowProc'._wrap(super(Buffer, self).lpfnWndProc())

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
    def hIconSm(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX$Buffer.hIconSm()"""
        return int._wrap(super(Buffer, self).hIconSm())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def style(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.style(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).style(_int.valueOf(arg0)))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def lpszClassName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszClassName()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).lpszClassName())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def hCursor(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.hCursor(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).hCursor(_long.valueOf(arg0)))

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
    def cbClsExtra(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbClsExtra(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).cbClsExtra(_int.valueOf(arg0)))

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
    def lpszMenuName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszMenuName()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).lpszMenuName())

    @overload
    def style(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX$Buffer.style()"""
        return int._wrap(super(Buffer, self).style())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def lpfnWndProc(self, arg0: 'WindowProcI') -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpfnWndProc(org.lwjgl.system.windows.WindowProcI)"""
        return 'Buffer'._wrap(super(_Buffer, self).lpfnWndProc(arg0))

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
    def hInstance(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.hInstance(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).hInstance(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def cbWndExtra(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbWndExtra()"""
        return int._wrap(super(Buffer, self).cbWndExtra())

    @overload
    def lpszMenuName(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszMenuName(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).lpszMenuName(arg0))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.WINDOWPLACEMENT
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
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.windows.RECT as _RECT
_RECT = _RECT
import org.lwjgl.system.windows.WINDOWPLACEMENT as _WINDOWPLACEMENT
_WINDOWPLACEMENT = _WINDOWPLACEMENT
import org.lwjgl.system.windows.WINDOWPLACEMENT as _WINDOWPLACEMENT_Buffer
_Buffer = _WINDOWPLACEMENT_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
import org.lwjgl.system.windows.POINT as _POINT
_POINT = _POINT
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WINDOWPLACEMENT():
    """org.lwjgl.system.windows.WINDOWPLACEMENT"""
 
    @staticmethod
    def _wrap(java_value: _WINDOWPLACEMENT) -> 'WINDOWPLACEMENT':
        return WINDOWPLACEMENT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WINDOWPLACEMENT):
        """
        Dynamic initializer for WINDOWPLACEMENT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WINDOWPLACEMENT__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WINDOWPLACEMENT__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.calloc(int)"""
        return Buffer._wrap(_WINDOWPLACEMENT.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.calloc(org.lwjgl.system.MemoryStack)"""
        return WINDOWPLACEMENT._wrap(_WINDOWPLACEMENT.calloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.create(int)"""
        return Buffer._wrap(_WINDOWPLACEMENT.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_WINDOWPLACEMENT.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT.sizeof()"""
        return int._wrap(super(WINDOWPLACEMENT, self).sizeof())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.createSafe(long,int)"""
        return Buffer._wrap(_WINDOWPLACEMENT.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nlength(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WINDOWPLACEMENT.nlength(long)"""
        return int._wrap(_WINDOWPLACEMENT.nlength(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_WINDOWPLACEMENT.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.callocStack(org.lwjgl.system.MemoryStack)"""
        return WINDOWPLACEMENT._wrap(_WINDOWPLACEMENT.callocStack(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.callocStack(int)"""
        return Buffer._wrap(_WINDOWPLACEMENT.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nptMinPosition(arg0: int) -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT.nptMinPosition(long)"""
        return POINT._wrap(_WINDOWPLACEMENT.nptMinPosition(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nptMinPosition(arg0: int, arg1: 'POINT'):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nptMinPosition(long,org.lwjgl.system.windows.POINT)"""
        _WINDOWPLACEMENT.nptMinPosition(_long.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def ptMaxPosition(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMaxPosition()"""
        return 'POINT'._wrap(super(WINDOWPLACEMENT, self).ptMaxPosition())

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
    def nptMaxPosition(arg0: int, arg1: 'POINT'):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nptMaxPosition(long,org.lwjgl.system.windows.POINT)"""
        _WINDOWPLACEMENT.nptMaxPosition(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def mallocStack() -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.mallocStack()"""
        return WINDOWPLACEMENT._wrap(_WINDOWPLACEMENT.mallocStack())

    @overload
    def set(self, arg0: 'WINDOWPLACEMENT') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.set(org.lwjgl.system.windows.WINDOWPLACEMENT)"""
        return 'WINDOWPLACEMENT'._wrap(super(_WINDOWPLACEMENT, self).set(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.mallocStack(int)"""
        return Buffer._wrap(_WINDOWPLACEMENT.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.calloc()"""
        return WINDOWPLACEMENT._wrap(_WINDOWPLACEMENT.calloc())

    @staticmethod
    @overload
    def nptMaxPosition(arg0: int) -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT.nptMaxPosition(long)"""
        return POINT._wrap(_WINDOWPLACEMENT.nptMaxPosition(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.create(long)"""
        return WINDOWPLACEMENT._wrap(_WINDOWPLACEMENT.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nflags(long,int)"""
        _WINDOWPLACEMENT.nflags(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'POINT', arg4: 'POINT', arg5: 'RECT') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.set(int,int,int,org.lwjgl.system.windows.POINT,org.lwjgl.system.windows.POINT,org.lwjgl.system.windows.RECT)"""
        return 'WINDOWPLACEMENT'._wrap(super(_WINDOWPLACEMENT, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5))

    @overload
    def showCmd(self, arg0: int) -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.showCmd(int)"""
        return 'WINDOWPLACEMENT'._wrap(super(_WINDOWPLACEMENT, self).showCmd(_int.valueOf(arg0)))

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
    def malloc(arg0: 'MemoryStack') -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.malloc(org.lwjgl.system.MemoryStack)"""
        return WINDOWPLACEMENT._wrap(_WINDOWPLACEMENT.malloc(arg0))

    @overload
    def showCmd(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT.showCmd()"""
        return int._wrap(super(WINDOWPLACEMENT, self).showCmd())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.WINDOWPLACEMENT(java.nio.ByteBuffer)"""
        val = _WINDOWPLACEMENT(arg0)
        self.__wrapper = val

    @overload
    def length(self, arg0: int) -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.length(int)"""
        return 'WINDOWPLACEMENT'._wrap(super(_WINDOWPLACEMENT, self).length(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.callocStack()"""
        return WINDOWPLACEMENT._wrap(_WINDOWPLACEMENT.callocStack())

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WINDOWPLACEMENT.nflags(long)"""
        return int._wrap(_WINDOWPLACEMENT.nflags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.malloc(int)"""
        return Buffer._wrap(_WINDOWPLACEMENT.malloc(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nrcNormalPosition(arg0: int, arg1: 'RECT'):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nrcNormalPosition(long,org.lwjgl.system.windows.RECT)"""
        _WINDOWPLACEMENT.nrcNormalPosition(_long.valueOf(arg0), arg1)

    @overload
    def ptMaxPosition(self, arg0: 'POINT') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMaxPosition(org.lwjgl.system.windows.POINT)"""
        return 'WINDOWPLACEMENT'._wrap(super(_WINDOWPLACEMENT, self).ptMaxPosition(arg0))

    @overload
    def length(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT.length()"""
        return int._wrap(super(WINDOWPLACEMENT, self).length())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def rcNormalPosition(self, arg0: 'RECT') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.rcNormalPosition(org.lwjgl.system.windows.RECT)"""
        return 'WINDOWPLACEMENT'._wrap(super(_WINDOWPLACEMENT, self).rcNormalPosition(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nshowCmd(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WINDOWPLACEMENT.nshowCmd(long)"""
        return int._wrap(_WINDOWPLACEMENT.nshowCmd(_long.valueOf(arg0)))

    @overload
    def flags(self, arg0: int) -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.flags(int)"""
        return 'WINDOWPLACEMENT'._wrap(super(_WINDOWPLACEMENT, self).flags(_int.valueOf(arg0)))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT.flags()"""
        return int._wrap(super(WINDOWPLACEMENT, self).flags())

    @staticmethod
    @overload
    def create() -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.create()"""
        return WINDOWPLACEMENT._wrap(_WINDOWPLACEMENT.create())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return WINDOWPLACEMENT._wrap(_WINDOWPLACEMENT.mallocStack(arg0))

    @staticmethod
    @overload
    def malloc() -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.malloc()"""
        return WINDOWPLACEMENT._wrap(_WINDOWPLACEMENT.malloc())

    @staticmethod
    @overload
    def nrcNormalPosition(arg0: int) -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.WINDOWPLACEMENT.nrcNormalPosition(long)"""
        return RECT._wrap(_WINDOWPLACEMENT.nrcNormalPosition(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_WINDOWPLACEMENT.callocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.create(long,int)"""
        return Buffer._wrap(_WINDOWPLACEMENT.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def ptMinPosition(self, arg0: 'Consumer') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMinPosition(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'WINDOWPLACEMENT'._wrap(super(_WINDOWPLACEMENT, self).ptMinPosition(arg0))

    @staticmethod
    @overload
    def nshowCmd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nshowCmd(long,int)"""
        _WINDOWPLACEMENT.nshowCmd(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def rcNormalPosition(self, arg0: 'Consumer') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.rcNormalPosition(java.util.function.Consumer<org.lwjgl.system.windows.RECT>)"""
        return 'WINDOWPLACEMENT'._wrap(super(_WINDOWPLACEMENT, self).rcNormalPosition(arg0))

    @overload
    def ptMinPosition(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMinPosition()"""
        return 'POINT'._wrap(super(WINDOWPLACEMENT, self).ptMinPosition())

    @overload
    def rcNormalPosition(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.WINDOWPLACEMENT.rcNormalPosition()"""
        return 'RECT'._wrap(super(WINDOWPLACEMENT, self).rcNormalPosition())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.createSafe(long)"""
        return WINDOWPLACEMENT._wrap(_WINDOWPLACEMENT.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_WINDOWPLACEMENT.malloc(_int.valueOf(arg0), arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nlength(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nlength(long,int)"""
        _WINDOWPLACEMENT.nlength(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def ptMinPosition(self, arg0: 'POINT') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMinPosition(org.lwjgl.system.windows.POINT)"""
        return 'WINDOWPLACEMENT'._wrap(super(_WINDOWPLACEMENT, self).ptMinPosition(arg0))

    @overload
    def ptMaxPosition(self, arg0: 'Consumer') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMaxPosition(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'WINDOWPLACEMENT'._wrap(super(_WINDOWPLACEMENT, self).ptMaxPosition(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.windows.RECT
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
import org.lwjgl.system.windows.RECT as _RECT
_RECT = _RECT
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.windows.RECT as _RECT_Buffer
_Buffer = _RECT_Buffer.Buffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RECT():
    """org.lwjgl.system.windows.RECT"""
 
    @staticmethod
    def _wrap(java_value: _RECT) -> 'RECT':
        return RECT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RECT):
        """
        Dynamic initializer for RECT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RECT__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RECT__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'RECT') -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.set(org.lwjgl.system.windows.RECT)"""
        return 'RECT'._wrap(super(_RECT, self).set(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.calloc(int)"""
        return Buffer._wrap(_RECT.calloc(_int.valueOf(arg0)))

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

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def top(self) -> int:
        """public int org.lwjgl.system.windows.RECT.top()"""
        return int._wrap(super(RECT, self).top())

    @staticmethod
    @overload
    def create() -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.create()"""
        return RECT._wrap(_RECT.create())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.callocStack(org.lwjgl.system.MemoryStack)"""
        return RECT._wrap(_RECT.callocStack(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.RECT(java.nio.ByteBuffer)"""
        val = _RECT(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.createSafe(long,int)"""
        return Buffer._wrap(_RECT.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def ntop(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.RECT.ntop(long)"""
        return int._wrap(_RECT.ntop(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.mallocStack()"""
        return RECT._wrap(_RECT.mallocStack())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_RECT.malloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.create(long,int)"""
        return Buffer._wrap(_RECT.create(_long.valueOf(arg0), _int.valueOf(arg1)))

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
    def malloc(arg0: 'MemoryStack') -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.malloc(org.lwjgl.system.MemoryStack)"""
        return RECT._wrap(_RECT.malloc(arg0))

    @staticmethod
    @overload
    def nleft(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.RECT.nleft(long,int)"""
        _RECT.nleft(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return RECT._wrap(_RECT.mallocStack(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nright(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.RECT.nright(long)"""
        return int._wrap(_RECT.nright(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def top(self, arg0: int) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.top(int)"""
        return 'RECT'._wrap(super(_RECT, self).top(_int.valueOf(arg0)))

    @overload
    def left(self, arg0: int) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.left(int)"""
        return 'RECT'._wrap(super(_RECT, self).left(_int.valueOf(arg0)))

    @overload
    def bottom(self) -> int:
        """public int org.lwjgl.system.windows.RECT.bottom()"""
        return int._wrap(super(RECT, self).bottom())

    @staticmethod
    @overload
    def ntop(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.RECT.ntop(long,int)"""
        _RECT.ntop(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def bottom(self, arg0: int) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.bottom(int)"""
        return 'RECT'._wrap(super(_RECT, self).bottom(_int.valueOf(arg0)))

    @overload
    def right(self, arg0: int) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.right(int)"""
        return 'RECT'._wrap(super(_RECT, self).right(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nright(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.RECT.nright(long,int)"""
        _RECT.nright(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.malloc(int)"""
        return Buffer._wrap(_RECT.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.callocStack(int)"""
        return Buffer._wrap(_RECT.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nbottom(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.RECT.nbottom(long,int)"""
        _RECT.nbottom(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def right(self) -> int:
        """public int org.lwjgl.system.windows.RECT.right()"""
        return int._wrap(super(RECT, self).right())

    @staticmethod
    @overload
    def nbottom(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.RECT.nbottom(long)"""
        return int._wrap(_RECT.nbottom(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.createSafe(long)"""
        return RECT._wrap(_RECT.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.malloc()"""
        return RECT._wrap(_RECT.malloc())

    @staticmethod
    @overload
    def create(arg0: int) -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.create(long)"""
        return RECT._wrap(_RECT.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.calloc()"""
        return RECT._wrap(_RECT.calloc())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.RECT.sizeof()"""
        return int._wrap(super(RECT, self).sizeof())

    @staticmethod
    @overload
    def nleft(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.RECT.nleft(long)"""
        return int._wrap(_RECT.nleft(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.calloc(org.lwjgl.system.MemoryStack)"""
        return RECT._wrap(_RECT.calloc(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.mallocStack(int)"""
        return Buffer._wrap(_RECT.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_RECT.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_RECT.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.create(int)"""
        return Buffer._wrap(_RECT.create(_int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def callocStack() -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.callocStack()"""
        return RECT._wrap(_RECT.callocStack())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.set(int,int,int,int)"""
        return 'RECT'._wrap(super(_RECT, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_RECT.calloc(_int.valueOf(arg0), arg1))

    @overload
    def left(self) -> int:
        """public int org.lwjgl.system.windows.RECT.left()"""
        return int._wrap(super(RECT, self).left())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.windows.SECURITY_ATTRIBUTES
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
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.windows.SECURITY_ATTRIBUTES as _SECURITY_ATTRIBUTES
_SECURITY_ATTRIBUTES = _SECURITY_ATTRIBUTES
import org.lwjgl.system.windows.SECURITY_ATTRIBUTES as _SECURITY_ATTRIBUTES_Buffer
_Buffer = _SECURITY_ATTRIBUTES_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SECURITY_ATTRIBUTES():
    """org.lwjgl.system.windows.SECURITY_ATTRIBUTES"""
 
    @staticmethod
    def _wrap(java_value: _SECURITY_ATTRIBUTES) -> 'SECURITY_ATTRIBUTES':
        return SECURITY_ATTRIBUTES(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SECURITY_ATTRIBUTES):
        """
        Dynamic initializer for SECURITY_ATTRIBUTES.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SECURITY_ATTRIBUTES__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SECURITY_ATTRIBUTES__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.create(long,int)"""
        return Buffer._wrap(_SECURITY_ATTRIBUTES.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_SECURITY_ATTRIBUTES.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nbInheritHandle(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nbInheritHandle(long)"""
        return int._wrap(_SECURITY_ATTRIBUTES.nbInheritHandle(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nnLength(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nnLength(long)"""
        return int._wrap(_SECURITY_ATTRIBUTES.nnLength(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.calloc(org.lwjgl.system.MemoryStack)"""
        return SECURITY_ATTRIBUTES._wrap(_SECURITY_ATTRIBUTES.calloc(arg0))

    @overload
    def bInheritHandle(self) -> bool:
        """public boolean org.lwjgl.system.windows.SECURITY_ATTRIBUTES.bInheritHandle()"""
        return bool._wrap(super(SECURITY_ATTRIBUTES, self).bInheritHandle())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.calloc(int)"""
        return Buffer._wrap(_SECURITY_ATTRIBUTES.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.createSafe(long)"""
        return SECURITY_ATTRIBUTES._wrap(_SECURITY_ATTRIBUTES.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.mallocStack(int)"""
        return Buffer._wrap(_SECURITY_ATTRIBUTES.mallocStack(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def nLength(self) -> int:
        """public int org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nLength()"""
        return int._wrap(super(SECURITY_ATTRIBUTES, self).nLength())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.createSafe(long,int)"""
        return Buffer._wrap(_SECURITY_ATTRIBUTES.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def lpSecurityDescriptor(self, arg0: int) -> 'SECURITY_ATTRIBUTES':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.lpSecurityDescriptor(long)"""
        return 'SECURITY_ATTRIBUTES'._wrap(super(_SECURITY_ATTRIBUTES, self).lpSecurityDescriptor(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.create()"""
        return SECURITY_ATTRIBUTES._wrap(_SECURITY_ATTRIBUTES.create())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_SECURITY_ATTRIBUTES.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.create(int)"""
        return Buffer._wrap(_SECURITY_ATTRIBUTES.create(_int.valueOf(arg0)))

    @overload
    def lpSecurityDescriptor(self) -> int:
        """public long org.lwjgl.system.windows.SECURITY_ATTRIBUTES.lpSecurityDescriptor()"""
        return int._wrap(super(SECURITY_ATTRIBUTES, self).lpSecurityDescriptor())

    @staticmethod
    @overload
    def nnLength(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nnLength(long,int)"""
        _SECURITY_ATTRIBUTES.nnLength(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def callocStack() -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.callocStack()"""
        return SECURITY_ATTRIBUTES._wrap(_SECURITY_ATTRIBUTES.callocStack())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES(java.nio.ByteBuffer)"""
        val = _SECURITY_ATTRIBUTES(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.callocStack(int)"""
        return Buffer._wrap(_SECURITY_ATTRIBUTES.callocStack(_int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.mallocStack(org.lwjgl.system.MemoryStack)"""
        return SECURITY_ATTRIBUTES._wrap(_SECURITY_ATTRIBUTES.mallocStack(arg0))

    @staticmethod
    @overload
    def nbInheritHandle(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nbInheritHandle(long,int)"""
        _SECURITY_ATTRIBUTES.nbInheritHandle(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_SECURITY_ATTRIBUTES.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc() -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.malloc()"""
        return SECURITY_ATTRIBUTES._wrap(_SECURITY_ATTRIBUTES.malloc())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.windows.SECURITY_ATTRIBUTES.validate(long)"""
        _SECURITY_ATTRIBUTES.validate(_long.valueOf(arg0))

    @overload
    def set(self, arg0: 'SECURITY_ATTRIBUTES') -> 'SECURITY_ATTRIBUTES':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.set(org.lwjgl.system.windows.SECURITY_ATTRIBUTES)"""
        return 'SECURITY_ATTRIBUTES'._wrap(super(_SECURITY_ATTRIBUTES, self).set(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: bool) -> 'SECURITY_ATTRIBUTES':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.set(int,long,boolean)"""
        return 'SECURITY_ATTRIBUTES'._wrap(super(_SECURITY_ATTRIBUTES, self).set(_int.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.malloc(int)"""
        return Buffer._wrap(_SECURITY_ATTRIBUTES.malloc(_int.valueOf(arg0)))

    @overload
    def bInheritHandle(self, arg0: bool) -> 'SECURITY_ATTRIBUTES':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.bInheritHandle(boolean)"""
        return 'SECURITY_ATTRIBUTES'._wrap(super(_SECURITY_ATTRIBUTES, self).bInheritHandle(_boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_SECURITY_ATTRIBUTES.calloc(_int.valueOf(arg0), arg1))

    @overload
    def nLength(self, arg0: int) -> 'SECURITY_ATTRIBUTES':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nLength(int)"""
        return 'SECURITY_ATTRIBUTES'._wrap(super(_SECURITY_ATTRIBUTES, self).nLength(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nlpSecurityDescriptor(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nlpSecurityDescriptor(long,long)"""
        _SECURITY_ATTRIBUTES.nlpSecurityDescriptor(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nlpSecurityDescriptor(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nlpSecurityDescriptor(long)"""
        return int._wrap(_SECURITY_ATTRIBUTES.nlpSecurityDescriptor(_long.valueOf(arg0)))

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
        """public int org.lwjgl.system.windows.SECURITY_ATTRIBUTES.sizeof()"""
        return int._wrap(super(SECURITY_ATTRIBUTES, self).sizeof())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.malloc(org.lwjgl.system.MemoryStack)"""
        return SECURITY_ATTRIBUTES._wrap(_SECURITY_ATTRIBUTES.malloc(arg0))

    @staticmethod
    @overload
    def mallocStack() -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.mallocStack()"""
        return SECURITY_ATTRIBUTES._wrap(_SECURITY_ATTRIBUTES.mallocStack())

    @staticmethod
    @overload
    def create(arg0: int) -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.create(long)"""
        return SECURITY_ATTRIBUTES._wrap(_SECURITY_ATTRIBUTES.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.callocStack(org.lwjgl.system.MemoryStack)"""
        return SECURITY_ATTRIBUTES._wrap(_SECURITY_ATTRIBUTES.callocStack(arg0))

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

    @staticmethod
    @overload
    def calloc() -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.calloc()"""
        return SECURITY_ATTRIBUTES._wrap(_SECURITY_ATTRIBUTES.calloc()) 
 
 
# CLASS: org.lwjgl.system.windows.User32
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.nio.IntBuffer as IntBuffer
import java.lang.Object as _object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
import org.lwjgl.system.windows.User32 as _User32
_User32 = _User32
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class User32():
    """org.lwjgl.system.windows.User32"""
 
    @staticmethod
    def _wrap(java_value: _User32) -> 'User32':
        return User32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _User32):
        """
        Dynamic initializer for User32.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_User32__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_User32__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def GetWindowRect(arg0: int, arg1: 'RECT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetWindowRect(long,org.lwjgl.system.windows.RECT)"""
        return bool._wrap(_User32.GetWindowRect(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nIsTouchWindow(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nIsTouchWindow(long,long)"""
        return int._wrap(_User32.nIsTouchWindow(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def RegisterTouchWindow(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.RegisterTouchWindow(long,int)"""
        return bool._wrap(_User32.RegisterTouchWindow(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def SetCursorPos(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetCursorPos(int,int)"""
        return bool._wrap(_User32.SetCursorPos(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetTouchInputInfo(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nGetTouchInputInfo(long,int,long,int,long)"""
        return int._wrap(_User32.nGetTouchInputInfo(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def SetWindowLongPtr(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.windows.User32.SetWindowLongPtr(long,int,long)"""
        return int._wrap(_User32.SetWindowLongPtr(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nGetWindowRect(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nGetWindowRect(long,long,long)"""
        return int._wrap(_User32.nGetWindowRect(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def ShowWindow(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.ShowWindow(long,int)"""
        return bool._wrap(_User32.ShowWindow(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def GetMonitorInfo(arg0: int, arg1: 'MONITORINFOEX') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetMonitorInfo(long,org.lwjgl.system.windows.MONITORINFOEX)"""
        return bool._wrap(_User32.GetMonitorInfo(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def GetWindowPlacement(arg0: int, arg1: 'WINDOWPLACEMENT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetWindowPlacement(long,org.lwjgl.system.windows.WINDOWPLACEMENT)"""
        return bool._wrap(_User32.GetWindowPlacement(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nTranslateMessage(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nTranslateMessage(long)"""
        return int._wrap(_User32.nTranslateMessage(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nChangeDisplaySettingsEx(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nChangeDisplaySettingsEx(long,long,long,int,long)"""
        return int._wrap(_User32.nChangeDisplaySettingsEx(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def SetClassLongPtr(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.windows.User32.SetClassLongPtr(long,int,long)"""
        return int._wrap(_User32.SetClassLongPtr(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def GetMessageExtraInfo() -> int:
        """public static long org.lwjgl.system.windows.User32.GetMessageExtraInfo()"""
        return int._wrap(_User32.GetMessageExtraInfo())

    @staticmethod
    @overload
    def nGetWindowRect(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetWindowRect(long,long)"""
        return int._wrap(_User32.nGetWindowRect(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def PostMessage(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.PostMessage(long,int,long,long)"""
        return bool._wrap(_User32.PostMessage(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def nSetWindowPos(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nSetWindowPos(long,long,int,int,int,int,int,long)"""
        return int._wrap(_User32.nSetWindowPos(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def GetDC(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.User32.GetDC(long)"""
        return int._wrap(_User32.GetDC(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def UnregisterClass(arg0: 'CharSequence', arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.UnregisterClass(java.lang.CharSequence,long)"""
        return bool._wrap(_User32.UnregisterClass(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nAdjustWindowRectEx(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nAdjustWindowRectEx(long,int,int,int,long)"""
        return int._wrap(_User32.nAdjustWindowRectEx(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def IsWindowVisible(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsWindowVisible(long)"""
        return bool._wrap(_User32.IsWindowVisible(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def DefWindowProc(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static long org.lwjgl.system.windows.User32.DefWindowProc(long,int,long,long)"""
        return int._wrap(_User32.DefWindowProc(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def AdjustWindowRectEx(arg0: 'RECT', arg1: int, arg2: bool, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.AdjustWindowRectEx(org.lwjgl.system.windows.RECT,int,boolean,int)"""
        return bool._wrap(_User32.AdjustWindowRectEx(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nSetWindowText(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nSetWindowText(long,long)"""
        return int._wrap(_User32.nSetWindowText(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def SetWindowPlacement(arg0: int, arg1: 'WINDOWPLACEMENT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetWindowPlacement(long,org.lwjgl.system.windows.WINDOWPLACEMENT)"""
        return bool._wrap(_User32.SetWindowPlacement(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def LoadIcon(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.windows.User32.LoadIcon(long,java.nio.ByteBuffer)"""
        return int._wrap(_User32.LoadIcon(_long.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nAdjustWindowRectEx(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nAdjustWindowRectEx(long,int,int,int)"""
        return int._wrap(_User32.nAdjustWindowRectEx(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nRegisterClassEx(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.User32.nRegisterClassEx(long)"""
        return int._wrap(_User32.nRegisterClassEx(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nEnumDisplaySettingsEx(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nEnumDisplaySettingsEx(long,int,long,int)"""
        return int._wrap(_User32.nEnumDisplaySettingsEx(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def ShowCursor(arg0: bool) -> int:
        """public static int org.lwjgl.system.windows.User32.ShowCursor(boolean)"""
        return int._wrap(_User32.ShowCursor(_boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def nSetWindowLongPtr(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nSetWindowLongPtr(long,int,long,long)"""
        return int._wrap(_User32.nSetWindowLongPtr(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def nSetWindowPlacement(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nSetWindowPlacement(long,long,long)"""
        return int._wrap(_User32.nSetWindowPlacement(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def SetLayeredWindowAttributes(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetLayeredWindowAttributes(long,int,byte,int)"""
        return bool._wrap(_User32.SetLayeredWindowAttributes(_long.valueOf(arg0), _int.valueOf(arg1), _byte.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def DispatchMessage(arg0: 'MSG') -> int:
        """public static long org.lwjgl.system.windows.User32.DispatchMessage(org.lwjgl.system.windows.MSG)"""
        return int._wrap(_User32.DispatchMessage(arg0))

    @staticmethod
    @overload
    def IsZoomed(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsZoomed(long)"""
        return bool._wrap(_User32.IsZoomed(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def CreateWindowEx(arg0: int, arg1: 'ByteBuffer', arg2: 'ByteBuffer', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static long org.lwjgl.system.windows.User32.CreateWindowEx(int,java.nio.ByteBuffer,java.nio.ByteBuffer,int,int,int,int,int,long,long,long,long)"""
        return int._wrap(_User32.CreateWindowEx(_int.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def SetThreadDpiAwarenessContext(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.User32.SetThreadDpiAwarenessContext(long)"""
        return int._wrap(_User32.SetThreadDpiAwarenessContext(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def GetMessage(arg0: 'MSG', arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetMessage(org.lwjgl.system.windows.MSG,long,int,int)"""
        return bool._wrap(_User32.GetMessage(arg0, _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def SendMessage(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SendMessage(long,int,long,long)"""
        return bool._wrap(_User32.SendMessage(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def GetDpiForWindow(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.GetDpiForWindow(long)"""
        return int._wrap(_User32.GetDpiForWindow(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def DestroyWindow(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.DestroyWindow(long)"""
        return bool._wrap(_User32.DestroyWindow(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nWaitMessage(arg0: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nWaitMessage(long)"""
        return int._wrap(_User32.nWaitMessage(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def GetThreadDpiAwarenessContext() -> int:
        """public static long org.lwjgl.system.windows.User32.GetThreadDpiAwarenessContext()"""
        return int._wrap(_User32.GetThreadDpiAwarenessContext())

    @staticmethod
    @overload
    def nLoadIcon(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nLoadIcon(long,long,long)"""
        return int._wrap(_User32.nLoadIcon(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nClientToScreen(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nClientToScreen(long,long)"""
        return int._wrap(_User32.nClientToScreen(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def GetCursorPos(arg0: 'POINT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetCursorPos(org.lwjgl.system.windows.POINT)"""
        return bool._wrap(_User32.GetCursorPos(arg0))

    @staticmethod
    @overload
    def nCreateWindowEx(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nCreateWindowEx(int,long,long,int,int,int,int,int,long,long,long,long,long)"""
        return int._wrap(_User32.nCreateWindowEx(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11), _long.valueOf(arg12)))

    @staticmethod
    @overload
    def SetWindowText(arg0: int, arg1: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetWindowText(long,java.nio.ByteBuffer)"""
        return bool._wrap(_User32.SetWindowText(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nLoadCursor(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.windows.User32.nLoadCursor(long,long)"""
        return int._wrap(_User32.nLoadCursor(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def UnregisterClass(arg0: 'ByteBuffer', arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.UnregisterClass(java.nio.ByteBuffer,long)"""
        return bool._wrap(_User32.UnregisterClass(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetCursorPos(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetCursorPos(long)"""
        return int._wrap(_User32.nGetCursorPos(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def MonitorFromWindow(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.windows.User32.MonitorFromWindow(long,int)"""
        return int._wrap(_User32.MonitorFromWindow(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def GetAwarenessFromDpiAwarenessContext(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.GetAwarenessFromDpiAwarenessContext(long)"""
        return int._wrap(_User32.GetAwarenessFromDpiAwarenessContext(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nUnregisterTouchWindow(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nUnregisterTouchWindow(long,long)"""
        return int._wrap(_User32.nUnregisterTouchWindow(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nUnregisterClass(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nUnregisterClass(long,long)"""
        return int._wrap(_User32.nUnregisterClass(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetWindowPlacement(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nGetWindowPlacement(long,long,long)"""
        return int._wrap(_User32.nGetWindowPlacement(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nGetTouchInputInfo(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetTouchInputInfo(long,int,long,int)"""
        return int._wrap(_User32.nGetTouchInputInfo(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def IsIconic(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsIconic(long)"""
        return bool._wrap(_User32.IsIconic(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nGetWindowPlacement(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetWindowPlacement(long,long)"""
        return int._wrap(_User32.nGetWindowPlacement(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def CallWindowProc(arg0: 'WindowProcI', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.lwjgl.system.windows.User32.CallWindowProc(org.lwjgl.system.windows.WindowProcI,long,int,long,long)"""
        return int._wrap(_User32.CallWindowProc(arg0, _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nCallWindowProc(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.lwjgl.system.windows.User32.nCallWindowProc(long,long,int,long,long)"""
        return int._wrap(_User32.nCallWindowProc(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def EnumDisplayDevices(arg0: 'ByteBuffer', arg1: int, arg2: 'DISPLAY_DEVICE', arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.EnumDisplayDevices(java.nio.ByteBuffer,int,org.lwjgl.system.windows.DISPLAY_DEVICE,int)"""
        return bool._wrap(_User32.EnumDisplayDevices(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def GetAsyncKeyState(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.User32.GetAsyncKeyState(int)"""
        return int._wrap(_User32.GetAsyncKeyState(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nPeekMessage(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nPeekMessage(long,long,int,int,int)"""
        return int._wrap(_User32.nPeekMessage(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nMoveWindow(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nMoveWindow(long,int,int,int,int,int,long)"""
        return int._wrap(_User32.nMoveWindow(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def GetTouchInputInfo(arg0: int, arg1: 'Buffer', arg2: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetTouchInputInfo(long,org.lwjgl.system.windows.TOUCHINPUT$Buffer,int)"""
        return bool._wrap(_User32.GetTouchInputInfo(_long.valueOf(arg0), arg1, _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nUnregisterClass(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nUnregisterClass(long,long,long)"""
        return int._wrap(_User32.nUnregisterClass(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def nSetLayeredWindowAttributes(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nSetLayeredWindowAttributes(long,int,byte,int,long)"""
        return int._wrap(_User32.nSetLayeredWindowAttributes(_long.valueOf(arg0), _int.valueOf(arg1), _byte.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def ChangeDisplaySettingsEx(arg0: 'ByteBuffer', arg1: 'DEVMODE', arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.windows.User32.ChangeDisplaySettingsEx(java.nio.ByteBuffer,org.lwjgl.system.windows.DEVMODE,long,int,long)"""
        return int._wrap(_User32.ChangeDisplaySettingsEx(arg0, arg1, _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nPostMessage(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nPostMessage(long,int,long,long,long)"""
        return int._wrap(_User32.nPostMessage(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nGetClassLongPtr(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nGetClassLongPtr(long,int,long)"""
        return int._wrap(_User32.nGetClassLongPtr(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def TranslateMessage(arg0: 'MSG') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.TranslateMessage(org.lwjgl.system.windows.MSG)"""
        return bool._wrap(_User32.TranslateMessage(arg0))

    @staticmethod
    @overload
    def UnregisterTouchWindow(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.UnregisterTouchWindow(long)"""
        return bool._wrap(_User32.UnregisterTouchWindow(_long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def MoveWindow(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.MoveWindow(long,int,int,int,int,boolean)"""
        return bool._wrap(_User32.MoveWindow(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5)))

    @staticmethod
    @overload
    def GetSystemMetrics(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.GetSystemMetrics(int)"""
        return int._wrap(_User32.GetSystemMetrics(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nSetWindowPlacement(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nSetWindowPlacement(long,long)"""
        return int._wrap(_User32.nSetWindowPlacement(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def EnumDisplayDevices(arg0: 'CharSequence', arg1: int, arg2: 'DISPLAY_DEVICE', arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.EnumDisplayDevices(java.lang.CharSequence,int,org.lwjgl.system.windows.DISPLAY_DEVICE,int)"""
        return bool._wrap(_User32.EnumDisplayDevices(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def nSendInput(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nSendInput(int,long,int)"""
        return int._wrap(_User32.nSendInput(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def LoadCursor(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.windows.User32.LoadCursor(long,java.nio.ByteBuffer)"""
        return int._wrap(_User32.LoadCursor(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nLoadCursor(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nLoadCursor(long,long,long)"""
        return int._wrap(_User32.nLoadCursor(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def ReleaseDC(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.ReleaseDC(long,long)"""
        return bool._wrap(_User32.ReleaseDC(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nRegisterTouchWindow(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nRegisterTouchWindow(long,int,long)"""
        return int._wrap(_User32.nRegisterTouchWindow(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def ClipCursor(arg0: 'RECT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.ClipCursor(org.lwjgl.system.windows.RECT)"""
        return bool._wrap(_User32.ClipCursor(arg0))

    @staticmethod
    @overload
    def IsValidDpiAwarenessContext(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsValidDpiAwarenessContext(long)"""
        return bool._wrap(_User32.IsValidDpiAwarenessContext(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nGetMessage(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nGetMessage(long,long,int,int,long)"""
        return int._wrap(_User32.nGetMessage(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def UpdateWindow(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.UpdateWindow(long)"""
        return bool._wrap(_User32.UpdateWindow(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def CloseTouchInputHandle(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.CloseTouchInputHandle(long)"""
        return bool._wrap(_User32.CloseTouchInputHandle(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nCloseTouchInputHandle(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nCloseTouchInputHandle(long,long)"""
        return int._wrap(_User32.nCloseTouchInputHandle(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def GetWindowLongPtr(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.windows.User32.GetWindowLongPtr(long,int)"""
        return int._wrap(_User32.GetWindowLongPtr(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def GetClassLongPtr(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.windows.User32.GetClassLongPtr(long,int)"""
        return int._wrap(_User32.GetClassLongPtr(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nSetWindowText(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nSetWindowText(long,long,long)"""
        return int._wrap(_User32.nSetWindowText(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def LoadIcon(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.windows.User32.LoadIcon(long,java.lang.CharSequence)"""
        return int._wrap(_User32.LoadIcon(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def IsTouchWindow(arg0: int, arg1: 'int') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsTouchWindow(long,int[])"""
        return bool._wrap(_User32.IsTouchWindow(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def SetWindowPos(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetWindowPos(long,long,int,int,int,int,int)"""
        return bool._wrap(_User32.SetWindowPos(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6)))

    @staticmethod
    @overload
    def nSendMessage(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nSendMessage(long,int,long,long,long)"""
        return int._wrap(_User32.nSendMessage(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def SetWindowText(arg0: int, arg1: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetWindowText(long,java.lang.CharSequence)"""
        return bool._wrap(_User32.SetWindowText(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def SendInput(arg0: 'Buffer', arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.SendInput(org.lwjgl.system.windows.INPUT$Buffer,int)"""
        return int._wrap(_User32.SendInput(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def SetCursor(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.User32.SetCursor(long)"""
        return int._wrap(_User32.SetCursor(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def CreateWindowEx(arg0: int, arg1: 'CharSequence', arg2: 'CharSequence', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static long org.lwjgl.system.windows.User32.CreateWindowEx(int,java.lang.CharSequence,java.lang.CharSequence,int,int,int,int,int,long,long,long,long)"""
        return int._wrap(_User32.CreateWindowEx(_int.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def nSetClassLongPtr(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nSetClassLongPtr(long,int,long,long)"""
        return int._wrap(_User32.nSetClassLongPtr(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def nCreateWindowEx(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static long org.lwjgl.system.windows.User32.nCreateWindowEx(int,long,long,int,int,int,int,int,long,long,long,long)"""
        return int._wrap(_User32.nCreateWindowEx(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def EnumDisplaySettingsEx(arg0: 'ByteBuffer', arg1: int, arg2: 'DEVMODE', arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.EnumDisplaySettingsEx(java.nio.ByteBuffer,int,org.lwjgl.system.windows.DEVMODE,int)"""
        return bool._wrap(_User32.EnumDisplaySettingsEx(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nGetMonitorInfo(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetMonitorInfo(long,long)"""
        return int._wrap(_User32.nGetMonitorInfo(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def WaitMessage() -> bool:
        """public static boolean org.lwjgl.system.windows.User32.WaitMessage()"""
        return bool._wrap(_User32.WaitMessage())

    @staticmethod
    @overload
    def RegisterClassEx(arg0: 'WNDCLASSEX') -> int:
        """public static short org.lwjgl.system.windows.User32.RegisterClassEx(org.lwjgl.system.windows.WNDCLASSEX)"""
        return int._wrap(_User32.RegisterClassEx(arg0))

    @staticmethod
    @overload
    def nGetMessage(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetMessage(long,long,int,int)"""
        return int._wrap(_User32.nGetMessage(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nClipCursor(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nClipCursor(long)"""
        return int._wrap(_User32.nClipCursor(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def BringWindowToTop(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.BringWindowToTop(long)"""
        return bool._wrap(_User32.BringWindowToTop(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def IsTouchWindow(arg0: int, arg1: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsTouchWindow(long,java.nio.IntBuffer)"""
        return bool._wrap(_User32.IsTouchWindow(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def PeekMessage(arg0: 'MSG', arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.PeekMessage(org.lwjgl.system.windows.MSG,long,int,int,int)"""
        return bool._wrap(_User32.PeekMessage(arg0, _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @staticmethod
    @overload
    def nDestroyWindow(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nDestroyWindow(long,long)"""
        return int._wrap(_User32.nDestroyWindow(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nLoadIcon(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.windows.User32.nLoadIcon(long,long)"""
        return int._wrap(_User32.nLoadIcon(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def LoadCursor(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.windows.User32.LoadCursor(long,java.lang.CharSequence)"""
        return int._wrap(_User32.LoadCursor(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ClientToScreen(arg0: int, arg1: 'POINT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.ClientToScreen(long,org.lwjgl.system.windows.POINT)"""
        return bool._wrap(_User32.ClientToScreen(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nEnumDisplayDevices(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nEnumDisplayDevices(long,int,long,int)"""
        return int._wrap(_User32.nEnumDisplayDevices(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.windows.User32.getLibrary()"""
        return pyglsystem.SharedLibrary._wrap(_User32.getLibrary())

    @staticmethod
    @overload
    def EnumDisplaySettingsEx(arg0: 'CharSequence', arg1: int, arg2: 'DEVMODE', arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.EnumDisplaySettingsEx(java.lang.CharSequence,int,org.lwjgl.system.windows.DEVMODE,int)"""
        return bool._wrap(_User32.EnumDisplaySettingsEx(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def GetDpiForSystem() -> int:
        """public static int org.lwjgl.system.windows.User32.GetDpiForSystem()"""
        return int._wrap(_User32.GetDpiForSystem())

    @staticmethod
    @overload
    def GetWindowDpiAwarenessContext(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.User32.GetWindowDpiAwarenessContext(long)"""
        return int._wrap(_User32.GetWindowDpiAwarenessContext(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nDispatchMessage(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.User32.nDispatchMessage(long)"""
        return int._wrap(_User32.nDispatchMessage(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nRegisterClassEx(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.windows.User32.nRegisterClassEx(long,long)"""
        return int._wrap(_User32.nRegisterClassEx(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetWindowLongPtr(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nGetWindowLongPtr(long,int,long)"""
        return int._wrap(_User32.nGetWindowLongPtr(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def ChangeDisplaySettingsEx(arg0: 'CharSequence', arg1: 'DEVMODE', arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.windows.User32.ChangeDisplaySettingsEx(java.lang.CharSequence,org.lwjgl.system.windows.DEVMODE,long,int,long)"""
        return int._wrap(_User32.ChangeDisplaySettingsEx(arg0, arg1, _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))) 
 
 
# CLASS: org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT
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
import org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT as _CRYPTPROTECT_PROMPTSTRUCT
_CRYPTPROTECT_PROMPTSTRUCT = _CRYPTPROTECT_PROMPTSTRUCT
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CRYPTPROTECT_PROMPTSTRUCT():
    """org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT"""
 
    @staticmethod
    def _wrap(java_value: _CRYPTPROTECT_PROMPTSTRUCT) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        return CRYPTPROTECT_PROMPTSTRUCT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CRYPTPROTECT_PROMPTSTRUCT):
        """
        Dynamic initializer for CRYPTPROTECT_PROMPTSTRUCT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CRYPTPROTECT_PROMPTSTRUCT__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CRYPTPROTECT_PROMPTSTRUCT__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ndwPromptFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.ndwPromptFlags(long)"""
        return int._wrap(_CRYPTPROTECT_PROMPTSTRUCT.ndwPromptFlags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nhwndApp(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.nhwndApp(long)"""
        return int._wrap(_CRYPTPROTECT_PROMPTSTRUCT.nhwndApp(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.calloc(org.lwjgl.system.MemoryStack)"""
        return CRYPTPROTECT_PROMPTSTRUCT._wrap(_CRYPTPROTECT_PROMPTSTRUCT.calloc(arg0))

    @staticmethod
    @overload
    def ncbSize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.ncbSize(long,int)"""
        _CRYPTPROTECT_PROMPTSTRUCT.ncbSize(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def dwPromptFlags(self) -> int:
        """public int org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.dwPromptFlags()"""
        return int._wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).dwPromptFlags())

    @staticmethod
    @overload
    def ndwPromptFlags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.ndwPromptFlags(long,int)"""
        _CRYPTPROTECT_PROMPTSTRUCT.ndwPromptFlags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def szPrompt(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.szPrompt()"""
        return 'ByteBuffer'._wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).szPrompt())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def calloc() -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.calloc()"""
        return CRYPTPROTECT_PROMPTSTRUCT._wrap(_CRYPTPROTECT_PROMPTSTRUCT.calloc())

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
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'ByteBuffer') -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.set(int,int,long,java.nio.ByteBuffer)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'._wrap(super(_CRYPTPROTECT_PROMPTSTRUCT, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.malloc(org.lwjgl.system.MemoryStack)"""
        return CRYPTPROTECT_PROMPTSTRUCT._wrap(_CRYPTPROTECT_PROMPTSTRUCT.malloc(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.sizeof()"""
        return int._wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).sizeof())

    @staticmethod
    @overload
    def nszPrompt(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.nszPrompt(long)"""
        return ByteBuffer._wrap(_CRYPTPROTECT_PROMPTSTRUCT.nszPrompt(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nszPromptString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.nszPromptString(long)"""
        return str._wrap(_CRYPTPROTECT_PROMPTSTRUCT.nszPromptString(_long.valueOf(arg0)))

    @overload
    def hwndApp(self) -> int:
        """public long org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.hwndApp()"""
        return int._wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).hwndApp())

    @overload
    def dwPromptFlags(self, arg0: int) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.dwPromptFlags(int)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'._wrap(super(_CRYPTPROTECT_PROMPTSTRUCT, self).dwPromptFlags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nhwndApp(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.nhwndApp(long,long)"""
        _CRYPTPROTECT_PROMPTSTRUCT.nhwndApp(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def cbSize(self, arg0: int) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.cbSize(int)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'._wrap(super(_CRYPTPROTECT_PROMPTSTRUCT, self).cbSize(_int.valueOf(arg0)))

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

    @overload
    def set(self, arg0: 'CRYPTPROTECT_PROMPTSTRUCT') -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.set(org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'._wrap(super(_CRYPTPROTECT_PROMPTSTRUCT, self).set(arg0))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT(java.nio.ByteBuffer)"""
        val = _CRYPTPROTECT_PROMPTSTRUCT(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def create(arg0: int) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.create(long)"""
        return CRYPTPROTECT_PROMPTSTRUCT._wrap(_CRYPTPROTECT_PROMPTSTRUCT.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nszPrompt(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.nszPrompt(long,java.nio.ByteBuffer)"""
        _CRYPTPROTECT_PROMPTSTRUCT.nszPrompt(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.createSafe(long)"""
        return CRYPTPROTECT_PROMPTSTRUCT._wrap(_CRYPTPROTECT_PROMPTSTRUCT.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def szPrompt(self, arg0: 'ByteBuffer') -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.szPrompt(java.nio.ByteBuffer)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'._wrap(super(_CRYPTPROTECT_PROMPTSTRUCT, self).szPrompt(arg0))

    @staticmethod
    @overload
    def ncbSize(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.ncbSize(long)"""
        return int._wrap(_CRYPTPROTECT_PROMPTSTRUCT.ncbSize(_long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @overload
    def cbSize(self) -> int:
        """public int org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.cbSize()"""
        return int._wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).cbSize())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create() -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.create()"""
        return CRYPTPROTECT_PROMPTSTRUCT._wrap(_CRYPTPROTECT_PROMPTSTRUCT.create())

    @overload
    def cbSize$Default(self) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.cbSize$Default()"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'._wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).cbSize$Default())

    @overload
    def hwndApp(self, arg0: int) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.hwndApp(long)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'._wrap(super(_CRYPTPROTECT_PROMPTSTRUCT, self).hwndApp(_long.valueOf(arg0)))

    @overload
    def szPromptString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.szPromptString()"""
        return str._wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).szPromptString())

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.validate(long)"""
        _CRYPTPROTECT_PROMPTSTRUCT.validate(_long.valueOf(arg0))

    @staticmethod
    @overload
    def malloc() -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.malloc()"""
        return CRYPTPROTECT_PROMPTSTRUCT._wrap(_CRYPTPROTECT_PROMPTSTRUCT.malloc())

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
 
 
# CLASS: org.lwjgl.system.windows.POINT$Buffer
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
import org.lwjgl.system.windows.POINT as _POINT_Buffer
_Buffer = _POINT_Buffer.Buffer
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
    """org.lwjgl.system.windows.POINT.Buffer"""
 
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
        """public org.lwjgl.system.windows.POINT$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.POINT$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def y(self) -> int:
        """public int org.lwjgl.system.windows.POINT$Buffer.y()"""
        return int._wrap(super(Buffer, self).y())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def y(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT$Buffer.y(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).y(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def x(self) -> int:
        """public int org.lwjgl.system.windows.POINT$Buffer.x()"""
        return int._wrap(super(Buffer, self).x())

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
    def x(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT$Buffer.x(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).x(_int.valueOf(arg0)))

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

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer
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
import org.lwjgl.system.windows.SECURITY_ATTRIBUTES as _SECURITY_ATTRIBUTES_Buffer
_Buffer = _SECURITY_ATTRIBUTES_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.windows.SECURITY_ATTRIBUTES.Buffer"""
 
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
    def nLength(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.nLength(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).nLength(_int.valueOf(arg0)))

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
    def nLength(self) -> int:
        """public int org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.nLength()"""
        return int._wrap(super(Buffer, self).nLength())

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
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer(java.nio.ByteBuffer)"""
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
    def bInheritHandle(self) -> bool:
        """public boolean org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.bInheritHandle()"""
        return bool._wrap(super(Buffer, self).bInheritHandle())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer(long,int)"""
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
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def lpSecurityDescriptor(self) -> int:
        """public long org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.lpSecurityDescriptor()"""
        return int._wrap(super(Buffer, self).lpSecurityDescriptor())

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
    def bInheritHandle(self, arg0: bool) -> 'Buffer':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.bInheritHandle(boolean)"""
        return 'Buffer'._wrap(super(_Buffer, self).bInheritHandle(_boolean.valueOf(arg0)))

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
    def lpSecurityDescriptor(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.lpSecurityDescriptor(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).lpSecurityDescriptor(_long.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.system.windows.GDI32
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
import org.lwjgl.system.windows.GDI32 as _GDI32
_GDI32 = _GDI32
import java.lang.Integer as _int
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GDI32():
    """org.lwjgl.system.windows.GDI32"""
 
    @staticmethod
    def _wrap(java_value: _GDI32) -> 'GDI32':
        return GDI32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GDI32):
        """
        Dynamic initializer for GDI32.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GDI32__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GDI32__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def DescribePixelFormat(arg0: int, arg1: int, arg2: 'PIXELFORMATDESCRIPTOR') -> int:
        """public static int org.lwjgl.system.windows.GDI32.DescribePixelFormat(long,int,org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR)"""
        return int._wrap(_GDI32.DescribePixelFormat(_long.valueOf(arg0), _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nDescribePixelFormat(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.GDI32.nDescribePixelFormat(long,int,int,long,long)"""
        return int._wrap(_GDI32.nDescribePixelFormat(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def SwapBuffers(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.GDI32.SwapBuffers(long)"""
        return bool._wrap(_GDI32.SwapBuffers(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nDescribePixelFormat(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.GDI32.nDescribePixelFormat(long,int,int,long)"""
        return int._wrap(_GDI32.nDescribePixelFormat(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def nGetPixelFormat(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.windows.GDI32.nGetPixelFormat(long,long)"""
        return int._wrap(_GDI32.nGetPixelFormat(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def DescribePixelFormat(arg0: int, arg1: int, arg2: int, arg3: 'PIXELFORMATDESCRIPTOR') -> int:
        """public static int org.lwjgl.system.windows.GDI32.DescribePixelFormat(long,int,int,org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR)"""
        return int._wrap(_GDI32.DescribePixelFormat(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3))

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
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.windows.GDI32.getLibrary()"""
        return pyglsystem.SharedLibrary._wrap(_GDI32.getLibrary())

    @staticmethod
    @overload
    def nChoosePixelFormat(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.GDI32.nChoosePixelFormat(long,long,long)"""
        return int._wrap(_GDI32.nChoosePixelFormat(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nSetPixelFormat(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.windows.GDI32.nSetPixelFormat(long,int,long,long)"""
        return int._wrap(_GDI32.nSetPixelFormat(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def nSetPixelFormat(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.windows.GDI32.nSetPixelFormat(long,int,long)"""
        return int._wrap(_GDI32.nSetPixelFormat(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

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
    def GetPixelFormat(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.GDI32.GetPixelFormat(long)"""
        return int._wrap(_GDI32.GetPixelFormat(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def SetPixelFormat(arg0: int, arg1: int, arg2: 'PIXELFORMATDESCRIPTOR') -> bool:
        """public static boolean org.lwjgl.system.windows.GDI32.SetPixelFormat(long,int,org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR)"""
        return bool._wrap(_GDI32.SetPixelFormat(_long.valueOf(arg0), _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nChoosePixelFormat(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.GDI32.nChoosePixelFormat(long,long)"""
        return int._wrap(_GDI32.nChoosePixelFormat(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def ChoosePixelFormat(arg0: int, arg1: 'PIXELFORMATDESCRIPTOR') -> int:
        """public static int org.lwjgl.system.windows.GDI32.ChoosePixelFormat(long,org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR)"""
        return int._wrap(_GDI32.ChoosePixelFormat(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nSwapBuffers(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.windows.GDI32.nSwapBuffers(long,long)"""
        return int._wrap(_GDI32.nSwapBuffers(_long.valueOf(arg0), _long.valueOf(arg1)))

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
 
 
# CLASS: org.lwjgl.system.windows.WNDCLASSEX
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.system.windows.WNDCLASSEX as _WNDCLASSEX
_WNDCLASSEX = _WNDCLASSEX
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
import org.lwjgl.system.windows.WNDCLASSEX as _WNDCLASSEX_Buffer
_Buffer = _WNDCLASSEX_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.windows.WindowProc as _WindowProc
_WindowProc = _WindowProc
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WNDCLASSEX():
    """org.lwjgl.system.windows.WNDCLASSEX"""
 
    @staticmethod
    def _wrap(java_value: _WNDCLASSEX) -> 'WNDCLASSEX':
        return WNDCLASSEX(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WNDCLASSEX):
        """
        Dynamic initializer for WNDCLASSEX.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WNDCLASSEX__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WNDCLASSEX__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nhIconSm(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WNDCLASSEX.nhIconSm(long)"""
        return int._wrap(_WNDCLASSEX.nhIconSm(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: 'WindowProcI', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'ByteBuffer', arg10: 'ByteBuffer', arg11: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.set(int,int,org.lwjgl.system.windows.WindowProcI,int,int,long,long,long,long,java.nio.ByteBuffer,java.nio.ByteBuffer,long)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).set(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), arg9, arg10, _long.valueOf(arg11)))

    @overload
    def lpszClassName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX.lpszClassName()"""
        return 'ByteBuffer'._wrap(super(WNDCLASSEX, self).lpszClassName())

    @staticmethod
    @overload
    def ncbWndExtra(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WNDCLASSEX.ncbWndExtra(long)"""
        return int._wrap(_WNDCLASSEX.ncbWndExtra(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nlpszClassName(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nlpszClassName(long,java.nio.ByteBuffer)"""
        _WNDCLASSEX.nlpszClassName(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.mallocStack(org.lwjgl.system.MemoryStack)"""
        return WNDCLASSEX._wrap(_WNDCLASSEX.mallocStack(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.mallocStack(int)"""
        return Buffer._wrap(_WNDCLASSEX.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.callocStack(org.lwjgl.system.MemoryStack)"""
        return WNDCLASSEX._wrap(_WNDCLASSEX.callocStack(arg0))

    @overload
    def lpfnWndProc(self) -> 'WindowProc':
        """public org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WNDCLASSEX.lpfnWndProc()"""
        return 'WindowProc'._wrap(super(WNDCLASSEX, self).lpfnWndProc())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: 'WNDCLASSEX') -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.set(org.lwjgl.system.windows.WNDCLASSEX)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).set(arg0))

    @staticmethod
    @overload
    def nlpszMenuName(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nlpszMenuName(long,java.nio.ByteBuffer)"""
        _WNDCLASSEX.nlpszMenuName(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.create(int)"""
        return Buffer._wrap(_WNDCLASSEX.create(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def lpfnWndProc(self, arg0: 'WindowProcI') -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.lpfnWndProc(org.lwjgl.system.windows.WindowProcI)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).lpfnWndProc(arg0))

    @staticmethod
    @overload
    def nhInstance(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nhInstance(long,long)"""
        _WNDCLASSEX.nhInstance(_long.valueOf(arg0), _long.valueOf(arg1))

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
    def nhIcon(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WNDCLASSEX.nhIcon(long)"""
        return int._wrap(_WNDCLASSEX.nhIcon(_long.valueOf(arg0)))

    @overload
    def cbClsExtra(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.cbClsExtra(int)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).cbClsExtra(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.calloc(org.lwjgl.system.MemoryStack)"""
        return WNDCLASSEX._wrap(_WNDCLASSEX.calloc(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.createSafe(long,int)"""
        return Buffer._wrap(_WNDCLASSEX.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_WNDCLASSEX.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nlpszClassNameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.WNDCLASSEX.nlpszClassNameString(long)"""
        return str._wrap(_WNDCLASSEX.nlpszClassNameString(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.WNDCLASSEX(java.nio.ByteBuffer)"""
        val = _WNDCLASSEX(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def nlpszMenuName(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX.nlpszMenuName(long)"""
        return ByteBuffer._wrap(_WNDCLASSEX.nlpszMenuName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncbWndExtra(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.ncbWndExtra(long,int)"""
        _WNDCLASSEX.ncbWndExtra(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def nhCursor(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WNDCLASSEX.nhCursor(long)"""
        return int._wrap(_WNDCLASSEX.nhCursor(_long.valueOf(arg0)))

    @overload
    def cbSize(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX.cbSize()"""
        return int._wrap(super(WNDCLASSEX, self).cbSize())

    @overload
    def cbWndExtra(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.cbWndExtra(int)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).cbWndExtra(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def hIcon(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX.hIcon()"""
        return int._wrap(super(WNDCLASSEX, self).hIcon())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def cbWndExtra(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX.cbWndExtra()"""
        return int._wrap(super(WNDCLASSEX, self).cbWndExtra())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.createSafe(long)"""
        return WNDCLASSEX._wrap(_WNDCLASSEX.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.calloc(int)"""
        return Buffer._wrap(_WNDCLASSEX.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_WNDCLASSEX.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nstyle(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WNDCLASSEX.nstyle(long)"""
        return int._wrap(_WNDCLASSEX.nstyle(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_WNDCLASSEX.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create() -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.create()"""
        return WNDCLASSEX._wrap(_WNDCLASSEX.create())

    @staticmethod
    @overload
    def nhbrBackground(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WNDCLASSEX.nhbrBackground(long)"""
        return int._wrap(_WNDCLASSEX.nhbrBackground(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.create(long)"""
        return WNDCLASSEX._wrap(_WNDCLASSEX.create(_long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX.sizeof()"""
        return int._wrap(super(WNDCLASSEX, self).sizeof())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def style(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX.style()"""
        return int._wrap(super(WNDCLASSEX, self).style())

    @staticmethod
    @overload
    def nlpfnWndProc(arg0: int, arg1: 'WindowProcI'):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nlpfnWndProc(long,org.lwjgl.system.windows.WindowProcI)"""
        _WNDCLASSEX.nlpfnWndProc(_long.valueOf(arg0), arg1)

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def hbrBackground(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.hbrBackground(long)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).hbrBackground(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.malloc(int)"""
        return Buffer._wrap(_WNDCLASSEX.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.mallocStack()"""
        return WNDCLASSEX._wrap(_WNDCLASSEX.mallocStack())

    @overload
    def cbSize(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.cbSize(int)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).cbSize(_int.valueOf(arg0)))

    @overload
    def lpszMenuName(self, arg0: 'ByteBuffer') -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.lpszMenuName(java.nio.ByteBuffer)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).lpszMenuName(arg0))

    @overload
    def hCursor(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.hCursor(long)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).hCursor(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.malloc(org.lwjgl.system.MemoryStack)"""
        return WNDCLASSEX._wrap(_WNDCLASSEX.malloc(arg0))

    @overload
    def lpszClassName(self, arg0: 'ByteBuffer') -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.lpszClassName(java.nio.ByteBuffer)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).lpszClassName(arg0))

    @staticmethod
    @overload
    def nstyle(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nstyle(long,int)"""
        _WNDCLASSEX.nstyle(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nhCursor(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nhCursor(long,long)"""
        _WNDCLASSEX.nhCursor(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def ncbClsExtra(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WNDCLASSEX.ncbClsExtra(long)"""
        return int._wrap(_WNDCLASSEX.ncbClsExtra(_long.valueOf(arg0)))

    @overload
    def hIcon(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.hIcon(long)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).hIcon(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.callocStack(int)"""
        return Buffer._wrap(_WNDCLASSEX.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nhIcon(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nhIcon(long,long)"""
        _WNDCLASSEX.nhIcon(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nhIconSm(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nhIconSm(long,long)"""
        _WNDCLASSEX.nhIconSm(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nlpszMenuNameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.WNDCLASSEX.nlpszMenuNameString(long)"""
        return str._wrap(_WNDCLASSEX.nlpszMenuNameString(_long.valueOf(arg0)))

    @overload
    def hCursor(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX.hCursor()"""
        return int._wrap(super(WNDCLASSEX, self).hCursor())

    @overload
    def cbClsExtra(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX.cbClsExtra()"""
        return int._wrap(super(WNDCLASSEX, self).cbClsExtra())

    @staticmethod
    @overload
    def callocStack() -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.callocStack()"""
        return WNDCLASSEX._wrap(_WNDCLASSEX.callocStack())

    @overload
    def lpszClassNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.WNDCLASSEX.lpszClassNameString()"""
        return str._wrap(super(WNDCLASSEX, self).lpszClassNameString())

    @overload
    def hInstance(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.hInstance(long)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).hInstance(_long.valueOf(arg0)))

    @overload
    def style(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.style(int)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).style(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def lpszMenuNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.WNDCLASSEX.lpszMenuNameString()"""
        return str._wrap(super(WNDCLASSEX, self).lpszMenuNameString())

    @overload
    def hInstance(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX.hInstance()"""
        return int._wrap(super(WNDCLASSEX, self).hInstance())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.create(long,int)"""
        return Buffer._wrap(_WNDCLASSEX.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc() -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.calloc()"""
        return WNDCLASSEX._wrap(_WNDCLASSEX.calloc())

    @overload
    def hIconSm(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.hIconSm(long)"""
        return 'WNDCLASSEX'._wrap(super(_WNDCLASSEX, self).hIconSm(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.validate(long)"""
        _WNDCLASSEX.validate(_long.valueOf(arg0))

    @overload
    def hIconSm(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX.hIconSm()"""
        return int._wrap(super(WNDCLASSEX, self).hIconSm())

    @staticmethod
    @overload
    def ncbSize(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WNDCLASSEX.ncbSize(long)"""
        return int._wrap(_WNDCLASSEX.ncbSize(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncbClsExtra(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.ncbClsExtra(long,int)"""
        _WNDCLASSEX.ncbClsExtra(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nhInstance(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WNDCLASSEX.nhInstance(long)"""
        return int._wrap(_WNDCLASSEX.nhInstance(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nhbrBackground(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nhbrBackground(long,long)"""
        _WNDCLASSEX.nhbrBackground(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nlpszClassName(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX.nlpszClassName(long)"""
        return ByteBuffer._wrap(_WNDCLASSEX.nlpszClassName(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_WNDCLASSEX.mallocStack(_int.valueOf(arg0), arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncbSize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.ncbSize(long,int)"""
        _WNDCLASSEX.ncbSize(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def hbrBackground(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX.hbrBackground()"""
        return int._wrap(super(WNDCLASSEX, self).hbrBackground())

    @staticmethod
    @overload
    def nlpfnWndProc(arg0: int) -> 'WindowProc':
        """public static org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WNDCLASSEX.nlpfnWndProc(long)"""
        return WindowProc._wrap(_WNDCLASSEX.nlpfnWndProc(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.malloc()"""
        return WNDCLASSEX._wrap(_WNDCLASSEX.malloc())

    @overload
    def lpszMenuName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX.lpszMenuName()"""
        return 'ByteBuffer'._wrap(super(WNDCLASSEX, self).lpszMenuName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.windows.MSG
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
import java.util.function.Consumer as Consumer
import org.lwjgl.system.windows.MSG as _MSG_Buffer
_Buffer = _MSG_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.windows.MSG as _MSG
_MSG = _MSG
from builtins import bool
import java.lang.Long as _long
import org.lwjgl.system.windows.POINT as _POINT
_POINT = _POINT
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MSG():
    """org.lwjgl.system.windows.MSG"""
 
    @staticmethod
    def _wrap(java_value: _MSG) -> 'MSG':
        return MSG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MSG):
        """
        Dynamic initializer for MSG.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MSG__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MSG__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.callocStack(org.lwjgl.system.MemoryStack)"""
        return MSG._wrap(_MSG.callocStack(arg0))

    @staticmethod
    @overload
    def nhwnd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MSG.nhwnd(long,long)"""
        _MSG.nhwnd(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MSG.calloc(_int.valueOf(arg0), arg1))

    @overload
    def wParam(self) -> int:
        """public long org.lwjgl.system.windows.MSG.wParam()"""
        return int._wrap(super(MSG, self).wParam())

    @staticmethod
    @overload
    def create(arg0: int) -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.create(long)"""
        return MSG._wrap(_MSG.create(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def lParam(self) -> int:
        """public long org.lwjgl.system.windows.MSG.lParam()"""
        return int._wrap(super(MSG, self).lParam())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.malloc(int)"""
        return Buffer._wrap(_MSG.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.create(int)"""
        return Buffer._wrap(_MSG.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nmessage(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MSG.nmessage(long,int)"""
        _MSG.nmessage(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def pt(self, arg0: 'POINT') -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.pt(org.lwjgl.system.windows.POINT)"""
        return 'MSG'._wrap(super(_MSG, self).pt(arg0))

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

    @overload
    def lParam(self, arg0: int) -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.lParam(long)"""
        return 'MSG'._wrap(super(_MSG, self).lParam(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.mallocStack(org.lwjgl.system.MemoryStack)"""
        return MSG._wrap(_MSG.mallocStack(arg0))

    @overload
    def wParam(self, arg0: int) -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.wParam(long)"""
        return 'MSG'._wrap(super(_MSG, self).wParam(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.callocStack()"""
        return MSG._wrap(_MSG.callocStack())

    @staticmethod
    @overload
    def nwParam(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.MSG.nwParam(long)"""
        return int._wrap(_MSG.nwParam(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MSG.malloc(_int.valueOf(arg0), arg1))

    @overload
    def hwnd(self) -> int:
        """public long org.lwjgl.system.windows.MSG.hwnd()"""
        return int._wrap(super(MSG, self).hwnd())

    @overload
    def message(self) -> int:
        """public int org.lwjgl.system.windows.MSG.message()"""
        return int._wrap(super(MSG, self).message())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MSG.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def set(self, arg0: 'MSG') -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.set(org.lwjgl.system.windows.MSG)"""
        return 'MSG'._wrap(super(_MSG, self).set(arg0))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def ntime(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MSG.ntime(long)"""
        return int._wrap(_MSG.ntime(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nlParam(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MSG.nlParam(long,long)"""
        _MSG.nlParam(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.createSafe(long,int)"""
        return Buffer._wrap(_MSG.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.calloc(org.lwjgl.system.MemoryStack)"""
        return MSG._wrap(_MSG.calloc(arg0))

    @overload
    def hwnd(self, arg0: int) -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.hwnd(long)"""
        return 'MSG'._wrap(super(_MSG, self).hwnd(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nmessage(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MSG.nmessage(long)"""
        return int._wrap(_MSG.nmessage(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.callocStack(int)"""
        return Buffer._wrap(_MSG.callocStack(_int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.mallocStack(int)"""
        return Buffer._wrap(_MSG.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nhwnd(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.MSG.nhwnd(long)"""
        return int._wrap(_MSG.nhwnd(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.create(long,int)"""
        return Buffer._wrap(_MSG.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create() -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.create()"""
        return MSG._wrap(_MSG.create())

    @staticmethod
    @overload
    def npt(arg0: int) -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.MSG.npt(long)"""
        return POINT._wrap(_MSG.npt(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def npt(arg0: int, arg1: 'POINT'):
        """public static void org.lwjgl.system.windows.MSG.npt(long,org.lwjgl.system.windows.POINT)"""
        _MSG.npt(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.malloc(org.lwjgl.system.MemoryStack)"""
        return MSG._wrap(_MSG.malloc(arg0))

    @overload
    def pt(self, arg0: 'Consumer') -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.pt(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'MSG'._wrap(super(_MSG, self).pt(arg0))

    @overload
    def pt(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.MSG.pt()"""
        return 'POINT'._wrap(super(MSG, self).pt())

    @staticmethod
    @overload
    def ntime(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MSG.ntime(long,int)"""
        _MSG.ntime(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nlParam(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.MSG.nlParam(long)"""
        return int._wrap(_MSG.nlParam(_long.valueOf(arg0)))

    @overload
    def time(self) -> int:
        """public int org.lwjgl.system.windows.MSG.time()"""
        return int._wrap(super(MSG, self).time())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'POINT') -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.set(long,int,long,long,int,org.lwjgl.system.windows.POINT)"""
        return 'MSG'._wrap(super(_MSG, self).set(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), arg5))

    @overload
    def message(self, arg0: int) -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.message(int)"""
        return 'MSG'._wrap(super(_MSG, self).message(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.calloc(int)"""
        return Buffer._wrap(_MSG.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.mallocStack()"""
        return MSG._wrap(_MSG.mallocStack())

    @staticmethod
    @overload
    def nwParam(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MSG.nwParam(long,long)"""
        _MSG.nwParam(_long.valueOf(arg0), _long.valueOf(arg1))

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
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MSG.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc() -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.malloc()"""
        return MSG._wrap(_MSG.malloc())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.MSG.sizeof()"""
        return int._wrap(super(MSG, self).sizeof())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.MSG(java.nio.ByteBuffer)"""
        val = _MSG(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.createSafe(long)"""
        return MSG._wrap(_MSG.createSafe(_long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @overload
    def time(self, arg0: int) -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.time(int)"""
        return 'MSG'._wrap(super(_MSG, self).time(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.calloc()"""
        return MSG._wrap(_MSG.calloc())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.windows.MOUSEINPUT
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

import org.lwjgl.system.windows.MOUSEINPUT as _MOUSEINPUT
_MOUSEINPUT = _MOUSEINPUT
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.windows.MOUSEINPUT as _MOUSEINPUT_Buffer
_Buffer = _MOUSEINPUT_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MOUSEINPUT():
    """org.lwjgl.system.windows.MOUSEINPUT"""
 
    @staticmethod
    def _wrap(java_value: _MOUSEINPUT) -> 'MOUSEINPUT':
        return MOUSEINPUT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MOUSEINPUT):
        """
        Dynamic initializer for MOUSEINPUT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MOUSEINPUT__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MOUSEINPUT__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ndwFlags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.ndwFlags(long,int)"""
        _MOUSEINPUT.ndwFlags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def dy(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.dy(int)"""
        return 'MOUSEINPUT'._wrap(super(_MOUSEINPUT, self).dy(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.malloc()"""
        return MOUSEINPUT._wrap(_MOUSEINPUT.malloc())

    @staticmethod
    @overload
    def nmouseData(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MOUSEINPUT.nmouseData(long)"""
        return int._wrap(_MOUSEINPUT.nmouseData(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.set(int,int,int,int,int,long)"""
        return 'MOUSEINPUT'._wrap(super(_MOUSEINPUT, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.malloc(org.lwjgl.system.MemoryStack)"""
        return MOUSEINPUT._wrap(_MOUSEINPUT.malloc(arg0))

    @staticmethod
    @overload
    def ndwExtraInfo(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.MOUSEINPUT.ndwExtraInfo(long)"""
        return int._wrap(_MOUSEINPUT.ndwExtraInfo(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.create(long)"""
        return MOUSEINPUT._wrap(_MOUSEINPUT.create(_long.valueOf(arg0)))

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
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MOUSEINPUT.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ntime(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.ntime(long,int)"""
        _MOUSEINPUT.ntime(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.MOUSEINPUT.dwExtraInfo()"""
        return int._wrap(super(MOUSEINPUT, self).dwExtraInfo())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.sizeof()"""
        return int._wrap(super(MOUSEINPUT, self).sizeof())

    @staticmethod
    @overload
    def ntime(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MOUSEINPUT.ntime(long)"""
        return int._wrap(_MOUSEINPUT.ntime(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.createSafe(long,int)"""
        return Buffer._wrap(_MOUSEINPUT.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.callocStack(int)"""
        return Buffer._wrap(_MOUSEINPUT.callocStack(_int.valueOf(arg0)))

    @overload
    def mouseData(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.mouseData(int)"""
        return 'MOUSEINPUT'._wrap(super(_MOUSEINPUT, self).mouseData(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.callocStack(org.lwjgl.system.MemoryStack)"""
        return MOUSEINPUT._wrap(_MOUSEINPUT.callocStack(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MOUSEINPUT.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def ndy(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MOUSEINPUT.ndy(long)"""
        return int._wrap(_MOUSEINPUT.ndy(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.create()"""
        return MOUSEINPUT._wrap(_MOUSEINPUT.create())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.mallocStack(int)"""
        return Buffer._wrap(_MOUSEINPUT.mallocStack(_int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def dx(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.dx(int)"""
        return 'MOUSEINPUT'._wrap(super(_MOUSEINPUT, self).dx(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.calloc(int)"""
        return Buffer._wrap(_MOUSEINPUT.calloc(_int.valueOf(arg0)))

    @overload
    def dwFlags(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.dwFlags(int)"""
        return 'MOUSEINPUT'._wrap(super(_MOUSEINPUT, self).dwFlags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nmouseData(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.nmouseData(long,int)"""
        _MOUSEINPUT.nmouseData(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def callocStack() -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.callocStack()"""
        return MOUSEINPUT._wrap(_MOUSEINPUT.callocStack())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.create(int)"""
        return Buffer._wrap(_MOUSEINPUT.create(_int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def time(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.time(int)"""
        return 'MOUSEINPUT'._wrap(super(_MOUSEINPUT, self).time(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MOUSEINPUT.callocStack(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def mouseData(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.mouseData()"""
        return int._wrap(super(MOUSEINPUT, self).mouseData())

    @staticmethod
    @overload
    def ndy(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.ndy(long,int)"""
        _MOUSEINPUT.ndy(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def ndwFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MOUSEINPUT.ndwFlags(long)"""
        return int._wrap(_MOUSEINPUT.ndwFlags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return MOUSEINPUT._wrap(_MOUSEINPUT.mallocStack(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.create(long,int)"""
        return Buffer._wrap(_MOUSEINPUT.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def ndx(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.ndx(long,int)"""
        _MOUSEINPUT.ndx(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def time(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.time()"""
        return int._wrap(super(MOUSEINPUT, self).time())

    @overload
    def dy(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.dy()"""
        return int._wrap(super(MOUSEINPUT, self).dy())

    @staticmethod
    @overload
    def mallocStack() -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.mallocStack()"""
        return MOUSEINPUT._wrap(_MOUSEINPUT.mallocStack())

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.dwFlags()"""
        return int._wrap(super(MOUSEINPUT, self).dwFlags())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.MOUSEINPUT(java.nio.ByteBuffer)"""
        val = _MOUSEINPUT(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def ndx(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MOUSEINPUT.ndx(long)"""
        return int._wrap(_MOUSEINPUT.ndx(_long.valueOf(arg0)))

    @overload
    def dwExtraInfo(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.dwExtraInfo(long)"""
        return 'MOUSEINPUT'._wrap(super(_MOUSEINPUT, self).dwExtraInfo(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwExtraInfo(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.ndwExtraInfo(long,long)"""
        _MOUSEINPUT.ndwExtraInfo(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.malloc(int)"""
        return Buffer._wrap(_MOUSEINPUT.malloc(_int.valueOf(arg0)))

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
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_MOUSEINPUT.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.calloc(org.lwjgl.system.MemoryStack)"""
        return MOUSEINPUT._wrap(_MOUSEINPUT.calloc(arg0))

    @overload
    def set(self, arg0: 'MOUSEINPUT') -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.set(org.lwjgl.system.windows.MOUSEINPUT)"""
        return 'MOUSEINPUT'._wrap(super(_MOUSEINPUT, self).set(arg0))

    @overload
    def dx(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.dx()"""
        return int._wrap(super(MOUSEINPUT, self).dx())

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
    def calloc() -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.calloc()"""
        return MOUSEINPUT._wrap(_MOUSEINPUT.calloc())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.createSafe(long)"""
        return MOUSEINPUT._wrap(_MOUSEINPUT.createSafe(_long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR as _PIXELFORMATDESCRIPTOR_Buffer
_Buffer = _PIXELFORMATDESCRIPTOR_Buffer.Buffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR as _PIXELFORMATDESCRIPTOR
_PIXELFORMATDESCRIPTOR = _PIXELFORMATDESCRIPTOR
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Integer as _int
import java.lang.Byte as _byte
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PIXELFORMATDESCRIPTOR():
    """org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR"""
 
    @staticmethod
    def _wrap(java_value: _PIXELFORMATDESCRIPTOR) -> 'PIXELFORMATDESCRIPTOR':
        return PIXELFORMATDESCRIPTOR(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PIXELFORMATDESCRIPTOR):
        """
        Dynamic initializer for PIXELFORMATDESCRIPTOR.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PIXELFORMATDESCRIPTOR__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PIXELFORMATDESCRIPTOR__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ndwDamageMask(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwDamageMask(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ndwDamageMask(_long.valueOf(arg0)))

    @overload
    def bReserved(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.bReserved()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).bReserved())

    @overload
    def cGreenBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cGreenBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cGreenBits())

    @staticmethod
    @overload
    def ncAccumAlphaBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumAlphaBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncAccumAlphaBits(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwLayerMask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwLayerMask(long,int)"""
        _PIXELFORMATDESCRIPTOR.ndwLayerMask(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack() -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.mallocStack()"""
        return PIXELFORMATDESCRIPTOR._wrap(_PIXELFORMATDESCRIPTOR.mallocStack())

    @overload
    def cStencilBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cStencilBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cStencilBits(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwLayerMask(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwLayerMask(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ndwLayerMask(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.callocStack(int)"""
        return Buffer._wrap(_PIXELFORMATDESCRIPTOR.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncDepthBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncDepthBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncDepthBits(_long.valueOf(arg0), _byte.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ncAccumBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncAccumBits(_long.valueOf(arg0), _byte.valueOf(arg1))

    @overload
    def cAccumRedBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumRedBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cAccumRedBits())

    @overload
    def cAlphaShift(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAlphaShift(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cAlphaShift(_byte.valueOf(arg0)))

    @overload
    def cAccumBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cAccumBits(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.calloc(org.lwjgl.system.MemoryStack)"""
        return PIXELFORMATDESCRIPTOR._wrap(_PIXELFORMATDESCRIPTOR.calloc(arg0))

    @staticmethod
    @overload
    def nnSize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nnSize(long,short)"""
        _PIXELFORMATDESCRIPTOR.nnSize(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def ncRedShift(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncRedShift(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncRedShift(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def ncGreenShift(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncGreenShift(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncGreenShift(_long.valueOf(arg0)))

    @overload
    def cColorBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cColorBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cColorBits())

    @staticmethod
    @overload
    def ncAccumAlphaBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumAlphaBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncAccumAlphaBits(_long.valueOf(arg0), _byte.valueOf(arg1))

    @overload
    def dwFlags(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwFlags(int)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).dwFlags(_int.valueOf(arg0)))

    @overload
    def cAccumRedBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumRedBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cAccumRedBits(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ncGreenBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncGreenBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncGreenBits(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncAccumBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncAccumBits(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def cRedShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cRedShift()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cRedShift())

    @overload
    def cStencilBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cStencilBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cStencilBits())

    @overload
    def cBlueShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cBlueShift()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cBlueShift())

    @overload
    def cRedShift(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cRedShift(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cRedShift(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.malloc(org.lwjgl.system.MemoryStack)"""
        return PIXELFORMATDESCRIPTOR._wrap(_PIXELFORMATDESCRIPTOR.malloc(arg0))

    @staticmethod
    @overload
    def niPixelType(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.niPixelType(long,byte)"""
        _PIXELFORMATDESCRIPTOR.niPixelType(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def ncAccumBlueBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumBlueBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncAccumBlueBits(_long.valueOf(arg0), _byte.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int, arg19: int, arg20: int, arg21: int, arg22: int, arg23: int, arg24: int, arg25: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.set(short,short,int,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,int,int,int)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).set(_short.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _byte.valueOf(arg3), _byte.valueOf(arg4), _byte.valueOf(arg5), _byte.valueOf(arg6), _byte.valueOf(arg7), _byte.valueOf(arg8), _byte.valueOf(arg9), _byte.valueOf(arg10), _byte.valueOf(arg11), _byte.valueOf(arg12), _byte.valueOf(arg13), _byte.valueOf(arg14), _byte.valueOf(arg15), _byte.valueOf(arg16), _byte.valueOf(arg17), _byte.valueOf(arg18), _byte.valueOf(arg19), _byte.valueOf(arg20), _byte.valueOf(arg21), _byte.valueOf(arg22), _int.valueOf(arg23), _int.valueOf(arg24), _int.valueOf(arg25)))

    @staticmethod
    @overload
    def nnVersion(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nnVersion(long,short)"""
        _PIXELFORMATDESCRIPTOR.nnVersion(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def ncAccumGreenBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumGreenBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncAccumGreenBits(_long.valueOf(arg0)))

    @overload
    def cRedBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cRedBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cRedBits())

    @overload
    def cBlueShift(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cBlueShift(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cBlueShift(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_PIXELFORMATDESCRIPTOR.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.calloc(int)"""
        return Buffer._wrap(_PIXELFORMATDESCRIPTOR.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncAlphaShift(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAlphaShift(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncAlphaShift(_long.valueOf(arg0)))

    @overload
    def iPixelType(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.iPixelType()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).iPixelType())

    @staticmethod
    @overload
    def niLayerType(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.niLayerType(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.niLayerType(_long.valueOf(arg0)))

    @overload
    def cAccumGreenBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumGreenBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cAccumGreenBits(_byte.valueOf(arg0)))

    @overload
    def cBlueBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cBlueBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cBlueBits(_byte.valueOf(arg0)))

    @overload
    def dwVisibleMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwVisibleMask()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).dwVisibleMask())

    @staticmethod
    @overload
    def nnVersion(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nnVersion(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.nnVersion(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncDepthBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncDepthBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncDepthBits(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.create()"""
        return PIXELFORMATDESCRIPTOR._wrap(_PIXELFORMATDESCRIPTOR.create())

    @staticmethod
    @overload
    def ncAlphaShift(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAlphaShift(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncAlphaShift(_long.valueOf(arg0), _byte.valueOf(arg1))

    @overload
    def cGreenBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cGreenBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cGreenBits(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwVisibleMask(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwVisibleMask(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ndwVisibleMask(_long.valueOf(arg0)))

    @overload
    def cAccumBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cAccumBits())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.malloc(int)"""
        return Buffer._wrap(_PIXELFORMATDESCRIPTOR.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_PIXELFORMATDESCRIPTOR.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ncAccumRedBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumRedBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncAccumRedBits(_long.valueOf(arg0)))

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
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.create(long,int)"""
        return Buffer._wrap(_PIXELFORMATDESCRIPTOR.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def iPixelType(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.iPixelType(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).iPixelType(_byte.valueOf(arg0)))

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR(java.nio.ByteBuffer)"""
        val = _PIXELFORMATDESCRIPTOR(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def ncColorBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncColorBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncColorBits(_long.valueOf(arg0), _byte.valueOf(arg1))

    @overload
    def nSize(self) -> int:
        """public short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nSize()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).nSize())

    @overload
    def dwLayerMask(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwLayerMask(int)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).dwLayerMask(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_PIXELFORMATDESCRIPTOR.calloc(_int.valueOf(arg0), arg1))

    @overload
    def nSize(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nSize(short)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).nSize(_short.valueOf(arg0)))

    @overload
    def iLayerType(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.iLayerType()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).iLayerType())

    @overload
    def cDepthBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cDepthBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cDepthBits(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.createSafe(long,int)"""
        return Buffer._wrap(_PIXELFORMATDESCRIPTOR.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def iLayerType(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.iLayerType(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).iLayerType(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ncGreenShift(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncGreenShift(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncGreenShift(_long.valueOf(arg0), _byte.valueOf(arg1))

    @overload
    def cAccumBlueBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumBlueBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cAccumBlueBits(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ncBlueShift(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncBlueShift(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncBlueShift(_long.valueOf(arg0), _byte.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def ncStencilBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncStencilBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncStencilBits(_long.valueOf(arg0), _byte.valueOf(arg1))

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
    def cAccumAlphaBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumAlphaBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cAccumAlphaBits(_byte.valueOf(arg0)))

    @overload
    def dwLayerMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwLayerMask()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).dwLayerMask())

    @staticmethod
    @overload
    def callocStack() -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.callocStack()"""
        return PIXELFORMATDESCRIPTOR._wrap(_PIXELFORMATDESCRIPTOR.callocStack())

    @staticmethod
    @overload
    def ncAccumRedBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumRedBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncAccumRedBits(_long.valueOf(arg0), _byte.valueOf(arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.sizeof()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).sizeof())

    @staticmethod
    @overload
    def niPixelType(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.niPixelType(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.niPixelType(_long.valueOf(arg0)))

    @overload
    def cAccumGreenBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumGreenBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cAccumGreenBits())

    @overload
    def cAccumBlueBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumBlueBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cAccumBlueBits())

    @staticmethod
    @overload
    def ncColorBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncColorBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncColorBits(_long.valueOf(arg0)))

    @overload
    def cGreenShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cGreenShift()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cGreenShift())

    @overload
    def cAuxBuffers(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAuxBuffers()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cAuxBuffers())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_PIXELFORMATDESCRIPTOR.malloc(_int.valueOf(arg0), arg1))

    @overload
    def dwDamageMask(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwDamageMask(int)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).dwDamageMask(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nbReserved(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nbReserved(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.nbReserved(_long.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def ndwFlags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwFlags(long,int)"""
        _PIXELFORMATDESCRIPTOR.ndwFlags(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.create(long)"""
        return PIXELFORMATDESCRIPTOR._wrap(_PIXELFORMATDESCRIPTOR.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.mallocStack(int)"""
        return Buffer._wrap(_PIXELFORMATDESCRIPTOR.mallocStack(_int.valueOf(arg0)))

    @overload
    def bReserved(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.bReserved(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).bReserved(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def nbReserved(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nbReserved(long,byte)"""
        _PIXELFORMATDESCRIPTOR.nbReserved(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def ncAlphaBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAlphaBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncAlphaBits(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.create(int)"""
        return Buffer._wrap(_PIXELFORMATDESCRIPTOR.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.malloc()"""
        return PIXELFORMATDESCRIPTOR._wrap(_PIXELFORMATDESCRIPTOR.malloc())

    @overload
    def nVersion(self) -> int:
        """public short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nVersion()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).nVersion())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def ncAccumBlueBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumBlueBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncAccumBlueBits(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncRedShift(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncRedShift(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncRedShift(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.mallocStack(org.lwjgl.system.MemoryStack)"""
        return PIXELFORMATDESCRIPTOR._wrap(_PIXELFORMATDESCRIPTOR.mallocStack(arg0))

    @overload
    def cAlphaBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAlphaBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cAlphaBits(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ncGreenBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncGreenBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncGreenBits(_long.valueOf(arg0), _byte.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def ncAuxBuffers(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAuxBuffers(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncAuxBuffers(_long.valueOf(arg0), _byte.valueOf(arg1))

    @overload
    def cAccumAlphaBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumAlphaBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cAccumAlphaBits())

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwFlags()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).dwFlags())

    @overload
    def cColorBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cColorBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cColorBits(_byte.valueOf(arg0)))

    @overload
    def cAuxBuffers(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAuxBuffers(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cAuxBuffers(_byte.valueOf(arg0)))

    @overload
    def cDepthBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cDepthBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cDepthBits())

    @overload
    def dwDamageMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwDamageMask()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).dwDamageMask())

    @staticmethod
    @overload
    def ncRedBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncRedBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncRedBits(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncBlueBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncBlueBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncBlueBits(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncAlphaBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAlphaBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncAlphaBits(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwFlags(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ndwFlags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwDamageMask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwDamageMask(long,int)"""
        _PIXELFORMATDESCRIPTOR.ndwDamageMask(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def ncRedBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncRedBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncRedBits(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def calloc() -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.calloc()"""
        return PIXELFORMATDESCRIPTOR._wrap(_PIXELFORMATDESCRIPTOR.calloc())

    @staticmethod
    @overload
    def ncStencilBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncStencilBits(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncStencilBits(_long.valueOf(arg0)))

    @overload
    def cBlueBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cBlueBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cBlueBits())

    @overload
    def cRedBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cRedBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cRedBits(_byte.valueOf(arg0)))

    @overload
    def cAlphaShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAlphaShift()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cAlphaShift())

    @overload
    def dwVisibleMask(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwVisibleMask(int)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).dwVisibleMask(_int.valueOf(arg0)))

    @overload
    def cGreenShift(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cGreenShift(byte)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).cGreenShift(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwVisibleMask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwVisibleMask(long,int)"""
        _PIXELFORMATDESCRIPTOR.ndwVisibleMask(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def cAlphaBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAlphaBits()"""
        return int._wrap(super(PIXELFORMATDESCRIPTOR, self).cAlphaBits())

    @overload
    def set(self, arg0: 'PIXELFORMATDESCRIPTOR') -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.set(org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).set(arg0))

    @overload
    def nVersion(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nVersion(short)"""
        return 'PIXELFORMATDESCRIPTOR'._wrap(super(_PIXELFORMATDESCRIPTOR, self).nVersion(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def ncAccumGreenBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumGreenBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncAccumGreenBits(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def ncAuxBuffers(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAuxBuffers(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncAuxBuffers(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def niLayerType(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.niLayerType(long,byte)"""
        _PIXELFORMATDESCRIPTOR.niLayerType(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def nnSize(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nnSize(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.nnSize(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncBlueShift(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncBlueShift(long)"""
        return int._wrap(_PIXELFORMATDESCRIPTOR.ncBlueShift(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.createSafe(long)"""
        return PIXELFORMATDESCRIPTOR._wrap(_PIXELFORMATDESCRIPTOR.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncBlueBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncBlueBits(long,byte)"""
        _PIXELFORMATDESCRIPTOR.ncBlueBits(_long.valueOf(arg0), _byte.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.callocStack(org.lwjgl.system.MemoryStack)"""
        return PIXELFORMATDESCRIPTOR._wrap(_PIXELFORMATDESCRIPTOR.callocStack(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.HARDWAREINPUT$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.system.windows.HARDWAREINPUT as _HARDWAREINPUT_Buffer
_Buffer = _HARDWAREINPUT_Buffer.Buffer
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
    """org.lwjgl.system.windows.HARDWAREINPUT.Buffer"""
 
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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.HARDWAREINPUT$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.HARDWAREINPUT$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

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
    def wParamL(self) -> int:
        """public short org.lwjgl.system.windows.HARDWAREINPUT$Buffer.wParamL()"""
        return int._wrap(super(Buffer, self).wParamL())

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
    def wParamL(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT$Buffer.wParamL(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).wParamL(_short.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def uMsg(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT$Buffer.uMsg(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).uMsg(_int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def uMsg(self) -> int:
        """public int org.lwjgl.system.windows.HARDWAREINPUT$Buffer.uMsg()"""
        return int._wrap(super(Buffer, self).uMsg())

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
    def wParamH(self) -> int:
        """public short org.lwjgl.system.windows.HARDWAREINPUT$Buffer.wParamH()"""
        return int._wrap(super(Buffer, self).wParamH())

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
    def wParamH(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT$Buffer.wParamH(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).wParamH(_short.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.DATA_BLOB$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.system.windows.DATA_BLOB as _DATA_BLOB_Buffer
_Buffer = _DATA_BLOB_Buffer.Buffer
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
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.windows.DATA_BLOB.Buffer"""
 
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
    def pbData(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB$Buffer.pbData(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).pbData(arg0))

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
        """public org.lwjgl.system.windows.DATA_BLOB$Buffer(java.nio.ByteBuffer)"""
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
    def cbData(self) -> int:
        """public int org.lwjgl.system.windows.DATA_BLOB$Buffer.cbData()"""
        return int._wrap(super(Buffer, self).cbData())

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
    def pbData(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DATA_BLOB$Buffer.pbData()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).pbData())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.DATA_BLOB$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
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
 
 
# CLASS: org.lwjgl.system.windows.MSG$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.util.function.Consumer as Consumer
import org.lwjgl.system.windows.MSG as _MSG_Buffer
_Buffer = _MSG_Buffer.Buffer
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
import org.lwjgl.system.windows.POINT as _POINT
_POINT = _POINT
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.windows.MSG.Buffer"""
 
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
        """public org.lwjgl.system.windows.MSG$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def message(self) -> int:
        """public int org.lwjgl.system.windows.MSG$Buffer.message()"""
        return int._wrap(super(Buffer, self).message())

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
    def wParam(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.wParam(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).wParam(_long.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @overload
    def time(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.time(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).time(_int.valueOf(arg0)))

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
    def lParam(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.lParam(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).lParam(_long.valueOf(arg0)))

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
    def lParam(self) -> int:
        """public long org.lwjgl.system.windows.MSG$Buffer.lParam()"""
        return int._wrap(super(Buffer, self).lParam())

    @overload
    def pt(self, arg0: 'POINT') -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.pt(org.lwjgl.system.windows.POINT)"""
        return 'Buffer'._wrap(super(_Buffer, self).pt(arg0))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.MSG$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def hwnd(self) -> int:
        """public long org.lwjgl.system.windows.MSG$Buffer.hwnd()"""
        return int._wrap(super(Buffer, self).hwnd())

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
    def time(self) -> int:
        """public int org.lwjgl.system.windows.MSG$Buffer.time()"""
        return int._wrap(super(Buffer, self).time())

    @overload
    def pt(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.MSG$Buffer.pt()"""
        return 'POINT'._wrap(super(Buffer, self).pt())

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
    def message(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.message(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).message(_int.valueOf(arg0)))

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def wParam(self) -> int:
        """public long org.lwjgl.system.windows.MSG$Buffer.wParam()"""
        return int._wrap(super(Buffer, self).wParam())

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
    def pt(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.pt(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'Buffer'._wrap(super(_Buffer, self).pt(arg0))

    @overload
    def hwnd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.hwnd(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).hwnd(_long.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.User32$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.windows.User32 as _User32_Functions
_Functions = _User32_Functions.Functions
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.system.windows.User32.Functions"""
 
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
 
 
# CLASS: org.lwjgl.system.windows.KEYBDINPUT
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
import org.lwjgl.system.windows.KEYBDINPUT as _KEYBDINPUT_Buffer
_Buffer = _KEYBDINPUT_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.windows.KEYBDINPUT as _KEYBDINPUT
_KEYBDINPUT = _KEYBDINPUT
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KEYBDINPUT():
    """org.lwjgl.system.windows.KEYBDINPUT"""
 
    @staticmethod
    def _wrap(java_value: _KEYBDINPUT) -> 'KEYBDINPUT':
        return KEYBDINPUT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KEYBDINPUT):
        """
        Dynamic initializer for KEYBDINPUT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KEYBDINPUT__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KEYBDINPUT__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.KEYBDINPUT.dwExtraInfo()"""
        return int._wrap(super(KEYBDINPUT, self).dwExtraInfo())

    @overload
    def time(self) -> int:
        """public int org.lwjgl.system.windows.KEYBDINPUT.time()"""
        return int._wrap(super(KEYBDINPUT, self).time())

    @overload
    def wVk(self, arg0: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.wVk(short)"""
        return 'KEYBDINPUT'._wrap(super(_KEYBDINPUT, self).wVk(_short.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.KEYBDINPUT.sizeof()"""
        return int._wrap(super(KEYBDINPUT, self).sizeof())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_KEYBDINPUT.mallocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.KEYBDINPUT(java.nio.ByteBuffer)"""
        val = _KEYBDINPUT(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def create() -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.create()"""
        return KEYBDINPUT._wrap(_KEYBDINPUT.create())

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
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.mallocStack(int)"""
        return Buffer._wrap(_KEYBDINPUT.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.create(long)"""
        return KEYBDINPUT._wrap(_KEYBDINPUT.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.malloc(int)"""
        return Buffer._wrap(_KEYBDINPUT.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.create(long,int)"""
        return Buffer._wrap(_KEYBDINPUT.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nwScan(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.KEYBDINPUT.nwScan(long,short)"""
        _KEYBDINPUT.nwScan(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def ndwFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.KEYBDINPUT.ndwFlags(long)"""
        return int._wrap(_KEYBDINPUT.ndwFlags(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.malloc()"""
        return KEYBDINPUT._wrap(_KEYBDINPUT.malloc())

    @staticmethod
    @overload
    def callocStack() -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.callocStack()"""
        return KEYBDINPUT._wrap(_KEYBDINPUT.callocStack())

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
    def callocStack(arg0: 'MemoryStack') -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.callocStack(org.lwjgl.system.MemoryStack)"""
        return KEYBDINPUT._wrap(_KEYBDINPUT.callocStack(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.createSafe(long)"""
        return KEYBDINPUT._wrap(_KEYBDINPUT.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_KEYBDINPUT.calloc(_int.valueOf(arg0), arg1))

    @overload
    def dwFlags(self, arg0: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.dwFlags(int)"""
        return 'KEYBDINPUT'._wrap(super(_KEYBDINPUT, self).dwFlags(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwExtraInfo(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.KEYBDINPUT.ndwExtraInfo(long,long)"""
        _KEYBDINPUT.ndwExtraInfo(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_KEYBDINPUT.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc() -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.calloc()"""
        return KEYBDINPUT._wrap(_KEYBDINPUT.calloc())

    @overload
    def wScan(self) -> int:
        """public short org.lwjgl.system.windows.KEYBDINPUT.wScan()"""
        return int._wrap(super(KEYBDINPUT, self).wScan())

    @overload
    def dwExtraInfo(self, arg0: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.dwExtraInfo(long)"""
        return 'KEYBDINPUT'._wrap(super(_KEYBDINPUT, self).dwExtraInfo(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nwVk(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.KEYBDINPUT.nwVk(long)"""
        return int._wrap(_KEYBDINPUT.nwVk(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.callocStack(int)"""
        return Buffer._wrap(_KEYBDINPUT.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.calloc(org.lwjgl.system.MemoryStack)"""
        return KEYBDINPUT._wrap(_KEYBDINPUT.calloc(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def time(self, arg0: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.time(int)"""
        return 'KEYBDINPUT'._wrap(super(_KEYBDINPUT, self).time(_int.valueOf(arg0)))

    @overload
    def wVk(self) -> int:
        """public short org.lwjgl.system.windows.KEYBDINPUT.wVk()"""
        return int._wrap(super(KEYBDINPUT, self).wVk())

    @overload
    def wScan(self, arg0: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.wScan(short)"""
        return 'KEYBDINPUT'._wrap(super(_KEYBDINPUT, self).wScan(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwExtraInfo(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.KEYBDINPUT.ndwExtraInfo(long)"""
        return int._wrap(_KEYBDINPUT.ndwExtraInfo(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.set(short,short,int,int,long)"""
        return 'KEYBDINPUT'._wrap(super(_KEYBDINPUT, self).set(_short.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return KEYBDINPUT._wrap(_KEYBDINPUT.mallocStack(arg0))

    @staticmethod
    @overload
    def nwScan(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.KEYBDINPUT.nwScan(long)"""
        return int._wrap(_KEYBDINPUT.nwScan(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nwVk(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.KEYBDINPUT.nwVk(long,short)"""
        _KEYBDINPUT.nwVk(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.createSafe(long,int)"""
        return Buffer._wrap(_KEYBDINPUT.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def ndwFlags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.KEYBDINPUT.ndwFlags(long,int)"""
        _KEYBDINPUT.ndwFlags(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: 'KEYBDINPUT') -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.set(org.lwjgl.system.windows.KEYBDINPUT)"""
        return 'KEYBDINPUT'._wrap(super(_KEYBDINPUT, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def ntime(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.KEYBDINPUT.ntime(long,int)"""
        _KEYBDINPUT.ntime(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def ntime(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.KEYBDINPUT.ntime(long)"""
        return int._wrap(_KEYBDINPUT.ntime(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.malloc(org.lwjgl.system.MemoryStack)"""
        return KEYBDINPUT._wrap(_KEYBDINPUT.malloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.calloc(int)"""
        return Buffer._wrap(_KEYBDINPUT.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.create(int)"""
        return Buffer._wrap(_KEYBDINPUT.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_KEYBDINPUT.callocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.KEYBDINPUT.dwFlags()"""
        return int._wrap(super(KEYBDINPUT, self).dwFlags())

    @staticmethod
    @overload
    def mallocStack() -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.mallocStack()"""
        return KEYBDINPUT._wrap(_KEYBDINPUT.mallocStack())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.windows.DEVMODE
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.system.windows.DEVMODE as _DEVMODE
_DEVMODE = _DEVMODE
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
import java.lang.Short as _short
import java.lang.Integer as _int
import org.lwjgl.system.windows.POINTL as _POINTL
_POINTL = _POINTL
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import org.lwjgl.system.windows.DEVMODE as _DEVMODE_Buffer
_Buffer = _DEVMODE_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DEVMODE():
    """org.lwjgl.system.windows.DEVMODE"""
 
    @staticmethod
    def _wrap(java_value: _DEVMODE) -> 'DEVMODE':
        return DEVMODE(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DEVMODE):
        """
        Dynamic initializer for DEVMODE.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DEVMODE__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DEVMODE__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def dmCopies(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmCopies()"""
        return int._wrap(super(DEVMODE, self).dmCopies())

    @staticmethod
    @overload
    def ndmYResolution(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmYResolution(long)"""
        return int._wrap(_DEVMODE.ndmYResolution(_long.valueOf(arg0)))

    @overload
    def dmFormName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE.dmFormName()"""
        return 'ByteBuffer'._wrap(super(DEVMODE, self).dmFormName())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def dmReserved1(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmReserved1()"""
        return int._wrap(super(DEVMODE, self).dmReserved1())

    @staticmethod
    @overload
    def ndmPanningWidth(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmPanningWidth(long)"""
        return int._wrap(_DEVMODE.ndmPanningWidth(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmSpecVersion(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmSpecVersion(long)"""
        return int._wrap(_DEVMODE.ndmSpecVersion(_long.valueOf(arg0)))

    @overload
    def dmDriverVersion(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmDriverVersion()"""
        return int._wrap(super(DEVMODE, self).dmDriverVersion())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.callocStack(org.lwjgl.system.MemoryStack)"""
        return DEVMODE._wrap(_DEVMODE.callocStack(arg0))

    @staticmethod
    @overload
    def ndmDisplayOrientation(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmDisplayOrientation(long)"""
        return int._wrap(_DEVMODE.ndmDisplayOrientation(_long.valueOf(arg0)))

    @overload
    def dmReserved2(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmReserved2()"""
        return int._wrap(super(DEVMODE, self).dmReserved2())

    @overload
    def dmFields(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmFields()"""
        return int._wrap(super(DEVMODE, self).dmFields())

    @overload
    def dmFormNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DEVMODE.dmFormNameString()"""
        return str._wrap(super(DEVMODE, self).dmFormNameString())

    @staticmethod
    @overload
    def calloc() -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.calloc()"""
        return DEVMODE._wrap(_DEVMODE.calloc())

    @staticmethod
    @overload
    def ndmSize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.DEVMODE.ndmSize(long,short)"""
        _DEVMODE.ndmSize(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.create(long)"""
        return DEVMODE._wrap(_DEVMODE.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmSpecVersion(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.DEVMODE.ndmSpecVersion(long,short)"""
        _DEVMODE.ndmSpecVersion(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.mallocStack(int)"""
        return Buffer._wrap(_DEVMODE.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmFormName(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE.ndmFormName(long)"""
        return ByteBuffer._wrap(_DEVMODE.ndmFormName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmCopies(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmCopies(long)"""
        return int._wrap(_DEVMODE.ndmCopies(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDriverExtra(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.DEVMODE.ndmDriverExtra(long,short)"""
        _DEVMODE.ndmDriverExtra(_long.valueOf(arg0), _short.valueOf(arg1))

    @overload
    def dmBitsPerPel(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmBitsPerPel()"""
        return int._wrap(super(DEVMODE, self).dmBitsPerPel())

    @staticmethod
    @overload
    def ndmICMMethod(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmICMMethod(long)"""
        return int._wrap(_DEVMODE.ndmICMMethod(_long.valueOf(arg0)))

    @overload
    def dmDisplayFrequency(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmDisplayFrequency()"""
        return int._wrap(super(DEVMODE, self).dmDisplayFrequency())

    @staticmethod
    @overload
    def ndmPaperLength(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmPaperLength(long)"""
        return int._wrap(_DEVMODE.ndmPaperLength(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmICMIntent(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmICMIntent(long)"""
        return int._wrap(_DEVMODE.ndmICMIntent(_long.valueOf(arg0)))

    @overload
    def dmSpecVersion(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmSpecVersion()"""
        return int._wrap(super(DEVMODE, self).dmSpecVersion())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ndmCollate(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmCollate(long)"""
        return int._wrap(_DEVMODE.ndmCollate(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.createSafe(long,int)"""
        return Buffer._wrap(_DEVMODE.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.callocStack(int)"""
        return Buffer._wrap(_DEVMODE.callocStack(_int.valueOf(arg0)))

    @overload
    def dmDitherType(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmDitherType()"""
        return int._wrap(super(DEVMODE, self).dmDitherType())

    @staticmethod
    @overload
    def ndmDefaultSource(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmDefaultSource(long)"""
        return int._wrap(_DEVMODE.ndmDefaultSource(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.calloc(int)"""
        return Buffer._wrap(_DEVMODE.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_DEVMODE.mallocStack(_int.valueOf(arg0), arg1))

    @overload
    def dmPelsWidth(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmPelsWidth()"""
        return int._wrap(super(DEVMODE, self).dmPelsWidth())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.mallocStack(org.lwjgl.system.MemoryStack)"""
        return DEVMODE._wrap(_DEVMODE.mallocStack(arg0))

    @staticmethod
    @overload
    def ndmScale(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmScale(long)"""
        return int._wrap(_DEVMODE.ndmScale(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmPanningHeight(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmPanningHeight(long)"""
        return int._wrap(_DEVMODE.ndmPanningHeight(_long.valueOf(arg0)))

    @overload
    def dmDeviceName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE.dmDeviceName()"""
        return 'ByteBuffer'._wrap(super(DEVMODE, self).dmDeviceName())

    @staticmethod
    @overload
    def ndmNup(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmNup(long)"""
        return int._wrap(_DEVMODE.ndmNup(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.create()"""
        return DEVMODE._wrap(_DEVMODE.create())

    @overload
    def dmSize(self, arg0: int) -> 'DEVMODE':
        """public org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.dmSize(short)"""
        return 'DEVMODE'._wrap(super(_DEVMODE, self).dmSize(_short.valueOf(arg0)))

    @overload
    def dmTTOption(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmTTOption()"""
        return int._wrap(super(DEVMODE, self).dmTTOption())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.malloc(int)"""
        return Buffer._wrap(_DEVMODE.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmLogPixels(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmLogPixels(long)"""
        return int._wrap(_DEVMODE.ndmLogPixels(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_DEVMODE.malloc(_int.valueOf(arg0), arg1))

    @overload
    def dmSize(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmSize()"""
        return int._wrap(super(DEVMODE, self).dmSize())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc() -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.malloc()"""
        return DEVMODE._wrap(_DEVMODE.malloc())

    @overload
    def dmDisplayOrientation(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmDisplayOrientation()"""
        return int._wrap(super(DEVMODE, self).dmDisplayOrientation())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.create(long,int)"""
        return Buffer._wrap(_DEVMODE.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def dmCollate(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmCollate()"""
        return int._wrap(super(DEVMODE, self).dmCollate())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_DEVMODE.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def mallocStack() -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.mallocStack()"""
        return DEVMODE._wrap(_DEVMODE.mallocStack())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDeviceNameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DEVMODE.ndmDeviceNameString(long)"""
        return str._wrap(_DEVMODE.ndmDeviceNameString(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmColor(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmColor(long)"""
        return int._wrap(_DEVMODE.ndmColor(_long.valueOf(arg0)))

    @overload
    def dmNup(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmNup()"""
        return int._wrap(super(DEVMODE, self).dmNup())

    @overload
    def dmDefaultSource(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmDefaultSource()"""
        return int._wrap(super(DEVMODE, self).dmDefaultSource())

    @overload
    def dmPosition(self) -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.DEVMODE.dmPosition()"""
        return 'POINTL'._wrap(super(DEVMODE, self).dmPosition())

    @staticmethod
    @overload
    def callocStack() -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.callocStack()"""
        return DEVMODE._wrap(_DEVMODE.callocStack())

    @staticmethod
    @overload
    def ndmPrintQuality(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmPrintQuality(long)"""
        return int._wrap(_DEVMODE.ndmPrintQuality(_long.valueOf(arg0)))

    @overload
    def dmPaperLength(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmPaperLength()"""
        return int._wrap(super(DEVMODE, self).dmPaperLength())

    @overload
    def dmICMIntent(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmICMIntent()"""
        return int._wrap(super(DEVMODE, self).dmICMIntent())

    @overload
    def dmOrientation(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmOrientation()"""
        return int._wrap(super(DEVMODE, self).dmOrientation())

    @overload
    def dmColor(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmColor()"""
        return int._wrap(super(DEVMODE, self).dmColor())

    @staticmethod
    @overload
    def ndmOrientation(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmOrientation(long)"""
        return int._wrap(_DEVMODE.ndmOrientation(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def dmDisplayFixedOutput(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmDisplayFixedOutput()"""
        return int._wrap(super(DEVMODE, self).dmDisplayFixedOutput())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def ndmFormNameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DEVMODE.ndmFormNameString(long)"""
        return str._wrap(_DEVMODE.ndmFormNameString(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDuplex(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmDuplex(long)"""
        return int._wrap(_DEVMODE.ndmDuplex(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.sizeof()"""
        return int._wrap(super(DEVMODE, self).sizeof())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_DEVMODE.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ndmPaperWidth(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmPaperWidth(long)"""
        return int._wrap(_DEVMODE.ndmPaperWidth(_long.valueOf(arg0)))

    @overload
    def dmPrintQuality(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmPrintQuality()"""
        return int._wrap(super(DEVMODE, self).dmPrintQuality())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.malloc(org.lwjgl.system.MemoryStack)"""
        return DEVMODE._wrap(_DEVMODE.malloc(arg0))

    @overload
    def dmDisplayFlags(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmDisplayFlags()"""
        return int._wrap(super(DEVMODE, self).dmDisplayFlags())

    @overload
    def dmICMMethod(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmICMMethod()"""
        return int._wrap(super(DEVMODE, self).dmICMMethod())

    @overload
    def dmPaperSize(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmPaperSize()"""
        return int._wrap(super(DEVMODE, self).dmPaperSize())

    @staticmethod
    @overload
    def ndmPelsHeight(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmPelsHeight(long)"""
        return int._wrap(_DEVMODE.ndmPelsHeight(_long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def ndmPosition(arg0: int) -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.DEVMODE.ndmPosition(long)"""
        return POINTL._wrap(_DEVMODE.ndmPosition(_long.valueOf(arg0)))

    @overload
    def dmDriverExtra(self, arg0: int) -> 'DEVMODE':
        """public org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.dmDriverExtra(short)"""
        return 'DEVMODE'._wrap(super(_DEVMODE, self).dmDriverExtra(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmTTOption(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmTTOption(long)"""
        return int._wrap(_DEVMODE.ndmTTOption(_long.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def dmMediaType(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmMediaType()"""
        return int._wrap(super(DEVMODE, self).dmMediaType())

    @overload
    def dmPanningWidth(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmPanningWidth()"""
        return int._wrap(super(DEVMODE, self).dmPanningWidth())

    @staticmethod
    @overload
    def ndmDriverExtra(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmDriverExtra(long)"""
        return int._wrap(_DEVMODE.ndmDriverExtra(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDriverVersion(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmDriverVersion(long)"""
        return int._wrap(_DEVMODE.ndmDriverVersion(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmPelsWidth(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmPelsWidth(long)"""
        return int._wrap(_DEVMODE.ndmPelsWidth(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmMediaType(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmMediaType(long)"""
        return int._wrap(_DEVMODE.ndmMediaType(_long.valueOf(arg0)))

    @overload
    def dmPaperWidth(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmPaperWidth()"""
        return int._wrap(super(DEVMODE, self).dmPaperWidth())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def dmSpecVersion(self, arg0: int) -> 'DEVMODE':
        """public org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.dmSpecVersion(short)"""
        return 'DEVMODE'._wrap(super(_DEVMODE, self).dmSpecVersion(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.calloc(org.lwjgl.system.MemoryStack)"""
        return DEVMODE._wrap(_DEVMODE.calloc(arg0))

    @staticmethod
    @overload
    def ndmDisplayFixedOutput(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmDisplayFixedOutput(long)"""
        return int._wrap(_DEVMODE.ndmDisplayFixedOutput(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def dmPanningHeight(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmPanningHeight()"""
        return int._wrap(super(DEVMODE, self).dmPanningHeight())

    @staticmethod
    @overload
    def ndmDitherType(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmDitherType(long)"""
        return int._wrap(_DEVMODE.ndmDitherType(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmBitsPerPel(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmBitsPerPel(long)"""
        return int._wrap(_DEVMODE.ndmBitsPerPel(_long.valueOf(arg0)))

    @overload
    def dmLogPixels(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmLogPixels()"""
        return int._wrap(super(DEVMODE, self).dmLogPixels())

    @staticmethod
    @overload
    def ndmPaperSize(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmPaperSize(long)"""
        return int._wrap(_DEVMODE.ndmPaperSize(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmReserved2(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmReserved2(long)"""
        return int._wrap(_DEVMODE.ndmReserved2(_long.valueOf(arg0)))

    @overload
    def dmDuplex(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmDuplex()"""
        return int._wrap(super(DEVMODE, self).dmDuplex())

    @staticmethod
    @overload
    def ndmSize(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmSize(long)"""
        return int._wrap(_DEVMODE.ndmSize(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.createSafe(long)"""
        return DEVMODE._wrap(_DEVMODE.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmFields(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmFields(long)"""
        return int._wrap(_DEVMODE.ndmFields(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.create(int)"""
        return Buffer._wrap(_DEVMODE.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDeviceName(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE.ndmDeviceName(long)"""
        return ByteBuffer._wrap(_DEVMODE.ndmDeviceName(_long.valueOf(arg0)))

    @overload
    def dmScale(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmScale()"""
        return int._wrap(super(DEVMODE, self).dmScale())

    @overload
    def dmYResolution(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmYResolution()"""
        return int._wrap(super(DEVMODE, self).dmYResolution())

    @overload
    def dmDeviceNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DEVMODE.dmDeviceNameString()"""
        return str._wrap(super(DEVMODE, self).dmDeviceNameString())

    @staticmethod
    @overload
    def ndmDisplayFrequency(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmDisplayFrequency(long)"""
        return int._wrap(_DEVMODE.ndmDisplayFrequency(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmReserved1(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmReserved1(long)"""
        return int._wrap(_DEVMODE.ndmReserved1(_long.valueOf(arg0)))

    @overload
    def dmPelsHeight(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmPelsHeight()"""
        return int._wrap(super(DEVMODE, self).dmPelsHeight())

    @overload
    def dmDriverExtra(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmDriverExtra()"""
        return int._wrap(super(DEVMODE, self).dmDriverExtra())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.DEVMODE(java.nio.ByteBuffer)"""
        val = _DEVMODE(arg0)
        self.__wrapper = val

    @overload
    def set(self, arg0: 'DEVMODE') -> 'DEVMODE':
        """public org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.set(org.lwjgl.system.windows.DEVMODE)"""
        return 'DEVMODE'._wrap(super(_DEVMODE, self).set(arg0))

    @staticmethod
    @overload
    def ndmDisplayFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmDisplayFlags(long)"""
        return int._wrap(_DEVMODE.ndmDisplayFlags(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.windows.LARGE_INTEGER$Buffer
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
import org.lwjgl.system.windows.LARGE_INTEGER as _LARGE_INTEGER_Buffer
_Buffer = _LARGE_INTEGER_Buffer.Buffer
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
    """org.lwjgl.system.windows.LARGE_INTEGER.Buffer"""
 
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
    def QuadPart(self) -> int:
        """public long org.lwjgl.system.windows.LARGE_INTEGER$Buffer.QuadPart()"""
        return int._wrap(super(Buffer, self).QuadPart())

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
    def u_HighPart(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER$Buffer.u_HighPart(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).u_HighPart(_int.valueOf(arg0)))

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
        """public org.lwjgl.system.windows.LARGE_INTEGER$Buffer(java.nio.ByteBuffer)"""
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
    def u_LowPart(self) -> int:
        """public int org.lwjgl.system.windows.LARGE_INTEGER$Buffer.u_LowPart()"""
        return int._wrap(super(Buffer, self).u_LowPart())

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
        """public org.lwjgl.system.windows.LARGE_INTEGER$Buffer(long,int)"""
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
    def u_LowPart(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER$Buffer.u_LowPart(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).u_LowPart(_int.valueOf(arg0)))

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
    def u_HighPart(self) -> int:
        """public int org.lwjgl.system.windows.LARGE_INTEGER$Buffer.u_HighPart()"""
        return int._wrap(super(Buffer, self).u_HighPart())

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
    def QuadPart(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER$Buffer.QuadPart(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).QuadPart(_long.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.INPUT$Buffer
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
import org.lwjgl.system.windows.INPUT as _INPUT_Buffer
_Buffer = _INPUT_Buffer.Buffer
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

import org.lwjgl.system.windows.MOUSEINPUT as _MOUSEINPUT
_MOUSEINPUT = _MOUSEINPUT
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import org.lwjgl.system.windows.HARDWAREINPUT as _HARDWAREINPUT
_HARDWAREINPUT = _HARDWAREINPUT
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.windows.KEYBDINPUT as _KEYBDINPUT
_KEYBDINPUT = _KEYBDINPUT
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.windows.INPUT.Buffer"""
 
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
    def DUMMYUNIONNAME_hi(self, arg0: 'HARDWAREINPUT') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_hi(org.lwjgl.system.windows.HARDWAREINPUT)"""
        return 'Buffer'._wrap(super(_Buffer, self).DUMMYUNIONNAME_hi(arg0))

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
    def type(self) -> int:
        """public int org.lwjgl.system.windows.INPUT$Buffer.type()"""
        return int._wrap(super(Buffer, self).type())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.INPUT$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
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
    def DUMMYUNIONNAME_mi(self, arg0: 'MOUSEINPUT') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_mi(org.lwjgl.system.windows.MOUSEINPUT)"""
        return 'Buffer'._wrap(super(_Buffer, self).DUMMYUNIONNAME_mi(arg0))

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
    def DUMMYUNIONNAME_mi(self) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_mi()"""
        return 'MOUSEINPUT'._wrap(super(Buffer, self).DUMMYUNIONNAME_mi())

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
    def DUMMYUNIONNAME_ki(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_ki(java.util.function.Consumer<org.lwjgl.system.windows.KEYBDINPUT>)"""
        return 'Buffer'._wrap(super(_Buffer, self).DUMMYUNIONNAME_ki(arg0))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def DUMMYUNIONNAME_ki(self, arg0: 'KEYBDINPUT') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_ki(org.lwjgl.system.windows.KEYBDINPUT)"""
        return 'Buffer'._wrap(super(_Buffer, self).DUMMYUNIONNAME_ki(arg0))

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
        """public org.lwjgl.system.windows.INPUT$Buffer(java.nio.ByteBuffer)"""
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
    def DUMMYUNIONNAME_ki(self) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_ki()"""
        return 'KEYBDINPUT'._wrap(super(Buffer, self).DUMMYUNIONNAME_ki())

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
    def DUMMYUNIONNAME_mi(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_mi(java.util.function.Consumer<org.lwjgl.system.windows.MOUSEINPUT>)"""
        return 'Buffer'._wrap(super(_Buffer, self).DUMMYUNIONNAME_mi(arg0))

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
    def DUMMYUNIONNAME_hi(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_hi(java.util.function.Consumer<org.lwjgl.system.windows.HARDWAREINPUT>)"""
        return 'Buffer'._wrap(super(_Buffer, self).DUMMYUNIONNAME_hi(arg0))

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
    def DUMMYUNIONNAME_hi(self) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_hi()"""
        return 'HARDWAREINPUT'._wrap(super(Buffer, self).DUMMYUNIONNAME_hi())

    @overload
    def type(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.type(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).type(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.MOUSEINPUT$Buffer
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
import org.lwjgl.system.windows.MOUSEINPUT as _MOUSEINPUT_Buffer
_Buffer = _MOUSEINPUT_Buffer.Buffer
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
    """org.lwjgl.system.windows.MOUSEINPUT.Buffer"""
 
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
    def dwExtraInfo(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.dwExtraInfo(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).dwExtraInfo(_long.valueOf(arg0)))

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
    def dy(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.dy(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).dy(_int.valueOf(arg0)))

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
    def mouseData(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.mouseData(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).mouseData(_int.valueOf(arg0)))

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
    def dy(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT$Buffer.dy()"""
        return int._wrap(super(Buffer, self).dy())

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
    def time(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT$Buffer.time()"""
        return int._wrap(super(Buffer, self).time())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mouseData(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT$Buffer.mouseData()"""
        return int._wrap(super(Buffer, self).mouseData())

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
    def dwFlags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.dwFlags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).dwFlags(_int.valueOf(arg0)))

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
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT$Buffer.dwFlags()"""
        return int._wrap(super(Buffer, self).dwFlags())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @overload
    def time(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.time(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).time(_int.valueOf(arg0)))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def dx(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.dx(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).dx(_int.valueOf(arg0)))

    @overload
    def dx(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT$Buffer.dx()"""
        return int._wrap(super(Buffer, self).dx())

    @overload
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.MOUSEINPUT$Buffer.dwExtraInfo()"""
        return int._wrap(super(Buffer, self).dwExtraInfo())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val 
 
 
# CLASS: org.lwjgl.system.windows.KEYBDINPUT$Buffer
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
import org.lwjgl.system.windows.KEYBDINPUT as _KEYBDINPUT_Buffer
_Buffer = _KEYBDINPUT_Buffer.Buffer
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
    """org.lwjgl.system.windows.KEYBDINPUT.Buffer"""
 
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
    def time(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT$Buffer.time(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).time(_int.valueOf(arg0)))

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
    def wScan(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT$Buffer.wScan(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).wScan(_short.valueOf(arg0)))

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
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.KEYBDINPUT$Buffer.dwFlags()"""
        return int._wrap(super(Buffer, self).dwFlags())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def dwExtraInfo(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT$Buffer.dwExtraInfo(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).dwExtraInfo(_long.valueOf(arg0)))

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
    def wVk(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT$Buffer.wVk(short)"""
        return 'Buffer'._wrap(super(_Buffer, self).wVk(_short.valueOf(arg0)))

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
    def time(self) -> int:
        """public int org.lwjgl.system.windows.KEYBDINPUT$Buffer.time()"""
        return int._wrap(super(Buffer, self).time())

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
    def wVk(self) -> int:
        """public short org.lwjgl.system.windows.KEYBDINPUT$Buffer.wVk()"""
        return int._wrap(super(Buffer, self).wVk())

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
    def dwFlags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT$Buffer.dwFlags(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).dwFlags(_int.valueOf(arg0)))

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer(java.nio.ByteBuffer)"""
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
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.KEYBDINPUT$Buffer.dwExtraInfo()"""
        return int._wrap(super(Buffer, self).dwExtraInfo())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def wScan(self) -> int:
        """public short org.lwjgl.system.windows.KEYBDINPUT$Buffer.wScan()"""
        return int._wrap(super(Buffer, self).wScan())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0))