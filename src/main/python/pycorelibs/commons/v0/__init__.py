from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Float as _float
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import java.lang.Byte as _byte
import dev.ultreon.libs.commons.v0.Color as _Color
_Color = _Color
import java.math.BigDecimal as BigDecimal
import dev.ultreon.libs.commons.v0.Mth as _Mth
_Mth = _Mth
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Mth():
    """dev.ultreon.libs.commons.v0.Mth"""
 
    @staticmethod
    def _wrap(java_value: _Mth) -> 'Mth':
        return Mth(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Mth):
        """
        Dynamic initializer for Mth.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Mth__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Mth__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static short dev.ultreon.libs.commons.v0.Mth.clamp(short,int,int)"""
        return int._wrap(_Mth.clamp(_short.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.Mth()"""
        val = _Mth()
        self.__wrapper = val

    @staticmethod
    @overload
    def lerp(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.lerp(double,double,double)"""
        return float._wrap(_Mth.lerp(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def mixColors(arg0: 'Color', arg1: 'Color', arg2: float) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Mth.mixColors(dev.ultreon.libs.commons.v0.Color,dev.ultreon.libs.commons.v0.Color,double)"""
        return Color._wrap(_Mth.mixColors(arg0, arg1, _double.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.Mth()"""
        val = _Mth()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def diff(arg0: float, arg1: float) -> float:
        """public static float dev.ultreon.libs.commons.v0.Mth.diff(float,float)"""
        return float._wrap(_Mth.diff(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static byte dev.ultreon.libs.commons.v0.Mth.diff(byte,byte)"""
        return int._wrap(_Mth.diff(_byte.valueOf(arg0), _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static short dev.ultreon.libs.commons.v0.Mth.diff(short,short)"""
        return int._wrap(_Mth.diff(_short.valueOf(arg0), _short.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def clamp(clamp) -> 'BigInteger':
        """public static java.math.BigInteger dev.ultreon.libs.commons.v0.Mth.clamp(java.math.BigInteger,java.math.BigInteger,java.math.BigInteger)"""
        return _transform(_arg0, arg1, arg2.Mth(arg0: 'BigInteger', arg1: 'BigInteger', arg2: 'BigInteger')).'BigInteger'Value()

    @staticmethod
    @overload
    def clamp(arg0: float, arg1: float, arg2: float) -> float:
        """public static float dev.ultreon.libs.commons.v0.Mth.clamp(float,float,float)"""
        return float._wrap(_Mth.clamp(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static long dev.ultreon.libs.commons.v0.Mth.diff(long,long)"""
        return int._wrap(_Mth.diff(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static int dev.ultreon.libs.commons.v0.Mth.diff(int,int)"""
        return int._wrap(_Mth.diff(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def round(arg0: float, arg1: int) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.round(double,int)"""
        return float._wrap(_Mth.round(_double.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def clamp(clamp) -> 'BigDecimal':
        """public static java.math.BigDecimal dev.ultreon.libs.commons.v0.Mth.clamp(java.math.BigDecimal,java.math.BigDecimal,java.math.BigDecimal)"""
        return _transform(_arg0, arg1, arg2.Mth(arg0: 'BigDecimal', arg1: 'BigDecimal', arg2: 'BigDecimal')).'BigDecimal'Value()

    @staticmethod
    @overload
    def diff(arg0: float, arg1: float) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.diff(double,double)"""
        return float._wrap(_Mth.diff(_double.valueOf(arg0), _double.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def clamp(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.clamp(double,double,double)"""
        return float._wrap(_Mth.clamp(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static byte dev.ultreon.libs.commons.v0.Mth.clamp(byte,int,int)"""
        return int._wrap(_Mth.clamp(_byte.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static long dev.ultreon.libs.commons.v0.Mth.clamp(long,long,long)"""
        return int._wrap(_Mth.clamp(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static int dev.ultreon.libs.commons.v0.Mth.clamp(int,int,int)"""
        return int._wrap(_Mth.clamp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def root(arg0: int, arg1: int) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.root(int,int)"""
        return float._wrap(_Mth.root(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Mth
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Float as _float
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import java.lang.Byte as _byte
import dev.ultreon.libs.commons.v0.Color as _Color
_Color = _Color
import java.math.BigDecimal as BigDecimal
import dev.ultreon.libs.commons.v0.Mth as _Mth
_Mth = _Mth
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Mth():
    """dev.ultreon.libs.commons.v0.Mth"""
 
    @staticmethod
    def _wrap(java_value: _Mth) -> 'Mth':
        return Mth(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Mth):
        """
        Dynamic initializer for Mth.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Mth__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Mth__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static short dev.ultreon.libs.commons.v0.Mth.clamp(short,int,int)"""
        return int._wrap(_Mth.clamp(_short.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.Mth()"""
        val = _Mth()
        self.__wrapper = val

    @staticmethod
    @overload
    def lerp(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.lerp(double,double,double)"""
        return float._wrap(_Mth.lerp(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def mixColors(arg0: 'Color', arg1: 'Color', arg2: float) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Mth.mixColors(dev.ultreon.libs.commons.v0.Color,dev.ultreon.libs.commons.v0.Color,double)"""
        return Color._wrap(_Mth.mixColors(arg0, arg1, _double.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.Mth()"""
        val = _Mth()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def diff(arg0: float, arg1: float) -> float:
        """public static float dev.ultreon.libs.commons.v0.Mth.diff(float,float)"""
        return float._wrap(_Mth.diff(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static byte dev.ultreon.libs.commons.v0.Mth.diff(byte,byte)"""
        return int._wrap(_Mth.diff(_byte.valueOf(arg0), _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static short dev.ultreon.libs.commons.v0.Mth.diff(short,short)"""
        return int._wrap(_Mth.diff(_short.valueOf(arg0), _short.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def clamp(clamp) -> 'BigInteger':
        """public static java.math.BigInteger dev.ultreon.libs.commons.v0.Mth.clamp(java.math.BigInteger,java.math.BigInteger,java.math.BigInteger)"""
        return _transform(_arg0, arg1, arg2.Mth(arg0: 'BigInteger', arg1: 'BigInteger', arg2: 'BigInteger')).'BigInteger'Value()

    @staticmethod
    @overload
    def clamp(arg0: float, arg1: float, arg2: float) -> float:
        """public static float dev.ultreon.libs.commons.v0.Mth.clamp(float,float,float)"""
        return float._wrap(_Mth.clamp(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static long dev.ultreon.libs.commons.v0.Mth.diff(long,long)"""
        return int._wrap(_Mth.diff(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static int dev.ultreon.libs.commons.v0.Mth.diff(int,int)"""
        return int._wrap(_Mth.diff(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def round(arg0: float, arg1: int) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.round(double,int)"""
        return float._wrap(_Mth.round(_double.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def clamp(clamp) -> 'BigDecimal':
        """public static java.math.BigDecimal dev.ultreon.libs.commons.v0.Mth.clamp(java.math.BigDecimal,java.math.BigDecimal,java.math.BigDecimal)"""
        return _transform(_arg0, arg1, arg2.Mth(arg0: 'BigDecimal', arg1: 'BigDecimal', arg2: 'BigDecimal')).'BigDecimal'Value()

    @staticmethod
    @overload
    def diff(arg0: float, arg1: float) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.diff(double,double)"""
        return float._wrap(_Mth.diff(_double.valueOf(arg0), _double.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def clamp(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.clamp(double,double,double)"""
        return float._wrap(_Mth.clamp(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static byte dev.ultreon.libs.commons.v0.Mth.clamp(byte,int,int)"""
        return int._wrap(_Mth.clamp(_byte.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static long dev.ultreon.libs.commons.v0.Mth.clamp(long,long,long)"""
        return int._wrap(_Mth.clamp(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static int dev.ultreon.libs.commons.v0.Mth.clamp(int,int,int)"""
        return int._wrap(_Mth.clamp(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

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
    def root(arg0: int, arg1: int) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.root(int,int)"""
        return float._wrap(_Mth.root(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Mth 
 
 
# CLASS: dev.ultreon.libs.commons.v0.VersionType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.commons.v0.VersionType as _VersionType
_VersionType = _VersionType
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
 
class VersionType():
    """dev.ultreon.libs.commons.v0.VersionType"""
 
    @staticmethod
    def _wrap(java_value: _VersionType) -> 'VersionType':
        return VersionType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VersionType):
        """
        Dynamic initializer for VersionType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VersionType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VersionType__wrapper":
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
        """public java.lang.String dev.ultreon.libs.commons.v0.VersionType.toString()"""
        return str._wrap(super(VersionType, self).toString())

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

    @overload
    def toRepresentation(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.VersionType.toRepresentation()"""
        return str._wrap(super(VersionType, self).toRepresentation())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.VersionType.getName()"""
        return str._wrap(super(VersionType, self).getName())

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
    def valueOf(arg0: str) -> 'VersionType':
        """public static dev.ultreon.libs.commons.v0.VersionType dev.ultreon.libs.commons.v0.VersionType.valueOf(java.lang.String)"""
        return VersionType._wrap(_VersionType.valueOf(arg0))

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
    def values() -> List['VersionType']:
        """public static dev.ultreon.libs.commons.v0.VersionType[] dev.ultreon.libs.commons.v0.VersionType.values()"""
        return List[VersionType]._wrap(_VersionType.values()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Logger$Level
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.commons.v0.Logger as _Logger_Level
_Level = _Logger_Level.Level
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
 
class Level():
    """dev.ultreon.libs.commons.v0.Logger.Level"""
 
    @staticmethod
    def _wrap(java_value: _Level) -> 'Level':
        return Level(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Level):
        """
        Dynamic initializer for Level.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Level__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Level__wrapper":
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

    @staticmethod
    @overload
    def values() -> List['Level']:
        """public static dev.ultreon.libs.commons.v0.Logger$Level[] dev.ultreon.libs.commons.v0.Logger$Level.values()"""
        return List[Level]._wrap(_Level.values())

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
    def valueOf(arg0: str) -> 'Level':
        """public static dev.ultreon.libs.commons.v0.Logger$Level dev.ultreon.libs.commons.v0.Logger$Level.valueOf(java.lang.String)"""
        return Level._wrap(_Level.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Color
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.Color as _Color
_Color = _Color
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Color():
    """dev.ultreon.libs.commons.v0.Color"""
 
    @staticmethod
    def _wrap(java_value: _Color) -> 'Color':
        return Color(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Color):
        """
        Dynamic initializer for Color.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Color__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Color__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def hsb(arg0: float, arg1: float, arg2: float) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.hsb(float,float,float)"""
        return Color._wrap(_Color.hsb(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def toAwt(self) -> 'Color':
        """public java.awt.Color dev.ultreon.libs.commons.v0.Color.toAwt()"""
        return 'Color'._wrap(super(Color, self).toAwt())

    @overload
    def withRed(self, arg0: int) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.withRed(int)"""
        return 'Color'._wrap(super(_Color, self).withRed(_int.valueOf(arg0)))

    @overload
    def getBlue(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getBlue()"""
        return int._wrap(super(Color, self).getBlue())

    @overload
    def withBlue(self, arg0: int) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.withBlue(int)"""
        return 'Color'._wrap(super(_Color, self).withBlue(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def abgr(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.abgr(int)"""
        return Color._wrap(_Color.abgr(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def rgba(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgba(int)"""
        return Color._wrap(_Color.rgba(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def hex(arg0: str) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.hex(java.lang.String)"""
        return Color._wrap(_Color.hex(arg0))

    @overload
    def darker(self) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.darker()"""
        return 'Color'._wrap(super(Color, self).darker())

    @staticmethod
    @overload
    def awt(arg0: 'Color') -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.awt(java.awt.Color)"""
        return Color._wrap(_Color.awt(arg0))

    @staticmethod
    @overload
    def rgb(arg0: float, arg1: float, arg2: float) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgb(float,float,float)"""
        return Color._wrap(_Color.rgb(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

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
    def brighter(self) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.brighter()"""
        return 'Color'._wrap(super(Color, self).brighter())

    @staticmethod
    @overload
    def bgr(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.bgr(int)"""
        return Color._wrap(_Color.bgr(_int.valueOf(arg0)))

    @overload
    def getGreen(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getGreen()"""
        return int._wrap(super(Color, self).getGreen())

    @overload
    def withGreen(self, arg0: int) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.withGreen(int)"""
        return 'Color'._wrap(super(_Color, self).withGreen(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def rgb(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgb(int)"""
        return Color._wrap(_Color.rgb(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def withAlpha(self, arg0: int) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.withAlpha(int)"""
        return 'Color'._wrap(super(_Color, self).withAlpha(_int.valueOf(arg0)))

    @overload
    def getRed(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getRed()"""
        return int._wrap(super(Color, self).getRed())

    @overload
    def getRgb(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getRgb()"""
        return int._wrap(super(Color, self).getRgb())

    @staticmethod
    @overload
    def rgba(arg0: float, arg1: float, arg2: float, arg3: float) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgba(float,float,float,float)"""
        return Color._wrap(_Color.rgba(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def getAlpha(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getAlpha()"""
        return int._wrap(super(Color, self).getAlpha())

    @staticmethod
    @overload
    def bgra(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.bgra(int)"""
        return Color._wrap(_Color.bgra(_int.valueOf(arg0)))

    @overload
    def getTransparency(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getTransparency()"""
        return int._wrap(super(Color, self).getTransparency())

    @staticmethod
    @overload
    def rgb(arg0: int, arg1: int, arg2: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgb(int,int,int)"""
        return Color._wrap(_Color.rgb(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def argb(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.argb(int)"""
        return Color._wrap(_Color.argb(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Color.toString()"""
        return str._wrap(super(Color, self).toString())

    @staticmethod
    @overload
    def rgba(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgba(int,int,int,int)"""
        return Color._wrap(_Color.rgba(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Pixel
from builtins import str
from pyquantum_helper import override
import java.awt.Point as _Point
_Point = _Point
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.awt.Point as Point
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.Pixel as _Pixel
_Pixel = _Pixel
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.Color as _Color
_Color = _Color
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Pixel():
    """dev.ultreon.libs.commons.v0.Pixel"""
 
    @staticmethod
    def _wrap(java_value: _Pixel) -> 'Pixel':
        return Pixel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pixel):
        """
        Dynamic initializer for Pixel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pixel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pixel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getX(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Pixel.getX()"""
        return int._wrap(super(Pixel, self).getX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getPos(self) -> 'Point':
        """public java.awt.Point dev.ultreon.libs.commons.v0.Pixel.getPos()"""
        return 'Point'._wrap(super(Pixel, self).getPos())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getColor(self) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Pixel.getColor()"""
        return 'Color'._wrap(super(Pixel, self).getColor())

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
    def __init__(self, arg0: int, arg1: int, arg2: 'Color'):
        """public dev.ultreon.libs.commons.v0.Pixel(int,int,dev.ultreon.libs.commons.v0.Color)"""
        val = _Pixel(_int.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Pixel.getY()"""
        return int._wrap(super(Pixel, self).getY())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Point', arg1: 'Color'):
        """public dev.ultreon.libs.commons.v0.Pixel(java.awt.Point,dev.ultreon.libs.commons.v0.Color)"""
        val = _Pixel(arg0, arg1)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.DummyMessenger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import dev.ultreon.libs.commons.v0.MessengerImpl as _MessengerImpl
_MessengerImpl = _MessengerImpl
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.DummyMessenger as _DummyMessenger
_DummyMessenger = _DummyMessenger
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DummyMessenger():
    """dev.ultreon.libs.commons.v0.DummyMessenger"""
 
    @staticmethod
    def _wrap(java_value: _DummyMessenger) -> 'DummyMessenger':
        return DummyMessenger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DummyMessenger):
        """
        Dynamic initializer for DummyMessenger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DummyMessenger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DummyMessenger__wrapper":
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
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.DummyMessenger()"""
        val = _DummyMessenger()
        self.__wrapper = val

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
    def send(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.MessengerImpl.send(java.lang.String)"""
        super(_MessengerImpl, self).send(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.DummyMessenger()"""
        val = _DummyMessenger()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.Either
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
from builtins import bool
import dev.ultreon.libs.commons.v0.Either as _Either
_Either = _Either
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Either():
    """dev.ultreon.libs.commons.v0.Either"""
 
    @staticmethod
    def _wrap(java_value: _Either) -> 'Either':
        return Either(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Either):
        """
        Dynamic initializer for Either.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Either__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Either__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def ifAny(self, arg0: 'Consumer', arg1: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Either.ifAny(java.util.function.Consumer<L>,java.util.function.Consumer<R>)"""
        super(_Either, self).ifAny(arg0, arg1)

    @staticmethod
    @overload
    def right(arg0: object) -> 'Either':
        """public static <L,R> dev.ultreon.libs.commons.v0.Either<L, R> dev.ultreon.libs.commons.v0.Either.right(R)"""
        return Either._wrap(_Either.right(arg0))

    @overload
    def ifRightOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.libs.commons.v0.Either.ifRightOrElse(java.util.function.Consumer<R>,java.lang.Runnable)"""
        super(_Either, self).ifRightOrElse(arg0, arg1)

    @overload
    def isLeftPresent(self) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Either.isLeftPresent()"""
        return bool._wrap(super(Either, self).isLeftPresent())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def ifLeft(self, arg0: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Either.ifLeft(java.util.function.Consumer<L>)"""
        super(_Either, self).ifLeft(arg0)

    @overload
    def getLeftOrNullOr(self, arg0: object) -> object:
        """public L dev.ultreon.libs.commons.v0.Either.getLeftOrNullOr(L)"""
        return object._wrap(super(_Either, self).getLeftOrNullOr(arg0))

    @overload
    def ifRight(self, arg0: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Either.ifRight(java.util.function.Consumer<R>)"""
        super(_Either, self).ifRight(arg0)

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
    def getRightOrNullOr(self, arg0: 'Supplier') -> object:
        """public R dev.ultreon.libs.commons.v0.Either.getRightOrNullOr(java.util.function.Supplier<? extends R>)"""
        return object._wrap(super(_Either, self).getRightOrNullOr(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def ifLeftOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.libs.commons.v0.Either.ifLeftOrElse(java.util.function.Consumer<L>,java.lang.Runnable)"""
        super(_Either, self).ifLeftOrElse(arg0, arg1)

    @overload
    def getLeftOrNull(self) -> object:
        """public L dev.ultreon.libs.commons.v0.Either.getLeftOrNull()"""
        return object._wrap(super(Either, self).getLeftOrNull())

    @overload
    def getLeft(self) -> object:
        """public L dev.ultreon.libs.commons.v0.Either.getLeft()"""
        return object._wrap(super(Either, self).getLeft())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getLeftOrNullOrGet(self, arg0: 'Supplier') -> object:
        """public L dev.ultreon.libs.commons.v0.Either.getLeftOrNullOrGet(java.util.function.Supplier<? extends L>)"""
        return object._wrap(super(_Either, self).getLeftOrNullOrGet(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getRightOrNull(self) -> object:
        """public R dev.ultreon.libs.commons.v0.Either.getRightOrNull()"""
        return object._wrap(super(Either, self).getRightOrNull())

    @staticmethod
    @overload
    def left(arg0: object) -> 'Either':
        """public static <L,R> dev.ultreon.libs.commons.v0.Either<L, R> dev.ultreon.libs.commons.v0.Either.left(L)"""
        return Either._wrap(_Either.left(arg0))

    @overload
    def getRightOrNullOr(self, arg0: object) -> object:
        """public R dev.ultreon.libs.commons.v0.Either.getRightOrNullOr(R)"""
        return object._wrap(super(_Either, self).getRightOrNullOr(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getRight(self) -> object:
        """public R dev.ultreon.libs.commons.v0.Either.getRight()"""
        return object._wrap(super(Either, self).getRight())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isRightPresent(self) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Either.isRightPresent()"""
        return bool._wrap(super(Either, self).isRightPresent())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Profiler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.Runnable as Runnable
import dev.ultreon.libs.commons.v0.Profiler as _Profiler
_Profiler = _Profiler
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Profiler():
    """dev.ultreon.libs.commons.v0.Profiler"""
 
    @staticmethod
    def _wrap(java_value: _Profiler) -> 'Profiler':
        return Profiler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Profiler):
        """
        Dynamic initializer for Profiler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Profiler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Profiler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def start(self):
        """public void dev.ultreon.libs.commons.v0.Profiler.start()"""
        super(Profiler, self).start()

    @overload
    def end(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Long> dev.ultreon.libs.commons.v0.Profiler.end()"""
        return 'Map'._wrap(super(Profiler, self).end())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.Profiler()"""
        val = _Profiler()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def startSection(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.Profiler.startSection(java.lang.String)"""
        super(_Profiler, self).startSection(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def section(self, arg0: str, arg1: 'Runnable'):
        """public void dev.ultreon.libs.commons.v0.Profiler.section(java.lang.String,java.lang.Runnable)"""
        super(_Profiler, self).section(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.Profiler()"""
        val = _Profiler()
        self.__wrapper = val

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
    def endSection(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.Profiler.endSection(java.lang.String)"""
        super(_Profiler, self).endSection(arg0)

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.Percentage
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.Percentage as _Percentage
_Percentage = _Percentage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Percentage():
    """dev.ultreon.libs.commons.v0.Percentage"""
 
    @staticmethod
    def _wrap(java_value: _Percentage) -> 'Percentage':
        return Percentage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Percentage):
        """
        Dynamic initializer for Percentage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Percentage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Percentage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Percentage.equals(java.lang.Object)"""
        return bool._wrap(super(_Percentage, self).equals(arg0))

    @staticmethod
    @overload
    def toPercentage(arg0: float) -> 'Percentage':
        """public static dev.ultreon.libs.commons.v0.Percentage dev.ultreon.libs.commons.v0.Percentage.toPercentage(double)"""
        return Percentage._wrap(_Percentage.toPercentage(_double.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def percentage(self) -> float:
        """public double dev.ultreon.libs.commons.v0.Percentage.percentage()"""
        return float._wrap(super(Percentage, self).percentage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Percentage.toString()"""
        return str._wrap(super(Percentage, self).toString())

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
    def __init__(self, arg0: float):
        """public dev.ultreon.libs.commons.v0.Percentage(double)"""
        val = _Percentage(_double.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compareTo(self, arg0: 'Percentage') -> int:
        """public int dev.ultreon.libs.commons.v0.Percentage.compareTo(dev.ultreon.libs.commons.v0.Percentage)"""
        return int._wrap(super(_Percentage, self).compareTo(arg0))

    @overload
    def value(self) -> float:
        """public double dev.ultreon.libs.commons.v0.Percentage.value()"""
        return float._wrap(super(Percentage, self).value())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.ValueAnimator
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.libs.commons.v0.ValueAnimator as _ValueAnimator
_ValueAnimator = _ValueAnimator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ValueAnimator():
    """dev.ultreon.libs.commons.v0.ValueAnimator"""
 
    @staticmethod
    def _wrap(java_value: _ValueAnimator) -> 'ValueAnimator':
        return ValueAnimator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValueAnimator):
        """
        Dynamic initializer for ValueAnimator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValueAnimator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValueAnimator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.libs.commons.v0.ValueAnimator(double,double,double)"""
        val = _ValueAnimator(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))
        self.__wrapper = val

    @overload
    def isEnded(self) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.ValueAnimator.isEnded()"""
        return bool._wrap(super(ValueAnimator, self).isEnded())

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
    def animate(self) -> float:
        """public double dev.ultreon.libs.commons.v0.ValueAnimator.animate()"""
        return float._wrap(super(ValueAnimator, self).animate())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def start(self):
        """public void dev.ultreon.libs.commons.v0.ValueAnimator.start()"""
        super(ValueAnimator, self).start()

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.Messenger
import dev.ultreon.libs.commons.v0.Messenger as _Messenger
_Messenger = _Messenger
from abc import abstractmethod, ABC
 
class Messenger():
    """dev.ultreon.libs.commons.v0.Messenger"""
 
    @staticmethod
    def _wrap(java_value: _Messenger) -> 'Messenger':
        return Messenger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Messenger):
        """
        Dynamic initializer for Messenger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Messenger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Messenger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def send(self, arg0: str):
        """public abstract void dev.ultreon.libs.commons.v0.Messenger.send(java.lang.String)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.commons.v0.UtilityClass
from builtins import str
import dev.ultreon.libs.commons.v0.UtilityClass as _UtilityClass
_UtilityClass = _UtilityClass
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
 
class UtilityClass():
    """dev.ultreon.libs.commons.v0.UtilityClass"""
 
    @staticmethod
    def _wrap(java_value: _UtilityClass) -> 'UtilityClass':
        return UtilityClass(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UtilityClass):
        """
        Dynamic initializer for UtilityClass.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UtilityClass__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UtilityClass__wrapper":
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
 
 
# CLASS: dev.ultreon.libs.commons.v0.Downloader
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
from builtins import float
import dev.ultreon.libs.commons.v0.IDownloader as _IDownloader
_IDownloader = _IDownloader
import java.lang.String as _String
_String = _String
import java.net.URL as URL
import dev.ultreon.libs.commons.v0.Downloader as _Downloader
_Downloader = _Downloader
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import java.util.concurrent.CompletableFuture as _CompletableFuture
_CompletableFuture = _CompletableFuture
from builtins import bool
import java.util.concurrent.CompletableFuture as CompletableFuture
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Downloader():
    """dev.ultreon.libs.commons.v0.Downloader"""
 
    @staticmethod
    def _wrap(java_value: _Downloader) -> 'Downloader':
        return Downloader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Downloader):
        """
        Dynamic initializer for Downloader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Downloader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Downloader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def downloadSync(self):
        """public void dev.ultreon.libs.commons.v0.Downloader.downloadSync() throws java.io.IOException"""
        super(Downloader, self).downloadSync()

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
    def downloadAsync(self) -> 'CompletableFuture':
        """public default java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.libs.commons.v0.IDownloader.downloadAsync()"""
        return 'CompletableFuture'._wrap(super(IDownloader, self).downloadAsync())

    @overload
    def __init__(self, arg0: 'URL', arg1: 'OutputStream', arg2: int):
        """public dev.ultreon.libs.commons.v0.Downloader(java.net.URL,java.io.OutputStream,int)"""
        val = _Downloader(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getBlockSize(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Downloader.getBlockSize()"""
        return int._wrap(super(Downloader, self).getBlockSize())

    @overload
    def __init__(self, arg0: 'URL', arg1: 'File', arg2: int):
        """public dev.ultreon.libs.commons.v0.Downloader(java.net.URL,java.io.File,int) throws java.io.IOException"""
        val = _Downloader(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getLength(self) -> int:
        """public long dev.ultreon.libs.commons.v0.Downloader.getLength()"""
        return int._wrap(super(Downloader, self).getLength())

    @override
    @overload
    def getRatio(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Downloader.getRatio()"""
        return float._wrap(super(Downloader, self).getRatio())

    @override
    @overload
    def getBytesDownloaded(self) -> int:
        """public long dev.ultreon.libs.commons.v0.Downloader.getBytesDownloaded()"""
        return int._wrap(super(Downloader, self).getBytesDownloaded())

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
    def getPercent(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Downloader.getPercent()"""
        return float._wrap(super(Downloader, self).getPercent())

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.IDownloader
import dev.ultreon.libs.commons.v0.IDownloader as _IDownloader
_IDownloader = _IDownloader
import java.util.concurrent.CompletableFuture as _CompletableFuture
_CompletableFuture = _CompletableFuture
from abc import abstractmethod, ABC
import java.util.concurrent.CompletableFuture as CompletableFuture
 
class IDownloader():
    """dev.ultreon.libs.commons.v0.IDownloader"""
 
    @staticmethod
    def _wrap(java_value: _IDownloader) -> 'IDownloader':
        return IDownloader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IDownloader):
        """
        Dynamic initializer for IDownloader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IDownloader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IDownloader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getBlockSize(self, ):
        """public abstract int dev.ultreon.libs.commons.v0.IDownloader.getBlockSize()"""
        pass

    @overload
    def downloadAsync(self) -> 'CompletableFuture':
        """public default java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.libs.commons.v0.IDownloader.downloadAsync()"""
        return 'CompletableFuture'._wrap(super(IDownloader, self).downloadAsync())

    @abstractmethod
    def downloadSync(self, ):
        """public abstract void dev.ultreon.libs.commons.v0.IDownloader.downloadSync() throws java.io.IOException,java.lang.InterruptedException"""
        pass

    @abstractmethod
    def getPercent(self, ):
        """public abstract float dev.ultreon.libs.commons.v0.IDownloader.getPercent()"""
        pass

    @abstractmethod
    def getRatio(self, ):
        """public abstract float dev.ultreon.libs.commons.v0.IDownloader.getRatio()"""
        pass

    @abstractmethod
    def getLength(self, ):
        """public abstract long dev.ultreon.libs.commons.v0.IDownloader.getLength()"""
        pass

    @abstractmethod
    def getBytesDownloaded(self, ):
        """public abstract long dev.ultreon.libs.commons.v0.IDownloader.getBytesDownloaded()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Anchor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import dev.ultreon.libs.commons.v0.Anchor as _Anchor
_Anchor = _Anchor
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
 
class Anchor():
    """dev.ultreon.libs.commons.v0.Anchor"""
 
    @staticmethod
    def _wrap(java_value: _Anchor) -> 'Anchor':
        return Anchor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Anchor):
        """
        Dynamic initializer for Anchor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Anchor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Anchor__wrapper":
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

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Anchor.getX()"""
        return int._wrap(super(Anchor, self).getX())

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
    def valueOf(arg0: str) -> 'Anchor':
        """public static dev.ultreon.libs.commons.v0.Anchor dev.ultreon.libs.commons.v0.Anchor.valueOf(java.lang.String)"""
        return Anchor._wrap(_Anchor.valueOf(arg0))

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Anchor.getY()"""
        return int._wrap(super(Anchor, self).getY())

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
    def values() -> List['Anchor']:
        """public static dev.ultreon.libs.commons.v0.Anchor[] dev.ultreon.libs.commons.v0.Anchor.values()"""
        return List[Anchor]._wrap(_Anchor.values()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Insets
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.libs.commons.v0.Insets as _Insets
_Insets = _Insets
import java.lang.Integer as _int
import java.awt.Insets as _Insets
_Insets = _Insets
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Insets():
    """dev.ultreon.libs.commons.v0.Insets"""
 
    @staticmethod
    def _wrap(java_value: _Insets) -> 'Insets':
        return Insets(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Insets):
        """
        Dynamic initializer for Insets.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Insets__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Insets__wrapper":
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.awt.Insets.toString()"""
        return str._wrap(super(Insets, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.libs.commons.v0.Insets(int,int,int,int)"""
        val = _Insets(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.awt.Insets.equals(java.lang.Object)"""
        return bool._wrap(super(_Insets, self).equals(arg0))

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.awt.Insets.clone()"""
        return object._wrap(super(Insets, self).clone())

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
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void java.awt.Insets.set(int,int,int,int)"""
        super(_Insets, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def grow(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.Insets.grow(int)"""
        super(_Insets, self).grow(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def shrink(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.Insets.shrink(int)"""
        super(_Insets, self).shrink(_int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.awt.Insets.hashCode()"""
        return int._wrap(super(Insets, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.MessengerImpl
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import dev.ultreon.libs.commons.v0.MessengerImpl as _MessengerImpl
_MessengerImpl = _MessengerImpl
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MessengerImpl():
    """dev.ultreon.libs.commons.v0.MessengerImpl"""
 
    @staticmethod
    def _wrap(java_value: _MessengerImpl) -> 'MessengerImpl':
        return MessengerImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessengerImpl):
        """
        Dynamic initializer for MessengerImpl.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessengerImpl__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessengerImpl__wrapper":
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
    def __init__(self, arg0: 'Consumer'):
        """public dev.ultreon.libs.commons.v0.MessengerImpl(java.util.function.Consumer<java.lang.String>)"""
        val = _MessengerImpl(arg0)
        self.__wrapper = val

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
    def send(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.MessengerImpl.send(java.lang.String)"""
        super(_MessengerImpl, self).send(arg0)

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.Version
import dev.ultreon.libs.commons.v0.Version as _Version
_Version = _Version
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.commons.v0.VersionType as _VersionType
_VersionType = _VersionType
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Version():
    """dev.ultreon.libs.commons.v0.Version"""
 
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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def build(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Version.build()"""
        return int._wrap(super(Version, self).build())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def minor(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Version.minor()"""
        return int._wrap(super(Version, self).minor())

    @overload
    def type(self) -> 'VersionType':
        """public dev.ultreon.libs.commons.v0.VersionType dev.ultreon.libs.commons.v0.Version.type()"""
        return 'VersionType'._wrap(super(Version, self).type())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Version.hashCode()"""
        return int._wrap(super(Version, self).hashCode())

    @overload
    def major(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Version.major()"""
        return int._wrap(super(Version, self).major())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Version.toString()"""
        return str._wrap(super(Version, self).toString())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Version.equals(java.lang.Object)"""
        return bool._wrap(super(_Version, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: 'VersionType', arg4: int):
        """public dev.ultreon.libs.commons.v0.Version(int,int,int,dev.ultreon.libs.commons.v0.VersionType,int)"""
        val = _Version(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3, _int.valueOf(arg4))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def release(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Version.release()"""
        return int._wrap(super(Version, self).release()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Identifier
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pycorelibs.commons.v0 import tuple
except ImportError:
    tuple = _import_once("pycorelibs.commons.v0.tuple")

import java.util.Collection as Collection
import java.lang.String as _string
import java.util.ArrayList as ArrayList
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.libs.commons.v0.tuple.Pair as _Pair
_Pair = _Pair
import java.util.List as _List
_List = _List
import java.util.function.BiFunction as BiFunction
from typing import List
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import dev.ultreon.libs.commons.v0.Identifier as _Identifier
_Identifier = _Identifier
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.Function as Function
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Identifier():
    """dev.ultreon.libs.commons.v0.Identifier"""
 
    @staticmethod
    def _wrap(java_value: _Identifier) -> 'Identifier':
        return Identifier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Identifier):
        """
        Dynamic initializer for Identifier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Identifier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Identifier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getDefaultNamespace() -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.Identifier.getDefaultNamespace()"""
        return str._wrap(_Identifier.getDefaultNamespace())

    @overload
    def mapLocation(self, arg0: 'Function') -> 'Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.mapLocation(java.util.function.Function<java.lang.String, java.lang.String>)"""
        return 'Identifier'._wrap(super(_Identifier, self).mapLocation(arg0))

    @overload
    def reduce(self, arg0: 'BiFunction') -> object:
        """public <T> T dev.ultreon.libs.commons.v0.Identifier.reduce(java.util.function.BiFunction<java.lang.String, java.lang.String, T>)"""
        return object._wrap(super(_Identifier, self).reduce(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toCollection(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.libs.commons.v0.Identifier.toCollection()"""
        return 'Collection'._wrap(super(Identifier, self).toCollection())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.libs.commons.v0.Identifier(java.lang.String)"""
        val = _Identifier(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def tryParse(arg0: str) -> 'Identifier':
        """public static dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.tryParse(java.lang.String)"""
        return Identifier._wrap(_Identifier.tryParse(arg0))

    @overload
    def withLocation(self, arg0: str) -> 'Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.withLocation(java.lang.String)"""
        return 'Identifier'._wrap(super(_Identifier, self).withLocation(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Identifier.equals(java.lang.Object)"""
        return bool._wrap(super(_Identifier, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toArray(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.libs.commons.v0.Identifier.toArray()"""
        return List[str]._wrap(super(Identifier, self).toArray())

    @overload
    def toList(self) -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.libs.commons.v0.Identifier.toList()"""
        return 'List'._wrap(super(Identifier, self).toList())

    @overload
    def mapPath(self, arg0: 'Function') -> 'Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.mapPath(java.util.function.Function<java.lang.String, java.lang.String>)"""
        return 'Identifier'._wrap(super(_Identifier, self).mapPath(arg0))

    @overload
    def withPath(self, arg0: str) -> 'Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.withPath(java.lang.String)"""
        return 'Identifier'._wrap(super(_Identifier, self).withPath(arg0))

    @staticmethod
    @overload
    def testLocation(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.Identifier.testLocation(java.lang.String)"""
        return str._wrap(_Identifier.testLocation(arg0))

    @staticmethod
    @overload
    def testPath(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.Identifier.testPath(java.lang.String)"""
        return str._wrap(_Identifier.testPath(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Identifier.toString()"""
        return str._wrap(super(Identifier, self).toString())

    @overload
    def toArrayList(self) -> 'ArrayList':
        """public java.util.ArrayList<java.lang.String> dev.ultreon.libs.commons.v0.Identifier.toArrayList()"""
        return 'ArrayList'._wrap(super(Identifier, self).toArrayList())

    @overload
    def toPair(self) -> 'tuple.Pair':
        """public dev.ultreon.libs.commons.v0.tuple.Pair<java.lang.String, java.lang.String> dev.ultreon.libs.commons.v0.Identifier.toPair()"""
        return 'tuple.Pair'._wrap(super(Identifier, self).toPair())

    @overload
    def location(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Identifier.location()"""
        return str._wrap(super(Identifier, self).location())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def map(self, arg0: 'Function', arg1: 'Function') -> 'Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.map(java.util.function.Function<java.lang.String, java.lang.String>,java.util.function.Function<java.lang.String, java.lang.String>)"""
        return 'Identifier'._wrap(super(_Identifier, self).map(arg0, arg1))

    @overload
    def path(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Identifier.path()"""
        return str._wrap(super(Identifier, self).path())

    @staticmethod
    @overload
    def setDefaultNamespace(arg0: str):
        """public static synchronized void dev.ultreon.libs.commons.v0.Identifier.setDefaultNamespace(java.lang.String)"""
        _Identifier.setDefaultNamespace(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Identifier.hashCode()"""
        return int._wrap(super(Identifier, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def parse(arg0: str) -> 'Identifier':
        """public static dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.parse(java.lang.String)"""
        return Identifier._wrap(_Identifier.parse(arg0))

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.libs.commons.v0.Identifier(java.lang.String,java.lang.String)"""
        val = _Identifier(arg0, arg1)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Progress
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.Progress as _Progress
_Progress = _Progress
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Progress():
    """dev.ultreon.libs.commons.v0.Progress"""
 
    @staticmethod
    def _wrap(java_value: _Progress) -> 'Progress':
        return Progress(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Progress):
        """
        Dynamic initializer for Progress.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Progress__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Progress__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def compareTo(self, arg0: 'Progress') -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.compareTo(dev.ultreon.libs.commons.v0.Progress)"""
        return int._wrap(super(_Progress, self).compareTo(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.commons.v0.Progress(int,int)"""
        val = _Progress(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getProgress(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.getProgress()"""
        return int._wrap(super(Progress, self).getProgress())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getPercentage(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Progress.getPercentage()"""
        return float._wrap(super(Progress, self).getPercentage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.hashCode()"""
        return int._wrap(super(Progress, self).hashCode())

    @overload
    def increment(self):
        """public void dev.ultreon.libs.commons.v0.Progress.increment()"""
        super(Progress, self).increment()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Progress.equals(java.lang.Object)"""
        return bool._wrap(super(_Progress, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getMax(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.getMax()"""
        return int._wrap(super(Progress, self).getMax())

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
    def getRelativeProgress(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Progress.getRelativeProgress()"""
        return float._wrap(super(Progress, self).getRelativeProgress())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.libs.commons.v0.Progress(int)"""
        val = _Progress(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Progress.toString()"""
        return str._wrap(super(Progress, self).toString()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Logger
import java.lang.String as _string
import dev.ultreon.libs.commons.v0.Logger as _Logger
_Logger = _Logger
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class Logger():
    """dev.ultreon.libs.commons.v0.Logger"""
 
    @staticmethod
    def _wrap(java_value: _Logger) -> 'Logger':
        return Logger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Logger):
        """
        Dynamic initializer for Logger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Logger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Logger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def info(self, arg0: str):
        """public default void dev.ultreon.libs.commons.v0.Logger.info(java.lang.String)"""
        super(_Logger, self).info(arg0)

    @overload
    def warn(self, arg0: str):
        """public default void dev.ultreon.libs.commons.v0.Logger.warn(java.lang.String)"""
        super(_Logger, self).warn(arg0)

    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public default void dev.ultreon.libs.commons.v0.Logger.error(java.lang.String,java.lang.Throwable)"""
        super(_Logger, self).error(arg0, arg1)

    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public default void dev.ultreon.libs.commons.v0.Logger.warn(java.lang.String,java.lang.Throwable)"""
        super(_Logger, self).warn(arg0, arg1)

    @overload
    def debug(self, arg0: str):
        """public default void dev.ultreon.libs.commons.v0.Logger.debug(java.lang.String)"""
        super(_Logger, self).debug(arg0)

    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public default void dev.ultreon.libs.commons.v0.Logger.info(java.lang.String,java.lang.Throwable)"""
        super(_Logger, self).info(arg0, arg1)

    @overload
    def log(self, arg0: str, arg1: 'Throwable'):
        """public default void dev.ultreon.libs.commons.v0.Logger.log(java.lang.String,java.lang.Throwable)"""
        super(_Logger, self).log(arg0, arg1)

    @overload
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public default void dev.ultreon.libs.commons.v0.Logger.debug(java.lang.String,java.lang.Throwable)"""
        super(_Logger, self).debug(arg0, arg1)

    @abstractmethod
    def log(self, arg0: 'Level', arg1: str, arg2: 'Throwable'):
        """public abstract void dev.ultreon.libs.commons.v0.Logger.log(dev.ultreon.libs.commons.v0.Logger$Level,java.lang.String,java.lang.Throwable)"""
        pass

    @overload
    def error(self, arg0: str):
        """public default void dev.ultreon.libs.commons.v0.Logger.error(java.lang.String)"""
        super(_Logger, self).error(arg0)

    @overload
    def log(self, arg0: str):
        """public default void dev.ultreon.libs.commons.v0.Logger.log(java.lang.String)"""
        super(_Logger, self).log(arg0) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Result
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.libs.commons.v0.Result as _Result
_Result = _Result
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Result():
    """dev.ultreon.libs.commons.v0.Result"""
 
    @staticmethod
    def _wrap(java_value: _Result) -> 'Result':
        return Result(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Result):
        """
        Dynamic initializer for Result.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Result__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Result__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isValuePresent(self) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Result.isValuePresent()"""
        return bool._wrap(super(Result, self).isValuePresent())

    @overload
    def getFailureOrNullOr(self, arg0: 'Supplier') -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.commons.v0.Result.getFailureOrNullOr(java.util.function.Supplier<? extends java.lang.Throwable>)"""
        return 'Throwable'._wrap(super(_Result, self).getFailureOrNullOr(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getValueOrNullOr(self, arg0: object) -> object:
        """public T dev.ultreon.libs.commons.v0.Result.getValueOrNullOr(T)"""
        return object._wrap(super(_Result, self).getValueOrNullOr(arg0))

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
    def ifFailureOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.libs.commons.v0.Result.ifFailureOrElse(java.util.function.Consumer<java.lang.Throwable>,java.lang.Runnable)"""
        super(_Result, self).ifFailureOrElse(arg0, arg1)

    @staticmethod
    @overload
    def left(arg0: object) -> 'Result':
        """public static <T> dev.ultreon.libs.commons.v0.Result<T> dev.ultreon.libs.commons.v0.Result.left(T)"""
        return Result._wrap(_Result.left(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def ifFailure(self, arg0: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Result.ifFailure(java.util.function.Consumer<java.lang.Throwable>)"""
        super(_Result, self).ifFailure(arg0)

    @overload
    def ifAny(self, arg0: 'Consumer', arg1: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Result.ifAny(java.util.function.Consumer<T>,java.util.function.Consumer<java.lang.Throwable>)"""
        super(_Result, self).ifAny(arg0, arg1)

    @overload
    def getFailure(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.commons.v0.Result.getFailure()"""
        return 'Throwable'._wrap(super(Result, self).getFailure())

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.libs.commons.v0.Result.getValue()"""
        return object._wrap(super(Result, self).getValue())

    @overload
    def getValueOrNull(self) -> object:
        """public T dev.ultreon.libs.commons.v0.Result.getValueOrNull()"""
        return object._wrap(super(Result, self).getValueOrNull())

    @overload
    def getFailureOrNullOr(self, arg0: 'Throwable') -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.commons.v0.Result.getFailureOrNullOr(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Result, self).getFailureOrNullOr(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def ifValueOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.libs.commons.v0.Result.ifValueOrElse(java.util.function.Consumer<T>,java.lang.Runnable)"""
        super(_Result, self).ifValueOrElse(arg0, arg1)

    @overload
    def isFailurePresent(self) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Result.isFailurePresent()"""
        return bool._wrap(super(Result, self).isFailurePresent())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getValueOrNullOrGet(self, arg0: 'Supplier') -> object:
        """public T dev.ultreon.libs.commons.v0.Result.getValueOrNullOrGet(java.util.function.Supplier<? extends T>)"""
        return object._wrap(super(_Result, self).getValueOrNullOrGet(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def ifValue(self, arg0: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Result.ifValue(java.util.function.Consumer<T>)"""
        super(_Result, self).ifValue(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def right(arg0: 'Throwable') -> 'Result':
        """public static <T> dev.ultreon.libs.commons.v0.Result<T> dev.ultreon.libs.commons.v0.Result.right(java.lang.Throwable)"""
        return Result._wrap(_Result.right(arg0))

    @overload
    def getFailureOrNull(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.commons.v0.Result.getFailureOrNull()"""
        return 'Throwable'._wrap(super(Result, self).getFailureOrNull())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.ProgressMessenger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.commons.v0.ProgressMessenger as _ProgressMessenger
_ProgressMessenger = _ProgressMessenger
from builtins import float
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.Progress as _Progress
_Progress = _Progress
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ProgressMessenger():
    """dev.ultreon.libs.commons.v0.ProgressMessenger"""
 
    @staticmethod
    def _wrap(java_value: _ProgressMessenger) -> 'ProgressMessenger':
        return ProgressMessenger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ProgressMessenger):
        """
        Dynamic initializer for ProgressMessenger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ProgressMessenger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ProgressMessenger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def compareTo(self, arg0: 'Progress') -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.compareTo(dev.ultreon.libs.commons.v0.Progress)"""
        return int._wrap(super(_Progress, self).compareTo(arg0))

    @override
    @overload
    def getProgress(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.getProgress()"""
        return int._wrap(super(Progress, self).getProgress())

    @override
    @overload
    def increment(self):
        """public void dev.ultreon.libs.commons.v0.Progress.increment()"""
        super(Progress, self).increment()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Messenger', arg1: int):
        """public dev.ultreon.libs.commons.v0.ProgressMessenger(dev.ultreon.libs.commons.v0.Messenger,int)"""
        val = _ProgressMessenger(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRelativeProgress(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Progress.getRelativeProgress()"""
        return float._wrap(super(Progress, self).getRelativeProgress())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.hashCode()"""
        return int._wrap(super(Progress, self).hashCode())

    @override
    @overload
    def getMax(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.getMax()"""
        return int._wrap(super(Progress, self).getMax())

    @overload
    def send(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.ProgressMessenger.send(java.lang.String)"""
        super(_ProgressMessenger, self).send(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Progress.equals(java.lang.Object)"""
        return bool._wrap(super(_Progress, self).equals(arg0))

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
    def __init__(self, arg0: 'Messenger', arg1: int, arg2: int):
        """public dev.ultreon.libs.commons.v0.ProgressMessenger(dev.ultreon.libs.commons.v0.Messenger,int,int)"""
        val = _ProgressMessenger(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def sendNext(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.ProgressMessenger.sendNext(java.lang.String)"""
        super(_ProgressMessenger, self).sendNext(arg0)

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Progress.toString()"""
        return str._wrap(super(Progress, self).toString())

    @override
    @overload
    def getPercentage(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Progress.getPercentage()"""
        return float._wrap(super(Progress, self).getPercentage())