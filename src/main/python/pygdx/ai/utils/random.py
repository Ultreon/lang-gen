from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.utils.random.LongDistribution as _LongDistribution
_LongDistribution = _LongDistribution
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.Distribution as _Distribution
_Distribution = _Distribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LongDistribution():
    """com.badlogic.gdx.ai.utils.random.LongDistribution"""
 
    @staticmethod
    def _wrap(java_value: _LongDistribution) -> 'LongDistribution':
        return LongDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongDistribution):
        """
        Dynamic initializer for LongDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongDistribution__wrapper":
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
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @abstractmethod
    def nextLong(self, ):
        """public abstract long com.badlogic.gdx.ai.utils.random.Distribution.nextLong()"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.random.LongDistribution()"""
        val = _LongDistribution()
        self.__wrapper = val

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.LongDistribution.nextDouble()"""
        return float._wrap(super(LongDistribution, self).nextDouble())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.LongDistribution.nextFloat()"""
        return float._wrap(super(LongDistribution, self).nextFloat())

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
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.LongDistribution.nextInt()"""
        return int._wrap(super(LongDistribution, self).nextInt())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.random.LongDistribution()"""
        val = _LongDistribution()
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

 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.LongDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.utils.random.LongDistribution as _LongDistribution
_LongDistribution = _LongDistribution
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.Distribution as _Distribution
_Distribution = _Distribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LongDistribution():
    """com.badlogic.gdx.ai.utils.random.LongDistribution"""
 
    @staticmethod
    def _wrap(java_value: _LongDistribution) -> 'LongDistribution':
        return LongDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongDistribution):
        """
        Dynamic initializer for LongDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongDistribution__wrapper":
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
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @abstractmethod
    def nextLong(self, ):
        """public abstract long com.badlogic.gdx.ai.utils.random.Distribution.nextLong()"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.random.LongDistribution()"""
        val = _LongDistribution()
        self.__wrapper = val

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.LongDistribution.nextDouble()"""
        return float._wrap(super(LongDistribution, self).nextDouble())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.LongDistribution.nextFloat()"""
        return float._wrap(super(LongDistribution, self).nextFloat())

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
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.LongDistribution.nextInt()"""
        return int._wrap(super(LongDistribution, self).nextInt())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.random.LongDistribution()"""
        val = _LongDistribution()
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

 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.LongDistribution 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.DoubleDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.Distribution as _Distribution
