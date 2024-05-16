from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.rng.JavaRNG as __JavaRNG
__JavaRNG = __JavaRNG
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
import java.util.Random as Random
 
class JavaRNG():
    """dev.ultreon.quantum.world.rng.JavaRNG"""
 
    @staticmethod
    def __wrap(java_value: __JavaRNG) -> 'JavaRNG':
        return JavaRNG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JavaRNG):
        """
        Dynamic initializer for JavaRNG.
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
    def chance(self, arg0: float) -> bool:
        """public boolean dev.ultreon.quantum.world.rng.JavaRNG.chance(float)"""
        return bool.__wrap(super(__JavaRNG, self).chance(__float.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.rng.JavaRNG()"""
        val = __JavaRNG()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextFloat(self) -> float:
        """public float dev.ultreon.quantum.world.rng.JavaRNG.nextFloat()"""
        return float.__wrap(super(JavaRNG, self).nextFloat())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def nextLong(self) -> int:
        """public long dev.ultreon.quantum.world.rng.JavaRNG.nextLong()"""
        return int.__wrap(super(JavaRNG, self).nextLong())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def randint(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.randint(int,int)"""
        return int.__wrap(super(__JavaRNG, self).randint(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def randrange(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.rng.JavaRNG.randrange(double,double)"""
        return float.__wrap(super(__JavaRNG, self).randrange(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setSeed(self, arg0: int):
        """public void dev.ultreon.quantum.world.rng.JavaRNG.setSeed(long)"""
        super(__JavaRNG, self).setSeed(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Random'):
        """public dev.ultreon.quantum.world.rng.JavaRNG(java.util.Random)"""
        val = __JavaRNG(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def randrange(self, arg0: float, arg1: float) -> float:
        """public float dev.ultreon.quantum.world.rng.JavaRNG.randrange(float,float)"""
        return float.__wrap(super(__JavaRNG, self).randrange(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def nextInt(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.nextInt(int,int)"""
        return int.__wrap(super(__JavaRNG, self).nextInt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def chance(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.world.rng.JavaRNG.chance(int)"""
        return bool.__wrap(super(__JavaRNG, self).chance(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.rng.JavaRNG()"""
        val = __JavaRNG()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def nextInt(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.nextInt(int)"""
        return int.__wrap(super(__JavaRNG, self).nextInt(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.rng.JavaRNG(long)"""
        val = __JavaRNG(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.world.rng.JavaRNG
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.world.rng.JavaRNG as __JavaRNG
__JavaRNG = __JavaRNG
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
import java.util.Random as Random
 
class JavaRNG():
    """dev.ultreon.quantum.world.rng.JavaRNG"""
 
    @staticmethod
    def __wrap(java_value: __JavaRNG) -> 'JavaRNG':
        return JavaRNG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JavaRNG):
        """
        Dynamic initializer for JavaRNG.
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
    def chance(self, arg0: float) -> bool:
        """public boolean dev.ultreon.quantum.world.rng.JavaRNG.chance(float)"""
        return bool.__wrap(super(__JavaRNG, self).chance(__float.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.rng.JavaRNG()"""
        val = __JavaRNG()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def nextFloat(self) -> float:
        """public float dev.ultreon.quantum.world.rng.JavaRNG.nextFloat()"""
        return float.__wrap(super(JavaRNG, self).nextFloat())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def nextLong(self) -> int:
        """public long dev.ultreon.quantum.world.rng.JavaRNG.nextLong()"""
        return int.__wrap(super(JavaRNG, self).nextLong())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def randint(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.randint(int,int)"""
        return int.__wrap(super(__JavaRNG, self).randint(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def randrange(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.rng.JavaRNG.randrange(double,double)"""
        return float.__wrap(super(__JavaRNG, self).randrange(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setSeed(self, arg0: int):
        """public void dev.ultreon.quantum.world.rng.JavaRNG.setSeed(long)"""
        super(__JavaRNG, self).setSeed(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Random'):
        """public dev.ultreon.quantum.world.rng.JavaRNG(java.util.Random)"""
        val = __JavaRNG(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def randrange(self, arg0: float, arg1: float) -> float:
        """public float dev.ultreon.quantum.world.rng.JavaRNG.randrange(float,float)"""
        return float.__wrap(super(__JavaRNG, self).randrange(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def nextInt(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.nextInt(int,int)"""
        return int.__wrap(super(__JavaRNG, self).nextInt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def chance(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.world.rng.JavaRNG.chance(int)"""
        return bool.__wrap(super(__JavaRNG, self).chance(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.world.rng.JavaRNG()"""
        val = __JavaRNG()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def nextInt(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.nextInt(int)"""
        return int.__wrap(super(__JavaRNG, self).nextInt(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.rng.JavaRNG(long)"""
        val = __JavaRNG(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.quantum.world.rng.JavaRNG 
 
 
# CLASS: dev.ultreon.quantum.world.rng.RNG
from abc import abstractmethod, ABC
import dev.ultreon.quantum.world.rng.RNG as __RNG
__RNG = __RNG
 
class RNG(ABC):
    """dev.ultreon.quantum.world.rng.RNG"""
 
    @staticmethod
    def __wrap(java_value: __RNG) -> 'RNG':
        return RNG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RNG):
        """
        Dynamic initializer for RNG.
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
        """public abstract long dev.ultreon.quantum.world.rng.RNG.nextLong()"""
        pass

    @abstractmethod
    def nextInt(self, arg0: int, arg1: int):
        """public abstract int dev.ultreon.quantum.world.rng.RNG.nextInt(int,int)"""
        pass

    @abstractmethod
    def randint(self, arg0: int, arg1: int):
        """public abstract int dev.ultreon.quantum.world.rng.RNG.randint(int,int)"""
        pass

    @abstractmethod
    def randrange(self, arg0: float, arg1: float):
        """public abstract float dev.ultreon.quantum.world.rng.RNG.randrange(float,float)"""
        pass

    @abstractmethod
    def randrange(self, arg0: float, arg1: float):
        """public abstract double dev.ultreon.quantum.world.rng.RNG.randrange(double,double)"""
        pass

    @abstractmethod
    def chance(self, arg0: int):
        """public abstract boolean dev.ultreon.quantum.world.rng.RNG.chance(int)"""
        pass

    @abstractmethod
    def nextInt(self, arg0: int):
        """public abstract int dev.ultreon.quantum.world.rng.RNG.nextInt(int)"""
        pass

    @abstractmethod
    def setSeed(self, arg0: int):
        """public abstract void dev.ultreon.quantum.world.rng.RNG.setSeed(long)"""
        pass

    @abstractmethod
    def nextFloat(self, ):
        """public abstract float dev.ultreon.quantum.world.rng.RNG.nextFloat()"""
        pass

    @abstractmethod
    def chance(self, arg0: float):
        """public abstract boolean dev.ultreon.quantum.world.rng.RNG.chance(float)"""
        pass