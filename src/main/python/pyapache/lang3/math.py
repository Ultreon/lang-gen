from __future__ import annotations
from overload import overload


 
import org.apache.commons.lang3.math.Fraction as _Fraction
_Fraction = _Fraction
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Fraction():
    """org.apache.commons.lang3.math.Fraction"""
 
    @staticmethod
    def _wrap(java_value: _Fraction) -> 'Fraction':
        return Fraction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Fraction):
        """
        Dynamic initializer for Fraction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Fraction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Fraction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.math.Fraction.toString()"""
        return str._wrap(super(Fraction, self).toString())

    @overload
    def add(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.add(org.apache.commons.lang3.math.Fraction)"""
        return _transform(super(_Fraction, self).add(arg0)).'Fraction'Value()

    @overload
    def multiplyBy(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.multiplyBy(org.apache.commons.lang3.math.Fraction)"""
        return _transform(super(_Fraction, self).multiplyBy(arg0)).'Fraction'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getProperNumerator(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getProperNumerator()"""
        return int._wrap(super(Fraction, self).getProperNumerator())

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

    @overload
    def abs(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.abs()"""
        return _transform(super(Fraction, self).abs()).'Fraction'Value()

    @overload
    def invert(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.invert()"""
        return _transform(super(Fraction, self).invert()).'Fraction'Value()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getDenominator(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getDenominator()"""
        return int._wrap(super(Fraction, self).getDenominator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toProperString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.math.Fraction.toProperString()"""
        return str._wrap(super(Fraction, self).toProperString())

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int._wrap(super(Number, self).shortValue())

    @overload
    def compareTo(self, arg0: 'Fraction') -> int:
        """public int org.apache.commons.lang3.math.Fraction.compareTo(org.apache.commons.lang3.math.Fraction)"""
        return int._wrap(super(_Fraction, self).compareTo(arg0))

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(int,int)"""
        return _transform(__int.valueOf(arg0), _int.valueOf(arg1).Fraction(arg0: int, arg1: int)).'Fraction'Value()

    @overload
    def subtract(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.subtract(org.apache.commons.lang3.math.Fraction)"""
        return _transform(super(_Fraction, self).subtract(arg0)).'Fraction'Value()

    @overload
    def pow(self, arg0: int) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.pow(int)"""
        return _transform(super(_Fraction, self).pow(_int.valueOf(arg0))).'Fraction'Value()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.math.Fraction.longValue()"""
        return int._wrap(super(Fraction, self).longValue())

    @overload
    def negate(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.negate()"""
        return _transform(super(Fraction, self).negate()).'Fraction'Value()

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(int,int,int)"""
        return _transform(__int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2).Fraction(arg0: int, arg1: int, arg2: int)).'Fraction'Value()

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(java.lang.String)"""
        return _transform(_arg0.Fraction(arg0: str)).'Fraction'Value()

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.math.Fraction.doubleValue()"""
        return float._wrap(super(Fraction, self).doubleValue())

    @staticmethod
    @overload
    def getReducedFraction(getReducedFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getReducedFraction(int,int)"""
        return _transform(__int.valueOf(arg0), _int.valueOf(arg1).Fraction(arg0: int, arg1: int)).'Fraction'Value()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.hashCode()"""
        return int._wrap(super(Fraction, self).hashCode())

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(double)"""
        return _transform(__double.valueOf(arg0).Fraction(arg0: float)).'Fraction'Value()

    @overload
    def getNumerator(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getNumerator()"""
        return int._wrap(super(Fraction, self).getNumerator())

    @overload
    def reduce(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.reduce()"""
        return _transform(super(Fraction, self).reduce()).'Fraction'Value()

    @overload
    def divideBy(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.divideBy(org.apache.commons.lang3.math.Fraction)"""
        return _transform(super(_Fraction, self).divideBy(arg0)).'Fraction'Value()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.math.Fraction.floatValue()"""
        return float._wrap(super(Fraction, self).floatValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.math.Fraction.equals(java.lang.Object)"""
        return bool._wrap(super(_Fraction, self).equals(arg0))

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.intValue()"""
        return int._wrap(super(Fraction, self).intValue())

    @overload
    def getProperWhole(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getProperWhole()"""
        return int._wrap(super(Fraction, self).getProperWhole())

 
 
 
# CLASS: org.apache.commons.lang3.math.Fraction
import org.apache.commons.lang3.math.Fraction as _Fraction
_Fraction = _Fraction
from builtins import str
from pyquantum_helper import transform as _transform
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Number as _Number
_Number = _Number
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Fraction():
    """org.apache.commons.lang3.math.Fraction"""
 
    @staticmethod
    def _wrap(java_value: _Fraction) -> 'Fraction':
        return Fraction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Fraction):
        """
        Dynamic initializer for Fraction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Fraction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Fraction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.math.Fraction.toString()"""
        return str._wrap(super(Fraction, self).toString())

    @overload
    def add(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.add(org.apache.commons.lang3.math.Fraction)"""
        return _transform(super(_Fraction, self).add(arg0)).'Fraction'Value()

    @overload
    def multiplyBy(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.multiplyBy(org.apache.commons.lang3.math.Fraction)"""
        return _transform(super(_Fraction, self).multiplyBy(arg0)).'Fraction'Value()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getProperNumerator(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getProperNumerator()"""
        return int._wrap(super(Fraction, self).getProperNumerator())

    @override
    @overload
    def byteValue(self) -> int:
        """public byte java.lang.Number.byteValue()"""
        return int._wrap(super(Number, self).byteValue())

    @overload
    def abs(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.abs()"""
        return _transform(super(Fraction, self).abs()).'Fraction'Value()

    @overload
    def invert(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.invert()"""
        return _transform(super(Fraction, self).invert()).'Fraction'Value()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getDenominator(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getDenominator()"""
        return int._wrap(super(Fraction, self).getDenominator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toProperString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.math.Fraction.toProperString()"""
        return str._wrap(super(Fraction, self).toProperString())

    @override
    @overload
    def shortValue(self) -> int:
        """public short java.lang.Number.shortValue()"""
        return int._wrap(super(Number, self).shortValue())

    @overload
    def compareTo(self, arg0: 'Fraction') -> int:
        """public int org.apache.commons.lang3.math.Fraction.compareTo(org.apache.commons.lang3.math.Fraction)"""
        return int._wrap(super(_Fraction, self).compareTo(arg0))

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(int,int)"""
        return _transform(__int.valueOf(arg0), _int.valueOf(arg1).Fraction(arg0: int, arg1: int)).'Fraction'Value()

    @overload
    def subtract(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.subtract(org.apache.commons.lang3.math.Fraction)"""
        return _transform(super(_Fraction, self).subtract(arg0)).'Fraction'Value()

    @overload
    def pow(self, arg0: int) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.pow(int)"""
        return _transform(super(_Fraction, self).pow(_int.valueOf(arg0))).'Fraction'Value()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def longValue(self) -> int:
        """public long org.apache.commons.lang3.math.Fraction.longValue()"""
        return int._wrap(super(Fraction, self).longValue())

    @overload
    def negate(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.negate()"""
        return _transform(super(Fraction, self).negate()).'Fraction'Value()

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(int,int,int)"""
        return _transform(__int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2).Fraction(arg0: int, arg1: int, arg2: int)).'Fraction'Value()

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(java.lang.String)"""
        return _transform(_arg0.Fraction(arg0: str)).'Fraction'Value()

    @override
    @overload
    def doubleValue(self) -> float:
        """public double org.apache.commons.lang3.math.Fraction.doubleValue()"""
        return float._wrap(super(Fraction, self).doubleValue())

    @staticmethod
    @overload
    def getReducedFraction(getReducedFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getReducedFraction(int,int)"""
        return _transform(__int.valueOf(arg0), _int.valueOf(arg1).Fraction(arg0: int, arg1: int)).'Fraction'Value()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.hashCode()"""
        return int._wrap(super(Fraction, self).hashCode())

    @staticmethod
    @overload
    def getFraction(getFraction) -> 'Fraction':
        """public static org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.getFraction(double)"""
        return _transform(__double.valueOf(arg0).Fraction(arg0: float)).'Fraction'Value()

    @overload
    def getNumerator(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getNumerator()"""
        return int._wrap(super(Fraction, self).getNumerator())

    @overload
    def reduce(self) -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.reduce()"""
        return _transform(super(Fraction, self).reduce()).'Fraction'Value()

    @overload
    def divideBy(self, arg0: 'Fraction') -> 'Fraction':
        """public org.apache.commons.lang3.math.Fraction org.apache.commons.lang3.math.Fraction.divideBy(org.apache.commons.lang3.math.Fraction)"""
        return _transform(super(_Fraction, self).divideBy(arg0)).'Fraction'Value()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def floatValue(self) -> float:
        """public float org.apache.commons.lang3.math.Fraction.floatValue()"""
        return float._wrap(super(Fraction, self).floatValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.math.Fraction.equals(java.lang.Object)"""
        return bool._wrap(super(_Fraction, self).equals(arg0))

    @override
    @overload
    def intValue(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.intValue()"""
        return int._wrap(super(Fraction, self).intValue())

    @overload
    def getProperWhole(self) -> int:
        """public int org.apache.commons.lang3.math.Fraction.getProperWhole()"""
        return int._wrap(super(Fraction, self).getProperWhole())

 
 
 
# CLASS: org.apache.commons.lang3.math.Fraction 
 
 
# CLASS: org.apache.commons.lang3.math.IEEE754rUtils
from builtins import str
import java.lang.Double as _double
import org.apache.commons.lang3.math.IEEE754rUtils as _IEEE754rUtils
_IEEE754rUtils = _IEEE754rUtils
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IEEE754rUtils():
    """org.apache.commons.lang3.math.IEEE754rUtils"""
 
    @staticmethod
    def _wrap(java_value: _IEEE754rUtils) -> 'IEEE754rUtils':
        return IEEE754rUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IEEE754rUtils):
        """
        Dynamic initializer for IEEE754rUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IEEE754rUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IEEE754rUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def min(*arg0: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.min(float...)"""
        return float._wrap(_IEEE754rUtils.min(arg0))

    @staticmethod
    @overload
    def max(*arg0: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.max(float...)"""
        return float._wrap(_IEEE754rUtils.max(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.math.IEEE754rUtils()"""
        val = _IEEE754rUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def max(arg0: float, arg1: float, arg2: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.max(double,double,double)"""
        return float._wrap(_IEEE754rUtils.max(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.math.IEEE754rUtils()"""
        val = _IEEE754rUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def min(arg0: float, arg1: float, arg2: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.min(float,float,float)"""
        return float._wrap(_IEEE754rUtils.min(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def min(arg0: float, arg1: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.min(float,float)"""
        return float._wrap(_IEEE754rUtils.min(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def max(*arg0: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.max(double...)"""
        return float._wrap(_IEEE754rUtils.max(arg0))

    @staticmethod
    @overload
    def min(arg0: float, arg1: float, arg2: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.min(double,double,double)"""
        return float._wrap(_IEEE754rUtils.min(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def max(arg0: float, arg1: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.max(float,float)"""
        return float._wrap(_IEEE754rUtils.max(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def min(*arg0: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.min(double...)"""
        return float._wrap(_IEEE754rUtils.min(arg0))

    @staticmethod
    @overload
    def max(arg0: float, arg1: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.max(double,double)"""
        return float._wrap(_IEEE754rUtils.max(_double.valueOf(arg0), _double.valueOf(arg1)))

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

    @staticmethod
    @overload
    def min(arg0: float, arg1: float) -> float:
        """public static double org.apache.commons.lang3.math.IEEE754rUtils.min(double,double)"""
        return float._wrap(_IEEE754rUtils.min(_double.valueOf(arg0), _double.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def max(arg0: float, arg1: float, arg2: float) -> float:
        """public static float org.apache.commons.lang3.math.IEEE754rUtils.max(float,float,float)"""
        return float._wrap(_IEEE754rUtils.max(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.math.NumberUtils
import java.lang.Double as _double
import java.lang.Long as Long
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.lang3.math.NumberUtils as _NumberUtils
_NumberUtils = _NumberUtils
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Byte as _byte
from builtins import bool
from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.Float as Float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import java.lang.Integer as Integer
import java.math.RoundingMode as RoundingMode
import java.math.BigDecimal as BigDecimal
import java.lang.Long as _long
import java.lang.Double as Double
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NumberUtils():
    """org.apache.commons.lang3.math.NumberUtils"""
 
    @staticmethod
    def _wrap(java_value: _NumberUtils) -> 'NumberUtils':
        return NumberUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NumberUtils):
        """
        Dynamic initializer for NumberUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NumberUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NumberUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.math.NumberUtils()"""
        val = _NumberUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def toDouble(arg0: str) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.toDouble(java.lang.String)"""
        return float._wrap(_NumberUtils.toDouble(arg0))

    @staticmethod
    @overload
    def max(arg0: int, arg1: int, arg2: int) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.max(short,short,short)"""
        return int._wrap(_NumberUtils.max(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2)))

    @staticmethod
    @overload
    def createInteger(createInteger) -> 'Integer':
        """public static java.lang.Integer org.apache.commons.lang3.math.NumberUtils.createInteger(java.lang.String)"""
        return _transform(_arg0.NumberUtils(arg0: str)).'Integer'Value()

    @staticmethod
    @overload
    def max(arg0: int, arg1: int, arg2: int) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.max(byte,byte,byte)"""
        return int._wrap(_NumberUtils.max(_byte.valueOf(arg0), _byte.valueOf(arg1), _byte.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def isNumber(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.math.NumberUtils.isNumber(java.lang.String)"""
        return bool._wrap(_NumberUtils.isNumber(arg0))

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
    def toFloat(arg0: str) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.toFloat(java.lang.String)"""
        return float._wrap(_NumberUtils.toFloat(arg0))

    @staticmethod
    @overload
    def max(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.max(long,long,long)"""
        return int._wrap(_NumberUtils.max(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def toByte(arg0: str, arg1: int) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.toByte(java.lang.String,byte)"""
        return int._wrap(_NumberUtils.toByte(arg0, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def createBigDecimal(createBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.createBigDecimal(java.lang.String)"""
        return _transform(_arg0.NumberUtils(arg0: str)).'BigDecimal'Value()

    @staticmethod
    @overload
    def min(*arg0: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.min(double...)"""
        return float._wrap(_NumberUtils.min(arg0))

    @staticmethod
    @overload
    def max(*arg0: float) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.max(float...)"""
        return float._wrap(_NumberUtils.max(arg0))

    @staticmethod
    @overload
    def compare(arg0: int, arg1: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.compare(byte,byte)"""
        return int._wrap(_NumberUtils.compare(_byte.valueOf(arg0), _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.Double,int,java.math.RoundingMode)"""
        return _transform(_arg0, _int.valueOf(arg1), arg2.NumberUtils(arg0: 'Double', arg1: int, arg2: 'RoundingMode')).'BigDecimal'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def min(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.min(long,long,long)"""
        return int._wrap(_NumberUtils.min(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2)))

    @staticmethod
    @overload
    def min(arg0: int, arg1: int, arg2: int) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.min(short,short,short)"""
        return int._wrap(_NumberUtils.min(_short.valueOf(arg0), _short.valueOf(arg1), _short.valueOf(arg2)))

    @staticmethod
    @overload
    def compare(arg0: int, arg1: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.compare(int,int)"""
        return int._wrap(_NumberUtils.compare(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def max(*arg0: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.max(double...)"""
        return float._wrap(_NumberUtils.max(arg0))

    @staticmethod
    @overload
    def createBigInteger(createBigInteger) -> 'BigInteger':
        """public static java.math.BigInteger org.apache.commons.lang3.math.NumberUtils.createBigInteger(java.lang.String)"""
        return _transform(_arg0.NumberUtils(arg0: str)).'BigInteger'Value()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.math.NumberUtils()"""
        val = _NumberUtils()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def max(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.max(int,int,int)"""
        return int._wrap(_NumberUtils.max(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def max(*arg0: int) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.max(short...)"""
        return int._wrap(_NumberUtils.max(arg0))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.Double)"""
        return _transform(_arg0.NumberUtils(arg0: 'Double')).'BigDecimal'Value()

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.Float,int,java.math.RoundingMode)"""
        return _transform(_arg0, _int.valueOf(arg1), arg2.NumberUtils(arg0: 'Float', arg1: int, arg2: 'RoundingMode')).'BigDecimal'Value()

    @staticmethod
    @overload
    def createLong(createLong) -> 'Long':
        """public static java.lang.Long org.apache.commons.lang3.math.NumberUtils.createLong(java.lang.String)"""
        return _transform(_arg0.NumberUtils(arg0: str)).'Long'Value()

    @staticmethod
    @overload
    def min(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.min(int,int,int)"""
        return int._wrap(_NumberUtils.min(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def createFloat(createFloat) -> 'Float':
        """public static java.lang.Float org.apache.commons.lang3.math.NumberUtils.createFloat(java.lang.String)"""
        return _transform(_arg0.NumberUtils(arg0: str)).'Float'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.String,int,java.math.RoundingMode)"""
        return _transform(_arg0, _int.valueOf(arg1), arg2.NumberUtils(arg0: str, arg1: int, arg2: 'RoundingMode')).'BigDecimal'Value()

    @staticmethod
    @overload
    def toDouble(arg0: 'BigDecimal', arg1: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.toDouble(java.math.BigDecimal,double)"""
        return float._wrap(_NumberUtils.toDouble(arg0, _double.valueOf(arg1)))

    @staticmethod
    @overload
    def isCreatable(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.math.NumberUtils.isCreatable(java.lang.String)"""
        return bool._wrap(_NumberUtils.isCreatable(arg0))

    @staticmethod
    @overload
    def max(*arg0: int) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.max(byte...)"""
        return int._wrap(_NumberUtils.max(bytes))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.math.BigDecimal)"""
        return _transform(_arg0.NumberUtils(arg0: 'BigDecimal')).'BigDecimal'Value()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def toLong(arg0: str) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.toLong(java.lang.String)"""
        return int._wrap(_NumberUtils.toLong(arg0))

    @staticmethod
    @overload
    def toShort(arg0: str, arg1: int) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.toShort(java.lang.String,short)"""
        return int._wrap(_NumberUtils.toShort(arg0, _short.valueOf(arg1)))

    @staticmethod
    @overload
    def max(arg0: float, arg1: float, arg2: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.max(double,double,double)"""
        return float._wrap(_NumberUtils.max(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def toInt(arg0: str, arg1: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.toInt(java.lang.String,int)"""
        return int._wrap(_NumberUtils.toInt(arg0, _int.valueOf(arg1)))

    @staticmethod
    @overload
    def compare(arg0: int, arg1: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.compare(long,long)"""
        return int._wrap(_NumberUtils.compare(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def min(*arg0: float) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.min(float...)"""
        return float._wrap(_NumberUtils.min(arg0))

    @staticmethod
    @overload
    def min(*arg0: int) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.min(byte...)"""
        return int._wrap(_NumberUtils.min(bytes))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.math.BigDecimal,int,java.math.RoundingMode)"""
        return _transform(_arg0, _int.valueOf(arg1), arg2.NumberUtils(arg0: 'BigDecimal', arg1: int, arg2: 'RoundingMode')).'BigDecimal'Value()

    @staticmethod
    @overload
    def min(arg0: int, arg1: int, arg2: int) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.min(byte,byte,byte)"""
        return int._wrap(_NumberUtils.min(_byte.valueOf(arg0), _byte.valueOf(arg1), _byte.valueOf(arg2)))

    @staticmethod
    @overload
    def max(*arg0: int) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.max(long...)"""
        return int._wrap(_NumberUtils.max(arg0))

    @staticmethod
    @overload
    def toLong(arg0: str, arg1: int) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.toLong(java.lang.String,long)"""
        return int._wrap(_NumberUtils.toLong(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def isParsable(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.math.NumberUtils.isParsable(java.lang.String)"""
        return bool._wrap(_NumberUtils.isParsable(arg0))

    @staticmethod
    @overload
    def createDouble(createDouble) -> 'Double':
        """public static java.lang.Double org.apache.commons.lang3.math.NumberUtils.createDouble(java.lang.String)"""
        return _transform(_arg0.NumberUtils(arg0: str)).'Double'Value()

    @staticmethod
    @overload
    def min(*arg0: int) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.min(short...)"""
        return int._wrap(_NumberUtils.min(arg0))

    @staticmethod
    @overload
    def createNumber(createNumber) -> 'Number':
        """public static java.lang.Number org.apache.commons.lang3.math.NumberUtils.createNumber(java.lang.String)"""
        return _transform(_arg0.NumberUtils(arg0: str)).'Number'Value()

    @staticmethod
    @overload
    def min(*arg0: int) -> int:
        """public static long org.apache.commons.lang3.math.NumberUtils.min(long...)"""
        return int._wrap(_NumberUtils.min(arg0))

    @staticmethod
    @overload
    def toDouble(arg0: 'BigDecimal') -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.toDouble(java.math.BigDecimal)"""
        return float._wrap(_NumberUtils.toDouble(arg0))

    @staticmethod
    @overload
    def toFloat(arg0: str, arg1: float) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.toFloat(java.lang.String,float)"""
        return float._wrap(_NumberUtils.toFloat(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def min(*arg0: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.min(int...)"""
        return int._wrap(_NumberUtils.min(arg0))

    @staticmethod
    @overload
    def max(*arg0: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.max(int...)"""
        return int._wrap(_NumberUtils.max(arg0))

    @staticmethod
    @overload
    def min(arg0: float, arg1: float, arg2: float) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.min(float,float,float)"""
        return float._wrap(_NumberUtils.min(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def min(arg0: float, arg1: float, arg2: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.min(double,double,double)"""
        return float._wrap(_NumberUtils.min(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2)))

    @staticmethod
    @overload
    def toInt(arg0: str) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.toInt(java.lang.String)"""
        return int._wrap(_NumberUtils.toInt(arg0))

    @staticmethod
    @overload
    def compare(arg0: int, arg1: int) -> int:
        """public static int org.apache.commons.lang3.math.NumberUtils.compare(short,short)"""
        return int._wrap(_NumberUtils.compare(_short.valueOf(arg0), _short.valueOf(arg1)))

    @staticmethod
    @overload
    def toByte(arg0: str) -> int:
        """public static byte org.apache.commons.lang3.math.NumberUtils.toByte(java.lang.String)"""
        return int._wrap(_NumberUtils.toByte(arg0))

    @staticmethod
    @overload
    def toShort(arg0: str) -> int:
        """public static short org.apache.commons.lang3.math.NumberUtils.toShort(java.lang.String)"""
        return int._wrap(_NumberUtils.toShort(arg0))

    @staticmethod
    @overload
    def isDigits(arg0: str) -> bool:
        """public static boolean org.apache.commons.lang3.math.NumberUtils.isDigits(java.lang.String)"""
        return bool._wrap(_NumberUtils.isDigits(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def max(arg0: float, arg1: float, arg2: float) -> float:
        """public static float org.apache.commons.lang3.math.NumberUtils.max(float,float,float)"""
        return float._wrap(_NumberUtils.max(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @staticmethod
    @overload
    def toDouble(arg0: str, arg1: float) -> float:
        """public static double org.apache.commons.lang3.math.NumberUtils.toDouble(java.lang.String,double)"""
        return float._wrap(_NumberUtils.toDouble(arg0, _double.valueOf(arg1)))

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.String)"""
        return _transform(_arg0.NumberUtils(arg0: str)).'BigDecimal'Value()

    @staticmethod
    @overload
    def toScaledBigDecimal(toScaledBigDecimal) -> 'BigDecimal':
        """public static java.math.BigDecimal org.apache.commons.lang3.math.NumberUtils.toScaledBigDecimal(java.lang.Float)"""
        return _transform(_arg0.NumberUtils(arg0: 'Float')).'BigDecimal'Value()