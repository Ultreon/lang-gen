from __future__ import annotations
from overload import overload


 
import dev.ultreon.libs.datetime.v0.Date as __Date
__Date = __Date
from builtins import str
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
import dev.ultreon.libs.datetime.v0.Month as __Month
__Month = __Month
from builtins import int
 
class Month():
    """dev.ultreon.libs.datetime.v0.Month"""
 
    @staticmethod
    def __wrap(java_value: __Month) -> 'Month':
        return Month(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Month):
        """
        Dynamic initializer for Month.
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
    def values() -> List['Month']:
        """public static dev.ultreon.libs.datetime.v0.Month[] dev.ultreon.libs.datetime.v0.Month.values()"""
        return List[Month].__wrap(__Month.values())

    @overload
    def startDate(self, arg0: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Month.startDate(int)"""
        return 'Date'.__wrap(super(__Month, self).startDate(__int.valueOf(arg0)))

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

    @overload
    def getDays(self, arg0: int) -> int:
        """public int dev.ultreon.libs.datetime.v0.Month.getDays(int)"""
        return int.__wrap(super(__Month, self).getDays(__int.valueOf(arg0)))

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Month':
        """public static dev.ultreon.libs.datetime.v0.Month dev.ultreon.libs.datetime.v0.Month.valueOf(java.lang.String)"""
        return Month.__wrap(__Month.valueOf(arg0))

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

    @staticmethod
    @overload
    def from(arg0: int) -> 'Month':
        """public static dev.ultreon.libs.datetime.v0.Month dev.ultreon.libs.datetime.v0.Month.from(int)"""
        return Month.__wrap(__Month.from(__int.valueOf(arg0)))

    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Month.getIndex()"""
        return int.__wrap(super(Month, self).getIndex())

    @overload
    def endDate(self, arg0: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Month.endDate(int)"""
        return 'Date'.__wrap(super(__Month, self).endDate(__int.valueOf(arg0)))

    @overload
    def asDate(self, arg0: int, arg1: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Month.asDate(int,int)"""
        return 'Date'.__wrap(super(__Month, self).asDate(__int.valueOf(arg0), __int.valueOf(arg1)))

 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.Month
import dev.ultreon.libs.datetime.v0.Date as __Date
__Date = __Date
from builtins import str
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
import dev.ultreon.libs.datetime.v0.Month as __Month
__Month = __Month
from builtins import int
 
class Month():
    """dev.ultreon.libs.datetime.v0.Month"""
 
    @staticmethod
    def __wrap(java_value: __Month) -> 'Month':
        return Month(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Month):
        """
        Dynamic initializer for Month.
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
    def values() -> List['Month']:
        """public static dev.ultreon.libs.datetime.v0.Month[] dev.ultreon.libs.datetime.v0.Month.values()"""
        return List[Month].__wrap(__Month.values())

    @overload
    def startDate(self, arg0: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Month.startDate(int)"""
        return 'Date'.__wrap(super(__Month, self).startDate(__int.valueOf(arg0)))

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

    @overload
    def getDays(self, arg0: int) -> int:
        """public int dev.ultreon.libs.datetime.v0.Month.getDays(int)"""
        return int.__wrap(super(__Month, self).getDays(__int.valueOf(arg0)))

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Month':
        """public static dev.ultreon.libs.datetime.v0.Month dev.ultreon.libs.datetime.v0.Month.valueOf(java.lang.String)"""
        return Month.__wrap(__Month.valueOf(arg0))

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

    @staticmethod
    @overload
    def from(arg0: int) -> 'Month':
        """public static dev.ultreon.libs.datetime.v0.Month dev.ultreon.libs.datetime.v0.Month.from(int)"""
        return Month.__wrap(__Month.from(__int.valueOf(arg0)))

    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Month.getIndex()"""
        return int.__wrap(super(Month, self).getIndex())

    @overload
    def endDate(self, arg0: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Month.endDate(int)"""
        return 'Date'.__wrap(super(__Month, self).endDate(__int.valueOf(arg0)))

    @overload
    def asDate(self, arg0: int, arg1: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Month.asDate(int,int)"""
        return 'Date'.__wrap(super(__Month, self).asDate(__int.valueOf(arg0), __int.valueOf(arg1)))

 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.Month 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.DayPeriod
from builtins import str
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
import dev.ultreon.libs.datetime.v0.Time as __Time
__Time = __Time
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Enum as __Enum
__Enum = __Enum
import dev.ultreon.libs.datetime.v0.DayPeriod as __DayPeriod
__DayPeriod = __DayPeriod
from builtins import int
 
class DayPeriod():
    """dev.ultreon.libs.datetime.v0.DayPeriod"""
 
    @staticmethod
    def __wrap(java_value: __DayPeriod) -> 'DayPeriod':
        return DayPeriod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DayPeriod):
        """
        Dynamic initializer for DayPeriod.
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
    def getStart(self) -> 'Time':
        """public dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.DayPeriod.getStart()"""
        return 'Time'.__wrap(super(DayPeriod, self).getStart())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @overload
    def getEnd(self) -> 'Time':
        """public dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.DayPeriod.getEnd()"""
        return 'Time'.__wrap(super(DayPeriod, self).getEnd())

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

    @overload
    def isWithin(self, arg0: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.DayPeriod.isWithin(dev.ultreon.libs.datetime.v0.Time)"""
        return bool.__wrap(super(__DayPeriod, self).isWithin(arg0))

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
    def values() -> List['DayPeriod']:
        """public static dev.ultreon.libs.datetime.v0.DayPeriod[] dev.ultreon.libs.datetime.v0.DayPeriod.values()"""
        return List[DayPeriod].__wrap(__DayPeriod.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'DayPeriod':
        """public static dev.ultreon.libs.datetime.v0.DayPeriod dev.ultreon.libs.datetime.v0.DayPeriod.valueOf(java.lang.String)"""
        return DayPeriod.__wrap(__DayPeriod.valueOf(arg0))

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
 
 
# CLASS: dev.ultreon.libs.datetime.v0.Duration
from builtins import str
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.math.BigInteger as BigInteger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.datetime.v0.Duration as __Duration
__Duration = __Duration
import java.math.BigDecimal as BigDecimal
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Duration():
    """dev.ultreon.libs.datetime.v0.Duration"""
 
    @staticmethod
    def __wrap(java_value: __Duration) -> 'Duration':
        return Duration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Duration):
        """
        Dynamic initializer for Duration.
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
    def getYears(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getYears()"""
        return float.__wrap(super(Duration, self).getYears())

    @staticmethod
    @overload
    def ofHours(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofHours(double)"""
        return Duration.__wrap(__Duration.ofHours(__double.valueOf(arg0)))

    @overload
    def getYoctosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getYoctosecondPart()"""
        return int.__wrap(super(Duration, self).getYoctosecondPart())

    @overload
    def minus(self, arg0: 'Duration') -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.minus(dev.ultreon.libs.datetime.v0.Duration)"""
        return 'Duration'.__wrap(super(__Duration, self).minus(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.equals(java.lang.Object)"""
        return bool.__wrap(super(__Duration, self).equals(arg0))

    @overload
    def toBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.libs.datetime.v0.Duration.toBigInteger()"""
        return __transform(super(Duration, self).toBigInteger()).'BigInteger'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compareTo(self, arg0: 'Duration') -> int:
        """public int dev.ultreon.libs.datetime.v0.Duration.compareTo(dev.ultreon.libs.datetime.v0.Duration)"""
        return int.__wrap(super(__Duration, self).compareTo(arg0))

    @staticmethod
    @overload
    def ofYoctoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofYoctoseconds(double)"""
        return Duration.__wrap(__Duration.ofYoctoseconds(__double.valueOf(arg0)))

    @overload
    def getWeeks(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getWeeks()"""
        return float.__wrap(super(Duration, self).getWeeks())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.datetime.v0.Duration.toString()"""
        return str.__wrap(super(Duration, self).toString())

    @staticmethod
    @overload
    def ofMilliseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofMilliseconds(double)"""
        return Duration.__wrap(__Duration.ofMilliseconds(__double.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toSeconds(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toSeconds()"""
        return int.__wrap(super(Duration, self).toSeconds())

    @overload
    def getZeptoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getZeptoseconds()"""
        return float.__wrap(super(Duration, self).getZeptoseconds())

    @staticmethod
    @overload
    def ofMinutes(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofMinutes(double)"""
        return Duration.__wrap(__Duration.ofMinutes(__double.valueOf(arg0)))

    @overload
    def getMinutePart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getMinutePart()"""
        return int.__wrap(super(Duration, self).getMinutePart())

    @overload
    def getFemtoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getFemtoseconds()"""
        return float.__wrap(super(Duration, self).getFemtoseconds())

    @staticmethod
    @overload
    def ofSeconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofSeconds(double)"""
        return Duration.__wrap(__Duration.ofSeconds(__double.valueOf(arg0)))

    @overload
    def sleep(self):
        """public void dev.ultreon.libs.datetime.v0.Duration.sleep() throws java.lang.InterruptedException"""
        super(Duration, self).sleep()

    @overload
    def getWeekPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getWeekPart()"""
        return int.__wrap(super(Duration, self).getWeekPart())

    @staticmethod
    @overload
    def ofPicoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofPicoseconds(double)"""
        return Duration.__wrap(__Duration.ofPicoseconds(__double.valueOf(arg0)))

    @overload
    def getAttosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getAttosecondPart()"""
        return int.__wrap(super(Duration, self).getAttosecondPart())

    @overload
    def isZero(self) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.isZero()"""
        return bool.__wrap(super(Duration, self).isZero())

    @overload
    def plus(self, arg0: 'Duration') -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.plus(dev.ultreon.libs.datetime.v0.Duration)"""
        return 'Duration'.__wrap(super(__Duration, self).plus(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def toLong(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toLong()"""
        return int.__wrap(super(Duration, self).toLong())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getPicoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getPicoseconds()"""
        return float.__wrap(super(Duration, self).getPicoseconds())

    @overload
    def getFemtosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getFemtosecondPart()"""
        return int.__wrap(super(Duration, self).getFemtosecondPart())

    @overload
    def getZeptosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getZeptosecondPart()"""
        return int.__wrap(super(Duration, self).getZeptosecondPart())

    @staticmethod
    @overload
    def ofDays(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofDays(double)"""
        return Duration.__wrap(__Duration.ofDays(__double.valueOf(arg0)))

    @overload
    def toMillis(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toMillis()"""
        return int.__wrap(super(Duration, self).toMillis())

    @overload
    def getHours(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getHours()"""
        return float.__wrap(super(Duration, self).getHours())

    @staticmethod
    @overload
    def ofZeptoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofZeptoseconds(double)"""
        return Duration.__wrap(__Duration.ofZeptoseconds(__double.valueOf(arg0)))

    @overload
    def getNanoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getNanoseconds()"""
        return float.__wrap(super(Duration, self).getNanoseconds())

    @overload
    def getMicrosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getMicrosecondPart()"""
        return int.__wrap(super(Duration, self).getMicrosecondPart())

    @overload
    def getHourPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getHourPart()"""
        return int.__wrap(super(Duration, self).getHourPart())

    @staticmethod
    @overload
    def ofNanoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofNanoseconds(double)"""
        return Duration.__wrap(__Duration.ofNanoseconds(__double.valueOf(arg0)))

    @overload
    def getSeconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getSeconds()"""
        return float.__wrap(super(Duration, self).getSeconds())

    @overload
    def toBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal dev.ultreon.libs.datetime.v0.Duration.toBigDecimal()"""
        return __transform(super(Duration, self).toBigDecimal()).'BigDecimal'Value()

    @overload
    def getDays(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getDays()"""
        return float.__wrap(super(Duration, self).getDays())

    @overload
    def toDouble(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.toDouble()"""
        return float.__wrap(super(Duration, self).toDouble())

    @overload
    def toFloat(self) -> float:
        """public float dev.ultreon.libs.datetime.v0.Duration.toFloat()"""
        return float.__wrap(super(Duration, self).toFloat())

    @overload
    def toNanos(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.toNanos()"""
        return int.__wrap(super(Duration, self).toNanos())

    @overload
    def getPicosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getPicosecondPart()"""
        return int.__wrap(super(Duration, self).getPicosecondPart())

    @overload
    def isPositive(self) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.isPositive()"""
        return bool.__wrap(super(Duration, self).isPositive())

    @overload
    def negate(self) -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.negate()"""
        return 'Duration'.__wrap(super(Duration, self).negate())

    @overload
    def getSecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getSecondPart()"""
        return int.__wrap(super(Duration, self).getSecondPart())

    @overload
    def getYoctoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getYoctoseconds()"""
        return float.__wrap(super(Duration, self).getYoctoseconds())

    @overload
    def getMicroseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getMicroseconds()"""
        return float.__wrap(super(Duration, self).getMicroseconds())

    @overload
    def getNanosecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getNanosecondPart()"""
        return int.__wrap(super(Duration, self).getNanosecondPart())

    @staticmethod
    @overload
    def ofWeeks(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofWeeks(double)"""
        return Duration.__wrap(__Duration.ofWeeks(__double.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Duration.hashCode()"""
        return int.__wrap(super(Duration, self).hashCode())

    @overload
    def __init__(self, arg0: float):
        """public dev.ultreon.libs.datetime.v0.Duration(double)"""
        val = __Duration(__double.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def ofAttoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofAttoseconds(double)"""
        return Duration.__wrap(__Duration.ofAttoseconds(__double.valueOf(arg0)))

    @overload
    def getAttoseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getAttoseconds()"""
        return float.__wrap(super(Duration, self).getAttoseconds())

    @overload
    def getMinutes(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getMinutes()"""
        return float.__wrap(super(Duration, self).getMinutes())

    @staticmethod
    @overload
    def ofFemtoseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofFemtoseconds(double)"""
        return Duration.__wrap(__Duration.ofFemtoseconds(__double.valueOf(arg0)))

    @overload
    def isNegative(self) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Duration.isNegative()"""
        return bool.__wrap(super(Duration, self).isNegative())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getMilliseconds(self) -> float:
        """public double dev.ultreon.libs.datetime.v0.Duration.getMilliseconds()"""
        return float.__wrap(super(Duration, self).getMilliseconds())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def toSimpleString(self) -> str:
        """public java.lang.String dev.ultreon.libs.datetime.v0.Duration.toSimpleString()"""
        return str.__wrap(super(Duration, self).toSimpleString())

    @overload
    def getDayPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getDayPart()"""
        return int.__wrap(super(Duration, self).getDayPart())

    @staticmethod
    @overload
    def ofYears(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofYears(double)"""
        return Duration.__wrap(__Duration.ofYears(__double.valueOf(arg0)))

    @overload
    def getMillisecondPart(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Duration.getMillisecondPart()"""
        return int.__wrap(super(Duration, self).getMillisecondPart())

    @overload
    def toInt(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Duration.toInt()"""
        return int.__wrap(super(Duration, self).toInt())

    @overload
    def clone(self) -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.clone()"""
        return 'Duration'.__wrap(super(Duration, self).clone())

    @staticmethod
    @overload
    def ofMicroseconds(arg0: float) -> 'Duration':
        """public static dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.Duration.ofMicroseconds(double)"""
        return Duration.__wrap(__Duration.ofMicroseconds(__double.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.Time
import java.time.Instant as Instant
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.time.LocalTime as LocalTime
from builtins import float
import java.time.ZoneOffset as ZoneOffset
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.datetime.v0.Time as __Time
__Time = __Time
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.libs.datetime.v0.DayPeriod as __DayPeriod
__DayPeriod = __DayPeriod
from builtins import int
 
class Time():
    """dev.ultreon.libs.datetime.v0.Time"""
 
    @staticmethod
    def __wrap(java_value: __Time) -> 'Time':
        return Time(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Time):
        """
        Dynamic initializer for Time.
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
    def ofMillis(arg0: int) -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.ofMillis(long)"""
        return Time.__wrap(__Time.ofMillis(__long.valueOf(arg0)))

    @overload
    def clone(self) -> 'Time':
        """public dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.clone()"""
        return 'Time'.__wrap(super(Time, self).clone())

    @overload
    def toMillis(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Time.toMillis()"""
        return int.__wrap(super(Time, self).toMillis())

    @overload
    def setNano(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Time.setNano(int)"""
        super(__Time, self).setNano(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public dev.ultreon.libs.datetime.v0.Time(int,int,int,int)"""
        val = __Time(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def ofSeconds(arg0: int) -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.ofSeconds(long)"""
        return Time.__wrap(__Time.ofSeconds(__long.valueOf(arg0)))

    @overload
    def compareTo(self, arg0: 'Time') -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.compareTo(dev.ultreon.libs.datetime.v0.Time)"""
        return int.__wrap(super(__Time, self).compareTo(arg0))

    @overload
    def setMinute(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Time.setMinute(int)"""
        super(__Time, self).setMinute(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isBefore(self, arg0: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.isBefore(dev.ultreon.libs.datetime.v0.Time)"""
        return bool.__wrap(super(__Time, self).isBefore(arg0))

    @overload
    def getDayPeriod(self) -> 'DayPeriod':
        """public dev.ultreon.libs.datetime.v0.DayPeriod dev.ultreon.libs.datetime.v0.Time.getDayPeriod()"""
        return 'DayPeriod'.__wrap(super(Time, self).getDayPeriod())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.libs.datetime.v0.Time(int,int,int)"""
        val = __Time(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toMinutes(self) -> float:
        """public float dev.ultreon.libs.datetime.v0.Time.toMinutes()"""
        return float.__wrap(super(Time, self).toMinutes())

    @overload
    def isBetween(self, arg0: 'Time', arg1: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.isBetween(dev.ultreon.libs.datetime.v0.Time,dev.ultreon.libs.datetime.v0.Time)"""
        return bool.__wrap(super(__Time, self).isBetween(arg0, arg1))

    @staticmethod
    @overload
    def ofInstant(arg0: 'Instant', arg1: 'ZoneOffset') -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.ofInstant(java.time.Instant,java.time.ZoneOffset)"""
        return Time.__wrap(__Time.ofInstant(arg0, arg1))

    @overload
    def isAfter(self, arg0: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.isAfter(dev.ultreon.libs.datetime.v0.Time)"""
        return bool.__wrap(super(__Time, self).isAfter(arg0))

    @overload
    def getHour(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.getHour()"""
        return int.__wrap(super(Time, self).getHour())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.hashCode()"""
        return int.__wrap(super(Time, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toHours(self) -> float:
        """public float dev.ultreon.libs.datetime.v0.Time.toHours()"""
        return float.__wrap(super(Time, self).toHours())

    @overload
    def setSecond(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Time.setSecond(int)"""
        super(__Time, self).setSecond(__int.valueOf(arg0))

    @overload
    def toNanos(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Time.toNanos()"""
        return int.__wrap(super(Time, self).toNanos())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def ofNanos(arg0: int) -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.ofNanos(long)"""
        return Time.__wrap(__Time.ofNanos(__long.valueOf(arg0)))

    @overload
    def setHour(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Time.setHour(int)"""
        super(__Time, self).setHour(__int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def current() -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.current()"""
        return Time.__wrap(__Time.current())

    @staticmethod
    @overload
    def ofLocalTime(arg0: 'LocalTime') -> 'Time':
        """public static dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.Time.ofLocalTime(java.time.LocalTime)"""
        return Time.__wrap(__Time.ofLocalTime(arg0))

    @overload
    def getNano(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.getNano()"""
        return int.__wrap(super(Time, self).getNano())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.equals(java.lang.Object)"""
        return bool.__wrap(super(__Time, self).equals(arg0))

    @overload
    def getSecond(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.getSecond()"""
        return int.__wrap(super(Time, self).getSecond())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isBeforeOrEqual(self, arg0: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.isBeforeOrEqual(dev.ultreon.libs.datetime.v0.Time)"""
        return bool.__wrap(super(__Time, self).isBeforeOrEqual(arg0))

    @overload
    def getMinute(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.getMinute()"""
        return int.__wrap(super(Time, self).getMinute())

    @overload
    def toSeconds(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Time.toSeconds()"""
        return int.__wrap(super(Time, self).toSeconds())

    @overload
    def isAfterOrEqual(self, arg0: 'Time') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Time.isAfterOrEqual(dev.ultreon.libs.datetime.v0.Time)"""
        return bool.__wrap(super(__Time, self).isAfterOrEqual(arg0)) 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.Date
import java.time.Instant as Instant
import dev.ultreon.libs.datetime.v0.Date as __Date
__Date = __Date
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.time.chrono.Era as __Era
__Era = __Era
import java.time.chrono.Era as Era
import java.time.ZoneOffset as ZoneOffset
import java.lang.Long as __long
import java.time.chrono.IsoChronology as __IsoChronology
__IsoChronology = __IsoChronology
import java.time.DayOfWeek as __DayOfWeek
__DayOfWeek = __DayOfWeek
import java.time.LocalDate as LocalDate
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.time.DayOfWeek as DayOfWeek
import dev.ultreon.libs.datetime.v0.MeteorologicalSeason as __MeteorologicalSeason
__MeteorologicalSeason = __MeteorologicalSeason
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.libs.datetime.v0.Month as __Month
__Month = __Month
import java.time.chrono.IsoChronology as IsoChronology
import dev.ultreon.libs.datetime.v0.TimeSpan as __TimeSpan
__TimeSpan = __TimeSpan
from builtins import int
 
class Date():
    """dev.ultreon.libs.datetime.v0.Date"""
 
    @staticmethod
    def __wrap(java_value: __Date) -> 'Date':
        return Date(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Date):
        """
        Dynamic initializer for Date.
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
    def compareTo(self, arg0: 'Date') -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.compareTo(dev.ultreon.libs.datetime.v0.Date)"""
        return int.__wrap(super(__Date, self).compareTo(arg0))

    @overload
    def setMonthIndex(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Date.setMonthIndex(int)"""
        super(__Date, self).setMonthIndex(__int.valueOf(arg0))

    @overload
    def getDayOfWeek(self) -> 'DayOfWeek':
        """public java.time.DayOfWeek dev.ultreon.libs.datetime.v0.Date.getDayOfWeek()"""
        return 'DayOfWeek'.__wrap(super(Date, self).getDayOfWeek())

    @staticmethod
    @overload
    def ofLocalDate(arg0: 'LocalDate') -> 'Date':
        """public static dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.ofLocalDate(java.time.LocalDate)"""
        return Date.__wrap(__Date.ofLocalDate(arg0))

    @overload
    def setMonth(self, arg0: 'Month'):
        """public void dev.ultreon.libs.datetime.v0.Date.setMonth(dev.ultreon.libs.datetime.v0.Month)"""
        super(__Date, self).setMonth(arg0)

    @overload
    def toEpochMilli(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Date.toEpochMilli()"""
        return int.__wrap(super(Date, self).toEpochMilli())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def current() -> 'Date':
        """public static dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.current()"""
        return Date.__wrap(__Date.current())

    @staticmethod
    @overload
    def ofEpochSecond(arg0: int) -> 'Date':
        """public static dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.ofEpochSecond(long)"""
        return Date.__wrap(__Date.ofEpochSecond(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ofInstant(arg0: 'Instant', arg1: 'ZoneOffset') -> 'Date':
        """public static dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.ofInstant(java.time.Instant,java.time.ZoneOffset)"""
        return Date.__wrap(__Date.ofInstant(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getSeason(self) -> 'MeteorologicalSeason':
        """public dev.ultreon.libs.datetime.v0.MeteorologicalSeason dev.ultreon.libs.datetime.v0.Date.getSeason()"""
        return 'MeteorologicalSeason'.__wrap(super(Date, self).getSeason())

    @overload
    def __init__(self, arg0: int, arg1: 'Month', arg2: int):
        """public dev.ultreon.libs.datetime.v0.Date(int,dev.ultreon.libs.datetime.v0.Month,int)"""
        val = __Date(__int.valueOf(arg0), arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toEpochDay(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Date.toEpochDay()"""
        return int.__wrap(super(Date, self).toEpochDay())

    @staticmethod
    @overload
    def ofEpochDay(arg0: int) -> 'Date':
        """public static dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.ofEpochDay(long)"""
        return Date.__wrap(__Date.ofEpochDay(__long.valueOf(arg0)))

    @overload
    def getDay(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.getDay()"""
        return int.__wrap(super(Date, self).getDay())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Date.equals(java.lang.Object)"""
        return bool.__wrap(super(__Date, self).equals(arg0))

    @overload
    def clone(self) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.Date.clone()"""
        return 'Date'.__wrap(super(Date, self).clone())

    @overload
    def getChronology(self) -> 'IsoChronology':
        """public java.time.chrono.IsoChronology dev.ultreon.libs.datetime.v0.Date.getChronology()"""
        return 'IsoChronology'.__wrap(super(Date, self).getChronology())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getYear(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.getYear()"""
        return int.__wrap(super(Date, self).getYear())

    @overload
    def isLeapYear(self) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Date.isLeapYear()"""
        return bool.__wrap(super(Date, self).isLeapYear())

    @overload
    def equalsIgnoreYear(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.Date.equalsIgnoreYear(java.lang.Object)"""
        return bool.__wrap(super(__Date, self).equalsIgnoreYear(arg0))

    @overload
    def getMonthIndex(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.getMonthIndex()"""
        return int.__wrap(super(Date, self).getMonthIndex())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setDay(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Date.setDay(int)"""
        super(__Date, self).setDay(__int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getDayOfYear(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.getDayOfYear()"""
        return int.__wrap(super(Date, self).getDayOfYear())

    @overload
    def setYear(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.Date.setYear(int)"""
        super(__Date, self).setYear(__int.valueOf(arg0))

    @overload
    def getEra(self) -> 'Era':
        """public java.time.chrono.Era dev.ultreon.libs.datetime.v0.Date.getEra()"""
        return 'Era'.__wrap(super(Date, self).getEra())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.libs.datetime.v0.Date(int,int,int)"""
        val = __Date(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMonth(self) -> 'Month':
        """public dev.ultreon.libs.datetime.v0.Month dev.ultreon.libs.datetime.v0.Date.getMonth()"""
        return 'Month'.__wrap(super(Date, self).getMonth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.Date.hashCode()"""
        return int.__wrap(super(Date, self).hashCode())

    @staticmethod
    @overload
    def isBetween(arg0: 'Date', arg1: 'Date') -> bool:
        """public static boolean dev.ultreon.libs.datetime.v0.Date.isBetween(dev.ultreon.libs.datetime.v0.Date,dev.ultreon.libs.datetime.v0.Date)"""
        return bool.__wrap(__Date.isBetween(arg0, arg1))

    @overload
    def toTimeSpan(self) -> 'TimeSpan':
        """public dev.ultreon.libs.datetime.v0.TimeSpan dev.ultreon.libs.datetime.v0.Date.toTimeSpan()"""
        return 'TimeSpan'.__wrap(super(Date, self).toTimeSpan())

    @overload
    def toEpochSecond(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.Date.toEpochSecond()"""
        return int.__wrap(super(Date, self).toEpochSecond()) 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.TimeSpan
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.datetime.v0.DateTime as __DateTime
__DateTime = __DateTime
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.libs.datetime.v0.Duration as __Duration
__Duration = __Duration
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.libs.datetime.v0.TimeSpan as __TimeSpan
__TimeSpan = __TimeSpan
from builtins import int
 
class TimeSpan():
    """dev.ultreon.libs.datetime.v0.TimeSpan"""
 
    @staticmethod
    def __wrap(java_value: __TimeSpan) -> 'TimeSpan':
        return TimeSpan(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TimeSpan):
        """
        Dynamic initializer for TimeSpan.
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

    @overload
    def toDuration(self) -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.TimeSpan.toDuration()"""
        return 'Duration'.__wrap(super(TimeSpan, self).toDuration())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def clone(self) -> 'TimeSpan':
        """public dev.ultreon.libs.datetime.v0.TimeSpan dev.ultreon.libs.datetime.v0.TimeSpan.clone()"""
        return 'TimeSpan'.__wrap(super(TimeSpan, self).clone())

    @overload
    def getTo(self) -> 'DateTime':
        """public dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.TimeSpan.getTo()"""
        return 'DateTime'.__wrap(super(TimeSpan, self).getTo())

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
    def getFrom(self) -> 'DateTime':
        """public dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.TimeSpan.getFrom()"""
        return 'DateTime'.__wrap(super(TimeSpan, self).getFrom())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setTo(self, arg0: 'DateTime'):
        """public void dev.ultreon.libs.datetime.v0.TimeSpan.setTo(dev.ultreon.libs.datetime.v0.DateTime)"""
        super(__TimeSpan, self).setTo(arg0)

    @overload
    def contains(self, arg0: 'DateTime') -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.TimeSpan.contains(dev.ultreon.libs.datetime.v0.DateTime)"""
        return bool.__wrap(super(__TimeSpan, self).contains(arg0))

    @overload
    def __init__(self, arg0: 'DateTime', arg1: 'DateTime'):
        """public dev.ultreon.libs.datetime.v0.TimeSpan(dev.ultreon.libs.datetime.v0.DateTime,dev.ultreon.libs.datetime.v0.DateTime)"""
        val = __TimeSpan(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setFrom(self, arg0: 'DateTime'):
        """public void dev.ultreon.libs.datetime.v0.TimeSpan.setFrom(dev.ultreon.libs.datetime.v0.DateTime)"""
        super(__TimeSpan, self).setFrom(arg0) 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.DateTime
import java.time.Instant as Instant
import dev.ultreon.libs.datetime.v0.Date as __Date
__Date = __Date
from builtins import type
import java.time.LocalTime as LocalTime
import java.time.LocalDateTime as __LocalDateTime
__LocalDateTime = __LocalDateTime
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.datetime.v0.DateTime as __DateTime
__DateTime = __DateTime
import dev.ultreon.libs.datetime.v0.Duration as __Duration
__Duration = __Duration
from builtins import bool
import dev.ultreon.libs.datetime.v0.DayPeriod as __DayPeriod
__DayPeriod = __DayPeriod
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.time.LocalDateTime as LocalDateTime
import java.time.LocalDate as __LocalDate
__LocalDate = __LocalDate
import java.time.LocalTime as __LocalTime
__LocalTime = __LocalTime
import java.time.ZoneOffset as ZoneOffset
import java.lang.Long as __long
import java.time.LocalDate as LocalDate
import dev.ultreon.libs.datetime.v0.Time as __Time
__Time = __Time
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.libs.datetime.v0.Month as __Month
__Month = __Month
from builtins import int
 
class DateTime():
    """dev.ultreon.libs.datetime.v0.DateTime"""
 
    @staticmethod
    def __wrap(java_value: __DateTime) -> 'DateTime':
        return DateTime(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DateTime):
        """
        Dynamic initializer for DateTime.
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
    def __init__(self, arg0: 'DateTime'):
        """public dev.ultreon.libs.datetime.v0.DateTime(dev.ultreon.libs.datetime.v0.DateTime)"""
        val = __DateTime(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setSecond(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setSecond(int)"""
        super(__DateTime, self).setSecond(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSecond(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getSecond()"""
        return int.__wrap(super(DateTime, self).getSecond())

    @overload
    def compareTo(self, arg0: 'DateTime') -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.compareTo(dev.ultreon.libs.datetime.v0.DateTime)"""
        return int.__wrap(super(__DateTime, self).compareTo(arg0))

    @overload
    def getDay(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getDay()"""
        return int.__wrap(super(DateTime, self).getDay())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: 'Month', arg2: int, arg3: int, arg4: int, arg5: int):
        """public dev.ultreon.libs.datetime.v0.DateTime(int,dev.ultreon.libs.datetime.v0.Month,int,int,int,int)"""
        val = __DateTime(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTime(self) -> 'Time':
        """public dev.ultreon.libs.datetime.v0.Time dev.ultreon.libs.datetime.v0.DateTime.getTime()"""
        return 'Time'.__wrap(super(DateTime, self).getTime())

    @overload
    def getMonthIndex(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getMonthIndex()"""
        return int.__wrap(super(DateTime, self).getMonthIndex())

    @overload
    def setMonthIndex(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setMonthIndex(int)"""
        super(__DateTime, self).setMonthIndex(__int.valueOf(arg0))

    @staticmethod
    @overload
    def current() -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.current()"""
        return DateTime.__wrap(__DateTime.current())

    @overload
    def setMinute(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setMinute(int)"""
        super(__DateTime, self).setMinute(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def toLocalDate(self) -> 'LocalDate':
        """public java.time.LocalDate dev.ultreon.libs.datetime.v0.DateTime.toLocalDate()"""
        return 'LocalDate'.__wrap(super(DateTime, self).toLocalDate())

    @staticmethod
    @overload
    def ofEpochMilli(arg0: int, arg1: 'ZoneOffset') -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.ofEpochMilli(long,java.time.ZoneOffset)"""
        return DateTime.__wrap(__DateTime.ofEpochMilli(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ofLocalDateTime(arg0: 'LocalDateTime') -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.ofLocalDateTime(java.time.LocalDateTime)"""
        return DateTime.__wrap(__DateTime.ofLocalDateTime(arg0))

    @overload
    def __init__(self, arg0: 'Date', arg1: 'Time'):
        """public dev.ultreon.libs.datetime.v0.DateTime(dev.ultreon.libs.datetime.v0.Date,dev.ultreon.libs.datetime.v0.Time)"""
        val = __DateTime(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getNano(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getNano()"""
        return int.__wrap(super(DateTime, self).getNano())

    @staticmethod
    @overload
    def ofEpochNano(arg0: int, arg1: 'ZoneOffset') -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.ofEpochNano(long,java.time.ZoneOffset)"""
        return DateTime.__wrap(__DateTime.ofEpochNano(__long.valueOf(arg0), arg1))

    @overload
    def getMonth(self) -> 'Month':
        """public dev.ultreon.libs.datetime.v0.Month dev.ultreon.libs.datetime.v0.DateTime.getMonth()"""
        return 'Month'.__wrap(super(DateTime, self).getMonth())

    @overload
    def toEpochNano(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochNano()"""
        return int.__wrap(super(DateTime, self).toEpochNano())

    @overload
    def setYear(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setYear(int)"""
        super(__DateTime, self).setYear(__int.valueOf(arg0))

    @overload
    def getDayPeriod(self) -> 'DayPeriod':
        """public dev.ultreon.libs.datetime.v0.DayPeriod dev.ultreon.libs.datetime.v0.DateTime.getDayPeriod()"""
        return 'DayPeriod'.__wrap(super(DateTime, self).getDayPeriod())

    @overload
    def getYear(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getYear()"""
        return int.__wrap(super(DateTime, self).getYear())

    @overload
    def setNano(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setNano(int)"""
        super(__DateTime, self).setNano(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def toEpochNano(self, arg0: 'ZoneOffset') -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochNano(java.time.ZoneOffset)"""
        return int.__wrap(super(__DateTime, self).toEpochNano(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getDate(self, arg0: 'Date'):
        """public void dev.ultreon.libs.datetime.v0.DateTime.getDate(dev.ultreon.libs.datetime.v0.Date)"""
        super(__DateTime, self).getDate(arg0)

    @staticmethod
    @overload
    def isBetween(arg0: 'DateTime', arg1: 'DateTime') -> bool:
        """public static boolean dev.ultreon.libs.datetime.v0.DateTime.isBetween(dev.ultreon.libs.datetime.v0.DateTime,dev.ultreon.libs.datetime.v0.DateTime)"""
        return bool.__wrap(__DateTime.isBetween(arg0, arg1))

    @overload
    def clone(self) -> 'DateTime':
        """public dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.clone()"""
        return 'DateTime'.__wrap(super(DateTime, self).clone())

    @overload
    def getHour(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getHour()"""
        return int.__wrap(super(DateTime, self).getHour())

    @staticmethod
    @overload
    def isLeapYear(arg0: int) -> bool:
        """public static boolean dev.ultreon.libs.datetime.v0.DateTime.isLeapYear(int)"""
        return bool.__wrap(__DateTime.isLeapYear(__int.valueOf(arg0)))

    @overload
    def setDay(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setDay(int)"""
        super(__DateTime, self).setDay(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public dev.ultreon.libs.datetime.v0.DateTime(int,int,int,int,int,int,int)"""
        val = __DateTime(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setTime(self, arg0: 'Time'):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setTime(dev.ultreon.libs.datetime.v0.Time)"""
        super(__DateTime, self).setTime(arg0)

    @overload
    def setMonth(self, arg0: 'Month'):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setMonth(dev.ultreon.libs.datetime.v0.Month)"""
        super(__DateTime, self).setMonth(arg0)

    @overload
    def toEpochSecond(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochSecond()"""
        return int.__wrap(super(DateTime, self).toEpochSecond())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.datetime.v0.DateTime.equals(java.lang.Object)"""
        return bool.__wrap(super(__DateTime, self).equals(arg0))

    @overload
    def getMinute(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.getMinute()"""
        return int.__wrap(super(DateTime, self).getMinute())

    @overload
    def toLocalDateTime(self) -> 'LocalDateTime':
        """public java.time.LocalDateTime dev.ultreon.libs.datetime.v0.DateTime.toLocalDateTime()"""
        return 'LocalDateTime'.__wrap(super(DateTime, self).toLocalDateTime())

    @overload
    def getDate(self) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.DateTime.getDate()"""
        return 'Date'.__wrap(super(DateTime, self).getDate())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.datetime.v0.DateTime.hashCode()"""
        return int.__wrap(super(DateTime, self).hashCode())

    @overload
    def toEpochSeconds(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochSeconds()"""
        return int.__wrap(super(DateTime, self).toEpochSeconds())

    @overload
    def toEpochMilli(self) -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochMilli()"""
        return int.__wrap(super(DateTime, self).toEpochMilli())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public dev.ultreon.libs.datetime.v0.DateTime(int,int,int,int,int,int)"""
        val = __DateTime(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'Month', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public dev.ultreon.libs.datetime.v0.DateTime(int,dev.ultreon.libs.datetime.v0.Month,int,int,int,int,int)"""
        val = __DateTime(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def toEpochSecond(self, arg0: 'ZoneOffset') -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochSecond(java.time.ZoneOffset)"""
        return int.__wrap(super(__DateTime, self).toEpochSecond(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def toLocalTime(self) -> 'LocalTime':
        """public java.time.LocalTime dev.ultreon.libs.datetime.v0.DateTime.toLocalTime()"""
        return 'LocalTime'.__wrap(super(DateTime, self).toLocalTime())

    @overload
    def setHour(self, arg0: int):
        """public void dev.ultreon.libs.datetime.v0.DateTime.setHour(int)"""
        super(__DateTime, self).setHour(__int.valueOf(arg0))

    @overload
    def toEpochMilli(self, arg0: 'ZoneOffset') -> int:
        """public long dev.ultreon.libs.datetime.v0.DateTime.toEpochMilli(java.time.ZoneOffset)"""
        return int.__wrap(super(__DateTime, self).toEpochMilli(arg0))

    @overload
    def getDuration(self) -> 'Duration':
        """public dev.ultreon.libs.datetime.v0.Duration dev.ultreon.libs.datetime.v0.DateTime.getDuration()"""
        return 'Duration'.__wrap(super(DateTime, self).getDuration())

    @staticmethod
    @overload
    def ofEpochSecond(arg0: int, arg1: 'ZoneOffset') -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.ofEpochSecond(long,java.time.ZoneOffset)"""
        return DateTime.__wrap(__DateTime.ofEpochSecond(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ofInstant(arg0: 'Instant', arg1: 'ZoneOffset') -> 'DateTime':
        """public static dev.ultreon.libs.datetime.v0.DateTime dev.ultreon.libs.datetime.v0.DateTime.ofInstant(java.time.Instant,java.time.ZoneOffset)"""
        return DateTime.__wrap(__DateTime.ofInstant(arg0, arg1)) 
 
 
# CLASS: dev.ultreon.libs.datetime.v0.MeteorologicalSeason
import dev.ultreon.libs.datetime.v0.Date as __Date
__Date = __Date
from builtins import str
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
import dev.ultreon.libs.datetime.v0.MeteorologicalSeason as __MeteorologicalSeason
__MeteorologicalSeason = __MeteorologicalSeason
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class MeteorologicalSeason():
    """dev.ultreon.libs.datetime.v0.MeteorologicalSeason"""
 
    @staticmethod
    def __wrap(java_value: __MeteorologicalSeason) -> 'MeteorologicalSeason':
        return MeteorologicalSeason(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MeteorologicalSeason):
        """
        Dynamic initializer for MeteorologicalSeason.
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
    def values() -> List['MeteorologicalSeason']:
        """public static dev.ultreon.libs.datetime.v0.MeteorologicalSeason[] dev.ultreon.libs.datetime.v0.MeteorologicalSeason.values()"""
        return List[MeteorologicalSeason].__wrap(__MeteorologicalSeason.values())

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
    def valueOf(arg0: str) -> 'MeteorologicalSeason':
        """public static dev.ultreon.libs.datetime.v0.MeteorologicalSeason dev.ultreon.libs.datetime.v0.MeteorologicalSeason.valueOf(java.lang.String)"""
        return MeteorologicalSeason.__wrap(__MeteorologicalSeason.valueOf(arg0))

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

    @overload
    def getStartDate(self, arg0: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.MeteorologicalSeason.getStartDate(int)"""
        return 'Date'.__wrap(super(__MeteorologicalSeason, self).getStartDate(__int.valueOf(arg0)))

    @overload
    def getEndDate(self, arg0: int) -> 'Date':
        """public dev.ultreon.libs.datetime.v0.Date dev.ultreon.libs.datetime.v0.MeteorologicalSeason.getEndDate(int)"""
        return 'Date'.__wrap(super(__MeteorologicalSeason, self).getEndDate(__int.valueOf(arg0)))

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