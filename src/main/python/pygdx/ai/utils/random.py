from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.utils.random.Distribution as __Distribution
__Distribution = __Distribution
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.utils.random.FloatDistribution as __FloatDistribution
__FloatDistribution = __FloatDistribution
from abc import abstractmethod, ABC
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
 
class FloatDistribution(ABC):
    """com.badlogic.gdx.ai.utils.random.FloatDistribution"""
 
    @staticmethod
    def __wrap(java_value: __FloatDistribution) -> 'FloatDistribution':
        return FloatDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatDistribution):
        """
        Dynamic initializer for FloatDistribution.
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
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.FloatDistribution.nextLong()"""
        return int.__wrap(super(FloatDistribution, self).nextLong())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.random.FloatDistribution()"""
        val = __FloatDistribution()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.random.FloatDistribution()"""
        val = __FloatDistribution()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.FloatDistribution.nextDouble()"""
        return float.__wrap(super(FloatDistribution, self).nextDouble())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def nextFloat(self, ):
        """public abstract float com.badlogic.gdx.ai.utils.random.Distribution.nextFloat()"""
        pass

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.FloatDistribution.nextInt()"""
        return int.__wrap(super(FloatDistribution, self).nextInt())

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

 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.FloatDistribution
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.utils.random.Distribution as __Distribution
__Distribution = __Distribution
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.utils.random.FloatDistribution as __FloatDistribution
__FloatDistribution = __FloatDistribution
from abc import abstractmethod, ABC
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
 
class FloatDistribution(ABC):
    """com.badlogic.gdx.ai.utils.random.FloatDistribution"""
 
    @staticmethod
    def __wrap(java_value: __FloatDistribution) -> 'FloatDistribution':
        return FloatDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatDistribution):
        """
        Dynamic initializer for FloatDistribution.
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
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.FloatDistribution.nextLong()"""
        return int.__wrap(super(FloatDistribution, self).nextLong())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.random.FloatDistribution()"""
        val = __FloatDistribution()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.random.FloatDistribution()"""
        val = __FloatDistribution()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.FloatDistribution.nextDouble()"""
        return float.__wrap(super(FloatDistribution, self).nextDouble())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def nextFloat(self, ):
        """public abstract float com.badlogic.gdx.ai.utils.random.Distribution.nextFloat()"""
        pass

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.FloatDistribution.nextInt()"""
        return int.__wrap(super(FloatDistribution, self).nextInt())

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

 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.FloatDistribution 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import com.badlogic.gdx.ai.utils.random.IntegerDistribution as __IntegerDistribution
__IntegerDistribution = __IntegerDistribution
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution as __ConstantIntegerDistribution
__ConstantIntegerDistribution = __ConstantIntegerDistribution
from builtins import bool
from builtins import int
 
