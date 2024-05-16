from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Default():
    """org.lwjgl.system.Pointer.Default"""
 
    @staticmethod
    def _wrap(java_value: _Default) -> 'Default':
        return Default(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Default):
        """
        Dynamic initializer for Default.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Default__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Default__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(Default, self).toString())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(Default, self).address())

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
        return int._wrap(super(Default, self).hashCode())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_Default, self).equals(arg0))

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

 
 
 
# CLASS: org.lwjgl.system.Pointer$Default
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Default():
    """org.lwjgl.system.Pointer.Default"""
 
    @staticmethod
    def _wrap(java_value: _Default) -> 'Default':
        return Default(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Default):
        """
        Dynamic initializer for Default.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Default__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Default__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(Default, self).toString())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(Default, self).address())

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
        return int._wrap(super(Default, self).hashCode())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_Default, self).equals(arg0))

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

 
 
 
# CLASS: org.lwjgl.system.Pointer$Default 
 
 
# CLASS: org.lwjgl.system.MemoryUtil$MemoryAllocationReport
import org.lwjgl.system.MemoryUtil as _MemoryUtil_MemoryAllocationReport
_MemoryAllocationReport = _MemoryUtil_MemoryAllocationReport.MemoryAllocationReport
from abc import abstractmethod, ABC
import java.lang.StackTraceElement as StackTraceElement
 
