from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.math.Quantiles as __Quantiles_Scale
__Scale = __Quantiles_Scale.Scale
from builtins import type
import java.util.Collection as Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.math.Quantiles as __Quantiles_ScaleAndIndex
__ScaleAndIndex = __Quantiles_ScaleAndIndex.ScaleAndIndex
import java.lang.Object as __Object
__Object = __Object
import com.google.common.math.Quantiles as __Quantiles_ScaleAndIndexes
__ScaleAndIndexes = __Quantiles_ScaleAndIndexes.ScaleAndIndexes
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Scale():
    """com.google.common.math.Quantiles.Scale"""
 
    @staticmethod
    def __wrap(java_value: __Scale) -> 'Scale':
        return Scale(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Scale):
        """
        Dynamic initializer for Scale.
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

    @overload
    def index(self, index: int) -> 'ScaleAndIndex':
        """public com.google.common.math.Quantiles$ScaleAndIndex com.google.common.math.Quantiles$Scale.index(int)"""
        return 'ScaleAndIndex'.__wrap(super(__Scale, self).index(__int.valueOf(index)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def indexes(self, *indexes: int) -> 'ScaleAndIndexes':
        """public com.google.common.math.Quantiles$ScaleAndIndexes com.google.common.math.Quantiles$Scale.indexes(int...)"""
        return 'ScaleAndIndexes'.__wrap(super(__Scale, self).indexes(indexes))

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
    def indexes(self, indexes: 'Collection') -> 'ScaleAndIndexes':
        """public com.google.common.math.Quantiles$ScaleAndIndexes com.google.common.math.Quantiles$Scale.indexes(java.util.Collection<java.lang.Integer>)"""
        return 'ScaleAndIndexes'.__wrap(super(__Scale, self).indexes(indexes))

 
 
 
# CLASS: com.google.common.math.Quantiles$Scale
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.math.Quantiles as __Quantiles_Scale
__Scale = __Quantiles_Scale.Scale
from builtins import type
import java.util.Collection as Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.math.Quantiles as __Quantiles_ScaleAndIndex
__ScaleAndIndex = __Quantiles_ScaleAndIndex.ScaleAndIndex
import java.lang.Object as __Object
__Object = __Object
import com.google.common.math.Quantiles as __Quantiles_ScaleAndIndexes
__ScaleAndIndexes = __Quantiles_ScaleAndIndexes.ScaleAndIndexes
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Scale():
    """com.google.common.math.Quantiles.Scale"""
 
    @staticmethod
    def __wrap(java_value: __Scale) -> 'Scale':
        return Scale(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Scale):
        """
        Dynamic initializer for Scale.
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

    @overload
    def index(self, index: int) -> 'ScaleAndIndex':
        """public com.google.common.math.Quantiles$ScaleAndIndex com.google.common.math.Quantiles$Scale.index(int)"""
        return 'ScaleAndIndex'.__wrap(super(__Scale, self).index(__int.valueOf(index)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def indexes(self, *indexes: int) -> 'ScaleAndIndexes':
        """public com.google.common.math.Quantiles$ScaleAndIndexes com.google.common.math.Quantiles$Scale.indexes(int...)"""
        return 'ScaleAndIndexes'.__wrap(super(__Scale, self).indexes(indexes))

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
    def indexes(self, indexes: 'Collection') -> 'ScaleAndIndexes':
        """public com.google.common.math.Quantiles$ScaleAndIndexes com.google.common.math.Quantiles$Scale.indexes(java.util.Collection<java.lang.Integer>)"""
        return 'ScaleAndIndexes'.__wrap(super(__Scale, self).indexes(indexes))

 
 
 
# CLASS: com.google.common.math.Quantiles$Scale 
 
 
# CLASS: com.google.common.math.DoubleMath
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import java.util.Iterator as Iterator
import java.math.BigInteger as BigInteger
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.math.RoundingMode as RoundingMode
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
import com.google.common.math.DoubleMath as __DoubleMath
__DoubleMath = __DoubleMath
from builtins import int
 
class DoubleMath():
    """com.google.common.math.DoubleMath"""
 
    @staticmethod
    def __wrap(java_value: __DoubleMath) -> 'DoubleMath':
        return DoubleMath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleMath):
        """
        Dynamic initializer for DoubleMath.
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
    def factorial(n: int) -> float:
        """public static double com.google.common.math.DoubleMath.factorial(int)"""
        return float.__wrap(__DoubleMath.factorial(__int.valueOf(n)))

    @staticmethod
    @overload
    def roundToInt(x: float, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.DoubleMath.roundToInt(double,java.math.RoundingMode)"""
        return int.__wrap(__DoubleMath.roundToInt(__double.valueOf(x), mode))

    @staticmethod
    @overload
    def isMathematicalInteger(x: float) -> bool:
        """public static boolean com.google.common.math.DoubleMath.isMathematicalInteger(double)"""
        return bool.__wrap(__DoubleMath.isMathematicalInteger(__double.valueOf(x)))

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

    @staticmethod
    @overload
    def mean(*values: float) -> float:
        """public static double com.google.common.math.DoubleMath.mean(double...)"""
        return float.__wrap(__DoubleMath.mean(values))

    @staticmethod
    @overload
    def mean(*values: int) -> float:
        """public static double com.google.common.math.DoubleMath.mean(long...)"""
        return float.__wrap(__DoubleMath.mean(values))

    @staticmethod
    @overload
    def mean(*values: int) -> float:
        """public static double com.google.common.math.DoubleMath.mean(int...)"""
        return float.__wrap(__DoubleMath.mean(values))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def roundToLong(x: float, mode: 'RoundingMode') -> int:
        """public static long com.google.common.math.DoubleMath.roundToLong(double,java.math.RoundingMode)"""
        return int.__wrap(__DoubleMath.roundToLong(__double.valueOf(x), mode))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def roundToBigInteger(roundToBigInteger) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.DoubleMath.roundToBigInteger(double,java.math.RoundingMode)"""
        return __transform(____double.valueOf(x), mode.DoubleMath(x: float, mode: 'RoundingMode')).'BigInteger'Value()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def log2(x: float, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.DoubleMath.log2(double,java.math.RoundingMode)"""
        return int.__wrap(__DoubleMath.log2(__double.valueOf(x), mode))

    @staticmethod
    @overload
    def log2(x: float) -> float:
        """public static double com.google.common.math.DoubleMath.log2(double)"""
        return float.__wrap(__DoubleMath.log2(__double.valueOf(x)))

    @staticmethod
    @overload
    def mean(values: 'Iterable') -> float:
        """public static double com.google.common.math.DoubleMath.mean(java.lang.Iterable<? extends java.lang.Number>)"""
        return float.__wrap(__DoubleMath.mean(values))

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
    def mean(values: 'Iterator') -> float:
        """public static double com.google.common.math.DoubleMath.mean(java.util.Iterator<? extends java.lang.Number>)"""
        return float.__wrap(__DoubleMath.mean(values))

    @staticmethod
    @overload
    def isPowerOfTwo(x: float) -> bool:
        """public static boolean com.google.common.math.DoubleMath.isPowerOfTwo(double)"""
        return bool.__wrap(__DoubleMath.isPowerOfTwo(__double.valueOf(x)))

    @staticmethod
    @overload
    def fuzzyEquals(a: float, b: float, tolerance: float) -> bool:
        """public static boolean com.google.common.math.DoubleMath.fuzzyEquals(double,double,double)"""
        return bool.__wrap(__DoubleMath.fuzzyEquals(__double.valueOf(a), __double.valueOf(b), __double.valueOf(tolerance)))

    @staticmethod
    @overload
    def fuzzyCompare(a: float, b: float, tolerance: float) -> int:
        """public static int com.google.common.math.DoubleMath.fuzzyCompare(double,double,double)"""
        return int.__wrap(__DoubleMath.fuzzyCompare(__double.valueOf(a), __double.valueOf(b), __double.valueOf(tolerance)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.math.LinearTransformation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.math.LinearTransformation as __LinearTransformation
__LinearTransformation = __LinearTransformation
from abc import abstractmethod, ABC
import com.google.common.math.LinearTransformation as __LinearTransformation_LinearTransformationBuilder
__LinearTransformationBuilder = __LinearTransformation_LinearTransformationBuilder.LinearTransformationBuilder
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
 
class LinearTransformation(ABC):
    """com.google.common.math.LinearTransformation"""
 
    @staticmethod
    def __wrap(java_value: __LinearTransformation) -> 'LinearTransformation':
        return LinearTransformation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinearTransformation):
        """
        Dynamic initializer for LinearTransformation.
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

    @abstractmethod
    def isHorizontal(self, ):
        """public abstract boolean com.google.common.math.LinearTransformation.isHorizontal()"""
        pass

    @abstractmethod
    def slope(self, ):
        """public abstract double com.google.common.math.LinearTransformation.slope()"""
        pass

    @staticmethod
    @overload
    def vertical(x: float) -> 'LinearTransformation':
        """public static com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation.vertical(double)"""
        return LinearTransformation.__wrap(__LinearTransformation.vertical(__double.valueOf(x)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def mapping(x1: float, y1: float) -> 'LinearTransformationBuilder':
        """public static com.google.common.math.LinearTransformation$LinearTransformationBuilder com.google.common.math.LinearTransformation.mapping(double,double)"""
        return LinearTransformationBuilder.__wrap(__LinearTransformation.mapping(__double.valueOf(x1), __double.valueOf(y1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.google.common.math.LinearTransformation()"""
        val = __LinearTransformation()
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

    @abstractmethod
    def transform(self, x: float):
        """public abstract double com.google.common.math.LinearTransformation.transform(double)"""
        pass

    @staticmethod
    @overload
    def horizontal(y: float) -> 'LinearTransformation':
        """public static com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation.horizontal(double)"""
        return LinearTransformation.__wrap(__LinearTransformation.horizontal(__double.valueOf(y)))

    @abstractmethod
    def inverse(self, ):
        """public abstract com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation.inverse()"""
        pass

    @staticmethod
    @overload
    def forNaN() -> 'LinearTransformation':
        """public static com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation.forNaN()"""
        return LinearTransformation.__wrap(__LinearTransformation.forNaN())

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
    def __init__(self):
        """public com.google.common.math.LinearTransformation()"""
        val = __LinearTransformation()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def isVertical(self, ):
        """public abstract boolean com.google.common.math.LinearTransformation.isVertical()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.math.BigDecimalMath
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.math.BigDecimalMath as __BigDecimalMath
__BigDecimalMath = __BigDecimalMath
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.math.RoundingMode as RoundingMode
import java.math.BigDecimal as BigDecimal
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BigDecimalMath():
    """com.google.common.math.BigDecimalMath"""
 
    @staticmethod
    def __wrap(java_value: __BigDecimalMath) -> 'BigDecimalMath':
        return BigDecimalMath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BigDecimalMath):
        """
        Dynamic initializer for BigDecimalMath.
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

    @staticmethod
    @overload
    def roundToDouble(x: 'BigDecimal', mode: 'RoundingMode') -> float:
        """public static double com.google.common.math.BigDecimalMath.roundToDouble(java.math.BigDecimal,java.math.RoundingMode)"""
        return float.__wrap(__BigDecimalMath.roundToDouble(x, mode))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.math.Quantiles
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.math.Quantiles as __Quantiles_Scale
__Scale = __Quantiles_Scale.Scale
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.math.Quantiles as __Quantiles_ScaleAndIndex
__ScaleAndIndex = __Quantiles_ScaleAndIndex.ScaleAndIndex
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.math.Quantiles as __Quantiles
__Quantiles = __Quantiles
from builtins import int
 
class Quantiles():
    """com.google.common.math.Quantiles"""
 
    @staticmethod
    def __wrap(java_value: __Quantiles) -> 'Quantiles':
        return Quantiles(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Quantiles):
        """
        Dynamic initializer for Quantiles.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def scale(scale: int) -> 'Scale':
        """public static com.google.common.math.Quantiles$Scale com.google.common.math.Quantiles.scale(int)"""
        return Scale.__wrap(__Quantiles.scale(__int.valueOf(scale)))

    @staticmethod
    @overload
    def median() -> 'ScaleAndIndex':
        """public static com.google.common.math.Quantiles$ScaleAndIndex com.google.common.math.Quantiles.median()"""
        return ScaleAndIndex.__wrap(__Quantiles.median())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def quartiles() -> 'Scale':
        """public static com.google.common.math.Quantiles$Scale com.google.common.math.Quantiles.quartiles()"""
        return Scale.__wrap(__Quantiles.quartiles())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.google.common.math.Quantiles()"""
        val = __Quantiles()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def percentiles() -> 'Scale':
        """public static com.google.common.math.Quantiles$Scale com.google.common.math.Quantiles.percentiles()"""
        return Scale.__wrap(__Quantiles.percentiles())

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
    def __init__(self, ):
        """public com.google.common.math.Quantiles()"""
        val = __Quantiles()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.math.IntMath
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.math.IntMath as __IntMath
__IntMath = __IntMath
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.math.RoundingMode as RoundingMode
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntMath():
    """com.google.common.math.IntMath"""
 
    @staticmethod
    def __wrap(java_value: __IntMath) -> 'IntMath':
        return IntMath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntMath):
        """
        Dynamic initializer for IntMath.
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
    def saturatedPow(b: int, k: int) -> int:
        """public static int com.google.common.math.IntMath.saturatedPow(int,int)"""
        return int.__wrap(__IntMath.saturatedPow(__int.valueOf(b), __int.valueOf(k)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def saturatedMultiply(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.saturatedMultiply(int,int)"""
        return int.__wrap(__IntMath.saturatedMultiply(__int.valueOf(a), __int.valueOf(b)))

    @staticmethod
    @overload
    def floorPowerOfTwo(x: int) -> int:
        """public static int com.google.common.math.IntMath.floorPowerOfTwo(int)"""
        return int.__wrap(__IntMath.floorPowerOfTwo(__int.valueOf(x)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def divide(p: int, q: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.IntMath.divide(int,int,java.math.RoundingMode)"""
        return int.__wrap(__IntMath.divide(__int.valueOf(p), __int.valueOf(q), mode))

    @staticmethod
    @overload
    def log2(x: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.IntMath.log2(int,java.math.RoundingMode)"""
        return int.__wrap(__IntMath.log2(__int.valueOf(x), mode))

    @staticmethod
    @overload
    def checkedMultiply(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.checkedMultiply(int,int)"""
        return int.__wrap(__IntMath.checkedMultiply(__int.valueOf(a), __int.valueOf(b)))

    @staticmethod
    @overload
    def checkedSubtract(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.checkedSubtract(int,int)"""
        return int.__wrap(__IntMath.checkedSubtract(__int.valueOf(a), __int.valueOf(b)))

    @staticmethod
    @overload
    def saturatedSubtract(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.saturatedSubtract(int,int)"""
        return int.__wrap(__IntMath.saturatedSubtract(__int.valueOf(a), __int.valueOf(b)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isPowerOfTwo(x: int) -> bool:
        """public static boolean com.google.common.math.IntMath.isPowerOfTwo(int)"""
        return bool.__wrap(__IntMath.isPowerOfTwo(__int.valueOf(x)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def saturatedAdd(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.saturatedAdd(int,int)"""
        return int.__wrap(__IntMath.saturatedAdd(__int.valueOf(a), __int.valueOf(b)))

    @staticmethod
    @overload
    def binomial(n: int, k: int) -> int:
        """public static int com.google.common.math.IntMath.binomial(int,int)"""
        return int.__wrap(__IntMath.binomial(__int.valueOf(n), __int.valueOf(k)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def pow(b: int, k: int) -> int:
        """public static int com.google.common.math.IntMath.pow(int,int)"""
        return int.__wrap(__IntMath.pow(__int.valueOf(b), __int.valueOf(k)))

    @staticmethod
    @overload
    def checkedPow(b: int, k: int) -> int:
        """public static int com.google.common.math.IntMath.checkedPow(int,int)"""
        return int.__wrap(__IntMath.checkedPow(__int.valueOf(b), __int.valueOf(k)))

    @staticmethod
    @overload
    def mean(x: int, y: int) -> int:
        """public static int com.google.common.math.IntMath.mean(int,int)"""
        return int.__wrap(__IntMath.mean(__int.valueOf(x), __int.valueOf(y)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def log10(x: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.IntMath.log10(int,java.math.RoundingMode)"""
        return int.__wrap(__IntMath.log10(__int.valueOf(x), mode))

    @staticmethod
    @overload
    def ceilingPowerOfTwo(x: int) -> int:
        """public static int com.google.common.math.IntMath.ceilingPowerOfTwo(int)"""
        return int.__wrap(__IntMath.ceilingPowerOfTwo(__int.valueOf(x)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def factorial(n: int) -> int:
        """public static int com.google.common.math.IntMath.factorial(int)"""
        return int.__wrap(__IntMath.factorial(__int.valueOf(n)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def mod(x: int, m: int) -> int:
        """public static int com.google.common.math.IntMath.mod(int,int)"""
        return int.__wrap(__IntMath.mod(__int.valueOf(x), __int.valueOf(m)))

    @staticmethod
    @overload
    def sqrt(x: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.IntMath.sqrt(int,java.math.RoundingMode)"""
        return int.__wrap(__IntMath.sqrt(__int.valueOf(x), mode))

    @staticmethod
    @overload
    def checkedAdd(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.checkedAdd(int,int)"""
        return int.__wrap(__IntMath.checkedAdd(__int.valueOf(a), __int.valueOf(b)))

    @staticmethod
    @overload
    def isPrime(n: int) -> bool:
        """public static boolean com.google.common.math.IntMath.isPrime(int)"""
        return bool.__wrap(__IntMath.isPrime(__int.valueOf(n)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def gcd(a: int, b: int) -> int:
        """public static int com.google.common.math.IntMath.gcd(int,int)"""
        return int.__wrap(__IntMath.gcd(__int.valueOf(a), __int.valueOf(b))) 
 
 
# CLASS: com.google.common.math.Quantiles$ScaleAndIndexes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
from builtins import float
import java.util.Collection as Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.math.Quantiles as __Quantiles_ScaleAndIndexes
__ScaleAndIndexes = __Quantiles_ScaleAndIndexes.ScaleAndIndexes
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class ScaleAndIndexes():
    """com.google.common.math.Quantiles.ScaleAndIndexes"""
 
    @staticmethod
    def __wrap(java_value: __ScaleAndIndexes) -> 'ScaleAndIndexes':
        return ScaleAndIndexes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScaleAndIndexes):
        """
        Dynamic initializer for ScaleAndIndexes.
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
    def compute(self, *dataset: int) -> 'Map':
        """public java.util.Map<java.lang.Integer, java.lang.Double> com.google.common.math.Quantiles$ScaleAndIndexes.compute(int...)"""
        return 'Map'.__wrap(super(__ScaleAndIndexes, self).compute(dataset))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def compute(self, *dataset: float) -> 'Map':
        """public java.util.Map<java.lang.Integer, java.lang.Double> com.google.common.math.Quantiles$ScaleAndIndexes.compute(double...)"""
        return 'Map'.__wrap(super(__ScaleAndIndexes, self).compute(dataset))

    @overload
    def computeInPlace(self, *dataset: float) -> 'Map':
        """public java.util.Map<java.lang.Integer, java.lang.Double> com.google.common.math.Quantiles$ScaleAndIndexes.computeInPlace(double...)"""
        return 'Map'.__wrap(super(__ScaleAndIndexes, self).computeInPlace(dataset))

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
    def compute(self, *dataset: int) -> 'Map':
        """public java.util.Map<java.lang.Integer, java.lang.Double> com.google.common.math.Quantiles$ScaleAndIndexes.compute(long...)"""
        return 'Map'.__wrap(super(__ScaleAndIndexes, self).compute(dataset))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compute(self, dataset: 'Collection') -> 'Map':
        """public java.util.Map<java.lang.Integer, java.lang.Double> com.google.common.math.Quantiles$ScaleAndIndexes.compute(java.util.Collection<? extends java.lang.Number>)"""
        return 'Map'.__wrap(super(__ScaleAndIndexes, self).compute(dataset))

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
 
 
# CLASS: com.google.common.math.Stats
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.stream.Collector as __Collector
__Collector = __Collector
from builtins import float
import java.lang.Iterable as Iterable
import java.util.stream.Collector as Collector
import java.util.Iterator as Iterator
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.stream.LongStream as LongStream
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.DoubleStream as DoubleStream
import com.google.common.math.Stats as __Stats
__Stats = __Stats
import java.util.stream.IntStream as IntStream
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Stats():
    """com.google.common.math.Stats"""
 
    @staticmethod
    def __wrap(java_value: __Stats) -> 'Stats':
        return Stats(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Stats):
        """
        Dynamic initializer for Stats.
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
    def toByteArray(self) -> List[int]:
        """public byte[] com.google.common.math.Stats.toByteArray()"""
        return List[int].__wrap(super(Stats, self).toByteArray())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def meanOf(*values: int) -> float:
        """public static double com.google.common.math.Stats.meanOf(long...)"""
        return float.__wrap(__Stats.meanOf(values))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.math.Stats.hashCode()"""
        return int.__wrap(super(Stats, self).hashCode())

    @staticmethod
    @overload
    def of(*values: float) -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(double...)"""
        return Stats.__wrap(__Stats.of(values))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.math.Stats.toString()"""
        return str.__wrap(super(Stats, self).toString())

    @staticmethod
    @overload
    def of(values: 'Iterable') -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(java.lang.Iterable<? extends java.lang.Number>)"""
        return Stats.__wrap(__Stats.of(values))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def of(values: 'LongStream') -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(java.util.stream.LongStream)"""
        return Stats.__wrap(__Stats.of(values))

    @overload
    def populationVariance(self) -> float:
        """public double com.google.common.math.Stats.populationVariance()"""
        return float.__wrap(super(Stats, self).populationVariance())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.math.Stats.equals(java.lang.Object)"""
        return bool.__wrap(super(__Stats, self).equals(obj))

    @overload
    def mean(self) -> float:
        """public double com.google.common.math.Stats.mean()"""
        return float.__wrap(super(Stats, self).mean())

    @staticmethod
    @overload
    def of(values: 'Iterator') -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(java.util.Iterator<? extends java.lang.Number>)"""
        return Stats.__wrap(__Stats.of(values))

    @staticmethod
    @overload
    def of(*values: int) -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(long...)"""
        return Stats.__wrap(__Stats.of(values))

    @staticmethod
    @overload
    def meanOf(values: 'Iterator') -> float:
        """public static double com.google.common.math.Stats.meanOf(java.util.Iterator<? extends java.lang.Number>)"""
        return float.__wrap(__Stats.meanOf(values))

    @overload
    def sampleVariance(self) -> float:
        """public double com.google.common.math.Stats.sampleVariance()"""
        return float.__wrap(super(Stats, self).sampleVariance())

    @staticmethod
    @overload
    def of(values: 'DoubleStream') -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(java.util.stream.DoubleStream)"""
        return Stats.__wrap(__Stats.of(values))

    @staticmethod
    @overload
    def fromByteArray(byteArray: bytes) -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.fromByteArray(byte[])"""
        return Stats.__wrap(__Stats.fromByteArray(bytes))

    @staticmethod
    @overload
    def toStats() -> 'Collector':
        """public static java.util.stream.Collector<java.lang.Number, com.google.common.math.StatsAccumulator, com.google.common.math.Stats> com.google.common.math.Stats.toStats()"""
        return Collector.__wrap(__Stats.toStats())

    @overload
    def sum(self) -> float:
        """public double com.google.common.math.Stats.sum()"""
        return float.__wrap(super(Stats, self).sum())

    @overload
    def count(self) -> int:
        """public long com.google.common.math.Stats.count()"""
        return int.__wrap(super(Stats, self).count())

    @overload
    def max(self) -> float:
        """public double com.google.common.math.Stats.max()"""
        return float.__wrap(super(Stats, self).max())

    @staticmethod
    @overload
    def meanOf(*values: int) -> float:
        """public static double com.google.common.math.Stats.meanOf(int...)"""
        return float.__wrap(__Stats.meanOf(values))

    @overload
    def sampleStandardDeviation(self) -> float:
        """public double com.google.common.math.Stats.sampleStandardDeviation()"""
        return float.__wrap(super(Stats, self).sampleStandardDeviation())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def of(values: 'IntStream') -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(java.util.stream.IntStream)"""
        return Stats.__wrap(__Stats.of(values))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def of(*values: int) -> 'Stats':
        """public static com.google.common.math.Stats com.google.common.math.Stats.of(int...)"""
        return Stats.__wrap(__Stats.of(values))

    @staticmethod
    @overload
    def meanOf(values: 'Iterable') -> float:
        """public static double com.google.common.math.Stats.meanOf(java.lang.Iterable<? extends java.lang.Number>)"""
        return float.__wrap(__Stats.meanOf(values))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def populationStandardDeviation(self) -> float:
        """public double com.google.common.math.Stats.populationStandardDeviation()"""
        return float.__wrap(super(Stats, self).populationStandardDeviation())

    @overload
    def min(self) -> float:
        """public double com.google.common.math.Stats.min()"""
        return float.__wrap(super(Stats, self).min())

    @staticmethod
    @overload
    def meanOf(*values: float) -> float:
        """public static double com.google.common.math.Stats.meanOf(double...)"""
        return float.__wrap(__Stats.meanOf(values)) 
 
 
# CLASS: com.google.common.math.Quantiles$ScaleAndIndex
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.util.Collection as Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.math.Quantiles as __Quantiles_ScaleAndIndex
__ScaleAndIndex = __Quantiles_ScaleAndIndex.ScaleAndIndex
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ScaleAndIndex():
    """com.google.common.math.Quantiles.ScaleAndIndex"""
 
    @staticmethod
    def __wrap(java_value: __ScaleAndIndex) -> 'ScaleAndIndex':
        return ScaleAndIndex(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScaleAndIndex):
        """
        Dynamic initializer for ScaleAndIndex.
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
    def compute(self, *dataset: int) -> float:
        """public double com.google.common.math.Quantiles$ScaleAndIndex.compute(int...)"""
        return float.__wrap(super(__ScaleAndIndex, self).compute(dataset))

    @overload
    def compute(self, *dataset: float) -> float:
        """public double com.google.common.math.Quantiles$ScaleAndIndex.compute(double...)"""
        return float.__wrap(super(__ScaleAndIndex, self).compute(dataset))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compute(self, *dataset: int) -> float:
        """public double com.google.common.math.Quantiles$ScaleAndIndex.compute(long...)"""
        return float.__wrap(super(__ScaleAndIndex, self).compute(dataset))

    @overload
    def computeInPlace(self, *dataset: float) -> float:
        """public double com.google.common.math.Quantiles$ScaleAndIndex.computeInPlace(double...)"""
        return float.__wrap(super(__ScaleAndIndex, self).computeInPlace(dataset))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def compute(self, dataset: 'Collection') -> float:
        """public double com.google.common.math.Quantiles$ScaleAndIndex.compute(java.util.Collection<? extends java.lang.Number>)"""
        return float.__wrap(super(__ScaleAndIndex, self).compute(dataset))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.math.PairedStats
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.google.common.math.LinearTransformation as __LinearTransformation
__LinearTransformation = __LinearTransformation
import com.google.common.math.PairedStats as __PairedStats
__PairedStats = __PairedStats
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.math.Stats as __Stats
__Stats = __Stats
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PairedStats():
    """com.google.common.math.PairedStats"""
 
    @staticmethod
    def __wrap(java_value: __PairedStats) -> 'PairedStats':
        return PairedStats(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PairedStats):
        """
        Dynamic initializer for PairedStats.
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
    def populationCovariance(self) -> float:
        """public double com.google.common.math.PairedStats.populationCovariance()"""
        return float.__wrap(super(PairedStats, self).populationCovariance())

    @overload
    def leastSquaresFit(self) -> 'LinearTransformation':
        """public com.google.common.math.LinearTransformation com.google.common.math.PairedStats.leastSquaresFit()"""
        return 'LinearTransformation'.__wrap(super(PairedStats, self).leastSquaresFit())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.math.PairedStats.toString()"""
        return str.__wrap(super(PairedStats, self).toString())

    @overload
    def count(self) -> int:
        """public long com.google.common.math.PairedStats.count()"""
        return int.__wrap(super(PairedStats, self).count())

    @staticmethod
    @overload
    def fromByteArray(byteArray: bytes) -> 'PairedStats':
        """public static com.google.common.math.PairedStats com.google.common.math.PairedStats.fromByteArray(byte[])"""
        return PairedStats.__wrap(__PairedStats.fromByteArray(bytes))

    @overload
    def xStats(self) -> 'Stats':
        """public com.google.common.math.Stats com.google.common.math.PairedStats.xStats()"""
        return 'Stats'.__wrap(super(PairedStats, self).xStats())

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
    def hashCode(self) -> int:
        """public int com.google.common.math.PairedStats.hashCode()"""
        return int.__wrap(super(PairedStats, self).hashCode())

    @overload
    def yStats(self) -> 'Stats':
        """public com.google.common.math.Stats com.google.common.math.PairedStats.yStats()"""
        return 'Stats'.__wrap(super(PairedStats, self).yStats())

    @overload
    def pearsonsCorrelationCoefficient(self) -> float:
        """public double com.google.common.math.PairedStats.pearsonsCorrelationCoefficient()"""
        return float.__wrap(super(PairedStats, self).pearsonsCorrelationCoefficient())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.math.PairedStats.equals(java.lang.Object)"""
        return bool.__wrap(super(__PairedStats, self).equals(obj))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toByteArray(self) -> List[int]:
        """public byte[] com.google.common.math.PairedStats.toByteArray()"""
        return List[int].__wrap(super(PairedStats, self).toByteArray())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def sampleCovariance(self) -> float:
        """public double com.google.common.math.PairedStats.sampleCovariance()"""
        return float.__wrap(super(PairedStats, self).sampleCovariance()) 
 
 
# CLASS: com.google.common.math.BigIntegerMath
from builtins import str
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
import com.google.common.math.BigIntegerMath as __BigIntegerMath
__BigIntegerMath = __BigIntegerMath
import java.lang.Object as __Object
__Object = __Object
import java.math.RoundingMode as RoundingMode
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BigIntegerMath():
    """com.google.common.math.BigIntegerMath"""
 
    @staticmethod
    def __wrap(java_value: __BigIntegerMath) -> 'BigIntegerMath':
        return BigIntegerMath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BigIntegerMath):
        """
        Dynamic initializer for BigIntegerMath.
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
    def sqrt(sqrt) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.sqrt(java.math.BigInteger,java.math.RoundingMode)"""
        return __transform(__x, mode.BigIntegerMath(x: 'BigInteger', mode: 'RoundingMode')).'BigInteger'Value()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def log10(x: 'BigInteger', mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.BigIntegerMath.log10(java.math.BigInteger,java.math.RoundingMode)"""
        return int.__wrap(__BigIntegerMath.log10(x, mode))

    @staticmethod
    @overload
    def floorPowerOfTwo(floorPowerOfTwo) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.floorPowerOfTwo(java.math.BigInteger)"""
        return __transform(__x.BigIntegerMath(x: 'BigInteger')).'BigInteger'Value()

    @staticmethod
    @overload
    def log2(x: 'BigInteger', mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.BigIntegerMath.log2(java.math.BigInteger,java.math.RoundingMode)"""
        return int.__wrap(__BigIntegerMath.log2(x, mode))

    @staticmethod
    @overload
    def divide(divide) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.divide(java.math.BigInteger,java.math.BigInteger,java.math.RoundingMode)"""
        return __transform(__p, q, mode.BigIntegerMath(p: 'BigInteger', q: 'BigInteger', mode: 'RoundingMode')).'BigInteger'Value()

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

    @staticmethod
    @overload
    def isPowerOfTwo(x: 'BigInteger') -> bool:
        """public static boolean com.google.common.math.BigIntegerMath.isPowerOfTwo(java.math.BigInteger)"""
        return bool.__wrap(__BigIntegerMath.isPowerOfTwo(x))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def roundToDouble(x: 'BigInteger', mode: 'RoundingMode') -> float:
        """public static double com.google.common.math.BigIntegerMath.roundToDouble(java.math.BigInteger,java.math.RoundingMode)"""
        return float.__wrap(__BigIntegerMath.roundToDouble(x, mode))

    @staticmethod
    @overload
    def binomial(binomial) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.binomial(int,int)"""
        return __transform(____int.valueOf(n), __int.valueOf(k).BigIntegerMath(n: int, k: int)).'BigInteger'Value()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def ceilingPowerOfTwo(ceilingPowerOfTwo) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.ceilingPowerOfTwo(java.math.BigInteger)"""
        return __transform(__x.BigIntegerMath(x: 'BigInteger')).'BigInteger'Value()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def factorial(factorial) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.math.BigIntegerMath.factorial(int)"""
        return __transform(____int.valueOf(n).BigIntegerMath(n: int)).'BigInteger'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.math.LinearTransformation$LinearTransformationBuilder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.math.LinearTransformation as __LinearTransformation
__LinearTransformation = __LinearTransformation
import com.google.common.math.LinearTransformation as __LinearTransformation_LinearTransformationBuilder
__LinearTransformationBuilder = __LinearTransformation_LinearTransformationBuilder.LinearTransformationBuilder
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
 
class LinearTransformationBuilder():
    """com.google.common.math.LinearTransformation.LinearTransformationBuilder"""
 
    @staticmethod
    def __wrap(java_value: __LinearTransformationBuilder) -> 'LinearTransformationBuilder':
        return LinearTransformationBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinearTransformationBuilder):
        """
        Dynamic initializer for LinearTransformationBuilder.
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

    @overload
    def and(self, x2: float, y2: float) -> 'LinearTransformation':
        """public com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation$LinearTransformationBuilder.and(double,double)"""
        return 'LinearTransformation'.__wrap(super(__LinearTransformationBuilder, self).and(__double.valueOf(x2), __double.valueOf(y2)))

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

    @overload
    def withSlope(self, slope: float) -> 'LinearTransformation':
        """public com.google.common.math.LinearTransformation com.google.common.math.LinearTransformation$LinearTransformationBuilder.withSlope(double)"""
        return 'LinearTransformation'.__wrap(super(__LinearTransformationBuilder, self).withSlope(__double.valueOf(slope))) 
 
 
# CLASS: com.google.common.math.PairedStatsAccumulator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.google.common.math.LinearTransformation as __LinearTransformation
__LinearTransformation = __LinearTransformation
import com.google.common.math.PairedStats as __PairedStats
__PairedStats = __PairedStats
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.math.PairedStatsAccumulator as __PairedStatsAccumulator
__PairedStatsAccumulator = __PairedStatsAccumulator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import com.google.common.math.Stats as __Stats
__Stats = __Stats
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PairedStatsAccumulator():
    """com.google.common.math.PairedStatsAccumulator"""
 
    @staticmethod
    def __wrap(java_value: __PairedStatsAccumulator) -> 'PairedStatsAccumulator':
        return PairedStatsAccumulator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PairedStatsAccumulator):
        """
        Dynamic initializer for PairedStatsAccumulator.
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
    def add(self, x: float, y: float):
        """public void com.google.common.math.PairedStatsAccumulator.add(double,double)"""
        super(__PairedStatsAccumulator, self).add(__double.valueOf(x), __double.valueOf(y))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def sampleCovariance(self) -> float:
        """public final double com.google.common.math.PairedStatsAccumulator.sampleCovariance()"""
        return float.__wrap(super(PairedStatsAccumulator, self).sampleCovariance())

    @overload
    def yStats(self) -> 'Stats':
        """public com.google.common.math.Stats com.google.common.math.PairedStatsAccumulator.yStats()"""
        return 'Stats'.__wrap(super(PairedStatsAccumulator, self).yStats())

    @overload
    def populationCovariance(self) -> float:
        """public double com.google.common.math.PairedStatsAccumulator.populationCovariance()"""
        return float.__wrap(super(PairedStatsAccumulator, self).populationCovariance())

    @overload
    def leastSquaresFit(self) -> 'LinearTransformation':
        """public final com.google.common.math.LinearTransformation com.google.common.math.PairedStatsAccumulator.leastSquaresFit()"""
        return 'LinearTransformation'.__wrap(super(PairedStatsAccumulator, self).leastSquaresFit())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def xStats(self) -> 'Stats':
        """public com.google.common.math.Stats com.google.common.math.PairedStatsAccumulator.xStats()"""
        return 'Stats'.__wrap(super(PairedStatsAccumulator, self).xStats())

    @overload
    def __init__(self):
        """public com.google.common.math.PairedStatsAccumulator()"""
        val = __PairedStatsAccumulator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def pearsonsCorrelationCoefficient(self) -> float:
        """public final double com.google.common.math.PairedStatsAccumulator.pearsonsCorrelationCoefficient()"""
        return float.__wrap(super(PairedStatsAccumulator, self).pearsonsCorrelationCoefficient())

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
    def count(self) -> int:
        """public long com.google.common.math.PairedStatsAccumulator.count()"""
        return int.__wrap(super(PairedStatsAccumulator, self).count())

    @overload
    def __init__(self, ):
        """public com.google.common.math.PairedStatsAccumulator()"""
        val = __PairedStatsAccumulator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addAll(self, values: 'PairedStats'):
        """public void com.google.common.math.PairedStatsAccumulator.addAll(com.google.common.math.PairedStats)"""
        super(__PairedStatsAccumulator, self).addAll(values)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def snapshot(self) -> 'PairedStats':
        """public com.google.common.math.PairedStats com.google.common.math.PairedStatsAccumulator.snapshot()"""
        return 'PairedStats'.__wrap(super(PairedStatsAccumulator, self).snapshot()) 
 
 
# CLASS: com.google.common.math.LongMath
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.google.common.math.LongMath as __LongMath
__LongMath = __LongMath
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.math.RoundingMode as RoundingMode
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LongMath():
    """com.google.common.math.LongMath"""
 
    @staticmethod
    def __wrap(java_value: __LongMath) -> 'LongMath':
        return LongMath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongMath):
        """
        Dynamic initializer for LongMath.
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
    def checkedPow(b: int, k: int) -> int:
        """public static long com.google.common.math.LongMath.checkedPow(long,int)"""
        return int.__wrap(__LongMath.checkedPow(__long.valueOf(b), __int.valueOf(k)))

    @staticmethod
    @overload
    def mod(x: int, m: int) -> int:
        """public static long com.google.common.math.LongMath.mod(long,long)"""
        return int.__wrap(__LongMath.mod(__long.valueOf(x), __long.valueOf(m)))

    @staticmethod
    @overload
    def divide(p: int, q: int, mode: 'RoundingMode') -> int:
        """public static long com.google.common.math.LongMath.divide(long,long,java.math.RoundingMode)"""
        return int.__wrap(__LongMath.divide(__long.valueOf(p), __long.valueOf(q), mode))

    @staticmethod
    @overload
    def floorPowerOfTwo(x: int) -> int:
        """public static long com.google.common.math.LongMath.floorPowerOfTwo(long)"""
        return int.__wrap(__LongMath.floorPowerOfTwo(__long.valueOf(x)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def isPowerOfTwo(x: int) -> bool:
        """public static boolean com.google.common.math.LongMath.isPowerOfTwo(long)"""
        return bool.__wrap(__LongMath.isPowerOfTwo(__long.valueOf(x)))

    @staticmethod
    @overload
    def sqrt(x: int, mode: 'RoundingMode') -> int:
        """public static long com.google.common.math.LongMath.sqrt(long,java.math.RoundingMode)"""
        return int.__wrap(__LongMath.sqrt(__long.valueOf(x), mode))

    @staticmethod
    @overload
    def checkedSubtract(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.checkedSubtract(long,long)"""
        return int.__wrap(__LongMath.checkedSubtract(__long.valueOf(a), __long.valueOf(b)))

    @staticmethod
    @overload
    def isPrime(n: int) -> bool:
        """public static boolean com.google.common.math.LongMath.isPrime(long)"""
        return bool.__wrap(__LongMath.isPrime(__long.valueOf(n)))

    @staticmethod
    @overload
    def gcd(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.gcd(long,long)"""
        return int.__wrap(__LongMath.gcd(__long.valueOf(a), __long.valueOf(b)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def saturatedMultiply(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.saturatedMultiply(long,long)"""
        return int.__wrap(__LongMath.saturatedMultiply(__long.valueOf(a), __long.valueOf(b)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def pow(b: int, k: int) -> int:
        """public static long com.google.common.math.LongMath.pow(long,int)"""
        return int.__wrap(__LongMath.pow(__long.valueOf(b), __int.valueOf(k)))

    @staticmethod
    @overload
    def mean(x: int, y: int) -> int:
        """public static long com.google.common.math.LongMath.mean(long,long)"""
        return int.__wrap(__LongMath.mean(__long.valueOf(x), __long.valueOf(y)))

    @staticmethod
    @overload
    def checkedMultiply(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.checkedMultiply(long,long)"""
        return int.__wrap(__LongMath.checkedMultiply(__long.valueOf(a), __long.valueOf(b)))

    @staticmethod
    @overload
    def factorial(n: int) -> int:
        """public static long com.google.common.math.LongMath.factorial(int)"""
        return int.__wrap(__LongMath.factorial(__int.valueOf(n)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def saturatedSubtract(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.saturatedSubtract(long,long)"""
        return int.__wrap(__LongMath.saturatedSubtract(__long.valueOf(a), __long.valueOf(b)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def log10(x: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.LongMath.log10(long,java.math.RoundingMode)"""
        return int.__wrap(__LongMath.log10(__long.valueOf(x), mode))

    @staticmethod
    @overload
    def binomial(n: int, k: int) -> int:
        """public static long com.google.common.math.LongMath.binomial(int,int)"""
        return int.__wrap(__LongMath.binomial(__int.valueOf(n), __int.valueOf(k)))

    @staticmethod
    @overload
    def saturatedAdd(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.saturatedAdd(long,long)"""
        return int.__wrap(__LongMath.saturatedAdd(__long.valueOf(a), __long.valueOf(b)))

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
    def mod(x: int, m: int) -> int:
        """public static int com.google.common.math.LongMath.mod(long,int)"""
        return int.__wrap(__LongMath.mod(__long.valueOf(x), __int.valueOf(m)))

    @staticmethod
    @overload
    def log2(x: int, mode: 'RoundingMode') -> int:
        """public static int com.google.common.math.LongMath.log2(long,java.math.RoundingMode)"""
        return int.__wrap(__LongMath.log2(__long.valueOf(x), mode))

    @staticmethod
    @overload
    def roundToDouble(x: int, mode: 'RoundingMode') -> float:
        """public static double com.google.common.math.LongMath.roundToDouble(long,java.math.RoundingMode)"""
        return float.__wrap(__LongMath.roundToDouble(__long.valueOf(x), mode))

    @staticmethod
    @overload
    def saturatedPow(b: int, k: int) -> int:
        """public static long com.google.common.math.LongMath.saturatedPow(long,int)"""
        return int.__wrap(__LongMath.saturatedPow(__long.valueOf(b), __int.valueOf(k)))

    @staticmethod
    @overload
    def checkedAdd(a: int, b: int) -> int:
        """public static long com.google.common.math.LongMath.checkedAdd(long,long)"""
        return int.__wrap(__LongMath.checkedAdd(__long.valueOf(a), __long.valueOf(b)))

    @staticmethod
    @overload
    def ceilingPowerOfTwo(x: int) -> int:
        """public static long com.google.common.math.LongMath.ceilingPowerOfTwo(long)"""
        return int.__wrap(__LongMath.ceilingPowerOfTwo(__long.valueOf(x)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.math.StatsAccumulator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import java.util.Iterator as Iterator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.stream.LongStream as LongStream
import java.lang.String as __String
__String = __String
import com.google.common.math.StatsAccumulator as __StatsAccumulator
__StatsAccumulator = __StatsAccumulator
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.DoubleStream as DoubleStream
import java.lang.Double as __double
import java.util.stream.IntStream as IntStream
import com.google.common.math.Stats as __Stats
__Stats = __Stats
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StatsAccumulator():
    """com.google.common.math.StatsAccumulator"""
 
    @staticmethod
    def __wrap(java_value: __StatsAccumulator) -> 'StatsAccumulator':
        return StatsAccumulator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StatsAccumulator):
        """
        Dynamic initializer for StatsAccumulator.
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
    def sampleStandardDeviation(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.sampleStandardDeviation()"""
        return float.__wrap(super(StatsAccumulator, self).sampleStandardDeviation())

    @overload
    def addAll(self, values: 'Iterable'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.lang.Iterable<? extends java.lang.Number>)"""
        super(__StatsAccumulator, self).addAll(values)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def max(self) -> float:
        """public double com.google.common.math.StatsAccumulator.max()"""
        return float.__wrap(super(StatsAccumulator, self).max())

    @overload
    def addAll(self, values: 'IntStream'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.stream.IntStream)"""
        super(__StatsAccumulator, self).addAll(values)

    @overload
    def sampleVariance(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.sampleVariance()"""
        return float.__wrap(super(StatsAccumulator, self).sampleVariance())

    @overload
    def addAll(self, values: 'DoubleStream'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.stream.DoubleStream)"""
        super(__StatsAccumulator, self).addAll(values)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def count(self) -> int:
        """public long com.google.common.math.StatsAccumulator.count()"""
        return int.__wrap(super(StatsAccumulator, self).count())

    @overload
    def populationStandardDeviation(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.populationStandardDeviation()"""
        return float.__wrap(super(StatsAccumulator, self).populationStandardDeviation())

    @overload
    def sum(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.sum()"""
        return float.__wrap(super(StatsAccumulator, self).sum())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def addAll(self, values: 'Stats'):
        """public void com.google.common.math.StatsAccumulator.addAll(com.google.common.math.Stats)"""
        super(__StatsAccumulator, self).addAll(values)

    @overload
    def populationVariance(self) -> float:
        """public final double com.google.common.math.StatsAccumulator.populationVariance()"""
        return float.__wrap(super(StatsAccumulator, self).populationVariance())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addAll(self, *values: float):
        """public void com.google.common.math.StatsAccumulator.addAll(double...)"""
        super(__StatsAccumulator, self).addAll(values)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def addAll(self, values: 'LongStream'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.stream.LongStream)"""
        super(__StatsAccumulator, self).addAll(values)

    @overload
    def addAll(self, *values: int):
        """public void com.google.common.math.StatsAccumulator.addAll(long...)"""
        super(__StatsAccumulator, self).addAll(values)

    @overload
    def add(self, value: float):
        """public void com.google.common.math.StatsAccumulator.add(double)"""
        super(__StatsAccumulator, self).add(__double.valueOf(value))

    @overload
    def addAll(self, values: 'StatsAccumulator'):
        """public void com.google.common.math.StatsAccumulator.addAll(com.google.common.math.StatsAccumulator)"""
        super(__StatsAccumulator, self).addAll(values)

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
        """public com.google.common.math.StatsAccumulator()"""
        val = __StatsAccumulator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def snapshot(self) -> 'Stats':
        """public com.google.common.math.Stats com.google.common.math.StatsAccumulator.snapshot()"""
        return 'Stats'.__wrap(super(StatsAccumulator, self).snapshot())

    @overload
    def addAll(self, *values: int):
        """public void com.google.common.math.StatsAccumulator.addAll(int...)"""
        super(__StatsAccumulator, self).addAll(values)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def min(self) -> float:
        """public double com.google.common.math.StatsAccumulator.min()"""
        return float.__wrap(super(StatsAccumulator, self).min())

    @overload
    def mean(self) -> float:
        """public double com.google.common.math.StatsAccumulator.mean()"""
        return float.__wrap(super(StatsAccumulator, self).mean())

    @overload
    def addAll(self, values: 'Iterator'):
        """public void com.google.common.math.StatsAccumulator.addAll(java.util.Iterator<? extends java.lang.Number>)"""
        super(__StatsAccumulator, self).addAll(values)

    @overload
    def __init__(self):
        """public com.google.common.math.StatsAccumulator()"""
        val = __StatsAccumulator()
        self.__dict__ = val.__dict__
        self.__wrapper = val