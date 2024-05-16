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
import java.lang.Float as _float
import dev.ultreon.quantum.world.rng.JavaRNG as _JavaRNG
_JavaRNG = _JavaRNG
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.Random as Random
 
class JavaRNG():
    """dev.ultreon.quantum.world.rng.JavaRNG"""
 
    @staticmethod
    def _wrap(java_value: _JavaRNG) -> 'JavaRNG':
        return JavaRNG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JavaRNG):
        """
        Dynamic initializer for JavaRNG.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JavaRNG__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JavaRNG__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def chance(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.world.rng.JavaRNG.chance(int)"""
        return bool._wrap(super(_JavaRNG, self).chance(_int.valueOf(arg0)))

    @overload
    def chance(self, arg0: float) -> bool:
        """public boolean dev.ultreon.quantum.world.rng.JavaRNG.chance(float)"""
        return bool._wrap(super(_JavaRNG, self).chance(_float.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.rng.JavaRNG()"""
        val = _JavaRNG()
        self.__wrapper = val

    @overload
    def randrange(self, arg0: float, arg1: float) -> float:
        """public float dev.ultreon.quantum.world.rng.JavaRNG.randrange(float,float)"""
        return float._wrap(super(_JavaRNG, self).randrange(_float.valueOf(arg0), _float.valueOf(arg1)))

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
    def randrange(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.rng.JavaRNG.randrange(double,double)"""
        return float._wrap(super(_JavaRNG, self).randrange(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def nextInt(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.nextInt(int,int)"""
        return int._wrap(super(_JavaRNG, self).nextInt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def randint(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.randint(int,int)"""
        return int._wrap(super(_JavaRNG, self).randint(_int.valueOf(arg0), _int.valueOf(arg1)))

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
        """public dev.ultreon.quantum.world.rng.JavaRNG()"""
        val = _JavaRNG()
        self.__wrapper = val

    @override
    @overload
    def nextLong(self) -> int:
        """public long dev.ultreon.quantum.world.rng.JavaRNG.nextLong()"""
        return int._wrap(super(JavaRNG, self).nextLong())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.rng.JavaRNG(long)"""
        val = _JavaRNG(_long.valueOf(arg0))
        self.__wrapper = val

    @overload
    def nextInt(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.nextInt(int)"""
        return int._wrap(super(_JavaRNG, self).nextInt(_int.valueOf(arg0)))

    @override
    @overload
    def nextFloat(self) -> float:
        """public float dev.ultreon.quantum.world.rng.JavaRNG.nextFloat()"""
        return float._wrap(super(JavaRNG, self).nextFloat())

    @overload
    def __init__(self, arg0: 'Random'):
        """public dev.ultreon.quantum.world.rng.JavaRNG(java.util.Random)"""
        val = _JavaRNG(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setSeed(self, arg0: int):
        """public void dev.ultreon.quantum.world.rng.JavaRNG.setSeed(long)"""
        super(_JavaRNG, self).setSeed(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.world.rng.JavaRNG
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
import java.lang.Float as _float
import dev.ultreon.quantum.world.rng.JavaRNG as _JavaRNG
_JavaRNG = _JavaRNG
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.Random as Random
 
class JavaRNG():
    """dev.ultreon.quantum.world.rng.JavaRNG"""
 
    @staticmethod
    def _wrap(java_value: _JavaRNG) -> 'JavaRNG':
        return JavaRNG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JavaRNG):
        """
        Dynamic initializer for JavaRNG.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JavaRNG__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JavaRNG__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def chance(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.world.rng.JavaRNG.chance(int)"""
        return bool._wrap(super(_JavaRNG, self).chance(_int.valueOf(arg0)))

    @overload
    def chance(self, arg0: float) -> bool:
        """public boolean dev.ultreon.quantum.world.rng.JavaRNG.chance(float)"""
        return bool._wrap(super(_JavaRNG, self).chance(_float.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.world.rng.JavaRNG()"""
        val = _JavaRNG()
        self.__wrapper = val

    @overload
    def randrange(self, arg0: float, arg1: float) -> float:
        """public float dev.ultreon.quantum.world.rng.JavaRNG.randrange(float,float)"""
        return float._wrap(super(_JavaRNG, self).randrange(_float.valueOf(arg0), _float.valueOf(arg1)))

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
    def randrange(self, arg0: float, arg1: float) -> float:
        """public double dev.ultreon.quantum.world.rng.JavaRNG.randrange(double,double)"""
        return float._wrap(super(_JavaRNG, self).randrange(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def nextInt(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.nextInt(int,int)"""
        return int._wrap(super(_JavaRNG, self).nextInt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def randint(self, arg0: int, arg1: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.randint(int,int)"""
        return int._wrap(super(_JavaRNG, self).randint(_int.valueOf(arg0), _int.valueOf(arg1)))

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
        """public dev.ultreon.quantum.world.rng.JavaRNG()"""
        val = _JavaRNG()
        self.__wrapper = val

    @override
    @overload
    def nextLong(self) -> int:
        """public long dev.ultreon.quantum.world.rng.JavaRNG.nextLong()"""
        return int._wrap(super(JavaRNG, self).nextLong())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.world.rng.JavaRNG(long)"""
        val = _JavaRNG(_long.valueOf(arg0))
        self.__wrapper = val

    @overload
    def nextInt(self, arg0: int) -> int:
        """public int dev.ultreon.quantum.world.rng.JavaRNG.nextInt(int)"""
        return int._wrap(super(_JavaRNG, self).nextInt(_int.valueOf(arg0)))

    @override
    @overload
    def nextFloat(self) -> float:
        """public float dev.ultreon.quantum.world.rng.JavaRNG.nextFloat()"""
        return float._wrap(super(JavaRNG, self).nextFloat())

    @overload
    def __init__(self, arg0: 'Random'):
        """public dev.ultreon.quantum.world.rng.JavaRNG(java.util.Random)"""
        val = _JavaRNG(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setSeed(self, arg0: int):
        """public void dev.ultreon.quantum.world.rng.JavaRNG.setSeed(long)"""
        super(_JavaRNG, self).setSeed(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.world.rng.JavaRNG 
 
 
# CLASS: dev.ultreon.quantum.world.rng.RNG
import dev.ultreon.quantum.world.rng.RNG as _RNG
_RNG = _RNG
from abc import abstractmethod, ABC
 
class RNG():
    """dev.ultreon.quantum.world.rng.RNG"""
 
    @staticmethod
    def _wrap(java_value: _RNG) -> 'RNG':
        return RNG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RNG):
        """
        Dynamic initializer for RNG.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RNG__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RNG__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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