class MemoryAllocationReport():
    """org.lwjgl.system.MemoryUtil.MemoryAllocationReport"""
 
    @staticmethod
    def _wrap(java_value: _MemoryAllocationReport) -> 'MemoryAllocationReport':
        return MemoryAllocationReport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MemoryAllocationReport):
        """
        Dynamic initializer for MemoryAllocationReport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MemoryAllocationReport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MemoryAllocationReport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: str, *arg4: 'StackTraceElement'):
        """public abstract void org.lwjgl.system.MemoryUtil$MemoryAllocationReport.invoke(long,long,long,java.lang.String,java.lang.StackTraceElement...)"""
        pass 
 
 
# CLASS: org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.MemoryUtil as _MemoryUtil_MemoryAllocationReport_Aggregate
_Aggregate = _MemoryUtil_MemoryAllocationReport_Aggregate.MemoryAllocationReport.Aggregate
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
 
class Aggregate():
    """org.lwjgl.system.MemoryUtil.MemoryAllocationReport.Aggregate"""
 
    @staticmethod
    def _wrap(java_value: _Aggregate) -> 'Aggregate':
        return Aggregate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Aggregate):
        """
        Dynamic initializer for Aggregate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Aggregate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Aggregate__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Aggregate':
        """public static org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate.valueOf(java.lang.String)"""
        return Aggregate._wrap(_Aggregate.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['Aggregate']:
        """public static org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate[] org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate.values()"""
        return List[Aggregate]._wrap(_Aggregate.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.system.APIUtil$Encoder
import java.lang.CharSequence as CharSequence
import org.lwjgl.system.APIUtil as _APIUtil_Encoder
_Encoder = _APIUtil_Encoder.Encoder
from abc import abstractmethod, ABC
 
class Encoder():
    """org.lwjgl.system.APIUtil.Encoder"""
 
    @staticmethod
    def _wrap(java_value: _Encoder) -> 'Encoder':
        return Encoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Encoder):
        """
        Dynamic initializer for Encoder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Encoder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Encoder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def encode(self, arg0: 'CharSequence', arg1: bool):
        """public abstract java.nio.ByteBuffer org.lwjgl.system.APIUtil$Encoder.encode(java.lang.CharSequence,boolean)"""
        pass 
 
 
# CLASS: org.lwjgl.system.APIUtil
from pyquantum_helper import import_once as _import_once
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.lwjgl.system.libffi.FFIType as _FFIType
_FFIType = _FFIType
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
import org.lwjgl.system.APIUtil as _APIUtil_APIVersion
_APIVersion = _APIUtil_APIVersion.APIVersion
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _object
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.lang.String as _String
_String = _String
import org.lwjgl.system.APIUtil as _APIUtil
_APIUtil = _APIUtil
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import java.lang.Float as _float
import java.util.Set as Set
import java.lang.Integer as _int
import java.util.function.BiPredicate as BiPredicate
import java.nio.ByteBuffer as ByteBuffer
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class APIUtil():
    """org.lwjgl.system.APIUtil"""
 
    @staticmethod
    def _wrap(java_value: _APIUtil) -> 'APIUtil':
        return APIUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _APIUtil):
        """
        Dynamic initializer for APIUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_APIUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_APIUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def apiArrayp(arg0: 'MemoryStack', *arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.APIUtil.apiArrayp(org.lwjgl.system.MemoryStack,java.nio.ByteBuffer...)"""
        return int._wrap(_APIUtil.apiArrayp(arg0, arg1))

    @staticmethod
    @overload
    def apiArray(arg0: 'MemoryStack', *arg1: int) -> int:
        """public static long org.lwjgl.system.APIUtil.apiArray(org.lwjgl.system.MemoryStack,long...)"""
        return int._wrap(_APIUtil.apiArray(arg0, arg1))

    @staticmethod
    @overload
    def apiGetBytes(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.APIUtil.apiGetBytes(int,int)"""
        return int._wrap(_APIUtil.apiGetBytes(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def apiFindLibrary(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.lwjgl.system.APIUtil.apiFindLibrary(java.lang.String,java.lang.String)"""
        return str._wrap(_APIUtil.apiFindLibrary(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def apiStdcall() -> int:
        """public static int org.lwjgl.system.APIUtil.apiStdcall()"""
        return int._wrap(_APIUtil.apiStdcall())

    @staticmethod
    @overload
    def apiArray(arg0: 'MemoryStack', *arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.APIUtil.apiArray(org.lwjgl.system.MemoryStack,java.nio.ByteBuffer...)"""
        return int._wrap(_APIUtil.apiArray(arg0, arg1))

    @staticmethod
    @overload
    def apiCreateStruct(*arg0: 'libffi.FFIType') -> 'libffi.FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.APIUtil.apiCreateStruct(org.lwjgl.system.libffi.FFIType...)"""
        return libffi.FFIType._wrap(_APIUtil.apiCreateStruct(arg0))

    @staticmethod
    @overload
    def apiClosureRetP(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiClosureRetP(long,long)"""
        _APIUtil.apiClosureRetP(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def apiCreateArray(arg0: 'FFIType', arg1: int) -> 'libffi.FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.APIUtil.apiCreateArray(org.lwjgl.system.libffi.FFIType,int)"""
        return libffi.FFIType._wrap(_APIUtil.apiCreateArray(arg0, _int.valueOf(arg1)))

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
    def apiArrayp(arg0: 'MemoryStack', arg1: 'Encoder', *arg2: 'CharSequence') -> int:
        """public static long org.lwjgl.system.APIUtil.apiArrayp(org.lwjgl.system.MemoryStack,org.lwjgl.system.APIUtil$Encoder,java.lang.CharSequence...)"""
        return int._wrap(_APIUtil.apiArrayp(arg0, arg1, arg2))

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: float):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,float)"""
        _APIUtil.apiClosureRet(_long.valueOf(arg0), _float.valueOf(arg1))

    @staticmethod
    @overload
    def apiCreateUnion(*arg0: 'libffi.FFIType') -> 'libffi.FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.APIUtil.apiCreateUnion(org.lwjgl.system.libffi.FFIType...)"""
        return libffi.FFIType._wrap(_APIUtil.apiCreateUnion(arg0))

    @staticmethod
    @overload
    def apiArray(arg0: 'MemoryStack', arg1: 'Encoder', *arg2: 'CharSequence') -> int:
        """public static long org.lwjgl.system.APIUtil.apiArray(org.lwjgl.system.MemoryStack,org.lwjgl.system.APIUtil$Encoder,java.lang.CharSequence...)"""
        return int._wrap(_APIUtil.apiArray(arg0, arg1, arg2))

    @staticmethod
    @overload
    def apiLogMissing(arg0: str, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.APIUtil.apiLogMissing(java.lang.String,java.nio.ByteBuffer)"""
        _APIUtil.apiLogMissing(arg0, arg1)

    @staticmethod
    @overload
    def apiCreateCIF(arg0: int, arg1: 'FFIType', *arg2: 'libffi.FFIType') -> 'libffi.FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.APIUtil.apiCreateCIF(int,org.lwjgl.system.libffi.FFIType,org.lwjgl.system.libffi.FFIType...)"""
        return libffi.FFICIF._wrap(_APIUtil.apiCreateCIF(_int.valueOf(arg0), arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def apiParseVersion(arg0: str) -> 'APIVersion':
        """public static org.lwjgl.system.APIUtil$APIVersion org.lwjgl.system.APIUtil.apiParseVersion(java.lang.String)"""
        return APIVersion._wrap(_APIUtil.apiParseVersion(arg0))

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: float):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,double)"""
        _APIUtil.apiClosureRet(_long.valueOf(arg0), _double.valueOf(arg1))

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,int)"""
        _APIUtil.apiClosureRet(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def apiLog(arg0: 'CharSequence'):
        """public static void org.lwjgl.system.APIUtil.apiLog(java.lang.CharSequence)"""
        _APIUtil.apiLog(arg0)

    @staticmethod
    @overload
    def apiLogMore(arg0: 'CharSequence'):
        """public static void org.lwjgl.system.APIUtil.apiLogMore(java.lang.CharSequence)"""
        _APIUtil.apiLogMore(arg0)

    @staticmethod
    @overload
    def apiClosureRetL(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiClosureRetL(long,long)"""
        _APIUtil.apiClosureRetL(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def apiClassTokens(arg0: 'BiPredicate', arg1: 'Map', *arg2: 'type.Class') -> 'Map':
        """public static java.util.Map<java.lang.Integer, java.lang.String> org.lwjgl.system.APIUtil.apiClassTokens(java.util.function.BiPredicate<java.lang.reflect.Field, java.lang.Integer>,java.util.Map<java.lang.Integer, java.lang.String>,java.lang.Class<?>...)"""
        return Map._wrap(_APIUtil.apiClassTokens(arg0, arg1, arg2))

    @staticmethod
    @overload
    def apiArrayFree(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiArrayFree(long,int)"""
        _APIUtil.apiArrayFree(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,byte)"""
        _APIUtil.apiClosureRet(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def apiUnknownToken(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.APIUtil.apiUnknownToken(java.lang.String,int)"""
        return str._wrap(_APIUtil.apiUnknownToken(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def apiCreateCIFVar(arg0: int, arg1: int, arg2: 'FFIType', *arg3: 'libffi.FFIType') -> 'libffi.FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.APIUtil.apiCreateCIFVar(int,int,org.lwjgl.system.libffi.FFIType,org.lwjgl.system.libffi.FFIType...)"""
        return libffi.FFICIF._wrap(_APIUtil.apiCreateCIFVar(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def apiGetFunctionAddress(arg0: 'FunctionProvider', arg1: str) -> int:
        """public static long org.lwjgl.system.APIUtil.apiGetFunctionAddress(org.lwjgl.system.FunctionProvider,java.lang.String)"""
        return int._wrap(_APIUtil.apiGetFunctionAddress(arg0, arg1))

    @staticmethod
    @overload
    def apiGetFunctionAddressOptional(arg0: 'SharedLibrary', arg1: str) -> int:
        """public static long org.lwjgl.system.APIUtil.apiGetFunctionAddressOptional(org.lwjgl.system.SharedLibrary,java.lang.String)"""
        return int._wrap(_APIUtil.apiGetFunctionAddressOptional(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: bool):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,boolean)"""
        _APIUtil.apiClosureRet(_long.valueOf(arg0), _boolean.valueOf(arg1))

    @staticmethod
    @overload
    def apiCheckAllocation(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.APIUtil.apiCheckAllocation(int,long,long)"""
        return int._wrap(_APIUtil.apiCheckAllocation(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def apiFilterExtensions(arg0: 'Set', arg1: 'Configuration'):
        """public static void org.lwjgl.system.APIUtil.apiFilterExtensions(java.util.Set<java.lang.String>,org.lwjgl.system.Configuration<java.lang.Object>)"""
        _APIUtil.apiFilterExtensions(arg0, arg1)

    @staticmethod
    @overload
    def apiGetMappedBuffer(arg0: 'ByteBuffer', arg1: int, arg2: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.APIUtil.apiGetMappedBuffer(java.nio.ByteBuffer,long,int)"""
        return ByteBuffer._wrap(_APIUtil.apiGetMappedBuffer(arg0, _long.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def apiUnknownToken(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.APIUtil.apiUnknownToken(int)"""
        return str._wrap(_APIUtil.apiUnknownToken(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def apiArrayi(arg0: 'MemoryStack', arg1: 'Encoder', *arg2: 'CharSequence') -> int:
        """public static long org.lwjgl.system.APIUtil.apiArrayi(org.lwjgl.system.MemoryStack,org.lwjgl.system.APIUtil$Encoder,java.lang.CharSequence...)"""
        return int._wrap(_APIUtil.apiArrayi(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,short)"""
        _APIUtil.apiClosureRet(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def apiParseVersion(arg0: 'Configuration') -> 'APIVersion':
        """public static org.lwjgl.system.APIUtil$APIVersion org.lwjgl.system.APIUtil.apiParseVersion(org.lwjgl.system.Configuration<?>)"""
        return APIVersion._wrap(_APIUtil.apiParseVersion(arg0))

    @staticmethod
    @overload
    def apiCreateLibrary(arg0: str) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.APIUtil.apiCreateLibrary(java.lang.String)"""
        return SharedLibrary._wrap(_APIUtil.apiCreateLibrary(arg0))

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
 
 
# CLASS: org.lwjgl.system.MemoryStack
from pyquantum_helper import import_once as _import_once
import java.lang.Double as _double
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
import java.lang.Short as _short
import java.nio.FloatBuffer as FloatBuffer
import org.lwjgl.CLongBuffer as _CLongBuffer
_CLongBuffer = _CLongBuffer
import java.nio.DoubleBuffer as _DoubleBuffer
_DoubleBuffer = _DoubleBuffer
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
import java.nio.DoubleBuffer as DoubleBuffer
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
from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import org.lwjgl.system.MemoryStack as _MemoryStack
_MemoryStack = _MemoryStack
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MemoryStack():
    """org.lwjgl.system.MemoryStack"""
 
    @staticmethod
    def _wrap(java_value: _MemoryStack) -> 'MemoryStack':
        return MemoryStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MemoryStack):
        """
        Dynamic initializer for MemoryStack.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MemoryStack__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MemoryStack__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def stackCallocCLong(arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCallocCLong(int)"""
        return pygl.CLongBuffer._wrap(_MemoryStack.stackCallocCLong(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackMallocFloat(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackMallocFloat(int)"""
        return FloatBuffer._wrap(_MemoryStack.stackMallocFloat(_int.valueOf(arg0)))

    @overload
    def nmalloc(self, arg0: int, arg1: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nmalloc(int,int)"""
        return int._wrap(super(_MemoryStack, self).nmalloc(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def stackMallocCLong(arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackMallocCLong(int)"""
        return pygl.CLongBuffer._wrap(_MemoryStack.stackMallocCLong(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackBytes(arg0: int, arg1: int, arg2: int, arg3: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackBytes(byte,byte,byte,byte)"""
        return ByteBuffer._wrap(_MemoryStack.stackBytes(_byte.valueOf(arg0), _byte.valueOf(arg1), _byte.valueOf(arg2), _byte.valueOf(arg3)))

    @staticmethod
    @overload
    def stackBytes(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackBytes(byte)"""
        return ByteBuffer._wrap(_MemoryStack.stackBytes(_byte.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def ASCIISafe(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.ASCIISafe(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).ASCIISafe(arg0, _boolean.valueOf(arg1)))

    @overload
    def shorts(self, arg0: int, arg1: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.shorts(short,short)"""
        return 'ShortBuffer'._wrap(super(_MemoryStack, self).shorts(_short.valueOf(arg0), _short.valueOf(arg1)))

    @overload
    def nint(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nint(int)"""
        return int._wrap(super(_MemoryStack, self).nint(_int.valueOf(arg0)))

    @overload
    def longs(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.longs(long,long,long,long)"""
        return 'LongBuffer'._wrap(super(_MemoryStack, self).longs(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def stackCallocPointer(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackCallocPointer(int)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackCallocPointer(_int.valueOf(arg0)))

    @overload
    def floats(self, *arg0: float) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.floats(float...)"""
        return 'FloatBuffer'._wrap(super(_MemoryStack, self).floats(arg0))

    @overload
    def floats(self, arg0: float, arg1: float) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.floats(float,float)"""
        return 'FloatBuffer'._wrap(super(_MemoryStack, self).floats(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def stackUTF16Safe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF16Safe(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryStack.stackUTF16Safe(arg0))

    @staticmethod
    @overload
    def create() -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.create()"""
        return MemoryStack._wrap(_MemoryStack.create())

    @overload
    def doubles(self, *arg0: float) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.doubles(double...)"""
        return 'DoubleBuffer'._wrap(super(_MemoryStack, self).doubles(arg0))

    @overload
    def ints(self, arg0: int, arg1: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.ints(int,int)"""
        return 'IntBuffer'._wrap(super(_MemoryStack, self).ints(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def pointers(self, arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(long,long)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(_long.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def npointer(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.npointer(long)"""
        return int._wrap(super(_MemoryStack, self).npointer(_long.valueOf(arg0)))

    @overload
    def longs(self, arg0: int, arg1: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.longs(long,long)"""
        return 'LongBuffer'._wrap(super(_MemoryStack, self).longs(_long.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def getSize(self) -> int:
        """public int org.lwjgl.system.MemoryStack.getSize()"""
        return int._wrap(super(MemoryStack, self).getSize())

    @overload
    def ASCII(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.ASCII(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).ASCII(arg0, _boolean.valueOf(arg1)))

    @overload
    def UTF16Safe(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF16Safe(java.lang.CharSequence)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).UTF16Safe(arg0))

    @staticmethod
    @overload
    def stackCLongs(arg0: int, arg1: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCLongs(long,long)"""
        return pygl.CLongBuffer._wrap(_MemoryStack.stackCLongs(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def stackPointers(arg0: 'Pointer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(org.lwjgl.system.Pointer)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackPointers(arg0))

    @staticmethod
    @overload
    def stackFloats(arg0: float, arg1: float) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackFloats(float,float)"""
        return FloatBuffer._wrap(_MemoryStack.stackFloats(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def stackLongs(arg0: int, arg1: int, arg2: int, arg3: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackLongs(long,long,long,long)"""
        return LongBuffer._wrap(_MemoryStack.stackLongs(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @overload
    def floats(self, arg0: float) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.floats(float)"""
        return 'FloatBuffer'._wrap(super(_MemoryStack, self).floats(_float.valueOf(arg0)))

    @overload
    def callocShort(self, arg0: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.callocShort(int)"""
        return 'ShortBuffer'._wrap(super(_MemoryStack, self).callocShort(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackLongs(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackLongs(long)"""
        return LongBuffer._wrap(_MemoryStack.stackLongs(_long.valueOf(arg0)))

    @overload
    def pointers(self, arg0: 'Buffer', arg1: 'Buffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(java.nio.Buffer,java.nio.Buffer)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(arg0, arg1))

    @overload
    def nbyte(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nbyte(byte)"""
        return int._wrap(super(_MemoryStack, self).nbyte(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def stackCallocShort(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackCallocShort(int)"""
        return ShortBuffer._wrap(_MemoryStack.stackCallocShort(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackPointers(arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(long,long)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackPointers(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def stackUTF8Safe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF8Safe(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryStack.stackUTF8Safe(arg0))

    @overload
    def UTF16(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF16(java.lang.CharSequence)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).UTF16(arg0))

    @overload
    def calloc(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.calloc(int)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackPointers(*arg0: 'Pointer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(org.lwjgl.system.Pointer...)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackPointers(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def nUTF8(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nUTF8(java.lang.CharSequence,boolean)"""
        return int._wrap(super(_MemoryStack, self).nUTF8(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackUTF8(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF8(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryStack.stackUTF8(arg0))

    @overload
    def getFrameIndex(self) -> int:
        """public int org.lwjgl.system.MemoryStack.getFrameIndex()"""
        return int._wrap(super(MemoryStack, self).getFrameIndex())

    @staticmethod
    @overload
    def create(arg0: int) -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.create(int)"""
        return MemoryStack._wrap(_MemoryStack.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackGet() -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.stackGet()"""
        return MemoryStack._wrap(_MemoryStack.stackGet())

    @staticmethod
    @overload
    def stackInts(arg0: int, arg1: int, arg2: int, arg3: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackInts(int,int,int,int)"""
        return IntBuffer._wrap(_MemoryStack.stackInts(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def pointersOfElements(self, arg0: 'CustomBuffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointersOfElements(org.lwjgl.system.CustomBuffer<?>)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointersOfElements(arg0))

    @overload
    def floats(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.floats(float,float,float,float)"""
        return 'FloatBuffer'._wrap(super(_MemoryStack, self).floats(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def ASCIISafe(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.ASCIISafe(java.lang.CharSequence)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).ASCIISafe(arg0))

    @staticmethod
    @overload
    def stackFloats(arg0: float) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackFloats(float)"""
        return FloatBuffer._wrap(_MemoryStack.stackFloats(_float.valueOf(arg0)))

    @overload
    def npointer(self, arg0: 'Pointer') -> int:
        """public long org.lwjgl.system.MemoryStack.npointer(org.lwjgl.system.Pointer)"""
        return int._wrap(super(_MemoryStack, self).npointer(arg0))

    @overload
    def nUTF16Safe(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nUTF16Safe(java.lang.CharSequence,boolean)"""
        return int._wrap(super(_MemoryStack, self).nUTF16Safe(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def nstackMalloc(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryStack.nstackMalloc(int)"""
        return int._wrap(_MemoryStack.nstackMalloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackFloats(*arg0: float) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackFloats(float...)"""
        return FloatBuffer._wrap(_MemoryStack.stackFloats(arg0))

    @overload
    def longs(self, arg0: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.longs(long)"""
        return 'LongBuffer'._wrap(super(_MemoryStack, self).longs(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stackBytes(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackBytes(byte,byte)"""
        return ByteBuffer._wrap(_MemoryStack.stackBytes(_byte.valueOf(arg0), _byte.valueOf(arg1)))

    @overload
    def bytes(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.bytes(byte,byte,byte,byte)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).bytes(_byte.valueOf(arg0), _byte.valueOf(arg1), _byte.valueOf(arg2), _byte.valueOf(arg3)))

    @overload
    def UTF8(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF8(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).UTF8(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackPointers(arg0: 'Pointer', arg1: 'Pointer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackPointers(arg0, arg1))

    @overload
    def nUTF8Safe(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nUTF8Safe(java.lang.CharSequence,boolean)"""
        return int._wrap(super(_MemoryStack, self).nUTF8Safe(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackCLongs(arg0: int, arg1: int, arg2: int, arg3: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCLongs(long,long,long,long)"""
        return pygl.CLongBuffer._wrap(_MemoryStack.stackCLongs(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @overload
    def ints(self, *arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.ints(int...)"""
        return 'IntBuffer'._wrap(super(_MemoryStack, self).ints(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def stackCallocInt(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackCallocInt(int)"""
        return IntBuffer._wrap(_MemoryStack.stackCallocInt(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def nmalloc(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nmalloc(int)"""
        return int._wrap(super(_MemoryStack, self).nmalloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackLongs(*arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackLongs(long...)"""
        return LongBuffer._wrap(_MemoryStack.stackLongs(arg0))

    @overload
    def ints(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.ints(int)"""
        return 'IntBuffer'._wrap(super(_MemoryStack, self).ints(_int.valueOf(arg0)))

    @overload
    def clongs(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.clongs(long,long,long,long)"""
        return 'pygl.CLongBuffer'._wrap(super(_MemoryStack, self).clongs(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @overload
    def setPointer(self, arg0: int):
        """public void org.lwjgl.system.MemoryStack.setPointer(int)"""
        super(_MemoryStack, self).setPointer(_int.valueOf(arg0))

    @staticmethod
    @overload
    def stackFloats(arg0: float, arg1: float, arg2: float) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackFloats(float,float,float)"""
        return FloatBuffer._wrap(_MemoryStack.stackFloats(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def nstackCalloc(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.MemoryStack.nstackCalloc(int,int,int)"""
        return int._wrap(_MemoryStack.nstackCalloc(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def stackUTF16Safe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF16Safe(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryStack.stackUTF16Safe(arg0, _boolean.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_Default, self).equals(arg0))

    @staticmethod
    @overload
    def stackShorts(arg0: int, arg1: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackShorts(short,short)"""
        return ShortBuffer._wrap(_MemoryStack.stackShorts(_short.valueOf(arg0), _short.valueOf(arg1)))

    @overload
    def getPointerAddress(self) -> int:
        """public long org.lwjgl.system.MemoryStack.getPointerAddress()"""
        return int._wrap(super(MemoryStack, self).getPointerAddress())

    @staticmethod
    @overload
    def stackInts(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackInts(int,int)"""
        return IntBuffer._wrap(_MemoryStack.stackInts(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstackMalloc(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryStack.nstackMalloc(int,int)"""
        return int._wrap(_MemoryStack.nstackMalloc(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def stackMallocInt(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackMallocInt(int)"""
        return IntBuffer._wrap(_MemoryStack.stackMallocInt(_int.valueOf(arg0)))

    @overload
    def callocPointer(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.callocPointer(int)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).callocPointer(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackDoubles(arg0: float, arg1: float, arg2: float) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackDoubles(double,double,double)"""
        return DoubleBuffer._wrap(_MemoryStack.stackDoubles(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def stackShorts(arg0: int, arg1: int, arg2: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackShorts(short,short,short)"""
        return ShortBuffer._wrap(_MemoryStack.stackShorts(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2)))

    @overload
    def pointers(self, *arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(long...)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(arg0))

    @staticmethod
    @overload
    def stackMallocLong(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackMallocLong(int)"""
        return LongBuffer._wrap(_MemoryStack.stackMallocLong(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackPointers(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(long)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackPointers(_long.valueOf(arg0)))

    @overload
    def UTF16Safe(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF16Safe(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).UTF16Safe(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackUTF16(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF16(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryStack.stackUTF16(arg0, _boolean.valueOf(arg1)))

    @overload
    def mallocLong(self, arg0: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.mallocLong(int)"""
        return 'LongBuffer'._wrap(super(_MemoryStack, self).mallocLong(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackInts(*arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackInts(int...)"""
        return IntBuffer._wrap(_MemoryStack.stackInts(arg0))

    @staticmethod
    @overload
    def stackDoubles(arg0: float) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackDoubles(double)"""
        return DoubleBuffer._wrap(_MemoryStack.stackDoubles(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def stackCallocLong(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackCallocLong(int)"""
        return LongBuffer._wrap(_MemoryStack.stackCallocLong(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(Default, self).toString())

    @overload
    def pointers(self, arg0: 'Pointer', arg1: 'Pointer', arg2: 'Pointer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(arg0, arg1, arg2))

    @overload
    def callocLong(self, arg0: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.callocLong(int)"""
        return 'LongBuffer'._wrap(super(_MemoryStack, self).callocLong(_int.valueOf(arg0)))

    @overload
    def doubles(self, arg0: float, arg1: float) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.doubles(double,double)"""
        return 'DoubleBuffer'._wrap(super(_MemoryStack, self).doubles(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def bytes(self, *arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.bytes(byte...)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).bytes(bytes))

    @overload
    def ncalloc(self, arg0: int, arg1: int, arg2: int) -> int:
        """public long org.lwjgl.system.MemoryStack.ncalloc(int,int,int)"""
        return int._wrap(super(_MemoryStack, self).ncalloc(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def pointers(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(long)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(_long.valueOf(arg0)))

    @overload
    def nASCIISafe(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nASCIISafe(java.lang.CharSequence,boolean)"""
        return int._wrap(super(_MemoryStack, self).nASCIISafe(arg0, _boolean.valueOf(arg1)))

    @overload
    def pointers(self, arg0: 'Pointer', arg1: 'Pointer', arg2: 'Pointer', arg3: 'Pointer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stackPush() -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.stackPush()"""
        return MemoryStack._wrap(_MemoryStack.stackPush())

    @staticmethod
    @overload
    def stackBytes(*arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackBytes(byte...)"""
        return ByteBuffer._wrap(_MemoryStack.stackBytes(bytes))

    @overload
    def pointers(self, arg0: 'Buffer', arg1: 'Buffer', arg2: 'Buffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(java.nio.Buffer,java.nio.Buffer,java.nio.Buffer)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(arg0, arg1, arg2))

    @overload
    def mallocInt(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.mallocInt(int)"""
        return 'IntBuffer'._wrap(super(_MemoryStack, self).mallocInt(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackInts(arg0: int, arg1: int, arg2: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackInts(int,int,int)"""
        return IntBuffer._wrap(_MemoryStack.stackInts(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def stackMallocShort(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackMallocShort(int)"""
        return ShortBuffer._wrap(_MemoryStack.stackMallocShort(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackMallocDouble(arg0: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackMallocDouble(int)"""
        return DoubleBuffer._wrap(_MemoryStack.stackMallocDouble(_int.valueOf(arg0)))

    @overload
    def pointers(self, arg0: 'Buffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(java.nio.Buffer)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(arg0))

    @staticmethod
    @overload
    def stackLongs(arg0: int, arg1: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackLongs(long,long)"""
        return LongBuffer._wrap(_MemoryStack.stackLongs(_long.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def nASCII(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nASCII(java.lang.CharSequence,boolean)"""
        return int._wrap(super(_MemoryStack, self).nASCII(arg0, _boolean.valueOf(arg1)))

    @overload
    def doubles(self, arg0: float, arg1: float, arg2: float) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.doubles(double,double,double)"""
        return 'DoubleBuffer'._wrap(super(_MemoryStack, self).doubles(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def mallocDouble(self, arg0: int) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.mallocDouble(int)"""
        return 'DoubleBuffer'._wrap(super(_MemoryStack, self).mallocDouble(_int.valueOf(arg0)))

    @overload
    def ndouble(self, arg0: float) -> int:
        """public long org.lwjgl.system.MemoryStack.ndouble(double)"""
        return int._wrap(super(_MemoryStack, self).ndouble(_double.valueOf(arg0)))

    @overload
    def pointers(self, arg0: 'Pointer', arg1: 'Pointer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(arg0, arg1))

    @staticmethod
    @overload
    def stackShorts(*arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackShorts(short...)"""
        return ShortBuffer._wrap(_MemoryStack.stackShorts(arg0))

    @overload
    def pointers(self, arg0: int, arg1: int, arg2: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(long,long,long)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @overload
    def clongs(self, *arg0: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.clongs(long...)"""
        return 'pygl.CLongBuffer'._wrap(super(_MemoryStack, self).clongs(arg0))

    @staticmethod
    @overload
    def stackASCIISafe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackASCIISafe(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryStack.stackASCIISafe(arg0, _boolean.valueOf(arg1)))

    @overload
    def longs(self, arg0: int, arg1: int, arg2: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.longs(long,long,long)"""
        return 'LongBuffer'._wrap(super(_MemoryStack, self).longs(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @overload
    def nfloat(self, arg0: float) -> int:
        """public long org.lwjgl.system.MemoryStack.nfloat(float)"""
        return int._wrap(super(_MemoryStack, self).nfloat(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def stackUTF16(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF16(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryStack.stackUTF16(arg0))

    @overload
    def pointers(self, *arg0: 'Buffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(java.nio.Buffer...)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(arg0))

    @overload
    def calloc(self, arg0: int, arg1: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.calloc(int,int)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).calloc(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def mallocShort(self, arg0: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.mallocShort(int)"""
        return 'ShortBuffer'._wrap(super(_MemoryStack, self).mallocShort(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackDoubles(arg0: float, arg1: float, arg2: float, arg3: float) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackDoubles(double,double,double,double)"""
        return DoubleBuffer._wrap(_MemoryStack.stackDoubles(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @staticmethod
    @overload
    def stackMallocPointer(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackMallocPointer(int)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackMallocPointer(_int.valueOf(arg0)))

    @overload
    def malloc(self, arg0: int, arg1: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.malloc(int,int)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).malloc(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def pointers(self, arg0: 'Pointer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(org.lwjgl.system.Pointer)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(arg0))

    @staticmethod
    @overload
    def stackCLongs(arg0: int, arg1: int, arg2: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCLongs(long,long,long)"""
        return pygl.CLongBuffer._wrap(_MemoryStack.stackCLongs(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def malloc(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.malloc(int)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackDoubles(*arg0: float) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackDoubles(double...)"""
        return DoubleBuffer._wrap(_MemoryStack.stackDoubles(arg0))

    @staticmethod
    @overload
    def stackCLongs(arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCLongs(long)"""
        return pygl.CLongBuffer._wrap(_MemoryStack.stackCLongs(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stackCalloc(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackCalloc(int)"""
        return ByteBuffer._wrap(_MemoryStack.stackCalloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackPointers(arg0: int, arg1: int, arg2: int, arg3: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(long,long,long,long)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackPointers(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @overload
    def bytes(self, arg0: int, arg1: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.bytes(byte,byte)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).bytes(_byte.valueOf(arg0), _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def stackCLongs(*arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCLongs(long...)"""
        return pygl.CLongBuffer._wrap(_MemoryStack.stackCLongs(arg0))

    @staticmethod
    @overload
    def stackPop() -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.stackPop()"""
        return MemoryStack._wrap(_MemoryStack.stackPop())

    @overload
    def doubles(self, arg0: float) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.doubles(double)"""
        return 'DoubleBuffer'._wrap(super(_MemoryStack, self).doubles(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def stackCallocFloat(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackCallocFloat(int)"""
        return FloatBuffer._wrap(_MemoryStack.stackCallocFloat(_int.valueOf(arg0)))

    @overload
    def pointers(self, *arg0: 'Pointer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(org.lwjgl.system.Pointer...)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(arg0))

    @staticmethod
    @overload
    def stackShorts(arg0: int, arg1: int, arg2: int, arg3: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackShorts(short,short,short,short)"""
        return ShortBuffer._wrap(_MemoryStack.stackShorts(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3)))

    @overload
    def shorts(self, *arg0: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.shorts(short...)"""
        return 'ShortBuffer'._wrap(super(_MemoryStack, self).shorts(arg0))

    @overload
    def pop(self) -> 'MemoryStack':
        """public org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.pop()"""
        return 'MemoryStack'._wrap(super(MemoryStack, self).pop())

    @overload
    def nUTF16(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nUTF16(java.lang.CharSequence,boolean)"""
        return int._wrap(super(_MemoryStack, self).nUTF16(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackPointers(arg0: 'Pointer', arg1: 'Pointer', arg2: 'Pointer', arg3: 'Pointer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackPointers(arg0, arg1, arg2, arg3))

    @overload
    def shorts(self, arg0: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.shorts(short)"""
        return 'ShortBuffer'._wrap(super(_MemoryStack, self).shorts(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def stackBytes(arg0: int, arg1: int, arg2: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackBytes(byte,byte,byte)"""
        return ByteBuffer._wrap(_MemoryStack.stackBytes(_byte.valueOf(arg0), _byte.valueOf(arg1), _byte.valueOf(arg2)))

    @overload
    def callocInt(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.callocInt(int)"""
        return 'IntBuffer'._wrap(super(_MemoryStack, self).callocInt(_int.valueOf(arg0)))

    @overload
    def pointers(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(long,long,long,long)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def longs(self, *arg0: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.longs(long...)"""
        return 'LongBuffer'._wrap(super(_MemoryStack, self).longs(arg0))

    @staticmethod
    @overload
    def stackCallocDouble(arg0: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackCallocDouble(int)"""
        return DoubleBuffer._wrap(_MemoryStack.stackCallocDouble(_int.valueOf(arg0)))

    @overload
    def clongs(self, arg0: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.clongs(long)"""
        return 'pygl.CLongBuffer'._wrap(super(_MemoryStack, self).clongs(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stackUTF8Safe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF8Safe(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryStack.stackUTF8Safe(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: 'ByteBuffer') -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.create(java.nio.ByteBuffer)"""
        return MemoryStack._wrap(_MemoryStack.create(arg0))

    @staticmethod
    @overload
    def stackASCII(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackASCII(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryStack.stackASCII(arg0, _boolean.valueOf(arg1)))

    @overload
    def nclong(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nclong(long)"""
        return int._wrap(super(_MemoryStack, self).nclong(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def stackPointers(arg0: int, arg1: int, arg2: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(long,long,long)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackPointers(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def ncreate(arg0: int, arg1: int) -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.ncreate(long,int)"""
        return MemoryStack._wrap(_MemoryStack.ncreate(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def push(self) -> 'MemoryStack':
        """public org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.push()"""
        return 'MemoryStack'._wrap(super(MemoryStack, self).push())

    @overload
    def callocFloat(self, arg0: int) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.callocFloat(int)"""
        return 'FloatBuffer'._wrap(super(_MemoryStack, self).callocFloat(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackFloats(arg0: float, arg1: float, arg2: float, arg3: float) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackFloats(float,float,float,float)"""
        return FloatBuffer._wrap(_MemoryStack.stackFloats(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @staticmethod
    @overload
    def stackASCIISafe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackASCIISafe(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryStack.stackASCIISafe(arg0))

    @overload
    def ints(self, arg0: int, arg1: int, arg2: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.ints(int,int,int)"""
        return 'IntBuffer'._wrap(super(_MemoryStack, self).ints(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def shorts(self, arg0: int, arg1: int, arg2: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.shorts(short,short,short)"""
        return 'ShortBuffer'._wrap(super(_MemoryStack, self).shorts(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2)))

    @overload
    def bytes(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.bytes(byte)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).bytes(_byte.valueOf(arg0)))

    @overload
    def UTF8(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF8(java.lang.CharSequence)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).UTF8(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(Default, self).address())

    @overload
    def floats(self, arg0: float, arg1: float, arg2: float) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.floats(float,float,float)"""
        return 'FloatBuffer'._wrap(super(_MemoryStack, self).floats(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def mallocPointer(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.mallocPointer(int)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).mallocPointer(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(Default, self).hashCode())

    @staticmethod
    @overload
    def stackInts(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackInts(int)"""
        return IntBuffer._wrap(_MemoryStack.stackInts(_int.valueOf(arg0)))

    @overload
    def UTF16(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF16(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).UTF16(arg0, _boolean.valueOf(arg1)))

    @overload
    def mallocCLong(self, arg0: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.mallocCLong(int)"""
        return 'pygl.CLongBuffer'._wrap(super(_MemoryStack, self).mallocCLong(_int.valueOf(arg0)))

    @overload
    def UTF8Safe(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF8Safe(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).UTF8Safe(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackPointers(*arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(long...)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackPointers(arg0))

    @overload
    def clongs(self, arg0: int, arg1: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.clongs(long,long)"""
        return 'pygl.CLongBuffer'._wrap(super(_MemoryStack, self).clongs(_long.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def UTF8Safe(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF8Safe(java.lang.CharSequence)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).UTF8Safe(arg0))

    @overload
    def mallocFloat(self, arg0: int) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.mallocFloat(int)"""
        return 'FloatBuffer'._wrap(super(_MemoryStack, self).mallocFloat(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackPointers(arg0: 'Pointer', arg1: 'Pointer', arg2: 'Pointer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return pygl.PointerBuffer._wrap(_MemoryStack.stackPointers(arg0, arg1, arg2))

    @overload
    def clongs(self, arg0: int, arg1: int, arg2: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.clongs(long,long,long)"""
        return 'pygl.CLongBuffer'._wrap(super(_MemoryStack, self).clongs(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @overload
    def pointers(self, arg0: 'Buffer', arg1: 'Buffer', arg2: 'Buffer', arg3: 'Buffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(java.nio.Buffer,java.nio.Buffer,java.nio.Buffer,java.nio.Buffer)"""
        return 'pygl.PointerBuffer'._wrap(super(_MemoryStack, self).pointers(arg0, arg1, arg2, arg3))

    @overload
    def nlong(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nlong(long)"""
        return int._wrap(super(_MemoryStack, self).nlong(_long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public void org.lwjgl.system.MemoryStack.close()"""
        super(MemoryStack, self).close()

    @staticmethod
    @overload
    def stackLongs(arg0: int, arg1: int, arg2: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackLongs(long,long,long)"""
        return LongBuffer._wrap(_MemoryStack.stackLongs(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @overload
    def ints(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.ints(int,int,int,int)"""
        return 'IntBuffer'._wrap(super(_MemoryStack, self).ints(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @staticmethod
    @overload
    def stackShorts(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackShorts(short)"""
        return ShortBuffer._wrap(_MemoryStack.stackShorts(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def stackUTF8(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF8(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryStack.stackUTF8(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackDoubles(arg0: float, arg1: float) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackDoubles(double,double)"""
        return DoubleBuffer._wrap(_MemoryStack.stackDoubles(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def getAddress(self) -> int:
        """public long org.lwjgl.system.MemoryStack.getAddress()"""
        return int._wrap(super(MemoryStack, self).getAddress())

    @overload
    def shorts(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.shorts(short,short,short,short)"""
        return 'ShortBuffer'._wrap(super(_MemoryStack, self).shorts(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3)))

    @overload
    def nshort(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nshort(short)"""
        return int._wrap(super(_MemoryStack, self).nshort(_short.valueOf(arg0)))

    @overload
    def bytes(self, arg0: int, arg1: int, arg2: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.bytes(byte,byte,byte)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).bytes(_byte.valueOf(arg0), _byte.valueOf(arg1), _byte.valueOf(arg2)))

    @overload
    def doubles(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.doubles(double,double,double,double)"""
        return 'DoubleBuffer'._wrap(super(_MemoryStack, self).doubles(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3)))

    @staticmethod
    @overload
    def stackASCII(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackASCII(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryStack.stackASCII(arg0))

    @overload
    def callocCLong(self, arg0: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.callocCLong(int)"""
        return 'pygl.CLongBuffer'._wrap(super(_MemoryStack, self).callocCLong(_int.valueOf(arg0)))

    @overload
    def getPointer(self) -> int:
        """public int org.lwjgl.system.MemoryStack.getPointer()"""
        return int._wrap(super(MemoryStack, self).getPointer())

    @staticmethod
    @overload
    def stackMalloc(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackMalloc(int)"""
        return ByteBuffer._wrap(_MemoryStack.stackMalloc(_int.valueOf(arg0)))

    @overload
    def ASCII(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.ASCII(java.lang.CharSequence)"""
        return 'ByteBuffer'._wrap(super(_MemoryStack, self).ASCII(arg0))

    @overload
    def npointer(self, arg0: 'Buffer') -> int:
        """public long org.lwjgl.system.MemoryStack.npointer(java.nio.Buffer)"""
        return int._wrap(super(_MemoryStack, self).npointer(arg0))

    @overload
    def callocDouble(self, arg0: int) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.callocDouble(int)"""
        return 'DoubleBuffer'._wrap(super(_MemoryStack, self).callocDouble(_int.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.Struct
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Struct():
    """org.lwjgl.system.Struct"""
 
    @staticmethod
    def _wrap(java_value: _Struct) -> 'Struct':
        return Struct(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Struct):
        """
        Dynamic initializer for Struct.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Struct__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Struct__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(Default, self).toString())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(Default, self).address())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_Struct, self).isNull(_int.valueOf(arg0)))

    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(Struct, self).clear()

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
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(Struct, self).free()

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

    @abstractmethod
    def sizeof(self, ):
        """public abstract int org.lwjgl.system.Struct.sizeof()"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(Default, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_Default, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.system.Struct$Layout
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.lwjgl.system.Struct as _Struct_Member
_Member = _Struct_Member.Member
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct_Layout
_Layout = _Struct_Layout.Layout
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Layout():
    """org.lwjgl.system.Struct.Layout"""
 
    @staticmethod
    def _wrap(java_value: _Layout) -> 'Layout':
        return Layout(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Layout):
        """
        Dynamic initializer for Layout.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Layout__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Layout__wrapper":
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
    def getSize(self) -> int:
        """public int org.lwjgl.system.Struct$Member.getSize()"""
        return int._wrap(super(Member, self).getSize())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def offsetof(self, arg0: int) -> int:
        """public int org.lwjgl.system.Struct$Layout.offsetof(int)"""
        return int._wrap(super(_Layout, self).offsetof(_int.valueOf(arg0)))

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

    @overload
    def getAlignment(self, arg0: int) -> int:
        """public int org.lwjgl.system.Struct$Member.getAlignment(int)"""
        return int._wrap(super(_Member, self).getAlignment(_int.valueOf(arg0)))

    @override
    @overload
    def getAlignment(self) -> int:
        """public int org.lwjgl.system.Struct$Member.getAlignment()"""
        return int._wrap(super(Member, self).getAlignment())

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
 
 
# CLASS: org.lwjgl.system.Library
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import org.lwjgl.system.Library as _Library
_Library = _Library
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Library():
    """org.lwjgl.system.Library"""
 
    @staticmethod
    def _wrap(java_value: _Library) -> 'Library':
        return Library(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Library):
        """
        Dynamic initializer for Library.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Library__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Library__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def loadNative(arg0: 'Class', arg1: str, arg2: str, arg3: bool) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.Library.loadNative(java.lang.Class<?>,java.lang.String,java.lang.String,boolean)"""
        return SharedLibrary._wrap(_Library.loadNative(arg0, arg1, arg2, _boolean.valueOf(arg3)))

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
    def loadSystem(arg0: 'Consumer', arg1: 'Consumer', arg2: 'Class', arg3: str, arg4: str):
        """public static void org.lwjgl.system.Library.loadSystem(java.util.function.Consumer<java.lang.String>,java.util.function.Consumer<java.lang.String>,java.lang.Class<?>,java.lang.String,java.lang.String) throws java.lang.UnsatisfiedLinkError"""
        _Library.loadSystem(arg0, arg1, arg2, arg3, arg4)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def loadSystem(arg0: str, arg1: str):
        """public static void org.lwjgl.system.Library.loadSystem(java.lang.String,java.lang.String) throws java.lang.UnsatisfiedLinkError"""
        _Library.loadSystem(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def loadNative(arg0: 'Class', arg1: str, arg2: str) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.Library.loadNative(java.lang.Class<?>,java.lang.String,java.lang.String)"""
        return SharedLibrary._wrap(_Library.loadNative(arg0, arg1, arg2))

    @staticmethod
    @overload
    def loadNative(arg0: 'Class', arg1: str, arg2: 'Configuration', *arg3: str) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.Library.loadNative(java.lang.Class<?>,java.lang.String,org.lwjgl.system.Configuration<java.lang.String>,java.lang.String...)"""
        return SharedLibrary._wrap(_Library.loadNative(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

        @staticmethod
        @overload
        def initialize():
            """public static void org.lwjgl.system.Library.initialize()"""
            _Library.initialize()

    @staticmethod
    @overload
    def loadNative(arg0: 'Class', arg1: str, arg2: 'Configuration', arg3: 'Supplier', *arg4: str) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.Library.loadNative(java.lang.Class<?>,java.lang.String,org.lwjgl.system.Configuration<java.lang.String>,java.util.function.Supplier<org.lwjgl.system.SharedLibrary>,java.lang.String...)"""
        return SharedLibrary._wrap(_Library.loadNative(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def loadNative(arg0: str, arg1: str) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.Library.loadNative(java.lang.String,java.lang.String)"""
        return SharedLibrary._wrap(_Library.loadNative(arg0, arg1))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.Pointer
import org.lwjgl.system.Pointer as _Pointer
_Pointer = _Pointer
from abc import abstractmethod, ABC
 
class Pointer():
    """org.lwjgl.system.Pointer"""
 
    @staticmethod
    def _wrap(java_value: _Pointer) -> 'Pointer':
        return Pointer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pointer):
        """
        Dynamic initializer for Pointer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pointer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pointer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def address(self, ):
        """public abstract long org.lwjgl.system.Pointer.address()"""
        pass 
 
 
# CLASS: org.lwjgl.system.Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.lang.String as _String
_String = _String
import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Callback():
    """org.lwjgl.system.Callback"""
 
    @staticmethod
    def _wrap(java_value: _Callback) -> 'Callback':
        return Callback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Callback):
        """
        Dynamic initializer for Callback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Callback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Callback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(Callback, self).hashCode())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(Callback, self).free()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_Callback, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def get(arg0: int) -> 'CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

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
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(Callback, self).toString())

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(Callback, self).address())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(NativeResource, self).close()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.system.SharedLibrary$Delegate
from builtins import str
import org.lwjgl.system.SharedLibrary as _SharedLibrary_Delegate
_Delegate = _SharedLibrary_Delegate.Delegate
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.lwjgl.system.FunctionProvider as _FunctionProvider
_FunctionProvider = _FunctionProvider
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Delegate():
    """org.lwjgl.system.SharedLibrary.Delegate"""
 
    @staticmethod
    def _wrap(java_value: _Delegate) -> 'Delegate':
        return Delegate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Delegate):
        """
        Dynamic initializer for Delegate.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Delegate__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Delegate__wrapper":
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

    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int._wrap(super(_FunctionProvider, self).getFunctionAddress(arg0))

    @override
    @overload
    def getPath(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Delegate.getPath()"""
        return str._wrap(super(Delegate, self).getPath())

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
    def address(self) -> int:
        """public long org.lwjgl.system.SharedLibrary$Delegate.address()"""
        return int._wrap(super(Delegate, self).address())

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
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(NativeResource, self).close()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.SharedLibrary$Delegate.free()"""
        super(Delegate, self).free()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Delegate.getName()"""
        return str._wrap(super(Delegate, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass 
 
 
# CLASS: org.lwjgl.system.MemoryUtil$MemoryAllocator
import org.lwjgl.system.MemoryUtil as _MemoryUtil_MemoryAllocator
_MemoryAllocator = _MemoryUtil_MemoryAllocator.MemoryAllocator
from abc import abstractmethod, ABC
 
class MemoryAllocator():
    """org.lwjgl.system.MemoryUtil.MemoryAllocator"""
 
    @staticmethod
    def _wrap(java_value: _MemoryAllocator) -> 'MemoryAllocator':
        return MemoryAllocator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MemoryAllocator):
        """
        Dynamic initializer for MemoryAllocator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MemoryAllocator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MemoryAllocator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getAlignedFree(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getAlignedFree()"""
        pass

    @abstractmethod
    def getAlignedAlloc(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getAlignedAlloc()"""
        pass

    @abstractmethod
    def getCalloc(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getCalloc()"""
        pass

    @abstractmethod
    def realloc(self, arg0: int, arg1: int):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.realloc(long,long)"""
        pass

    @abstractmethod
    def getMalloc(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getMalloc()"""
        pass

    @abstractmethod
    def malloc(self, arg0: int):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.malloc(long)"""
        pass

    @abstractmethod
    def calloc(self, arg0: int, arg1: int):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.calloc(long,long)"""
        pass

    @abstractmethod
    def aligned_alloc(self, arg0: int, arg1: int):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.aligned_alloc(long,long)"""
        pass

    @abstractmethod
    def aligned_free(self, arg0: int):
        """public abstract void org.lwjgl.system.MemoryUtil$MemoryAllocator.aligned_free(long)"""
        pass

    @abstractmethod
    def getRealloc(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getRealloc()"""
        pass

    @abstractmethod
    def free(self, arg0: int):
        """public abstract void org.lwjgl.system.MemoryUtil$MemoryAllocator.free(long)"""
        pass

    @abstractmethod
    def getFree(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getFree()"""
        pass 
 
 
# CLASS: org.lwjgl.system.CheckIntrinsics
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.CheckIntrinsics as _CheckIntrinsics
_CheckIntrinsics = _CheckIntrinsics
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CheckIntrinsics():
    """org.lwjgl.system.CheckIntrinsics"""
 
    @staticmethod
    def _wrap(java_value: _CheckIntrinsics) -> 'CheckIntrinsics':
        return CheckIntrinsics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CheckIntrinsics):
        """
        Dynamic initializer for CheckIntrinsics.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CheckIntrinsics__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CheckIntrinsics__wrapper":
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
    def checkIndex(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.CheckIntrinsics.checkIndex(int,int)"""
        return int._wrap(_CheckIntrinsics.checkIndex(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def checkFromIndexSize(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.CheckIntrinsics.checkFromIndexSize(int,int,int)"""
        return int._wrap(_CheckIntrinsics.checkFromIndexSize(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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

    @staticmethod
    @overload
    def checkFromToIndex(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.CheckIntrinsics.checkFromToIndex(int,int,int)"""
        return int._wrap(_CheckIntrinsics.checkFromToIndex(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
 
 
# CLASS: org.lwjgl.system.Platform
from builtins import str
from pyquantum_helper import override
import org.lwjgl.system.Platform as _Platform_Architecture
_Architecture = _Platform_Architecture.Architecture
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import org.lwjgl.system.Platform as _Platform
_Platform = _Platform
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
 
class Platform():
    """org.lwjgl.system.Platform"""
 
    @staticmethod
    def _wrap(java_value: _Platform) -> 'Platform':
        return Platform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Platform):
        """
        Dynamic initializer for Platform.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Platform__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Platform__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Platform':
        """public static org.lwjgl.system.Platform org.lwjgl.system.Platform.valueOf(java.lang.String)"""
        return Platform._wrap(_Platform.valueOf(arg0))

    @staticmethod
    @overload
    def getArchitecture() -> 'Architecture':
        """public static org.lwjgl.system.Platform$Architecture org.lwjgl.system.Platform.getArchitecture()"""
        return Architecture._wrap(_Platform.getArchitecture())

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

    @staticmethod
    @overload
    def get() -> 'Platform':
        """public static org.lwjgl.system.Platform org.lwjgl.system.Platform.get()"""
        return Platform._wrap(_Platform.get())

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

    @staticmethod
    @overload
    def mapLibraryNameBundled(arg0: str) -> str:
        """public static java.lang.String org.lwjgl.system.Platform.mapLibraryNameBundled(java.lang.String)"""
        return str._wrap(_Platform.mapLibraryNameBundled(arg0))

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

    @overload
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.Platform.getName()"""
        return str._wrap(super(Platform, self).getName())

    @staticmethod
    @overload
    def values() -> List['Platform']:
        """public static org.lwjgl.system.Platform[] org.lwjgl.system.Platform.values()"""
        return List[Platform]._wrap(_Platform.values()) 
 
 
# CLASS: org.lwjgl.system.SharedLibrary
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import org.lwjgl.system.FunctionProvider as _FunctionProvider
_FunctionProvider = _FunctionProvider
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.system.Pointer as _Pointer
_Pointer = _Pointer
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
from abc import abstractmethod, ABC
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class SharedLibrary():
    """org.lwjgl.system.SharedLibrary"""
 
    @staticmethod
    def _wrap(java_value: _SharedLibrary) -> 'SharedLibrary':
        return SharedLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SharedLibrary):
        """
        Dynamic initializer for SharedLibrary.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SharedLibrary__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SharedLibrary__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String org.lwjgl.system.SharedLibrary.getName()"""
        pass

    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int._wrap(super(_FunctionProvider, self).getFunctionAddress(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(NativeResource, self).close()

    @abstractmethod
    def getPath(self, ):
        """public abstract java.lang.String org.lwjgl.system.SharedLibrary.getPath()"""
        pass

    @abstractmethod
    def free(self, ):
        """public abstract void org.lwjgl.system.NativeResource.free()"""
        pass

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass

    @abstractmethod
    def address(self, ):
        """public abstract long org.lwjgl.system.Pointer.address()"""
        pass 
 
 
# CLASS: org.lwjgl.system.Checks
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

import java.nio.IntBuffer as IntBuffer
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.nio.LongBuffer as LongBuffer
from builtins import object
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import java.lang.String as _string
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
import org.lwjgl.system.Checks as _Checks
_Checks = _Checks
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Checks():
    """org.lwjgl.system.Checks"""
 
    @staticmethod
    def _wrap(java_value: _Checks) -> 'Checks':
        return Checks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Checks):
        """
        Dynamic initializer for Checks.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Checks__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Checks__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def check(arg0: int) -> int:
        """public static long org.lwjgl.system.Checks.check(long)"""
        return int._wrap(_Checks.check(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def check(arg0: 'double', arg1: int):
        """public static void org.lwjgl.system.Checks.check(double[],int)"""
        _Checks.check(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkFunctions(arg0: 'FunctionProviderLocal', arg1: int, arg2: 'PointerBuffer', arg3: 'int', *arg4: str) -> bool:
        """public static boolean org.lwjgl.system.Checks.checkFunctions(org.lwjgl.system.FunctionProviderLocal,long,org.lwjgl.PointerBuffer,int[],java.lang.String...)"""
        return bool._wrap(_Checks.checkFunctions(arg0, _long.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'long'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(long[])"""
        _Checks.checkNTSafe(arg0)

    @staticmethod
    @overload
    def checkNT(arg0: 'long'):
        """public static void org.lwjgl.system.Checks.checkNT(long[])"""
        _Checks.checkNT(arg0)

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'LongBuffer'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(java.nio.LongBuffer)"""
        _Checks.checkNTSafe(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'int', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNTSafe(int[],int)"""
        _Checks.checkNTSafe(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'FloatBuffer'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(java.nio.FloatBuffer)"""
        _Checks.checkNTSafe(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def lengthSafe(arg0: 'double') -> int:
        """public static int org.lwjgl.system.Checks.lengthSafe(double[])"""
        return int._wrap(_Checks.lengthSafe(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def check(arg0: 'CharSequence', arg1: int):
        """public static void org.lwjgl.system.Checks.check(java.lang.CharSequence,int)"""
        _Checks.check(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkFunctions(*arg0: int) -> bool:
        """public static boolean org.lwjgl.system.Checks.checkFunctions(long...)"""
        return bool._wrap(_Checks.checkFunctions(arg0))

    @staticmethod
    @overload
    def checkFunctions(arg0: 'FunctionProvider', arg1: 'PointerBuffer', arg2: 'int', *arg3: str) -> bool:
        """public static boolean org.lwjgl.system.Checks.checkFunctions(org.lwjgl.system.FunctionProvider,org.lwjgl.PointerBuffer,int[],java.lang.String...)"""
        return bool._wrap(_Checks.checkFunctions(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def checkNT2Safe(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT2Safe(java.nio.ByteBuffer)"""
        _Checks.checkNT2Safe(arg0)

    @staticmethod
    @overload
    def checkFunctions(arg0: 'FunctionProvider', arg1: 'long', arg2: 'int', *arg3: str) -> bool:
        """public static boolean org.lwjgl.system.Checks.checkFunctions(org.lwjgl.system.FunctionProvider,long[],int[],java.lang.String...)"""
        return bool._wrap(_Checks.checkFunctions(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'PointerBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNTSafe(org.lwjgl.PointerBuffer,long)"""
        _Checks.checkNTSafe(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'float'):
        """public static void org.lwjgl.system.Checks.checkNT(float[])"""
        _Checks.checkNT(arg0)

    @staticmethod
    @overload
    def checkSafe(arg0: 'float', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(float[],int)"""
        _Checks.checkSafe(arg0, _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def checkNT2(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT2(java.nio.ByteBuffer)"""
        _Checks.checkNT2(arg0)

    @staticmethod
    @overload
    def check(arg0: 'CustomBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.check(org.lwjgl.system.CustomBuffer<?>,long)"""
        _Checks.check(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def checkSafe(arg0: 'CustomBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(org.lwjgl.system.CustomBuffer<?>,int)"""
        _Checks.checkSafe(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def check(arg0: 'short', arg1: int):
        """public static void org.lwjgl.system.Checks.check(short[],int)"""
        _Checks.check(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkGT(arg0: 'Buffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkGT(java.nio.Buffer,int)"""
        _Checks.checkGT(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def check(arg0: 'int', arg1: int):
        """public static void org.lwjgl.system.Checks.check(int[],int)"""
        _Checks.check(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkSafe(arg0: 'short', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(short[],int)"""
        _Checks.checkSafe(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'int'):
        """public static void org.lwjgl.system.Checks.checkNT(int[])"""
        _Checks.checkNT(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def checkNT(arg0: 'IntBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT(java.nio.IntBuffer)"""
        _Checks.checkNT(arg0)

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'IntBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNTSafe(java.nio.IntBuffer,int)"""
        _Checks.checkNTSafe(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkSafe(arg0: 'double', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(double[],int)"""
        _Checks.checkSafe(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'FloatBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT(java.nio.FloatBuffer)"""
        _Checks.checkNT(arg0)

    @staticmethod
    @overload
    def lengthSafe(arg0: 'long') -> int:
        """public static int org.lwjgl.system.Checks.lengthSafe(long[])"""
        return int._wrap(_Checks.lengthSafe(arg0))

    @staticmethod
    @overload
    def check(arg0: bytes, arg1: int):
        """public static void org.lwjgl.system.Checks.check(byte[],int)"""
        _Checks.check(bytes, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'PointerBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT(org.lwjgl.PointerBuffer)"""
        _Checks.checkNT(arg0)

    @staticmethod
    @overload
    def checkNT(arg0: 'int', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNT(int[],int)"""
        _Checks.checkNT(arg0, _int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'IntBuffer'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(java.nio.IntBuffer)"""
        _Checks.checkNTSafe(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def lengthSafe(arg0: 'int') -> int:
        """public static int org.lwjgl.system.Checks.lengthSafe(int[])"""
        return int._wrap(_Checks.lengthSafe(arg0))

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'float'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(float[])"""
        _Checks.checkNTSafe(arg0)

    @staticmethod
    @overload
    def checkNT1Safe(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT1Safe(java.nio.ByteBuffer)"""
        _Checks.checkNT1Safe(arg0)

    @staticmethod
    @overload
    def check(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.Checks.check(int,int)"""
        return int._wrap(_Checks.check(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def lengthSafe(arg0: 'float') -> int:
        """public static int org.lwjgl.system.Checks.lengthSafe(float[])"""
        return int._wrap(_Checks.lengthSafe(arg0))

    @staticmethod
    @overload
    def checkNT(arg0: 'LongBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT(java.nio.LongBuffer)"""
        _Checks.checkNT(arg0)

    @staticmethod
    @overload
    def checkSafe(arg0: 'long', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(long[],int)"""
        _Checks.checkSafe(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def lengthSafe(arg0: 'short') -> int:
        """public static int org.lwjgl.system.Checks.lengthSafe(short[])"""
        return int._wrap(_Checks.lengthSafe(arg0))

    @staticmethod
    @overload
    def reportMissing(arg0: str, arg1: str) -> bool:
        """public static boolean org.lwjgl.system.Checks.reportMissing(java.lang.String,java.lang.String)"""
        return bool._wrap(_Checks.reportMissing(arg0, arg1))

    @staticmethod
    @overload
    def check(arg0: 'Object', arg1: int):
        """public static void org.lwjgl.system.Checks.check(java.lang.Object[],int)"""
        _Checks.check(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkGT(arg0: 'CustomBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkGT(org.lwjgl.system.CustomBuffer<?>,int)"""
        _Checks.checkGT(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def check(arg0: 'Buffer', arg1: int):
        """public static void org.lwjgl.system.Checks.check(java.nio.Buffer,long)"""
        _Checks.check(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'PointerBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNT(org.lwjgl.PointerBuffer,long)"""
        _Checks.checkNT(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'IntBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNT(java.nio.IntBuffer,int)"""
        _Checks.checkNT(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def remainingSafe(arg0: 'Buffer') -> int:
        """public static int org.lwjgl.system.Checks.remainingSafe(java.nio.Buffer)"""
        return int._wrap(_Checks.remainingSafe(arg0))

    @staticmethod
    @overload
    def checkSafe(arg0: 'Buffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(java.nio.Buffer,int)"""
        _Checks.checkSafe(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def check(arg0: 'CustomBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.check(org.lwjgl.system.CustomBuffer<?>,int)"""
        _Checks.check(arg0, _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkSafe(arg0: 'int', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(int[],int)"""
        _Checks.checkSafe(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkSafe(arg0: 'Buffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(java.nio.Buffer,long)"""
        _Checks.checkSafe(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def check(arg0: 'long', arg1: int):
        """public static void org.lwjgl.system.Checks.check(long[],int)"""
        _Checks.check(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT1(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT1(java.nio.ByteBuffer)"""
        _Checks.checkNT1(arg0)

    @staticmethod
    @overload
    def check(arg0: 'Buffer', arg1: int):
        """public static void org.lwjgl.system.Checks.check(java.nio.Buffer,int)"""
        _Checks.check(arg0, _int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'int'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(int[])"""
        _Checks.checkNTSafe(arg0)

    @staticmethod
    @overload
    def remainingSafe(arg0: 'CustomBuffer') -> int:
        """public static int org.lwjgl.system.Checks.remainingSafe(org.lwjgl.system.CustomBuffer<?>)"""
        return int._wrap(_Checks.remainingSafe(arg0))

    @staticmethod
    @overload
    def checkSafe(arg0: 'CustomBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(org.lwjgl.system.CustomBuffer<?>,long)"""
        _Checks.checkSafe(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def check(arg0: 'float', arg1: int):
        """public static void org.lwjgl.system.Checks.check(float[],int)"""
        _Checks.check(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'PointerBuffer'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(org.lwjgl.PointerBuffer)"""
        _Checks.checkNTSafe(arg0) 
 
 
# CLASS: org.lwjgl.system.CustomBuffer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CustomBuffer():
    """org.lwjgl.system.CustomBuffer"""
 
    @staticmethod
    def _wrap(java_value: _CustomBuffer) -> 'CustomBuffer':
        return CustomBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CustomBuffer):
        """
        Dynamic initializer for CustomBuffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CustomBuffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CustomBuffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def limit(self, arg0: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'CustomBuffer'._wrap(super(_CustomBuffer, self).limit(_int.valueOf(arg0)))

    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(CustomBuffer, self).address0())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mark(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).mark())

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
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(CustomBuffer, self).free()

    @overload
    def slice(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).slice())

    @overload
    def rewind(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).rewind())

    @overload
    def duplicate(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).duplicate())

    @overload
    def compact(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).compact())

    @overload
    def position(self, arg0: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'CustomBuffer'._wrap(super(_CustomBuffer, self).position(_int.valueOf(arg0)))

    @overload
    def flip(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).flip())

    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(CustomBuffer, self).remaining())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def reset(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).reset())

    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(CustomBuffer, self).hasRemaining())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_CustomBuffer, self).address(_int.valueOf(arg0)))

    @overload
    def slice(self, arg0: int, arg1: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'CustomBuffer'._wrap(super(_CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(CustomBuffer, self).limit())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(CustomBuffer, self).address())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'CustomBuffer'._wrap(super(_CustomBuffer, self).put(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(Default, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(CustomBuffer, self).capacity())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_Default, self).equals(arg0))

    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(CustomBuffer, self).position())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def clear(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).clear())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(CustomBuffer, self).toString())

    @abstractmethod
    def sizeof(self, ):
        """public abstract int org.lwjgl.system.CustomBuffer.sizeof()"""
        pass 
 
 
# CLASS: org.lwjgl.system.FunctionProvider
import java.lang.CharSequence as CharSequence
import org.lwjgl.system.FunctionProvider as _FunctionProvider
_FunctionProvider = _FunctionProvider
import java.nio.ByteBuffer as ByteBuffer
from abc import abstractmethod, ABC
from builtins import int
 
class FunctionProvider():
    """org.lwjgl.system.FunctionProvider"""
 
    @staticmethod
    def _wrap(java_value: _FunctionProvider) -> 'FunctionProvider':
        return FunctionProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FunctionProvider):
        """
        Dynamic initializer for FunctionProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FunctionProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FunctionProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int._wrap(super(_FunctionProvider, self).getFunctionAddress(arg0))

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass 
 
 
# CLASS: org.lwjgl.system.SharedLibrary$Default
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
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Default():
    """org.lwjgl.system.SharedLibrary.Default"""
 
    @staticmethod
    def _wrap(java_value: _Default) -> 'Default':
        return Default(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Default):
        """
        Dynamic initializer for Default.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Default__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Default__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(Default, self).toString())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(Default, self).address())

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

    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int._wrap(super(_FunctionProvider, self).getFunctionAddress(arg0))

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
        return int._wrap(super(Default, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_Default, self).equals(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(NativeResource, self).close()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Default.getName()"""
        return str._wrap(super(Default, self).getName())

    @abstractmethod
    def getPath(self, ):
        """public abstract java.lang.String org.lwjgl.system.SharedLibrary.getPath()"""
        pass

    @abstractmethod
    def free(self, ):
        """public abstract void org.lwjgl.system.NativeResource.free()"""
        pass

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass 
 
 
# CLASS: org.lwjgl.system.NativeType
import org.lwjgl.system.NativeType as _NativeType
_NativeType = _NativeType
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class NativeType():
    """org.lwjgl.system.NativeType"""
 
    @staticmethod
    def _wrap(java_value: _NativeType) -> 'NativeType':
        return NativeType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NativeType):
        """
        Dynamic initializer for NativeType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NativeType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NativeType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def value(self, ):
        """public abstract java.lang.String org.lwjgl.system.NativeType.value()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.lwjgl.system.CallbackI
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
from abc import abstractmethod, ABC
from builtins import int
 
class CallbackI():
    """org.lwjgl.system.CallbackI"""
 
    @staticmethod
    def _wrap(java_value: _CallbackI) -> 'CallbackI':
        return CallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CallbackI):
        """
        Dynamic initializer for CallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(CallbackI, self).address())

    @abstractmethod
    def callback(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.system.CallbackI.callback(long,long)"""
        pass

    @abstractmethod
    def getCallInterface(self, ):
        """public abstract org.lwjgl.system.libffi.FFICIF org.lwjgl.system.CallbackI.getCallInterface()"""
        pass 
 
 
# CLASS: org.lwjgl.system.StructBuffer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Integer as _int
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StructBuffer():
    """org.lwjgl.system.StructBuffer"""
 
    @staticmethod
    def _wrap(java_value: _StructBuffer) -> 'StructBuffer':
        return StructBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StructBuffer):
        """
        Dynamic initializer for StructBuffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StructBuffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StructBuffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def flip(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).flip())

    @overload
    def limit(self, arg0: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'CustomBuffer'._wrap(super(_CustomBuffer, self).limit(_int.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).duplicate())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'StructBuffer'._wrap(super(_StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: 'Struct') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'StructBuffer'._wrap(super(_StructBuffer, self).put(arg0))

    @override
    @overload
    def reset(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).reset())

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
    def get(self) -> 'Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'Struct'._wrap(super(StructBuffer, self).get())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(CustomBuffer, self).limit())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(CustomBuffer, self).remaining())

    @override
    @overload
    def clear(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).clear())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(CustomBuffer, self).hasRemaining())

    @overload
    def apply(self, arg0: 'Consumer') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'StructBuffer'._wrap(super(_StructBuffer, self).apply(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_StructBuffer, self).forEach(arg0)

    @overload
    def position(self, arg0: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'CustomBuffer'._wrap(super(_CustomBuffer, self).position(_int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'Struct'._wrap(super(_StructBuffer, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def rewind(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).rewind())

    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(StructBuffer, self).stream())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int._wrap(super(StructBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(StructBuffer, self).iterator())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_CustomBuffer, self).address(_int.valueOf(arg0)))

    @overload
    def slice(self, arg0: int, arg1: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'CustomBuffer'._wrap(super(_CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(CustomBuffer, self).free()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(CustomBuffer, self).capacity())

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(CustomBuffer, self).address0())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(CustomBuffer, self).address())

    @override
    @overload
    def compact(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).compact())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'StructBuffer'._wrap(super(_StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'CustomBuffer'._wrap(super(_CustomBuffer, self).put(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(Default, self).hashCode())

    @override
    @overload
    def mark(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).mark())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(StructBuffer, self).spliterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_Default, self).equals(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'StructBuffer'._wrap(super(_StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(CustomBuffer, self).position())

    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(StructBuffer, self).parallelStream())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: 'Struct') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'StructBuffer'._wrap(super(_StructBuffer, self).get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(CustomBuffer, self).toString())

    @override
    @overload
    def slice(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'CustomBuffer'._wrap(super(CustomBuffer, self).slice()) 
 
 
# CLASS: org.lwjgl.system.MathUtil
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import org.lwjgl.system.MathUtil as _MathUtil
_MathUtil = _MathUtil
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MathUtil():
    """org.lwjgl.system.MathUtil"""
 
    @staticmethod
    def _wrap(java_value: _MathUtil) -> 'MathUtil':
        return MathUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MathUtil):
        """
        Dynamic initializer for MathUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MathUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MathUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def mathMultiplyHighU64(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MathUtil.mathMultiplyHighU64(long,long)"""
        return int._wrap(_MathUtil.mathMultiplyHighU64(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def mathHasZeroByte(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MathUtil.mathHasZeroByte(long)"""
        return bool._wrap(_MathUtil.mathHasZeroByte(_long.valueOf(arg0)))

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
    def mathDivideUnsigned(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MathUtil.mathDivideUnsigned(long,long)"""
        return int._wrap(_MathUtil.mathDivideUnsigned(_long.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def mathRemainderUnsigned(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MathUtil.mathRemainderUnsigned(long,long)"""
        return int._wrap(_MathUtil.mathRemainderUnsigned(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def mathRoundPoT(arg0: int) -> int:
        """public static int org.lwjgl.system.MathUtil.mathRoundPoT(int)"""
        return int._wrap(_MathUtil.mathRoundPoT(_int.valueOf(arg0)))

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
    def mathHasZeroShort(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MathUtil.mathHasZeroShort(long)"""
        return bool._wrap(_MathUtil.mathHasZeroShort(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def mathIsPoT(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MathUtil.mathIsPoT(int)"""
        return bool._wrap(_MathUtil.mathIsPoT(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mathHasZeroShort(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MathUtil.mathHasZeroShort(int)"""
        return bool._wrap(_MathUtil.mathHasZeroShort(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def mathMultiplyHighS64(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MathUtil.mathMultiplyHighS64(long,long)"""
        return int._wrap(_MathUtil.mathMultiplyHighS64(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def mathHasZeroByte(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MathUtil.mathHasZeroByte(int)"""
        return bool._wrap(_MathUtil.mathHasZeroByte(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.ThreadLocalUtil
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
from builtins import type
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
import java.lang.String as _String
_String = _String
import org.lwjgl.system.ThreadLocalUtil as _ThreadLocalUtil
_ThreadLocalUtil = _ThreadLocalUtil
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ThreadLocalUtil():
    """org.lwjgl.system.ThreadLocalUtil"""
 
    @staticmethod
    def _wrap(java_value: _ThreadLocalUtil) -> 'ThreadLocalUtil':
        return ThreadLocalUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadLocalUtil):
        """
        Dynamic initializer for ThreadLocalUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadLocalUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadLocalUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def setFunctionMissingAddresses(arg0: int):
        """public static void org.lwjgl.system.ThreadLocalUtil.setFunctionMissingAddresses(int)"""
        _ThreadLocalUtil.setFunctionMissingAddresses(_int.valueOf(arg0))

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
    def areCapabilitiesDifferent(arg0: 'PointerBuffer', arg1: 'PointerBuffer') -> bool:
        """public static boolean org.lwjgl.system.ThreadLocalUtil.areCapabilitiesDifferent(org.lwjgl.PointerBuffer,org.lwjgl.PointerBuffer)"""
        return bool._wrap(_ThreadLocalUtil.areCapabilitiesDifferent(arg0, arg1))

    @staticmethod
    @overload
    def setupEnvData() -> int:
        """public static long org.lwjgl.system.ThreadLocalUtil.setupEnvData()"""
        return int._wrap(_ThreadLocalUtil.setupEnvData())

    @staticmethod
    @overload
    def setupAddressBuffer(arg0: 'PointerBuffer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.ThreadLocalUtil.setupAddressBuffer(org.lwjgl.PointerBuffer)"""
        return pygl.PointerBuffer._wrap(_ThreadLocalUtil.setupAddressBuffer(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def setCapabilities(arg0: int):
        """public static void org.lwjgl.system.ThreadLocalUtil.setCapabilities(long)"""
        _ThreadLocalUtil.setCapabilities(_long.valueOf(arg0))

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
 
 
# CLASS: org.lwjgl.system.Platform$Architecture
from builtins import str
from pyquantum_helper import override
import org.lwjgl.system.Platform as _Platform_Architecture
_Architecture = _Platform_Architecture.Architecture
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
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
 
class Architecture():
    """org.lwjgl.system.Platform.Architecture"""
 
    @staticmethod
    def _wrap(java_value: _Architecture) -> 'Architecture':
        return Architecture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Architecture):
        """
        Dynamic initializer for Architecture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Architecture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Architecture__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Architecture':
        """public static org.lwjgl.system.Platform$Architecture org.lwjgl.system.Platform$Architecture.valueOf(java.lang.String)"""
        return Architecture._wrap(_Architecture.valueOf(arg0))

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
    def values() -> List['Architecture']:
        """public static org.lwjgl.system.Platform$Architecture[] org.lwjgl.system.Platform$Architecture.values()"""
        return List[Architecture]._wrap(_Architecture.values()) 
 
 
# CLASS: org.lwjgl.system.Struct$Member
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.lwjgl.system.Struct as _Struct_Member
_Member = _Struct_Member.Member
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Member():
    """org.lwjgl.system.Struct.Member"""
 
    @staticmethod
    def _wrap(java_value: _Member) -> 'Member':
        return Member(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Member):
        """
        Dynamic initializer for Member.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Member__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Member__wrapper":
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

    @overload
    def getAlignment(self) -> int:
        """public int org.lwjgl.system.Struct$Member.getAlignment()"""
        return int._wrap(super(Member, self).getAlignment())

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

    @overload
    def getAlignment(self, arg0: int) -> int:
        """public int org.lwjgl.system.Struct$Member.getAlignment(int)"""
        return int._wrap(super(_Member, self).getAlignment(_int.valueOf(arg0)))

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
    def getSize(self) -> int:
        """public int org.lwjgl.system.Struct$Member.getSize()"""
        return int._wrap(super(Member, self).getSize())

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
 
 
# CLASS: org.lwjgl.system.Configuration
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.Configuration as _Configuration
_Configuration = _Configuration
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Configuration():
    """org.lwjgl.system.Configuration"""
 
    @staticmethod
    def _wrap(java_value: _Configuration) -> 'Configuration':
        return Configuration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Configuration):
        """
        Dynamic initializer for Configuration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Configuration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Configuration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: object) -> object:
        """public T org.lwjgl.system.Configuration.get(T)"""
        return object._wrap(super(_Configuration, self).get(arg0))

    @overload
    def getProperty(self) -> str:
        """public java.lang.String org.lwjgl.system.Configuration.getProperty()"""
        return str._wrap(super(Configuration, self).getProperty())

    @overload
    def get(self) -> object:
        """public T org.lwjgl.system.Configuration.get()"""
        return object._wrap(super(Configuration, self).get())

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

    @overload
    def set(self, arg0: object):
        """public void org.lwjgl.system.Configuration.set(T)"""
        super(_Configuration, self).set(arg0)

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
 
 
# CLASS: org.lwjgl.system.NonnullDefault
import org.lwjgl.system.NonnullDefault as _NonnullDefault
_NonnullDefault = _NonnullDefault
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class NonnullDefault():
    """org.lwjgl.system.NonnullDefault"""
 
    @staticmethod
    def _wrap(java_value: _NonnullDefault) -> 'NonnullDefault':
        return NonnullDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NonnullDefault):
        """
        Dynamic initializer for NonnullDefault.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NonnullDefault__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NonnullDefault__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.lwjgl.system.SharedLibraryUtil
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.SharedLibraryUtil as _SharedLibraryUtil
_SharedLibraryUtil = _SharedLibraryUtil
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SharedLibraryUtil():
    """org.lwjgl.system.SharedLibraryUtil"""
 
    @staticmethod
    def _wrap(java_value: _SharedLibraryUtil) -> 'SharedLibraryUtil':
        return SharedLibraryUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SharedLibraryUtil):
        """
        Dynamic initializer for SharedLibraryUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SharedLibraryUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SharedLibraryUtil__wrapper":
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

    @overload
    def __init__(self):
        """public org.lwjgl.system.SharedLibraryUtil()"""
        val = _SharedLibraryUtil()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.lwjgl.system.SharedLibraryUtil()"""
        val = _SharedLibraryUtil()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getLibraryPath(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.SharedLibraryUtil.getLibraryPath(long)"""
        return str._wrap(_SharedLibraryUtil.getLibraryPath(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.JNI
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import org.lwjgl.system.JNI as _JNI
_JNI = _JNI
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JNI():
    """org.lwjgl.system.JNI"""
 
    @staticmethod
    def _wrap(java_value: _JNI) -> 'JNI':
        return JNI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JNI):
        """
        Dynamic initializer for JNI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JNI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JNI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(int,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPP(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,int,long,int,long)"""
        return int._wrap(_JNI.callPJJI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,float,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: 'long', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,long[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: 'int', arg2: int, arg3: 'int', arg4: int, arg5: bool, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(int,int[],int,int[],int,boolean,long)"""
        return int._wrap(_JNI.invokePPI(_int.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, _int.valueOf(arg4), _boolean.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePP(arg0: 'double', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(double[],int,long)"""
        return int._wrap(_JNI.invokePP(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,long,long,int,long,long)"""
        _JNI.callPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: 'int', arg13: 'int', arg14: int, arg15: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPPPI(long,long,long,long,long,long,long,long,long,long,long,int,int[],int[],long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _int.valueOf(arg11), arg12, arg13, _long.valueOf(arg14), _long.valueOf(arg15)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int[],long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeJV(long,int,long)"""
        _JNI.invokeJV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,int,long,long,long,long)"""
        _JNI.callPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,int,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,long,long)"""
        _JNI.callPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPPI(long,int,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPJPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int[],long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,long,int,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeCC(arg0: int, arg1: bool, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCC(short,boolean,long)"""
        return int._wrap(_JNI.invokeCC(_short.valueOf(arg0), _boolean.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: 'int', arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPP(long,long,long,long,long,long,int[],int[],long)"""
        return int._wrap(_JNI.callPJPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), arg6, arg7, _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'short', arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), arg10, _long.valueOf(arg11))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,long,int,long)"""
        _JNI.callPJV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callJPV(int,int,long,long,long)"""
        _JNI.callJPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int[],int[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,boolean,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _boolean.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callJJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callJJV(int,long,long,long)"""
        _JNI.callJJV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,int,int,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNI(long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPNI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,long,int,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePNPNN(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNPNN(long,long,long,long,long)"""
        return int._wrap(_JNI.invokePNPNN(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,int,long,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,long,long)"""
        _JNI.callPJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,long,long,long,long,int,long)"""
        _JNI.callPPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePNI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNI(long,long,long)"""
        return int._wrap(_JNI.invokePNI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,long,int,int,int,long)"""
        _JNI.callPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPBPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPBPPP(long,long,byte,long,long,long)"""
        return int._wrap(_JNI.invokePPBPPP(_long.valueOf(arg0), _long.valueOf(arg1), _byte.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],long[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPS(long,long,short,long,long)"""
        return int._wrap(_JNI.callPPSPS(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: 'int', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int[],long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJJI(long,long,long,long,long)"""
        return int._wrap(_JNI.callPJJJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPI(long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPJPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: 'int', arg6: 'int', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(int,int,long,int[],int[],int[],int[],long)"""
        _JNI.callPPPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, arg4, arg5, arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,int,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'long', arg6: int, arg7: 'int', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,int,long,int,int,long[],int,int[],long)"""
        _JNI.callPJPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _int.valueOf(arg6), arg7, _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokeCPUI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPUI(short,long,byte,long)"""
        return int._wrap(_JNI.invokeCPUI(_short.valueOf(arg0), _long.valueOf(arg1), _byte.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,long,int,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def callPJPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPPI(long,int,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPJPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,long,long)"""
        _JNI.callJV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePF(arg0: int, arg1: int, arg2: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePF(long,int,long)"""
        return float._wrap(_JNI.invokePF(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int,long,int,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPP(long,int,long,long,long,int[],int[],long)"""
        return int._wrap(_JNI.callPPPPPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, arg6, _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,int,int,long,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: float, arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,long,int,int,float,int[],long)"""
        return int._wrap(_JNI.callPPI(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPNV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPNV(long,long,long,long,long)"""
        _JNI.callPPPNV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callJJ(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callJJ(long,long)"""
        return int._wrap(_JNI.callJJ(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,int,boolean,int,long,long)"""
        _JNI.callJV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _boolean.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def callJ(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callJ(int,int,boolean,int,int,long)"""
        return int._wrap(_JNI.callJ(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeNN(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeNN(long,long)"""
        return int._wrap(_JNI.invokeNN(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,int[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeCCCUJP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeCCCUJP(short,short,short,byte,int,long,long)"""
        return int._wrap(_JNI.invokeCCCUJP(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _byte.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: float, arg10: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,long,int,int,float,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _float.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: float, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,float,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int, arg6: 'int', arg7: 'int', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int,int[],int,int[],int[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), arg6, arg7, _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPJPPI(long,int,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPJPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokeCPUI(arg0: int, arg1: 'int', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPUI(short,int[],byte,long)"""
        return int._wrap(_JNI.invokeCPUI(_short.valueOf(arg0), arg1, _byte.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,int,long,long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,int,int,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long,int,int,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,short,long)"""
        _JNI.invokePCV(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPPNJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNJI(long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPNJI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,int,int,long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int,int,long,long)"""
        return int._wrap(_JNI.callPPP(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePZ(long,int,long)"""
        return bool._wrap(_JNI.invokePZ(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long,int,int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'float', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,int,float[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7, _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: 'int', arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,long,long,long,long,int,int[],int[],long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), arg7, arg8, _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callV(arg0: bool, arg1: int):
        """public static native void org.lwjgl.system.JNI.callV(boolean,long)"""
        _JNI.callV(_boolean.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'int', arg12: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11, _long.valueOf(arg12))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(double,double,long)"""
        _JNI.callV(_double.valueOf(arg0), _double.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,int,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeCC(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCC(int,short,long)"""
        return int._wrap(_JNI.invokeCC(_int.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callS(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.JNI.callS(int,long)"""
        return int._wrap(_JNI.callS(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int[],long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,long,long)"""
        _JNI.callJV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(int,int,int,int,int,long,long,long,long)"""
        return int._wrap(_JNI.callJPPI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,long,int[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPPPPPPI(long,long,long,long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callJPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCCCUV(long,short,short,short,short,short,int,byte,long)"""
        _JNI.invokePCCCCCUV(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _short.valueOf(arg5), _int.valueOf(arg6), _byte.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPPNNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNNI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPNNI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,long,long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float,float,int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePNPN(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNPN(long,long,long,long)"""
        return int._wrap(_JNI.invokePNPN(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,int,long,int,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'long', arg5: 'long', arg6: 'long', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,int,long[],long[],long[],long[],long)"""
        _JNI.callPPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5, arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeCPPV(arg0: int, arg1: 'float', arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPPV(short,float[],float[],long)"""
        _JNI.invokeCPPV(_short.valueOf(arg0), arg1, arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callI(arg0: int) -> int:
        """public static native int org.lwjgl.system.JNI.callI(long)"""
        return int._wrap(_JNI.callI(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,long,int,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePD(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokePD(long,int,int,long)"""
        return float._wrap(_JNI.invokePD(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(long,int,int,int,long)"""
        return int._wrap(_JNI.invokePI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,int,long,int,int,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,int[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePF(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePF(long,int,int,long)"""
        return float._wrap(_JNI.invokePF(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: float, arg2: float, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,float,float,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callSPSPPPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native short org.lwjgl.system.JNI.callSPSPPPSPS(short,long,short,long,long,long,short,long,long)"""
        return int._wrap(_JNI.callSPSPPPSPS(_short.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _short.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(long,int,boolean,long)"""
        return int._wrap(_JNI.callJI(_long.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPJPP(long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPJPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'short', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],int,long,int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPPJJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJJPPPPPPP(long,long,long,long,long,int,long,int,long,int,long,long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPJJPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11), _int.valueOf(arg12), _long.valueOf(arg13), _long.valueOf(arg14), _long.valueOf(arg15), _long.valueOf(arg16), _long.valueOf(arg17)))

    @staticmethod
    @overload
    def invokePPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: 'float', arg7: 'int', arg8: 'int', arg9: 'int', arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPPPI(long,int,int,long,int[],int[],float[],int[],int[],int[],long)"""
        return int._wrap(_JNI.invokePPPPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, arg6, arg7, arg8, arg9, _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,short[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,int,long,int[],long)"""
        return int._wrap(_JNI.callPJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,long)"""
        _JNI.callPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,int,long,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int,int,int,int,int[],long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long,long[],long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: float, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,int,int,int,float,long,long)"""
        _JNI.invokePPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,int,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,long,int,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,int,long,int,long,int,long)"""
        return int._wrap(_JNI.callJPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPJJJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callPPJJJJJJV(long,long,long,long,int,long,long,long,long,long)"""
        _JNI.callPPJJJJJJV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int[],long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,int,int,int[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,long,int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPUPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPUPI(long,byte,long,long)"""
        return int._wrap(_JNI.callPUPI(_long.valueOf(arg0), _byte.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,long,int,long)"""
        return int._wrap(_JNI.callJPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'int', arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), arg10, _long.valueOf(arg11))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,short[],int,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), arg1, _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPV(arg0: 'int', arg1: 'int', arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int[],int[],int[],long)"""
        _JNI.invokePPPV(arg0, arg1, arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPP(long,long,int,int,int,int[],long)"""
        return int._wrap(_JNI.callPJPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePNPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNPI(long,long,long,long)"""
        return int._wrap(_JNI.invokePNPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long[],long,int,int[],long)"""
        return int._wrap(_JNI.callPPPPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'short', arg7: 'int', arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPP(long,long,long,long,long,long,short[],int[],long)"""
        return int._wrap(_JNI.callPJPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), arg6, arg7, _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,int,int,int,int,int,int,int,int,long)"""
        _JNI.callPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _long.valueOf(arg11))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,int,int,long,int[],long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), arg6, _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPCV(long,int,short,long)"""
        _JNI.callPCV(_long.valueOf(arg0), _int.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int, arg19: int, arg20: int, arg21: int, arg22: int, arg23: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(int,long,long,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16), _int.valueOf(arg17), _int.valueOf(arg18), _int.valueOf(arg19), _int.valueOf(arg20), _long.valueOf(arg21), _long.valueOf(arg22), _long.valueOf(arg23)))

    @staticmethod
    @overload
    def callPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPI(long,long,long,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPV(arg0: 'int', arg1: 'int', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int[],int[],long)"""
        _JNI.callPPV(arg0, arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJPPP(long,int,long,long,long,long,int,int,long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPJPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11), _long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,int,long)"""
        _JNI.callPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: int):
        """public static native void org.lwjgl.system.JNI.callV(double,long)"""
        _JNI.callV(_double.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeJC(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeJC(int,int,long,long)"""
        return int._wrap(_JNI.invokeJC(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNPI(long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPNPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPI(long,int,int,long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokeP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeP(int,int,long)"""
        return int._wrap(_JNI.invokeP(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,long,long)"""
        _JNI.callPJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,double,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'double', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,double[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,int,int,long,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,int,long,long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeC(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeC(int,long)"""
        return int._wrap(_JNI.invokeC(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJJV(long,long,long,int,long)"""
        _JNI.callPJJV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: 'int', arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,long,int[],long,long,int,int[],int[],long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), arg7, arg8, _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,float[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,long,int,long,int,long,int,long,long)"""
        _JNI.invokePPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,long,int,int,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,long,int,long)"""
        return int._wrap(_JNI.callPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeCCUV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUV(short,short,int,float,byte,long)"""
        _JNI.invokeCCUV(_short.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _byte.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int[],int[],int[],long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), arg1, arg2, arg3, _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,float,float,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,long,int[],long)"""
        return int._wrap(_JNI.callPJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: bool, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int[],boolean,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _boolean.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(int,int,int,int,long,int,long,long)"""
        return int._wrap(_JNI.invokePPP(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,long,long,int,long)"""
        return int._wrap(_JNI.callJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,int,int,int,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,short,int,int,long)"""
        _JNI.invokePCV(_long.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,int,long,int[],long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'int', arg9: 'int', arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPPPP(long,long,long,long,long,long,long,long,int[],int[],long)"""
        return int._wrap(_JNI.callPJPPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), arg8, arg9, _long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPP(long,long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,int[],int[],int[],int[],int[],long)"""
        return int._wrap(_JNI.callPPPPPPI(_long.valueOf(arg0), arg1, arg2, arg3, arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,long,int,int,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,int,int,short,long)"""
        _JNI.invokePCV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: float, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,long,int,int,float,long,long)"""
        return int._wrap(_JNI.callPPI(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPP(long,long,long,int,long)"""
        return int._wrap(_JNI.callPJPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,int,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: float, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,float,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,int,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPSPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPSPS(long,long,short,long,short,long,long)"""
        return int._wrap(_JNI.callPPSPSPS(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(float,float,float,long)"""
        _JNI.callV(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,float,float,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int[],int[],long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,long,long,long,int,long,long,int,long)"""
        return int._wrap(_JNI.callPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,long,long)"""
        _JNI.callJV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPNI(long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPNI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: 'double', arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,double[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,int,int,int,int,long,int,long,int,long,long)"""
        _JNI.callPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,long,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,boolean,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,long,int,long,long,long,long)"""
        _JNI.callPPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePNNPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNNPP(long,long,long,long,long)"""
        return int._wrap(_JNI.invokePNNPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callJV(long,int,long)"""
        _JNI.callJV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(double,double,double,double,double,double,long)"""
        _JNI.callV(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _double.valueOf(arg4), _double.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,long[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: bool, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(float,boolean,long)"""
        _JNI.callV(_float.valueOf(arg0), _boolean.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _double.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(int,long,int[],long)"""
        return int._wrap(_JNI.callPPP(_int.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,int,int,int,int,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(int,long,int,long,long,long,int,long,int,boolean,long)"""
        _JNI.invokePPPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _boolean.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'double', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int,long,long)"""
        return int._wrap(_JNI.callPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPJI(long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callBBBBV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callBBBBV(byte,byte,byte,byte,long)"""
        _JNI.callBBBBV(_byte.valueOf(arg0), _byte.valueOf(arg1), _byte.valueOf(arg2), _byte.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'short', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,int,long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,long,long,long,long)"""
        _JNI.invokePPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,long,int,long)"""
        _JNI.callPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPPZ(long,int,long,long,long,long)"""
        return bool._wrap(_JNI.invokePPPPZ(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,boolean,int,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _boolean.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int[],int,int,int,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeUPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeUPV(byte,long,long)"""
        _JNI.invokeUPV(_byte.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPCPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPCPPV(long,long,short,long,long,long)"""
        _JNI.invokePPCPPV(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,boolean,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _boolean.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPJJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,int,long)"""
        return int._wrap(_JNI.invokePP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,long,long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],int[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), arg1, arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePCCUV(long,short,short,int,byte,long)"""
        _JNI.invokePCCUV(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _byte.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,long[],long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callCV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callCV(int,short,long)"""
        _JNI.callCV(_int.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int[],long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'double', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,double[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,int,int,long,int,long,long)"""
        return int._wrap(_JNI.callPPI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNPI(long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPNPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,long[],long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,float,long,int,int,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: float, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,long,int,int,int,int,float,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _float.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'float', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7, _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPS(long,int,long,int,long)"""
        return int._wrap(_JNI.callPPS(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,long[],int[],int[],long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePP(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(int[],int,long)"""
        return int._wrap(_JNI.invokePP(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeZ(arg0: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokeZ(long)"""
        return bool._wrap(_JNI.invokeZ(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(int,long,long,long)"""
        return int._wrap(_JNI.callPPP(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callSSSV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callSSSV(short,short,short,long)"""
        _JNI.callSSSV(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,long)"""
        _JNI.invokeV(_int.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def invokeCV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokeCV(short,long)"""
        _JNI.invokeCV(_short.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int,long,int[],long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeJ(arg0: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeJ(long)"""
        return int._wrap(_JNI.invokeJ(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def invokePPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPPI(long,long,long,int,long,float,float,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokeCCJZ(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokeCCJZ(short,boolean,short,int,long,long)"""
        return bool._wrap(_JNI.invokeCCJZ(_short.valueOf(arg0), _boolean.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeF(arg0: int, arg1: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokeF(int,long)"""
        return float._wrap(_JNI.invokeF(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,long,int,int,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int,int[],int[],long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: bool, arg12: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,int,int,int,int,int,long,boolean,long)"""
        _JNI.callJV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _boolean.valueOf(arg11), _long.valueOf(arg12))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,boolean,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPZ(long,long,long,int,long)"""
        return bool._wrap(_JNI.invokePPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,int,long,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: 'float', arg2: 'float', arg3: 'float', arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,float[],float[],float[],long)"""
        _JNI.invokePPPV(_int.valueOf(arg0), arg1, arg2, arg3, _long.valueOf(arg4))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def invokePPPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPNI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPNI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,long,long[],long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,int,long,int,long,int,int,long)"""
        return int._wrap(_JNI.invokePPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePPNNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNNI(long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPNNI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPP(long,long,long,long,long,int[],long)"""
        return int._wrap(_JNI.callPJPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'long', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int,long[],long[],long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,long,long,int,long)"""
        return int._wrap(_JNI.callPPJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,int,long,long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPI(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int[],long,long)"""
        return int._wrap(_JNI.callPPI(arg0, _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,float,long)"""
        _JNI.invokeV(_int.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(long,int,long)"""
        return int._wrap(_JNI.invokePI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,float,long,long)"""
        _JNI.callPPV(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,long,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'int', arg9: 'int', arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPI(long,long,long,long,long,long,long,int,int[],int[],long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), arg8, arg9, _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePUCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePUCV(long,byte,short,int,int,long)"""
        _JNI.invokePUCV(_long.valueOf(arg0), _byte.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: 'int', arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int[],long)"""
        return int._wrap(_JNI.callPI(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,float,float,float,long)"""
        _JNI.invokeV(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: 'short', arg2: int, arg3: 'short', arg4: int, arg5: bool, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(int,short[],int,short[],int,boolean,long)"""
        return int._wrap(_JNI.invokePPI(_int.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, _int.valueOf(arg4), _boolean.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,long,int,long,int,long)"""
        return int._wrap(_JNI.invokePPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,float,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPNNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNNPI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPNNPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,long[],long)"""
        _JNI.callPJJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeUV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokeUV(byte,long)"""
        _JNI.invokeUV(_byte.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: float, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,int,long,long,int,int,int,int,float,long)"""
        return int._wrap(_JNI.callPPI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _float.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPCV(long,long,int,long,short,long)"""
        _JNI.invokePPPCV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPZ(long,long,int,long,int,boolean,long)"""
        return bool._wrap(_JNI.invokePPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(int,int,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,long,long)"""
        _JNI.invokePV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,double,double,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _double.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,long,long)"""
        _JNI.callPJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,long,int,int,int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: 'int', arg2: 'float', arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int[],float[],int,int[],int[],long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callJPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPJI(long,int,long,int,long,long)"""
        return int._wrap(_JNI.callJPJI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPI(long,int,long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,int,int,long,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,float,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: float, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,float,int,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPJV(long,int,long,int,long,int,long)"""
        _JNI.callPPJV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,int,long,long)"""
        _JNI.callJV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'short', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,long,long,int,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,int,int,int,long)"""
        _JNI.callPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'int', arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPPPP(long,long,long,long,long,long,long,long,long,int[],long)"""
        return int._wrap(_JNI.callPJPPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), arg9, _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,int,long,int,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokeCV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeCV(int,short,long)"""
        _JNI.invokeCV(_int.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,int,long,long,long)"""
        return int._wrap(_JNI.callPPI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPCCPSPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCCPSPPS(long,short,short,long,short,long,long,long)"""
        return int._wrap(_JNI.callPCCPSPPS(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJJPI(long,long,long,long,int,long,long)"""
        return int._wrap(_JNI.callPJJJPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,long,long,long,long,long)"""
        _JNI.invokePPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long[],long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPSSSPSSPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSSSPSSPPPS(long,short,short,short,long,short,short,long,long,long,long)"""
        return int._wrap(_JNI.callPSSSPSSPPPS(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4), _short.valueOf(arg5), _short.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'float', arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,int,long,long,long,long,float[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), arg7, _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def callUV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.callUV(byte,long)"""
        _JNI.callUV(_byte.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,long,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,float,float,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: bool, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,boolean,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _boolean.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokeCCCCPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCCPCV(short,short,short,short,long,short,long)"""
        _JNI.invokeCCCCPCV(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4), _short.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,long,long)"""
        return int._wrap(_JNI.callPJJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: 'double', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,double,double,int,int,double,double,int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _double.valueOf(arg5), _double.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), arg9, _long.valueOf(arg10))

    @staticmethod
    @overload
    def invokePCC(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePCC(long,int,short,long)"""
        return int._wrap(_JNI.invokePCC(_long.valueOf(arg0), _int.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUV(short,short,int,byte,long)"""
        _JNI.invokeCCUV(_short.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _byte.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,int[],long)"""
        _JNI.callPJJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: 'long', arg2: 'int', arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long[],int[],long)"""
        return int._wrap(_JNI.callPPPP(_long.valueOf(arg0), arg1, arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJJV(long,long,long,long)"""
        _JNI.callPJJV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeP(arg0: bool, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeP(boolean,long)"""
        return int._wrap(_JNI.invokeP(_boolean.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPPI(int,int,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callJPPPPI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,int,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPJPPI(long,long,long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,int,int,int,long,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,long,int,long,long)"""
        return int._wrap(_JNI.callPJPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,boolean,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(int,int,long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPJJI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPJJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def callPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJI(long,int,int,long,long)"""
        return int._wrap(_JNI.callPJI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPP(long,long,long,long,float[],int[],long)"""
        return int._wrap(_JNI.callPJPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPPPV(long,int,long,long,long,long,long,long,long)"""
        _JNI.invokePPPPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePNPNPN(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNPNPN(long,long,int,int,int,int,int,int,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePNPNPN(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11), _long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: bool, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,boolean,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPPZ(long,long,long,long,long)"""
        return bool._wrap(_JNI.invokePPPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePUV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePUV(long,byte,long)"""
        _JNI.invokePUV(_long.valueOf(arg0), _byte.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokeCPP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeCPP(short,long,long)"""
        return int._wrap(_JNI.invokeCPP(_short.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,float,float,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeCPI(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPI(short,int[],long)"""
        return int._wrap(_JNI.invokeCPI(_short.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: bool, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,boolean,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _boolean.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callJZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callJZ(int,long,long)"""
        return bool._wrap(_JNI.callJZ(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeCCUPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUPPV(short,short,byte,long,long,long)"""
        _JNI.invokeCCUPPV(_short.valueOf(arg0), _short.valueOf(arg1), _byte.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,float[],long)"""
        _JNI.callPJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,int,long,int,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPNV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPNV(long,long,long,long)"""
        _JNI.callPPNV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJJPI(long,long,long,int,long)"""
        return int._wrap(_JNI.callJJPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPNN(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPNN(long,int,int,long,long,long)"""
        return int._wrap(_JNI.invokePPNN(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(int,int,int,long,long,long)"""
        _JNI.invokePPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(int,long,long,long)"""
        return int._wrap(_JNI.invokePPP(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCCCUV(short,short,short,short,short,byte,long)"""
        _JNI.invokeCCCCCUV(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _byte.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPCPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPSPS(long,short,long,short,long,long)"""
        return int._wrap(_JNI.callPCPSPS(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'float', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8, _long.valueOf(arg9))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,long,int[],long,long)"""
        _JNI.callPJPPV(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeCJC(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCJC(int,boolean,short,int,long,long)"""
        return int._wrap(_JNI.invokeCJC(_int.valueOf(arg0), _boolean.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,boolean,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: bool, arg9: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,boolean,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _boolean.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,int,int,int,int,int,int,long,int,int,int,int,int,int,int,int,int,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16), _int.valueOf(arg17), _long.valueOf(arg18))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,boolean,long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,int,int,long,long,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,double,long)"""
        _JNI.invokeV(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,long,int,int,int,long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,int,long,int,long)"""
        return int._wrap(_JNI.invokePPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,int,int,long,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int,int,int,long,long)"""
        return int._wrap(_JNI.callPPP(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPJJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPJJPPP(long,long,long,long,int,long,int,long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPPJJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.callV(int,long)"""
        _JNI.callV(_int.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int,long,long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeUPC(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeUPC(byte,long,boolean,long)"""
        return int._wrap(_JNI.invokeUPC(_byte.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeI(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(int,long)"""
        return int._wrap(_JNI.invokeI(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,float,float,float,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPP(long,long,long,long,long,long,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(int,int,int,int,long,long,long)"""
        return int._wrap(_JNI.invokePPP(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCCJPC(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCJPC(short,boolean,short,int,long,long,long)"""
        return int._wrap(_JNI.invokeCCJPC(_short.valueOf(arg0), _boolean.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,int,long,long,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,long[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: 'short', arg1: int):
        """public static native void org.lwjgl.system.JNI.callPV(short[],long)"""
        _JNI.callPV(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def invokeCV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeCV(short,int,long)"""
        _JNI.invokeCV(_short.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPNNP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPNNP(long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPNNP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPJV(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPJV(long,int,long[],int,long,int,long)"""
        _JNI.callPPJV(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPJP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPJP(long,long,long,long,int,int,long)"""
        return int._wrap(_JNI.invokePPPJP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPCPPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPPPPS(long,short,long,long,long,long,long)"""
        return int._wrap(_JNI.callPCPPPPS(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,int,int,long,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'double', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: 'int', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int[],int,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,int,int,long,int[],long)"""
        return int._wrap(_JNI.callPJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,long,int,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(long,int,int,long)"""
        return int._wrap(_JNI.callPP(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJJ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJ(long,long,int,int,long)"""
        return int._wrap(_JNI.callPJJ(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(int,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPI(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,long,int[],long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,int,int[],long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'long', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,long[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,int,long,long,long,long)"""
        _JNI.invokePPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'int', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), arg9, _long.valueOf(arg10))

    @staticmethod
    @overload
    def invokeCPCC(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCPCC(short,long,short,long)"""
        return int._wrap(_JNI.invokeCPCC(_short.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int,long,long)"""
        return int._wrap(_JNI.callPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPNP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPNP(long,long,long)"""
        return int._wrap(_JNI.callPNP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int[],long)"""
        return int._wrap(_JNI.callPPPP(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,int,long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,int,int,float[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePJI(long,long,int,long)"""
        return int._wrap(_JNI.invokePJI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: 'short', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,short[],short,long)"""
        _JNI.invokePCPCV(_long.valueOf(arg0), _short.valueOf(arg1), arg2, _short.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,long,int,long[],long)"""
        return int._wrap(_JNI.callPJPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPCPS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPS(long,short,long,long)"""
        return int._wrap(_JNI.callPCPS(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,long,short,long)"""
        _JNI.invokePCPCV(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,long,int[],long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,long,int,int,int,int[],long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJPPPI(long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPJJPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPJPPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPP(long,long[],long,long,long,int[],int[],long)"""
        return int._wrap(_JNI.callPPJPPPPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, arg6, _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,int,long,int,long,int,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,long,long)"""
        _JNI.callPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPF(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.callPF(int,int,long,long)"""
        return float._wrap(_JNI.callPF(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,int,long,int,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePJ(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJ(long,long)"""
        return int._wrap(_JNI.invokePJ(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int,float[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPP(long,long,long,long,int,long,long)"""
        return int._wrap(_JNI.callPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callP(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callP(int,float,float,float,long)"""
        return int._wrap(_JNI.callP(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeCI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCI(int,short,long)"""
        return int._wrap(_JNI.invokeCI(_int.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,int,long,int[],long,long,long)"""
        _JNI.invokePPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,long,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPCS(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCS(long,short,long)"""
        return int._wrap(_JNI.callPCS(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeUPC(arg0: int, arg1: 'short', arg2: bool, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeUPC(byte,short[],boolean,long)"""
        return int._wrap(_JNI.invokeUPC(_byte.valueOf(arg0), arg1, _boolean.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPNPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNPPI(long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPNPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,long,int,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePNPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePNPPV(long,long,long,long,long)"""
        _JNI.invokePNPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePNP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNP(long,long,long)"""
        return int._wrap(_JNI.invokePNP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,int,int,int[],long)"""
        _JNI.callPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callJPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callJPPZ(long,long,long,long)"""
        return bool._wrap(_JNI.callJPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callJJV(int,int,long,long,long)"""
        _JNI.callJJV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPCPSPSPSCCS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPSPSPSCCS(long,short,long,short,long,short,long,short,short,short,long)"""
        return int._wrap(_JNI.callPCPSPSPSCCS(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4), _short.valueOf(arg5), _long.valueOf(arg6), _short.valueOf(arg7), _short.valueOf(arg8), _short.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePD(arg0: int, arg1: int, arg2: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokePD(long,int,long)"""
        return float._wrap(_JNI.invokePD(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'float', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,float[],int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), arg2, _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,long,int,int,long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'float', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), arg9, _long.valueOf(arg10))

    @staticmethod
    @overload
    def invokeCPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPPV(short,long,long,long)"""
        _JNI.invokeCPPV(_short.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPJI(long,long,long,long)"""
        return int._wrap(_JNI.invokePPJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPP(long,long,long,long,int[],int[],long)"""
        return int._wrap(_JNI.callPJPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJJJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJJJPI(long,long,long,long,long,int[],long)"""
        return int._wrap(_JNI.callPJJJJPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPJPPP(long,long,long,int,int,long,long,long)"""
        return int._wrap(_JNI.invokePPJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,int,int,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,long,long,long)"""
        _JNI.callPJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,int[],long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeD(arg0: int, arg1: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokeD(int,long)"""
        return float._wrap(_JNI.invokeD(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,long,int,int,int,long)"""
        return int._wrap(_JNI.invokePPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,long,int,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPP(long,int,long,long,long,int[],long)"""
        return int._wrap(_JNI.callPPPPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'int', arg9: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPPP(long,int,long,long,int,long,long,long,int[],long)"""
        return int._wrap(_JNI.callPPPPPPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), arg8, _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPJPPPPPI(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPPPPI(long,long[],long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPJPPPPPI(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: 'float', arg3: 'float', arg4: 'float', arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,int,float[],float[],float[],long)"""
        _JNI.invokePPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,int,long,int,long)"""
        _JNI.callPJV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,float[],long)"""
        _JNI.callPJJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,int[],long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePZ(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePZ(long,long)"""
        return bool._wrap(_JNI.invokePZ(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,int,long,int,long,long)"""
        return int._wrap(_JNI.callPPJI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,float,float,float,float,float,float,float,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _long.valueOf(arg11))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,int,long,int,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,long,int,long,long)"""
        return int._wrap(_JNI.callJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPZ(arg0: int, arg1: 'int', arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPZ(long,int[],long)"""
        return bool._wrap(_JNI.invokePPZ(_long.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'short', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,short[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: float, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,float,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _long.valueOf(arg11), _long.valueOf(arg12))

    @staticmethod
    @overload
    def callPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPP(long,long,int,long,long)"""
        return int._wrap(_JNI.callPJPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,int,int,int,int,long)"""
        _JNI.callPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPP(long,long,long,long,int,long,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,float,float,int,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,int,int[],long)"""
        _JNI.callPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,long,long[],long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,long,long,int,int,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,int,int,long,int,long,long,int,int,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,float,float,float,float,float,float,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'float', arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,int,long,long,long,long,long,long,long,float[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), arg10, _int.valueOf(arg11), _long.valueOf(arg12), _long.valueOf(arg13), _long.valueOf(arg14)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,int,int[],int[],long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'int', arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int[],int,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPP(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,long)"""
        _JNI.invokeV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int[],long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePNV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePNV(long,long,long)"""
        _JNI.invokePNV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,int,long,int,long,long)"""
        _JNI.callPJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJV(long,long,long,int,int,long)"""
        _JNI.callPJJV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPJPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,int,long,long,long,long)"""
        _JNI.callPJJPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,int,int,float[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,int,int,int,long)"""
        return int._wrap(_JNI.invokePP(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,boolean,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,int[],long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,float,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,double,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _double.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPJPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPI(long,long,long,int[],long,long)"""
        return int._wrap(_JNI.callPPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(float,float,long)"""
        _JNI.callV(_float.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: float, arg2: int, arg3: float, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,float,int,float,int,long)"""
        return int._wrap(_JNI.invokePP(_long.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeUCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeUCUV(byte,short,byte,int,int,long)"""
        _JNI.invokeUCUV(_byte.valueOf(arg0), _short.valueOf(arg1), _byte.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPV(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(float[],int,long,long,int,long)"""
        _JNI.invokePPPV(arg0, _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,int,int,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def callPJPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'float', arg9: 'int', arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPPPP(long,long,long,long,long,long,long,long,float[],int[],long)"""
        return int._wrap(_JNI.callPJPPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), arg8, arg9, _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPCPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPCPI(long,short,long,long)"""
        return int._wrap(_JNI.callPCPI(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,int,int,long)"""
        _JNI.callPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJV(int,long,int,long,long)"""
        _JNI.callPJV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(float,float,float,float,long)"""
        _JNI.callV(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPPPPPPI(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'int', arg10: 'int', arg11: int, arg12: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPI(long,long,long[],long,int,long,long,long,int,int[],int[],long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), arg9, arg10, _long.valueOf(arg11), _long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,short[],long)"""
        _JNI.callPJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,long,long)"""
        return int._wrap(_JNI.invokePPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int[],int[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPPPV(long,long,long,long,long,long,long,long)"""
        _JNI.invokePPPPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,double,double,double,long)"""
        _JNI.invokeV(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _double.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callUUUUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callUUUUV(byte,byte,byte,byte,long)"""
        _JNI.callUUUUV(_byte.valueOf(arg0), _byte.valueOf(arg1), _byte.valueOf(arg2), _byte.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePJV(long,int,long,long)"""
        _JNI.invokePJV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,long,int,int,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPJPPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPP(long,long[],long,long,long,float[],int[],long)"""
        return int._wrap(_JNI.callPPJPPPPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, arg6, _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,float,float,int,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callJ(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callJ(int,long)"""
        return int._wrap(_JNI.callJ(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int):
        """public static native void org.lwjgl.system.JNI.callV(float,float,float,float,float,float,float,float,long)"""
        _JNI.callV(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: 'long', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],long[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), arg1, arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int,int,long,long)"""
        return int._wrap(_JNI.callPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,float,float,float,float,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(int,long,int,int,long)"""
        return int._wrap(_JNI.callJI(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,long,long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePCC(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePCC(long,short,long)"""
        return int._wrap(_JNI.invokePCC(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,long,int,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,float,float,long,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,double,int,double,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _int.valueOf(arg3), _double.valueOf(arg4), _double.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,int,long,int,int,long,long)"""
        _JNI.callPJPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: 'long', arg2: 'long', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long[],long[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), arg1, arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'float', arg12: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11, _long.valueOf(arg12))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,int,long,int[],long)"""
        return int._wrap(_JNI.callPJPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,int,int,int,int,int,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,float,float,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(double,double,double,double,long)"""
        _JNI.callV(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJI(long,long,long)"""
        return int._wrap(_JNI.callPJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7, _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPP(long,long,long,long,short[],int[],long)"""
        return int._wrap(_JNI.callPJPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'int', arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,long,long[],int[],long,long)"""
        _JNI.callPPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, arg4, _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callJPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPJI(long,int,int,int,long,int,long,boolean,long,long)"""
        return int._wrap(_JNI.callJPPJI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _boolean.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPJ(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJ(long,long)"""
        return int._wrap(_JNI.callPJ(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'short', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), arg9, _long.valueOf(arg10))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'float', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,long,int,int,float[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7, _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,int,int,boolean,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],long,int,int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int[],int,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,int,int,long,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: 'float', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,float[],short,long)"""
        _JNI.invokePCPCV(_long.valueOf(arg0), _short.valueOf(arg1), arg2, _short.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(int,long,int,long,int,boolean,long)"""
        return int._wrap(_JNI.invokePPI(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,long,long)"""
        return int._wrap(_JNI.callPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,boolean,int,long,long)"""
        _JNI.callJV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'double', arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,int,long,long,long,long,long,long,long,double[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), arg10, _int.valueOf(arg11), _long.valueOf(arg12), _long.valueOf(arg13), _long.valueOf(arg14)))

    @staticmethod
    @overload
    def invokePPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPP(long,long,long,long,long,long,long,int,long,int,int,int,int,int,long)"""
        return int._wrap(_JNI.invokePPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _long.valueOf(arg14)))

    @staticmethod
    @overload
    def callJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callJJJV(int,long,long,long,long)"""
        _JNI.callJJJV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callSPPS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callSPPS(short,long,long,long)"""
        return int._wrap(_JNI.callSPPS(_short.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,float,float,float,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPI(long,long,long,long,long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPJPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPP(long,long,int,int[],long)"""
        return int._wrap(_JNI.callPJPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,short,int,int,int,long)"""
        _JNI.invokePCV(_long.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'double', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,double[],long)"""
        _JNI.callPJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'float', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPSSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSSPS(long,short,short,long,int,long)"""
        return int._wrap(_JNI.callPSSPS(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPZ(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPZ(long,long,long,boolean,int,long)"""
        return bool._wrap(_JNI.invokePPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeNNN(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeNNN(long,long,long)"""
        return int._wrap(_JNI.invokeNNN(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,float,float,float,int,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callSV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callSV(int,short,long)"""
        _JNI.callSV(_int.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callJ(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callJ(int,int,long)"""
        return int._wrap(_JNI.callJ(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: 'double', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,double[],short,long)"""
        _JNI.invokePCPCV(_long.valueOf(arg0), _short.valueOf(arg1), arg2, _short.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,int,long,long,int,long)"""
        return int._wrap(_JNI.callPJPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callCCCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callCCCV(short,short,short,long)"""
        _JNI.callCCCV(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long,boolean,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _boolean.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePNNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNPI(long,long,int,long,long,long)"""
        return int._wrap(_JNI.invokePNNPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int,int,int,int[],long)"""
        return int._wrap(_JNI.callPPP(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,float,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPI(long,int,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPJPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: 'int', arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(int,int[],long,long)"""
        return bool._wrap(_JNI.callPPZ(_int.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'int', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int[],int,long)"""
        _JNI.callPV(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,int,long,int,int,long,int,long,long)"""
        _JNI.callPJPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePUCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePUCCV(long,byte,short,short,int,long)"""
        _JNI.invokePUCCV(_long.valueOf(arg0), _byte.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPI(long,long,int,long,long,long)"""
        return int._wrap(_JNI.callJPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeI(arg0: int, arg1: bool, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(int,boolean,long)"""
        return int._wrap(_JNI.invokeI(_int.valueOf(arg0), _boolean.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,long,long,long,long)"""
        _JNI.callPJPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPSSPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSSPPS(long,short,short,long,int,long,long)"""
        return int._wrap(_JNI.callPSSPPS(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,int,int[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,long,int,int,int,long)"""
        return int._wrap(_JNI.callPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,long,int,int,long,long)"""
        return int._wrap(_JNI.callJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,int,long,int,long,int,int,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePN(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePN(long,int,long)"""
        return int._wrap(_JNI.invokePN(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int[],long,long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPS(long,long,int,long)"""
        return int._wrap(_JNI.callPPS(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,float,float,float,float,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPPPPPP(arg0: int, arg1: 'int', arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'int', arg12: 'long', arg13: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPPP(int,int[],long[],int,int,int,int,long,long,long,int,int[],long[],long)"""
        return int._wrap(_JNI.callPPPPPPPP(_int.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _int.valueOf(arg10), arg11, arg12, _long.valueOf(arg13)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,int,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,long,int[],long)"""
        return int._wrap(_JNI.callPJPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'float', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float[],long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int[],int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,int,int,int,long,long)"""
        return int._wrap(_JNI.invokePPP(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,int[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,int,int,long,long)"""
        _JNI.callPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPI(long,long,int,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,int,long,long,int,long)"""
        return int._wrap(_JNI.callJPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,int[],int[],long)"""
        return int._wrap(_JNI.callPJJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'double', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,double[],int[],long)"""
        return int._wrap(_JNI.callPJJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPN(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPN(long,long)"""
        return int._wrap(_JNI.callPN(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPJPPI(long,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(float,float,float,float,float,boolean,long)"""
        _JNI.callV(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _boolean.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int,int[],long)"""
        return int._wrap(_JNI.callPPP(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,float,float,float,long)"""
        _JNI.callPV(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int[],long)"""
        _JNI.callPPV(_long.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPCC(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePPCC(long,long,short,long)"""
        return int._wrap(_JNI.invokePPCC(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,long[],long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: float, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,long,int,int,float,int,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPNI(long,int,long,long,long)"""
        return int._wrap(_JNI.callPPNI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,float,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPN(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPN(long,long,long)"""
        return int._wrap(_JNI.invokePPN(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPUPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPUPZ(long,long,long,byte,long,long)"""
        return bool._wrap(_JNI.invokePPPUPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _byte.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPV(arg0: 'long', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long[],int[],int[],int[],int,long)"""
        _JNI.callPPPPV(arg0, arg1, arg2, arg3, _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,int,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,double,double,int,int,double,double,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _double.valueOf(arg5), _double.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,int[],int[],int[],long,long)"""
        return int._wrap(_JNI.invokePPPPPI(_long.valueOf(arg0), arg1, arg2, arg3, _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _long.valueOf(arg15))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,long,long)"""
        _JNI.invokePPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'short', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7, _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],int[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPJ(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPJ(long,long,long)"""
        return int._wrap(_JNI.invokePPJ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long,int,long,long)"""
        return int._wrap(_JNI.callPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: 'int', arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,long,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPPPZ(long,long,long,long,long,int,long)"""
        return bool._wrap(_JNI.invokePPPPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: 'double', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,double[],short,long)"""
        _JNI.invokeCPCV(_short.valueOf(arg0), arg1, _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,long)"""
        _JNI.callPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,float[],int[],long)"""
        return int._wrap(_JNI.callPJJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callF(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.callF(int,int,int,long)"""
        return float._wrap(_JNI.callF(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(int,long,long)"""
        return bool._wrap(_JNI.callPZ(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,int,int,boolean,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callJZ(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callJZ(long,long)"""
        return bool._wrap(_JNI.callJZ(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(long,long)"""
        return int._wrap(_JNI.invokePI(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,long,int,long,int,long,long)"""
        _JNI.callPJPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeCCV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeCCV(short,short,long)"""
        _JNI.invokeCCV(_short.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,float,float,long,long)"""
        _JNI.invokePPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,int[],long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,long,int,int,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,int,int,long,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,long,long,int,int,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJCCS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPJCCS(long,long,short,short,long)"""
        return int._wrap(_JNI.callPJCCS(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,long,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float,float,int,int,float,float,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,float,float,float,float,long,long)"""
        _JNI.invokePPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePNNPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: 'int', arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNPPPI(long,long,long,int,int,int[],int[],long,long)"""
        return int._wrap(_JNI.invokePNNPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, arg6, _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePUPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePUPCV(long,byte,long,int,int,short,long)"""
        _JNI.invokePUPCV(_long.valueOf(arg0), _byte.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _short.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,float[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'double', arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int,double[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'long', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int[],int[],long[],long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePC(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePC(long,long)"""
        return int._wrap(_JNI.invokePC(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPJPPP(long,long,long,long,long,int[],long)"""
        return int._wrap(_JNI.callPPPJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,int,long,int,int,long,int,long)"""
        _JNI.callPJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'short', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8, _long.valueOf(arg9))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,int,int[],long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int[],long,long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeJJJV(int,int,long,long,long,long)"""
        _JNI.invokeJJJV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: 'int', arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,int,int,int[],int[],int[],long,long)"""
        _JNI.callPPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5, _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePJP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJP(long,long,long)"""
        return int._wrap(_JNI.invokePJP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callSSV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callSSV(short,short,long)"""
        _JNI.callSSV(_short.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPPPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int, arg7: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPPPZ(long,long,long,long,long,boolean,int,long)"""
        return bool._wrap(_JNI.invokePPPPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _boolean.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokeI(arg0: bool, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(boolean,long)"""
        return int._wrap(_JNI.invokeI(_boolean.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,double,double,double,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _double.valueOf(arg3), _double.valueOf(arg4), _double.valueOf(arg5), _double.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callSV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.callSV(short,long)"""
        _JNI.callSV(_short.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPPPPP(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPP(long,long,long[],long,int,int[],long)"""
        return int._wrap(_JNI.callPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,int,int,long,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,int[],long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callJZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callJZ(int,long,int,long)"""
        return bool._wrap(_JNI.callJZ(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPI(arg0: 'int', arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(int[],long,int[],long)"""
        return int._wrap(_JNI.callPPPI(arg0, _long.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: 'int', arg1: int):
        """public static native void org.lwjgl.system.JNI.callPV(int[],long)"""
        _JNI.callPV(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'double', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,double[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'short', arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,int,long,long,long,long,long,long,long,short[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), arg10, _int.valueOf(arg11), _long.valueOf(arg12), _long.valueOf(arg13), _long.valueOf(arg14)))

    @staticmethod
    @overload
    def invokeCCUCCCCPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUCCCCPCV(short,short,byte,short,short,short,short,long,short,long)"""
        _JNI.invokeCCUCCCCPCV(_short.valueOf(arg0), _short.valueOf(arg1), _byte.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _short.valueOf(arg5), _short.valueOf(arg6), _long.valueOf(arg7), _short.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: 'long', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,long[],short,long)"""
        _JNI.invokeCPCV(_short.valueOf(arg0), arg1, _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long[],int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), arg2, _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(int,long,long,long)"""
        return bool._wrap(_JNI.callPPZ(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,int,int,long,long,long)"""
        return int._wrap(_JNI.callPPI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,int[],int,int[],long)"""
        return int._wrap(_JNI.callPJPPP(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: bool, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(int,boolean,long)"""
        _JNI.callV(_int.valueOf(arg0), _boolean.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,float,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePUV(long,int,int,byte,long)"""
        _JNI.invokePUV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _byte.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePJJPV(long,int,long,long,long,long)"""
        _JNI.invokePJJPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,int,long,int[],long)"""
        return int._wrap(_JNI.callPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPP(long,long,long,long,long,int,long,int,long,int,long)"""
        return int._wrap(_JNI.invokePPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePPPPPJJJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJJJPP(long,long,long,long,long,int,long,long,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPPJJJPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,long,long)"""
        return int._wrap(_JNI.callJPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,long,int,long)"""
        return int._wrap(_JNI.callPJJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callI(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.callI(int,long)"""
        return int._wrap(_JNI.callI(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float,float,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,int,int,long,long,long)"""
        return int._wrap(_JNI.callPJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPV(short,long,int,long)"""
        _JNI.invokeCPV(_short.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callJPJI(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPJI(long,int,float,long,int,long,long)"""
        return int._wrap(_JNI.callJPJI(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePJPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJPJPP(long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePJPJPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,long,float,long)"""
        return int._wrap(_JNI.callPJJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeI(arg0: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(long)"""
        return int._wrap(_JNI.invokeI(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def invokePCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePCCUV(long,short,short,int,int,int,byte,long)"""
        _JNI.invokePCCUV(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _byte.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,int,float[],long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int,int,int[],long)"""
        return int._wrap(_JNI.callPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePSSCCPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePSSCCPP(long,short,short,short,short,long,long)"""
        return int._wrap(_JNI.invokePSSCCPP(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,long,int,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callSPSS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callSPSS(short,long,short,long)"""
        return int._wrap(_JNI.callSPSS(_short.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int[],int[],long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJV(long,int,long,long,int,long)"""
        _JNI.callPJJV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,long,boolean,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _boolean.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int,int[],int[],long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPI(long,long,long,long,int,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,long,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,boolean,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,int,int,long,int[],long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), arg6, _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'float', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,float[],long)"""
        _JNI.callPPV(_long.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJV(long,long,long,long,int,long)"""
        _JNI.callPJJJV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,int,int[],long,long)"""
        return int._wrap(_JNI.callPPPP(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(long,long,int,long)"""
        return bool._wrap(_JNI.callPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,long,int,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,float,float,int,int,long,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'double', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int,long[],long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJ(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJ(int,int,long,long)"""
        return int._wrap(_JNI.callPJ(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,float,float,int,float,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,float,int,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJI(long,int,long,long)"""
        return int._wrap(_JNI.callPJI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,long,long,long)"""
        return int._wrap(_JNI.callPPJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: 'float', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePCI(arg0: 'float', arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePCI(float[],short,long)"""
        return int._wrap(_JNI.invokePCI(arg0, _short.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPV(arg0: 'float', arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(float[],boolean,int,long,long,int,long)"""
        _JNI.invokePPPV(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'double', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPJP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPJP(int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPJP(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callP(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callP(int,long)"""
        return int._wrap(_JNI.callP(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokeCV(arg0: int, arg1: bool, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeCV(short,boolean,long)"""
        _JNI.invokeCV(_short.valueOf(arg0), _boolean.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,int,long,long,long)"""
        return int._wrap(_JNI.callPPJI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPJ(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJ(long,int,long,long)"""
        return int._wrap(_JNI.callPPJ(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPJPP(long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPJPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPJI(long,long,int,int,long,int[],long,int,long)"""
        return int._wrap(_JNI.callPJPPJI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), arg5, _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,int,long,long,long,long,long)"""
        _JNI.invokePPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'long', arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPJI(long,long,int,int,long,long[],long,int,long)"""
        return int._wrap(_JNI.callPJPPJI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), arg5, _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,long,int,long,long)"""
        return int._wrap(_JNI.callPPJI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int,long,long[],long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePJV(long,long,long)"""
        _JNI.invokePJV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeUV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeUV(byte,int,long)"""
        _JNI.invokeUV(_byte.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokeD(arg0: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokeD(long)"""
        return float._wrap(_JNI.invokeD(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callF(arg0: int) -> float:
        """public static native float org.lwjgl.system.JNI.callF(long)"""
        return float._wrap(_JNI.callF(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callJJI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJJI(long,long,long)"""
        return int._wrap(_JNI.callJJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'long', arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJPPPI(long,long,long,int,long,long,long[],long)"""
        return int._wrap(_JNI.callPJJPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), arg6, _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,float[],int,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), arg1, _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(int,int,int,long,int,long,boolean,long,long)"""
        return int._wrap(_JNI.callPPJI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _boolean.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callP(arg0: int) -> int:
        """public static native long org.lwjgl.system.JNI.callP(long)"""
        return int._wrap(_JNI.callP(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: 'long', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,int,long,int,int,int[],long[],long)"""
        _JNI.callPJPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,int,long,long,int,int,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(int,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,long,short,long)"""
        _JNI.invokeCPCV(_short.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,boolean,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,short[],short,long)"""
        _JNI.invokeCPCV(_short.valueOf(arg0), arg1, _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,long[],short,long)"""
        _JNI.invokePCPCV(_long.valueOf(arg0), _short.valueOf(arg1), arg2, _short.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,int,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePP(arg0: 'short', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(short[],int,long)"""
        return int._wrap(_JNI.invokePP(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],int[],int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callI(int,int,int,long)"""
        return int._wrap(_JNI.callI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,int,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePSV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePSV(long,int,int,short,long)"""
        _JNI.invokePSV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,long,int,int,int,long,int,long,int,long,long)"""
        _JNI.callPPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: 'double', arg2: 'double', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,double[],double[],long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), arg1, arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeUCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeUCCV(byte,short,short,int,long)"""
        _JNI.invokeUCCV(_byte.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'double', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7, _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: 'long', arg3: 'long', arg4: 'long', arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,int,long[],long[],long[],long)"""
        _JNI.invokePPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'long', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,long[],long)"""
        _JNI.callPV(_int.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePP(arg0: 'float', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(float[],int,long)"""
        return int._wrap(_JNI.invokePP(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,short[],long)"""
        _JNI.callPJJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int,long,int,long)"""
        return int._wrap(_JNI.callPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPZ(arg0: int, arg1: int, arg2: int, arg3: float, arg4: 'float', arg5: 'float', arg6: 'float', arg7: 'float', arg8: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPPPZ(int,int,int,float,float[],float[],float[],float[],long)"""
        return bool._wrap(_JNI.callPPPPZ(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4, arg5, arg6, arg7, _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPUP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPUP(long,long,int,byte,long)"""
        return int._wrap(_JNI.invokePPUP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _byte.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(int,long,long)"""
        return int._wrap(_JNI.callPP(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPPI(long,long,long,int,int,long,long,int,long,int,long,int,long)"""
        return int._wrap(_JNI.invokePPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _int.valueOf(arg11), _long.valueOf(arg12)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,int,long,int,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long,int[],long)"""
        return int._wrap(_JNI.callPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,boolean,boolean,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int,int,int,int,long,long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,int,long,long,long)"""
        return int._wrap(_JNI.callPJPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(int,float,float,long,long)"""
        return bool._wrap(_JNI.callPZ(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callZ(arg0: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(long)"""
        return bool._wrap(_JNI.callZ(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,int,int,int,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int,long,long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,int,int[],long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: 'double', arg1: 'double', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(double[],double[],long)"""
        _JNI.callPPV(arg0, arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,boolean,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,float,float,float,float,float,float,long,long)"""
        _JNI.invokePPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: 'int', arg2: 'int', arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int[],int[],int,int[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,long,int,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPP(long,long,int,int,int,long,long)"""
        return int._wrap(_JNI.callPJPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCCUUUUUUUUUV(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUUUUUUUUUV(short,short,float,byte,byte,byte,byte,byte,byte,byte,byte,byte,long)"""
        _JNI.invokeCCUUUUUUUUUV(_short.valueOf(arg0), _short.valueOf(arg1), _float.valueOf(arg2), _byte.valueOf(arg3), _byte.valueOf(arg4), _byte.valueOf(arg5), _byte.valueOf(arg6), _byte.valueOf(arg7), _byte.valueOf(arg8), _byte.valueOf(arg9), _byte.valueOf(arg10), _byte.valueOf(arg11), _long.valueOf(arg12))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,int,int[],int[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,int,long,int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPSS(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSS(long,short,long)"""
        return int._wrap(_JNI.callPSS(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,int,long,int[],long,long)"""
        _JNI.callPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeCPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeCPP(int,short,long,long)"""
        return int._wrap(_JNI.invokeCPP(_int.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(long,int,boolean,long)"""
        return int._wrap(_JNI.invokePI(_long.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPI(long,long,long,long,int,long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11), _long.valueOf(arg12)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(int,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,double,double,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,float,float,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,int[],int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), arg2, _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPF(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePPF(long,float,long,int,long)"""
        return float._wrap(_JNI.invokePPF(_long.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,int,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,long,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,boolean,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: int, arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],int,int[],int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePJV(int,long,long,long)"""
        _JNI.invokePJV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPJ(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPJ(long,long,int,long)"""
        return int._wrap(_JNI.invokePPJ(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,int,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int,int[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,int,long,long)"""
        return int._wrap(_JNI.callJPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callP(int,int,long)"""
        return int._wrap(_JNI.callP(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPSPSPPPPPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSPSPPPPPPPS(long,short,long,short,long,long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPSPSPPPPPPPS(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokeP(arg0: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeP(long)"""
        return int._wrap(_JNI.invokeP(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def invokePPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPZ(long,long,long,long)"""
        return bool._wrap(_JNI.invokePPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,int[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: float, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,long,int,int,int,float,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,int,long,int,int,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(long,int,long)"""
        return bool._wrap(_JNI.callPZ(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long,int,int,int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePJPV(long,long,long,int,long)"""
        _JNI.invokePJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeCCCJPC(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCCJPC(short,short,boolean,short,int,long,long,long)"""
        return int._wrap(_JNI.invokeCCCJPC(_short.valueOf(arg0), _short.valueOf(arg1), _boolean.valueOf(arg2), _short.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePNI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNI(long,long,int,long)"""
        return int._wrap(_JNI.invokePNI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPPV(long,long,long,int,int,long,long,long,long)"""
        _JNI.callPPPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPPS(long,int,long,int,long,long)"""
        return int._wrap(_JNI.callPPPS(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callNV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callNV(long,int,int,int,long)"""
        _JNI.callNV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(int,long,int,long)"""
        return bool._wrap(_JNI.callPZ(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(int,int,long)"""
        return bool._wrap(_JNI.callZ(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'double', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,double[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,int,long[],long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,int,int,long,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokeI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(int,int,long)"""
        return int._wrap(_JNI.invokeI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: float, arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,int,int,int,int,int,float,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _float.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,int,int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(int,long,long,int,long)"""
        return int._wrap(_JNI.callPPP(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,int,int,int,int,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePUCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePUCCV(long,byte,short,int,int,short,long)"""
        _JNI.invokePUCCV(_long.valueOf(arg0), _byte.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _short.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callJJI(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJJI(long,float,float,float,float,long,long)"""
        return int._wrap(_JNI.callJJI(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCCCUV(short,short,short,short,short,int,byte,long)"""
        _JNI.invokeCCCCCUV(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _int.valueOf(arg5), _byte.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,long,boolean,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _boolean.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJPPP(long,long,long,long,long,int,long,int,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPPJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(long,int,long)"""
        return int._wrap(_JNI.callPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,int,long,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callSSSSV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callSSSSV(int,short,short,short,short,long)"""
        _JNI.callSSSSV(_int.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCV(short,short,short,int,long)"""
        _JNI.invokeCCCV(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callJJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJJPPI(long,long,long,long,long)"""
        return int._wrap(_JNI.callJJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,long,int,int,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,long,int[],int[],int[],int,long)"""
        _JNI.callPPPPV(_int.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, arg4, _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPPJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJPPPP(long,long,long,long,long,int,long,int,int,long,int,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _long.valueOf(arg12), _long.valueOf(arg13), _long.valueOf(arg14)))

    @staticmethod
    @overload
    def invokeCPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeCPV(short,long,long)"""
        _JNI.invokeCPV(_short.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,long,long,int,int,long)"""
        return int._wrap(_JNI.callJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,int,int,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,int,int[],int[],long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeUPU(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native byte org.lwjgl.system.JNI.invokeUPU(byte,int[],long)"""
        return int._wrap(_JNI.invokeUPU(_byte.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePNI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNI(long,int,long,long)"""
        return int._wrap(_JNI.invokePNI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPNI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNI(long,long,long,long)"""
        return int._wrap(_JNI.invokePPNI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(long,long)"""
        return int._wrap(_JNI.callJI(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callJJJJV(int,int,long,long,long,long,long)"""
        _JNI.callJJJJV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callCCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callCCCCV(short,short,short,short,long)"""
        _JNI.callCCCCV(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeJV(int,int,long,long)"""
        _JNI.invokeJV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'long', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'double', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), arg9, _long.valueOf(arg10))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'float', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,int,int,float[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8, _long.valueOf(arg9))

    @staticmethod
    @overload
    def invokePPF(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePPF(long,int,long,long)"""
        return float._wrap(_JNI.invokePPF(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPI(long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPJPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: 'double', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,double[],int[],long)"""
        return int._wrap(_JNI.callPJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,double,double,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _double.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: 'int', arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int[],int,int[],int[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), arg4, arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callZ(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(int,int,float,float,long)"""
        return bool._wrap(_JNI.callZ(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePCP(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePCP(long,short,boolean,long)"""
        return int._wrap(_JNI.invokePCP(_long.valueOf(arg0), _short.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: bool, arg2: bool, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,boolean,boolean,long,long)"""
        return int._wrap(_JNI.invokePPP(_long.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPJPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPP(long,long,long,int[],long)"""
        return int._wrap(_JNI.callPPJPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,int,long)"""
        _JNI.invokeV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'float', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long[],long,long,float[],int[],long)"""
        return int._wrap(_JNI.callPPJPPPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPJPPPPPI(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPPPPI(long,long[],long,long,long,int,long,int[],long,long)"""
        return int._wrap(_JNI.callPPJPPPPPI(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), arg7, _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPF(arg0: int, arg1: float, arg2: int) -> float:
        """public static native float org.lwjgl.system.JNI.callPF(long,float,long)"""
        return float._wrap(_JNI.callPF(_long.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,long,int,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPS(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPS(long,long,long)"""
        return int._wrap(_JNI.callPPS(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,int,int,long,int,long)"""
        return int._wrap(_JNI.callJPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,float[],long)"""
        _JNI.callPPV(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,long,int,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJJV(long,int,int,long,long,int,int,long)"""
        _JNI.callPJJV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(int,int,int,long)"""
        return int._wrap(_JNI.invokeI(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPJV(int,long,long,int,long,boolean,long)"""
        _JNI.callPPJV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _boolean.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPNPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPNPI(long,long,long,long[],long)"""
        return int._wrap(_JNI.callPPNPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: 'float', arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,float[],float[],long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), arg1, arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,long,int,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,int,int,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPI(long,long,long,long,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPSPSPSPSS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPSPSPSS(long,long,short,long,short,long,short,long,short,long)"""
        return int._wrap(_JNI.callPPSPSPSPSS(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5), _short.valueOf(arg6), _long.valueOf(arg7), _short.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,int,long,int,long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,int[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16), _long.valueOf(arg17))

    @staticmethod
    @overload
    def callPJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJPI(long,long,long,long,long)"""
        return int._wrap(_JNI.callPJJPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,int,long,long,long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPNPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPNPP(long,long,long,long,long)"""
        return int._wrap(_JNI.callPPNPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePNNI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNI(long,long,long,long)"""
        return int._wrap(_JNI.invokePNNI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPZ(arg0: int, arg1: int, arg2: 'int', arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPZ(long,long,int[],long)"""
        return bool._wrap(_JNI.invokePPPZ(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'float', arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), arg10, _long.valueOf(arg11))

    @staticmethod
    @overload
    def invokePNPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNPPI(long,long,long,long,long)"""
        return int._wrap(_JNI.invokePNPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,int,int,long)"""
        _JNI.invokeV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int[],long)"""
        return int._wrap(_JNI.callPPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: 'long', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,long,long[],long)"""
        return int._wrap(_JNI.callPJPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPSS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSS(long,long,short,long)"""
        return int._wrap(_JNI.callPPSS(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPNP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPNP(long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPNP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,long,int,int,long)"""
        _JNI.callPJV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePJI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePJI(long,long,long)"""
        return int._wrap(_JNI.invokePJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeCCUPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUPV(short,short,byte,long,long)"""
        _JNI.invokeCCUPV(_short.valueOf(arg0), _short.valueOf(arg1), _byte.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,int[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,int[],long)"""
        _JNI.callPJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: 'int', arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPP(long,long,long,long,long,long,float[],int[],long)"""
        return int._wrap(_JNI.callPJPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), arg6, arg7, _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,int,boolean,boolean,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4), _boolean.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,long,long,long,long,long,int,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,double,double,double,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _double.valueOf(arg4), _double.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPJI(long,long,int,int,long,long,long,int,long)"""
        return int._wrap(_JNI.callPJPPJI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,int,int,long)"""
        return int._wrap(_JNI.invokePP(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,long,int[],long)"""
        return int._wrap(_JNI.callPJJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCCUV(long,short,int,short,short,short,byte,long)"""
        _JNI.invokePCCCCUV(_long.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _short.valueOf(arg5), _byte.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeUPV(arg0: int, arg1: 'float', arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeUPV(byte,float[],long)"""
        _JNI.invokeUPV(_byte.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: 'long', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long[],int[],long)"""
        return int._wrap(_JNI.callPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callZ(arg0: bool, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(boolean,long)"""
        return bool._wrap(_JNI.callZ(_boolean.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(int,int,int,long,long,long)"""
        return int._wrap(_JNI.callPPP(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: 'int', arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int, arg19: int, arg20: int, arg21: 'int', arg22: 'long', arg23: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(int,int[],long[],int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int[],long[],long)"""
        return int._wrap(_JNI.callPPPPI(_int.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16), _int.valueOf(arg17), _int.valueOf(arg18), _int.valueOf(arg19), _int.valueOf(arg20), arg21, arg22, _long.valueOf(arg23)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(int,int,long,long,long)"""
        _JNI.invokePPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int[],int,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,long,boolean,long)"""
        return int._wrap(_JNI.callPJJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _boolean.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'short', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,short[],long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJJJJV(long,long,long,long,long,int,int,long)"""
        _JNI.callPJJJJV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,double,double,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'long', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,long[],long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,long,int,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCPCC(arg0: int, arg1: 'short', arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCPCC(short,short[],short,long)"""
        return int._wrap(_JNI.invokeCPCC(_short.valueOf(arg0), arg1, _short.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,long,int,int,int,long)"""
        _JNI.callPJV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,int[],int,int[],long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _int.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPCSSSPSPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCSSSPSPPPS(long,short,short,short,short,long,short,long,long,long,long)"""
        return int._wrap(_JNI.callPCSSSPSPPPS(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5), _short.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(long,int,long,long)"""
        return bool._wrap(_JNI.callPPZ(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPCS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPCS(long,long,short,long)"""
        return int._wrap(_JNI.callPPCS(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,int,int,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int[],long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callJJJJV(int,long,long,long,long,long)"""
        _JNI.callJJJJV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: 'double', arg1: int):
        """public static native void org.lwjgl.system.JNI.callPV(double[],long)"""
        _JNI.callPV(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,long,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(long,int,long)"""
        return int._wrap(_JNI.callJI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,long,int,long,long)"""
        return int._wrap(_JNI.callPJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPPP(long,int,long,long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,long,float,long)"""
        _JNI.callPJV(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(int,long,long)"""
        return int._wrap(_JNI.invokePI(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(int,long,int,long)"""
        return int._wrap(_JNI.callPP(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int, arg19: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPPPPPP(long,int,long,long,long,int,long,long,int,long,long,int,int,int,int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPPPPPPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _long.valueOf(arg15), _long.valueOf(arg16), _long.valueOf(arg17), _long.valueOf(arg18), _long.valueOf(arg19)))

    @staticmethod
    @overload
    def invokePPD(arg0: int, arg1: int, arg2: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokePPD(long,long,long)"""
        return float._wrap(_JNI.invokePPD(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPUPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPUPPI(long,long,byte,long,long,long)"""
        return int._wrap(_JNI.callPPUPPI(_long.valueOf(arg0), _long.valueOf(arg1), _byte.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,int,long,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPV(short,int,long,long)"""
        _JNI.invokeCPV(_short.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPPS(long,long,long,long)"""
        return int._wrap(_JNI.callPPPS(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: 'long', arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long[],long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,long,int,int,long,long)"""
        _JNI.callPJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long,int,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePN(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePN(long,long)"""
        return int._wrap(_JNI.invokePN(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPV(arg0: 'float', arg1: int):
        """public static native void org.lwjgl.system.JNI.callPV(float[],long)"""
        _JNI.callPV(arg0, _long.valueOf(arg1))

    @staticmethod
    @overload
    def invokePNNPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNPPI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePNNPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: 'int', arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int[],int[],long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), arg1, arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callCV(int,int,short,long)"""
        _JNI.callCV(_int.valueOf(arg0), _int.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPZ(long,long,long)"""
        return bool._wrap(_JNI.invokePPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,long[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,int,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPPPP(long,long,long,long,long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPJPPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(int,int,long,long,long,long,long,long)"""
        _JNI.callPPPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: float, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,double,long)"""
        return int._wrap(_JNI.invokePP(_long.valueOf(arg0), _double.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeUPU(arg0: int, arg1: int, arg2: int) -> int:
        """public static native byte org.lwjgl.system.JNI.invokeUPU(byte,long,long)"""
        return int._wrap(_JNI.invokeUPU(_byte.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePD(arg0: int, arg1: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokePD(long,long)"""
        return float._wrap(_JNI.invokePD(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokeCCCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCCCV(short,short,short,short,short,long)"""
        _JNI.invokeCCCCCV(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePZ(arg0: int, arg1: bool, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePZ(long,boolean,long)"""
        return bool._wrap(_JNI.invokePZ(_long.valueOf(arg0), _boolean.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeCCUUCCCCPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUUCCCCPCV(short,short,byte,byte,short,short,short,short,long,short,long)"""
        _JNI.invokeCCUUCCCCPCV(_short.valueOf(arg0), _short.valueOf(arg1), _byte.valueOf(arg2), _byte.valueOf(arg3), _short.valueOf(arg4), _short.valueOf(arg5), _short.valueOf(arg6), _short.valueOf(arg7), _long.valueOf(arg8), _short.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: 'short', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,short[],int[],long)"""
        return int._wrap(_JNI.callPJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(int,long,int[],long)"""
        return int._wrap(_JNI.invokePPI(_int.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: 'double', arg3: 'double', arg4: 'double', arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,int,double[],double[],double[],long)"""
        _JNI.invokePPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'short', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPNV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPNV(long,long,long,long)"""
        _JNI.invokePPNV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPPPP(long,long,long,long,long,long,long,int,long,int,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11), _int.valueOf(arg12), _long.valueOf(arg13)))

    @staticmethod
    @overload
    def callPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPP(long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPJPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPNNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNNI(long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPNNI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNI(long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPNI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,int,long,long)"""
        return int._wrap(_JNI.callPJJI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeV(arg0: int):
        """public static native void org.lwjgl.system.JNI.invokeV(long)"""
        _JNI.invokeV(_long.valueOf(arg0))

    @staticmethod
    @overload
    def invokeJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeJV(int,long,long)"""
        _JNI.invokeJV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,int,long,long,long,long,long,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _int.valueOf(arg11), _long.valueOf(arg12), _long.valueOf(arg13), _long.valueOf(arg14)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'short', arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,short[],int,int,long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,int,long,long)"""
        _JNI.invokePPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,boolean,int,long,long,int,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _boolean.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,int[],long)"""
        _JNI.callPPV(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,int,long,int,long,long)"""
        return int._wrap(_JNI.callJPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPJI(long,long,int,long,long)"""
        return int._wrap(_JNI.callJPJI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(int,long,int,long,long)"""
        return bool._wrap(_JNI.callPPZ(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,int,long,int,int,long)"""
        return int._wrap(_JNI.invokePPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,long,long,long,long)"""
        _JNI.callPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,int,int,int,int,int,long,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePCC(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePCC(int,long,short,long)"""
        return int._wrap(_JNI.invokePCC(_int.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,int,int[],long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePF(arg0: int, arg1: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePF(long,long)"""
        return float._wrap(_JNI.invokePF(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,long,int,long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeCUC(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCUC(short,byte,long)"""
        return int._wrap(_JNI.invokeCUC(_short.valueOf(arg0), _byte.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callV(arg0: bool, arg1: bool, arg2: bool, arg3: bool, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(boolean,boolean,boolean,boolean,long)"""
        _JNI.callV(_boolean.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePJV(long,long,int,long)"""
        _JNI.invokePJV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPJPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPPP(long,long,int,long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPJPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,int,long,long,long)"""
        return int._wrap(_JNI.callJPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPNPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNPPPI(long,int,long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPNPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPJPPP(long,long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callUUUUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callUUUUV(int,byte,byte,byte,byte,long)"""
        _JNI.callUUUUV(_int.valueOf(arg0), _byte.valueOf(arg1), _byte.valueOf(arg2), _byte.valueOf(arg3), _byte.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,boolean,int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callSSSSV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callSSSSV(short,short,short,short,long)"""
        _JNI.callSSSSV(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeV(arg0: float, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokeV(float,long)"""
        _JNI.invokeV(_float.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def invokePPPI(arg0: 'short', arg1: int, arg2: int, arg3: int, arg4: bool, arg5: float, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(short[],long,long,int,boolean,float,long)"""
        return int._wrap(_JNI.invokePPPI(arg0, _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,int,int,long,long,long,long,long)"""
        _JNI.callPPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long,int,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(int,long,long)"""
        return int._wrap(_JNI.invokePP(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPP(long,long,long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,float,float,float,float,float,float,long,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def invokeCPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPI(short,long,long)"""
        return int._wrap(_JNI.invokeCPI(_short.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPJI(long,long,long,int,long,long)"""
        return int._wrap(_JNI.callPPPJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPP(arg0: 'int', arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(int[],long)"""
        return int._wrap(_JNI.callPP(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCUV(short,short,short,int,byte,long)"""
        _JNI.invokeCCCUV(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _byte.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'double', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: 'int', arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int[],boolean,long)"""
        _JNI.invokePV(_int.valueOf(arg0), arg1, _boolean.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,float[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPSPSPCS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPPSPSPCS(long,long,long,short,long,short,long,short,long)"""
        return int._wrap(_JNI.callPPPSPSPCS(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4), _short.valueOf(arg5), _long.valueOf(arg6), _short.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,int,int,int,long,int,boolean,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _boolean.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,int,int,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,long,int,int,int,int,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],float[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), arg1, arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePF(arg0: int, arg1: float, arg2: float, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePF(long,float,float,long)"""
        return float._wrap(_JNI.invokePF(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'int', arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,int,long,long,long,long,long,long,long,int[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), arg10, _int.valueOf(arg11), _long.valueOf(arg12), _long.valueOf(arg13), _long.valueOf(arg14)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'short', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,short[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,int,int,long,long,long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJJJJJJJJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int):
        """public static native void org.lwjgl.system.JNI.callPJJJJJJJJJJJV(long,long,long,long,long,long,long,long,long,long,long,long,int,int,int,long)"""
        _JNI.callPJJJJJJJJJJJV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _long.valueOf(arg15))

    @staticmethod
    @overload
    def invokePNNNPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNNNPP(long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePNNNPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeZ(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokeZ(int,long)"""
        return bool._wrap(_JNI.invokeZ(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePNNV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePNNV(long,long,int,int,long,long)"""
        _JNI.invokePNNV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePJJ(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJJ(long,long,long)"""
        return int._wrap(_JNI.invokePJJ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,float,float,float,float,float,float,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,int,int,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNPI(long,long,int,long,long)"""
        return int._wrap(_JNI.invokePNPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPNPI(long,long,long,long,long)"""
        return int._wrap(_JNI.callPPNPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: 'float', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float,float,int,int,float,float,int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), arg9, _long.valueOf(arg10))

    @staticmethod
    @overload
    def callJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callJPV(int,long,int,long,long)"""
        _JNI.callJPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokeCCCCC(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCCCC(short,short,short,short,long)"""
        return int._wrap(_JNI.invokeCCCCC(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeNNNN(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeNNNN(long,long,long,long)"""
        return int._wrap(_JNI.invokeNNNN(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int[],long[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPJP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPJP(long,long,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPJP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPPPP(long,long,long,long,long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,long)"""
        return int._wrap(_JNI.invokePP(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: 'short', arg2: int, arg3: 'float', arg4: 'float', arg5: int, arg6: int, arg7: 'short', arg8: int, arg9: bool, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(int,short[],int,float[],float[],long,int,short[],int,boolean,long)"""
        _JNI.invokePPPPPV(_int.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, arg4, _long.valueOf(arg5), _int.valueOf(arg6), arg7, _int.valueOf(arg8), _boolean.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,int,long,long,long,long,int[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), arg7, _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePPUP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPUP(long,long,byte,long)"""
        return int._wrap(_JNI.invokePPUP(_long.valueOf(arg0), _long.valueOf(arg1), _byte.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,float,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,int,long,long,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,long,int,int,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,int[],int[],int[],int[],long)"""
        _JNI.invokePPPPPV(_long.valueOf(arg0), arg1, arg2, arg3, arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,long,long,long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeP(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeP(int,long)"""
        return int._wrap(_JNI.invokeP(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'double', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,double[],long)"""
        _JNI.callPJJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,long)"""
        _JNI.callPV(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPP(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJ(arg0: int) -> int:
        """public static native long org.lwjgl.system.JNI.callJ(long)"""
        return int._wrap(_JNI.callJ(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long,long[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,long,long,int,long)"""
        return int._wrap(_JNI.callPPI(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int):
        """public static native void org.lwjgl.system.JNI.callV(long)"""
        _JNI.callV(_long.valueOf(arg0))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long[],int,long,int[],long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), arg1, _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeCCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCCCCUV(short,short,short,short,short,int,short,int,byte,long)"""
        _JNI.invokeCCCCCCUV(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _int.valueOf(arg5), _short.valueOf(arg6), _int.valueOf(arg7), _byte.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,int,int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _long.valueOf(arg12))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'double', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8, _long.valueOf(arg9))

    @staticmethod
    @overload
    def callPJPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPJPPPV(long,int,int,long,long,int,long,long,long)"""
        _JNI.callPJPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,long,int,long,int,int,long,long)"""
        return int._wrap(_JNI.invokePPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int[],int,int,long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,int,int,int,int,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: 'float', arg1: 'float', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(float[],float[],long)"""
        _JNI.callPPV(arg0, arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPPPV(int,int,int,long,int,long,long,long,long,long,long,long)"""
        _JNI.callPPPPPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,int,int,long,int,long,long)"""
        _JNI.callPJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPI(long,long,long,long,long[],long)"""
        return int._wrap(_JNI.callPJPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,int,long,long,long[],long)"""
        _JNI.callPJJPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,float,float,float,float,float,int,long,int,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _int.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePUPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePUPV(long,byte,long,int,int,long)"""
        _JNI.invokePUPV(_long.valueOf(arg0), _byte.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,long,long,long,int,long)"""
        _JNI.callPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,int,float,float,int,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,long,long)"""
        _JNI.callPJJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,long,long,long,long,long)"""
        _JNI.callPPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: 'int', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int[],int,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), arg1, _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'long', arg5: 'long', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,int,int,long[],long[],long[],long)"""
        _JNI.callPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,int,long,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,int[],short,long)"""
        _JNI.invokePCPCV(_long.valueOf(arg0), _short.valueOf(arg1), arg2, _short.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,float[],int[],long)"""
        return int._wrap(_JNI.callPJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,int,long,long)"""
        return int._wrap(_JNI.invokePPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'double', arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,double[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,int,int,int,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,boolean,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _boolean.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,boolean,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int,long,int[],long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPJI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: 'int', arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int[],long,int,int[],long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int[],long,int[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPI(long,int,int,long,long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,boolean,int,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _boolean.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePJP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJP(long,int,long,long)"""
        return int._wrap(_JNI.invokePJP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePNNV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePNNV(long,long,long,long)"""
        _JNI.invokePNNV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,long,long,long)"""
        return int._wrap(_JNI.callPJPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeCUCCCCCCPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.invokeCUCCCCCCPV(short,byte,short,short,short,short,short,short,long,long)"""
        _JNI.invokeCUCCCCCCPV(_short.valueOf(arg0), _byte.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _short.valueOf(arg5), _short.valueOf(arg6), _short.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9))

    @staticmethod
    @overload
    def callPJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJI(long,long,int,long)"""
        return int._wrap(_JNI.callPJI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int[],int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePNPN(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNPN(long,long,long,int,long)"""
        return int._wrap(_JNI.invokePNPN(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPP(long,long,long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPJPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,float,float,int,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,long,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,float[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callZ(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(int,long)"""
        return bool._wrap(_JNI.callZ(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPPP(long,long,long,long,long,long,long,int,long,int,long,int,long)"""
        return int._wrap(_JNI.invokePPPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _int.valueOf(arg11), _long.valueOf(arg12)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,int,long,int,int,long,long,long)"""
        _JNI.callPJPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPPPI(long,int,int,long,long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'double', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long[],long,long,double[],int[],long)"""
        return int._wrap(_JNI.callPPJPPPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,float,float,float,float,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePUCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePUCUV(long,byte,short,byte,int,int,long)"""
        _JNI.invokePUCUV(_long.valueOf(arg0), _byte.valueOf(arg1), _short.valueOf(arg2), _byte.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: 'float', arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(int,long,int,float[],float[],long,int,long,int,boolean,long)"""
        _JNI.invokePPPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _boolean.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def invokePPPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPNI(long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPNI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],long,int,int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), arg1, _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'long', arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long[],int[],int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), arg1, arg2, _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'short', arg12: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11, _long.valueOf(arg12))

    @staticmethod
    @overload
    def invokePP(arg0: 'long', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long[],int,long)"""
        return int._wrap(_JNI.invokePP(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,int,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPI(arg0: 'int', arg1: int, arg2: int, arg3: int, arg4: bool, arg5: float, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(int[],long,long,int,boolean,float,long)"""
        return int._wrap(_JNI.invokePPPI(arg0, _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPJV(long,long,long,long,long,long,long)"""
        _JNI.callPPPPPJV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePCCCCC(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePCCCCC(long,short,short,short,short,long)"""
        return int._wrap(_JNI.invokePCCCCC(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,float,float,float,float,float,float,float,float,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _long.valueOf(arg9)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,short[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokeCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUV(short,short,int,int,int,byte,long)"""
        _JNI.invokeCCUV(_short.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _byte.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePUCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePUCV(long,byte,short,int,long)"""
        _JNI.invokePUCV(_long.valueOf(arg0), _byte.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,int,long,int,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,float,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: 'short', arg1: 'short', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(short[],short[],long)"""
        _JNI.callPPV(arg0, arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def callSPSSPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native short org.lwjgl.system.JNI.callSPSSPSPS(short,long,short,short,long,short,long,long)"""
        return int._wrap(_JNI.callSPSSPSPS(_short.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4), _short.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'double', arg12: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), arg11, _long.valueOf(arg12))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,int,float[],int[],long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,long,int,long,long,int,int,long,long)"""
        _JNI.invokePPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokeCCC(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCC(short,short,boolean,long)"""
        return int._wrap(_JNI.invokeCCC(_short.valueOf(arg0), _short.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,int[],int[],long)"""
        return int._wrap(_JNI.callPJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPSPSPSCCS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPSPSCCS(long,long,short,long,short,long,short,short,short,long)"""
        return int._wrap(_JNI.callPPSPSPSCCS(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5), _short.valueOf(arg6), _short.valueOf(arg7), _short.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,int,int,int,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPJPPP(long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: bool, arg2: bool, arg3: bool, arg4: bool, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,boolean,boolean,boolean,boolean,long)"""
        _JNI.callV(_int.valueOf(arg0), _boolean.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: int):
        """public static native void org.lwjgl.system.JNI.callJV(long,int,float,float,float,float,float,float,float,float,float,long)"""
        _JNI.callJV(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _long.valueOf(arg11))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,int,int,int,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callJJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJJPPPI(long,long,int,long,int,long,long,long)"""
        return int._wrap(_JNI.callJJPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPPPPZ(long,long,long,long,long,long)"""
        return bool._wrap(_JNI.callPPPPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPPP(int,long,long,int,int,int,int,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPP(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _int.valueOf(arg10), _long.valueOf(arg11), _long.valueOf(arg12), _long.valueOf(arg13)))

    @staticmethod
    @overload
    def invokeV(arg0: float, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokeV(double,long)"""
        _JNI.invokeV(_double.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: float, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(long,float,long)"""
        return int._wrap(_JNI.callJI(_long.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,int,long,long,int[],long)"""
        return int._wrap(_JNI.callPPPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPPP(long,long,long,long,int,long,long,long,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNI(long,long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPNI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePNPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePNPV(long,long,long,long)"""
        _JNI.invokePNPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeCCJC(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCJC(short,short,int,long,long)"""
        return int._wrap(_JNI.invokeCCJC(_short.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'double', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeCCUCCCCUCCCCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUCCCCUCCCCCCV(short,short,byte,short,short,short,short,byte,short,short,short,short,short,short,long)"""
        _JNI.invokeCCUCCCCUCCCCCCV(_short.valueOf(arg0), _short.valueOf(arg1), _byte.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _short.valueOf(arg5), _short.valueOf(arg6), _byte.valueOf(arg7), _short.valueOf(arg8), _short.valueOf(arg9), _short.valueOf(arg10), _short.valueOf(arg11), _short.valueOf(arg12), _short.valueOf(arg13), _long.valueOf(arg14))

    @staticmethod
    @overload
    def callPPUPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPUPPPI(long,long,byte,long,long,long,long)"""
        return int._wrap(_JNI.callPPUPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _byte.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,long,int,int,long)"""
        return int._wrap(_JNI.callJPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long,int,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPI(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPJPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'int', arg12: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPPPPP(long,long,int,long,long,long,long,long,int,long,long,int[],long)"""
        return int._wrap(_JNI.callPPJPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), arg11, _long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long[],long,long,int[],int[],long)"""
        return int._wrap(_JNI.callPPJPPPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPJPPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPP(long,long[],long,long,long,short[],int[],long)"""
        return int._wrap(_JNI.callPPJPPPPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, arg6, _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: 'int', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int[],long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'long', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long[],long[],long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,int,int,int,int,int,long)"""
        return int._wrap(_JNI.invokePP(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,int,long,long,long,long,int,long)"""
        _JNI.callPPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPCSPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCSPPPS(long,short,short,long,long,long,long)"""
        return int._wrap(_JNI.callPCSPPPS(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPPZ(long,long,long,long)"""
        return bool._wrap(_JNI.callPPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPI(long,long,long,long,long)"""
        return int._wrap(_JNI.callJPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePNNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNI(long,long,long,int,int,long)"""
        return int._wrap(_JNI.invokePNNI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,int,long[],int,long,long)"""
        return int._wrap(_JNI.callPPJI(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeJPPP(int,int,int,long,long,long,long)"""
        return int._wrap(_JNI.invokeJPPP(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,long,long)"""
        return int._wrap(_JNI.callPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callSSV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callSSV(int,short,short,long)"""
        _JNI.callSSV(_int.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePJP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJP(long,long,int,long)"""
        return int._wrap(_JNI.invokePJP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,long,int,int,int,long)"""
        return int._wrap(_JNI.callJPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,int,int,long,long,long,long,long,int,int,long,int,int,int,int,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _long.valueOf(arg15)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,boolean,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: 'long', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(int,long,long[],int[],long)"""
        return int._wrap(_JNI.callPPPP(_int.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,long,long,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: 'int', arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int[],int,long,int,int[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,int,int,long,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: bool, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,boolean,long,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _boolean.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,int,int,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int[],long[],long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePCCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCCCCUV(long,short,short,short,short,short,int,short,int,byte,long)"""
        _JNI.invokePCCCCCCUV(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _short.valueOf(arg5), _int.valueOf(arg6), _short.valueOf(arg7), _int.valueOf(arg8), _byte.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,int,int,int,long,long)"""
        return int._wrap(_JNI.invokePPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callJPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callJPV(long,long,long)"""
        _JNI.callJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,int,long,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,long,long,long,long,long,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _int.valueOf(arg10), _long.valueOf(arg11), _long.valueOf(arg12), _long.valueOf(arg13)))

    @staticmethod
    @overload
    def invokeC(arg0: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeC(long)"""
        return int._wrap(_JNI.invokeC(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(int,int,int,int,long,long,long)"""
        _JNI.invokePPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long,boolean,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _boolean.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callJPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callJPZ(long,long,int,long)"""
        return bool._wrap(_JNI.callJPZ(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,long,int,int,long)"""
        return int._wrap(_JNI.invokePPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPNP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPNP(long,long,long,long)"""
        return int._wrap(_JNI.callPPNP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,int,long,long,long)"""
        _JNI.invokePPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,float,long)"""
        _JNI.invokeV(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPI(long,int,long,long,long,int,long)"""
        return int._wrap(_JNI.callJPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'short', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long[],long,long,short[],int[],long)"""
        return int._wrap(_JNI.callPPJPPPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,float,float,long)"""
        _JNI.callPV(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'double', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,double[],long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,long,int,long,long)"""
        _JNI.callPJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePNPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNPPPI(long,int,int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePNPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,int,long,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callI(arg0: int, arg1: float, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callI(int,float,long)"""
        return int._wrap(_JNI.callI(_int.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int[],int[],int[],long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'short', arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,int,long,long,long,long,short[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), arg7, _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'short', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,int,int,short[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: 'double', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'short', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,short[],int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), arg2, _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,long,int,long)"""
        return int._wrap(_JNI.callPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,long[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPI(long,long,long,long,long)"""
        return int._wrap(_JNI.callPPJPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCV(short,int,int,long)"""
        _JNI.invokeCV(_short.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,float,float,float,float,long,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeCPUI(arg0: int, arg1: 'float', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPUI(short,float[],byte,long)"""
        return int._wrap(_JNI.invokeCPUI(_short.valueOf(arg0), arg1, _byte.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'short', arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int,short[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,long,int,int,long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPUPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPUPPI(long,byte,long,long,long)"""
        return int._wrap(_JNI.callPUPPI(_long.valueOf(arg0), _byte.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,float[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePZ(long,int,int,long)"""
        return bool._wrap(_JNI.invokePZ(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'double', arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), arg10, _long.valueOf(arg11))

    @staticmethod
    @overload
    def callJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callJJJV(int,int,long,long,long,long)"""
        _JNI.callJJJV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,float,long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPPPS(long,long,int,long,int,long,long)"""
        return int._wrap(_JNI.callPPPPS(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,float[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int, arg6: 'int', arg7: 'float', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int,int[],int,int[],float[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _int.valueOf(arg5), arg6, arg7, _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPZ(long,int,long,long)"""
        return bool._wrap(_JNI.invokePPZ(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,int[],long)"""
        return int._wrap(_JNI.invokePPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(long,float,float,float,long)"""
        return int._wrap(_JNI.callJI(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeUPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeUPCV(byte,long,int,int,short,long)"""
        _JNI.invokeUPCV(_byte.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePNPPV(arg0: int, arg1: int, arg2: int, arg3: 'short', arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePNPPV(long,long,long,short[],long)"""
        _JNI.invokePNPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callSPS(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.callSPS(short,long,long)"""
        return int._wrap(_JNI.callSPS(_short.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long,long,int,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,int,long,int,long)"""
        return int._wrap(_JNI.invokePPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,long,int,int,long)"""
        _JNI.callPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPZ(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPPPZ(int,int,int,float,long,long,long,long,long)"""
        return bool._wrap(_JNI.callPPPPZ(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callUUUV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callUUUV(byte,byte,byte,long)"""
        _JNI.callUUUV(_byte.valueOf(arg0), _byte.valueOf(arg1), _byte.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeUV(arg0: int, arg1: bool, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeUV(byte,boolean,long)"""
        _JNI.invokeUV(_byte.valueOf(arg0), _boolean.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,float,float,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int[],long)"""
        return int._wrap(_JNI.callPI(_int.valueOf(arg0), arg1, _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,float,float,float,float,int,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPCPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPCPPPI(long,long,short,long,long,long,long)"""
        return int._wrap(_JNI.callPPCPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,float[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePZ(long,int,int,int,long)"""
        return bool._wrap(_JNI.invokePZ(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJPPP(long,long,int,long,long,int,long)"""
        return int._wrap(_JNI.invokePJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPJPI(long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPJPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeUCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeUCV(byte,short,int,int,long)"""
        _JNI.invokeUCV(_byte.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(int,int,int,long,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPP(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPJJJJV(long,long,int,int,long,long,long,int,long)"""
        _JNI.callPJJJJV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,long,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,long,int,long,int,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,float,long)"""
        _JNI.callPV(_long.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPJ(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJ(long,long,long)"""
        return int._wrap(_JNI.callPPJ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJPPP(long,int,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePJPPP(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,long,long,long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(int,long,long,long)"""
        _JNI.invokePPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(long,long,long)"""
        return bool._wrap(_JNI.callPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'int', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), arg8, _long.valueOf(arg9))

    @staticmethod
    @overload
    def callPJJJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJJJPI(long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPJJJJPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,long,int[],long,long)"""
        _JNI.callPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,int,int,int,int,long,int,int,int,int,int,int,int,int,int,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _int.valueOf(arg13), _int.valueOf(arg14), _int.valueOf(arg15), _int.valueOf(arg16), _long.valueOf(arg17)))

    @staticmethod
    @overload
    def callPSPS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSPS(long,short,long,long)"""
        return int._wrap(_JNI.callPSPS(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,int,long,long,long,long)"""
        _JNI.invokePPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(long,long)"""
        return int._wrap(_JNI.callPP(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int[],long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePUP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePUP(long,byte,long)"""
        return int._wrap(_JNI.invokePUP(_long.valueOf(arg0), _byte.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'long', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPI(long,long,int,long,long,long[],long)"""
        return int._wrap(_JNI.callPJPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPF(arg0: int, arg1: int, arg2: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePPF(long,long,long)"""
        return float._wrap(_JNI.invokePPF(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,float,float,float,long)"""
        _JNI.invokeV(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPSPSPSS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPSPSS(long,long,short,long,short,long,short,long)"""
        return int._wrap(_JNI.callPPSPSPSS(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5), _short.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPJPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPJPPZ(long,long,long,long,long,long)"""
        return bool._wrap(_JNI.callPPJPPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: 'float', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,float[],long,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.callJV(long,long)"""
        _JNI.callJV(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float,long,int,long)"""
        _JNI.callPV(_int.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'double', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,double[],int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), arg2, _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'short', arg9: 'int', arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPPPP(long,long,long,long,long,long,long,long,short[],int[],long)"""
        return int._wrap(_JNI.callPJPPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), arg8, arg9, _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPJPPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPP(long,long[],long,long,long,long,int[],long)"""
        return int._wrap(_JNI.callPPJPPPPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), arg6, _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(int,int,int,int[],int[],long)"""
        return int._wrap(_JNI.callPPP(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePNPV(arg0: int, arg1: int, arg2: 'short', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePNPV(long,long,short[],long)"""
        _JNI.invokePNPV(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPCPSPPPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPSPPPPPS(long,short,long,short,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPCPSPPPPPS(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPCI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPCI(long,long,short,long)"""
        return int._wrap(_JNI.invokePPCI(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,long,long,int,int,int,int,long)"""
        return int._wrap(_JNI.invokePPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePB(arg0: int, arg1: int) -> int:
        """public static native byte org.lwjgl.system.JNI.invokePB(long,long)"""
        return int._wrap(_JNI.invokePB(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: bool, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,boolean,boolean,long)"""
        _JNI.invokePPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,int,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,int,int[],int[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPPJPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJPPPPPP(long,long,long,long,long,int,long,int,int,long,long,int,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPJPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _int.valueOf(arg11), _int.valueOf(arg12), _long.valueOf(arg13), _long.valueOf(arg14), _long.valueOf(arg15), _long.valueOf(arg16)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int[],long,int[],long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(int,int,long,long)"""
        return bool._wrap(_JNI.callPZ(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPI(long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,long[],long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,int,int,long,long)"""
        _JNI.callJV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,float,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,int,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,double,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,int,int,int,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,short,boolean,long)"""
        _JNI.invokePCV(_long.valueOf(arg0), _short.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeUCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeUCV(byte,short,int,long)"""
        _JNI.invokeUCV(_byte.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,long,long)"""
        _JNI.callPJV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,long[],int,int,int,long,int,long,int,long,long)"""
        _JNI.callPPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPPPI(long,long,long,long,long,long,long,long,long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _int.valueOf(arg11), _long.valueOf(arg12), _long.valueOf(arg13), _long.valueOf(arg14), _long.valueOf(arg15)))

    @staticmethod
    @overload
    def invokeUCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeUCCV(byte,short,int,int,short,long)"""
        _JNI.invokeUCCV(_byte.valueOf(arg0), _short.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int,int[],long)"""
        return int._wrap(_JNI.callPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long[],long,long,long,int[],long)"""
        return int._wrap(_JNI.callPPJPPPP(_long.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPCI(arg0: int, arg1: 'float', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPCI(long,float[],short,long)"""
        return int._wrap(_JNI.invokePPCI(_long.valueOf(arg0), arg1, _short.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: bool, arg3: 'double', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,boolean,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'long', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,long[],long)"""
        _JNI.callPJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'float', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],float[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeCP(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeCP(short,long)"""
        return int._wrap(_JNI.invokeCP(_short.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,float[],short,long)"""
        _JNI.invokeCPCV(_short.valueOf(arg0), arg1, _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJPPP(long,int,long,long,long,long,int,int,long,int,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPJPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _long.valueOf(arg11), _long.valueOf(arg12), _long.valueOf(arg13)))

    @staticmethod
    @overload
    def callPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPP(long,int,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,int,int,int,int,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,int,int[],long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'short', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,long,int,int,short[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), arg7, _long.valueOf(arg8))

    @staticmethod
    @overload
    def callI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callI(int,int,long)"""
        return int._wrap(_JNI.callI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,float[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), arg6, _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPZ(long,int,int,long,long)"""
        return bool._wrap(_JNI.invokePPZ(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _double.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int,long,long,long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,long,int,long,int,long)"""
        return int._wrap(_JNI.invokePPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,int,int,long,long)"""
        return int._wrap(_JNI.invokePPP(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,long,long,long,long,int,int,int,long)"""
        _JNI.callPPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPCPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPCPPI(long,long,short,long,long,long)"""
        return int._wrap(_JNI.callPPCPPI(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePCI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePCI(long,short,long)"""
        return int._wrap(_JNI.invokePCI(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,long,long,int,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'float', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,int,int[],float[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: float, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,long,int,boolean,float,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(int,int,int,long,long,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPP(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(int,int,int,long,long)"""
        return int._wrap(_JNI.invokePP(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,long,int[],long)"""
        return int._wrap(_JNI.callPPI(_int.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,long,int,long,int,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: 'int', arg2: int, arg3: 'float', arg4: 'float', arg5: int, arg6: int, arg7: 'int', arg8: int, arg9: bool, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(int,int[],int,float[],float[],long,int,int[],int,boolean,long)"""
        _JNI.invokePPPPPV(_int.valueOf(arg0), arg1, _int.valueOf(arg2), arg3, arg4, _long.valueOf(arg5), _int.valueOf(arg6), arg7, _int.valueOf(arg8), _boolean.valueOf(arg9), _long.valueOf(arg10))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,long,long,float[],long,long)"""
        _JNI.invokePPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int', arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(int,int,int[],int[],int[],int[],long,long)"""
        return int._wrap(_JNI.callPPPPPI(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, arg5, _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,short[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,int,long,long)"""
        _JNI.callPJV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,long[],long)"""
        _JNI.callPJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,long,int,long)"""
        _JNI.invokePPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,double,double,double,double,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _double.valueOf(arg4), _double.valueOf(arg5), _double.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,int,int,int,long,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,int,long,int,int,long,long)"""
        _JNI.callPJJPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPV(arg0: 'int', arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int[],int,int[],long)"""
        _JNI.callPPV(arg0, _int.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPP(long,long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPJPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,long,int,int,long)"""
        return int._wrap(_JNI.invokePPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPCPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPCPV(long,long,short,int,long,long)"""
        _JNI.invokePPCPV(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,float,float,float,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,double,double,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _double.valueOf(arg2), _double.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int[],boolean,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _boolean.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(long,long)"""
        return bool._wrap(_JNI.callPZ(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,float,float,float,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(int,int,long,long)"""
        return int._wrap(_JNI.invokePP(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'float', arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,float[],int,int,long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePCCC(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePCCC(long,short,short,int,int,long)"""
        return int._wrap(_JNI.invokePCCC(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def invokePJPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePJPPNI(long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePJPPNI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCCCJPC(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCCJPC(short,short,short,boolean,int,long,long,long)"""
        return int._wrap(_JNI.invokeCCCJPC(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCUV(long,short,short,short,int,byte,long)"""
        _JNI.invokePCCCUV(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _int.valueOf(arg4), _byte.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,long,long,long)"""
        return int._wrap(_JNI.callJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeUPZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokeUPZ(byte,long,long)"""
        return bool._wrap(_JNI.invokeUPZ(_byte.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,float[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,long,long,long)"""
        return int._wrap(_JNI.callPPI(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePCPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePCPI(long,short,long,long)"""
        return int._wrap(_JNI.invokePCPI(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeUPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeUPV(byte,long,int,int,long)"""
        _JNI.invokeUPV(_byte.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,int,long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPJJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJJI(long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPJJJI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: int):
        """public static native void org.lwjgl.system.JNI.callV(float,long)"""
        _JNI.callV(_float.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,int,long,int,long)"""
        return int._wrap(_JNI.callJPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,int,long,int,long,long)"""
        return int._wrap(_JNI.callPPI(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePBV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePBV(long,int,int,byte,long)"""
        _JNI.invokePBV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _byte.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePCCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: bool, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCCV(long,short,short,short,boolean,boolean,short,int,long)"""
        _JNI.invokePCCCCV(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _boolean.valueOf(arg4), _boolean.valueOf(arg5), _short.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long[],int,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokeCCPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCCPV(short,short,long,long)"""
        _JNI.invokeCCPV(_short.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,long,boolean,boolean,long)"""
        return int._wrap(_JNI.invokePPP(_long.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'int', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,boolean,int,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPSPSPSPSPSPSS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPSPSPSPSPSS(long,long,short,long,short,long,short,long,short,long,short,long,short,long)"""
        return int._wrap(_JNI.callPPSPSPSPSPSPSS(_long.valueOf(arg0), _long.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3), _short.valueOf(arg4), _long.valueOf(arg5), _short.valueOf(arg6), _long.valueOf(arg7), _short.valueOf(arg8), _long.valueOf(arg9), _short.valueOf(arg10), _long.valueOf(arg11), _short.valueOf(arg12), _long.valueOf(arg13)))

    @staticmethod
    @overload
    def callJPJPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPJPPJI(long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callJPJPPJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callSSSV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callSSSV(int,short,short,short,long)"""
        _JNI.callSSSV(_int.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: 'int', arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,long,float[],long,long,int,int[],int[],long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), arg7, arg8, _long.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,long,long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePJJP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJJP(long,long,long,long)"""
        return int._wrap(_JNI.invokePJJP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePJPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePJPZ(long,long,long,int,long)"""
        return bool._wrap(_JNI.invokePJPZ(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callZ(arg0: int, arg1: float, arg2: float, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(int,float,float,long)"""
        return bool._wrap(_JNI.callZ(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPP(long,long,long,long,long,long,long,int[],long)"""
        return int._wrap(_JNI.callPJPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), arg7, _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int,long,int,long,long,long)"""
        _JNI.callPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: 'int', arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,int,long,int[],int[],int[],int,long)"""
        _JNI.callPPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, arg4, arg5, _int.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,boolean,long,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,long,long,int,long,int[],long,long)"""
        return int._wrap(_JNI.callPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), arg6, _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,int,int,long,long,long,long,long)"""
        _JNI.invokePPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(int,int,long,long)"""
        return int._wrap(_JNI.callPP(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPJJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPJJPPP(long,long,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPJJPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,float,float,float,float,long)"""
        _JNI.invokePPV(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,long,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,long,int[],long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'double', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,double,double,int,int,double[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: 'long', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,long[],long)"""
        _JNI.callPJPV(_long.valueOf(arg0), _long.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,long,int,long,long,long,long)"""
        _JNI.invokePPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,int,long,long,long)"""
        return int._wrap(_JNI.callPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,long,int,int,int,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int[],int[],long)"""
        return int._wrap(_JNI.callPJPPI(_long.valueOf(arg0), _long.valueOf(arg1), arg2, arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'double', arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,double[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(int,float,long)"""
        _JNI.callV(_int.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(double,double,double,long)"""
        _JNI.callV(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,int,long,long)"""
        _JNI.callPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPJPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'int', arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPPP(long,long,int,long,long,long,int,long,long,int[],long)"""
        return int._wrap(_JNI.callPPJPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), arg9, _long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPPV(long,long,long,long,long,long,long)"""
        _JNI.invokePPPPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,int,int,int,long,int,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(int,long,long,long)"""
        return int._wrap(_JNI.invokePPI(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,int,int,long,long,int,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _int.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: float, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,float,long,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _float.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,int,int,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,int,int,long,long,long,long,long,int,int,int,int,long)"""
        return int._wrap(_JNI.callPPPPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _int.valueOf(arg10), _int.valueOf(arg11), _long.valueOf(arg12)))

    @staticmethod
    @overload
    def callBBBV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callBBBV(byte,byte,byte,long)"""
        _JNI.callBBBV(_byte.valueOf(arg0), _byte.valueOf(arg1), _byte.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,short[],int[],long)"""
        return int._wrap(_JNI.callPJJPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), arg4, arg5, _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePJUPC(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePJUPC(long,long,byte,long,long)"""
        return int._wrap(_JNI.invokePJUPC(_long.valueOf(arg0), _long.valueOf(arg1), _byte.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,long,int,int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],int,int[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _int.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,long,int,long)"""
        return int._wrap(_JNI.invokePPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,int,long)"""
        return int._wrap(_JNI.callPI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePJJJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePJJJJPI(long,long,long,long,long,int,long,long)"""
        return int._wrap(_JNI.invokePJJJJPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,int,int,long,long,long,long)"""
        _JNI.callPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPCPSPPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPSPPSPS(long,short,long,short,long,long,short,long,long)"""
        return int._wrap(_JNI.callPCPSPPSPS(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _short.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _short.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,int,long,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,int,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPNPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNPPI(long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.invokePPNPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPCPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPPPS(long,short,long,long,long,long)"""
        return int._wrap(_JNI.callPCPPPS(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,long,long)"""
        return int._wrap(_JNI.invokePPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callC(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.JNI.callC(int,long)"""
        return int._wrap(_JNI.callC(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPP(long,long,long,long,long)"""
        return int._wrap(_JNI.callPPJPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPJJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJJPP(long,long,long,long,long,int,long,int,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPPPJJPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _long.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,int,short,long)"""
        _JNI.invokePCV(_long.valueOf(arg0), _int.valueOf(arg1), _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long,long,int,long)"""
        return int._wrap(_JNI.callPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPP(long,int,long,long,long,long,long)"""
        return int._wrap(_JNI.callPPPPPP(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePJ(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJ(long,int,long)"""
        return int._wrap(_JNI.invokePJ(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePUP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: bool, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePUP(long,int,byte,int,boolean,boolean,long)"""
        return int._wrap(_JNI.invokePUP(_long.valueOf(arg0), _int.valueOf(arg1), _byte.valueOf(arg2), _int.valueOf(arg3), _boolean.valueOf(arg4), _boolean.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCCPV(arg0: int, arg1: int, arg2: 'short', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCCPV(short,short,short[],long)"""
        _JNI.invokeCCPV(_short.valueOf(arg0), _short.valueOf(arg1), arg2, _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPJPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPPPPI(long,long,long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPJPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8), _long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPJI(arg0: int, arg1: int, arg2: float, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJI(long,long,float,long)"""
        return int._wrap(_JNI.callPJI(_long.valueOf(arg0), _long.valueOf(arg1), _float.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,long,int,int,int,long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,long,int,long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,short[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5, _long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePNNPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNPPPI(long,long,long,int,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePNNPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,long,int,int,long)"""
        _JNI.callJV(_int.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int[],long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPJPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPPPPP(long,long,int,long,long,long,long,long,int,long,long,long,long)"""
        return int._wrap(_JNI.callPPJPPPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7), _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11), _long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,int[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJPPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPJI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.callJPPPJI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,int,long)"""
        _JNI.invokePV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePCCUCCCCUCCCCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int):
        """public static native void org.lwjgl.system.JNI.invokePCCUCCCCUCCCCCCV(long,short,short,byte,short,short,short,short,byte,short,short,short,short,short,short,long)"""
        _JNI.invokePCCUCCCCUCCCCCCV(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _byte.valueOf(arg3), _short.valueOf(arg4), _short.valueOf(arg5), _short.valueOf(arg6), _short.valueOf(arg7), _byte.valueOf(arg8), _short.valueOf(arg9), _short.valueOf(arg10), _short.valueOf(arg11), _short.valueOf(arg12), _short.valueOf(arg13), _short.valueOf(arg14), _long.valueOf(arg15))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long,int,long)"""
        _JNI.callPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeU(arg0: int, arg1: int) -> int:
        """public static native byte org.lwjgl.system.JNI.invokeU(int,long)"""
        return int._wrap(_JNI.invokeU(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,long,long,long,long,long)"""
        _JNI.callPPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int', arg10: 'long', arg11: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPPPV(int,int,int,long,int,long,int[],int[],int[],int[],long[],long)"""
        _JNI.callPPPPPPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5), arg6, arg7, arg8, arg9, arg10, _long.valueOf(arg11))

    @staticmethod
    @overload
    def callPI(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int[],int,long)"""
        return int._wrap(_JNI.callPI(arg0, _int.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPCPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPCPPI(long,short,long,long,long)"""
        return int._wrap(_JNI.callPCPPI(_long.valueOf(arg0), _short.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(long,int,int,long)"""
        return int._wrap(_JNI.invokePI(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(int,long,long,long,long,long,long)"""
        _JNI.invokePPPPPV(_int.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,int,int,long)"""
        return int._wrap(_JNI.callPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePBPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePBPPP(long,byte,long,long,long)"""
        return int._wrap(_JNI.invokePBPPP(_long.valueOf(arg0), _byte.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,int,int,int,long)"""
        _JNI.invokeV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long,int,int[],long)"""
        return int._wrap(_JNI.callPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), arg4, _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,long,int,long,int,int,int,long)"""
        return int._wrap(_JNI.invokePPPPPPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _int.valueOf(arg5), _long.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'double', arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,int,long,long,long,long,double[],int,long,long,long)"""
        return int._wrap(_JNI.callPPPPPPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), arg7, _int.valueOf(arg8), _long.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCCCUV(long,short,short,short,short,short,byte,long)"""
        _JNI.invokePCCCCCUV(_long.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2), _short.valueOf(arg3), _short.valueOf(arg4), _short.valueOf(arg5), _byte.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: 'float', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,int,float,float,int,float[],long)"""
        _JNI.callPPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _int.valueOf(arg7), arg8, _long.valueOf(arg9))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,long,long)"""
        _JNI.callPV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _int.valueOf(arg9), _long.valueOf(arg10), _long.valueOf(arg11))

    @staticmethod
    @overload
    def invokePJV(arg0: int, arg1: 'int', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePJV(int,int[],long,long)"""
        _JNI.invokePJV(_int.valueOf(arg0), arg1, _long.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJPPI(long,long,long,long,long,long)"""
        return int._wrap(_JNI.callPJJPPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNPI(long,long,long,int,long)"""
        return int._wrap(_JNI.invokePNPI(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'short', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,short[],long)"""
        _JNI.callPV(_int.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokeCPUI(arg0: int, arg1: 'short', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPUI(short,short[],byte,long)"""
        return int._wrap(_JNI.invokeCPUI(_short.valueOf(arg0), arg1, _byte.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int', arg6: 'int', arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(int,int,int[],int[],int[],int[],int[],long,long)"""
        return int._wrap(_JNI.callPPPPPPI(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, arg4, arg5, arg6, _long.valueOf(arg7), _long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(int,int,long,int,long)"""
        return int._wrap(_JNI.callPP(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,int,long,long,long,long,long)"""
        _JNI.callPPPPPV(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(int,int,long,int,long,long)"""
        return bool._wrap(_JNI.callPPZ(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPS(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPS(long,long)"""
        return int._wrap(_JNI.callPS(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: 'float', arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,float[],long)"""
        _JNI.invokePV(_int.valueOf(arg0), arg1, _long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,long,boolean,long)"""
        _JNI.invokePV(_int.valueOf(arg0), _long.valueOf(arg1), _boolean.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,int,int,long,long,long,long)"""
        return int._wrap(_JNI.invokePPPPPI(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5), _long.valueOf(arg6), _long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,long,int,long,long)"""
        return int._wrap(_JNI.invokePPPI(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _int.valueOf(arg3), _long.valueOf(arg4), _long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPF(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.callPPPF(long,long,long,long)"""
        return float._wrap(_JNI.callPPPF(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,boolean,long)"""
        _JNI.callV(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _boolean.valueOf(arg6), _long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: 'int', arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int[],int[],long)"""
        return int._wrap(_JNI.callPPPI(_long.valueOf(arg0), arg1, arg2, _long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int[],long[],long)"""
        _JNI.callPPPV(_long.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: 'int', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,int[],short,long)"""
        _JNI.invokeCPCV(_short.valueOf(arg0), arg1, _short.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPNPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPNPP(long,long,long,int[],long)"""
        return int._wrap(_JNI.callPPNPP(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), arg3, _long.valueOf(arg4))) 
 
 
# CLASS: org.lwjgl.system.FunctionProviderLocal
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import org.lwjgl.system.FunctionProvider as _FunctionProvider
_FunctionProvider = _FunctionProvider
import org.lwjgl.system.FunctionProviderLocal as _FunctionProviderLocal
_FunctionProviderLocal = _FunctionProviderLocal
import java.nio.ByteBuffer as ByteBuffer
from abc import abstractmethod, ABC
import java.lang.Long as _long
from builtins import int
 
class FunctionProviderLocal():
    """org.lwjgl.system.FunctionProviderLocal"""
 
    @staticmethod
    def _wrap(java_value: _FunctionProviderLocal) -> 'FunctionProviderLocal':
        return FunctionProviderLocal(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FunctionProviderLocal):
        """
        Dynamic initializer for FunctionProviderLocal.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FunctionProviderLocal__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FunctionProviderLocal__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFunctionAddress(self, arg0: int, arg1: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProviderLocal.getFunctionAddress(long,java.nio.ByteBuffer)"""
        pass

    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int._wrap(super(_FunctionProvider, self).getFunctionAddress(arg0))

    @overload
    def getFunctionAddress(self, arg0: int, arg1: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProviderLocal.getFunctionAddress(long,java.lang.CharSequence)"""
        return int._wrap(super(_FunctionProviderLocal, self).getFunctionAddress(_long.valueOf(arg0), arg1))

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass 
 
 
# CLASS: org.lwjgl.system.LibraryResource
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import org.lwjgl.system.LibraryResource as _LibraryResource
_LibraryResource = _LibraryResource
import java.lang.String as _string
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LibraryResource():
    """org.lwjgl.system.LibraryResource"""
 
    @staticmethod
    def _wrap(java_value: _LibraryResource) -> 'LibraryResource':
        return LibraryResource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LibraryResource):
        """
        Dynamic initializer for LibraryResource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LibraryResource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LibraryResource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def load(arg0: 'Class', arg1: str, arg2: 'Configuration', *arg3: str) -> 'Path':
        """public static java.nio.file.Path org.lwjgl.system.LibraryResource.load(java.lang.Class<?>,java.lang.String,org.lwjgl.system.Configuration<java.lang.String>,java.lang.String...)"""
        return Path._wrap(_LibraryResource.load(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def load(arg0: 'Class', arg1: str, arg2: str, arg3: bool) -> 'Path':
        """public static java.nio.file.Path org.lwjgl.system.LibraryResource.load(java.lang.Class<?>,java.lang.String,java.lang.String,boolean)"""
        return Path._wrap(_LibraryResource.load(arg0, arg1, arg2, _boolean.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def load(arg0: str, arg1: str) -> 'Path':
        """public static java.nio.file.Path org.lwjgl.system.LibraryResource.load(java.lang.String,java.lang.String)"""
        return Path._wrap(_LibraryResource.load(arg0, arg1))

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

    @staticmethod
    @overload
    def load(arg0: 'Class', arg1: str, arg2: str) -> 'Path':
        """public static java.nio.file.Path org.lwjgl.system.LibraryResource.load(java.lang.Class<?>,java.lang.String,java.lang.String)"""
        return Path._wrap(_LibraryResource.load(arg0, arg1, arg2))

    @staticmethod
    @overload
    def load(arg0: 'Class', arg1: str, arg2: 'Configuration', arg3: 'Supplier', *arg4: str) -> 'Path':
        """public static java.nio.file.Path org.lwjgl.system.LibraryResource.load(java.lang.Class<?>,java.lang.String,org.lwjgl.system.Configuration<java.lang.String>,java.util.function.Supplier<java.nio.file.Path>,java.lang.String...)"""
        return Path._wrap(_LibraryResource.load(arg0, arg1, arg2, arg3, arg4))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.system.NativeResource
from pyquantum_helper import override
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
from abc import abstractmethod, ABC
 
class NativeResource():
    """org.lwjgl.system.NativeResource"""
 
    @staticmethod
    def _wrap(java_value: _NativeResource) -> 'NativeResource':
        return NativeResource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NativeResource):
        """
        Dynamic initializer for NativeResource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NativeResource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NativeResource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(NativeResource, self).close()

    @abstractmethod
    def free(self, ):
        """public abstract void org.lwjgl.system.NativeResource.free()"""
        pass 
 
 
# CLASS: org.lwjgl.system.Struct$StructValidation
import org.lwjgl.system.Struct as _Struct_StructValidation
_StructValidation = _Struct_StructValidation.StructValidation
from abc import abstractmethod, ABC
 
class StructValidation():
    """org.lwjgl.system.Struct.StructValidation"""
 
    @staticmethod
    def _wrap(java_value: _StructValidation) -> 'StructValidation':
        return StructValidation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StructValidation):
        """
        Dynamic initializer for StructValidation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StructValidation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StructValidation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def validate(self, arg0: int):
        """public abstract void org.lwjgl.system.Struct$StructValidation.validate(long)"""
        pass 
 
 
# CLASS: org.lwjgl.system.MemoryUtil
from pyquantum_helper import import_once as _import_once
import java.lang.Double as _double
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
import java.lang.Short as _short
import org.lwjgl.CLongBuffer as _CLongBuffer
_CLongBuffer = _CLongBuffer
import org.lwjgl.system.MemoryUtil as _MemoryUtil_MemoryAllocator
_MemoryAllocator = _MemoryUtil_MemoryAllocator.MemoryAllocator
import java.nio.DoubleBuffer as _DoubleBuffer
_DoubleBuffer = _DoubleBuffer
import java.lang.Boolean as _boolean
import java.nio.CharBuffer as _CharBuffer
_CharBuffer = _CharBuffer
import java.lang.Byte as _byte
import java.nio.CharBuffer as CharBuffer
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.lang.Object as _object
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
from builtins import float
import org.lwjgl.system.MemoryUtil as _MemoryUtil
_MemoryUtil = _MemoryUtil
import java.nio.LongBuffer as LongBuffer
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Float as _float
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MemoryUtil():
    """org.lwjgl.system.MemoryUtil"""
 
    @staticmethod
    def _wrap(java_value: _MemoryUtil) -> 'MemoryUtil':
        return MemoryUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MemoryUtil):
        """
        Dynamic initializer for MemoryUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MemoryUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MemoryUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def memAddressSafe(arg0: 'LongBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.LongBuffer)"""
        return int._wrap(_MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def getAllocator() -> 'MemoryAllocator':
        """public static org.lwjgl.system.MemoryUtil$MemoryAllocator org.lwjgl.system.MemoryUtil.getAllocator()"""
        return MemoryAllocator._wrap(_MemoryUtil.getAllocator())

    @staticmethod
    @overload
    def memAddress(arg0: 'FloatBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.FloatBuffer,int)"""
        return int._wrap(_MemoryUtil.memAddress(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'ShortBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.ShortBuffer)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memDoubleBuffer(arg0: int, arg1: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memDoubleBuffer(long,int)"""
        return DoubleBuffer._wrap(_MemoryUtil.memDoubleBuffer(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memSlice(arg0: 'ShortBuffer', arg1: int, arg2: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.ShortBuffer,int,int)"""
        return ShortBuffer._wrap(_MemoryUtil.memSlice(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def memFloatBuffer(arg0: int, arg1: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memFloatBuffer(long,int)"""
        return FloatBuffer._wrap(_MemoryUtil.memFloatBuffer(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memCallocPointer(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryUtil.memCallocPointer(int)"""
        return pygl.PointerBuffer._wrap(_MemoryUtil.memCallocPointer(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'IntBuffer') -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.IntBuffer)"""
        return IntBuffer._wrap(_MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memPutByte(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutByte(long,byte)"""
        _MemoryUtil.memPutByte(_long.valueOf(arg0), _byte.valueOf(arg1))

    @staticmethod
    @overload
    def memCallocLong(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memCallocLong(int)"""
        return LongBuffer._wrap(_MemoryUtil.memCallocLong(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memUTF8(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.MemoryUtil.memUTF8(java.lang.CharSequence,boolean,java.nio.ByteBuffer)"""
        return int._wrap(_MemoryUtil.memUTF8(arg0, _boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def memSlice(arg0: 'CharBuffer', arg1: int, arg2: int) -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.CharBuffer,int,int)"""
        return CharBuffer._wrap(_MemoryUtil.memSlice(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def memAllocLong(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memAllocLong(int)"""
        return LongBuffer._wrap(_MemoryUtil.memAllocLong(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memASCII(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memASCII(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryUtil.memASCII(arg0))

    @staticmethod
    @overload
    def memAddress0(arg0: 'Buffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress0(java.nio.Buffer)"""
        return int._wrap(_MemoryUtil.memAddress0(arg0))

    @staticmethod
    @overload
    def memUTF8(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF8(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryUtil.memUTF8(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'LongBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.LongBuffer)"""
        return int._wrap(_MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memASCII(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer', arg3: int) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memASCII(java.lang.CharSequence,boolean,java.nio.ByteBuffer,int)"""
        return int._wrap(_MemoryUtil.memASCII(arg0, _boolean.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'LongBuffer') -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.LongBuffer)"""
        return LongBuffer._wrap(_MemoryUtil.memDuplicate(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def memGetLong(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memGetLong(long)"""
        return int._wrap(_MemoryUtil.memGetLong(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmemAlloc(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemAlloc(long)"""
        return int._wrap(_MemoryUtil.nmemAlloc(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memReport(arg0: 'MemoryAllocationReport'):
        """public static void org.lwjgl.system.MemoryUtil.memReport(org.lwjgl.system.MemoryUtil$MemoryAllocationReport)"""
        _MemoryUtil.memReport(arg0)

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'FloatBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.FloatBuffer)"""
        return int._wrap(_MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'DoubleBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.DoubleBuffer)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memSlice(arg0: 'ByteBuffer', arg1: int, arg2: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.ByteBuffer,int,int)"""
        return ByteBuffer._wrap(_MemoryUtil.memSlice(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.ByteBuffer)"""
        return ByteBuffer._wrap(_MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memByteBufferNT1(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT1(long,int)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBufferNT1(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def memFloatBufferSafe(arg0: int, arg1: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memFloatBufferSafe(long,int)"""
        return FloatBuffer._wrap(_MemoryUtil.memFloatBufferSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memSlice(arg0: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.ByteBuffer)"""
        return ByteBuffer._wrap(_MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memAlignedFree(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memAlignedFree(java.nio.ByteBuffer)"""
        _MemoryUtil.memAlignedFree(arg0)

    @staticmethod
    @overload
    def memUTF8Safe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF8Safe(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryUtil.memUTF8Safe(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memSet(arg0: 'CustomBuffer', arg1: int):
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> void org.lwjgl.system.MemoryUtil.memSet(T,int)"""
        _MemoryUtil.memSet(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def memCopy(arg0: 'DoubleBuffer', arg1: 'DoubleBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.DoubleBuffer,java.nio.DoubleBuffer)"""
        _MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memAddress(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.ByteBuffer)"""
        return int._wrap(_MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memASCII(arg0: 'ByteBuffer', arg1: int, arg2: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCII(java.nio.ByteBuffer,int,int)"""
        return str._wrap(_MemoryUtil.memASCII(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def memAddress(arg0: 'FloatBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.FloatBuffer)"""
        return int._wrap(_MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memSet(arg0: 'LongBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.LongBuffer,int)"""
        _MemoryUtil.memSet(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def memSlice(arg0: 'LongBuffer', arg1: int, arg2: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.LongBuffer,int,int)"""
        return LongBuffer._wrap(_MemoryUtil.memSlice(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def memByteBufferNT1Safe(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT1Safe(long,int)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBufferNT1Safe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nmemAlignedAllocChecked(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemAlignedAllocChecked(long,long)"""
        return int._wrap(_MemoryUtil.nmemAlignedAllocChecked(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF16(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16(long)"""
        return str._wrap(_MemoryUtil.memUTF16(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'DoubleBuffer', arg1: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.DoubleBuffer,int)"""
        return DoubleBuffer._wrap(_MemoryUtil.memRealloc(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'ShortBuffer', arg1: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.ShortBuffer,int)"""
        return ShortBuffer._wrap(_MemoryUtil.memRealloc(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memGetByte(arg0: int) -> int:
        """public static byte org.lwjgl.system.MemoryUtil.memGetByte(long)"""
        return int._wrap(_MemoryUtil.memGetByte(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def memLongBuffer(arg0: int, arg1: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memLongBuffer(long,int)"""
        return LongBuffer._wrap(_MemoryUtil.memLongBuffer(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memASCIISafe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memASCIISafe(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryUtil.memASCIISafe(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memCalloc(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memCalloc(int,int)"""
        return ByteBuffer._wrap(_MemoryUtil.memCalloc(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'IntBuffer', arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.IntBuffer,int)"""
        return IntBuffer._wrap(_MemoryUtil.memRealloc(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memASCIISafe(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCIISafe(long)"""
        return str._wrap(_MemoryUtil.memASCIISafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'Struct') -> 'ByteBuffer':
        """public static <T extends org.lwjgl.system.Struct<T>> java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(T)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'Pointer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(org.lwjgl.system.Pointer)"""
        return int._wrap(_MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memLengthUTF16(arg0: 'CharSequence', arg1: bool) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memLengthUTF16(java.lang.CharSequence,boolean)"""
        return int._wrap(_MemoryUtil.memLengthUTF16(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.ByteBuffer)"""
        return int._wrap(_MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memPutShort(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutShort(long,short)"""
        _MemoryUtil.memPutShort(_long.valueOf(arg0), _short.valueOf(arg1))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'IntBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.IntBuffer)"""
        return int._wrap(_MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memDoubleBufferSafe(arg0: int, arg1: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memDoubleBufferSafe(long,int)"""
        return DoubleBuffer._wrap(_MemoryUtil.memDoubleBufferSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAllocDouble(arg0: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memAllocDouble(int)"""
        return DoubleBuffer._wrap(_MemoryUtil.memAllocDouble(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddress(arg0: 'ShortBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.ShortBuffer)"""
        return int._wrap(_MemoryUtil.memAddress(arg0))

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
    def memUTF16(arg0: 'ByteBuffer', arg1: int, arg2: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16(java.nio.ByteBuffer,int,int)"""
        return str._wrap(_MemoryUtil.memUTF16(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def memCallocFloat(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memCallocFloat(int)"""
        return FloatBuffer._wrap(_MemoryUtil.memCallocFloat(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memLengthNT2(arg0: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.MemoryUtil.memLengthNT2(java.nio.ByteBuffer)"""
        return int._wrap(_MemoryUtil.memLengthNT2(arg0))

    @staticmethod
    @overload
    def memGetDouble(arg0: int) -> float:
        """public static double org.lwjgl.system.MemoryUtil.memGetDouble(long)"""
        return float._wrap(_MemoryUtil.memGetDouble(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memPutInt(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutInt(long,int)"""
        _MemoryUtil.memPutInt(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def memUTF8(arg0: 'ByteBuffer', arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8(java.nio.ByteBuffer,int)"""
        return str._wrap(_MemoryUtil.memUTF8(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAllocShort(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memAllocShort(int)"""
        return ShortBuffer._wrap(_MemoryUtil.memAllocShort(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddress(arg0: 'IntBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.IntBuffer,int)"""
        return int._wrap(_MemoryUtil.memAddress(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAllocCLong(arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryUtil.memAllocCLong(int)"""
        return pygl.CLongBuffer._wrap(_MemoryUtil.memAllocCLong(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memGetShort(arg0: int) -> int:
        """public static short org.lwjgl.system.MemoryUtil.memGetShort(long)"""
        return int._wrap(_MemoryUtil.memGetShort(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memSet(arg0: 'ShortBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.ShortBuffer,int)"""
        _MemoryUtil.memSet(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def memASCII(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCII(long)"""
        return str._wrap(_MemoryUtil.memASCII(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memUTF8Safe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF8Safe(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryUtil.memUTF8Safe(arg0))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'LongBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.LongBuffer)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memAlignedAlloc(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memAlignedAlloc(int,int)"""
        return ByteBuffer._wrap(_MemoryUtil.memAlignedAlloc(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memCopy(arg0: 'ByteBuffer', arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        _MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memRealloc(arg0: 'CLongBuffer', arg1: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryUtil.memRealloc(org.lwjgl.CLongBuffer,int)"""
        return pygl.CLongBuffer._wrap(_MemoryUtil.memRealloc(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAlloc(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memAlloc(int)"""
        return ByteBuffer._wrap(_MemoryUtil.memAlloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memUTF16Safe(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16Safe(long)"""
        return str._wrap(_MemoryUtil.memUTF16Safe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmemCalloc(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemCalloc(long,long)"""
        return int._wrap(_MemoryUtil.nmemCalloc(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF8(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF8(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryUtil.memUTF8(arg0))

    @staticmethod
    @overload
    def memSlice(arg0: 'FloatBuffer') -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.FloatBuffer)"""
        return FloatBuffer._wrap(_MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memUTF8(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8(java.nio.ByteBuffer)"""
        return str._wrap(_MemoryUtil.memUTF8(arg0))

    @staticmethod
    @overload
    def memCLongBuffer(arg0: int, arg1: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryUtil.memCLongBuffer(long,int)"""
        return pygl.CLongBuffer._wrap(_MemoryUtil.memCLongBuffer(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memCallocDouble(arg0: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memCallocDouble(int)"""
        return DoubleBuffer._wrap(_MemoryUtil.memCallocDouble(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memUTF16Safe(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16Safe(java.nio.ByteBuffer)"""
        return str._wrap(_MemoryUtil.memUTF16Safe(arg0))

    @staticmethod
    @overload
    def memCopy(arg0: 'LongBuffer', arg1: 'LongBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.LongBuffer,java.nio.LongBuffer)"""
        _MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memASCIISafe(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCIISafe(java.nio.ByteBuffer)"""
        return str._wrap(_MemoryUtil.memASCIISafe(arg0))

    @staticmethod
    @overload
    def memUTF16Safe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF16Safe(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryUtil.memUTF16Safe(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF16Safe(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16Safe(long,int)"""
        return str._wrap(_MemoryUtil.memUTF16Safe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF8Safe(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8Safe(long,int)"""
        return str._wrap(_MemoryUtil.memUTF8Safe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF8(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8(long)"""
        return str._wrap(_MemoryUtil.memUTF8(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memUTF16(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF16(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryUtil.memUTF16(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'CustomBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(org.lwjgl.system.CustomBuffer<?>)"""
        return int._wrap(_MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memCopy(arg0: 'FloatBuffer', arg1: 'FloatBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        _MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memCLongBufferSafe(arg0: int, arg1: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryUtil.memCLongBufferSafe(long,int)"""
        return pygl.CLongBuffer._wrap(_MemoryUtil.memCLongBufferSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'DoubleBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.DoubleBuffer)"""
        return int._wrap(_MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memASCII(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memASCII(java.lang.CharSequence,boolean)"""
        return ByteBuffer._wrap(_MemoryUtil.memASCII(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def nmemCallocChecked(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemCallocChecked(long,long)"""
        return int._wrap(_MemoryUtil.nmemCallocChecked(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'DoubleBuffer') -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.DoubleBuffer)"""
        return DoubleBuffer._wrap(_MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memSet(arg0: 'FloatBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.FloatBuffer,int)"""
        _MemoryUtil.memSet(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def memAddress(arg0: 'CustomBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(org.lwjgl.system.CustomBuffer<?>,int)"""
        return int._wrap(_MemoryUtil.memAddress(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'ShortBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.ShortBuffer)"""
        return ShortBuffer._wrap(_MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memAddress(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.ByteBuffer,int)"""
        return int._wrap(_MemoryUtil.memAddress(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBufferNT1Safe(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT1Safe(long)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBufferNT1Safe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memByteBufferNT2Safe(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT2Safe(long,int)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBufferNT2Safe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBufferNT2(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT2(long)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBufferNT2(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmemAllocChecked(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemAllocChecked(long)"""
        return int._wrap(_MemoryUtil.nmemAllocChecked(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memUTF8Safe(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8Safe(long)"""
        return str._wrap(_MemoryUtil.memUTF8Safe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddress(arg0: 'DoubleBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.DoubleBuffer,int)"""
        return int._wrap(_MemoryUtil.memAddress(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memSlice(arg0: 'FloatBuffer', arg1: int, arg2: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.FloatBuffer,int,int)"""
        return FloatBuffer._wrap(_MemoryUtil.memSlice(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def memSlice(arg0: 'DoubleBuffer', arg1: int, arg2: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.DoubleBuffer,int,int)"""
        return DoubleBuffer._wrap(_MemoryUtil.memSlice(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'LongBuffer', arg1: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.LongBuffer,int)"""
        return LongBuffer._wrap(_MemoryUtil.memRealloc(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memIntBufferSafe(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memIntBufferSafe(long,int)"""
        return IntBuffer._wrap(_MemoryUtil.memIntBufferSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF8(arg0: 'ByteBuffer', arg1: int, arg2: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8(java.nio.ByteBuffer,int,int)"""
        return str._wrap(_MemoryUtil.memUTF8(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'FloatBuffer', arg1: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.FloatBuffer,int)"""
        return FloatBuffer._wrap(_MemoryUtil.memRealloc(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'ByteBuffer', arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.ByteBuffer,int)"""
        return ByteBuffer._wrap(_MemoryUtil.memRealloc(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAllocPointer(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryUtil.memAllocPointer(int)"""
        return pygl.PointerBuffer._wrap(_MemoryUtil.memAllocPointer(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.IntBuffer)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBuffer(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def memPutFloat(arg0: int, arg1: float):
        """public static void org.lwjgl.system.MemoryUtil.memPutFloat(long,float)"""
        _MemoryUtil.memPutFloat(_long.valueOf(arg0), _float.valueOf(arg1))

    @staticmethod
    @overload
    def memRealloc(arg0: 'PointerBuffer', arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryUtil.memRealloc(org.lwjgl.PointerBuffer,int)"""
        return pygl.PointerBuffer._wrap(_MemoryUtil.memRealloc(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF16Safe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF16Safe(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryUtil.memUTF16Safe(arg0))

    @staticmethod
    @overload
    def memGetAddress(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memGetAddress(long)"""
        return int._wrap(_MemoryUtil.memGetAddress(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memCopy(arg0: 'Struct', arg1: 'Struct'):
        """public static <T extends org.lwjgl.system.Struct<T>> void org.lwjgl.system.MemoryUtil.memCopy(T,T)"""
        _MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memUTF16(arg0: 'ByteBuffer', arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16(java.nio.ByteBuffer,int)"""
        return str._wrap(_MemoryUtil.memUTF16(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memGetCLong(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memGetCLong(long)"""
        return int._wrap(_MemoryUtil.memGetCLong(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'FloatBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.FloatBuffer)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memAllocInt(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memAllocInt(int)"""
        return IntBuffer._wrap(_MemoryUtil.memAllocInt(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memLengthASCII(arg0: 'CharSequence', arg1: bool) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memLengthASCII(java.lang.CharSequence,boolean)"""
        return int._wrap(_MemoryUtil.memLengthASCII(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memCallocInt(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memCallocInt(int)"""
        return IntBuffer._wrap(_MemoryUtil.memCallocInt(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memCallocShort(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memCallocShort(int)"""
        return ShortBuffer._wrap(_MemoryUtil.memCallocShort(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memPutAddress(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutAddress(long,long)"""
        _MemoryUtil.memPutAddress(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def memSet(arg0: 'DoubleBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.DoubleBuffer,int)"""
        _MemoryUtil.memSet(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def memSet(arg0: 'CharBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.CharBuffer,int)"""
        _MemoryUtil.memSet(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def memAddress(arg0: 'IntBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.IntBuffer)"""
        return int._wrap(_MemoryUtil.memAddress(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def memSet(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(long,int,long)"""
        _MemoryUtil.memSet(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def nmemAlignedAlloc(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemAlignedAlloc(long,long)"""
        return int._wrap(_MemoryUtil.nmemAlignedAlloc(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def memGetFloat(arg0: int) -> float:
        """public static float org.lwjgl.system.MemoryUtil.memGetFloat(long)"""
        return float._wrap(_MemoryUtil.memGetFloat(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memUTF16(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.MemoryUtil.memUTF16(java.lang.CharSequence,boolean,java.nio.ByteBuffer)"""
        return int._wrap(_MemoryUtil.memUTF16(arg0, _boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nmemAlignedFree(arg0: int):
        """public static void org.lwjgl.system.MemoryUtil.nmemAlignedFree(long)"""
        _MemoryUtil.nmemAlignedFree(_long.valueOf(arg0))

    @staticmethod
    @overload
    def memASCII(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCII(java.nio.ByteBuffer)"""
        return str._wrap(_MemoryUtil.memASCII(arg0))

    @staticmethod
    @overload
    def getAllocator(arg0: bool) -> 'MemoryAllocator':
        """public static org.lwjgl.system.MemoryUtil$MemoryAllocator org.lwjgl.system.MemoryUtil.getAllocator(boolean)"""
        return MemoryAllocator._wrap(_MemoryUtil.getAllocator(_boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def memLengthNT1(arg0: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.MemoryUtil.memLengthNT1(java.nio.ByteBuffer)"""
        return int._wrap(_MemoryUtil.memLengthNT1(arg0))

    @staticmethod
    @overload
    def memShortBuffer(arg0: int, arg1: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memShortBuffer(long,int)"""
        return ShortBuffer._wrap(_MemoryUtil.memShortBuffer(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memASCIISafe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memASCIISafe(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryUtil.memASCIISafe(arg0))

    @staticmethod
    @overload
    def memFree(arg0: 'CustomBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memFree(org.lwjgl.system.CustomBuffer<?>)"""
        _MemoryUtil.memFree(arg0)

    @staticmethod
    @overload
    def memAddress(arg0: 'LongBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.LongBuffer,int)"""
        return int._wrap(_MemoryUtil.memAddress(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memShortBufferSafe(arg0: int, arg1: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memShortBufferSafe(long,int)"""
        return ShortBuffer._wrap(_MemoryUtil.memShortBufferSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memPutCLong(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutCLong(long,long)"""
        _MemoryUtil.memPutCLong(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def memSet(arg0: 'Struct', arg1: int):
        """public static <T extends org.lwjgl.system.Struct<T>> void org.lwjgl.system.MemoryUtil.memSet(T,int)"""
        _MemoryUtil.memSet(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def memPutDouble(arg0: int, arg1: float):
        """public static void org.lwjgl.system.MemoryUtil.memPutDouble(long,double)"""
        _MemoryUtil.memPutDouble(_long.valueOf(arg0), _double.valueOf(arg1))

    @staticmethod
    @overload
    def memASCII(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.MemoryUtil.memASCII(java.lang.CharSequence,boolean,java.nio.ByteBuffer)"""
        return int._wrap(_MemoryUtil.memASCII(arg0, _boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def memCharBufferSafe(arg0: int, arg1: int) -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.system.MemoryUtil.memCharBufferSafe(long,int)"""
        return CharBuffer._wrap(_MemoryUtil.memCharBufferSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'Buffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.Buffer)"""
        return int._wrap(_MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memCopy(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(long,long,long)"""
        _MemoryUtil.memCopy(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def memGetBoolean(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MemoryUtil.memGetBoolean(long)"""
        return bool._wrap(_MemoryUtil.memGetBoolean(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memSlice(arg0: 'LongBuffer') -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.LongBuffer)"""
        return LongBuffer._wrap(_MemoryUtil.memSlice(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def memReport(arg0: 'MemoryAllocationReport', arg1: 'Aggregate', arg2: bool):
        """public static void org.lwjgl.system.MemoryUtil.memReport(org.lwjgl.system.MemoryUtil$MemoryAllocationReport,org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate,boolean)"""
        _MemoryUtil.memReport(arg0, arg1, _boolean.valueOf(arg2))

    @staticmethod
    @overload
    def memSlice(arg0: 'IntBuffer') -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.IntBuffer)"""
        return IntBuffer._wrap(_MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memPointerBuffer(arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryUtil.memPointerBuffer(long,int)"""
        return pygl.PointerBuffer._wrap(_MemoryUtil.memPointerBuffer(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memSlice(arg0: 'ShortBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.ShortBuffer)"""
        return ShortBuffer._wrap(_MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memUTF8(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer', arg3: int) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memUTF8(java.lang.CharSequence,boolean,java.nio.ByteBuffer,int)"""
        return int._wrap(_MemoryUtil.memUTF8(arg0, _boolean.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def memUTF16(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16(long,int)"""
        return str._wrap(_MemoryUtil.memUTF16(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memASCIISafe(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCIISafe(long,int)"""
        return str._wrap(_MemoryUtil.memASCIISafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBuffer(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(long,int)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBuffer(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memCalloc(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memCalloc(int)"""
        return ByteBuffer._wrap(_MemoryUtil.memCalloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memByteBufferSafe(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferSafe(long,int)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBufferSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memLengthUTF8(arg0: 'CharSequence', arg1: bool) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memLengthUTF8(java.lang.CharSequence,boolean)"""
        return int._wrap(_MemoryUtil.memLengthUTF8(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def nmemFree(arg0: int):
        """public static void org.lwjgl.system.MemoryUtil.nmemFree(long)"""
        _MemoryUtil.nmemFree(_long.valueOf(arg0))

    @staticmethod
    @overload
    def memCallocCLong(arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryUtil.memCallocCLong(int)"""
        return pygl.CLongBuffer._wrap(_MemoryUtil.memCallocCLong(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memSet(arg0: 'IntBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.IntBuffer,int)"""
        _MemoryUtil.memSet(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def memGetInt(arg0: int) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memGetInt(long)"""
        return int._wrap(_MemoryUtil.memGetInt(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddress(arg0: 'CharBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.CharBuffer,int)"""
        return int._wrap(_MemoryUtil.memAddress(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'DoubleBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.DoubleBuffer)"""
        return int._wrap(_MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memCopy(arg0: 'IntBuffer', arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.IntBuffer,java.nio.IntBuffer)"""
        _MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memUTF8(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8(long,int)"""
        return str._wrap(_MemoryUtil.memUTF8(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memSlice(arg0: 'IntBuffer', arg1: int, arg2: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.IntBuffer,int,int)"""
        return IntBuffer._wrap(_MemoryUtil.memSlice(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def nmemRealloc(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemRealloc(long,long)"""
        return int._wrap(_MemoryUtil.nmemRealloc(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def memSlice(arg0: 'DoubleBuffer') -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.DoubleBuffer)"""
        return DoubleBuffer._wrap(_MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'CustomBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(org.lwjgl.system.CustomBuffer<?>)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memASCII(arg0: 'ByteBuffer', arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCII(java.nio.ByteBuffer,int)"""
        return str._wrap(_MemoryUtil.memASCII(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memPutLong(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutLong(long,long)"""
        _MemoryUtil.memPutLong(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def memCopy(arg0: 'CharBuffer', arg1: 'CharBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.CharBuffer,java.nio.CharBuffer)"""
        _MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'CharBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.CharBuffer)"""
        return int._wrap(_MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memSlice(arg0: 'CharBuffer') -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.CharBuffer)"""
        return CharBuffer._wrap(_MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memUTF16(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer', arg3: int) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memUTF16(java.lang.CharSequence,boolean,java.nio.ByteBuffer,int)"""
        return int._wrap(_MemoryUtil.memUTF16(arg0, _boolean.valueOf(arg1), arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def memGlobalRefToObject(arg0: int) -> object:
        """public static native <T> T org.lwjgl.system.MemoryUtil.memGlobalRefToObject(long)"""
        return object._wrap(_MemoryUtil.memGlobalRefToObject(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memIntBuffer(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memIntBuffer(long,int)"""
        return IntBuffer._wrap(_MemoryUtil.memIntBuffer(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'CharBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.CharBuffer)"""
        return int._wrap(_MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memCharBuffer(arg0: int, arg1: int) -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.system.MemoryUtil.memCharBuffer(long,int)"""
        return CharBuffer._wrap(_MemoryUtil.memCharBuffer(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBufferNT2Safe(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT2Safe(long)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBufferNT2Safe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memByteBufferNT2(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT2(long,int)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBufferNT2(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nmemReallocChecked(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemReallocChecked(long,long)"""
        return int._wrap(_MemoryUtil.nmemReallocChecked(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def memAllocFloat(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memAllocFloat(int)"""
        return FloatBuffer._wrap(_MemoryUtil.memAllocFloat(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def memPointerBufferSafe(arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryUtil.memPointerBufferSafe(long,int)"""
        return pygl.PointerBuffer._wrap(_MemoryUtil.memPointerBufferSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'ShortBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.ShortBuffer,int)"""
        return int._wrap(_MemoryUtil.memAddress(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memLongBufferSafe(arg0: int, arg1: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memLongBufferSafe(long,int)"""
        return LongBuffer._wrap(_MemoryUtil.memLongBufferSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF16(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF16(java.lang.CharSequence)"""
        return ByteBuffer._wrap(_MemoryUtil.memUTF16(arg0))

    @staticmethod
    @overload
    def memUTF8Safe(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8Safe(java.nio.ByteBuffer)"""
        return str._wrap(_MemoryUtil.memUTF8Safe(arg0))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'ShortBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.ShortBuffer)"""
        return int._wrap(_MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memSlice(arg0: 'CustomBuffer', arg1: int, arg2: int) -> 'CustomBuffer':
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> T org.lwjgl.system.MemoryUtil.memSlice(T,int,int)"""
        return CustomBuffer._wrap(_MemoryUtil.memSlice(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def memCopy(arg0: 'CustomBuffer', arg1: 'CustomBuffer'):
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> void org.lwjgl.system.MemoryUtil.memCopy(T,T)"""
        _MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memSet(arg0: 'ByteBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.ByteBuffer,int)"""
        _MemoryUtil.memSet(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def memFree(arg0: 'Buffer'):
        """public static void org.lwjgl.system.MemoryUtil.memFree(java.nio.Buffer)"""
        _MemoryUtil.memFree(arg0)

    @staticmethod
    @overload
    def memByteBufferNT1(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT1(long)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBufferNT1(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'CharBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.CharBuffer)"""
        return ByteBuffer._wrap(_MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'CharBuffer') -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.CharBuffer)"""
        return CharBuffer._wrap(_MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memCopy(arg0: 'ShortBuffer', arg1: 'ShortBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.ShortBuffer,java.nio.ShortBuffer)"""
        _MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memASCII(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCII(long,int)"""
        return str._wrap(_MemoryUtil.memASCII(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF16(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16(java.nio.ByteBuffer)"""
        return str._wrap(_MemoryUtil.memUTF16(arg0))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'FloatBuffer') -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.FloatBuffer)"""
        return FloatBuffer._wrap(_MemoryUtil.memDuplicate(arg0)) 
 
 
# CLASS: org.lwjgl.system.APIUtil$APIVersion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.lwjgl.system.APIUtil as _APIUtil_APIVersion
_APIVersion = _APIUtil_APIVersion.APIVersion
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class APIVersion():
    """org.lwjgl.system.APIUtil.APIVersion"""
 
    @staticmethod
    def _wrap(java_value: _APIVersion) -> 'APIVersion':
        return APIVersion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _APIVersion):
        """
        Dynamic initializer for APIVersion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_APIVersion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_APIVersion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.APIUtil$APIVersion.equals(java.lang.Object)"""
        return bool._wrap(super(_APIVersion, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: str, arg3: str):
        """public org.lwjgl.system.APIUtil$APIVersion(int,int,java.lang.String,java.lang.String)"""
        val = _APIVersion(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.APIUtil$APIVersion.hashCode()"""
        return int._wrap(super(APIVersion, self).hashCode())

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

    @overload
    def compareTo(self, arg0: 'APIVersion') -> int:
        """public int org.lwjgl.system.APIUtil$APIVersion.compareTo(org.lwjgl.system.APIUtil$APIVersion)"""
        return int._wrap(super(_APIVersion, self).compareTo(arg0))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.APIUtil$APIVersion(int,int)"""
        val = _APIVersion(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.APIUtil$APIVersion.toString()"""
        return str._wrap(super(APIVersion, self).toString())