_Distribution = _Distribution
import com.badlogic.gdx.ai.utils.random.DoubleDistribution as _DoubleDistribution
_DoubleDistribution = _DoubleDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DoubleDistribution():
    """com.badlogic.gdx.ai.utils.random.DoubleDistribution"""
 
    @staticmethod
    def _wrap(java_value: _DoubleDistribution) -> 'DoubleDistribution':
        return DoubleDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleDistribution):
        """
        Dynamic initializer for DoubleDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.random.DoubleDistribution()"""
        val = _DoubleDistribution()
        self.__wrapper = val

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

    @abstractmethod
    def nextDouble(self, ):
        """public abstract double com.badlogic.gdx.ai.utils.random.Distribution.nextDouble()"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextInt()"""
        return int._wrap(super(DoubleDistribution, self).nextInt())

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.random.DoubleDistribution()"""
        val = _DoubleDistribution()
        self.__wrapper = val

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextLong()"""
        return int._wrap(super(DoubleDistribution, self).nextLong())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextFloat()"""
        return float._wrap(super(DoubleDistribution, self).nextFloat())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution
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
import com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution as _ConstantDoubleDistribution
_ConstantDoubleDistribution = _ConstantDoubleDistribution
import com.badlogic.gdx.ai.utils.random.DoubleDistribution as _DoubleDistribution
_DoubleDistribution = _DoubleDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConstantDoubleDistribution():
    """com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution"""
 
    @staticmethod
    def _wrap(java_value: _ConstantDoubleDistribution) -> 'ConstantDoubleDistribution':
        return ConstantDoubleDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstantDoubleDistribution):
        """
        Dynamic initializer for ConstantDoubleDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstantDoubleDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstantDoubleDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getValue(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution.getValue()"""
        return float._wrap(super(ConstantDoubleDistribution, self).getValue())

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
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextInt()"""
        return int._wrap(super(DoubleDistribution, self).nextInt())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution.nextDouble()"""
        return float._wrap(super(ConstantDoubleDistribution, self).nextDouble())

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
        """public com.badlogic.gdx.ai.utils.random.ConstantDoubleDistribution(double)"""
        val = _ConstantDoubleDistribution(_double.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextLong()"""
        return int._wrap(super(DoubleDistribution, self).nextLong())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextFloat()"""
        return float._wrap(super(DoubleDistribution, self).nextFloat())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution as _TriangularFloatDistribution
_TriangularFloatDistribution = _TriangularFloatDistribution
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.FloatDistribution as _FloatDistribution
_FloatDistribution = _FloatDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TriangularFloatDistribution():
    """com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution"""
 
    @staticmethod
    def _wrap(java_value: _TriangularFloatDistribution) -> 'TriangularFloatDistribution':
        return TriangularFloatDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TriangularFloatDistribution):
        """
        Dynamic initializer for TriangularFloatDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TriangularFloatDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TriangularFloatDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.FloatDistribution.nextInt()"""
        return int._wrap(super(FloatDistribution, self).nextInt())

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution(float)"""
        val = _TriangularFloatDistribution(_float.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getMode(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution.getMode()"""
        return float._wrap(super(TriangularFloatDistribution, self).getMode())

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
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution(float,float,float)"""
        val = _TriangularFloatDistribution(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.FloatDistribution.nextLong()"""
        return int._wrap(super(FloatDistribution, self).nextLong())

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
    def getLow(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution.getLow()"""
        return float._wrap(super(TriangularFloatDistribution, self).getLow())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution.nextFloat()"""
        return float._wrap(super(TriangularFloatDistribution, self).nextFloat())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution(float,float)"""
        val = _TriangularFloatDistribution(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.FloatDistribution.nextDouble()"""
        return float._wrap(super(FloatDistribution, self).nextDouble())

    @overload
    def getHigh(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.TriangularFloatDistribution.getHigh()"""
        return float._wrap(super(TriangularFloatDistribution, self).getHigh())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.FloatDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.FloatDistribution as _FloatDistribution
_FloatDistribution = _FloatDistribution
import com.badlogic.gdx.ai.utils.random.Distribution as _Distribution
_Distribution = _Distribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatDistribution():
    """com.badlogic.gdx.ai.utils.random.FloatDistribution"""
 
    @staticmethod
    def _wrap(java_value: _FloatDistribution) -> 'FloatDistribution':
        return FloatDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatDistribution):
        """
        Dynamic initializer for FloatDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.FloatDistribution.nextInt()"""
        return int._wrap(super(FloatDistribution, self).nextInt())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.random.FloatDistribution()"""
        val = _FloatDistribution()
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.random.FloatDistribution()"""
        val = _FloatDistribution()
        self.__wrapper = val

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.FloatDistribution.nextLong()"""
        return int._wrap(super(FloatDistribution, self).nextLong())

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
    def nextFloat(self, ):
        """public abstract float com.badlogic.gdx.ai.utils.random.Distribution.nextFloat()"""
        pass

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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.FloatDistribution.nextDouble()"""
        return float._wrap(super(FloatDistribution, self).nextDouble())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.UniformFloatDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.utils.random.UniformFloatDistribution as _UniformFloatDistribution
_UniformFloatDistribution = _UniformFloatDistribution
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.FloatDistribution as _FloatDistribution
_FloatDistribution = _FloatDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UniformFloatDistribution():
    """com.badlogic.gdx.ai.utils.random.UniformFloatDistribution"""
 
    @staticmethod
    def _wrap(java_value: _UniformFloatDistribution) -> 'UniformFloatDistribution':
        return UniformFloatDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UniformFloatDistribution):
        """
        Dynamic initializer for UniformFloatDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UniformFloatDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UniformFloatDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.FloatDistribution.nextInt()"""
        return int._wrap(super(FloatDistribution, self).nextInt())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.UniformFloatDistribution(float,float)"""
        val = _UniformFloatDistribution(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

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
    def getHigh(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.UniformFloatDistribution.getHigh()"""
        return float._wrap(super(UniformFloatDistribution, self).getHigh())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.FloatDistribution.nextLong()"""
        return int._wrap(super(FloatDistribution, self).nextLong())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getLow(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.UniformFloatDistribution.getLow()"""
        return float._wrap(super(UniformFloatDistribution, self).getLow())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.UniformFloatDistribution.nextFloat()"""
        return float._wrap(super(UniformFloatDistribution, self).nextFloat())

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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.FloatDistribution.nextDouble()"""
        return float._wrap(super(FloatDistribution, self).nextDouble())

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.utils.random.UniformFloatDistribution(float)"""
        val = _UniformFloatDistribution(_float.valueOf(arg0))
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
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.IntegerDistribution
import com.badlogic.gdx.ai.utils.random.IntegerDistribution as _IntegerDistribution
_IntegerDistribution = _IntegerDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.Distribution as _Distribution
_Distribution = _Distribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntegerDistribution():
    """com.badlogic.gdx.ai.utils.random.IntegerDistribution"""
 
    @staticmethod
    def _wrap(java_value: _IntegerDistribution) -> 'IntegerDistribution':
        return IntegerDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntegerDistribution):
        """
        Dynamic initializer for IntegerDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntegerDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntegerDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def nextInt(self, ):
        """public abstract int com.badlogic.gdx.ai.utils.random.Distribution.nextInt()"""
        pass

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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextDouble()"""
        return float._wrap(super(IntegerDistribution, self).nextDouble())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextFloat()"""
        return float._wrap(super(IntegerDistribution, self).nextFloat())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.utils.random.IntegerDistribution()"""
        val = _IntegerDistribution()
        self.__wrapper = val

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
    def __init__(self):
        """public com.badlogic.gdx.ai.utils.random.IntegerDistribution()"""
        val = _IntegerDistribution()
        self.__wrapper = val

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextLong()"""
        return int._wrap(super(IntegerDistribution, self).nextLong())

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
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution as _TriangularDoubleDistribution
_TriangularDoubleDistribution = _TriangularDoubleDistribution
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.DoubleDistribution as _DoubleDistribution
_DoubleDistribution = _DoubleDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TriangularDoubleDistribution():
    """com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution"""
 
    @staticmethod
    def _wrap(java_value: _TriangularDoubleDistribution) -> 'TriangularDoubleDistribution':
        return TriangularDoubleDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TriangularDoubleDistribution):
        """
        Dynamic initializer for TriangularDoubleDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TriangularDoubleDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TriangularDoubleDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getLow(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution.getLow()"""
        return float._wrap(super(TriangularDoubleDistribution, self).getLow())

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution(double)"""
        val = _TriangularDoubleDistribution(_double.valueOf(arg0))
        self.__wrapper = val

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
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextInt()"""
        return int._wrap(super(DoubleDistribution, self).nextInt())

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution.nextDouble()"""
        return float._wrap(super(TriangularDoubleDistribution, self).nextDouble())

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
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution(double,double)"""
        val = _TriangularDoubleDistribution(_double.valueOf(arg0), _double.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getMode(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution.getMode()"""
        return float._wrap(super(TriangularDoubleDistribution, self).getMode())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextLong()"""
        return int._wrap(super(DoubleDistribution, self).nextLong())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution(double,double,double)"""
        val = _TriangularDoubleDistribution(_double.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getHigh(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.TriangularDoubleDistribution.getHigh()"""
        return float._wrap(super(TriangularDoubleDistribution, self).getHigh())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextFloat()"""
        return float._wrap(super(DoubleDistribution, self).nextFloat())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution
import com.badlogic.gdx.ai.utils.random.IntegerDistribution as _IntegerDistribution
_IntegerDistribution = _IntegerDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution as _UniformIntegerDistribution
_UniformIntegerDistribution = _UniformIntegerDistribution
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UniformIntegerDistribution():
    """com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution"""
 
    @staticmethod
    def _wrap(java_value: _UniformIntegerDistribution) -> 'UniformIntegerDistribution':
        return UniformIntegerDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UniformIntegerDistribution):
        """
        Dynamic initializer for UniformIntegerDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UniformIntegerDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UniformIntegerDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution(int)"""
        val = _UniformIntegerDistribution(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def getHigh(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution.getHigh()"""
        return int._wrap(super(UniformIntegerDistribution, self).getHigh())

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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextDouble()"""
        return float._wrap(super(IntegerDistribution, self).nextDouble())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution.nextInt()"""
        return int._wrap(super(UniformIntegerDistribution, self).nextInt())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextFloat()"""
        return float._wrap(super(IntegerDistribution, self).nextFloat())

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
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution(int,int)"""
        val = _UniformIntegerDistribution(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextLong()"""
        return int._wrap(super(IntegerDistribution, self).nextLong())

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
    def getLow(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.UniformIntegerDistribution.getLow()"""
        return int._wrap(super(UniformIntegerDistribution, self).getLow())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution as _GaussianFloatDistribution
_GaussianFloatDistribution = _GaussianFloatDistribution
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.FloatDistribution as _FloatDistribution
_FloatDistribution = _FloatDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GaussianFloatDistribution():
    """com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution"""
 
    @staticmethod
    def _wrap(java_value: _GaussianFloatDistribution) -> 'GaussianFloatDistribution':
        return GaussianFloatDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GaussianFloatDistribution):
        """
        Dynamic initializer for GaussianFloatDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GaussianFloatDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GaussianFloatDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.FloatDistribution.nextInt()"""
        return int._wrap(super(FloatDistribution, self).nextInt())

    @overload
    def getStandardDeviation(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution.getStandardDeviation()"""
        return float._wrap(super(GaussianFloatDistribution, self).getStandardDeviation())

    @overload
    def getMean(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution.getMean()"""
        return float._wrap(super(GaussianFloatDistribution, self).getMean())

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
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution.nextFloat()"""
        return float._wrap(super(GaussianFloatDistribution, self).nextFloat())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.FloatDistribution.nextLong()"""
        return int._wrap(super(FloatDistribution, self).nextLong())

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

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.FloatDistribution.nextDouble()"""
        return float._wrap(super(FloatDistribution, self).nextDouble())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.GaussianFloatDistribution(float,float)"""
        val = _GaussianFloatDistribution(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution
import com.badlogic.gdx.ai.utils.random.IntegerDistribution as _IntegerDistribution
_IntegerDistribution = _IntegerDistribution
from builtins import str
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
import com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution as _TriangularIntegerDistribution
_TriangularIntegerDistribution = _TriangularIntegerDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TriangularIntegerDistribution():
    """com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution"""
 
    @staticmethod
    def _wrap(java_value: _TriangularIntegerDistribution) -> 'TriangularIntegerDistribution':
        return TriangularIntegerDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TriangularIntegerDistribution):
        """
        Dynamic initializer for TriangularIntegerDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TriangularIntegerDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TriangularIntegerDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution(int)"""
        val = _TriangularIntegerDistribution(_int.valueOf(arg0))
        self.__wrapper = val

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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextDouble()"""
        return float._wrap(super(IntegerDistribution, self).nextDouble())

    @overload
    def getLow(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution.getLow()"""
        return int._wrap(super(TriangularIntegerDistribution, self).getLow())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextFloat()"""
        return float._wrap(super(IntegerDistribution, self).nextFloat())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution(int,int)"""
        val = _TriangularIntegerDistribution(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getMode(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution.getMode()"""
        return float._wrap(super(TriangularIntegerDistribution, self).getMode())

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
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextLong()"""
        return int._wrap(super(IntegerDistribution, self).nextLong())

    @overload
    def getHigh(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution.getHigh()"""
        return int._wrap(super(TriangularIntegerDistribution, self).getHigh())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution(int,int,float)"""
        val = _TriangularIntegerDistribution(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.TriangularIntegerDistribution.nextInt()"""
        return int._wrap(super(TriangularIntegerDistribution, self).nextInt())

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
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.ConstantLongDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.utils.random.ConstantLongDistribution as _ConstantLongDistribution
_ConstantLongDistribution = _ConstantLongDistribution
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.utils.random.LongDistribution as _LongDistribution
_LongDistribution = _LongDistribution
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConstantLongDistribution():
    """com.badlogic.gdx.ai.utils.random.ConstantLongDistribution"""
 
    @staticmethod
    def _wrap(java_value: _ConstantLongDistribution) -> 'ConstantLongDistribution':
        return ConstantLongDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstantLongDistribution):
        """
        Dynamic initializer for ConstantLongDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstantLongDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstantLongDistribution__wrapper":
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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.LongDistribution.nextDouble()"""
        return float._wrap(super(LongDistribution, self).nextDouble())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.LongDistribution.nextFloat()"""
        return float._wrap(super(LongDistribution, self).nextFloat())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.ConstantLongDistribution.nextLong()"""
        return int._wrap(super(ConstantLongDistribution, self).nextLong())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.LongDistribution.nextInt()"""
        return int._wrap(super(LongDistribution, self).nextInt())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.ConstantLongDistribution(long)"""
        val = _ConstantLongDistribution(_long.valueOf(arg0))
        self.__wrapper = val

    @overload
    def getValue(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.ConstantLongDistribution.getValue()"""
        return int._wrap(super(ConstantLongDistribution, self).getValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.Distribution
import com.badlogic.gdx.ai.utils.random.Distribution as _Distribution
_Distribution = _Distribution
from abc import abstractmethod, ABC
 
class Distribution():
    """com.badlogic.gdx.ai.utils.random.Distribution"""
 
    @staticmethod
    def _wrap(java_value: _Distribution) -> 'Distribution':
        return Distribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Distribution):
        """
        Dynamic initializer for Distribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Distribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Distribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution
from builtins import str
import java.lang.Double as _double
import com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution as _GaussianDoubleDistribution
_GaussianDoubleDistribution = _GaussianDoubleDistribution
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.DoubleDistribution as _DoubleDistribution
_DoubleDistribution = _DoubleDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GaussianDoubleDistribution():
    """com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution"""
 
    @staticmethod
    def _wrap(java_value: _GaussianDoubleDistribution) -> 'GaussianDoubleDistribution':
        return GaussianDoubleDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GaussianDoubleDistribution):
        """
        Dynamic initializer for GaussianDoubleDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GaussianDoubleDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GaussianDoubleDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getStandardDeviation(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution.getStandardDeviation()"""
        return float._wrap(super(GaussianDoubleDistribution, self).getStandardDeviation())

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
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextInt()"""
        return int._wrap(super(DoubleDistribution, self).nextInt())

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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution.nextDouble()"""
        return float._wrap(super(GaussianDoubleDistribution, self).nextDouble())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextLong()"""
        return int._wrap(super(DoubleDistribution, self).nextLong())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextFloat()"""
        return float._wrap(super(DoubleDistribution, self).nextFloat())

    @overload
    def getMean(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution.getMean()"""
        return float._wrap(super(GaussianDoubleDistribution, self).getMean())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.GaussianDoubleDistribution(double,double)"""
        val = _GaussianDoubleDistribution(_double.valueOf(arg0), _double.valueOf(arg1))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution
import com.badlogic.gdx.ai.utils.random.IntegerDistribution as _IntegerDistribution
_IntegerDistribution = _IntegerDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution as _ConstantIntegerDistribution
_ConstantIntegerDistribution = _ConstantIntegerDistribution
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConstantIntegerDistribution():
    """com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution"""
 
    @staticmethod
    def _wrap(java_value: _ConstantIntegerDistribution) -> 'ConstantIntegerDistribution':
        return ConstantIntegerDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstantIntegerDistribution):
        """
        Dynamic initializer for ConstantIntegerDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstantIntegerDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstantIntegerDistribution__wrapper":
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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextDouble()"""
        return float._wrap(super(IntegerDistribution, self).nextDouble())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextFloat()"""
        return float._wrap(super(IntegerDistribution, self).nextFloat())

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
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.IntegerDistribution.nextLong()"""
        return int._wrap(super(IntegerDistribution, self).nextLong())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution.nextInt()"""
        return int._wrap(super(ConstantIntegerDistribution, self).nextInt())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getValue(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution.getValue()"""
        return int._wrap(super(ConstantIntegerDistribution, self).getValue())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.ConstantIntegerDistribution(int)"""
        val = _ConstantIntegerDistribution(_int.valueOf(arg0))
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
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution
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
import com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution as _UniformDoubleDistribution
_UniformDoubleDistribution = _UniformDoubleDistribution
import com.badlogic.gdx.ai.utils.random.DoubleDistribution as _DoubleDistribution
_DoubleDistribution = _DoubleDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UniformDoubleDistribution():
    """com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution"""
 
    @staticmethod
    def _wrap(java_value: _UniformDoubleDistribution) -> 'UniformDoubleDistribution':
        return UniformDoubleDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UniformDoubleDistribution):
        """
        Dynamic initializer for UniformDoubleDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UniformDoubleDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UniformDoubleDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getHigh(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution.getHigh()"""
        return float._wrap(super(UniformDoubleDistribution, self).getHigh())

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution(double)"""
        val = _UniformDoubleDistribution(_double.valueOf(arg0))
        self.__wrapper = val

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
    def getLow(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution.getLow()"""
        return float._wrap(super(UniformDoubleDistribution, self).getLow())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextInt()"""
        return int._wrap(super(DoubleDistribution, self).nextInt())

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution.nextDouble()"""
        return float._wrap(super(UniformDoubleDistribution, self).nextDouble())

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
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.ai.utils.random.UniformDoubleDistribution(double,double)"""
        val = _UniformDoubleDistribution(_double.valueOf(arg0), _double.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextLong()"""
        return int._wrap(super(DoubleDistribution, self).nextLong())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.DoubleDistribution.nextFloat()"""
        return float._wrap(super(DoubleDistribution, self).nextFloat())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.TriangularLongDistribution
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
import com.badlogic.gdx.ai.utils.random.LongDistribution as _LongDistribution
_LongDistribution = _LongDistribution
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.TriangularLongDistribution as _TriangularLongDistribution
_TriangularLongDistribution = _TriangularLongDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TriangularLongDistribution():
    """com.badlogic.gdx.ai.utils.random.TriangularLongDistribution"""
 
    @staticmethod
    def _wrap(java_value: _TriangularLongDistribution) -> 'TriangularLongDistribution':
        return TriangularLongDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TriangularLongDistribution):
        """
        Dynamic initializer for TriangularLongDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TriangularLongDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TriangularLongDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getMode(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.TriangularLongDistribution.getMode()"""
        return float._wrap(super(TriangularLongDistribution, self).getMode())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.TriangularLongDistribution.nextLong()"""
        return int._wrap(super(TriangularLongDistribution, self).nextLong())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public com.badlogic.gdx.ai.utils.random.TriangularLongDistribution(long,long,double)"""
        val = _TriangularLongDistribution(_long.valueOf(arg0), _long.valueOf(arg1), _double.valueOf(arg2))
        self.__wrapper = val

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
    def getLow(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.TriangularLongDistribution.getLow()"""
        return int._wrap(super(TriangularLongDistribution, self).getLow())

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
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.LongDistribution.nextDouble()"""
        return float._wrap(super(LongDistribution, self).nextDouble())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.ai.utils.random.TriangularLongDistribution(long,long)"""
        val = _TriangularLongDistribution(_long.valueOf(arg0), _long.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.TriangularLongDistribution(long)"""
        val = _TriangularLongDistribution(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.LongDistribution.nextFloat()"""
        return float._wrap(super(LongDistribution, self).nextFloat())

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
    def getHigh(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.TriangularLongDistribution.getHigh()"""
        return int._wrap(super(TriangularLongDistribution, self).getHigh())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.LongDistribution.nextInt()"""
        return int._wrap(super(LongDistribution, self).nextInt())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.UniformLongDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.utils.random.UniformLongDistribution as _UniformLongDistribution
_UniformLongDistribution = _UniformLongDistribution
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.utils.random.LongDistribution as _LongDistribution
_LongDistribution = _LongDistribution
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UniformLongDistribution():
    """com.badlogic.gdx.ai.utils.random.UniformLongDistribution"""
 
    @staticmethod
    def _wrap(java_value: _UniformLongDistribution) -> 'UniformLongDistribution':
        return UniformLongDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UniformLongDistribution):
        """
        Dynamic initializer for UniformLongDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UniformLongDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UniformLongDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.ai.utils.random.UniformLongDistribution(long,long)"""
        val = _UniformLongDistribution(_long.valueOf(arg0), _long.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getHigh(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.UniformLongDistribution.getHigh()"""
        return int._wrap(super(UniformLongDistribution, self).getHigh())

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
    def getLow(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.UniformLongDistribution.getLow()"""
        return int._wrap(super(UniformLongDistribution, self).getLow())

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.LongDistribution.nextDouble()"""
        return float._wrap(super(LongDistribution, self).nextDouble())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.utils.random.UniformLongDistribution(long)"""
        val = _UniformLongDistribution(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.LongDistribution.nextFloat()"""
        return float._wrap(super(LongDistribution, self).nextFloat())

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
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.LongDistribution.nextInt()"""
        return int._wrap(super(LongDistribution, self).nextInt())

    @override
    @overload
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.UniformLongDistribution.nextLong()"""
        return int._wrap(super(UniformLongDistribution, self).nextLong())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution as _ConstantFloatDistribution
_ConstantFloatDistribution = _ConstantFloatDistribution
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.random.FloatDistribution as _FloatDistribution
_FloatDistribution = _FloatDistribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConstantFloatDistribution():
    """com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution"""
 
    @staticmethod
    def _wrap(java_value: _ConstantFloatDistribution) -> 'ConstantFloatDistribution':
        return ConstantFloatDistribution(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstantFloatDistribution):
        """
        Dynamic initializer for ConstantFloatDistribution.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstantFloatDistribution__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstantFloatDistribution__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def nextFloat(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution.nextFloat()"""
        return float._wrap(super(ConstantFloatDistribution, self).nextFloat())

    @override
    @overload
    def nextInt(self) -> int:
        """public int com.badlogic.gdx.ai.utils.random.FloatDistribution.nextInt()"""
        return int._wrap(super(FloatDistribution, self).nextInt())

    @overload
    def getValue(self) -> float:
        """public float com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution.getValue()"""
        return float._wrap(super(ConstantFloatDistribution, self).getValue())

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
    def nextLong(self) -> int:
        """public long com.badlogic.gdx.ai.utils.random.FloatDistribution.nextLong()"""
        return int._wrap(super(FloatDistribution, self).nextLong())

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
        """public com.badlogic.gdx.ai.utils.random.ConstantFloatDistribution(float)"""
        val = _ConstantFloatDistribution(_float.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def nextDouble(self) -> float:
        """public double com.badlogic.gdx.ai.utils.random.FloatDistribution.nextDouble()"""
        return float._wrap(super(FloatDistribution, self).nextDouble())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())