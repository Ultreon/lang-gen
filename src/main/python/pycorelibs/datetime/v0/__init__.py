from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import dev.ultreon.libs.datetime.v0.Duration as _Duration
_Duration = _Duration
import java.math.BigDecimal as BigDecimal
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Duration():
    """dev.ultreon.libs.datetime.v0.Duration"""
 
    @staticmethod
    def _wrap(java_value: _Duration) -> 'Duration':
        return Duration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Duration):
        """
        Dynamic initializer for Duration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Duration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Duration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def toMillis(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toMillis()"""
        return int._wrap(super(Duration, self).toMillis())

    @staticmethod
    @overload
    def ofDays(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofDays(double)"""
        return Duration._wrap(_Duration.ofDays(_double.valueOf(arg0)))

    @overload
    def getYoctosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getYoctosecondPart()"""
        return int._wrap(super(Duration, self).getYoctosecondPart())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.datetime.v0.Duration.toString()"""
        return str._wrap(super(Duration, self).toString())

    @overload
    def getZeptosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getZeptosecondPart()"""
        return int._wrap(super(Duration, self).getZeptosecondPart())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def minus(self, arg0: 'Duration') -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.minus(dev.ultreon.libs.datetime.v0.Duration)"""
        return 'Duration'._wrap(super(_Duration, self).minus(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Duration.hashCode()"""
        return int._wrap(super(Duration, self).hashCode())

    @overload
    def getMinutes(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getMinutes()"""
        return float._wrap(super(Duration, self).getMinutes())

    @overload
    def getMinutePart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getMinutePart()"""
        return int._wrap(super(Duration, self).getMinutePart())

    @overload
    def getDays(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getDays()"""
        return float._wrap(super(Duration, self).getDays())

    @overload
    def negate(self) -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.negate()"""
        return 'Duration'._wrap(super(Duration, self).negate())

    @staticmethod
    @overload
    def ofNanoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofNanoseconds(double)"""
        return Duration._wrap(_Duration.ofNanoseconds(_double.valueOf(arg0)))

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
    def toBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.libs.datetime.v0.Duration.toBigInteger()"""
        return _transform(super(Duration, self).toBigInteger()).'BigInteger'Value()

    @overload
    def toLong(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toLong()"""
        return int._wrap(super(Duration, self).toLong())

    @overload
    def isNegative(self) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.isNegative()"""
        return bool._wrap(super(Duration, self).isNegative())

    @overload
    def getNanosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getNanosecondPart()"""
        return int._wrap(super(Duration, self).getNanosecondPart())

    @overload
    def getSeconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getSeconds()"""
        return float._wrap(super(Duration, self).getSeconds())

    @overload
    def getWeeks(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getWeeks()"""
        return float._wrap(super(Duration, self).getWeeks())

    @overload
    def toSeconds(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toSeconds()"""
        return int._wrap(super(Duration, self).toSeconds())

    @overload
    def toBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal dev.ultreon.libs.datetime.v0.Duration.toBigDecimal()"""
        return _transform(super(Duration, self).toBigDecimal()).'BigDecimal'Value()

    @overload
    def getHours(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getHours()"""
        return float._wrap(super(Duration, self).getHours())

    @overload
    def getDayPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getDayPart()"""
        return int._wrap(super(Duration, self).getDayPart())

    @overload
    def getSecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getSecondPart()"""
        return int._wrap(super(Duration, self).getSecondPart())

    @staticmethod
    @overload
    def ofHours(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofHours(double)"""
        return Duration._wrap(_Duration.ofHours(_double.valueOf(arg0)))

    @overload
    def getMicroseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getMicroseconds()"""
        return float._wrap(super(Duration, self).getMicroseconds())

    @overload
    def sleep(self):
        """public void dev.ultreon.libs.datetime.v0.Duration.sleep() throws java.lang.InterruptedException"""
        super(Duration, self).sleep()

    @overload
    def toFloat(self) -> float:
        """public float dev.ultreon.libs.datetime.v0.Duration.toFloat()"""
        return float._wrap(super(Duration, self).toFloat())

    @staticmethod
    @overload
    def ofPicoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofPicoseconds(double)"""
        return Duration._wrap(_Duration.ofPicoseconds(_double.valueOf(arg0)))

    @overload
    def clone(self) -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.clone()"""
        return 'Duration'._wrap(super(Duration, self).clone())

    @overload
    def getAttoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getAttoseconds()"""
        return float._wrap(super(Duration, self).getAttoseconds())

    @overload
    def toSimpleString(self) -> str:
        """public java.lang.String dev.ultreon.libs.datetime.v0.Duration.toSimpleString()"""
        return str._wrap(super(Duration, self).toSimpleString())

    @overload
    def toDouble(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.toDouble()"""
        return float._wrap(super(Duration, self).toDouble())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getMillisecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getMillisecondPart()"""
        return int._wrap(super(Duration, self).getMillisecondPart())

    @overload
    def toNanos(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toNanos()"""
        return int._wrap(super(Duration, self).toNanos())

    @overload
    def getNanoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getNanoseconds()"""
        return float._wrap(super(Duration, self).getNanoseconds())

    @staticmethod
    @overload
    def ofWeeks(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofWeeks(double)"""
        return Duration._wrap(_Duration.ofWeeks(_double.valueOf(arg0)))

    @overload
    def getFemtoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getFemtoseconds()"""
        return float._wrap(super(Duration, self).getFemtoseconds())

    @staticmethod
    @overload
    def ofMinutes(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofMinutes(double)"""
        return Duration._wrap(_Duration.ofMinutes(_double.valueOf(arg0)))

    @overload
    def plus(self, arg0: 'Duration') -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.plus(dev.ultreon.libs.datetime.v0.Duration)"""
        return 'Duration'._wrap(super(_Duration, self).plus(arg0))

    @overload
    def getMicrosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getMicrosecondPart()"""
        return int._wrap(super(Duration, self).getMicrosecondPart())

    @overload
    def getPicosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getPicosecondPart()"""
        return int._wrap(super(Duration, self).getPicosecondPart())

    @staticmethod
    @overload
    def ofAttoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofAttoseconds(double)"""
        return Duration._wrap(_Duration.ofAttoseconds(_double.valueOf(arg0)))

    @overload
    def getAttosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getAttosecondPart()"""
        return int._wrap(super(Duration, self).getAttosecondPart())

    @overload
    def compareTo(self, arg0: 'Duration') -> int:
        """public int dev.ultreon.libs.datetime.v0.Duration.compareTo(dev.ultreon.libs.datetime.v0.Duration)"""
        return int._wrap(super(_Duration, self).compareTo(arg0))

    @overload
    def getYoctoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getYoctoseconds()"""
        return float._wrap(super(Duration, self).getYoctoseconds())

    @staticmethod
    @overload
    def ofYoctoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofYoctoseconds(double)"""
        return Duration._wrap(_Duration.ofYoctoseconds(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def ofSeconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofSeconds(double)"""
        return Duration._wrap(_Duration.ofSeconds(_double.valueOf(arg0)))

    @overload
    def getPicoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getPicoseconds()"""
        return float._wrap(super(Duration, self).getPicoseconds())

    @staticmethod
    @overload
    def ofMilliseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofMilliseconds(double)"""
        return Duration._wrap(_Duration.ofMilliseconds(_double.valueOf(arg0)))

    @overload
    def isPositive(self) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.isPositive()"""
        return bool._wrap(super(Duration, self).isPositive())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getZeptoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getZeptoseconds()"""
        return float._wrap(super(Duration, self).getZeptoseconds())

    @overload
    def getMilliseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getMilliseconds()"""
        return float._wrap(super(Duration, self).getMilliseconds())

    @overload
    def getFemtosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getFemtosecondPart()"""
        return int._wrap(super(Duration, self).getFemtosecondPart())

    @overload
    def isZero(self) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.isZero()"""
        return bool._wrap(super(Duration, self).isZero())

    @overload
    def toInt(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Duration.toInt()"""
        return int._wrap(super(Duration, self).toInt())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getYears(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getYears()"""
        return float._wrap(super(Duration, self).getYears())

    @staticmethod
    @overload
    def ofYears(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofYears(double)"""
        return Duration._wrap(_Duration.ofYears(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def ofMicroseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofMicroseconds(double)"""
        return Duration._wrap(_Duration.ofMicroseconds(_double.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.equals(java.lang.Object)"""
        return bool._wrap(super(_Duration, self).equals(arg0))

    @staticmethod
    @overload
    def ofFemtoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofFemtoseconds(double)"""
        return Duration._wrap(_Duration.ofFemtoseconds(_double.valueOf(arg0)))

    @overload
    def getWeekPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getWeekPart()"""
        return int._wrap(super(Duration, self).getWeekPart())

    @staticmethod
    @overload
    def ofZeptoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofZeptoseconds(double)"""
        return Duration._wrap(_Duration.ofZeptoseconds(_double.valueOf(arg0)))

    @overload
    def getHourPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getHourPart()"""
        return int._wrap(super(Duration, self).getHourPart())

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.libs.datetime.v0.Duration(double)"""
        val = _Duration(_double.valueOf(arg0))
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.Duration
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import dev.ultreon.libs.datetime.v0.Duration as _Duration
_Duration = _Duration
import java.math.BigDecimal as BigDecimal
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Duration():
    """dev.ultreon.libs.datetime.v0.Duration"""
 
    @staticmethod
    def _wrap(java_value: _Duration) -> 'Duration':
        return Duration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Duration):
        """
        Dynamic initializer for Duration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Duration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Duration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def toMillis(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toMillis()"""
        return int._wrap(super(Duration, self).toMillis())

    @staticmethod
    @overload
    def ofDays(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofDays(double)"""
        return Duration._wrap(_Duration.ofDays(_double.valueOf(arg0)))

    @overload
    def getYoctosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getYoctosecondPart()"""
        return int._wrap(super(Duration, self).getYoctosecondPart())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.datetime.v0.Duration.toString()"""
        return str._wrap(super(Duration, self).toString())

    @overload
    def getZeptosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getZeptosecondPart()"""
        return int._wrap(super(Duration, self).getZeptosecondPart())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def minus(self, arg0: 'Duration') -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.minus(dev.ultreon.libs.datetime.v0.Duration)"""
        return 'Duration'._wrap(super(_Duration, self).minus(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Duration.hashCode()"""
        return int._wrap(super(Duration, self).hashCode())

    @overload
    def getMinutes(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getMinutes()"""
        return float._wrap(super(Duration, self).getMinutes())

    @overload
    def getMinutePart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getMinutePart()"""
        return int._wrap(super(Duration, self).getMinutePart())

    @overload
    def getDays(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getDays()"""
        return float._wrap(super(Duration, self).getDays())

    @overload
    def negate(self) -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.negate()"""
        return 'Duration'._wrap(super(Duration, self).negate())

    @staticmethod
    @overload
    def ofNanoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofNanoseconds(double)"""
        return Duration._wrap(_Duration.ofNanoseconds(_double.valueOf(arg0)))

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
    def toBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.libs.datetime.v0.Duration.toBigInteger()"""
        return _transform(super(Duration, self).toBigInteger()).'BigInteger'Value()

    @overload
    def toLong(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toLong()"""
        return int._wrap(super(Duration, self).toLong())

    @overload
    def isNegative(self) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.isNegative()"""
        return bool._wrap(super(Duration, self).isNegative())

    @overload
    def getNanosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getNanosecondPart()"""
        return int._wrap(super(Duration, self).getNanosecondPart())

    @overload
    def getSeconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getSeconds()"""
        return float._wrap(super(Duration, self).getSeconds())

    @overload
    def getWeeks(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getWeeks()"""
        return float._wrap(super(Duration, self).getWeeks())

    @overload
    def toSeconds(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toSeconds()"""
        return int._wrap(super(Duration, self).toSeconds())

    @overload
    def toBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal dev.ultreon.libs.datetime.v0.Duration.toBigDecimal()"""
        return _transform(super(Duration, self).toBigDecimal()).'BigDecimal'Value()

    @overload
    def getHours(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getHours()"""
        return float._wrap(super(Duration, self).getHours())

    @overload
    def getDayPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getDayPart()"""
        return int._wrap(super(Duration, self).getDayPart())

    @overload
    def getSecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getSecondPart()"""
        return int._wrap(super(Duration, self).getSecondPart())

    @staticmethod
    @overload
    def ofHours(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofHours(double)"""
        return Duration._wrap(_Duration.ofHours(_double.valueOf(arg0)))

    @overload
    def getMicroseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getMicroseconds()"""
        return float._wrap(super(Duration, self).getMicroseconds())

    @overload
    def sleep(self):
        """public void dev.ultreon.libs.datetime.v0.Duration.sleep() throws java.lang.InterruptedException"""
        super(Duration, self).sleep()

    @overload
    def toFloat(self) -> float:
        """public float dev.ultreon.libs.datetime.v0.Duration.toFloat()"""
        return float._wrap(super(Duration, self).toFloat())

    @staticmethod
    @overload
    def ofPicoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofPicoseconds(double)"""
        return Duration._wrap(_Duration.ofPicoseconds(_double.valueOf(arg0)))

    @overload
    def clone(self) -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.clone()"""
        return 'Duration'._wrap(super(Duration, self).clone())

    @overload
    def getAttoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getAttoseconds()"""
        return float._wrap(super(Duration, self).getAttoseconds())

    @overload
    def toSimpleString(self) -> str:
        """public java.lang.String dev.ultreon.libs.datetime.v0.Duration.toSimpleString()"""
        return str._wrap(super(Duration, self).toSimpleString())

    @overload
    def toDouble(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.toDouble()"""
        return float._wrap(super(Duration, self).toDouble())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getMillisecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getMillisecondPart()"""
        return int._wrap(super(Duration, self).getMillisecondPart())

    @overload
    def toNanos(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toNanos()"""
        return int._wrap(super(Duration, self).toNanos())

    @overload
    def getNanoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getNanoseconds()"""
        return float._wrap(super(Duration, self).getNanoseconds())

    @staticmethod
    @overload
    def ofWeeks(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofWeeks(double)"""
        return Duration._wrap(_Duration.ofWeeks(_double.valueOf(arg0)))

    @overload
    def getFemtoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getFemtoseconds()"""
        return float._wrap(super(Duration, self).getFemtoseconds())

    @staticmethod
    @overload
    def ofMinutes(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofMinutes(double)"""
        return Duration._wrap(_Duration.ofMinutes(_double.valueOf(arg0)))

    @overload
    def plus(self, arg0: 'Duration') -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.plus(dev.ultreon.libs.datetime.v0.Duration)"""
        return 'Duration'._wrap(super(_Duration, self).plus(arg0))

    @overload
    def getMicrosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getMicrosecondPart()"""
        return int._wrap(super(Duration, self).getMicrosecondPart())

    @overload
    def getPicosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getPicosecondPart()"""
        return int._wrap(super(Duration, self).getPicosecondPart())

    @staticmethod
    @overload
    def ofAttoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofAttoseconds(double)"""
        return Duration._wrap(_Duration.ofAttoseconds(_double.valueOf(arg0)))

    @overload
    def getAttosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getAttosecondPart()"""
        return int._wrap(super(Duration, self).getAttosecondPart())

    @overload
    def compareTo(self, arg0: 'Duration') -> int:
        """public int dev.ultreon.libs.datetime.v0.Duration.compareTo(dev.ultreon.libs.datetime.v0.Duration)"""
        return int._wrap(super(_Duration, self).compareTo(arg0))

    @overload
    def getYoctoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getYoctoseconds()"""
        return float._wrap(super(Duration, self).getYoctoseconds())

    @staticmethod
    @overload
    def ofYoctoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofYoctoseconds(double)"""
        return Duration._wrap(_Duration.ofYoctoseconds(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def ofSeconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofSeconds(double)"""
        return Duration._wrap(_Duration.ofSeconds(_double.valueOf(arg0)))

    @overload
    def getPicoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getPicoseconds()"""
        return float._wrap(super(Duration, self).getPicoseconds())

    @staticmethod
    @overload
    def ofMilliseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofMilliseconds(double)"""
        return Duration._wrap(_Duration.ofMilliseconds(_double.valueOf(arg0)))

    @overload
    def isPositive(self) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.isPositive()"""
        return bool._wrap(super(Duration, self).isPositive())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getZeptoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getZeptoseconds()"""
        return float._wrap(super(Duration, self).getZeptoseconds())

    @overload
    def getMilliseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getMilliseconds()"""
        return float._wrap(super(Duration, self).getMilliseconds())

    @overload
    def getFemtosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getFemtosecondPart()"""
        return int._wrap(super(Duration, self).getFemtosecondPart())

    @overload
    def isZero(self) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.isZero()"""
        return bool._wrap(super(Duration, self).isZero())

    @overload
    def toInt(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Duration.toInt()"""
        return int._wrap(super(Duration, self).toInt())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getYears(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getYears()"""
        return float._wrap(super(Duration, self).getYears())

    @staticmethod
    @overload
    def ofYears(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofYears(double)"""
        return Duration._wrap(_Duration.ofYears(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def ofMicroseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofMicroseconds(double)"""
        return Duration._wrap(_Duration.ofMicroseconds(_double.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.equals(java.lang.Object)"""
        return bool._wrap(super(_Duration, self).equals(arg0))

    @staticmethod
    @overload
    def ofFemtoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofFemtoseconds(double)"""
        return Duration._wrap(_Duration.ofFemtoseconds(_double.valueOf(arg0)))

    @overload
    def getWeekPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getWeekPart()"""
        return int._wrap(super(Duration, self).getWeekPart())

    @staticmethod
    @overload
    def ofZeptoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofZeptoseconds(double)"""
        return Duration._wrap(_Duration.ofZeptoseconds(_double.valueOf(arg0)))

    @overload
    def getHourPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getHourPart()"""
        return int._wrap(super(Duration, self).getHourPart())

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.libs.datetime.v0.Duration(double)"""
        val = _Duration(_double.valueOf(arg0))
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.Duration 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.DateTime
import java.time.Instant as Instant
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.time.LocalTime as LocalTime
import dev.ultreon.libs.datetime.v0.Date as _Date
_Date = _Date
import java.time.LocalDateTime as _LocalDateTime
_LocalDateTime = _LocalDateTime
import dev.ultreon.libs.datetime.v0.Duration as _Duration
_Duration = _Duration
from builtins import bool
import dev.ultreon.libs.datetime.v0.DateTime as _DateTime
_DateTime = _DateTime
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.time.LocalDateTime as LocalDateTime
import dev.ultreon.libs.datetime.v0.Month as _Month
_Month = _Month
import java.lang.String as _String
_String = _String
import java.time.ZoneOffset as ZoneOffset
import dev.ultreon.libs.datetime.v0.Time as _Time
_Time = _Time
import java.time.LocalDate as LocalDate
import java.lang.Integer as _int
import dev.ultreon.libs.datetime.v0.DayPeriod as _DayPeriod
_DayPeriod = _DayPeriod
import java.time.LocalTime as _LocalTime
_LocalTime = _LocalTime
import java.lang.Long as _long
from builtins import int
import java.time.LocalDate as _LocalDate
_LocalDate = _LocalDate
import java.lang.Class as _Class
_Class = _Class
 
class DateTime():
    """dev.ultreon.libs.datetime.v0.DateTime"""
 
    @staticmethod
    def _wrap(java_value: _DateTime) -> 'DateTime':
        return DateTime(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DateTime):
        """
        Dynamic initializer for DateTime.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DateTime__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DateTime__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def clone(self) -> 'DateTime':
        """public dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.clone()"""
        return 'DateTime'._wrap(super(DateTime, self).clone())

    @staticmethod
    @overload
    def ofLocalDateTime(arg0: 'LocalDateTime') -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.ofLocalDateTime(java.time.LocalDateTime)"""
        return DateTime._wrap(_DateTime.ofLocalDateTime(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Date', arg1: 'Time'):
        """public dev.ultreon.libs.datetime.v0.DateTime(dev.ultreon.libs.datetime.v0.Date,dev.ultreon.libs.datetime.v0.Time)"""
        val = _DateTime(arg0, arg1)
        self.__wrapper = val

    @overload
    def toLocalDateTime(self) -> 'LocalDateTime':
        """public java.time.LocalDateTime dev.ultreon.libs.datetime.v0.DateTime.toLocalDateTime()"""
        return 'LocalDateTime'._wrap(super(DateTime, self).toLocalDateTime())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def toEpochNano(self, arg0: 'ZoneOffset') -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochNano(java.time.ZoneOffset)"""
        return int._wrap(super(_DateTime, self).toEpochNano(arg0))

    @overload
    def getMonthIndex(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getMonthIndex()"""
        return int._wrap(super(DateTime, self).getMonthIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'DateTime'):
        """public dev.ultreon.libs.datetime.v0.DateTime(dev.ultreon.libs.datetime.v0.DateTime)"""
        val = _DateTime(arg0)
        self.__wrapper = val

    @overload
    def setSecond(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setSecond(int)"""
        super(_DateTime, self).setSecond(_int.valueOf(arg0))

    @overload
    def setHour(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setHour(int)"""
        super(_DateTime, self).setHour(_int.valueOf(arg0))

    @overload
    def getDate(self) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.DateTime.getDate()"""
        return 'Date'._wrap(super(DateTime, self).getDate())

    @overload
    def toEpochMilli(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochMilli()"""
        return int._wrap(super(DateTime, self).toEpochMilli())

    @overload
    def __init__(self, arg0: int, arg1: 'Month', arg2: int, arg3: int, arg4: int, arg5: int):
        """public dev.ultreon.libs.datetime.v0.DateTime(int,dev.ultreon.libs.datetime.v0.Month,int,int,int,int)"""
        val = _DateTime(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))
        self.__wrapper = val

    @overload
    def getYear(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getYear()"""
        return int._wrap(super(DateTime, self).getYear())

    @overload
    def setYear(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setYear(int)"""
        super(_DateTime, self).setYear(_int.valueOf(arg0))

    @overload
    def setTime(self, arg0: 'Time'):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setTime(dev.ultreon.libs.datetime.v0.Time)"""
        super(_DateTime, self).setTime(arg0)

    @overload
    def setDay(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setDay(int)"""
        super(_DateTime, self).setDay(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setMonth(self, arg0: 'Month'):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setMonth(dev.ultreon.libs.datetime.v0.Month)"""
        super(_DateTime, self).setMonth(arg0)

    @overload
    def getNano(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getNano()"""
        return int._wrap(super(DateTime, self).getNano())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.hashCode()"""
        return int._wrap(super(DateTime, self).hashCode())

    @staticmethod
    @overload
    def ofEpochMilli(arg0: int, arg1: 'ZoneOffset') -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.ofEpochMilli(long,java.time.ZoneOffset)"""
        return DateTime._wrap(_DateTime.ofEpochMilli(_long.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: int, arg1: 'Month', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public dev.ultreon.libs.datetime.v0.DateTime(int,dev.ultreon.libs.datetime.v0.Month,int,int,int,int,int)"""
        val = _DateTime(_int.valueOf(arg0), arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))
        self.__wrapper = val

    @overload
    def toEpochSecond(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochSecond()"""
        return int._wrap(super(DateTime, self).toEpochSecond())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.DateTime.equals(java.lang.Object)"""
        return bool._wrap(super(_DateTime, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def toLocalDate(self) -> 'LocalDate':
        """public java.time.LocalDate dev.ultreon.libs.datetime.v0.DateTime.toLocalDate()"""
        return 'LocalDate'._wrap(super(DateTime, self).toLocalDate())

    @staticmethod
    @overload
    def ofEpochNano(arg0: int, arg1: 'ZoneOffset') -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.ofEpochNano(long,java.time.ZoneOffset)"""
        return DateTime._wrap(_DateTime.ofEpochNano(_long.valueOf(arg0), arg1))

    @overload
    def setMonthIndex(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setMonthIndex(int)"""
        super(_DateTime, self).setMonthIndex(_int.valueOf(arg0))

    @staticmethod
    @overload
    def isBetween(arg0: 'DateTime', arg1: 'DateTime') -> bool:
        """public static boolean dev.ultreon.libs.datetime.v0.DateTime.isBetween(dev.ultreon.libs.datetime.v0.DateTime,dev.ultreon.libs.datetime.v0.DateTime)"""
        return bool._wrap(_DateTime.isBetween(arg0, arg1))

    @overload
    def getDayPeriod(self) -> 'DayPeriod':
        """public dev.ultreon.libs.datetime.v0.DayPeriod dev.ultreon.libs.datetime.v0.DateTime.getDayPeriod()"""
        return 'DayPeriod'._wrap(super(DateTime, self).getDayPeriod())

    @staticmethod
    @overload
    def ofEpochSecond(arg0: int, arg1: 'ZoneOffset') -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.ofEpochSecond(long,java.time.ZoneOffset)"""
        return DateTime._wrap(_DateTime.ofEpochSecond(_long.valueOf(arg0), arg1))

    @overload
    def getHour(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getHour()"""
        return int._wrap(super(DateTime, self).getHour())

    @staticmethod
    @overload
    def ofInstant(arg0: 'Instant', arg1: 'ZoneOffset') -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.ofInstant(java.time.Instant,java.time.ZoneOffset)"""
        return DateTime._wrap(_DateTime.ofInstant(arg0, arg1))

    @overload
    def getTime(self) -> 'Time':
        """public dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.DateTime.getTime()"""
        return 'Time'._wrap(super(DateTime, self).getTime())

    @overload
    def toEpochSeconds(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochSeconds()"""
        return int._wrap(super(DateTime, self).toEpochSeconds())

    @staticmethod
    @overload
    def isLeapYear(arg0: int) -> bool:
        """public static boolean dev.ultreon.libs.datetime.v0.DateTime.isLeapYear(int)"""
        return bool._wrap(_DateTime.isLeapYear(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public dev.ultreon.libs.datetime.v0.DateTime(int,int,int,int,int,int,int)"""
        val = _DateTime(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))
        self.__wrapper = val

    @overload
    def toEpochSecond(self, arg0: 'ZoneOffset') -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochSecond(java.time.ZoneOffset)"""
        return int._wrap(super(_DateTime, self).toEpochSecond(arg0))

    @overload
    def getDuration(self) -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.DateTime.getDuration()"""
        return 'Duration'._wrap(super(DateTime, self).getDuration())

    @overload
    def getMonth(self) -> 'Month':
        """public dev.ultreon.libs.datetime.v0.Month dev.ultreon.libs.datetime.v0.DateTime.getMonth()"""
        return 'Month'._wrap(super(DateTime, self).getMonth())

    @overload
    def setNano(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setNano(int)"""
        super(_DateTime, self).setNano(_int.valueOf(arg0))

    @overload
    def getMinute(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getMinute()"""
        return int._wrap(super(DateTime, self).getMinute())

    @overload
    def getDate(self, arg0: 'Date'):
        """public void dev.ultreon.libs.datetime.v0.DateTime.getDate(dev.ultreon.libs.datetime.v0.Date)"""
        super(_DateTime, self).getDate(arg0)

    @overload
    def toEpochMilli(self, arg0: 'ZoneOffset') -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochMilli(java.time.ZoneOffset)"""
        return int._wrap(super(_DateTime, self).toEpochMilli(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def compareTo(self, arg0: 'DateTime') -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.compareTo(dev.ultreon.libs.datetime.v0.DateTime)"""
        return int._wrap(super(_DateTime, self).compareTo(arg0))

    @overload
    def setMinute(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setMinute(int)"""
        super(_DateTime, self).setMinute(_int.valueOf(arg0))

    @overload
    def toLocalTime(self) -> 'LocalTime':
        """public java.time.LocalTime dev.ultreon.libs.datetime.v0.DateTime.toLocalTime()"""
        return 'LocalTime'._wrap(super(DateTime, self).toLocalTime())

    @overload
    def getDay(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getDay()"""
        return int._wrap(super(DateTime, self).getDay())

    @staticmethod
    @overload
    def current() -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.current()"""
        return DateTime._wrap(_DateTime.current())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def toEpochNano(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochNano()"""
        return int._wrap(super(DateTime, self).toEpochNano())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public dev.ultreon.libs.datetime.v0.DateTime(int,int,int,int,int,int)"""
        val = _DateTime(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))
        self.__wrapper = val

    @overload
    def getSecond(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getSecond()"""
        return int._wrap(super(DateTime, self).getSecond()) 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.TimeSpan
import dev.ultreon.libs.datetime.v0.DateTime as _DateTime
_DateTime = _DateTime
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.libs.datetime.v0.TimeSpan as _TimeSpan
_TimeSpan = _TimeSpan
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.libs.datetime.v0.Duration as _Duration
_Duration = _Duration
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TimeSpan():
    """dev.ultreon.libs.datetime.v0.TimeSpan"""
 
    @staticmethod
    def _wrap(java_value: _TimeSpan) -> 'TimeSpan':
        return TimeSpan(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TimeSpan):
        """
        Dynamic initializer for TimeSpan.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TimeSpan__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TimeSpan__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setFrom(self, arg0: 'DateTime'):
        """public void dev.ultreon.libs.datetime.v0.TimeSpan.setFrom(dev.ultreon.libs.datetime.v0.DateTime)"""
        super(_TimeSpan, self).setFrom(arg0)

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
    def contains(self, arg0: 'DateTime') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.TimeSpan.contains(dev.ultreon.libs.datetime.v0.DateTime)"""
        return bool._wrap(super(_TimeSpan, self).contains(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setTo(self, arg0: 'DateTime'):
        """public void dev.ultreon.libs.datetime.v0.TimeSpan.setTo(dev.ultreon.libs.datetime.v0.DateTime)"""
        super(_TimeSpan, self).setTo(arg0)

    @overload
    def __init__(self, arg0: 'DateTime', arg1: 'DateTime'):
        """public dev.ultreon.libs.datetime.v0.TimeSpan(dev.ultreon.libs.datetime.v0.DateTime,dev.ultreon.libs.datetime.v0.DateTime)"""
        val = _TimeSpan(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def toDuration(self) -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.TimeSpan.toDuration()"""
        return 'Duration'._wrap(super(TimeSpan, self).toDuration())

    @overload
    def getTo(self) -> 'DateTime':
        """public dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.TimeSpan.getTo()"""
        return 'DateTime'._wrap(super(TimeSpan, self).getTo())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getFrom(self) -> 'DateTime':
        """public dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.TimeSpan.getFrom()"""
        return 'DateTime'._wrap(super(TimeSpan, self).getFrom())

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
    def clone(self) -> 'TimeSpan':
        """public dev.ultreon.libs.datetime.v0.TimeSpan dev.ultreon.libs.datetime.v0.TimeSpan.clone()"""
        return 'TimeSpan'._wrap(super(TimeSpan, self).clone())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.DayPeriod
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import dev.ultreon.libs.datetime.v0.Time as _Time
_Time = _Time
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import dev.ultreon.libs.datetime.v0.DayPeriod as _DayPeriod
_DayPeriod = _DayPeriod
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DayPeriod():
    """dev.ultreon.libs.datetime.v0.DayPeriod"""
 
    @staticmethod
    def _wrap(java_value: _DayPeriod) -> 'DayPeriod':
        return DayPeriod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DayPeriod):
        """
        Dynamic initializer for DayPeriod.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DayPeriod__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DayPeriod__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getStart(self) -> 'Time':
        """public dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.DayPeriod.getStart()"""
        return 'Time'._wrap(super(DayPeriod, self).getStart())

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
    def isWithin(self, arg0: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.DayPeriod.isWithin(dev.ultreon.libs.datetime.v0.Time)"""
        return bool._wrap(super(_DayPeriod, self).isWithin(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'DayPeriod':
        """public static dev.ultreon.libs.datetime.v0.DayPeriod dev.ultreon.libs.datetime.v0.DayPeriod.valueOf(java.lang.String)"""
        return DayPeriod._wrap(_DayPeriod.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['DayPeriod']:
        """public static dev.ultreon.libs.datetime.v0.DayPeriod[] dev.ultreon.libs.datetime.v0.DayPeriod.values()"""
        return List[DayPeriod]._wrap(_DayPeriod.values())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @overload
    def getEnd(self) -> 'Time':
        """public dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.DayPeriod.getEnd()"""
        return 'Time'._wrap(super(DayPeriod, self).getEnd())

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
 
 
# CLASS: dev.ultreon.libs.datetime.v0.Month
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.datetime.v0.Month as _Month
_Month = _Month
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import dev.ultreon.libs.datetime.v0.Date as _Date
_Date = _Date
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Month():
    """dev.ultreon.libs.datetime.v0.Month"""
 
    @staticmethod
    def _wrap(java_value: _Month) -> 'Month':
        return Month(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Month):
        """
        Dynamic initializer for Month.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Month__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Month__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def asDate(self, arg0: int, arg1: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Month.asDate(int,int)"""
        return 'Date'._wrap(super(_Month, self).asDate(_int.valueOf(arg0), _int.valueOf(arg1)))

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
    def values() -> List['Month']:
        """public static dev.ultreon.libs.datetime.v0.Month[] dev.ultreon.libs.datetime.v0.Month.values()"""
        return List[Month]._wrap(_Month.values())

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
    def startDate(self, arg0: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Month.startDate(int)"""
        return 'Date'._wrap(super(_Month, self).startDate(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Month':
        """public static dev.ultreon.libs.datetime.v0.Month dev.ultreon.libs.datetime.v0.Month.valueOf(java.lang.String)"""
        return Month._wrap(_Month.valueOf(arg0))

    @overload
    def getDays(self, arg0: int) -> int:
        """public int dev.ultreon.libs.datetime.v0.Month.getDays(int)"""
        return int._wrap(super(_Month, self).getDays(_int.valueOf(arg0)))

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

    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Month.getIndex()"""
        return int._wrap(super(Month, self).getIndex())

    @overload
    def endDate(self, arg0: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Month.endDate(int)"""
        return 'Date'._wrap(super(_Month, self).endDate(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def from(arg0: int) -> 'Month':
        """public static dev.ultreon.libs.datetime.v0.Month dev.ultreon.libs.datetime.v0.Month.from(int)"""
        return Month._wrap(_Month.from(_int.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.Time
import java.time.Instant as Instant
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.time.LocalTime as LocalTime
from builtins import float
import java.lang.String as _String
_String = _String
import java.time.ZoneOffset as ZoneOffset
import dev.ultreon.libs.datetime.v0.Time as _Time
_Time = _Time
import java.lang.Integer as _int
import dev.ultreon.libs.datetime.v0.DayPeriod as _DayPeriod
_DayPeriod = _DayPeriod
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Time():
    """dev.ultreon.libs.datetime.v0.Time"""
 
    @staticmethod
    def _wrap(java_value: _Time) -> 'Time':
        return Time(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Time):
        """
        Dynamic initializer for Time.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Time__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Time__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def current() -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.current()"""
        return Time._wrap(_Time.current())

    @staticmethod
    @overload
    def ofInstant(arg0: 'Instant', arg1: 'ZoneOffset') -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.ofInstant(java.time.Instant,java.time.ZoneOffset)"""
        return Time._wrap(_Time.ofInstant(arg0, arg1))

    @overload
    def isBetween(self, arg0: 'Time', arg1: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.isBetween(dev.ultreon.libs.datetime.v0.Time,dev.ultreon.libs.datetime.v0.Time)"""
        return bool._wrap(super(_Time, self).isBetween(arg0, arg1))

    @overload
    def isBefore(self, arg0: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.isBefore(dev.ultreon.libs.datetime.v0.Time)"""
        return bool._wrap(super(_Time, self).isBefore(arg0))

    @overload
    def toHours(self) -> float:
        """public float dev.ultreon.libs.datetime.v0.Time.toHours()"""
        return float._wrap(super(Time, self).toHours())

    @overload
    def toMillis(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Time.toMillis()"""
        return int._wrap(super(Time, self).toMillis())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.hashCode()"""
        return int._wrap(super(Time, self).hashCode())

    @overload
    def toSeconds(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.toSeconds()"""
        return int._wrap(super(Time, self).toSeconds())

    @staticmethod
    @overload
    def ofMillis(arg0: int) -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.ofMillis(long)"""
        return Time._wrap(_Time.ofMillis(_long.valueOf(arg0)))

    @overload
    def getNano(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.getNano()"""
        return int._wrap(super(Time, self).getNano())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setHour(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Time.setHour(int)"""
        super(_Time, self).setHour(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toNanos(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Time.toNanos()"""
        return int._wrap(super(Time, self).toNanos())

    @overload
    def getHour(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.getHour()"""
        return int._wrap(super(Time, self).getHour())

    @staticmethod
    @overload
    def ofNanos(arg0: int) -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.ofNanos(long)"""
        return Time._wrap(_Time.ofNanos(_long.valueOf(arg0)))

    @overload
    def setNano(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Time.setNano(int)"""
        super(_Time, self).setNano(_int.valueOf(arg0))

    @overload
    def isBeforeOrEqual(self, arg0: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.isBeforeOrEqual(dev.ultreon.libs.datetime.v0.Time)"""
        return bool._wrap(super(_Time, self).isBeforeOrEqual(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.libs.datetime.v0.Time(int,int,int,int)"""
        val = _Time(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @overload
    def getSecond(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.getSecond()"""
        return int._wrap(super(Time, self).getSecond())

    @staticmethod
    @overload
    def ofLocalTime(arg0: 'LocalTime') -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.ofLocalTime(java.time.LocalTime)"""
        return Time._wrap(_Time.ofLocalTime(arg0))

    @overload
    def isAfter(self, arg0: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.isAfter(dev.ultreon.libs.datetime.v0.Time)"""
        return bool._wrap(super(_Time, self).isAfter(arg0))

    @overload
    def getDayPeriod(self) -> 'DayPeriod':
        """public dev.ultreon.libs.datetime.v0.DayPeriod dev.ultreon.libs.datetime.v0.Time.getDayPeriod()"""
        return 'DayPeriod'._wrap(super(Time, self).getDayPeriod())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.libs.datetime.v0.Time(int,int,int)"""
        val = _Time(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.equals(java.lang.Object)"""
        return bool._wrap(super(_Time, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setMinute(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Time.setMinute(int)"""
        super(_Time, self).setMinute(_int.valueOf(arg0))

    @overload
    def toMinutes(self) -> float:
        """public float dev.ultreon.libs.datetime.v0.Time.toMinutes()"""
        return float._wrap(super(Time, self).toMinutes())

    @staticmethod
    @overload
    def ofSeconds(arg0: int) -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.ofSeconds(long)"""
        return Time._wrap(_Time.ofSeconds(_long.valueOf(arg0)))

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
    def compareTo(self, arg0: 'Time') -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.compareTo(dev.ultreon.libs.datetime.v0.Time)"""
        return int._wrap(super(_Time, self).compareTo(arg0))

    @overload
    def isAfterOrEqual(self, arg0: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.isAfterOrEqual(dev.ultreon.libs.datetime.v0.Time)"""
        return bool._wrap(super(_Time, self).isAfterOrEqual(arg0))

    @overload
    def clone(self) -> 'Time':
        """public dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.clone()"""
        return 'Time'._wrap(super(Time, self).clone())

    @overload
    def getMinute(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.getMinute()"""
        return int._wrap(super(Time, self).getMinute())

    @overload
    def setSecond(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Time.setSecond(int)"""
        super(_Time, self).setSecond(_int.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.MeteorologicalSeason
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import dev.ultreon.libs.datetime.v0.MeteorologicalSeason as _MeteorologicalSeason
_MeteorologicalSeason = _MeteorologicalSeason
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import dev.ultreon.libs.datetime.v0.Date as _Date
_Date = _Date
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MeteorologicalSeason():
    """dev.ultreon.libs.datetime.v0.MeteorologicalSeason"""
 
    @staticmethod
    def _wrap(java_value: _MeteorologicalSeason) -> 'MeteorologicalSeason':
        return MeteorologicalSeason(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MeteorologicalSeason):
        """
        Dynamic initializer for MeteorologicalSeason.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MeteorologicalSeason__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MeteorologicalSeason__wrapper":
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
    def getEndDate(self, arg0: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.MeteorologicalSeason.getEndDate(int)"""
        return 'Date'._wrap(super(_MeteorologicalSeason, self).getEndDate(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['MeteorologicalSeason']:
        """public static dev.ultreon.libs.datetime.v0.MeteorologicalSeason[] dev.ultreon.libs.datetime.v0.MeteorologicalSeason.values()"""
        return List[MeteorologicalSeason]._wrap(_MeteorologicalSeason.values())

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
    def valueOf(arg0: str) -> 'MeteorologicalSeason':
        """public static dev.ultreon.libs.datetime.v0.MeteorologicalSeason dev.ultreon.libs.datetime.v0.MeteorologicalSeason.valueOf(java.lang.String)"""
        return MeteorologicalSeason._wrap(_MeteorologicalSeason.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @overload
    def getStartDate(self, arg0: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.MeteorologicalSeason.getStartDate(int)"""
        return 'Date'._wrap(super(_MeteorologicalSeason, self).getStartDate(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.Date
import java.time.Instant as Instant
import java.time.chrono.IsoChronology as _IsoChronology
_IsoChronology = _IsoChronology
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import dev.ultreon.libs.datetime.v0.TimeSpan as _TimeSpan
_TimeSpan = _TimeSpan
from builtins import type
import dev.ultreon.libs.datetime.v0.Month as _Month
_Month = _Month
import java.time.chrono.Era as Era
import java.lang.String as _String
_String = _String
import java.time.ZoneOffset as ZoneOffset
import dev.ultreon.libs.datetime.v0.MeteorologicalSeason as _MeteorologicalSeason
_MeteorologicalSeason = _MeteorologicalSeason
import dev.ultreon.libs.datetime.v0.Date as _Date
_Date = _Date
import java.time.LocalDate as LocalDate
import java.lang.Integer as _int
import java.time.chrono.Era as _Era
_Era = _Era
import java.time.DayOfWeek as DayOfWeek
from builtins import bool
import java.lang.Long as _long
import java.time.chrono.IsoChronology as IsoChronology
from builtins import int
import java.time.DayOfWeek as _DayOfWeek
_DayOfWeek = _DayOfWeek
import java.lang.Class as _Class
_Class = _Class
 
class Date():
    """dev.ultreon.libs.datetime.v0.Date"""
 
    @staticmethod
    def _wrap(java_value: _Date) -> 'Date':
        return Date(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Date):
        """
        Dynamic initializer for Date.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Date__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Date__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isLeapYear(self) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Date.isLeapYear()"""
        return bool._wrap(super(Date, self).isLeapYear())

    @overload
    def toTimeSpan(self) -> 'TimeSpan':
        """public dev.ultreon.libs.datetime.v0.TimeSpan dev.ultreon.libs.datetime.v0.Date.toTimeSpan()"""
        return 'TimeSpan'._wrap(super(Date, self).toTimeSpan())

    @overload
    def getSeason(self) -> 'MeteorologicalSeason':
        """public dev.ultreon.libs.datetime.v0.MeteorologicalSeason dev.ultreon.libs.datetime.v0.Date.getSeason()"""
        return 'MeteorologicalSeason'._wrap(super(Date, self).getSeason())

    @staticmethod
    @overload
    def ofInstant(arg0: 'Instant', arg1: 'ZoneOffset') -> 'Date':
        """public static dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.ofInstant(java.time.Instant,java.time.ZoneOffset)"""
        return Date._wrap(_Date.ofInstant(arg0, arg1))

    @overload
    def getMonthIndex(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.getMonthIndex()"""
        return int._wrap(super(Date, self).getMonthIndex())

    @overload
    def getDayOfYear(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.getDayOfYear()"""
        return int._wrap(super(Date, self).getDayOfYear())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def clone(self) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.clone()"""
        return 'Date'._wrap(super(Date, self).clone())

    @overload
    def toEpochSecond(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Date.toEpochSecond()"""
        return int._wrap(super(Date, self).toEpochSecond())

    @overload
    def setMonthIndex(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Date.setMonthIndex(int)"""
        super(_Date, self).setMonthIndex(_int.valueOf(arg0))

    @overload
    def getDay(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.getDay()"""
        return int._wrap(super(Date, self).getDay())

    @overload
    def getEra(self) -> 'Era':
        """public java.time.chrono.Era dev.ultreon.libs.datetime.v0.Date.getEra()"""
        return 'Era'._wrap(super(Date, self).getEra())

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
    def setMonth(self, arg0: 'Month'):
        """public void dev.ultreon.libs.datetime.v0.Date.setMonth(dev.ultreon.libs.datetime.v0.Month)"""
        super(_Date, self).setMonth(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Date.equals(java.lang.Object)"""
        return bool._wrap(super(_Date, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.hashCode()"""
        return int._wrap(super(Date, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: 'Month', arg2: int):
        """public dev.ultreon.libs.datetime.v0.Date(int,dev.ultreon.libs.datetime.v0.Month,int)"""
        val = _Date(_int.valueOf(arg0), arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getYear(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.getYear()"""
        return int._wrap(super(Date, self).getYear())

    @overload
    def setDay(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Date.setDay(int)"""
        super(_Date, self).setDay(_int.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Date') -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.compareTo(dev.ultreon.libs.datetime.v0.Date)"""
        return int._wrap(super(_Date, self).compareTo(arg0))

    @overload
    def toEpochDay(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Date.toEpochDay()"""
        return int._wrap(super(Date, self).toEpochDay())

    @overload
    def setYear(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Date.setYear(int)"""
        super(_Date, self).setYear(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def ofEpochDay(arg0: int) -> 'Date':
        """public static dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.ofEpochDay(long)"""
        return Date._wrap(_Date.ofEpochDay(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ofLocalDate(arg0: 'LocalDate') -> 'Date':
        """public static dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.ofLocalDate(java.time.LocalDate)"""
        return Date._wrap(_Date.ofLocalDate(arg0))

    @staticmethod
    @overload
    def isBetween(arg0: 'Date', arg1: 'Date') -> bool:
        """public static boolean dev.ultreon.libs.datetime.v0.Date.isBetween(dev.ultreon.libs.datetime.v0.Date,dev.ultreon.libs.datetime.v0.Date)"""
        return bool._wrap(_Date.isBetween(arg0, arg1))

    @overload
    def equalsIgnoreYear(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Date.equalsIgnoreYear(java.lang.Object)"""
        return bool._wrap(super(_Date, self).equalsIgnoreYear(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def toEpochMilli(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Date.toEpochMilli()"""
        return int._wrap(super(Date, self).toEpochMilli())

    @staticmethod
    @overload
    def current() -> 'Date':
        """public static dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.current()"""
        return Date._wrap(_Date.current())

    @overload
    def getChronology(self) -> 'IsoChronology':
        """public java.time.chrono.IsoChronology dev.ultreon.libs.datetime.v0.Date.getChronology()"""
        return 'IsoChronology'._wrap(super(Date, self).getChronology())

    @staticmethod
    @overload
    def ofEpochSecond(arg0: int) -> 'Date':
        """public static dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.ofEpochSecond(long)"""
        return Date._wrap(_Date.ofEpochSecond(_long.valueOf(arg0)))

    @overload
    def getDayOfWeek(self) -> 'DayOfWeek':
        """public java.time.DayOfWeek dev.ultreon.libs.datetime.v0.Date.getDayOfWeek()"""
        return 'DayOfWeek'._wrap(super(Date, self).getDayOfWeek())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.libs.datetime.v0.Date(int,int,int)"""
        val = _Date(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getMonth(self) -> 'Month':
        """public dev.ultreon.libs.datetime.v0.Month dev.ultreon.libs.datetime.v0.Date.getMonth()"""
        return 'Month'._wrap(super(Date, self).getMonth())