class ConstantIntegerDistribution():
    """com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution"""
 
    @staticmethod
    def __wrap(java_value: __ConstantIntegerDistribution) -> 'ConstantIntegerDistribution':
        return ConstantIntegerDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConstantIntegerDistribution):
        """
        Dynamic initializer for ConstantIntegerDistribution.
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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextDouble()"""
        return float.__wrap(super(IntegerDistribution, self).nextDouble())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getValue(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution.getValue()"""
        return int.__wrap(super(ConstantIntegerDistribution, self).getValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution.nextInt()"""
        return int.__wrap(super(ConstantIntegerDistribution, self).nextInt())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextLong()"""
        return int.__wrap(super(IntegerDistribution, self).nextLong())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextFloat()"""
        return float.__wrap(super(IntegerDistribution, self).nextFloat())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution(int)"""
        val = __ConstantIntegerDistribution(__int.valueOf(arg0))
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.UniformFloatDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.utils.random.FloatDistribution as __FloatDistribution
__FloatDistribution = __FloatDistribution
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.utils.random.UniformFloatDistribution as __UniformFloatDistribution
__UniformFloatDistribution = __UniformFloatDistribution
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UniformFloatDistribution():
    """com.badlogic.gdx.ai.utils.random.UniformFloatDistribution"""
 
    @staticmethod
    def __wrap(java_value: __UniformFloatDistribution) -> 'UniformFloatDistribution':
        return UniformFloatDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UniformFloatDistribution):
        """
        Dynamic initializer for UniformFloatDistribution.
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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.utils.random.UniformFloatDistribution(float)"""
        val = __UniformFloatDistribution(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getLow(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.UniformFloatDistribution.getLow()"""
        return float.__wrap(super(UniformFloatDistribution, self).getLow())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.FloatDistribution.nextLong()"""
        return int.__wrap(super(FloatDistribution, self).nextLong())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.UniformFloatDistribution.nextFloat()"""
        return float.__wrap(super(UniformFloatDistribution, self).nextFloat())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getHigh(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.UniformFloatDistribution.getHigh()"""
        return float.__wrap(super(UniformFloatDistribution, self).getHigh())

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
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.UniformFloatDistribution(float,float)"""
        val = __UniformFloatDistribution(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.FloatDistribution.nextDouble()"""
        return float.__wrap(super(FloatDistribution, self).nextDouble())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.FloatDistribution.nextInt()"""
        return int.__wrap(super(FloatDistribution, self).nextInt())

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
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution
import com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution as __UniformIntegerDistribution
__UniformIntegerDistribution = __UniformIntegerDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import com.badlogic.gdx.ai.utils.random.IntegerDistribution as __IntegerDistribution
__IntegerDistribution = __IntegerDistribution
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UniformIntegerDistribution():
    """com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution"""
 
    @staticmethod
    def __wrap(java_value: __UniformIntegerDistribution) -> 'UniformIntegerDistribution':
        return UniformIntegerDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UniformIntegerDistribution):
        """
        Dynamic initializer for UniformIntegerDistribution.
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
    def getLow(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution.getLow()"""
        return int.__wrap(super(UniformIntegerDistribution, self).getLow())

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextDouble()"""
        return float.__wrap(super(IntegerDistribution, self).nextDouble())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution(int,int)"""
        val = __UniformIntegerDistribution(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextLong()"""
        return int.__wrap(super(IntegerDistribution, self).nextLong())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextFloat()"""
        return float.__wrap(super(IntegerDistribution, self).nextFloat())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution(int)"""
        val = __UniformIntegerDistribution(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getHigh(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution.getHigh()"""
        return int.__wrap(super(UniformIntegerDistribution, self).getHigh())

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
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution.nextInt()"""
        return int.__wrap(super(UniformIntegerDistribution, self).nextInt())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution
import com.badlogic.gdx.ai.utils.random.DoubleDistribution as __DoubleDistribution
__DoubleDistribution = __DoubleDistribution
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
import com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution as __ConstantDoubleDistribution
__ConstantDoubleDistribution = __ConstantDoubleDistribution
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class ConstantDoubleDistribution():
    """com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution"""
 
    @staticmethod
    def __wrap(java_value: __ConstantDoubleDistribution) -> 'ConstantDoubleDistribution':
        return ConstantDoubleDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConstantDoubleDistribution):
        """
        Dynamic initializer for ConstantDoubleDistribution.
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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution.nextDouble()"""
        return float.__wrap(super(ConstantDoubleDistribution, self).nextDouble())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution(double)"""
        val = __ConstantDoubleDistribution(__double.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getValue(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution.getValue()"""
        return float.__wrap(super(ConstantDoubleDistribution, self).getValue())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextInt()"""
        return int.__wrap(super(DoubleDistribution, self).nextInt())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextLong()"""
        return int.__wrap(super(DoubleDistribution, self).nextLong())

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
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextFloat()"""
        return float.__wrap(super(DoubleDistribution, self).nextFloat())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.LongDistribution
import com.badlogic.gdx.ai.utils.random.LongDistribution as __LongDistribution
__LongDistribution = __LongDistribution
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.utils.random.Distribution as __Distribution
__Distribution = __Distribution
import java.lang.Object as __object
from builtins import type
from builtins import float
from abc import abstractmethod, ABC
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
 
class LongDistribution(ABC):
    """com.badlogic.gdx.ai.utils.random.LongDistribution"""
 
    @staticmethod
    def __wrap(java_value: __LongDistribution) -> 'LongDistribution':
        return LongDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongDistribution):
        """
        Dynamic initializer for LongDistribution.
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
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.random.LongDistribution()"""
        val = __LongDistribution()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.LongDistribution.nextFloat()"""
        return float.__wrap(super(LongDistribution, self).nextFloat())

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
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.LongDistribution.nextInt()"""
        return int.__wrap(super(LongDistribution, self).nextInt())

    @abstractmethod
    def nextLong(self, ):
        """public abstract long com.badlogic.gdx.ai.utils.random.Distribution.nextLong()"""
        pass

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.LongDistribution.nextDouble()"""
        return float.__wrap(super(LongDistribution, self).nextDouble())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.random.LongDistribution()"""
        val = __LongDistribution()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.UniformLongDistribution
import com.badlogic.gdx.ai.utils.random.LongDistribution as __LongDistribution
__LongDistribution = __LongDistribution
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
import com.badlogic.gdx.ai.utils.random.UniformLongDistribution as __UniformLongDistribution
__UniformLongDistribution = __UniformLongDistribution
from builtins import bool
from builtins import int
 
class UniformLongDistribution():
    """com.badlogic.gdx.ai.utils.random.UniformLongDistribution"""
 
    @staticmethod
    def __wrap(java_value: __UniformLongDistribution) -> 'UniformLongDistribution':
        return UniformLongDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UniformLongDistribution):
        """
        Dynamic initializer for UniformLongDistribution.
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
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.ai.utils.random.UniformLongDistribution(long,long)"""
        val = __UniformLongDistribution(__long.valueOf(arg0), __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.LongDistribution.nextFloat()"""
        return float.__wrap(super(LongDistribution, self).nextFloat())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.UniformLongDistribution.nextLong()"""
        return int.__wrap(super(UniformLongDistribution, self).nextLong())

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
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.LongDistribution.nextInt()"""
        return int.__wrap(super(LongDistribution, self).nextInt())

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
    def getLow(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.UniformLongDistribution.getLow()"""
        return int.__wrap(super(UniformLongDistribution, self).getLow())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.UniformLongDistribution(long)"""
        val = __UniformLongDistribution(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getHigh(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.UniformLongDistribution.getHigh()"""
        return int.__wrap(super(UniformLongDistribution, self).getHigh())

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.LongDistribution.nextDouble()"""
        return float.__wrap(super(LongDistribution, self).nextDouble()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution as __TriangularIntegerDistribution
__TriangularIntegerDistribution = __TriangularIntegerDistribution
from builtins import float
import java.lang.Long as __long
import com.badlogic.gdx.ai.utils.random.IntegerDistribution as __IntegerDistribution
__IntegerDistribution = __IntegerDistribution
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TriangularIntegerDistribution():
    """com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution"""
 
    @staticmethod
    def __wrap(java_value: __TriangularIntegerDistribution) -> 'TriangularIntegerDistribution':
        return TriangularIntegerDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TriangularIntegerDistribution):
        """
        Dynamic initializer for TriangularIntegerDistribution.
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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution(int)"""
        val = __TriangularIntegerDistribution(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getLow(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution.getLow()"""
        return int.__wrap(super(TriangularIntegerDistribution, self).getLow())

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextDouble()"""
        return float.__wrap(super(IntegerDistribution, self).nextDouble())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution(int,int)"""
        val = __TriangularIntegerDistribution(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution.nextInt()"""
        return int.__wrap(super(TriangularIntegerDistribution, self).nextInt())

    @overload
    def getMode(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution.getMode()"""
        return float.__wrap(super(TriangularIntegerDistribution, self).getMode())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextLong()"""
        return int.__wrap(super(IntegerDistribution, self).nextLong())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextFloat()"""
        return float.__wrap(super(IntegerDistribution, self).nextFloat())

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

    @overload
    def getHigh(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution.getHigh()"""
        return int.__wrap(super(TriangularIntegerDistribution, self).getHigh())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution(int,int,float)"""
        val = __TriangularIntegerDistribution(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))
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
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution
import com.badlogic.gdx.ai.utils.random.DoubleDistribution as __DoubleDistribution
__DoubleDistribution = __DoubleDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution as __TriangularDoubleDistribution
__TriangularDoubleDistribution = __TriangularDoubleDistribution
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class TriangularDoubleDistribution():
    """com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution"""
 
    @staticmethod
    def __wrap(java_value: __TriangularDoubleDistribution) -> 'TriangularDoubleDistribution':
        return TriangularDoubleDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TriangularDoubleDistribution):
        """
        Dynamic initializer for TriangularDoubleDistribution.
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
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution(double,double,double)"""
        val = __TriangularDoubleDistribution(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getHigh(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution.getHigh()"""
        return float.__wrap(super(TriangularDoubleDistribution, self).getHigh())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextInt()"""
        return int.__wrap(super(DoubleDistribution, self).nextInt())

    @overload
    def getLow(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution.getLow()"""
        return float.__wrap(super(TriangularDoubleDistribution, self).getLow())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution(double,double)"""
        val = __TriangularDoubleDistribution(__double.valueOf(arg0), __double.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMode(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution.getMode()"""
        return float.__wrap(super(TriangularDoubleDistribution, self).getMode())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextLong()"""
        return int.__wrap(super(DoubleDistribution, self).nextLong())

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution.nextDouble()"""
        return float.__wrap(super(TriangularDoubleDistribution, self).nextDouble())

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

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution(double)"""
        val = __TriangularDoubleDistribution(__double.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextFloat()"""
        return float.__wrap(super(DoubleDistribution, self).nextFloat())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution as __ConstantFloatDistribution
__ConstantFloatDistribution = __ConstantFloatDistribution
from builtins import float
import com.badlogic.gdx.ai.utils.random.FloatDistribution as __FloatDistribution
__FloatDistribution = __FloatDistribution
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ConstantFloatDistribution():
    """com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution"""
 
    @staticmethod
    def __wrap(java_value: __ConstantFloatDistribution) -> 'ConstantFloatDistribution':
        return ConstantFloatDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConstantFloatDistribution):
        """
        Dynamic initializer for ConstantFloatDistribution.
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
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution.nextFloat()"""
        return float.__wrap(super(ConstantFloatDistribution, self).nextFloat())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.FloatDistribution.nextLong()"""
        return int.__wrap(super(FloatDistribution, self).nextLong())

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

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution(float)"""
        val = __ConstantFloatDistribution(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.FloatDistribution.nextDouble()"""
        return float.__wrap(super(FloatDistribution, self).nextDouble())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.FloatDistribution.nextInt()"""
        return int.__wrap(super(FloatDistribution, self).nextInt())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getValue(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution.getValue()"""
        return float.__wrap(super(ConstantFloatDistribution, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.utils.random.FloatDistribution as __FloatDistribution
__FloatDistribution = __FloatDistribution
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution as __TriangularFloatDistribution
__TriangularFloatDistribution = __TriangularFloatDistribution
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TriangularFloatDistribution():
    """com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution"""
 
    @staticmethod
    def __wrap(java_value: __TriangularFloatDistribution) -> 'TriangularFloatDistribution':
        return TriangularFloatDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TriangularFloatDistribution):
        """
        Dynamic initializer for TriangularFloatDistribution.
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
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.FloatDistribution.nextLong()"""
        return int.__wrap(super(FloatDistribution, self).nextLong())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getHigh(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution.getHigh()"""
        return float.__wrap(super(TriangularFloatDistribution, self).getHigh())

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
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution(float,float)"""
        val = __TriangularFloatDistribution(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution.nextFloat()"""
        return float.__wrap(super(TriangularFloatDistribution, self).nextFloat())

    @overload
    def getLow(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution.getLow()"""
        return float.__wrap(super(TriangularFloatDistribution, self).getLow())

    @overload
    def getMode(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution.getMode()"""
        return float.__wrap(super(TriangularFloatDistribution, self).getMode())

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.FloatDistribution.nextDouble()"""
        return float.__wrap(super(FloatDistribution, self).nextDouble())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.FloatDistribution.nextInt()"""
        return int.__wrap(super(FloatDistribution, self).nextInt())

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
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution(float,float,float)"""
        val = __TriangularFloatDistribution(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution(float)"""
        val = __TriangularFloatDistribution(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.IntegerDistribution
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.utils.random.Distribution as __Distribution
__Distribution = __Distribution
import java.lang.Object as __object
from builtins import type
from builtins import float
from abc import abstractmethod, ABC
import java.lang.Long as __long
import com.badlogic.gdx.ai.utils.random.IntegerDistribution as __IntegerDistribution
__IntegerDistribution = __IntegerDistribution
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntegerDistribution(ABC):
    """com.badlogic.gdx.ai.utils.random.IntegerDistribution"""
 
    @staticmethod
    def __wrap(java_value: __IntegerDistribution) -> 'IntegerDistribution':
        return IntegerDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntegerDistribution):
        """
        Dynamic initializer for IntegerDistribution.
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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextDouble()"""
        return float.__wrap(super(IntegerDistribution, self).nextDouble())

    @abstractmethod
    def nextInt(self, ):
        """public abstract int com.badlogic.gdx.ai.utils.random.Distribution.nextInt()"""
        pass

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
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextLong()"""
        return int.__wrap(super(IntegerDistribution, self).nextLong())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextFloat()"""
        return float.__wrap(super(IntegerDistribution, self).nextFloat())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.random.IntegerDistribution()"""
        val = __IntegerDistribution()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.random.IntegerDistribution()"""
        val = __IntegerDistribution()
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
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.TriangularLongDistribution
import com.badlogic.gdx.ai.utils.random.LongDistribution as __LongDistribution
__LongDistribution = __LongDistribution
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
import java.lang.Double as __double
from builtins import bool
import com.badlogic.gdx.ai.utils.random.TriangularLongDistribution as __TriangularLongDistribution
__TriangularLongDistribution = __TriangularLongDistribution
from builtins import int
 
class TriangularLongDistribution():
    """com.badlogic.gdx.ai.utils.random.TriangularLongDistribution"""
 
    @staticmethod
    def __wrap(java_value: __TriangularLongDistribution) -> 'TriangularLongDistribution':
        return TriangularLongDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TriangularLongDistribution):
        """
        Dynamic initializer for TriangularLongDistribution.
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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.TriangularLongDistribution(long)"""
        val = __TriangularLongDistribution(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getMode(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.TriangularLongDistribution.getMode()"""
        return float.__wrap(super(TriangularLongDistribution, self).getMode())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.LongDistribution.nextFloat()"""
        return float.__wrap(super(LongDistribution, self).nextFloat())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getHigh(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.TriangularLongDistribution.getHigh()"""
        return int.__wrap(super(TriangularLongDistribution, self).getHigh())

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
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularLongDistribution(long,long,double)"""
        val = __TriangularLongDistribution(__long.valueOf(arg0), __long.valueOf(arg1), __double.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.LongDistribution.nextInt()"""
        return int.__wrap(super(LongDistribution, self).nextInt())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.ai.utils.random.TriangularLongDistribution(long,long)"""
        val = __TriangularLongDistribution(__long.valueOf(arg0), __long.valueOf(arg1))
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.TriangularLongDistribution.nextLong()"""
        return int.__wrap(super(TriangularLongDistribution, self).nextLong())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getLow(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.TriangularLongDistribution.getLow()"""
        return int.__wrap(super(TriangularLongDistribution, self).getLow())

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.LongDistribution.nextDouble()"""
        return float.__wrap(super(LongDistribution, self).nextDouble()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution
import com.badlogic.gdx.ai.utils.random.DoubleDistribution as __DoubleDistribution
__DoubleDistribution = __DoubleDistribution
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
import com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution as __UniformDoubleDistribution
__UniformDoubleDistribution = __UniformDoubleDistribution
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class UniformDoubleDistribution():
    """com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution"""
 
    @staticmethod
    def __wrap(java_value: __UniformDoubleDistribution) -> 'UniformDoubleDistribution':
        return UniformDoubleDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UniformDoubleDistribution):
        """
        Dynamic initializer for UniformDoubleDistribution.
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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution.nextDouble()"""
        return float.__wrap(super(UniformDoubleDistribution, self).nextDouble())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextInt()"""
        return int.__wrap(super(DoubleDistribution, self).nextInt())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextLong()"""
        return int.__wrap(super(DoubleDistribution, self).nextLong())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution(double)"""
        val = __UniformDoubleDistribution(__double.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getLow(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution.getLow()"""
        return float.__wrap(super(UniformDoubleDistribution, self).getLow())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getHigh(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution.getHigh()"""
        return float.__wrap(super(UniformDoubleDistribution, self).getHigh())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution(double,double)"""
        val = __UniformDoubleDistribution(__double.valueOf(arg0), __double.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextFloat()"""
        return float.__wrap(super(DoubleDistribution, self).nextFloat())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.ConstantLongDistribution
import com.badlogic.gdx.ai.utils.random.LongDistribution as __LongDistribution
__LongDistribution = __LongDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.utils.random.ConstantLongDistribution as __ConstantLongDistribution
__ConstantLongDistribution = __ConstantLongDistribution
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
from builtins import int
 
class ConstantLongDistribution():
    """com.badlogic.gdx.ai.utils.random.ConstantLongDistribution"""
 
    @staticmethod
    def __wrap(java_value: __ConstantLongDistribution) -> 'ConstantLongDistribution':
        return ConstantLongDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConstantLongDistribution):
        """
        Dynamic initializer for ConstantLongDistribution.
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
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.ConstantLongDistribution.nextLong()"""
        return int.__wrap(super(ConstantLongDistribution, self).nextLong())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.LongDistribution.nextFloat()"""
        return float.__wrap(super(LongDistribution, self).nextFloat())

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.ConstantLongDistribution(long)"""
        val = __ConstantLongDistribution(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.LongDistribution.nextInt()"""
        return int.__wrap(super(LongDistribution, self).nextInt())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getValue(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.ConstantLongDistribution.getValue()"""
        return int.__wrap(super(ConstantLongDistribution, self).getValue())

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

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.LongDistribution.nextDouble()"""
        return float.__wrap(super(LongDistribution, self).nextDouble()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.Distribution
import com.badlogic.gdx.ai.utils.random.Distribution as __Distribution
__Distribution = __Distribution
from abc import abstractmethod, ABC
 
class Distribution(ABC):
    """com.badlogic.gdx.ai.utils.random.Distribution"""
 
    @staticmethod
    def __wrap(java_value: __Distribution) -> 'Distribution':
        return Distribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Distribution):
        """
        Dynamic initializer for Distribution.
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
    def nextLong(self, ):
        """public abstract long com.badlogic.gdx.ai.utils.random.Distribution.nextLong()"""
        pass

    @abstractmethod
    def nextInt(self, ):
        """public abstract int com.badlogic.gdx.ai.utils.random.Distribution.nextInt()"""
        pass

    @abstractmethod
    def nextFloat(self, ):
        """public abstract float com.badlogic.gdx.ai.utils.random.Distribution.nextFloat()"""
        pass

    @abstractmethod
    def nextDouble(self, ):
        """public abstract double com.badlogic.gdx.ai.utils.random.Distribution.nextDouble()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.DoubleDistribution
import com.badlogic.gdx.ai.utils.random.DoubleDistribution as __DoubleDistribution
__DoubleDistribution = __DoubleDistribution
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.utils.random.Distribution as __Distribution
__Distribution = __Distribution
import java.lang.Object as __object
from builtins import type
from builtins import float
from abc import abstractmethod, ABC
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
 
class DoubleDistribution(ABC):
    """com.badlogic.gdx.ai.utils.random.DoubleDistribution"""
 
    @staticmethod
    def __wrap(java_value: __DoubleDistribution) -> 'DoubleDistribution':
        return DoubleDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleDistribution):
        """
        Dynamic initializer for DoubleDistribution.
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
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextInt()"""
        return int.__wrap(super(DoubleDistribution, self).nextInt())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def nextDouble(self, ):
        """public abstract double com.badlogic.gdx.ai.utils.random.Distribution.nextDouble()"""
        pass

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.random.DoubleDistribution()"""
        val = __DoubleDistribution()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextLong()"""
        return int.__wrap(super(DoubleDistribution, self).nextLong())

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
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.random.DoubleDistribution()"""
        val = __DoubleDistribution()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextFloat()"""
        return float.__wrap(super(DoubleDistribution, self).nextFloat())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.utils.random.FloatDistribution as __FloatDistribution
__FloatDistribution = __FloatDistribution
import com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution as __GaussianFloatDistribution
__GaussianFloatDistribution = __GaussianFloatDistribution
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GaussianFloatDistribution():
    """com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution"""
 
    @staticmethod
    def __wrap(java_value: __GaussianFloatDistribution) -> 'GaussianFloatDistribution':
        return GaussianFloatDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GaussianFloatDistribution):
        """
        Dynamic initializer for GaussianFloatDistribution.
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
    def getStandardDeviation(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution.getStandardDeviation()"""
        return float.__wrap(super(GaussianFloatDistribution, self).getStandardDeviation())

    @overload
    def getMean(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution.getMean()"""
        return float.__wrap(super(GaussianFloatDistribution, self).getMean())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.FloatDistribution.nextLong()"""
        return int.__wrap(super(FloatDistribution, self).nextLong())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution.nextFloat()"""
        return float.__wrap(super(GaussianFloatDistribution, self).nextFloat())

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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.FloatDistribution.nextDouble()"""
        return float.__wrap(super(FloatDistribution, self).nextDouble())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution(float,float)"""
        val = __GaussianFloatDistribution(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.FloatDistribution.nextInt()"""
        return int.__wrap(super(FloatDistribution, self).nextInt())

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
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution
import com.badlogic.gdx.ai.utils.random.DoubleDistribution as __DoubleDistribution
__DoubleDistribution = __DoubleDistribution
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
import com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution as __GaussianDoubleDistribution
__GaussianDoubleDistribution = __GaussianDoubleDistribution
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class GaussianDoubleDistribution():
    """com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution"""
 
    @staticmethod
    def __wrap(java_value: __GaussianDoubleDistribution) -> 'GaussianDoubleDistribution':
        return GaussianDoubleDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GaussianDoubleDistribution):
        """
        Dynamic initializer for GaussianDoubleDistribution.
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
    def getStandardDeviation(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution.getStandardDeviation()"""
        return float.__wrap(super(GaussianDoubleDistribution, self).getStandardDeviation())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution(double,double)"""
        val = __GaussianDoubleDistribution(__double.valueOf(arg0), __double.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextInt()"""
        return int.__wrap(super(DoubleDistribution, self).nextInt())

    @overload
    def getMean(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution.getMean()"""
        return float.__wrap(super(GaussianDoubleDistribution, self).getMean())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextLong()"""
        return int.__wrap(super(DoubleDistribution, self).nextLong())

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
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextFloat()"""
        return float.__wrap(super(DoubleDistribution, self).nextFloat())

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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution.nextDouble()"""
        return float.__wrap(super(GaussianDoubleDistribution, self).nextDouble())