from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.libs.commons.v0.Progress as __Progress
__Progress = __Progress
from builtins import int
 
class Progress(__Cloneable, Cloneable, __Comparable, Comparable, __Serializable, Serializable):
    """dev.ultreon.libs.commons.v0.Progress"""
 
    @staticmethod
    def __wrap(java_value: __Progress) -> 'Progress':
        return Progress(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Progress):
        """
        Dynamic initializer for Progress.
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
    def getMax(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.getMax()"""
        return int.__wrap(super(Progress, self).getMax())

    @overload
    def compareTo(self, arg0: 'Progress') -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.compareTo(dev.ultreon.libs.commons.v0.Progress)"""
        return int.__wrap(super(__Progress, self).compareTo(arg0))

    @overload
    def getRelativeProgress(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Progress.getRelativeProgress()"""
        return float.__wrap(super(Progress, self).getRelativeProgress())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.libs.commons.v0.Progress(int)"""
        val = __Progress(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Progress.equals(java.lang.Object)"""
        return bool.__wrap(super(__Progress, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getProgress(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.getProgress()"""
        return int.__wrap(super(Progress, self).getProgress())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def increment(self):
        """public void dev.ultreon.libs.commons.v0.Progress.increment()"""
        super(Progress, self).increment()

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Progress.toString()"""
        return str.__wrap(super(Progress, self).toString())

    @overload
    def getPercentage(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Progress.getPercentage()"""
        return float.__wrap(super(Progress, self).getPercentage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.hashCode()"""
        return int.__wrap(super(Progress, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.commons.v0.Progress(int,int)"""
        val = __Progress(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Progress
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.libs.commons.v0.Progress as __Progress
__Progress = __Progress
from builtins import int
 
class Progress(__Cloneable, Cloneable, __Comparable, Comparable, __Serializable, Serializable):
    """dev.ultreon.libs.commons.v0.Progress"""
 
    @staticmethod
    def __wrap(java_value: __Progress) -> 'Progress':
        return Progress(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Progress):
        """
        Dynamic initializer for Progress.
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
    def getMax(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.getMax()"""
        return int.__wrap(super(Progress, self).getMax())

    @overload
    def compareTo(self, arg0: 'Progress') -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.compareTo(dev.ultreon.libs.commons.v0.Progress)"""
        return int.__wrap(super(__Progress, self).compareTo(arg0))

    @overload
    def getRelativeProgress(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Progress.getRelativeProgress()"""
        return float.__wrap(super(Progress, self).getRelativeProgress())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.libs.commons.v0.Progress(int)"""
        val = __Progress(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Progress.equals(java.lang.Object)"""
        return bool.__wrap(super(__Progress, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getProgress(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.getProgress()"""
        return int.__wrap(super(Progress, self).getProgress())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def increment(self):
        """public void dev.ultreon.libs.commons.v0.Progress.increment()"""
        super(Progress, self).increment()

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Progress.toString()"""
        return str.__wrap(super(Progress, self).toString())

    @overload
    def getPercentage(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Progress.getPercentage()"""
        return float.__wrap(super(Progress, self).getPercentage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.hashCode()"""
        return int.__wrap(super(Progress, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.commons.v0.Progress(int,int)"""
        val = __Progress(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Progress 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Mth
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.math.BigInteger as BigInteger
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.commons.v0.Color as __Color
__Color = __Color
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.math.BigDecimal as BigDecimal
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.libs.commons.v0.Mth as __Mth
__Mth = __Mth
from builtins import int
 
class Mth():
    """dev.ultreon.libs.commons.v0.Mth"""
 
    @staticmethod
    def __wrap(java_value: __Mth) -> 'Mth':
        return Mth(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Mth):
        """
        Dynamic initializer for Mth.
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
    def clamp(clamp) -> 'BigInteger':
        """public static java.math.BigInteger dev.ultreon.libs.commons.v0.Mth.clamp(java.math.BigInteger,java.math.BigInteger,java.math.BigInteger)"""
        return __transform(__arg0, arg1, arg2.Mth(arg0: 'BigInteger', arg1: 'BigInteger', arg2: 'BigInteger')).'BigInteger'Value()

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static long dev.ultreon.libs.commons.v0.Mth.diff(long,long)"""
        return int.__wrap(__Mth.diff(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static int dev.ultreon.libs.commons.v0.Mth.diff(int,int)"""
        return int.__wrap(__Mth.diff(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def diff(arg0: float, arg1: float) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.diff(double,double)"""
        return float.__wrap(__Mth.diff(__double.valueOf(arg0), __double.valueOf(arg1)))

    @staticmethod
    @overload
    def clamp(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.clamp(double,double,double)"""
        return float.__wrap(__Mth.clamp(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def clamp(clamp) -> 'BigDecimal':
        """public static java.math.BigDecimal dev.ultreon.libs.commons.v0.Mth.clamp(java.math.BigDecimal,java.math.BigDecimal,java.math.BigDecimal)"""
        return __transform(__arg0, arg1, arg2.Mth(arg0: 'BigDecimal', arg1: 'BigDecimal', arg2: 'BigDecimal')).'BigDecimal'Value()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def lerp(arg0: float, arg1: float, arg2: float) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.lerp(double,double,double)"""
        return float.__wrap(__Mth.lerp(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def round(arg0: float, arg1: int) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.round(double,int)"""
        return float.__wrap(__Mth.round(__double.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def mixColors(arg0: 'Color', arg1: 'Color', arg2: float) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Mth.mixColors(dev.ultreon.libs.commons.v0.Color,dev.ultreon.libs.commons.v0.Color,double)"""
        return Color.__wrap(__Mth.mixColors(arg0, arg1, __double.valueOf(arg2)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.Mth()"""
        val = __Mth()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.Mth()"""
        val = __Mth()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static byte dev.ultreon.libs.commons.v0.Mth.clamp(byte,int,int)"""
        return int.__wrap(__Mth.clamp(__byte.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def diff(arg0: float, arg1: float) -> float:
        """public static float dev.ultreon.libs.commons.v0.Mth.diff(float,float)"""
        return float.__wrap(__Mth.diff(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static short dev.ultreon.libs.commons.v0.Mth.clamp(short,int,int)"""
        return int.__wrap(__Mth.clamp(__short.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static int dev.ultreon.libs.commons.v0.Mth.clamp(int,int,int)"""
        return int.__wrap(__Mth.clamp(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

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
    def clamp(arg0: float, arg1: float, arg2: float) -> float:
        """public static float dev.ultreon.libs.commons.v0.Mth.clamp(float,float,float)"""
        return float.__wrap(__Mth.clamp(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def clamp(arg0: int, arg1: int, arg2: int) -> int:
        """public static long dev.ultreon.libs.commons.v0.Mth.clamp(long,long,long)"""
        return int.__wrap(__Mth.clamp(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static byte dev.ultreon.libs.commons.v0.Mth.diff(byte,byte)"""
        return int.__wrap(__Mth.diff(__byte.valueOf(arg0), __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def diff(arg0: int, arg1: int) -> int:
        """public static short dev.ultreon.libs.commons.v0.Mth.diff(short,short)"""
        return int.__wrap(__Mth.diff(__short.valueOf(arg0), __short.valueOf(arg1)))

    @staticmethod
    @overload
    def root(arg0: int, arg1: int) -> float:
        """public static double dev.ultreon.libs.commons.v0.Mth.root(int,int)"""
        return float.__wrap(__Mth.root(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Result
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.lang.Runnable as Runnable
from builtins import object
import java.util.function.Consumer as Consumer
import dev.ultreon.libs.commons.v0.Result as __Result
__Result = __Result
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Result():
    """dev.ultreon.libs.commons.v0.Result"""
 
    @staticmethod
    def __wrap(java_value: __Result) -> 'Result':
        return Result(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Result):
        """
        Dynamic initializer for Result.
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
    def getValueOrNullOr(self, arg0: object) -> object:
        """public T dev.ultreon.libs.commons.v0.Result.getValueOrNullOr(T)"""
        return object.__wrap(super(__Result, self).getValueOrNullOr(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getFailureOrNullOr(self, arg0: 'Supplier') -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.commons.v0.Result.getFailureOrNullOr(java.util.function.Supplier<? extends java.lang.Throwable>)"""
        return 'Throwable'.__wrap(super(__Result, self).getFailureOrNullOr(arg0))

    @overload
    def getFailure(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.commons.v0.Result.getFailure()"""
        return 'Throwable'.__wrap(super(Result, self).getFailure())

    @overload
    def ifValueOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.libs.commons.v0.Result.ifValueOrElse(java.util.function.Consumer<T>,java.lang.Runnable)"""
        super(__Result, self).ifValueOrElse(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isValuePresent(self) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Result.isValuePresent()"""
        return bool.__wrap(super(Result, self).isValuePresent())

    @overload
    def getValueOrNullOrGet(self, arg0: 'Supplier') -> object:
        """public T dev.ultreon.libs.commons.v0.Result.getValueOrNullOrGet(java.util.function.Supplier<? extends T>)"""
        return object.__wrap(super(__Result, self).getValueOrNullOrGet(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def ifFailure(self, arg0: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Result.ifFailure(java.util.function.Consumer<java.lang.Throwable>)"""
        super(__Result, self).ifFailure(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def ifFailureOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.libs.commons.v0.Result.ifFailureOrElse(java.util.function.Consumer<java.lang.Throwable>,java.lang.Runnable)"""
        super(__Result, self).ifFailureOrElse(arg0, arg1)

    @overload
    def getFailureOrNullOr(self, arg0: 'Throwable') -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.commons.v0.Result.getFailureOrNullOr(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Result, self).getFailureOrNullOr(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def left(arg0: object) -> 'Result':
        """public static <T> dev.ultreon.libs.commons.v0.Result<T> dev.ultreon.libs.commons.v0.Result.left(T)"""
        return Result.__wrap(__Result.left(arg0))

    @overload
    def ifValue(self, arg0: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Result.ifValue(java.util.function.Consumer<T>)"""
        super(__Result, self).ifValue(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isFailurePresent(self) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Result.isFailurePresent()"""
        return bool.__wrap(super(Result, self).isFailurePresent())

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
    def ifAny(self, arg0: 'Consumer', arg1: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Result.ifAny(java.util.function.Consumer<T>,java.util.function.Consumer<java.lang.Throwable>)"""
        super(__Result, self).ifAny(arg0, arg1)

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.libs.commons.v0.Result.getValue()"""
        return object.__wrap(super(Result, self).getValue())

    @overload
    def getValueOrNull(self) -> object:
        """public T dev.ultreon.libs.commons.v0.Result.getValueOrNull()"""
        return object.__wrap(super(Result, self).getValueOrNull())

    @overload
    def getFailureOrNull(self) -> 'Throwable':
        """public java.lang.Throwable dev.ultreon.libs.commons.v0.Result.getFailureOrNull()"""
        return 'Throwable'.__wrap(super(Result, self).getFailureOrNull())

    @staticmethod
    @overload
    def right(arg0: 'Throwable') -> 'Result':
        """public static <T> dev.ultreon.libs.commons.v0.Result<T> dev.ultreon.libs.commons.v0.Result.right(java.lang.Throwable)"""
        return Result.__wrap(__Result.right(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Percentage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.Percentage as __Percentage
__Percentage = __Percentage
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Percentage(__Serializable, Serializable, __Comparable, Comparable):
    """dev.ultreon.libs.commons.v0.Percentage"""
 
    @staticmethod
    def __wrap(java_value: __Percentage) -> 'Percentage':
        return Percentage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Percentage):
        """
        Dynamic initializer for Percentage.
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
    def value(self) -> float:
        """public double dev.ultreon.libs.commons.v0.Percentage.value()"""
        return float.__wrap(super(Percentage, self).value())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Percentage.equals(java.lang.Object)"""
        return bool.__wrap(super(__Percentage, self).equals(arg0))

    @overload
    def percentage(self) -> float:
        """public double dev.ultreon.libs.commons.v0.Percentage.percentage()"""
        return float.__wrap(super(Percentage, self).percentage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def toPercentage(arg0: float) -> 'Percentage':
        """public static dev.ultreon.libs.commons.v0.Percentage dev.ultreon.libs.commons.v0.Percentage.toPercentage(double)"""
        return Percentage.__wrap(__Percentage.toPercentage(__double.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Percentage.toString()"""
        return str.__wrap(super(Percentage, self).toString())

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

    @overload
    def compareTo(self, arg0: 'Percentage') -> int:
        """public int dev.ultreon.libs.commons.v0.Percentage.compareTo(dev.ultreon.libs.commons.v0.Percentage)"""
        return int.__wrap(super(__Percentage, self).compareTo(arg0))

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.libs.commons.v0.Percentage(double)"""
        val = __Percentage(__double.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Pixel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.awt.Point as Point
import java.awt.Point as __Point
__Point = __Point
import java.lang.Long as __long
import dev.ultreon.libs.commons.v0.Pixel as __Pixel
__Pixel = __Pixel
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.commons.v0.Color as __Color
__Color = __Color
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Pixel(__Serializable, Serializable):
    """dev.ultreon.libs.commons.v0.Pixel"""
 
    @staticmethod
    def __wrap(java_value: __Pixel) -> 'Pixel':
        return Pixel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pixel):
        """
        Dynamic initializer for Pixel.
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
    def getPos(self) -> 'Point':
        """public java.awt.Point dev.ultreon.libs.commons.v0.Pixel.getPos()"""
        return 'Point'.__wrap(super(Pixel, self).getPos())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'Color'):
        """public dev.ultreon.libs.commons.v0.Pixel(int,int,dev.ultreon.libs.commons.v0.Color)"""
        val = __Pixel(__int.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Pixel.getY()"""
        return int.__wrap(super(Pixel, self).getY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getColor(self) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Pixel.getColor()"""
        return 'Color'.__wrap(super(Pixel, self).getColor())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Pixel.getX()"""
        return int.__wrap(super(Pixel, self).getX())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Point', arg1: 'Color'):
        """public dev.ultreon.libs.commons.v0.Pixel(java.awt.Point,dev.ultreon.libs.commons.v0.Color)"""
        val = __Pixel(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.MessengerImpl
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.libs.commons.v0.MessengerImpl as __MessengerImpl
__MessengerImpl = __MessengerImpl
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MessengerImpl(__Messenger, Messenger):
    """dev.ultreon.libs.commons.v0.MessengerImpl"""
 
    @staticmethod
    def __wrap(java_value: __MessengerImpl) -> 'MessengerImpl':
        return MessengerImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessengerImpl):
        """
        Dynamic initializer for MessengerImpl.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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

    @overload
    def __init__(self, arg0: 'Consumer'):
        """public dev.ultreon.libs.commons.v0.MessengerImpl(java.util.function.Consumer<java.lang.String>)"""
        val = __MessengerImpl(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.MessengerImpl.send(java.lang.String)"""
        super(__MessengerImpl, self).send(arg0)

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.ProgressMessenger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.libs.commons.v0.ProgressMessenger as __ProgressMessenger
__ProgressMessenger = __ProgressMessenger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.libs.commons.v0.Progress as __Progress
__Progress = __Progress
from builtins import int
 
class ProgressMessenger(__Progress, Progress):
    """dev.ultreon.libs.commons.v0.ProgressMessenger"""
 
    @staticmethod
    def __wrap(java_value: __ProgressMessenger) -> 'ProgressMessenger':
        return ProgressMessenger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ProgressMessenger):
        """
        Dynamic initializer for ProgressMessenger.
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
    def getMax(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.getMax()"""
        return int.__wrap(super(Progress, self).getMax())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def compareTo(self, arg0: 'Progress') -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.compareTo(dev.ultreon.libs.commons.v0.Progress)"""
        return int.__wrap(super(__Progress, self).compareTo(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Progress.equals(java.lang.Object)"""
        return bool.__wrap(super(__Progress, self).equals(arg0))

    @override
    @overload
    def increment(self):
        """public void dev.ultreon.libs.commons.v0.Progress.increment()"""
        super(Progress, self).increment()

    @override
    @overload
    def getPercentage(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Progress.getPercentage()"""
        return float.__wrap(super(Progress, self).getPercentage())

    @override
    @overload
    def getProgress(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.getProgress()"""
        return int.__wrap(super(Progress, self).getProgress())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRelativeProgress(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Progress.getRelativeProgress()"""
        return float.__wrap(super(Progress, self).getRelativeProgress())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Progress.toString()"""
        return str.__wrap(super(Progress, self).toString())

    @overload
    def __init__(self, arg0: 'Messenger', arg1: int, arg2: int):
        """public dev.ultreon.libs.commons.v0.ProgressMessenger(dev.ultreon.libs.commons.v0.Messenger,int,int)"""
        val = __ProgressMessenger(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def sendNext(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.ProgressMessenger.sendNext(java.lang.String)"""
        super(__ProgressMessenger, self).sendNext(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Progress.hashCode()"""
        return int.__wrap(super(Progress, self).hashCode())

    @overload
    def send(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.ProgressMessenger.send(java.lang.String)"""
        super(__ProgressMessenger, self).send(arg0)

    @overload
    def __init__(self, arg0: 'Messenger', arg1: int):
        """public dev.ultreon.libs.commons.v0.ProgressMessenger(dev.ultreon.libs.commons.v0.Messenger,int)"""
        val = __ProgressMessenger(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.libs.commons.v0.UtilityClass
from builtins import str
import dev.ultreon.libs.commons.v0.UtilityClass as __UtilityClass
__UtilityClass = __UtilityClass
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
from builtins import bool
from builtins import int
 
class UtilityClass():
    """dev.ultreon.libs.commons.v0.UtilityClass"""
 
    @staticmethod
    def __wrap(java_value: __UtilityClass) -> 'UtilityClass':
        return UtilityClass(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UtilityClass):
        """
        Dynamic initializer for UtilityClass.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.Logger$Level
from builtins import str
import dev.ultreon.libs.commons.v0.Logger as __Logger_Level
__Level = __Logger_Level.Level
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
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
 
class Level(__Enum, Enum):
    """dev.ultreon.libs.commons.v0.Logger.Level"""
 
    @staticmethod
    def __wrap(java_value: __Level) -> 'Level':
        return Level(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Level):
        """
        Dynamic initializer for Level.
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
    def valueOf(arg0: str) -> 'Level':
        """public static dev.ultreon.libs.commons.v0.Logger$Level dev.ultreon.libs.commons.v0.Logger$Level.valueOf(java.lang.String)"""
        return Level.__wrap(__Level.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['Level']:
        """public static dev.ultreon.libs.commons.v0.Logger$Level[] dev.ultreon.libs.commons.v0.Logger$Level.values()"""
        return List[Level].__wrap(__Level.values())

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.VersionType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.libs.commons.v0.VersionType as __VersionType
__VersionType = __VersionType
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class VersionType(__Enum, Enum):
    """dev.ultreon.libs.commons.v0.VersionType"""
 
    @staticmethod
    def __wrap(java_value: __VersionType) -> 'VersionType':
        return VersionType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VersionType):
        """
        Dynamic initializer for VersionType.
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
    def valueOf(arg0: str) -> 'VersionType':
        """public static dev.ultreon.libs.commons.v0.VersionType dev.ultreon.libs.commons.v0.VersionType.valueOf(java.lang.String)"""
        return VersionType.__wrap(__VersionType.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['VersionType']:
        """public static dev.ultreon.libs.commons.v0.VersionType[] dev.ultreon.libs.commons.v0.VersionType.values()"""
        return List[VersionType].__wrap(__VersionType.values())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.VersionType.getName()"""
        return str.__wrap(super(VersionType, self).getName())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.VersionType.toString()"""
        return str.__wrap(super(VersionType, self).toString())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def toRepresentation(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.VersionType.toRepresentation()"""
        return str.__wrap(super(VersionType, self).toRepresentation()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Identifier
from pyquantum_helper import import_once as __import_once__
from builtins import type
try:
    from pycorelibs.commons.v0 import tuple
except ImportError:
    tuple = __import_once__("pycorelibs.commons.v0.tuple")

import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
import dev.ultreon.libs.commons.v0.Identifier as __Identifier
__Identifier = __Identifier
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import object
import java.util.function.BiFunction as BiFunction
from typing import List
import java.util.List as __List
__List = __List
import dev.ultreon.libs.commons.v0.tuple.Pair as __Pair
__Pair = __Pair
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import int
import java.util.List as List
 
class Identifier():
    """dev.ultreon.libs.commons.v0.Identifier"""
 
    @staticmethod
    def __wrap(java_value: __Identifier) -> 'Identifier':
        return Identifier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Identifier):
        """
        Dynamic initializer for Identifier.
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

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Identifier.hashCode()"""
        return int.__wrap(super(Identifier, self).hashCode())

    @staticmethod
    @overload
    def testLocation(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.Identifier.testLocation(java.lang.String)"""
        return str.__wrap(__Identifier.testLocation(arg0))

    @overload
    def withLocation(self, arg0: str) -> 'Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.withLocation(java.lang.String)"""
        return 'Identifier'.__wrap(super(__Identifier, self).withLocation(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toCollection(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.libs.commons.v0.Identifier.toCollection()"""
        return 'Collection'.__wrap(super(Identifier, self).toCollection())

    @overload
    def mapPath(self, arg0: 'Function') -> 'Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.mapPath(java.util.function.Function<java.lang.String, java.lang.String>)"""
        return 'Identifier'.__wrap(super(__Identifier, self).mapPath(arg0))

    @staticmethod
    @overload
    def testPath(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.Identifier.testPath(java.lang.String)"""
        return str.__wrap(__Identifier.testPath(arg0))

    @overload
    def path(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Identifier.path()"""
        return str.__wrap(super(Identifier, self).path())

    @overload
    def mapLocation(self, arg0: 'Function') -> 'Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.mapLocation(java.util.function.Function<java.lang.String, java.lang.String>)"""
        return 'Identifier'.__wrap(super(__Identifier, self).mapLocation(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Identifier.equals(java.lang.Object)"""
        return bool.__wrap(super(__Identifier, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toList(self) -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.libs.commons.v0.Identifier.toList()"""
        return 'List'.__wrap(super(Identifier, self).toList())

    @overload
    def toArrayList(self) -> 'ArrayList':
        """public java.util.ArrayList<java.lang.String> dev.ultreon.libs.commons.v0.Identifier.toArrayList()"""
        return 'ArrayList'.__wrap(super(Identifier, self).toArrayList())

    @staticmethod
    @overload
    def tryParse(arg0: str) -> 'Identifier':
        """public static dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.tryParse(java.lang.String)"""
        return Identifier.__wrap(__Identifier.tryParse(arg0))

    @staticmethod
    @overload
    def getDefaultNamespace() -> str:
        """public static java.lang.String dev.ultreon.libs.commons.v0.Identifier.getDefaultNamespace()"""
        return str.__wrap(__Identifier.getDefaultNamespace())

    @staticmethod
    @overload
    def parse(arg0: str) -> 'Identifier':
        """public static dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.parse(java.lang.String)"""
        return Identifier.__wrap(__Identifier.parse(arg0))

    @overload
    def reduce(self, arg0: 'BiFunction') -> object:
        """public <T> T dev.ultreon.libs.commons.v0.Identifier.reduce(java.util.function.BiFunction<java.lang.String, java.lang.String, T>)"""
        return object.__wrap(super(__Identifier, self).reduce(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Identifier.toString()"""
        return str.__wrap(super(Identifier, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def toArray(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.libs.commons.v0.Identifier.toArray()"""
        return List[str].__wrap(super(Identifier, self).toArray())

    @overload
    def location(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Identifier.location()"""
        return str.__wrap(super(Identifier, self).location())

    @overload
    def withPath(self, arg0: str) -> 'Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.withPath(java.lang.String)"""
        return 'Identifier'.__wrap(super(__Identifier, self).withPath(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.libs.commons.v0.Identifier(java.lang.String,java.lang.String)"""
        val = __Identifier(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def map(self, arg0: 'Function', arg1: 'Function') -> 'Identifier':
        """public dev.ultreon.libs.commons.v0.Identifier dev.ultreon.libs.commons.v0.Identifier.map(java.util.function.Function<java.lang.String, java.lang.String>,java.util.function.Function<java.lang.String, java.lang.String>)"""
        return 'Identifier'.__wrap(super(__Identifier, self).map(arg0, arg1))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.libs.commons.v0.Identifier(java.lang.String)"""
        val = __Identifier(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def setDefaultNamespace(arg0: str):
        """public static synchronized void dev.ultreon.libs.commons.v0.Identifier.setDefaultNamespace(java.lang.String)"""
        __Identifier.setDefaultNamespace(arg0)

    @overload
    def toPair(self) -> 'tuple.Pair':
        """public dev.ultreon.libs.commons.v0.tuple.Pair<java.lang.String, java.lang.String> dev.ultreon.libs.commons.v0.Identifier.toPair()"""
        return 'tuple.Pair'.__wrap(super(Identifier, self).toPair()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Downloader
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.CompletableFuture as __CompletableFuture
__CompletableFuture = __CompletableFuture
import dev.ultreon.libs.commons.v0.IDownloader as __IDownloader
__IDownloader = __IDownloader
import java.io.File as File
from builtins import float
import dev.ultreon.libs.commons.v0.Downloader as __Downloader
__Downloader = __Downloader
import java.net.URL as URL
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.concurrent.CompletableFuture as CompletableFuture
from builtins import int
 
class Downloader(__IDownloader, IDownloader):
    """dev.ultreon.libs.commons.v0.Downloader"""
 
    @staticmethod
    def __wrap(java_value: __Downloader) -> 'Downloader':
        return Downloader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Downloader):
        """
        Dynamic initializer for Downloader.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def downloadSync(self):
        """public void dev.ultreon.libs.commons.v0.Downloader.downloadSync() throws java.io.IOException"""
        super(Downloader, self).downloadSync()

    @overload
    def __init__(self, arg0: 'URL', arg1: 'OutputStream', arg2: int):
        """public dev.ultreon.libs.commons.v0.Downloader(java.net.URL,java.io.OutputStream,int)"""
        val = __Downloader(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getPercent(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Downloader.getPercent()"""
        return float.__wrap(super(Downloader, self).getPercent())

    @overload
    def __init__(self, arg0: 'URL', arg1: 'File', arg2: int):
        """public dev.ultreon.libs.commons.v0.Downloader(java.net.URL,java.io.File,int) throws java.io.IOException"""
        val = __Downloader(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getLength(self) -> int:
        """public long dev.ultreon.libs.commons.v0.Downloader.getLength()"""
        return int.__wrap(super(Downloader, self).getLength())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getRatio(self) -> float:
        """public float dev.ultreon.libs.commons.v0.Downloader.getRatio()"""
        return float.__wrap(super(Downloader, self).getRatio())

    @override
    @overload
    def downloadAsync(self) -> 'CompletableFuture':
        """public default java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.libs.commons.v0.IDownloader.downloadAsync()"""
        return 'CompletableFuture'.__wrap(super(IDownloader, self).downloadAsync())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getBlockSize(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Downloader.getBlockSize()"""
        return int.__wrap(super(Downloader, self).getBlockSize())

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
    def getBytesDownloaded(self) -> int:
        """public long dev.ultreon.libs.commons.v0.Downloader.getBytesDownloaded()"""
        return int.__wrap(super(Downloader, self).getBytesDownloaded()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Version
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.VersionType as __VersionType
__VersionType = __VersionType
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.libs.commons.v0.Version as __Version
__Version = __Version
from builtins import int
 
class Version(__Serializable, Serializable):
    """dev.ultreon.libs.commons.v0.Version"""
 
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def release(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Version.release()"""
        return int.__wrap(super(Version, self).release())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: 'VersionType', arg4: int):
        """public dev.ultreon.libs.commons.v0.Version(int,int,int,dev.ultreon.libs.commons.v0.VersionType,int)"""
        val = __Version(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def type(self) -> 'VersionType':
        """public dev.ultreon.libs.commons.v0.VersionType dev.ultreon.libs.commons.v0.Version.type()"""
        return 'VersionType'.__wrap(super(Version, self).type())

    @overload
    def minor(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Version.minor()"""
        return int.__wrap(super(Version, self).minor())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Version.toString()"""
        return str.__wrap(super(Version, self).toString())

    @overload
    def build(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Version.build()"""
        return int.__wrap(super(Version, self).build())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def major(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Version.major()"""
        return int.__wrap(super(Version, self).major())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Version.hashCode()"""
        return int.__wrap(super(Version, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Version.equals(java.lang.Object)"""
        return bool.__wrap(super(__Version, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Color
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.awt.Color as __Color
__Color = __Color
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.commons.v0.Color as __Color
__Color = __Color
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.awt.Color as Color
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Color():
    """dev.ultreon.libs.commons.v0.Color"""
 
    @staticmethod
    def __wrap(java_value: __Color) -> 'Color':
        return Color(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Color):
        """
        Dynamic initializer for Color.
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
    def withBlue(self, arg0: int) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.withBlue(int)"""
        return 'Color'.__wrap(super(__Color, self).withBlue(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def rgb(arg0: float, arg1: float, arg2: float) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgb(float,float,float)"""
        return Color.__wrap(__Color.rgb(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def hex(arg0: str) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.hex(java.lang.String)"""
        return Color.__wrap(__Color.hex(arg0))

    @staticmethod
    @overload
    def argb(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.argb(int)"""
        return Color.__wrap(__Color.argb(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def bgra(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.bgra(int)"""
        return Color.__wrap(__Color.bgra(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def abgr(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.abgr(int)"""
        return Color.__wrap(__Color.abgr(__int.valueOf(arg0)))

    @overload
    def withAlpha(self, arg0: int) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.withAlpha(int)"""
        return 'Color'.__wrap(super(__Color, self).withAlpha(__int.valueOf(arg0)))

    @overload
    def toAwt(self) -> 'Color':
        """public java.awt.Color dev.ultreon.libs.commons.v0.Color.toAwt()"""
        return 'Color'.__wrap(super(Color, self).toAwt())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def rgb(arg0: int, arg1: int, arg2: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgb(int,int,int)"""
        return Color.__wrap(__Color.rgb(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getGreen(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getGreen()"""
        return int.__wrap(super(Color, self).getGreen())

    @overload
    def getAlpha(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getAlpha()"""
        return int.__wrap(super(Color, self).getAlpha())

    @overload
    def getRgb(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getRgb()"""
        return int.__wrap(super(Color, self).getRgb())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.Color.toString()"""
        return str.__wrap(super(Color, self).toString())

    @staticmethod
    @overload
    def rgba(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgba(int)"""
        return Color.__wrap(__Color.rgba(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def bgr(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.bgr(int)"""
        return Color.__wrap(__Color.bgr(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def awt(arg0: 'Color') -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.awt(java.awt.Color)"""
        return Color.__wrap(__Color.awt(arg0))

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
    def getBlue(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getBlue()"""
        return int.__wrap(super(Color, self).getBlue())

    @staticmethod
    @overload
    def rgba(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgba(int,int,int,int)"""
        return Color.__wrap(__Color.rgba(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def darker(self) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.darker()"""
        return 'Color'.__wrap(super(Color, self).darker())

    @staticmethod
    @overload
    def rgba(arg0: float, arg1: float, arg2: float, arg3: float) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgba(float,float,float,float)"""
        return Color.__wrap(__Color.rgba(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def rgb(arg0: int) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.rgb(int)"""
        return Color.__wrap(__Color.rgb(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getRed(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getRed()"""
        return int.__wrap(super(Color, self).getRed())

    @overload
    def withGreen(self, arg0: int) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.withGreen(int)"""
        return 'Color'.__wrap(super(__Color, self).withGreen(__int.valueOf(arg0)))

    @overload
    def brighter(self) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.brighter()"""
        return 'Color'.__wrap(super(Color, self).brighter())

    @overload
    def getTransparency(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Color.getTransparency()"""
        return int.__wrap(super(Color, self).getTransparency())

    @staticmethod
    @overload
    def hsb(arg0: float, arg1: float, arg2: float) -> 'Color':
        """public static dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.hsb(float,float,float)"""
        return Color.__wrap(__Color.hsb(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def withRed(self, arg0: int) -> 'Color':
        """public dev.ultreon.libs.commons.v0.Color dev.ultreon.libs.commons.v0.Color.withRed(int)"""
        return 'Color'.__wrap(super(__Color, self).withRed(__int.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Insets
import java.awt.Insets as __Insets
__Insets = __Insets
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.libs.commons.v0.Insets as __Insets
__Insets = __Insets
from builtins import int
 
class Insets(__Insets, Insets):
    """dev.ultreon.libs.commons.v0.Insets"""
 
    @staticmethod
    def __wrap(java_value: __Insets) -> 'Insets':
        return Insets(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Insets):
        """
        Dynamic initializer for Insets.
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
    def clone(self) -> object:
        """public java.lang.Object java.awt.Insets.clone()"""
        return object.__wrap(super(Insets, self).clone())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.libs.commons.v0.Insets(int,int,int,int)"""
        val = __Insets(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def shrink(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.Insets.shrink(int)"""
        super(__Insets, self).shrink(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.awt.Insets.toString()"""
        return str.__wrap(super(Insets, self).toString())

    @overload
    def grow(self, arg0: int):
        """public void dev.ultreon.libs.commons.v0.Insets.grow(int)"""
        super(__Insets, self).grow(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.awt.Insets.hashCode()"""
        return int.__wrap(super(Insets, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.awt.Insets.equals(java.lang.Object)"""
        return bool.__wrap(super(__Insets, self).equals(arg0))

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void java.awt.Insets.set(int,int,int,int)"""
        super(__Insets, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.libs.commons.v0.IDownloader
import dev.ultreon.libs.commons.v0.IDownloader as __IDownloader
__IDownloader = __IDownloader
import java.util.concurrent.CompletableFuture as __CompletableFuture
__CompletableFuture = __CompletableFuture
from abc import abstractmethod, ABC
import java.util.concurrent.CompletableFuture as CompletableFuture
 
class IDownloader(ABC):
    """dev.ultreon.libs.commons.v0.IDownloader"""
 
    @staticmethod
    def __wrap(java_value: __IDownloader) -> 'IDownloader':
        return IDownloader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IDownloader):
        """
        Dynamic initializer for IDownloader.
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
 
    @abstractmethod
    def getBlockSize(self, ):
        """public abstract int dev.ultreon.libs.commons.v0.IDownloader.getBlockSize()"""
        pass

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

    @overload
    def downloadAsync(self) -> 'CompletableFuture':
        """public default java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.libs.commons.v0.IDownloader.downloadAsync()"""
        return 'CompletableFuture'.__wrap(super(IDownloader, self).downloadAsync())

    @abstractmethod
    def getLength(self, ):
        """public abstract long dev.ultreon.libs.commons.v0.IDownloader.getLength()"""
        pass

    @abstractmethod
    def getBytesDownloaded(self, ):
        """public abstract long dev.ultreon.libs.commons.v0.IDownloader.getBytesDownloaded()"""
        pass 
 
 
# CLASS: dev.ultreon.libs.commons.v0.ValueAnimator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.commons.v0.ValueAnimator as __ValueAnimator
__ValueAnimator = __ValueAnimator
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class ValueAnimator():
    """dev.ultreon.libs.commons.v0.ValueAnimator"""
 
    @staticmethod
    def __wrap(java_value: __ValueAnimator) -> 'ValueAnimator':
        return ValueAnimator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValueAnimator):
        """
        Dynamic initializer for ValueAnimator.
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
    def isEnded(self) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.ValueAnimator.isEnded()"""
        return bool.__wrap(super(ValueAnimator, self).isEnded())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public dev.ultreon.libs.commons.v0.ValueAnimator(double,double,double)"""
        val = __ValueAnimator(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def start(self):
        """public void dev.ultreon.libs.commons.v0.ValueAnimator.start()"""
        super(ValueAnimator, self).start()

    @overload
    def animate(self) -> float:
        """public double dev.ultreon.libs.commons.v0.ValueAnimator.animate()"""
        return float.__wrap(super(ValueAnimator, self).animate())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Messenger
import dev.ultreon.libs.commons.v0.Messenger as __Messenger
__Messenger = __Messenger
from abc import abstractmethod, ABC
 
class Messenger(ABC):
    """dev.ultreon.libs.commons.v0.Messenger"""
 
    @staticmethod
    def __wrap(java_value: __Messenger) -> 'Messenger':
        return Messenger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Messenger):
        """
        Dynamic initializer for Messenger.
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
 
    @abstractmethod
    def send(self, arg0: str):
        """public abstract void dev.ultreon.libs.commons.v0.Messenger.send(java.lang.String)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.commons.v0.DummyMessenger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.DummyMessenger as __DummyMessenger
__DummyMessenger = __DummyMessenger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.libs.commons.v0.MessengerImpl as __MessengerImpl
__MessengerImpl = __MessengerImpl
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DummyMessenger(__MessengerImpl, MessengerImpl):
    """dev.ultreon.libs.commons.v0.DummyMessenger"""
 
    @staticmethod
    def __wrap(java_value: __DummyMessenger) -> 'DummyMessenger':
        return DummyMessenger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DummyMessenger):
        """
        Dynamic initializer for DummyMessenger.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.DummyMessenger()"""
        val = __DummyMessenger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.MessengerImpl.send(java.lang.String)"""
        super(__MessengerImpl, self).send(arg0)

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

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.DummyMessenger()"""
        val = __DummyMessenger()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Anchor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.libs.commons.v0.Anchor as __Anchor
__Anchor = __Anchor
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
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
 
class Anchor(__Enum, Enum):
    """dev.ultreon.libs.commons.v0.Anchor"""
 
    @staticmethod
    def __wrap(java_value: __Anchor) -> 'Anchor':
        return Anchor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Anchor):
        """
        Dynamic initializer for Anchor.
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Anchor':
        """public static dev.ultreon.libs.commons.v0.Anchor dev.ultreon.libs.commons.v0.Anchor.valueOf(java.lang.String)"""
        return Anchor.__wrap(__Anchor.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Anchor.getY()"""
        return int.__wrap(super(Anchor, self).getY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def values() -> List['Anchor']:
        """public static dev.ultreon.libs.commons.v0.Anchor[] dev.ultreon.libs.commons.v0.Anchor.values()"""
        return List[Anchor].__wrap(__Anchor.values())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.libs.commons.v0.Anchor.getX()"""
        return int.__wrap(super(Anchor, self).getX())

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
 
 
# CLASS: dev.ultreon.libs.commons.v0.Logger
import dev.ultreon.libs.commons.v0.Logger as __Logger
__Logger = __Logger
import java.lang.String as __string
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class Logger(ABC):
    """dev.ultreon.libs.commons.v0.Logger"""
 
    @staticmethod
    def __wrap(java_value: __Logger) -> 'Logger':
        return Logger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Logger):
        """
        Dynamic initializer for Logger.
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
    def debug(self, arg0: str, arg1: 'Throwable'):
        """public default void dev.ultreon.libs.commons.v0.Logger.debug(java.lang.String,java.lang.Throwable)"""
        super(__Logger, self).debug(arg0, arg1)

    @overload
    def error(self, arg0: str):
        """public default void dev.ultreon.libs.commons.v0.Logger.error(java.lang.String)"""
        super(__Logger, self).error(arg0)

    @overload
    def warn(self, arg0: str):
        """public default void dev.ultreon.libs.commons.v0.Logger.warn(java.lang.String)"""
        super(__Logger, self).warn(arg0)

    @overload
    def log(self, arg0: str, arg1: 'Throwable'):
        """public default void dev.ultreon.libs.commons.v0.Logger.log(java.lang.String,java.lang.Throwable)"""
        super(__Logger, self).log(arg0, arg1)

    @overload
    def info(self, arg0: str):
        """public default void dev.ultreon.libs.commons.v0.Logger.info(java.lang.String)"""
        super(__Logger, self).info(arg0)

    @abstractmethod
    def log(self, arg0: 'Level', arg1: str, arg2: 'Throwable'):
        """public abstract void dev.ultreon.libs.commons.v0.Logger.log(dev.ultreon.libs.commons.v0.Logger$Level,java.lang.String,java.lang.Throwable)"""
        pass

    @overload
    def error(self, arg0: str, arg1: 'Throwable'):
        """public default void dev.ultreon.libs.commons.v0.Logger.error(java.lang.String,java.lang.Throwable)"""
        super(__Logger, self).error(arg0, arg1)

    @overload
    def debug(self, arg0: str):
        """public default void dev.ultreon.libs.commons.v0.Logger.debug(java.lang.String)"""
        super(__Logger, self).debug(arg0)

    @overload
    def warn(self, arg0: str, arg1: 'Throwable'):
        """public default void dev.ultreon.libs.commons.v0.Logger.warn(java.lang.String,java.lang.Throwable)"""
        super(__Logger, self).warn(arg0, arg1)

    @overload
    def log(self, arg0: str):
        """public default void dev.ultreon.libs.commons.v0.Logger.log(java.lang.String)"""
        super(__Logger, self).log(arg0)

    @overload
    def info(self, arg0: str, arg1: 'Throwable'):
        """public default void dev.ultreon.libs.commons.v0.Logger.info(java.lang.String,java.lang.Throwable)"""
        super(__Logger, self).info(arg0, arg1) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Either
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.libs.commons.v0.Either as __Either
__Either = __Either
from builtins import object
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Either():
    """dev.ultreon.libs.commons.v0.Either"""
 
    @staticmethod
    def __wrap(java_value: __Either) -> 'Either':
        return Either(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Either):
        """
        Dynamic initializer for Either.
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
    def getRightOrNullOr(self, arg0: object) -> object:
        """public R dev.ultreon.libs.commons.v0.Either.getRightOrNullOr(R)"""
        return object.__wrap(super(__Either, self).getRightOrNullOr(arg0))

    @overload
    def isRightPresent(self) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Either.isRightPresent()"""
        return bool.__wrap(super(Either, self).isRightPresent())

    @overload
    def ifLeftOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.libs.commons.v0.Either.ifLeftOrElse(java.util.function.Consumer<L>,java.lang.Runnable)"""
        super(__Either, self).ifLeftOrElse(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getLeftOrNull(self) -> object:
        """public L dev.ultreon.libs.commons.v0.Either.getLeftOrNull()"""
        return object.__wrap(super(Either, self).getLeftOrNull())

    @overload
    def ifLeft(self, arg0: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Either.ifLeft(java.util.function.Consumer<L>)"""
        super(__Either, self).ifLeft(arg0)

    @staticmethod
    @overload
    def left(arg0: object) -> 'Either':
        """public static <L,R> dev.ultreon.libs.commons.v0.Either<L, R> dev.ultreon.libs.commons.v0.Either.left(L)"""
        return Either.__wrap(__Either.left(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getRight(self) -> object:
        """public R dev.ultreon.libs.commons.v0.Either.getRight()"""
        return object.__wrap(super(Either, self).getRight())

    @overload
    def getRightOrNullOr(self, arg0: 'Supplier') -> object:
        """public R dev.ultreon.libs.commons.v0.Either.getRightOrNullOr(java.util.function.Supplier<? extends R>)"""
        return object.__wrap(super(__Either, self).getRightOrNullOr(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def ifAny(self, arg0: 'Consumer', arg1: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Either.ifAny(java.util.function.Consumer<L>,java.util.function.Consumer<R>)"""
        super(__Either, self).ifAny(arg0, arg1)

    @overload
    def ifRight(self, arg0: 'Consumer'):
        """public void dev.ultreon.libs.commons.v0.Either.ifRight(java.util.function.Consumer<R>)"""
        super(__Either, self).ifRight(arg0)

    @overload
    def getLeft(self) -> object:
        """public L dev.ultreon.libs.commons.v0.Either.getLeft()"""
        return object.__wrap(super(Either, self).getLeft())

    @overload
    def getRightOrNull(self) -> object:
        """public R dev.ultreon.libs.commons.v0.Either.getRightOrNull()"""
        return object.__wrap(super(Either, self).getRightOrNull())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getLeftOrNullOr(self, arg0: object) -> object:
        """public L dev.ultreon.libs.commons.v0.Either.getLeftOrNullOr(L)"""
        return object.__wrap(super(__Either, self).getLeftOrNullOr(arg0))

    @overload
    def isLeftPresent(self) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.Either.isLeftPresent()"""
        return bool.__wrap(super(Either, self).isLeftPresent())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def ifRightOrElse(self, arg0: 'Consumer', arg1: 'Runnable'):
        """public void dev.ultreon.libs.commons.v0.Either.ifRightOrElse(java.util.function.Consumer<R>,java.lang.Runnable)"""
        super(__Either, self).ifRightOrElse(arg0, arg1)

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
    def right(arg0: object) -> 'Either':
        """public static <L,R> dev.ultreon.libs.commons.v0.Either<L, R> dev.ultreon.libs.commons.v0.Either.right(R)"""
        return Either.__wrap(__Either.right(arg0))

    @overload
    def getLeftOrNullOrGet(self, arg0: 'Supplier') -> object:
        """public L dev.ultreon.libs.commons.v0.Either.getLeftOrNullOrGet(java.util.function.Supplier<? extends L>)"""
        return object.__wrap(super(__Either, self).getLeftOrNullOrGet(arg0)) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.Profiler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Runnable as Runnable
import dev.ultreon.libs.commons.v0.Profiler as __Profiler
__Profiler = __Profiler
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class Profiler():
    """dev.ultreon.libs.commons.v0.Profiler"""
 
    @staticmethod
    def __wrap(java_value: __Profiler) -> 'Profiler':
        return Profiler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Profiler):
        """
        Dynamic initializer for Profiler.
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
    def start(self):
        """public void dev.ultreon.libs.commons.v0.Profiler.start()"""
        super(Profiler, self).start()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def endSection(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.Profiler.endSection(java.lang.String)"""
        super(__Profiler, self).endSection(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def startSection(self, arg0: str):
        """public void dev.ultreon.libs.commons.v0.Profiler.startSection(java.lang.String)"""
        super(__Profiler, self).startSection(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.libs.commons.v0.Profiler()"""
        val = __Profiler()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def section(self, arg0: str, arg1: 'Runnable'):
        """public void dev.ultreon.libs.commons.v0.Profiler.section(java.lang.String,java.lang.Runnable)"""
        super(__Profiler, self).section(arg0, arg1)

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.commons.v0.Profiler()"""
        val = __Profiler()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def end(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.Long> dev.ultreon.libs.commons.v0.Profiler.end()"""
        return 'Map'.__wrap(super(Profiler, self).end())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))