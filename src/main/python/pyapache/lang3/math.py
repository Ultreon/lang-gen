from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import org.apache.commons.lang3.math.IEEE754rUtils as __IEEE754rUtils
__IEEE754rUtils = __IEEE754rUtils
import java.lang.Long as __long
import java.lang.Float as __float
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
 
class IEEE754rUtils():
    """org.apache.commons.lang3.math.IEEE754rUtils"""
 
    @staticmethod
    def __wrap(java_value: __IEEE754rUtils) -> 'IEEE754rUtils':
        return IEEE754rUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IEEE754rUtils):
        """
        Dynamic initializer for IEEE754rUtils.
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
    def max(arg0: float, arg1: float, arg2: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.max(float,float,float)"""
        return float.__wrap(__IEEE754rUtils.max(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def max(*arg0: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.max(float...)"""
        return float.__wrap(__IEEE754rUtils.max(arg0))

    @staticmethod
    @overload
    def min(arg0: float, arg1: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.min(double,double)"""
        return float.__wrap(__IEEE754rUtils.min(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def min(arg0: float, arg1: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.min(float,float)"""
        return float.__wrap(__IEEE754rUtils.min(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def max(arg0: float, arg1: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.max(float,float)"""
        return float.__wrap(__IEEE754rUtils.max(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def min(arg0: float, arg1: float, arg2: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.min(float,float,float)"""
        return float.__wrap(__IEEE754rUtils.min(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.math.IEEE754rUtils()"""
        val = __IEEE754rUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def min(arg0: float, arg1: float, arg2: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.min(double,double,double)"""
        return float.__wrap(__IEEE754rUtils.min(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def max(arg0: float, arg1: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.max(double,double)"""
        return float.__wrap(__IEEE754rUtils.max(__double.valueOf(arg0), __double.valueOf(arg1)))

    @staticmethod
    @overload
    def min(*arg0: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.min(double...)"""
        return float.__wrap(__IEEE754rUtils.min(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def max(*arg0: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.max(double...)"""
        return float.__wrap(__IEEE754rUtils.max(arg0))

    @staticmethod
    @overload
    def min(*arg0: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.min(float...)"""
        return float.__wrap(__IEEE754rUtils.min(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def max(arg0: float, arg1: float, arg2: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.max(double,double,double)"""
        return float.__wrap(__IEEE754rUtils.max(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.math.IEEE754rUtils()"""
        val = __IEEE754rUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.math.IEEE754rUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import org.apache.commons.lang3.math.IEEE754rUtils as __IEEE754rUtils
__IEEE754rUtils = __IEEE754rUtils
import java.lang.Long as __long
import java.lang.Float as __float
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
 
class IEEE754rUtils():
    """org.apache.commons.lang3.math.IEEE754rUtils"""
 
    @staticmethod
    def __wrap(java_value: __IEEE754rUtils) -> 'IEEE754rUtils':
        return IEEE754rUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IEEE754rUtils):
        """
        Dynamic initializer for IEEE754rUtils.
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
    def max(arg0: float, arg1: float, arg2: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.max(float,float,float)"""
        return float.__wrap(__IEEE754rUtils.max(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def max(*arg0: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.max(float...)"""
        return float.__wrap(__IEEE754rUtils.max(arg0))

    @staticmethod
    @overload
    def min(arg0: float, arg1: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.min(double,double)"""
        return float.__wrap(__IEEE754rUtils.min(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def min(arg0: float, arg1: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.min(float,float)"""
        return float.__wrap(__IEEE754rUtils.min(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def max(arg0: float, arg1: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.max(float,float)"""
        return float.__wrap(__IEEE754rUtils.max(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def min(arg0: float, arg1: float, arg2: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.min(float,float,float)"""
        return float.__wrap(__IEEE754rUtils.min(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.math.IEEE754rUtils()"""
        val = __IEEE754rUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def min(arg0: float, arg1: float, arg2: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.min(double,double,double)"""
        return float.__wrap(__IEEE754rUtils.min(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def max(arg0: float, arg1: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.max(double,double)"""
        return float.__wrap(__IEEE754rUtils.max(__double.valueOf(arg0), __double.valueOf(arg1)))

    @staticmethod
    @overload
    def min(*arg0: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.min(double...)"""
        return float.__wrap(__IEEE754rUtils.min(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def max(*arg0: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.max(double...)"""
        return float.__wrap(__IEEE754rUtils.max(arg0))

    @staticmethod
    @overload
    def min(*arg0: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.min(float...)"""
        return float.__wrap(__IEEE754rUtils.min(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def max(arg0: float, arg1: float, arg2: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.max(double,double,double)"""
        return float.__wrap(__IEEE754rUtils.max(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.math.IEEE754rUtils()"""
        val = __IEEE754rUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.lang3.math.IEEE754rUtils 
 
 
# CLASS: org.apache.commons.lang3.math.NumberUtils
import java.lang.Long as Long
from builtins import type
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import java.lang.String as __string
import java.lang.Short as __short
import org.apache.commons.lang3.math.NumberUtils as __NumberUtils
__NumberUtils = __NumberUtils
import java.lang.Double as __double
from builtins import bool
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import java.lang.Float as Float
import java.lang.Long as __long
import java.math.BigInteger as BigInteger
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.math.RoundingMode as RoundingMode
import java.math.BigDecimal as BigDecimal
import java.lang.Integer as __int
import java.lang.Double as Double
from builtins import int
 
class NumberUtils():
    """org.apache.commons.lang3.math.NumberUtils"""
 
    @staticmethod
    def __wrap(java_value: __NumberUtils) -> 'NumberUtils':
        return NumberUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NumberUtils):
        """
        Dynamic initializer for NumberUtils.
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
    def min(*arg0: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.min(int...)"""
        return int.__wrap(__NumberUtils.min(arg0))

    @staticmethod
    @overload
    def max(*arg0: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.max(int...)"""
        return int.__wrap(__NumberUtils.max(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.math.NumberUtils()"""
        val = __NumberUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def min(arg0: float, arg1: float, arg2: float) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.min(float,float,float)"""
        return float.__wrap(__NumberUtils.min(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.String,int,java.math.RoundingMode)"""
        return __transform(__arg0, __int.valueOf(arg1), arg2.NumberUtils(arg0: str, arg1: int, arg2: 'RoundingMode')).'BigDecimal'Value()

    @staticmethod
    @overload
    def isCreatable(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.math.NumberUtils.isCreatable(java.lang.String)"""
        return bool.__wrap(__NumberUtils.isCreatable(arg0))

    @staticmethod
    @overload
    def min(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.min(long,long,long)"""
        return int.__wrap(__NumberUtils.min(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def max(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.max(int,int,int)"""
        return int.__wrap(__NumberUtils.max(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def toFloat(arg0: str, arg1: float) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.toFloat(java.lang.String,float)"""
        return float.__wrap(__NumberUtils.toFloat(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def createBigDecimal(createBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.createBigDecimal(java.lang.String)"""
        return __transform(__arg0.NumberUtils(arg0: str)).'BigDecimal'Value()

    @staticmethod
    @overload
    def compare(arg0: int, arg1: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.compare(long,long)"""
        return int.__wrap(__NumberUtils.compare(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def isDigits(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.math.NumberUtils.isDigits(java.lang.String)"""
        return bool.__wrap(__NumberUtils.isDigits(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def toLong(arg0: str) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.toLong(java.lang.String)"""
        return int.__wrap(__NumberUtils.toLong(arg0))

    @staticmethod
    @overload
    def compare(arg0: int, arg1: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.compare(int,int)"""
        return int.__wrap(__NumberUtils.compare(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.math.BigDecimal)"""
        return __transform(__arg0.NumberUtils(arg0: 'BigDecimal')).'BigDecimal'Value()

    @staticmethod
    @overload
    def max(*arg0: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.max(double...)"""
        return float.__wrap(__NumberUtils.max(arg0))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.Float)"""
        return __transform(__arg0.NumberUtils(arg0: 'Float')).'BigDecimal'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.Float,int,java.math.RoundingMode)"""
        return __transform(__arg0, __int.valueOf(arg1), arg2.NumberUtils(arg0: 'Float', arg1: int, arg2: 'RoundingMode')).'BigDecimal'Value()

    @staticmethod
    @overload
    def min(*arg0: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.min(double...)"""
        return float.__wrap(__NumberUtils.min(arg0))

    @staticmethod
    @overload
    def toByte(arg0: str) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.toByte(java.lang.String)"""
        return int.__wrap(__NumberUtils.toByte(arg0))

    @staticmethod
    @overload
    def toShort(arg0: str, arg1: int) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.toShort(java.lang.String,short)"""
        return int.__wrap(__NumberUtils.toShort(arg0, __short.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def createBigInteger(createBigInteger) -> 'BigInteger':
        """public static java.math.BigInteger org.apache.commons.lang3.math.NumberUtils.createBigInteger(java.lang.String)"""
        return __transform(__arg0.NumberUtils(arg0: str)).'BigInteger'Value()

    @staticmethod
    @overload
    def max(arg0: int, arg1: int, arg2: int) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.max(byte,byte,byte)"""
        return int.__wrap(__NumberUtils.max(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2)))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.Double)"""
        return __transform(__arg0.NumberUtils(arg0: 'Double')).'BigDecimal'Value()

    @staticmethod
    @overload
    def max(arg0: float, arg1: float, arg2: float) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.max(float,float,float)"""
        return float.__wrap(__NumberUtils.max(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def max(*arg0: int) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.max(long...)"""
        return int.__wrap(__NumberUtils.max(arg0))

    @staticmethod
    @overload
    def createInteger(createInteger) -> 'Integer':
        """public static java.lang.Integer org.apache.commons.lang3.math.NumberUtils.createInteger(java.lang.String)"""
        return __transform(__arg0.NumberUtils(arg0: str)).'Integer'Value()

    @staticmethod
    @overload
    def createDouble(createDouble) -> 'Double':
        """public static java.lang.Double org.apache.commons.lang3.math.NumberUtils.createDouble(java.lang.String)"""
        return __transform(__arg0.NumberUtils(arg0: str)).'Double'Value()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.math.NumberUtils()"""
        val = __NumberUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def max(arg0: float, arg1: float, arg2: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.max(double,double,double)"""
        return float.__wrap(__NumberUtils.max(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @staticmethod
    @overload
    def toByte(arg0: str, arg1: int) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.toByte(java.lang.String,byte)"""
        return int.__wrap(__NumberUtils.toByte(arg0, __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def createFloat(createFloat) -> 'Float':
        """public static java.lang.Float org.apache.commons.lang3.math.NumberUtils.createFloat(java.lang.String)"""
        return __transform(__arg0.NumberUtils(arg0: str)).'Float'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def compare(arg0: int, arg1: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.compare(short,short)"""
        return int.__wrap(__NumberUtils.compare(__short.valueOf(arg0), __short.valueOf(arg1)))

    @staticmethod
    @overload
    def min(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.min(int,int,int)"""
        return int.__wrap(__NumberUtils.min(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def max(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.max(long,long,long)"""
        return int.__wrap(__NumberUtils.max(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createLong(createLong) -> 'Long':
        """public static java.lang.Long org.apache.commons.lang3.math.NumberUtils.createLong(java.lang.String)"""
        return __transform(__arg0.NumberUtils(arg0: str)).'Long'Value()

    @staticmethod
    @overload
    def min(arg0: int, arg1: int, arg2: int) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.min(short,short,short)"""
        return int.__wrap(__NumberUtils.min(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2)))

    @staticmethod
    @overload
    def createNumber(createNumber) -> 'Number':
        """public static java.lang.Number org.apache.commons.lang3.math.NumberUtils.createNumber(java.lang.String)"""
        return __transform(__arg0.NumberUtils(arg0: str)).'Number'Value()

    @staticmethod
    @overload
    def toDouble(arg0: 'BigDecimal') -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.toDouble(java.math.BigDecimal)"""
        return float.__wrap(__NumberUtils.toDouble(arg0))

    @staticmethod
    @overload
    def toDouble(arg0: str, arg1: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.toDouble(java.lang.String,double)"""
        return float.__wrap(__NumberUtils.toDouble(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def max(arg0: int, arg1: int, arg2: int) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.max(short,short,short)"""
        return int.__wrap(__NumberUtils.max(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2)))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.Double,int,java.math.RoundingMode)"""
        return __transform(__arg0, __int.valueOf(arg1), arg2.NumberUtils(arg0: 'Double', arg1: int, arg2: 'RoundingMode')).'BigDecimal'Value()

    @staticmethod
    @overload
    def isNumber(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.math.NumberUtils.isNumber(java.lang.String)"""
        return bool.__wrap(__NumberUtils.isNumber(arg0))

    @staticmethod
    @overload
    def min(arg0: int, arg1: int, arg2: int) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.min(byte,byte,byte)"""
        return int.__wrap(__NumberUtils.min(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2)))

    @staticmethod
    @overload
    def max(*arg0: int) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.max(byte...)"""
        return int.__wrap(__NumberUtils.max(bytes))

    @staticmethod
    @overload
    def toInt(arg0: str, arg1: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.toInt(java.lang.String,int)"""
        return int.__wrap(__NumberUtils.toInt(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def toLong(arg0: str, arg1: int) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.toLong(java.lang.String,long)"""
        return int.__wrap(__NumberUtils.toLong(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def toInt(arg0: str) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.toInt(java.lang.String)"""
        return int.__wrap(__NumberUtils.toInt(arg0))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.math.BigDecimal,int,java.math.RoundingMode)"""
        return __transform(__arg0, __int.valueOf(arg1), arg2.NumberUtils(arg0: 'BigDecimal', arg1: int, arg2: 'RoundingMode')).'BigDecimal'Value()

    @staticmethod
    @overload
    def max(*arg0: int) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.max(short...)"""
        return int.__wrap(__NumberUtils.max(arg0))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.String)"""
        return __transform(__arg0.NumberUtils(arg0: str)).'BigDecimal'Value()

    @staticmethod
    @overload
    def max(*arg0: float) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.max(float...)"""
        return float.__wrap(__NumberUtils.max(arg0))

    @staticmethod
    @overload
    def toShort(arg0: str) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.toShort(java.lang.String)"""
        return int.__wrap(__NumberUtils.toShort(arg0))

    @staticmethod
    @overload
    def min(arg0: float, arg1: float, arg2: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.min(double,double,double)"""
        return float.__wrap(__NumberUtils.min(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def min(*arg0: int) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.min(short...)"""
        return int.__wrap(__NumberUtils.min(arg0))

    @staticmethod
    @overload
    def min(*arg0: float) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.min(float...)"""
        return float.__wrap(__NumberUtils.min(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toDouble(arg0: 'BigDecimal', arg1: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.toDouble(java.math.BigDecimal,double)"""
        return float.__wrap(__NumberUtils.toDouble(arg0, __double.valueOf(arg1)))

    @staticmethod
    @overload
    def toFloat(arg0: str) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.toFloat(java.lang.String)"""
        return float.__wrap(__NumberUtils.toFloat(arg0))

    @staticmethod
    @overload
    def isParsable(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.math.NumberUtils.isParsable(java.lang.String)"""
        return bool.__wrap(__NumberUtils.isParsable(arg0))

    @staticmethod
    @overload
    def toDouble(arg0: str) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.toDouble(java.lang.String)"""
        return float.__wrap(__NumberUtils.toDouble(arg0))

    @staticmethod
    @overload
    def compare(arg0: int, arg1: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.compare(byte,byte)"""
        return int.__wrap(__NumberUtils.compare(__byte.valueOf(arg0), __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def min(*arg0: int) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.min(byte...)"""
        return int.__wrap(__NumberUtils.min(bytes))

    @staticmethod
    @overload
    def min(*arg0: int) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.min(long...)"""
        return int.__wrap(__NumberUtils.min(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.math.Fraction
from builtins import str
from pyquantum_helper import transform as __transform
import org.apache.commons.lang3.math.Fraction as __Fraction
__Fraction = __Fraction
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
import java.lang.Number as __Number
__Number = __Number
from builtins import int
 
class Fraction():
    """org.apache.commons.lang3.math.Fraction"""
 
    @staticmethod
    def __wrap(java_value: __Fraction) -> 'Fraction':
        return Fraction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Fraction):
        """
        Dynamic initializer for Fraction.
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
    def getProperWhole(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getProperWhole()"""
        return int.__wrap(super(Fraction, self).getProperWhole())

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(int,int,int)"""
        return __transform(____int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2).Fraction(arg0: int, arg1: int, arg2: int)).'Fraction'Value()

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(int,int)"""
        return __transform(____int.valueOf(arg0), __int.valueOf(arg1).Fraction(arg0: int, arg1: int)).'Fraction'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def invert(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.invert()"""
        return __transform(super(Fraction, self).invert()).'Fraction'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.math.Fraction.equals(java.lang.Object)"""
        return bool.__wrap(super(__Fraction, self).equals(arg0))

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.math.Fraction.doubleValue()"""
        return float.__wrap(super(Fraction, self).doubleValue())

    @overload
    def reduce(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.reduce()"""
        return __transform(super(Fraction, self).reduce()).'Fraction'Value()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def negate(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.negate()"""
        return __transform(super(Fraction, self).negate()).'Fraction'Value()

    @overload
    def abs(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.abs()"""
        return __transform(super(Fraction, self).abs()).'Fraction'Value()

    @overload
    def compareTo(self, arg0: 'Fraction') -> int:
        """public int org.apache.commons.lang3.math.Fraction.compareTo(org.apache.commons.lang3.math.Fraction)"""
        return int.__wrap(super(__Fraction, self).compareTo(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.math.Fraction.toString()"""
        return str.__wrap(super(Fraction, self).toString())

    @overload
    def multiplyBy(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.multiplyBy(org.apache.commons.lang3.math.Fraction)"""
        return __transform(super(__Fraction, self).multiplyBy(arg0)).'Fraction'Value()

    @overload
    def toProperString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.math.Fraction.toProperString()"""
        return str.__wrap(super(Fraction, self).toProperString())

    @overload
    def getDenominator(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getDenominator()"""
        return int.__wrap(super(Fraction, self).getDenominator())

    @overload
    def getProperNumerator(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getProperNumerator()"""
        return int.__wrap(super(Fraction, self).getProperNumerator())

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int.__wrap(super(Number, self).shortValue())

    @staticmethod
    @overload
    def getReducedFraction(getReducedFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getReducedFraction(int,int)"""
        return __transform(____int.valueOf(arg0), __int.valueOf(arg1).Fraction(arg0: int, arg1: int)).'Fraction'Value()

    @overload
    def pow(self, arg0: int) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.pow(int)"""
        return __transform(super(__Fraction, self).pow(__int.valueOf(arg0))).'Fraction'Value()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int.__wrap(super(Number, self).byteValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.intValue()"""
        return int.__wrap(super(Fraction, self).intValue())

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(java.lang.String)"""
        return __transform(__arg0.Fraction(arg0: str)).'Fraction'Value()

    @overload
    def getNumerator(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getNumerator()"""
        return int.__wrap(super(Fraction, self).getNumerator())

    @overload
    def add(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.add(org.apache.commons.lang3.math.Fraction)"""
        return __transform(super(__Fraction, self).add(arg0)).'Fraction'Value()

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.math.Fraction.longValue()"""
        return int.__wrap(super(Fraction, self).longValue())

    @overload
    def subtract(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.subtract(org.apache.commons.lang3.math.Fraction)"""
        return __transform(super(__Fraction, self).subtract(arg0)).'Fraction'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(double)"""
        return __transform(____double.valueOf(arg0).Fraction(arg0: float)).'Fraction'Value()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.hashCode()"""
        return int.__wrap(super(Fraction, self).hashCode())

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.math.Fraction.floatValue()"""
        return float.__wrap(super(Fraction, self).floatValue())

    @overload
    def divideBy(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.divideBy(org.apache.commons.lang3.math.Fraction)"""
        return __transform(super(__Fraction, self).divideBy(arg0)).'Fraction'Value()